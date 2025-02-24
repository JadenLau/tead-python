function p () {
    sleep $2
    clear
    /bin/echo -e "$1"
}

# Begin Video

p "e" 2
p "" 0

for i in {1..10}; do
    p "A........" .1
    p ".A......." .1
    p "..A......" .1
    p "...A....." .1
    p "....A...." .1
done