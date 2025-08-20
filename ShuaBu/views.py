from django.shortcuts import render, HttpResponse
from ShuaBu.shuabu_form import ShuabuForm
from ShuaBu import models,shuabu
from django.core.exceptions import ValidationError
# Create your views here.


def add_log(request):
    """
    处理用户提交的表单数据,测试用
    """
    if request.method == "GET":
        form = ShuabuForm()
        return render(request, "shuabu_checkin.html", {"form": form})
    elif request.method == 'POST':
        form = ShuabuForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('password')
            print(data)

            models.DataLog.objects.create(**data)
            return HttpResponse(
                'ok'
            )
            # return render(request, "shuabu_checkin.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print('clean-errors', clean_errors)
            # 将带有错误信息的form对象返回前端页面
            return render(request, 'shuabu_checkin.html', {'form': form})
    return render(request, "shuabu_checkin.html", {"form": form, "clean_errors": clean_errors})
    

def main(request):
    """
    刷步主函数，正式
    """
    if request.method == "GET":
        form = ShuabuForm()
        return render(request, "shuabu_checkin.html", {"form": form})
    elif request.method == 'POST':
        form = ShuabuForm(request.POST)
        if form.is_valid():  # 进行数据有效性校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            print(data)
            # 执行刷步
            try:
                # 调用刷步函数
                mi_response = shuabu.entrance(data)
                print('mi_response', mi_response)
                data.pop('password')
                data.update({'result': mi_response})
                # 记录日志到数据库
                models.DataLog.objects.create(**data)
                if mi_response == "success":
                    # 成功的消息需要特殊处理一下
                    mi_response = {'msg': {"code": 1, "msg": "刷步成功"}}
                return render(request, "result.html", {"result_message": mi_response})
            except Exception as e:
                print('刷步失败', e)
                data.pop('password')
                data.update({'result': e})
                # 记录失败日志到数据库
                models.DataLog.objects.create(**data)
            # return HttpResponse(
            #     'ok'
            # )
            # return render(request, "shuabu_checkin.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print('clean-errors', clean_errors)
            # 将带有错误信息的form对象返回前端页面
            return render(request, 'shuabu_checkin.html', {'form': form, 'errors': clean_errors})
    form = ShuabuForm()
    return render(request, "shuabu_checkin.html", {"form": form})
