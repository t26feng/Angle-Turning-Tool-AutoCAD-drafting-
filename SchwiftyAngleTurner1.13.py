;; *************************************************************************************
;;  Created by: Tianyu Feng
;;  NER GEomatics Spring 2017
;;  Schwifty Angle Turn Tool + Conversion Tool
;;  #README
;;  For unit conversions, you can use basic math operaters in the input, such as
;;  +, -, *, / and the program WILL follow order of operations. For all processes,
;;  the key to evaluate your expressions will be by hitting RETURN on the SECOND
;;  input window of any row (fairly intuitive). Lastly, reminder that angle inputs
;;  are read in the following format: quadrant|degree.minutesecond where TWO
;;  decimal spaces are required for both minute and second.
;;  For example: '167.2150' is read as bearing North 67 degrees 21 minutes 50 seconds East.
;;  and '39.0200' is read as bearing South 3 degrees 2 minutes 0 seconds West. 
;; *************************************************************************************


from Tkinter import *

master = Tk()
master.wm_title("Tony's Schwifty Conversion/Angle Tool")

Label(master, text="Unit Conversion Tool:", 
      fg = 'red', anchor='center', height='2').grid\
    (row=0, column=0, columnspan=6, sticky=W, padx=15)

Label(master, text="Ft to M").grid(row=1, sticky=W, padx=2, pady=4)
Label(master, text="M to Ft").grid(row=2, sticky=W, padx=2, pady=4)

ft = Entry(master, width=18)
m = Entry(master, width=18)

ft.grid(row=1, column=1, padx=2)
m.grid(row=2, column=1, padx=2)

Label(master, text="ft").grid(row=1, column=2, sticky=W)
Label(master, text="m").grid(row=2, column=2, sticky=W)

Label(master, text="equals").grid(row=1, column=3, sticky=W)
Label(master, text="equals").grid(row=2, column=3, sticky=W)

ft_m = Text(master, height=1, width=15, padx=2)
m_ft = Text(master, height=1, width=15, padx=2)

ft_m.grid(row=1, column=4)
m_ft.grid(row=2, column=4)

Label(master, text="m").grid(row=1, column=5, sticky=W)
Label(master, text="ft").grid(row=2, column=5, sticky=W)

def convert_ft(event):
    ft_m.delete('1.0', END)
    feet = eval(ft.get())
    converted_m = str(round(float(feet) *  0.3048, 3))
    ft_m.insert(INSERT, converted_m)
master.bind_class(ft, '<Return>', convert_ft)

def convert_m(event):
    m_ft.delete('1.0', END)
    metres = eval(m.get())
    converted_ft = str(round(float(metres) * 3.28084, 2))
    m_ft.insert(INSERT, converted_ft)
master.bind_class(m, '<Return>', convert_m)



Label(master, text="Angle Turning Tool: Input Quadrant followed by Angle", 
      fg = 'red', anchor='center', height='1').grid\
    (row=4, column=0, columnspan=6, sticky=W, padx=15)


# Row 7 Input NE and NE
Label(master, text="Input Back Bearing:").grid(row=7, sticky=W, padx=4, pady=4)

bs_ne = Entry(master, width=18)    
bs_ne.grid(row=7, column=1, padx=5, pady=4)

Label(master, text="Input Forward Bearing:").grid(row=7, column=2, padx=2)
    
fs_ne = Entry(master, width=18)
fs_ne.grid(row=7, column=3, padx=5, pady=15)

Label(master, text="Turn Angle Clockwise By").grid(row=7, column=4, padx=2)

ans_ne = Text(master, height=1, width=12, padx=2)
ans_ne.grid(row=7, column=5, padx=2)




# dms addition and subtraction functions

# dms_add(dms1, dms2) produces the sum of two dms angles added together
    # dms_add: Str Str -> Str
    # requires: sum of angle can be no greater than 360 degree

