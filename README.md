<h1> J.A.R.V.I.S- </h1>
 
J.A.R.V.I.S is an intelligent program which let you interact with your PC by talking to it. It has variuos feature in it that allow it to
do different task that its master asks for. Various functionalities of J.A.R.V.I.S are: <br />

1: Empty Recycle Bin <br />
2: Lock the home screen of your pc <br />
3: Answer mathematical queries and other general queries <br />
4: play a song when you are bored <br />
5: find you latest news from specified source, category or any topic <br />
6: Get you articles from wiki-pedia <br />
7: Search for books that you like or want to buy <br />
8: Allows you to search any video on youtube on voice command<br />
9: Shows you result of general query that you ask it on the browser <br/>
<br/>
More functionalities will be added soon.

<h2>Installation </h2>
<h3> In order to run J.A.R.V.I.S on your PC follow the following steps - </h3>
<ol>
  <li> Clone/Download the repository on your PC. </li>
  <li> You need to have python 3 or above installed on your PC if you don't have it than <a href="https://www.python.org/">Download Here</a> and make sure you have all the python packages and modules required to run J.A.R.V.I.S installed <strong>[use pip3 install -r requirements.txt].</strong>
  <ul>
    <li>speech_recognition</li>
    <li>ctypes</li>
    <li>nltk</li>
    <li>wikipedia</li>
    <li>requests</li>
  </ul>
  </li>
  <li>Change the file path according to your system in following files:</li>
  <ol>
    <li>jarvis.py change in os.chdir()</li>
    <li>book_api.py change in os.chdir()</li>
    <li>news_api.py change in os.chdir() and api_key"" <a href="https://newsapi.org/">get api key here</a></li>
    <li>open_app_feature.py in os.chdir() </li>
    <li>random_music_play_feature.py change in os.listdir('Music folder comes here')</li>
    <li>wikipedia_feature.py change in get_short_summary() method in os.chdir() </li>
    <li>wolframalpha_feature.py change the app_id <a href="https://www.wolframalpha.com/">get app id here</a></li>
  </ol>
  <li>Now run jarvis.py file and wait till it shows you "calibrating the noise level" message on python interactive shell. Speak your commands and query one at a time when it shows you "jarvis is listening..". </li>
  </ol>
    
<h3> If any issue arise do mention it in issues section <a href="https://github.com/hero-007/J.A.R.V.I.S---Intelligent-Personnel-Assistance/issues">here.</a></h3>
