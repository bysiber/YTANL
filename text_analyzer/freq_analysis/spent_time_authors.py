from datetime import datetime

def format_time(time):
    time_parts = time.split(":")
    if len(time_parts) == 1:  # SS format
        time = "00:00:" + time.zfill(2)
    elif len(time_parts) == 2:  # MM:SS format
        time = "00:" + time
    elif len(time_parts) == 3 and len(time_parts[0]) == 1:  # H:MM:SS format
        time = time.zfill(8) # zfill yerine başka bir şey kullanalım !!!!!!!!
    return time

def calculate_time_difference(time1, time2):
    try:
        time1 = format_time(time1)
        time2 = format_time(time2)
        format = "%H:%M:%S"
        time1 = datetime.strptime(time1, format)
        time2 = datetime.strptime(time2, format)
        print(str(time2 - time1))
        return str(time2 - time1).replace("-", "")
    except:
        return "00:00:00"
    
def get_min_max_time(time1, time2):
    "returns min,max"
    try:
        _time1 = format_time(time1)
        _time2 = format_time(time2)
        format = "%H:%M:%S"
        _time1 = datetime.strptime(_time1, format)
        _time2 = datetime.strptime(_time2, format)
        if _time1 > _time2: 
            return time2, time1
        else: 
            return time1, time2
    except:
        return "00:00:00", "00:00:00"


def get_spent_time_authors(content):
    """
    content is a list of dict has 2 keys: author and timeStamp
    this function finds the min and max timeStamps for each author
    and calculates the difference between them
    """
    authors = {}
    for message in content:
        author = message["author"]
        timeStamp = message["timeStamp"]

        if author in authors:
            try:
                if timeStamp < authors[author]["min"]:
                    authors[author]["min"] = timeStamp
            except:
                pass

            try:
                if timeStamp > authors[author]["max"]:
                    authors[author]["max"] = timeStamp
            except:
                pass
        else:
            authors[author] = {"min": timeStamp, "max": timeStamp}

    for author in authors:
        min_time = authors[author]["min"]
        max_time = authors[author]["max"]
        min_time, max_time = get_min_max_time(min_time, max_time)
        authors[author]["spent_time"] = calculate_time_difference(min_time, max_time)

    return authors