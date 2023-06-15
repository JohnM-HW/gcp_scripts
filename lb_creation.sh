#!/bin/bash

# Retrieve the list of load balancers
load_balancers=$(gcloud compute forwarding-rules list --format="table[no-heading](name,loadBalancingScheme,creationTimestamp)")

# Filter and print the creation dates of HTTP and HTTPS load balancers
echo "$load_balancers" | while IFS= read -r line; do
    scheme=$(echo "$line" | awk '{print $2}')
    if [[ "$scheme" == "EXTERNAL" ]]; then
        echo "$line"
    fi
done