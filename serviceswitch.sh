#!/bin/bash

echo "-------------------------------Service Status ------------------------------------------------------------"
services=("elasticsearch.service" "molochcapture.service" "kafka.service" "kibana.service" "zeek.service"
"suricata.service")

for service in "${services[@]}"; 
do
	sudo systemctl start $service 
	service_status=$(sudo systemctl is-active $service)
	echo $service
	echo $service_status
done
