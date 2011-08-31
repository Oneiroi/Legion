Legion
====================

Greetings Shephard Commander ...

About as geeky as you can get, yes I am making some serious mass effect references here, anyway the point of this is to leverage the power of python mutliprocessing lib, to provide grid / distributed computed.

Initial implementations will be very simple, such as large logfile processing, ongoing additions may well include other functionaities, render farm processing etc.

I intend to tie this into multiple nodes using the ARM processor from the project raspberrypi.org 


                             +------+
            +----------------> Geth |
            |                +------+
            |
            |                +------+
            +----------------> Geth |
     +------v                +------+
     |Legion+                +------+
     +------<+---------------> Geth |
             |               +------+
             |               +------+
             +---------------> Geth |
                             +------+

Each "Geth" is to reside on a single ARM platform, int he case where the hardware progresses each "Geth" could be modified to implement its own thraded pool of workers, Gethlings ... yeh SOMEONE was going to say it,
so ner I got there first.

As this is a project that I am working on from my own pocket and own time, (Amoungst everything else I have got going in my own time ...), all code will be based on Python 3.x, there is no intention to support older versions of python,
so do not ask


Changelog
---------

N/A still a w.i.p at this time, changelog will be updated with tag notes.

Support development
-------------------

N/A at this time, the best thing you can do is wait untill the project has matured past the first tag, then fork and contribute, better yet, grab an issue write the functioanlity and submit a pull request.

Copyright
---------

All code copyright David Busby <d.busby@saiweb.co.uk>, licensed under GPLv3, merges from pull requests will be credited where applicable.
All sound files copyright their respective owners, sound files are used purely for entertainment purposes only.


Credits
-------

Legion sound files: http://social.bioware.com/forum/1/topic/103/index/1718758


Contribute
----------

With an ever dwindling amount of free time to work on this project it is always appreciated there are workaround / hacks that other developers have made in order to get the required functioanlity.
As this project is GPL v3, please contribute to it your code changes as follows.

How
===
1. Fork it.
2. Create a branch (`git checkout -b my_markup`)
3. Commit your changes (`git commit -am "I made these changes 123"`)
4. Push to the branch (`git push origin my_markup`)
5. Create an [Issue][1] with a link to your branch

[1]: https://github.com/Oneiroi/Legion/issues

Rules
=====

1. 4 space tabbing, we are not using \t here!, if you are a vim junkie like me this is easy to get used to

Add the following to your .vimrc

set tabstop=4
set shiftwidth=4
set expandtab

