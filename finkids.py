# %%


import pygame, sys
# import time
# from time import sleep
from pygame.locals import *
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


# pygame settings
pygame.init()
width = 800
height = 600
mainClock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Finance for Kids!")

# setting the start date and end dates
today = datetime.now()
start = today - timedelta(days=90)
endY = today.strftime("%Y")
endM = today.strftime("%m")
endD = today.strftime("%d")
startY = start.strftime("%Y")
startM = start.strftime("%m")
startD = start.strftime("%d")
startdate = str(startY)+"-"+str(startM)+"-"+str(startD)
enddate = str(endY)+"-"+str(endM)+"-"+str(endD)

# Apple (AAPL)
data = yf.download("AAPL", start=startdate, end=enddate, progress=False)
plt.figure(figsize=(4,3))
data['Adj Close'].plot(color='#fa027a').tick_params(axis='both', which='both', labelsize=6)
plt.title("Apple Stock Prices", fontsize=10)
plt.ylabel('Price($)', fontsize=8)
plt.legend()
# convert to matplotlib graph to image
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
# loading graph image
plot_image = pygame.image.load(buf)


# Alphabet (GOOG)
data2 = yf.download("GOOG", start=startdate, end=enddate, progress=False)
plt.figure(figsize=(4,3))
data2['Adj Close'].plot(color='#008f0e').tick_params(axis='both', which='both', labelsize=6)
plt.title("Alphabet Stock Prices", fontsize=10)
plt.ylabel('Price($)', fontsize=8)
plt.legend()
# convert to matplotlib graph to image
buf2 = io.BytesIO()
plt.savefig(buf2, format='png')
buf2.seek(0)
# loading graph image
plot_image2 = pygame.image.load(buf2)


# Walmart (WMT)
data3 = yf.download("WMT", start=startdate, end=enddate, progress=False)
plt.figure(figsize=(4,3))
data3['Adj Close'].plot(color='#05a8ff').tick_params(axis='both', which='both', labelsize=6)
plt.title("Walmart Stock Prices", fontsize=10)
plt.ylabel('Price($)', fontsize=8)
plt.legend()
# convert to matplotlib graph to image
buf3 = io.BytesIO()
plt.savefig(buf3, format='png')
buf3.seek(0)
# loading graph image
plot_image3 = pygame.image.load(buf3)



# Loading the background images in each page
bkgdpic = pygame.image.load("Main.png")
storepic = pygame.image.load("Store.png")
howpic = pygame.image.load("How.png")
playpic = pygame.image.load("Play.png")
matchingpic = pygame.image.load("Matching.png")
yahoopic = pygame.image.load("Yahoo.png")
yahoo1pic = pygame.image.load("Yahoo1.png")
yahoo2pic = pygame.image.load("Yahoo2.png")
yahoo3pic = pygame.image.load("Yahoo3.png")

# main screen buttons
playbtn = (340, 705, 160, 280)
storebtn = (340, 705, 320, 440)
howbtn = (162, 637, 470, 515)

# back button
backbtn = (80, 145, 80, 130)

# store buttons
teddybtn = (70, 205, 270, 515)
cookiesbtn = (255, 390, 270, 515)
puzzlebtn = (430, 570, 270, 515)
bookbtn = (590, 730, 270, 515)

# play games buttons
matchbtn = (120, 375, 315, 500)
yfinbtn = (425, 680, 315, 500)

w1b = (70, 190, 185, 215)
w2b = (70, 190, 230, 260)
w3b = (70, 190, 275, 305)
w4b = (70, 190, 320, 350)
w5b = (70, 190, 365, 395)
w6b = (70, 190, 410, 440)
w7b = (70, 190, 455, 485)
w8b = (70, 190, 500, 530)

d1b = (300, 720, 180, 220)
d2b = (300, 720, 225, 265)
d3b = (300, 720, 270, 310)
d4b = (300, 720, 315, 355)
d5b = (300, 720, 360, 400)
d6b = (300, 720, 405, 445)
d7b = (300, 720, 450, 490)
d8b = (300, 720, 495, 535)

w1p = (w1b[1], (w1b[2]+15))
w2p = (w2b[1], (w2b[2]+15))
w3p = (w3b[1], (w3b[2]+15))
w4p = (w4b[1], (w4b[2]+15))
w5p = (w5b[1], (w5b[2]+15))
w6p = (w6b[1], (w6b[2]+15))
w7p = (w7b[1], (w7b[2]+15))
w8p = (w8b[1], (w8b[2]+15))

d1p = (d1b[0], (d1b[2]+20))
d2p = (d2b[0], (d2b[2]+20))
d3p = (d3b[0], (d3b[2]+20))
d4p = (d4b[0], (d4b[2]+20))
d5p = (d5b[0], (d5b[2]+20))
d6p = (d6b[0], (d6b[2]+20))
d7p = (d7b[0], (d7b[2]+20))
d8p = (d8b[0], (d8b[2]+20))

