#!/bin/sh
#!/bin/bash
#Written by: Filipe Dezordi (https://dezordi.github.io/)
#At FioCruz/IAM - 29 Nov. 2020

input="$1"

while read linha;do

    line=$(echo $linha)
    fastq-dump -I --split-files $line
done < $input