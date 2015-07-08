import random
from models import Reader
from forms import NewReaderForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response, get_object_or_404

def IndexView(request):
    # Main page view. The view you see when you open the page
    args = {}
    args.update(csrf(request))
    args['curTitle'] = 'Top 25'
    args['successful'] = True
    if request.method == 'POST':
        form = NewReaderForm(request.POST, request.FILES)
        if form.is_valid():
            if str(form.cleaned_data['raw_file']).split('.')[-1] != 'txt':
                args['successful'] = False
                return render_to_response('readers/index.html', args)
            newFile = form.save()
            newFile.store_analyzed_data()
            return HttpResponseRedirect('/readers/' + str(newFile.id) + '/')
        else:
            args['successful'] = False
    return render_to_response('readers/index.html', args)

def AnalysisView(request, reader_id):
    #The view of analyzed objects
    args = {}
    args.update(csrf(request)) 
    curReader = get_object_or_404(Reader, pk=reader_id)
    if not curReader.analyzed_data:
        curReader.store_analyzed_data()
    display_condition = request.GET.get('display')
    if display_condition == 'all':
        args['common_list'] = curReader.get_analyzed_data()
        args['button_text'] = 'View top 25 words'
        args['next_click'] = ''
        args['b_color'] = ''
    else:
        args['common_list'] = curReader.get_analyzed_data()[:25]
        args['button_text'] = 'View all words'
        args['next_click'] = "?display=all"
        args['b_color'] = 'secondary'
        
    args['curTitle'] = curReader.get_short_name().split('.')[0]
    args['curReader'] = curReader
    return render(request, 'readers/analysis.html', args)

def ArchiveView(request):
    #Displays all previously uploaded files
    args = {}
    args.update(csrf(request))
    args['curTitle'] = 'Top 25 Archive'
    args['reader_list'] = Reader.objects.all()
    return render_to_response('readers/archive.html', args)
