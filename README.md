How to use?

```
$ python merge.py -h
usage: merge.py [-h] [-i INPUT_DIR] [-o OUTPUT_FILE]

Merge multiple xml files into one

options:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input_dir INPUT_DIR
                        Path to input directory containing all xml files
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name
```

Example:

```
$ python merge.py -i xml-merge-sample/ -o output.xml 
Reading xml-merge-sample/msg1.xml ...
Reading xml-merge-sample/msg2.xml ...
<Element 'Mapplemessage' at 0x7f1f2ba109a0>
Reading xml-merge-sample/msg3.xml ...
<Element 'Mapplemessage' at 0x7f1f2ba218a0>
Reading xml-merge-sample/msg4.xml ...
<Element 'Mapplemessage' at 0x7f1f2ba28fe0>
Writing to output.xml ...

```

Does it work for thousands of files?

First lets create large number of inputs:

```
$ mkdir large_inputs
$ for ((i=1;i<=10000;i++)); do cp -v xml-merge-sample/msg1.xml large_inputs/msg$i.xml; done
```

Now lets execute the script to merge all xml files:

```
$ python merge.py -i large_inputs/ -o large_output.xml
... SKIPPED OUTPUT ...
<Element 'Mapplemessage' at 0x7f62778580e0>
Reading large_inputs/msg9999.xml ...
<Element 'Mapplemessage' at 0x7f6277868720>
Writing to large_output.xml ...
tuxdna@valley:~/IdeaProjects/tally-xml
$ ls -lha large_output.xml 
-rw-rw-r-- 1 tuxdna tuxdna 80M Jan  4 19:39 large_output.xml

```
We can verify that 10000 entries are indeed there in output:

```
$ python -c 'import xml.etree.ElementTree as ET; print(len(ET.parse("large_output.xml").findall("./BODY/IMPORTDATA/REQUESTDATA/Mapplemessage")))'
10000
```

So it works for large data also.
