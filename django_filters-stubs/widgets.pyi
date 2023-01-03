from typing import Any, Dict, Optional, Tuple

from django import forms
from django.forms.renderers import BaseRenderer
from django.utils.safestring import SafeText

_OptAttrs = Dict[str, Any]

class LinkWidget(forms.Widget):
    choices: Any = ...
    def __init__(self, attrs: Optional[Any] = ..., choices: Any = ...) -> None: ...
    data: Any = ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def render( # type: ignore[override]
        self,
        name: str,
        value: Any,
        attrs: Optional[_OptAttrs] = ...,
        choices: Tuple = ...,
        renderer: Optional[BaseRenderer] = ...,
    ) -> SafeText: ...
    def render_options(self, choices: Any, selected_choices: Any, name: Any): ...
    def render_option(
        self, name: Any, selected_choices: Any, option_value: Any, option_label: Any
    ): ...
    def option_string(self): ...

class SuffixedMultiWidget(forms.MultiWidget):
    suffixes: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def suffixed(self, name: Any, suffix: Any): ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...
    def replace_name(self, output: Any, index: Any): ...
    def decompress(self, value: Any): ...

class RangeWidget(SuffixedMultiWidget):
    template_name: str = ...
    suffixes: Any = ...
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...
    def decompress(self, value: Any): ...

class DateRangeWidget(RangeWidget):
    suffixes: Any = ...

class LookupChoiceWidget(SuffixedMultiWidget):
    suffixes: Any = ...
    def decompress(self, value: Any): ...

class BooleanWidget(forms.Select):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...
    def render(
        self,
        name: Any,
        value: Any,
        attrs: Optional[Any] = ...,
        renderer: Optional[Any] = ...,
    ): ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...

class BaseCSVWidget(forms.Widget):
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def render(
        self,
        name: Any,
        value: Any,
        attrs: Optional[Any] = ...,
        renderer: Optional[Any] = ...,
    ): ...

class CSVWidget(BaseCSVWidget, forms.TextInput): ...

class QueryArrayWidget(BaseCSVWidget, forms.TextInput):
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
