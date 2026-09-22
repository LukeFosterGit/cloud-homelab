#!/bin/bash

SERVER="http://localhost"

echo "=== HOMElab Nginx Check ==="
echo "Checking $SERVER..."

if systemctl is-active --quiet nginx; then
	echo "Nginx service: RUNNING"

	HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$SERVER")

	if [ "$HTTP_CODE" -eq 200 ]; then
		echo "Website: HEALTHY"
		echo "HTTP status: $HTTP_CODE" 
		exit 0
	else
		echo "Website: ERROR"
		echo "HTTP status: $HTTP_CODE"
		exit 1
	fi

else 
	echo "Nginx service: NOT RUNNING"
	exit 1
fi
