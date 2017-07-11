#!/bin/bash
set -e

readonly ERRBIN="/app/venv/bin/errbot"
readonly ERRRUN="/srv"
readonly ERRCONFIG="${ERRRUN}/config.py"


is_set() {
    local var=$1

    [[ -n $var ]]
}

# if mounted volume is empty create dirs
if [ ! "$(ls -A ${ERRRUN})" ]; then
    mkdir "${ERRRUN}/data" "${ERRRUN}/plugins" "${ERRRUN}/errbackends"
fi


# copy default container image config file if not exist on volume
[ -f ${ERRCONFIG} ] || cp /app/config.py ${ERRRUN}


# sleep if we need to wait for another container
if ( is_set ${WAIT} ); then
    echo "Sleep ${WAIT} seconds before starting err..."
    sleep ${WAIT}
fi


exec ${ERRBIN} -c ${ERRCONFIG} $@