def dms_add(dms1, dms2):
    # producing numbers from strings
    dms1_split = dms1.split('.')
    dms2_split = dms2.split('.')
    #print dms1_split
    #print '+'
    #print dms2_split
    # first angle
    degree1 = int(dms1_split[0])
    if len(dms1_split) == 1:
        minute1 = 0
        second1 = 0   
    elif len(dms1_split[1]) == 2:
        minute1 = int(dms1_split[1])
        second1 = 0
    else:
        m_s1 = dms1_split[1]
        minute1 = int(m_s1[:2])
        second1 = int(m_s1[2:])
    # second angle
    degree2 = int(dms2_split[0])
    if len(dms2_split) == 1:
        minute2 = 0
        second2 = 0   
    elif len(dms2_split[1]) == 2:
        minute2 = int(dms2_split[1])
        second2 = 0
    else:
        m_s2 = dms2_split[1]
        minute2 = int(m_s2[:2])
        second2 = int(m_s2[2:])
    # adding degrees
    degree_sum = degree1 + degree2
    # adding minutes
    minute_sum = minute1 + minute2
    if minute_sum >= 60:
        minute_sum -= 60
        degree_sum += 1
    # adding seconds
    second_sum = second1 + second2
    if second_sum >= 60:
        second_sum -= 60
        minute_sum += 1
        if minute_sum >= 60:
            minute_sum -= 60
            degree_sum += 1
    # reformatting back into string
    if minute_sum == 0:
        minute_string = '00'
    elif minute_sum < 10:
        minute_string = '0' + str(minute_sum)
    else:
        minute_string = str(minute_sum)
    if second_sum == 0:
        second_string = '00'
    elif second_sum < 10:
        second_string = '0' + str(minute_sum)
    else:
        second_string = str(second_sum)
    total_sum = str(degree_sum) + '.' + minute_string + second_string
    return total_sum

def dms_subtract(dms1, dms2):
    # producing numbers from strings
    dms1_split = dms1.split('.')
    dms2_split = dms2.split('.')
    #print dms1_split
    #print '-'
    #print dms2_split
    # first angle
    degree1 = int(dms1_split[0])
    if len(dms1_split) == 1:
        minute1 = 0
        second1 = 0   
    elif len(dms1_split[1]) == 2:
        minute1 = int(dms1_split[1])
        second1 = 0
    else:
        m_s1 = dms1_split[1]
        minute1 = int(m_s1[:2])
        second1 = int(m_s1[2:])
    # second angle
    degree2 = int(dms2_split[0])
    if len(dms2_split) == 1:
        minute2 = 0
        second2 = 0   
    elif len(dms2_split[1]) == 2:
        minute2 = int(dms2_split[1])
        second2 = 0
    else:
        m_s2 = dms2_split[1]
        minute2 = int(m_s2[:2])
        second2 = int(m_s2[2:])
    # subtracting degrees
    degree_diff = degree1 - degree2
    # sutracting minutes
    if minute2 > minute1:
        degree_diff -= 1
        minute1 += 60
    minute_diff = minute1 - minute2
    # subtracting seconds
    if second2 > second1:
        if minute_diff == 0:
            degree_diff -= 1
            minute_diff += 59
            second1 += 60
        minute_diff -= 1
        second1 += 60
    second_diff = second1 - second2
    # reformatting back into string
    if minute_diff == 0:
        minute_string = '00'
    elif minute_diff < 10:
        minute_string = '0' + str(minute_diff)
    else:
        minute_string = str(minute_diff)
    if second_diff == 0:
        second_string = '00'
    elif second_diff < 10:
        second_string = '0' + str(minute_diff)
    else:
        second_string = str(second_diff)
    total_diff = str(degree_diff) + '.' + minute_string + second_string
    return total_diff

# Angle and Azimuth Calculations
# ang_calc: Str Str -> Str

def ang_calc(bs, fs):
    # bs Azimuths
    bs_quad = int(bs[0])
    pure_bs = bs[1:]
    if bs_quad == 1:
        bs_azi = pure_bs
    elif bs_quad == 2:
        bs_azi = dms_subtract('180', pure_bs)
    elif bs_quad == 3:
        bs_azi = dms_add(pure_bs, '180')
    else:
        bs_azi = dms_subtract('360', pure_bs)
    # fs Azimuths
    fs_quad = int(fs[0])
    pure_fs = fs[1:]
    if fs_quad == 1:
        fs_azi = pure_fs
    elif fs_quad == 2:
        fs_azi = dms_subtract('180', pure_fs)
    elif fs_quad == 3:
        fs_azi = dms_add(pure_fs, '180')
    elif fs_quad == 4:
        fs_azi = dms_subtract('360', pure_fs)
    # calculate clockwise angle turn
    bs_num = int(bs_azi.replace('.', ''))
    fs_num = int(fs_azi.replace('.', ''))
    if bs_num < fs_num:
        print bs_azi
        print fs_azi
        clockwise_angle = dms_subtract(fs_azi, bs_azi)
    else:
        print bs_azi
        print fs_azi
        clockwise_angle = dms_add(dms_subtract('360', bs_azi), fs_azi)
    return clockwise_angle
    



# Angle Turn event function

def turn_ne(event):
    ans_ne.delete('1.0', END)
    bs = bs_ne.get()
    fs = fs_ne.get()
    result = ang_calc(bs, fs)
    ans_ne.insert(INSERT, result)
master.bind_class(fs_ne, '<Return>', turn_ne)



    
mainloop()
