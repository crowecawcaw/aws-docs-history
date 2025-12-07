# Source configuration for Palo Alto Networks Next-Generation Firewalls

## Integrating with Palo Alto Networks Next-Generation Firewalls

CloudWatch Pipeline integrates with Palo Alto Networks NGFW using the PAN-OS XML API to retrieve security, authentication, network activity, process activity, detection finding and threat activity. The PAN-OS XML API enables structured access, allowing the retrieval of System Logs, GlobalProtect, Traffic Logs, Threat Logs and URL Filtering Log.

## Authenticating with Palo Alto NGFW

To read network security logs, the pipeline needs to authenticate with your Palo Alto Networks NGFW login device interface. The plugin supports Basic Authentication.

- Create and Manage Users on a Palo Alto Networks NGFW Firewall via CLI
- Login firewall using with hostname using user admin and your password
- Store this username and password in a secret in AWS Secrets Manager under the keys `username` and `password`.
- Identify and note down your PAN-OS hostname.

Once configured, the pipeline can authenticate using the username and password and retrieve log activity from PAN-OS.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read logs from Palo Alto Networks NGFW, choose Palo Alto Networks Next-Generation Firewalls as the data source. Fill in the required information like `hostname`. Once you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and events that map to Authentication (3002), Network Activity (4001), Process Activity (1007), and Detection Finding (2004).

**Authentication** contains the following type and subtypes:

- GlobalProtect
  - data
  - file
  - flood
  - packet
  - scan
  - spyware
  - url
  - virus
  - vulnerability
  - wildfire
  - wildfire-virus

- System Logs
  - auth

**Network Activity** contains the following types and subtypes:

- Traffic Logs
  - start
  - end
  - drop
  - deny

- System Logs
  - vpn
  - url-filtering
  - app-cloud-engine
  - dhcp
  - ssh
  - dnsproxy
  - dns-security
  - wildfire
  - wildfire-appliance
  - ntpd
  - userid

[Show moreShow less](# "#")
**Process Activity** contains the following type and subtypes:

- System Logs
  - general
  - satd
  - ras
  - sslmgr
  - hw
  - iot
  - ctd-agent
  - routing
  - port
  - device-telemetry

**Detection Finding** contains the following type and subtypes:

- Threat Logs
  - data
  - file
  - flood
  - packet
  - scan
  - spyware
  - url
  - ml-virus
  - virus
  - vulnerability
  - wildfire
  - wildfire-virus

- URL Filtering Log

[Show moreShow less](# "#")
