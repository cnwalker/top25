import time, json
from django.db import models
from WordAnalyzer import WordCounter
from settings import MEDIA_ROOT, MEDIA_URL

def get_upload_file_name(instance, filename):
    #formats the file and gives it a unique name based on time to keep things consistent
    return "uploaded_files/%s_%s" % (str(time.time()).replace('.', '_'), filename)

class Reader(models.Model):
    #TextData object, which holds uploaded files and can return analyzer results
    raw_file = models.FileField(max_length=125, upload_to=get_upload_file_name)
    analyzed_data = models.TextField(null = True, blank = True)

    def __unicode__(self):
        return "".join("".join(self.raw_file.url.split('/')[-1]).split('_')[2:])
    
    def get_short_name(self):
        return "".join("".join(self.raw_file.url.split('/')[-1]).split('_')[2:])
    
    def get_most_common(self):
        return WordCounter.listify(WordCounter.analyzeStems(
            MEDIA_ROOT.replace(MEDIA_URL, '') + self.raw_file.url))

    def store_analyzed_data(self):
        self.analyzed_data = json.dumps(self.get_most_common())
        self.save()
        
    def get_analyzed_data(self):
        return json.loads(self.analyzed_data)
