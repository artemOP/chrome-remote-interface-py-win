from typing import Optional, List, Dict, Union
from collections import OrderedDict

from .shared import FRefCollector, TYPER
from .property import Property
from .ptype import Type


Props = Optional[List[Property]]


class DomainType(FRefCollector):

    def __init__(self, domain: str, dt: dict) -> None:
        super().__init__()
        self.domain = domain
        self.id: str = dt["id"]
        # print(self.domain, self.id)
        self.scoped_name: str = f"{self.domain}.{self.id}"
        self.description: Optional[str] = dt.get("description", None)
        self.type: Type = Type(dt)
        self.experimental: bool = dt.get("experimental", False)
        self.properties: Props = self._build_props(dt.get("properties", None))
        self.items: Optional[List[Type]] = self._build_items(dt.get("items", None))
        TYPER.add_type(self.id, self.type)
        TYPER.add_type(self.scoped_name, self.type)

    @property
    def code_description(self) -> str:
        return " ".join(self.description.split("\n"))

    @property
    def is_array(self) -> bool:
        return self.type.is_array

    @property
    def is_object(self) -> bool:
        return self.type.is_object

    @property
    def has_properties(self):
        return self.properties is not None

    @property
    def properties_dict(self) -> Optional[Dict[str, Property]]:
        if not self.has_properties:
            return None
        pdict = OrderedDict()
        for prop in self.properties:
            pdict[prop.name] = prop
        return pdict

    @property
    def constructor_string(self) -> str:
        if self.type.is_object:
            if self.has_properties:
                optionals = []
                notoptional = []
                for prop in self.properties:
                    if prop.optional:
                        optionals.append(
                            prop.constructor_string.replace("'Any'", "Any")
                        )
                    else:
                        notoptional.append(
                            prop.constructor_string.replace("'Any'", "Any")
                        )
                return ", ".join(notoptional + optionals)
            else:
                print(self.scoped_name, "is array", self.items)
                return ""
        else:
            print(self.scoped_name, "is array", self.items)
            return ""

    def _build_props(self, props_list: Optional[List[dict]]) -> Props:
        if props_list is None:
            return props_list
        props = []
        for aprop in props_list:
            prop = Property(self.id, aprop)
            self._if_foreign_ref_add(prop)
            props.append(prop)
        return props

    def __str__(self) -> str:
        if self.type.is_array:
            return f"{self.id}[]"
        elif self.type.is_object:
            if self.has_properties:
                ps = (
                    "\n "
                    + "\n ".join([prop.tinfo_str for prop in self.properties])
                    + "\n"
                )
            else:
                ps = ""
            return f"{self.id}" + " {%s}" % ps
        else:
            return f"{self.id}<{self.type}>"

    def __repr__(self) -> str:
        return self.__str__()

    def _build_items(
        self, items: Optional[Union[List[dict], dict]]
    ) -> Optional[Union[List[Type], Type]]:
        if items is None:
            return items
        if isinstance(items, list):
            itms = []
            for it in items:
                itms.append(Type(it))
            return itms
        else:
            return Type(items)