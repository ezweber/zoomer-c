import argparse
import os

parser = argparse.ArgumentParser(description="Convert Zoomer C to regular C and compile it.")
parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)
parser.add_argument('--encode',action='store_true')

args = parser.parse_args()

words_dict = {
"cheif": "int main",
"yeet": "return",
" rn": ";",
"no": "!",
"cap": "0",
"spittin": "printf",
"finna": "=",
"on god": "==",
"deadass": "continue",
"aint": "!=",
"fo": "for",
"cappin": "false",
"real": "true",
"peace": "break",
"homie": "include"
        }

keys = list(words_dict.keys())
values = list(words_dict.values())

try:
    with open(args.input_file,'r') as file:
        filedata = file.read()

        if args.encode:
            for i in values:
                position = values.index(i)
                filedata = filedata.replace(i,keys[position])
        else:
            for i in words:
                filedata = filedata.replace(i,words.get(i))


except FileNotFoundError:
    print(f"Shit is not bussin fr, {args.input_file} deadass gone.")
    quit()

with open(args.output_file,'w') as file:
    file.write(filedata)

if not args.encode:
    os.system(f"gcc {args.output_file}")