### Just a little fun exercise for vim practice
* Runs within the terminal. Keeps score along the way.
* Test your reflexes!
* Default is unicode arrows. If your terminal doesn't support that, there are two other options you can try
* Try the other options anyway. They are fun too.

#### Dependencies
* getch - pypi package
* python3
* unicode support in terminal(now optional)

#### Features
* Keeps score
* ~~Unforgiving - one mistake and game is over~~
* Three hearts. Can be easily reverted to old mode by changing the hearts to 1

### Screenshot
![Default mode](./screenshot.png?raw=true "No options given")

#### Usage
* Clone the repo
* `cd` to the directory
* `./game.py [ fallback | giant ]` optional args
* Enjoy

#### Todo
- [x] Use figlet/toilet for larger display (has known bug #1)
- [x] Fall back mode when unicode is not supported
- [x] Also track time along with score
- [x] Calculate speed
- [x] Accept command line options for fallback and giant mode
- [x] More forgiving, and show hearts to keep track of mistakes
- [ ] Show next arrow(?)

#### If you don't like unicode
- Set the fallback option to `True`
- Or the giant option

#### Feel free to fork and give a star if you enjoy it! Thanks!!
