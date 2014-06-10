from django.shortcuts import render_to_response

def list(request):

  l = thingster.objects.all()

  return render_to_response('list.html', dictionary={'list':l})

def view(request, group):

  t = thingster.objects.get(Group=group)
  things = Thingy.objects.filter(group_name=t)

  return render_to_response('thingster.html', dictionary={'thingster':t, 'things': things})


