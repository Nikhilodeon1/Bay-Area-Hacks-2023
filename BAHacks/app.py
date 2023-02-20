from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, abort
import urllib.request

#import os.path
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/course69', methods=['POST'])
def course():
    course1 = request.form['ez']
    #linked-In==========================================================
    a = course1.replace(' ', '%20')
    with urllib.request.urlopen('https://www.linkedin.com/learning/search?keywords={}&sortBy=RELEVANCE&u=42751868'.format(a)) as response:
        html = response.read()
        char = bytes('<h3 class="base-search-card__title">', "UTF-8")
        b = html.split(char)
        #link===========================================================
        char2 = bytes('<a href="', "UTF-8")
        linklist = b[1].split(char2)
        char3 = bytes('" target="_self" data-tracking-control-name="learning-serp_learning-search-card_search-card" data-tracking-will-navigate class="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link" aria-label="Practice It: JavaScript Loops and Conditionals, 1h 56m, By: J. David Eisenberg, ">', "UTF-8")
        linklist2 = linklist[1].split(char3)
        char9 = bytes('<!---->', "UTF-8")
        link2 = linklist2[0].split(char9)
        link = link2[0]
        #name=============================================================
        char4 = bytes('</h3>', "UTF-8")
        sus = b[1].split(char4)
        char5 = bytes('            ', "UTF-8")
        name2 = sus[0].split(char5)
        name = name2[1]
        #duration==========================================================
        char6 = bytes('<!---->    </div>', "UTF-8")
        deez = b[1].split(char6)
        char7 = bytes('<div class="search-entity-media__duration">', "UTF-8")
        bru = deez[0].split(char7)
        char8 = bytes('        ', "UTF-8")
        g = bru[1].split(char8)
        duration = g[2]
        print(a + '.')
        jdsfghjklghfjkghlskdjfghlsjkdfds = 'Linked-In Learning'
    #coursera===============================================================
    e = 'https://www.coursera.org/search?query={}'.format(a)
    print(e)
    with urllib.request.urlopen('https://www.coursera.org/search?query={}'.format(a)) as response2:
        html2 = response2.read()
        if html2.interClass[a] == 'NA':
            abort
        else:
            link = html[course1]['span']
    #udemy==================================================================
    with urllib.request.urlopen('https://www.khanacademy.org/search?page_search_query={}'.format(a)) as response2:
        html2 = response2.read()
        print(html2)
    link = html[course1]['div']
    name2 = str(name)
    name3 = name2.removeprefix("b'")
    link2 = str(link).removeprefix("b'")
    durlist = str(duration).split('m')
    duration2 = durlist[0].removeprefix("b'")
    return render_template('course.html', duration=duration2, link=link2, name=name3, jdsfghjklghfjkghlskdjfghlsjkdfds=jdsfghjklghfjkghlskdjfghlsjkdfds, link=link)