words = [w1b, w2b, w3b, w4b, w5b, w6b, w7b, w8b]
defs = [d1b, d2b, d3b, d4b, d5b, d6b, d7b, d8b]
combos = [(w1p, d3p), (w2p, d6p), (w3p, d8p), (w4p, d2p), (w5p, d7p), (w6p, d5p), (w7p, d1p), (w8p, d4p)]

# Yahoo finance buttons
aaplbtn = (100, 280, 200, 250)
googbtn = (300, 480, 200, 250)
wmtbtn = (500, 680, 200, 250)

# coins
coins = 10
# lines in matching game
firstclick = False
secondclick = False
inside = False 
pair = []
lines = []

# function to check if mouse position is inside the button
def inbtn(btn, mx, my):
	if mx > btn[0] and mx < btn[1] and my > btn[2] and my < btn[3]:
		return True
	return False

# function to display coin text
def showcointext(x, y, size):
	global coins # to access coins in all functions
	text = pygame.font.Font("Fredoka-SemiBold.ttf", size).render(str(coins), True, (0,0,0))
	textrect = text.get_rect(center=(x, y))
	screen.blit(text, textrect)

# function to draw lines from word to definition in matching game
def drawline(wp, dp):
	global lines
	global coins
	pygame.draw.line(screen, (0, 0, 0), [wp[0], wp[1]], [dp[0], dp[1]], 3)

