# Supported third-party

sources for data sources

The following table lists the third-party sources that are automatically categorized
by CloudWatch Logs as data sources when ingested through pipelines:

| Data Source Name (@data_source_name field) | Data Source Type (@data_source_type field) |
| ------------------------------------------ | ------------------------------------------ |
| `crowdstrike_falcon`                       | `detection_finding`                        |
| `crowdstrike_falcon`                       | `process_activity`                         |
| `github_auditlogs`                         | `account_change`                           |
| `github_auditlogs`                         | `api_activity`                             |
| `github_auditlogs`                         | `entity_management`                        |
| `microsoft_entraid`                        | `account_change`                           |
| `microsoft_entraid`                        | `authentication`                           |
| `microsoft_entraid`                        | `entity_management`                        |
| `microsoft_entraid`                        | `user_access_management`                   |
| `microsoft_office365`                      | `account_change`                           |
| `microsoft_office365`                      | `application_lifecycle`                    |
| `microsoft_office365`                      | `authentication`                           |
| `microsoft_office365`                      | `compliance_finding`                       |
| `microsoft_office365`                      | `detection_finding`                        |
| `microsoft_office365`                      | `email_activity`                           |
| `microsoft_office365`                      | `file_hosting_activity`                    |
| `microsoft_office365`                      | `group_management`                         |
| `microsoft_office365`                      | `incident_finding`                         |
| `microsoft_office365`                      | `user_access_management`                   |
| `microsoft_office365`                      | `vulnerability_finding`                    |
| `microsoft_office365`                      | `web_resources_activity`                   |
| `microsoft_windows`                        | `account_change`                           |
| `microsoft_windows`                        | `authentication`                           |
| `microsoft_windows`                        | `entity_management`                        |
| `microsoft_windows`                        | `event_log_activity`                       |
| `microsoft_windows`                        | `file_system_activity`                     |
| `microsoft_windows`                        | `group_management`                         |
| `microsoft_windows`                        | `kernel_activity`                          |
| `okta_auth0`                               | `api_activity`                             |
| `okta_auth0`                               | `authentication`                           |
| `okta_sso`                                 | `api_activity`                             |
| `okta_sso`                                 | `authentication`                           |
| `okta_sso`                                 | `detection_finding`                        |
| `okta_sso`                                 | `entity_management`                        |
| `paloaltonetworks_nextgenerationfirewall`  | `authentication`                           |
| `paloaltonetworks_nextgenerationfirewall`  | `detection_finding`                        |
| `paloaltonetworks_nextgenerationfirewall`  | `network_activity`                         |
| `paloaltonetworks_nextgenerationfirewall`  | `process_activity`                         |
| `sentinelone_endpointsecurity`             | `dns_activity`                             |
| `sentinelone_endpointsecurity`             | `file_system_activity`                     |
| `sentinelone_endpointsecurity`             | `http_activity`                            |
| `sentinelone_endpointsecurity`             | `process_activity`                         |
| `servicenow_cmdb`                          | `api_activity`                             |
| `servicenow_cmdb`                          | `datastore_activity`                       |
| `servicenow_cmdb`                          | `entity_management`                        |
| `wiz_cnapp`                                | `api_activity`                             |
| `wiz_cnapp`                                | `authentication`                           |
| `wiz_cnapp`                                | `compliance_finding`                       |
| `wiz_cnapp`                                | `detection_finding`                        |
| `wiz_cnapp`                                | `vulnerability_finding`                    |
| `zscaler_internetaccess`                   | `authentication`                           |
| `zscaler_internetaccess`                   | `dns_activity`                             |
| `zscaler_internetaccess`                   | `http_activity`                            |
| `zscaler_internetaccess`                   | `network_activity`                         |
