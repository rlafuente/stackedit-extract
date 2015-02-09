This only works for Firefox!

[Stackedit](https://stackedit.io) is a fantastic text editor, with a minor annoyance: your text documents are not in your file system. This little script takes care of extracting the text files from Firefox's profile directory.


Installation
------------

The only dependency is `click`:

    pip install click


Running
-------

Just locate the `webappsstore.sqlite` which should be inside your Firefox profile. Then, run:

    python extract.py path/to/your/webappsstore.sqlite

All the contained Stackedit text documents will be extracted to the `output/` directory.
