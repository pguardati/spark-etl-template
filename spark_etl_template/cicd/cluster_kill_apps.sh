for x in $(yarn application -list | awk 'NR > 2 { print $1 }');
do yarn application -kill $x;
done