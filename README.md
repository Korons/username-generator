# username-generator
A simple username generator in python

## Usage 

```python username-generate.py -f FIRSTNAME -l LASTNAME```

Or to generate names that include NFSW words

``python username-generate.py -f FIRSTNAME -l LASTNAME -n yes```

Inorder to use the gui you will need to install [Gooey][gooey]

```pip install Gooey```

Will return a username based on your first and lastnames 

## Features 
 1. Names base on random verb and noun (happy_horse)
 2. l33t speak (h4ppy_h0rs3)
 3. Names are generated randomly meaning you shouldn't get the same name twice in a row
 4. NFSW names by passing the script -n yes
[gooey]: https://github.com/chriskiehl/Gooey
