# This program prompts for a file name to read
# through the file and look for lines of the form,
# 'X-DSPAM-Confidence:' After finding the string, extract the
# spam confidence index and compute the average.

"""Make sure the file-path is correct and specified"""
path = '/home/ramani/Documents/Books/Python_for_Everybody_by_CharlesSeverance/'
ext = '.txt' # Creating a variable for the file extension gives more flexibility
fname = input("Enter filename: ")
try:
    fhand = open(path + fname + ext)
    count = 0
    spamConf = 0
    spamConf_total = 0
    spamConf_average = 0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:') is True:
            count = count + 1
            colonposition = line.find(':')
            spamConf = float(line[colonposition+1:])
            #spamConf_total = spamConf
            spamConf_total = spamConf_total + spamConf
    spamConf_average = spamConf_total/count
    print('Average spam confidence: ', spamConf_average)
except:
    print('File cannot be opened: ', fname)
    exit(1)
