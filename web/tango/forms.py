
from wtforms.compat import text_type
from wtforms import SelectField
class SelectFieldPro(SelectField):
    def __init__(self, label=None, validators=None, coerce=text_type, choices=None, **kwargs):
        if callable(choices):
            choices = choices()
        super(SelectFieldPro, self).__init__(label, validators, coerce, choices, **kwargs)
