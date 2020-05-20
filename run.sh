#!/bin/bash
f=${1:-doge.jpg}
[[ $f = - ]] && {
    f=$(mktemp /tmp/image.XXXXXX).jpg
    cat >$f
}
python3 main.py ${f} ${4:-g} ${5:-b} ${3:-300} ${2:--}
