from typing import Any, Optional

from .exceptions import FieldLookupError as FieldLookupError

def deprecate(msg: Any, level_modifier: int = ...) -> None: ...

class MigrationNotice(DeprecationWarning):
    url: str = ...
    def __init__(self, message: Any) -> None: ...

class RenameAttributesBase(type):
    renamed_attributes: Any = ...
    def __new__(metacls: Any, name: Any, bases: Any, attrs: Any): ...
    def get_name(metacls: Any, name: Any): ...
    def __getattr__(metacls: Any, name: Any): ...
    def __setattr__(metacls: Any, name: Any, value: Any): ...

def try_dbfield(fn: Any, field_class: Any): ...
def get_all_model_fields(model: Any): ...
def get_model_field(model: Any, field_name: Any): ...
def get_field_parts(model: Any, field_name: Any): ...
def resolve_field(model_field: Any, lookup_expr: Any): ...
def handle_timezone(value: Any, is_dst: Optional[Any] = ...): ...
def verbose_field_name(model: Any, field_name: Any): ...
def verbose_lookup_expr(lookup_expr: Any): ...
def label_for_filter(
    model: Any, field_name: Any, lookup_expr: Any, exclude: bool = ...
): ...
def translate_validation(error_dict: Any): ...
