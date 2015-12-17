from django.views.generic import edit
from .forms import DetailForm

class RegisterView(edit.CreateView):
    # 使用するテンプレートを指定
    # <ディレクトリ名>/<ファイル名>
    template_name = "create_view/create_view.html"

    # フォームとして使用するフォームのクラスを指定
    form_class = DetailForm
