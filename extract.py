#!/usr/bin/env python
import sqlite3
import os
import click

OUTPUT_DIR = "output"


def extract(filename):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = {}
    con = sqlite3.connect(filename)
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM webappsstore2 WHERE "scope" == "oi.tidekcats.:https:443"')
        rows = cur.fetchall()
        for row in rows:
            id, key, value, secure, owner = row
            if not key.startswith("file") or key == "file.list":
                continue
            key_type, file_id, key_name = key.split(".")
            if file_id not in files:
                files[file_id] = {}
            files[file_id][key_name] = value
    # from pprint import pprint
    # pprint(files)
    for id in files:
        f = files[id]
        filename = f['title'] + ".txt"
        import codecs
        fp = codecs.open(os.path.join(OUTPUT_DIR, filename), 'w', 'utf-8')
        fp.write(f['content'])
        fp.close()


@click.command()
@click.argument("filename")
def main(filename):
    extract(filename)

if __name__ == "__main__":
    main()
