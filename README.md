[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/BlitzKraft)
## NEW!! Guitar-hero like option `gtro` and `gtr`
![Default mode](./guitar.png?raw=true "No options given")
* `gtr` shows the strings and HJKL keys.
* `gtro` shows the strings with "O" for buttons
* Colors!!

### Just a little fun exercise for vim practice
* Runs within the terminal. Keeps score along the way.
* No install required!
* Test your reflexes!
* ... and accuracy 
* Keeps log of scores and accuracy.
* Now with windows support (testing required, \*nixers needn't panic, it's all the same for you)
* Default is unicode arrows. If your terminal doesn't support that, there are two other options you can try
* Try the other options anyway. They are fun too.

#### Dependencies
* getch - pypi package
* python3
* msvcrt (windows only)

#### Features
* Keeps score
* Logs score and accuracy
* Gets longest streak and logs it too!

### Screenshot
![Default mode](./screenshot.png?raw=true "No options given")

#### Usage
* Clone the repo
* `cd` to the directory
* `./game.py [ fallback | giant ] [ inf ]` optional args
* `./game.py help` to see the above line again
* Enjoy

#### Game modes
* `fallback`
    For terminals/emulators that don't support unicode but still one line per move
* `giant`
    Each arrow is four lines in height. Composed of slashes and backslashes.
* `inf`
    infinite game. 'q' to quit. Keeps track of score and accuracy ( percentage )

#### Todo
- [x] Use figlet/toilet for larger display (~~has known bug #1~~ fixed)
- [x] Fall back mode when unicode is not supported
- [x] Also track time along with score
- [x] Calculate speed
- [x] Accept command line options for fallback and giant mode
- [x] More forgiving, and show hearts to keep track of mistakes
- [x] Log score
- [x] Get longest streak
- [ ] Make it installable via pip.

#### Feel free to fork and give a star if you enjoy it! Thanks!!
