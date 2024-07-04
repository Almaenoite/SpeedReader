#!/bin/bash

NAME="speedreader"

build() {
    docker build -t ${NAME} .
}

run() {
    docker run -it --rm --name ${NAME} ${NAME}
}

clean() {
    docker rmi ${NAME}
}

re() {
    clean
    build
}

# Déclaration des cibles comme des fonctions
case "$1" in
    clean)
        clean
        ;;
    re)
        re
        ;;
    *)
        build
        run
        ;;
esac

exit 0
