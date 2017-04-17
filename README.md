# Introduction to Python Workshop at UH Manoa

**Instructor:** [Leonardo Uieda](http://www.leouieda.com)

**When**:
April 17, 19, and 20. 4:30pm - 6:30pm

**Where**:
Room 703 in the POST building. Department of Geology and Geophysics.

**What**:
We will teach a hands-on introduction to the [Python](https://www.python.org/)
programming language.
You **will not** fall asleep with PowerPoint slides full of code,
calculate Fibonacci numbers, organize lists of names, print
all odd numbers between 0 and 30, or any of that programmer nonsense.
You **will** write code from the start, work in pairs/groups, download data
from the internet, load data, perform linear regressions, make figures and
maps, and other things that you will actually need to do on a daily basis.

**Bring**:
Participants must bring their own **computers** (Mac, Windows, or Linux) with the
required **software already installed** (see [What to install](what-to-install)
below).
[Contact me](http://www.leouieda.com/contact/) if you need any help **before**
the workshop.


## Goals

This is going to be a hands-on workshop of the basic concepts you'll need to
use Python for your research and studies.
Participants who complete the workshop should be able to use Python to gather
data from one or more files, process the data, run an analysis, make
publication quality figures, and save the output.


## Schedule

| **Topics** |
|:-----------|
| **Day 1** |
| *Introductions* |
| First steps: Opening Python and running code |
| The Jupyter notebook |
| Using variables to store data |
| The power of libraries |
| Getting help |
| Loading data with numpy |
| **Day 2** |
| *Recap* |
| Computing with numpy arrays |
| Making plots with matplotlib |
| Repeating actions with `for` loops |
| Specifying conditions with `if` statements |
| Dealing with text |
| **Day 3** |
| *Recap* |
| Artisanal data input |
| Making functions for modular code and defensive programming |
| Analysing our data with `numpy` and `scipy` |
| Plotting results on a map |


## Shared class notes

We'll use Google Docs to edit shared class notes.
Please keep the document open during class.
You can post questions/comments/whatever on the notes or
on the group chat.

1. [Notes for day 1](https://docs.google.com/document/d/1cfmbCcUbqQZJHqEPifhVT5hC07r0LHNTwIlckaj5gRk/edit?usp=sharing)
2. [Notes for day 2](https://docs.google.com/document/d/1i1daJKs6qrqtVEjxLSGd69Atay2UYujTn2YXVB_-FjU/edit?usp=sharing)
3. [Notes for day 3](https://docs.google.com/document/d/1amWSLCPh1EkjpfAdaE3-TUus1Apdjr_d-oC3Z-eL93s/edit?usp=sharing)


## Data

Throughout the workshop, we will work with temperature data from
[Berkeley Earth](http://berkeleyearth.org/).

[![](http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Figures/global-land-TAVG-Trend.png)](http://berkeleyearth.lbl.gov/regions/global-land)

We'll start working with the time series of [average temperature in
Hawaii](http://berkeleyearth.lbl.gov/regions/hawaii) and try to reproduce the
figure from the website using Python tools.

Next, we will automatically download the temperature time series for a list of
countries, make plots, and run some analysis on the data.

The data files are available in the `data` folder just in case we have network
problems.
The files were downloaded using the script `download-data.py` which is what we
would write on day 2.


## What to install

There are many ways to get Python on your system and it can be very confusing
when you're first starting out.
I **don't** recommend downloading it from python.org or using the Python that
came with your system (common on Linux).
Instead, **use the Anaconda distribution**.
It will come with all the libraries you'll need and doesn't require
administrative access to install.

Go to https://www.continuum.io/downloads and select the **Python 3.6** version
of the installer for your system.
It's safe to use all the default configuration options when installing.

**Even if you already have Python** (say from your system package manager or
ArcGIS, etc), I recommend that you install Anaconda to avoid problems with
versioning.

You'll also need a **text editor**. If you don't already have one of your
choice, I recommend installing [Sublime Text](https://www.sublimetext.com/)
(it's available for Linux, Windows, and Mac).

**Please install all software BEFORE comming to the workshop.** If you have any
problems installing or don't know which version you need to download,
[come talk to me](http://www.leouieda.com/contact/).



## Recommended Literature

We will loosely follow the Python lessons from
[Software Carpentry](https://software-carpentry.org/).
I highly recommend taking a look at all of their material.
Everything there is worth learning.

See this blog post for more resources for getting started in Python:
http://www.leouieda.com/blog/getting-started-with-python-for-science.html

To perfect your Python-fu, I highly recommend trying to solve the
[Python Challenge](http://www.pythonchallenge.com/).
It's a fun way to learn general Python skills, like parsing text, downloading
web content, regular expressions, and much more.
The challenges are usually very difficult but also very rewarding when you can
complete them.


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This content is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
