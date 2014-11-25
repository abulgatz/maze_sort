This takes an image of a maze as input and solves it using BFS and DFS

# Notes

* Image must be in RGB, *not indexed* mode
* Maze must be surrounded by black border, or the solver will attempt to go off of the edge of the maze and you will get an index out of bounds error
* Start and end must be stated explicitly in (X,Y) coordinates. Top left of image is (0,0)

# Prerequisites

* Python 2
* Pillow python library

## Mac prerequisite installation

1. Install [Homebrew](http://brew.sh)

        $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    You may be asked to the install Xcode command line tools

2. Install python 2 (because we don't want to use system python)

        $ brew update
        $ brew upgrade
        $ brew install python

3. Install pillow python library

    **Easy way:**

        $ brew tap homebrew/python
        $ brew install pillow

    **Harder way:**

    Install pillow dependencies manually using homebrew, then install pillow using pip
    
        $ pip install pillow