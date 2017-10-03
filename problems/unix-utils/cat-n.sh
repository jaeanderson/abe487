#!/bin/bash

IN_FILE=$1		#creates variable for input file as argument1
 
if [[ $# -ne 1 ]]; then					#check is number of arguments is not zero
        printf "Usage: %s file\n" "$(basename "$0")"	#outputs error message with format
        exit 1						#exits script with error message
fi


if [[ ! -f $IN_FILE ]]; then				#check if input file is a correct file
	echo "\"$IN_FILE\" is not a file"		#outputs error message if input file is not a correct file
	exit 1						#exits script with error message
fi

i=0						#initialize counter
while read -r FILELINE; do			#reads every line in given file
	let i++					#increments counter by 1	
	printf "%d %s\n" $i "$FILELINE"		#output line of file preceded by number line
done < "$IN_FILE"

