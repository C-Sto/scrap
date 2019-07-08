#!/usr/bin/env bash

if [ $# -lt 1 ]; then
    echo Usage: $0 url-file
    exit
fi
for url in `cat $1`; do
	curl -s -o /dev/null -I -m 1 -w "%{url_effective}\t%{http_code}\t%{redirect_url}\n" $url
done
