#!/bin/bash

# Define services and Elasticsearch indices
declare -a services=("elasticsearch.service" "molochcapture.service" "kafka.service" "kibana.service" "zeek.service" "dispatcher-qa02.service"
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

declare -a indices=("qa02-cases/_count"
"qa02-raw-events-*/_count"
"qa02-meta-logs-*/_count"
"qa02-ioas/_count"
"qa02-deduped-events-*/_count"
"qa02-basic-artifacts-*/_count"
"qa02-scored-events-*/_count"
"qa02-raw-logs-*/_count")

base_url="http://10.4.0.10:9200/"

# Function to get service status and uptime
get_service_info() {
    local service_name=$1
    local service_status=$(sudo systemctl is-active "$service_name")
    local service_uptime_raw=$(sudo systemctl show --property=ActiveEnterTimestamp --value "$service_name")
    local service_uptime=$(date -d "$service_uptime_raw" +'%Y-%m-%d %H:%M:%S')

    echo "Service: $service_name"
    echo "Status: $service_status"
    echo "Uptime: $service_uptime"
    echo "---------------------------"
    echo "---------------------------"
}

# Function to get Elasticsearch document counts
get_indices_info() {
    local index_url=$1
    local response=$(curl -s -X GET "$base_url$index_url")
    local count_value=$(echo "$response" | jq -r '.count')

    echo "$index_url"
    echo "Count: $count_value"
    echo "---------------------------"
    echo "---------------------------"
}

# Check service status and uptime
echo "------------------------------- Service Status -------------------------------------------------------------"
for service in "${services[@]}"; do
    get_service_info "$service"
done

# Check Elasticsearch document counts
echo "--------------------------------- Elastic Search Doc Counts---------------------------------------------------------"
for index in "${indices[@]}"; do
    get_indices_info "$index"
done
