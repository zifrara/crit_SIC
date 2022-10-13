#!/bin/bash

	
i=75
while [ $i -le 100 ]
do
    echo $i
		gunzip *${i}*gz
		tar xvf circ${i}.* 
		mv -v circ${i}.* $i
    i=$(( $i + 1 ))
done
