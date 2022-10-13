#!/bin/bash

	
i=32
while [ $i -le 40 ]
do
    echo $i
    cd $i
    rm -v *k*
 cd ..
	i=$(( $i + 1 ))
done
