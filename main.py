import os
import datetime

#IMPORTANT README: websiteData.txt must contain each website and day on the same line
#for example if you need to visit https://example.org/ every 39 days, one line must be
# "https://example.org/@@39" without the quotation marks of course

#whenever you add a site to websiteData.txt also remember to add a line in last_visited.txt with the date of last visit

# define website URLs and their corresponding day frequency
#websitesList = ['https://example1.org', 'https://example2.org', 'https://example3.org']
#dayFrequency = [7, 14, 30]  # visit example1.org every 7 days, example2.org every 14 days, etc.

# initialize the two lists
import webbrowser

websitesList = []
dayFrequency = []

# open the file for reading
with open('websiteData.txt', 'r') as f:
    # read each line and split it into two parts
    for line in f:
        parts = line.strip().split('@@')
        # append the parts to the corresponding lists
        websitesList.append(parts[0])
        dayFrequency.append(int(parts[1]))

# check if last_visited.txt file exists
if os.path.isfile('last_visited.txt'):
    # read last visited dates from file
    with open('last_visited.txt', 'r') as f:
        lastVisited = [datetime.datetime.strptime(line.strip(), '%Y-%m-%d') for line in f]
else:
    # create last_visited.txt file and initialize all last visited dates to current date
    lastVisited = [datetime.datetime.today()] * len(websitesList)
    with open('last_visited.txt', 'w') as f:
        for date in lastVisited:
            f.write(date.strftime('%Y-%m-%d') + '\n')

# get today's date
today = datetime.datetime.today().date()

# check if it's time to visit each website
for i in range(len(websitesList)):
    if (today - lastVisited[i].date()).days >= dayFrequency[i]:
        print(f"It's time to visit {websitesList[i]}!")
        # Actually opening the page
        url = websitesList[i].strip()
        webbrowser.open(url)
        #
        # update lastVisited with today's date
        lastVisited[i] = datetime.datetime.today()
    else:
        numberOfDays = (today - lastVisited[i].date()).days
        print(str(numberOfDays) + " days has passed since last visited " + websitesList[i] + " on " + lastVisited[i].strftime('%Y-%m-%d'))
        daysNeededToOpenIt = str(dayFrequency[i] - numberOfDays)
        print(f"{websitesList[i]} will be opened in {daysNeededToOpenIt}")
        print()

# write updated lastVisited dates to file
with open('last_visited.txt', 'w') as f:
    for date in lastVisited:
        f.write(date.strftime('%Y-%m-%d') + '\n')

input("Press enter to exit")
