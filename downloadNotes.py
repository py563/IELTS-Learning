import requests

def loopFileLinks(file_url, file_name):
     for x in range(1,27):
          file_url1 = file_url.format(x)
          print file_url1
          r = requests.get(file_url1, stream = True)
          if r.ok:
               file_name1 = file_name.format(x)
               print file_name1
               with open(file_name1,"wb") as pdf:
                   for chunk in r.iter_content(chunk_size=1024):                        
                        # writing one chunk at a time to pdf file
                        if chunk:
                            pdf.write(chunk)
               print x

def loopFileLinks3(file_url, file_name):
     for x in range(3001,3027):
          file_url1 = file_url.format(x)
          print file_url1
          r = requests.get(file_url1, stream = True)
          if r.ok:
               file_name1 = file_name.format(x) 
               with open(file_name1,"wb") as pdf:
                   for chunk in r.iter_content(chunk_size=1024):
                        # writing one chunk at a time to pdf file
                        if chunk:
                            pdf.write(chunk)
               print x

if(__name__ == "__main__"):
     #series 1
     series_file_name = 'IELTS_10{:02}_notes.pdf'
     series_file_url = 'http://tv.australiaplus.com/learn-english/series-1/oct-16/study-notes/ep{}_studynotes_topdf.pdf'
     loopFileLinks(series_file_url, series_file_name)
     series_activities_file_name = 'IELTS_10{:02}_activity.pdf'
     series_activities_file_url = 'http://tv.australiaplus.com/learn-english/series-1/oct-16/activity/ep{}_activitysheet1_topdf.pdf'
     loopFileLinks(series_activities_file_url, series_activities_file_name)
     #series 2
     series_file_name = 'IELTS_20{:02}_notes.pdf'
     series_file_url = 'http://tv.australiaplus.com/learn-english/series-2/nov-16/study-notes/se2ep{}_studynotes_topdf.pdf'
     loopFileLinks(series_file_url, series_file_name)
     series_activities_file_name = 'IELTS_20{:02}_activity.pdf'
     series_activities_file_url = 'http://tv.australiaplus.com/learn-english/series-2/nov-16/activity/series2_ep{}_activitysheet_topdf.pdf'
     loopFileLinks(series_activities_file_url, series_activities_file_name)
     #series 3
     series_file_name = 'IELTS_{}_notes.pdf'
     series_file_url = 'http://tv.australiaplus.com/learn-english/series-3/study-notes/s{}_notes.pdf'
     loopFileLinks3(series_file_url, series_file_name)
     series_activities_file_name = 'IELTS_{}_activity.pdf'
     series_activities_file_url = 'http://tv.australiaplus.com/learn-english/series-3/activity/s{}_activities.pdf'
     loopFileLinks3(series_activities_file_url, series_activities_file_name)
