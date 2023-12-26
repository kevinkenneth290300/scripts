#!/bin/bash

echo "-------------------------------Service Status ------------------------------------------------------------"
services=("elasticsearch.service" "molochcapture.service" "kafka.service" "kibana.service" "zeek.service" "dispatcher-qa02.service" 
"appenricher.service"
"carbonblackingest.service"
"casemanager.service"
"ciscoampingest.service"
"classifier.service"
"crowdstrikeingest.service"
"cveinvestigator.service"
"deduper.service"
"domaininvestigator.service"
"emailer.service"
"eventscorer.service"
"fileinvestigator.service"
"firewallresponse.service"
"hosttracker.service"
"ipinvestigator.service"
"ja3hashinvestigator.service"
"logfinder.service"
"mistwatcher.service"
"networkinvestigator.service"
"oktalogsimport.service"
"packetserver.service"
"rapid7investigator.service"
"reporter.service"
"sentineloneingest.service"
"servicenowintegration.service"
"splunkwatcher.service"
"urlinvestigator.service"
"usertracker.service"
"windowsdefenderingest.service"
"suricata.service")

for service in "${services[@]}"; 
do
	sudo systemctl start $service 
	service_status=$(sudo systemctl is-active $service)
	echo $service
	echo $service_status
done