# function to check if word and definition are correct
def checkpairdraw(pair):
	global lines
	global coins
	w = pair[0]
	d = pair[1]
	wp = (w[1], (w[2]+((w[3]-w[2])//2)))
	dp = (d[0], (d[2]+((d[3]-d[2])//2)))
	wdpair = (wp, dp)
	for combo in combos:
		if wdpair == combo:
			lines.append(wdpair)
			coins += 5
			break

# function to keep track of correct word/def and draw the lines
def drawlines():
	global lines
	global coins	
	for line in lines:
		drawline(line[0], line[1])

# function to calculate the highest and lowest stock prices in the last 90 days
def stockcalc(ticker):
	global startdate
	global enddate
	data = yf.download(ticker, start=startdate, end=enddate, progress=False)
	pricehigh = str(round(data['Adj Close'].max(), 2))
	datehigh = str(data['Adj Close'].idxmax())[:10]

	pricelow = str(round(data['Adj Close'].min(), 2))
	datelow = str(data['Adj Close'].idxmin())[:10]

	return pricehigh, datehigh, pricelow, datelow

# function to display stock price and dates text
def stocktext(toppx, toppy, topdx, topdy, botpx, botpy, botdx, botdy, size, ticker):
	global coins # to access coins in all functions
	global startdate
	global enddate
	
	# set values for stock prices and dates
	hprice, hpricedate, lprice, lpricedate = stockcalc(ticker)
	
	# Highest
	hpricetext = pygame.font.Font("Fredoka-SemiBold.ttf", size).render(hprice, True, (0,0,0))
	hdatetext = pygame.font.Font("Fredoka-SemiBold.ttf", size).render(hpricedate, True, (0,0,0))
	
	# Lowest
	lpricetext = pygame.font.Font("Fredoka-SemiBold.ttf", size).render(lprice, True, (0,0,0))
	ldatetext = pygame.font.Font("Fredoka-SemiBold.ttf", size).render(lpricedate, True, (0,0,0))

	# Highest
	hpricetextrect = hpricetext.get_rect(center=(toppx, toppy))
	screen.blit(hpricetext, hpricetextrect)
	hdatetextrect = hdatetext.get_rect(center=(topdx, topdy))
	screen.blit(hdatetext, hdatetextrect)

	# Lowest
	lpricetextrect = lpricetext.get_rect(center=(botpx, botpy))
	screen.blit(lpricetext, lpricetextrect)
	ldatetextrect = ldatetext.get_rect(center=(botdx, botdy))
	screen.blit(ldatetext, ldatetextrect)


# function to display main menu screen
def menu():
	while True:
		global coins # to access coins in all functions
		# menu background pic
		screen.blit(bkgdpic, (0,0))
		# display # of coins
		showcointext(220, 400, 70)

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(playbtn, mx, my):
					play()
				if inbtn(storebtn, mx, my):
					store()
				if inbtn(howbtn, mx, my):
					how()

		pygame.display.update()

# function to display store screen
def store():
	while True:
		global coins # to access coins in all functions
		# Store background pic
		screen.blit(storepic, (0,0))
		# display # of coins
		showcointext(455, 190, 70)

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					menu()
				if inbtn(teddybtn, mx, my):
					if coins >= 50:
						coins -= 50
				if inbtn(cookiesbtn, mx, my):
					if coins >= 15:
						coins -= 15
				if inbtn(puzzlebtn, mx, my):
					if coins >= 45:
						coins -= 45
				if inbtn(bookbtn, mx, my):
					if coins >= 30:
						coins -= 30
				
		pygame.display.update()

# function to display play games screen
def play():
	while True:
		global coins # to access coins in all functions
		# play background pic
		screen.blit(playpic, (0,0))
		# display # of coins
		showcointext(455, 190, 70)

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					menu()
				if inbtn(matchbtn, mx, my):
					matching()
				if inbtn(yfinbtn, mx, my):
					yahoo()
				
		pygame.display.update()

# function to display matching game screen
def matching():
	while True:
		global coins # to access coins in all functions
		global firstclick
		global secondclick
		global pair
		global lines
		# matching background pic
		screen.blit(matchingpic, (0,0))
		# display # of coins
		showcointext(675, 110, 50)
		# make the lines to matching word and definition
		drawlines()

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					play()
				
				for word in words:
					if inbtn(word, mx, my):
						if len(pair) == 0:
							firstclick = True
							pair.append(word)
							break
						elif len(pair) == 1 and firstclick:
							pair.clear()
							pair.append(word)
							break
				for defbtn in defs:
					if inbtn(defbtn, mx, my):
						if len(pair) == 1 and firstclick:
							secondclick = True
							pair.append(defbtn)
							break
				if len(pair) == 2 and firstclick and secondclick:
					checkpairdraw(pair)
					pair.clear()
					firstclick = False
					secondclick = False
				
		pygame.display.update()

# function to display the Yahoo Finance screen
def yahoo():
	while True:
		global coins # to access coins in all functions

		# yahoo background pic
		screen.blit(yahoopic, (0,0))
		# display # of coins
		showcointext(675, 110, 50)

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					play()
				if inbtn(aaplbtn, mx, my):
					coins += 10
					yahooaapl()
				if inbtn(googbtn, mx, my):
					coins += 10
					yahoogoog()
				if inbtn(wmtbtn, mx, my):
					coins += 10
					yahoowmt()
	
		pygame.display.update()

# function to display the Yahoo Finance Apple screen
def yahooaapl():
	while True:
		global coins # to access coins in all functions

		# yahoo background pic
		screen.blit(yahoo1pic, (0,0))
		# AAPL graph draw on screen
		screen.blit(plot_image, (70, 270))
		# display # of coins
		showcointext(675, 110, 50)
		
		stocktext(630, 355, 650, 395, 630, 505, 650, 545, 25, "AAPL")

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					play()
				if inbtn(googbtn, mx, my):
					coins += 10
					yahoogoog()
				if inbtn(wmtbtn, mx, my):
					coins += 10
					yahoowmt()
	
		pygame.display.update()

# function to display the Yahoo Finance Alphabet screen
def yahoogoog():
	while True:
		global coins # to access coins in all functions

		# yahoo background pic
		screen.blit(yahoo2pic, (0,0))
		# AAPL graph draw on screen
		screen.blit(plot_image2, (70, 270))
		# display # of coins
		showcointext(675, 110, 50)
		
		stocktext(630, 355, 650, 395, 630, 505, 650, 545, 25, "GOOG")

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					play()
				if inbtn(aaplbtn, mx, my):
					coins += 10
					yahooaapl()
				if inbtn(wmtbtn, mx, my):
					coins += 10
					yahoowmt()
	
		pygame.display.update()

# function to display the Yahoo Finance Walmart screen
def yahoowmt():
	while True:
		global coins # to access coins in all functions

		# yahoo background pic
		screen.blit(yahoo3pic, (0,0))
		# AAPL graph draw on screen
		screen.blit(plot_image3, (70, 270))
		# display # of coins
		showcointext(675, 110, 50)
		
		stocktext(630, 355, 650, 395, 630, 505, 650, 545, 25, "WMT")

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					play()
				if inbtn(aaplbtn, mx, my):
					coins += 10
					yahooaapl()
				if inbtn(googbtn, mx, my):
					coins += 10
					yahoogoog()
	
		pygame.display.update()



# function to display the how to play screen
def how():
	while True:
		# how to play background pic
		screen.blit(howpic, (0,0))

		# get mouse coordinates using get_pos()
		mx, my = pygame.mouse.get_pos()

		# check for mouse events
		for event in pygame.event.get():
			# when x button is pressed, quit
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# check for when a button is pressed
			if event.type == MOUSEBUTTONDOWN:
				if inbtn(backbtn, mx, my):
					menu()
		
		pygame.display.update()

menu()




# %%
