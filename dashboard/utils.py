from dashboard.models.setting import Setting
def config(request):
    return {'config':Setting.objects.get()}