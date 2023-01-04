import os
import argparse
import xml.etree.ElementTree as ET


def process(data_dir, output_file_path):
    out_xml = None
    for f in sorted(os.listdir(data_dir)):
        file_path = os.path.join(data_dir, f)
        print(f"Reading {file_path} ...")
        this_xml = ET.parse(file_path)

        # store first xml as the output xml, which will eventually write to disk
        if out_xml is None:
            out_xml = this_xml
            # do not need to add to this one
            continue

        this_msg = this_xml.find("./BODY/IMPORTDATA/REQUESTDATA/Mapplemessage")
        print(this_msg)

        out_request_data = out_xml.find("./BODY/IMPORTDATA/REQUESTDATA")
        out_request_data.append(this_msg)


    print(f"Writing to {output_file_path} ...")
    out_xml.write(output_file_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge multiple xml files into one')
    parser.add_argument('-i', '--input_dir', default="xml-merge-sample",
                        metavar="INPUT_DIR", help='Path to input directory containing all xml files')
    parser.add_argument('-o', '--output_file', default="output.xml",
                        metavar="OUTPUT_FILE", help='Output file name')

    args = None

    try:
        args = parser.parse_args()
    except FileNotFoundError as ex:
        parser.error(ex)

    process(data_dir=args.input_dir, output_file_path=args.output_file)

