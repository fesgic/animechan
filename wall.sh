#!/bin/sh
$quote=`curl https://animechan.vercel.app/api/random`
if [ "$?" -eq 0 ]; then
	echo $quote
else
	echo "No internet Connection"
fi
