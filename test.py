# pretty uwsgi->nginx passthrough example
# allows nginx to serve pure python applications through the uwsgi application

import random
# define all of our static variables
# this was generated using a list of hexadecimal color codes and sed regularexp
colors = ['FF0000', 'FF1600', 'FF2C00', 'FF4200', 'FF5800', 'FF6E00', 'FF8400', 'FF9A00', 'FFB000', 'FFC600', 'FFDC00', 'FFF200', 'FFff00', 'E9ff00', 'D3ff00', 'BDff00', 'A7ff00', '91ff00', '7Bff00', '65ff00', '4Fff00', '39ff00', '23ff00', '0Dff00', '00ff00', '00ff16', '00ff2C', '00ff42', '00ff58', '00ff6E', '00ff84', '00ff9A', '00ffB0', '00ffC6', '00ffDC', '00ffF2', '00ffff', '00F2ff', '00DCff', '00C6ff', '00B0ff', '009Aff', '0084ff', '006Eff', '0058ff', '0042ff', '002Cff', '0016ff', '0000ff', '0D00ff', '2300ff', '3900ff', '4F00ff', '6500ff', '7B00ff', '9100ff', 'A700ff', 'BD00ff', 'D300ff', 'E900ff', 'FF00ff', 'FF00F2', 'FF00DC', 'FF00C6', 'FF00B0', 'FF009A', 'FF0084', 'FF006E', 'FF0058', 'FF0042', 'FF002C', 'FF0016']
letters = ['W', 'E', 'L', 'C', 'O', 'M', '!']
newcolors = []

# iterate through each letter in the letters array, choosing a random color for each character
for x in letters:
	newcolors.append(random.choice(colors))

# create a dictionary out of our letters and randomly chosen colors
cmap = dict(zip(letters, newcolors))

# html code for font colors
sline = "<FONT COLOR=#"
eline = "</FONT>"
nline = eline + sline

# need to rewrite this, it's complete garbage at the moment but it works.
# calls each dictionary color mapping by letter
welcome = sline + cmap['W'] + ">W" + nline + cmap['E'] + ">E" + nline + cmap['L'] + ">L" + nline + cmap['C'] + ">C" + nline + cmap['O'] + ">O" + nline + cmap['M'] + ">M" + nline + cmap['E'] + ">E" + eline + ">!" + eline + " "
# let's display this using a random amount of times, just because we can!
table = welcome * random.randint(1, 512)

# here we act as the server, providing http calls/html to the client
def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return["<HTML>\n""<TITLE>IT WORKS</TITLE>\n" ' + "<H3><CENTER>\n" + table + "\n</H3></CENTER>\n""</HTML>"]

# this allows us to use uwsgi's touch-reload option, allowing us to generate new random html each time
import os
os.utime('test.py', None)
