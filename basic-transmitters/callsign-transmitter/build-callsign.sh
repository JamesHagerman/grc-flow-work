#!/bin/bash

# All of this amounts to:
# espeak -v en -m "<say-as interpret-as='characters'>A S 1 D F G</say-as><break strength='strong' />Software defined radio transmit test<break time='5s' />" -w callsign-plus-sdr-transmit-notice.wav

CALLSIGN=$1
MESSAGE="Software defined radio transmission test"
DELAY="5s"

if [[ -z "$CALLSIGN" ]]; then
    echo "No Callsign provided"
    CALLSIGN="Illegal station"
    callsignMarkup="$CALLSIGN"
else 
    echo "Callsign: $CALLSIGN"
    # split callsign upwith spaces:
    CALLSIGN=`echo $CALLSIGN | sed 's/./& /g'`
    # echo " Callsign with spaces: $CALLSIGN"
    callsignMarkup="<say-as interpret-as='characters'>$CALLSIGN</say-as>"
fi

echo "Message: $MESSAGE"
echo "Post message delay time: $DELAY"
echo

messageMarkup="<break strength='strong' />$MESSAGE"

if [[ -z "$DELAY" ]]; then
    echo "No delay provided..."
else
    delayMarkup="<break time='$DELAY' />"
fi

# The actual text we'll turn into speach:
completeMarkup="$callsignMarkup $messageMarkup $delayMarkup"

# The actual command used to do the Text-to-speach:
ESPEAKCMD="espeak -v en -m"

echo "Speaking the message..."
$ESPEAKCMD "$completeMarkup"

echo "Enter a filename without extension or spaces (ctrl-c to quit)"
read FILENAME

echo "Okay! Saving speach output to: $FILENAME.wav"
$ESPEAKCMD "$completeMarkup" -w "$FILENAME.wav"
