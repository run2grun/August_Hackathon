from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload_driver(request):
    upload_file = request.FILES['drive_file']
    ret = {}
    if upload_file:
        target_folder = settings.PULL_DRIVER_UPLOAD_PATH
        if not os.path.exists(target_folder): os.mkdir(target_folder)
        rtime = str(int(time.time()))
        filename = request.POST['filename']
        target = os.path.join(target_folder, filename)
        with open(target, 'wb+') as dest:
            for c in upload_file.chunks():
                dest.write(c)
        ret['file_remote_path'] = target
    else:
        return HttpResponse(status=500)
    return HttpResponse(json.dumps(ret), mimetype = "application/json")