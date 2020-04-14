import requests
import os

def loopFileLinks(file_url, file_name,series_no):
    if(series_no == 3):
        for x in range(3001,3027):
            file_url1 = file_url.format(x)
            print(file_url1)
            r = requests.get(file_url1, stream = True)
            file_name1 = file_name.format(x)
            if r.ok and not os.path.exists(file_name1):
                print(file_name1)
                with open(file_name1,"wb") as pdf:
                    for chunk in r.iter_content(chunk_size=1024):
                        # writing one chunk at a time to pdf file
                        if chunk:
                            pdf.write(chunk)
                print(x)
    else:
        for x in range(1,27):
            for url1 in file_url:
                file_url1 = url1.format(x)
                print(file_url1)
                r = requests.get(file_url1, stream = True)
                file_name1 = file_name.format(x)
                if r.ok and not os.path.exists(file_name1):
                    print(file_name1)
                    with open(file_name1,"wb") as pdf:
                        for chunk in r.iter_content(chunk_size=1024):
                            # writing one chunk at a time to pdf file
                            if chunk:
                                pdf.write(chunk)
                    print(x)
                    break

if(__name__ == "__main__"):
    #begin
    # creates a specific folder for the resource here ABC Learn English
    dir_path = os.path.join('notes/ABCLearnEnglishSeries')
    os.makedirs(dir_path,exist_ok=True)
    # notes are named based on the episode or activity number in the videos
    # series 1 
    series_file_name = os.path.join(dir_path,'IELTS_10{:02}_notes.pdf')
    series_file_url = [
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/study-notes/ep{}_studynotes_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/study-notes/ep{}_notes_v2.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/study-notes/NEWep{}_studynotes_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/study-notes/ep{}(old17)_studynotes_topdf.pdf'
        ]
    loopFileLinks(series_file_url, series_file_name , 1)
    # activity file names end with _activity similarly _notes for instructor notes
    series_activities_file_name = os.path.join(dir_path,'IELTS_10{:02}_activity.pdf')
    series_activities_file_url = [
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/activity/ep{}_activitysheet1_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/activity/ep{}_activitysheet_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/activity/NEWep{}_activitysheet_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/activity/ep{}(old17)_activitysheet_topdf.pdf'
        ]
    loopFileLinks(series_activities_file_url, series_activities_file_name,1)
    #series 2
    series_file_name = os.path.join(dir_path,'IELTS_20{:02}_notes.pdf')
    series_file_url = [
        'http://tv.australiaplus.com/learn-english/series-2/nov-16/study-notes/se2ep{}_studynotes_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/study-notes/ep{}_studynotes_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-2/nov-16/study-notes/se2_episode%20{}%20studynotes_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-2/nov-16/study-notes/se2_episode%20{}%20study%20notes%20to%20pdf.pdf'
        ]
    loopFileLinks(series_file_url, series_file_name,2)
    series_activities_file_name = os.path.join(dir_path,'IELTS_20{:02}_activity.pdf')
    series_activities_file_url = [
        'http://tv.australiaplus.com/learn-english/series-2/nov-16/activity/series2_ep{}_activitysheet_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-1/oct-16/activity/ep{}_activitysheet_topdf.pdf',
        'http://tv.australiaplus.com/learn-english/series-2/nov-16/activity/series2_ep%20{}_activitysheet_topdf.pdf'
        ]
    loopFileLinks(series_activities_file_url, series_activities_file_name,2)
    #series 3
    series_file_name = os.path.join(dir_path,'IELTS_{}_notes.pdf')
    series_file_url = 'http://tv.australiaplus.com/learn-english/series-3/study-notes/s{}_notes.pdf'
    loopFileLinks(series_file_url, series_file_name,3)
    series_activities_file_name = os.path.join(dir_path,'IELTS_{}_activity.pdf')
    series_activities_file_url = 'http://tv.australiaplus.com/learn-english/series-3/activity/s{}_activities.pdf'
    loopFileLinks(series_activities_file_url, series_activities_file_name,3)
    #end
