#!/usr/bin/env python3
import json
import subprocess
import sys

# Example usage: python3 get_prefixes.py DNIC
if len(sys.argv) < 2:
    print("Usage: python get_prefixes.py <ORG_HANDLE>")
    sys.exit(1)

org_handle = sys.argv[1]
json_file = f"{org_handle}.json"
output_file = f"{org_handle}_prefixes.txt"

# Step 1: curl the RDAP JSON for the org handle
curl_cmd = ["curl", "-s", f"https://rdap.arin.net/registry/entity/{org_handle}"]
with open(json_file, "w") as f:
    subprocess.run(curl_cmd, stdout=f, check=True)

# Step 2: load the JSON
with open(json_file, "r") as f:
    data = json.load(f)

# Step 3: extract CIDR prefixes
networks = data.get("networks", [])
prefixes = []
for net in networks:
    for cidr_entry in net.get("cidr0_cidrs", []):
        prefix = cidr_entry.get("v4prefix") or cidr_entry.get("v6prefix")
        length = cidr_entry.get("length")
        if prefix and length is not None:
            prefixes.append(f"{prefix}/{length}")

# Step 4: write flat list to file
with open(output_file, "w") as f:
    for p in prefixes:
        f.write(f"{p}\n")

print(f"Saved {len(prefixes)} prefixes to {output_file}")
