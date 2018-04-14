set -o nounset
set -o errexit
set -o pipefail

wait_for() {
  # $1 hostname    $2 port
  n=0
  until [ $n -ge 15 ]; do
    nc -z -w 10 "$1" "$2" && break
    n=$(($n+1))
    echo "`date`: Waiting for $1:$2 to be available... n=$n"
    sleep 10
  done

  if [ $n -ge 15 ]; then
    echo "`date`: ERROR: Timeout out waiting for $1:$2."
    exit 1
  else
    echo "`date`: Dependency $1:$2 is online."
  fi
}

wait_for_url() {
  # parse the $1 (URL) to get the host/port of that system
  regex="http[s]?:\/\/(.*):(\d*).*"
  if [[ $1 =~ $regex ]]; then
    # wait for config-service to be reachable
    wait_for ${BASH_REMATCH[1]} ${BASH_REMATCH[2]}
  else
    echo "Unable to parse URL: $1"
    exit 1
  fi
}

wait_for_db() {
  until mysql -h $1 -P$2 -u$3 -p$4 cam -e "status"; 
  do echo waiting for mysql/mariadb.......; 
  sleep 2; 
  done;
}

# wait_for $DEPENDENCY_SERVICE_HOST $DEPENDENCY_SERVICE_PORT

/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
