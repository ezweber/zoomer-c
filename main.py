import argparse
import os

parser = argparse.ArgumentParser(description="Convert Zoomer C to regular C and compile it.")
parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)

args = parser.parse_args()

words = {
"cheif": "int main",
"yeet": "return",
" rn": ";",
"no": "!",
"cap": "0",
"spittin": "printf"
        }

with open(args.input_file,'r') as file:
    filedata = file.read()

    for i in words:
        filedata = filedata.replace(i,words.get(i))

with open(args.output_file,'w') as file:
    file.write(filedata)

os.system(f"gcc {args.output_file}")