jikkann = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
juunishi = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
get_gessho = [1,0,11,10,9,8,7,6,5,4,3,2]


#year = 1986
#month = 10
#day = 23

def jikkann_year(year,month,day):
    remainder = year % 10
    if month == 1 or month == 2 and day <= 3:
        remainder -= 1

    if remainder <= 3:
        index = remainder + 6
        return index
    else:
        index = remainder - 4
        return index

def juunishi_year(year,month,day):
    remainder = year % 12
    if month == 1 or month == 2 and day <= 3:
        remainder -= 1

    if remainder <= 3:
        index = remainder + 8
        return index
    else:
        index = remainder - 4
        return index

def Julian_Day(year,month,day):
    if month == 1 or month == 2:
        year -= 1
        month += 12

    month -= 2
    julian_day = int(year * 365.25) + int(month * 30.59) + day -678927
    return julian_day

def jikkann_month(julian_day):
    julian_month = int(julian_day / 30.59)
    remainder = julian_month % 10
    if remainder <= 2:
        index = remainder + 7
        return index
    else:
        index = remainder - 3
        return index

def juunishi_month(julian_day):
    julian_month = int(julian_day / 30.59)
    remainder = julian_month % 12
    if remainder <= 4:
        index = remainder + 7
        return index
    else:
        index = remainder - 5
        return index

def gessho(sekki,month,day):
    if day < sekki:
        index = month - 1
        index2 = get_gessho[index]
        return index2
    elif day >= sekki and month != 12:
        index = month
        index2 = get_gessho[index]
        return index2
    elif day >= sekki and month == 12:
        index = month - 12
        index2 = get_gessho[index]
        return index2



def jikkann_day(julian_day):
    julian_day += 50
    index = julian_day % 10
    return index

def juunishi_day(julian_day):
    julian_day += 50
    index = julian_day % 12
    return index

def get_jikkann(index):
    return jikkann[index]

def get_juunishi(index):
    return juunishi[index]
