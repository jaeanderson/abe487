#!/bin/bash


FILENAME=$1		#creates variable FILENAME as argument1
NUM_ARG=${2:-3}		#creates variable NUM_ARG as argument2 with default set to integer 3

if [[ $# -lt 1 ]] || [[ $# -gt 2 ]]; then			#checks input arguments is not zero and not greater than three
        printf "Usage: %s FILE [NUM]\n" "$(basename "$0")"	#outputs error message with format
        exit 1							#exits script with error message
fi

if [[ ! -f $FILENAME ]]; then					#checks given filename is a file
#        printf "%s %s\n" "\"$FILENAME\"" "is not a file"	#output error message
        echo "\"$FILENAME\" is not a file"
	exit 1							#exits script with error message
fi

i=0							#initialize counter
while read -r FILELINE; do				#reads every line in given file
        let i++						#increments counter by 1
	if [[ $i -gt $NUM_ARG ]]; then			#checks to see if counter is greater than given number of arguments
		break					#exits while loop if counter is greater than number of arguments
	else
		printf "%s\n" "$FILELINE"		#outputs number of file lines designated by given number of arguments
	fi
done < "$FILENAME"

