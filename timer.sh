

function mins0 {
    for m in {0..9}; do
        secs
    done
}

for h in {0..23}; do
    for m in {3..59}; do
        for s in {0..59}; do
            clear
            echo "Clock $h:$m:$s"
            sleep 1
        done
    done
done