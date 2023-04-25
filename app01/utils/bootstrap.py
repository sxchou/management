from django import forms


class Bootstrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            if field.widget.attrs:
                if name == "oid":
                    field.widget.attrs['class'] = 'form-control'
                else:
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = name
            else:
                field.widget.attrs = {
                    'class': 'form-control',
                    'placeholder': name,
                }


class BootstrapModerForm(Bootstrap, forms.ModelForm):
    """使用类进行批量添加部件"""
    pass


class BootstrapForm(Bootstrap, forms.Form):
    """使用类进行批量添加部件"""
    pass
