# Supported third-party sources for data sources

The following table lists the third-party sources that are automatically categorized
by CloudWatch Logs as data sources when ingested through pipelines:

| Data Source Name (@data\_source\_name field) | Data Source Type (@data\_source\_type field) |
| -------------------------------------------- | -------------------------------------------- |
| `akamai_datastream_2`                        | `base_event`                                 |
| `akamai_datastream_2`                        | `dns_activity`                               |
| `akamai_datastream_2`                        | `http_activity`                              |
| `cisco_meraki`                               | `api_activity`                               |
| `cisco_meraki`                               | `detection_finding`                          |
| `cisco_meraki`                               | `network_activity`                           |
| `cisco_umbrella`                             | `data_security_finding`                      |
| `cisco_umbrella`                             | `dns_activity`                               |
| `cisco_umbrella`                             | `entity_management`                          |
| `cisco_umbrella`                             | `network_activity`                           |
| `crowdstrike_falcon`                         | `detection_finding`                          |
| `crowdstrike_falcon`                         | `process_activity`                           |
| `drupal_core`                                | `application_lifecycle`                      |
| `drupal_core`                                | `authentication`                             |
| `drupal_core`                                | `entity_management`                          |
| `drupal_core`                                | `http_activity`                              |
| `entrust_idaas`                              | `authentication`                             |
| `entrust_idaas`                              | `entity_management`                          |
| `f5_bigip`                                   | `http_activity`                              |
| `f5_bigip`                                   | `network_activity`                           |
| `github_auditlogs`                           | `account_change`                             |
| `github_auditlogs`                           | `api_activity`                               |
| `github_auditlogs`                           | `entity_management`                          |
| `microsoft_entraid`                          | `account_change`                             |
| `microsoft_entraid`                          | `authentication`                             |
| `microsoft_entraid`                          | `entity_management`                          |
| `microsoft_entraid`                          | `user_access_management`                     |
| `microsoft_office365`                        | `account_change`                             |
| `microsoft_office365`                        | `application_lifecycle`                      |
| `microsoft_office365`                        | `authentication`                             |
| `microsoft_office365`                        | `compliance_finding`                         |
| `microsoft_office365`                        | `detection_finding`                          |
| `microsoft_office365`                        | `email_activity`                             |
| `microsoft_office365`                        | `file_hosting_activity`                      |
| `microsoft_office365`                        | `group_management`                           |
| `microsoft_office365`                        | `incident_finding`                           |
| `microsoft_office365`                        | `user_access_management`                     |
| `microsoft_office365`                        | `vulnerability_finding`                      |
| `microsoft_office365`                        | `web_resources_activity`                     |
| `microsoft_windows`                          | `account_change`                             |
| `microsoft_windows`                          | `authentication`                             |
| `microsoft_windows`                          | `entity_management`                          |
| `microsoft_windows`                          | `event_log_activity`                         |
| `microsoft_windows`                          | `file_system_activity`                       |
| `microsoft_windows`                          | `group_management`                           |
| `microsoft_windows`                          | `kernel_activity`                            |
| `netskope_cloudexchange`                     | `account_change`                             |
| `netskope_cloudexchange`                     | `authentication`                             |
| `netskope_cloudexchange`                     | `data_security_finding`                      |
| `netskope_cloudexchange`                     | `detection_finding`                          |
| `netskope_cloudexchange`                     | `device_inventory_info`                      |
| `netskope_cloudexchange`                     | `entity_management`                          |
| `netskope_cloudexchange`                     | `file_hosting_activity`                      |
| `netskope_cloudexchange`                     | `network_activity`                           |
| `okta_auth0`                                 | `api_activity`                               |
| `okta_auth0`                                 | `authentication`                             |
| `okta_sso`                                   | `api_activity`                               |
| `okta_sso`                                   | `authentication`                             |
| `okta_sso`                                   | `detection_finding`                          |
| `okta_sso`                                   | `entity_management`                          |
| `onelogin_identity`                          | `account_change`                             |
| `onelogin_identity`                          | `authentication`                             |
| `onelogin_identity`                          | `entity_management`                          |
| `paloaltonetworks_nextgenerationfirewall`    | `authentication`                             |
| `paloaltonetworks_nextgenerationfirewall`    | `detection_finding`                          |
| `paloaltonetworks_nextgenerationfirewall`    | `network_activity`                           |
| `paloaltonetworks_nextgenerationfirewall`    | `process_activity`                           |
| `pingidentity_pingone`                       | `account_change`                             |
| `pingidentity_pingone`                       | `authentication`                             |
| `pingidentity_pingone`                       | `entity_management`                          |
| `sentinelone_endpointsecurity`               | `dns_activity`                               |
| `sentinelone_endpointsecurity`               | `file_system_activity`                       |
| `sentinelone_endpointsecurity`               | `http_activity`                              |
| `sentinelone_endpointsecurity`               | `process_activity`                           |
| `servicenow_cmdb`                            | `api_activity`                               |
| `servicenow_cmdb`                            | `datastore_activity`                         |
| `servicenow_cmdb`                            | `entity_management`                          |
| `slack_auditlog`                             | `account_change`                             |
| `slack_auditlog`                             | `authentication`                             |
| `slack_auditlog`                             | `detection_finding`                          |
| `slack_auditlog`                             | `entity_management`                          |
| `slack_auditlog`                             | `file_hosting_activity`                      |
| `slack_auditlog`                             | `user_access_management`                     |
| `slack_auditlog`                             | `web_resources_activity`                     |
| `tanium_endpointmanagement`                  | `account_change`                             |
| `tanium_endpointmanagement`                  | `authentication`                             |
| `tanium_endpointmanagement`                  | `compliance_finding`                         |
| `tanium_endpointmanagement`                  | `detection_finding`                          |
| `tanium_endpointmanagement`                  | `device_inventory_info`                      |
| `tanium_endpointmanagement`                  | `entity_management`                          |
| `tanium_endpointmanagement`                  | `group_management`                           |
| `tanium_endpointmanagement`                  | `vulnerability_finding`                      |
| `wiz_cnapp`                                  | `api_activity`                               |
| `wiz_cnapp`                                  | `authentication`                             |
| `wiz_cnapp`                                  | `compliance_finding`                         |
| `wiz_cnapp`                                  | `detection_finding`                          |
| `wiz_cnapp`                                  | `vulnerability_finding`                      |
| `zeek`                                       | `authentication`                             |
| `zeek`                                       | `base_event`                                 |
| `zeek`                                       | `detection_finding`                          |
| `zeek`                                       | `dhcp_activity`                              |
| `zeek`                                       | `dns_activity`                               |
| `zeek`                                       | `email_activity`                             |
| `zeek`                                       | `ftp_activity`                               |
| `zeek`                                       | `http_activity`                              |
| `zeek`                                       | `network_activity`                           |
| `zeek`                                       | `rdp_activity`                               |
| `zeek`                                       | `smb_activity`                               |
| `zeek`                                       | `software_inventory_info`                    |
| `zeek`                                       | `ssh_activity`                               |
| `zeek`                                       | `tunnel_activity`                            |
| `zscaler_internetaccess`                     | `authentication`                             |
| `zscaler_internetaccess`                     | `dns_activity`                               |
| `zscaler_internetaccess`                     | `http_activity`                              |
| `zscaler_internetaccess`                     | `network_activity`                           |

