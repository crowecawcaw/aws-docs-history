# Cisco ISE integration configuration

Cisco Identity Services Engine (ISE) is the Cisco enterprise Network Access Control (NAC) and identity policy engine, providing AAA services (Authentication, Authorization, Accounting) using RADIUS and TACACS+ across wired, wireless, and VPN connections. ISE enforces who and what can connect to the network, under what conditions, and with what privileges, while providing rich session context including user identity, device type, posture, and location to other security tools.

Use this connector to collect Passed Authentications, Failed Attempts, Authentication Flow Diagnostics, Identity Store Diagnostics, Policy Diagnostics, RADIUS Accounting, Guest, and Administrative and Operational Audit events. Use CloudWatch pipelines to ingest Cisco ISE log data into CloudWatch Logs for scalable collection, processing, normalization, and integration with downstream AWS security and monitoring services.

###### Topics

- [Source configuration for Cisco ISE](cisco-ise-source-config.md "cisco-ise-source-config.md")
- [CloudWatch pipelines configuration for Cisco ISE](cisco-ise-pipeline-setup.md "cisco-ise-pipeline-setup.md")
