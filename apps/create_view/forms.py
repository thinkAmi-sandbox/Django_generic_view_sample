from django import forms
from .models import Purchase

class DetailForm(forms.ModelForm):

    class Meta:
        # フォームで使うModelを指定
        model = Purchase
        # フォームで使用するModelの列
        # 全部使用する場合は、`__all__`を指定する
        fields = "__all__"