## Additional third-party sources via AWS Security Hub CSPM

Additional third-party security findings are available through AWS Security Hub
CSPM integration. The following partners send findings to Security Hub CSPM, which
are then available as data sources in CloudWatch Logs. For comprehensive details about these
integrations, see [Third-party product integrations with Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-partner-providers.md "../../../securityhub/latest/userguide/securityhub-partner-providers.md") in the
_AWS Security Hub User Guide_.

| Partner                                          | Integration                                       |
| ------------------------------------------------ | ------------------------------------------------- |
| 3CORESec – NTA                                   | Sends findings via Security Hub CSPM              |
| Alert Logic – SIEMless Threat Management         | Sends findings via Security Hub CSPM              |
| Aqua Security – Cloud Native Security Platform   | Sends findings via Security Hub CSPM              |
| Aqua Security – Kube-bench                       | Sends findings via Security Hub CSPM              |
| Armor – Armor Anywhere                           | Sends findings via Security Hub CSPM              |
| AttackIQ                                         | Sends findings via Security Hub CSPM              |
| Barracuda Networks – Cloud Security Guardian     | Sends findings via Security Hub CSPM              |
| BigID – BigID Enterprise                         | Sends findings via Security Hub CSPM              |
| Blue Hexagon                                     | Sends findings via Security Hub CSPM              |
| Check Point – CloudGuard IaaS                    | Sends findings via Security Hub CSPM              |
| Check Point – CloudGuard Posture Management      | Sends findings via Security Hub CSPM              |
| Claroty – xDome                                  | Sends findings via Security Hub CSPM              |
| Cloud Storage Security – Antivirus for Amazon S3 | Sends findings via Security Hub CSPM              |
| Contrast Security – Contrast Assess              | Sends findings via Security Hub CSPM              |
| CrowdStrike – CrowdStrike Falcon                 | Sends findings via Security Hub CSPM              |
| CyberArk – Privileged Threat Analytics           | Sends findings via Security Hub CSPM              |
| Data Theorem                                     | Sends findings via Security Hub CSPM              |
| Drata                                            | Sends findings via Security Hub CSPM              |
| Forcepoint – CASB                                | Sends findings via Security Hub CSPM              |
| Forcepoint – Cloud Security Gateway              | Sends findings via Security Hub CSPM              |
| Forcepoint – DLP                                 | Sends findings via Security Hub CSPM              |
| Forcepoint – NGFW                                | Sends findings via Security Hub CSPM              |
| Fugue                                            | Sends findings via Security Hub CSPM              |
| Guardicore – Centra                              | Sends findings via Security Hub CSPM              |
| HackerOne – Vulnerability Intelligence           | Sends findings via Security Hub CSPM              |
| JFrog – Xray                                     | Sends findings via Security Hub CSPM              |
| Juniper Networks – vSRX Next Generation Firewall | Sends findings via Security Hub CSPM              |
| k9 Security – Access Analyzer                    | Sends findings via Security Hub CSPM              |
| Lacework                                         | Sends findings via Security Hub CSPM              |
| McAfee – MVISION CNAPP                           | Sends findings via Security Hub CSPM              |
| NETSCOUT – Cyber Investigator                    | Sends findings via Security Hub CSPM              |
| Orca – Cloud Security Platform                   | Sends findings via Security Hub CSPM              |
| Palo Alto Networks – Prisma Cloud Compute        | Sends findings via Security Hub CSPM              |
| Palo Alto Networks – Prisma Cloud Enterprise     | Sends findings via Security Hub CSPM              |
| Plerion – Cloud Security Platform                | Sends findings via Security Hub CSPM              |
| Prowler                                          | Sends findings via Security Hub CSPM              |
| Qualys – Vulnerability Management                | Sends findings via Security Hub CSPM              |
| Rapid7 – InsightVM                               | Sends findings via Security Hub CSPM              |
| SentinelOne                                      | Sends findings via Security Hub CSPM              |
| Snyk                                             | Sends findings via Security Hub CSPM              |
| Sonrai Security – Sonrai Dig                     | Sends findings via Security Hub CSPM              |
| Sophos – Server Protection                       | Sends findings via Security Hub CSPM              |
| StackRox – Kubernetes Security                   | Sends findings via Security Hub CSPM              |
| Sumo Logic – Machine Data Analytics              | Sends findings via Security Hub CSPM              |
| Symantec – Cloud Workload Protection             | Sends findings via Security Hub CSPM              |
| Tenable.io                                       | Sends findings via Security Hub CSPM              |
| Trend Micro – Cloud One                          | Sends findings via Security Hub CSPM              |
| Vectra – Cognito Detect                          | Sends findings via Security Hub CSPM              |
| Wiz                                              | Sends findings via Security Hub CSPM              |
| Caveonix – Caveonix Cloud                        | Sends and receives findings via Security Hub CSPM |
| Cloud Custodian                                  | Sends and receives findings via Security Hub CSPM |
| DisruptOps                                       | Sends and receives findings via Security Hub CSPM |
| Kion                                             | Sends and receives findings via Security Hub CSPM |
| Turbot                                           | Sends and receives findings via Security Hub CSPM |

###### Note

This list reflects the Security Hub partner integrations that send
findings at the time of writing. Because AWS Security Hub regularly adds
new partner integrations, refer to [Third-party product integrations with Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-partner-providers.md "../../../securityhub/latest/userguide/securityhub-partner-providers.md") in the
_AWS Security Hub User Guide_ for the most
up-to-date list of available partners.
