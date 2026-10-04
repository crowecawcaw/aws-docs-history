

# Supported third-party sources for data sources
<a name="supported-third-party-sources-data-sources"></a>

The following table lists the third-party sources that are automatically categorized by CloudWatch Logs as data sources when ingested through pipelines:


| Data Source Name (@data\_source\_name field) | Data Source Type (@data\_source\_type field) | 
| --- | --- | 
| akamai\_datastream\_2 | base\_event | 
| akamai\_datastream\_2 | dns\_activity | 
| akamai\_datastream\_2 | http\_activity | 
| box | account\_change | 
| box | authentication | 
| box | detection\_finding | 
| box | entity\_management | 
| box | file\_hosting\_activity | 
| box | group\_management | 
| box | user\_inventory\_info | 
| broadcom\_carbonblack | authentication | 
| broadcom\_carbonblack | detection\_finding | 
| broadcom\_carbonblack | file\_system\_activity | 
| broadcom\_carbonblack | module\_activity | 
| broadcom\_carbonblack | network\_activity | 
| broadcom\_carbonblack | process\_activity | 
| broadcom\_carbonblack | registry\_key\_activity | 
| broadcom\_carbonblack | registry\_value\_activity | 
| broadcom\_carbonblack | script\_activity | 
| checkpoint\_nextgenerationfirewall | data\_security\_finding | 
| checkpoint\_nextgenerationfirewall | detection\_finding | 
| checkpoint\_nextgenerationfirewall | entity\_management | 
| checkpoint\_nextgenerationfirewall | network\_activity | 
| cisco\_duo | authentication | 
| cisco\_duo | base\_event | 
| cisco\_duo | device\_inventory\_info | 
| cisco\_duo | entity\_management | 
| cisco\_duo | user\_inventory\_info | 
| cisco\_ftd | authentication | 
| cisco\_ftd | authorize\_session | 
| cisco\_ftd | detection\_finding | 
| cisco\_ftd | network\_activity | 
| cisco\_ftd | tunnel\_activity | 
| cisco\_ise | account\_change | 
| cisco\_ise | api\_activity | 
| cisco\_ise | application\_error | 
| cisco\_ise | application\_lifecycle | 
| cisco\_ise | authentication | 
| cisco\_ise | entity\_management | 
| cisco\_ise | network\_activity | 
| cisco\_ise | tunnel\_activity | 
| cisco\_ise | web\_resources\_activity | 
| cisco\_meraki | api\_activity | 
| cisco\_meraki | detection\_finding | 
| cisco\_meraki | network\_activity | 
| cisco\_umbrella | data\_security\_finding | 
| cisco\_umbrella | dns\_activity | 
| cisco\_umbrella | entity\_management | 
| cisco\_umbrella | network\_activity | 
| crowdstrike\_falcon | detection\_finding | 
| crowdstrike\_falcon | process\_activity | 
| drupal\_core | application\_lifecycle | 
| drupal\_core | authentication | 
| drupal\_core | entity\_management | 
| drupal\_core | http\_activity | 
| entrust\_idaas | authentication | 
| entrust\_idaas | entity\_management | 
| f5\_bigip | http\_activity | 
| f5\_bigip | network\_activity | 
| github\_auditlogs | account\_change | 
| github\_auditlogs | api\_activity | 
| github\_auditlogs | entity\_management | 
| gitlab | group\_management | 
| gitlab | software\_inventory\_info | 
| gitlab | user\_inventory\_info | 
| gitlab | vulnerability\_finding | 
| gitlab | web\_resources\_activity | 
| google\_workspace | account\_change | 
| google\_workspace | api\_activity | 
| google\_workspace | authentication | 
| google\_workspace | base\_event | 
| google\_workspace | data\_security\_finding | 
| google\_workspace | detection\_finding | 
| google\_workspace | email\_activity | 
| google\_workspace | entity\_management | 
| google\_workspace | file\_hosting\_activity | 
| google\_workspace | user\_access\_management | 
| google\_workspace | web\_resources\_activity | 
| hashicorp\_vault | api\_activity | 
| jamf\_pro | authentication | 
| jamf\_pro | device\_inventory\_info | 
| jamf\_pro | entity\_management | 
| jamf\_protect | detection\_finding | 
| jamf\_protect | device\_inventory\_info | 
| jamf\_protect | dns\_activity | 
| jamf\_protect | software\_inventory\_info | 
| jamf\_protect | vulnerability\_finding | 
| jumpcloud | account\_change | 
| jumpcloud | authentication | 
| jumpcloud | datastore\_activity | 
| jumpcloud | detection\_finding | 
| jumpcloud | entity\_management | 
| microsoft\_entraid | account\_change | 
| microsoft\_entraid | authentication | 
| microsoft\_entraid | entity\_management | 
| microsoft\_entraid | user\_access\_management | 
| microsoft\_office365 | account\_change | 
| microsoft\_office365 | application\_lifecycle | 
| microsoft\_office365 | authentication | 
| microsoft\_office365 | compliance\_finding | 
| microsoft\_office365 | detection\_finding | 
| microsoft\_office365 | email\_activity | 
| microsoft\_office365 | file\_hosting\_activity | 
| microsoft\_office365 | group\_management | 
| microsoft\_office365 | incident\_finding | 
| microsoft\_office365 | user\_access\_management | 
| microsoft\_office365 | vulnerability\_finding | 
| microsoft\_office365 | web\_resources\_activity | 
| microsoft\_windows | account\_change | 
| microsoft\_windows | authentication | 
| microsoft\_windows | entity\_management | 
| microsoft\_windows | event\_log\_activity | 
| microsoft\_windows | file\_system\_activity | 
| microsoft\_windows | group\_management | 
| microsoft\_windows | kernel\_activity | 
| netskope\_cloudexchange | account\_change | 
| netskope\_cloudexchange | authentication | 
| netskope\_cloudexchange | data\_security\_finding | 
| netskope\_cloudexchange | detection\_finding | 
| netskope\_cloudexchange | device\_inventory\_info | 
| netskope\_cloudexchange | entity\_management | 
| netskope\_cloudexchange | file\_hosting\_activity | 
| netskope\_cloudexchange | network\_activity | 
| okta\_auth0 | api\_activity | 
| okta\_auth0 | authentication | 
| okta\_sso | api\_activity | 
| okta\_sso | authentication | 
| okta\_sso | detection\_finding | 
| okta\_sso | entity\_management | 
| onelogin\_identity | account\_change | 
| onelogin\_identity | authentication | 
| onelogin\_identity | entity\_management | 
| paloaltonetworks\_nextgenerationfirewall | authentication | 
| paloaltonetworks\_nextgenerationfirewall | detection\_finding | 
| paloaltonetworks\_nextgenerationfirewall | network\_activity | 
| paloaltonetworks\_nextgenerationfirewall | process\_activity | 
| paloaltonetworks\_prismacloud | base\_event | 
| paloaltonetworks\_prismacloud | cloud\_resources\_inventory\_info | 
| paloaltonetworks\_prismacloud | compliance\_finding | 
| paloaltonetworks\_prismacloud | detection\_finding | 
| paloaltonetworks\_prismacloud | device\_inventory\_info | 
| paloaltonetworks\_prismacloud | entity\_management | 
| paloaltonetworks\_prismacloud | scan\_activity | 
| paloaltonetworks\_prismacloud | vulnerability\_finding | 
| pingidentity\_pingaccess | api\_activity | 
| pingidentity\_pingaccess | http\_activity | 
| pingidentity\_pingfederate | authentication | 
| pingidentity\_pingfederate | entity\_management | 
| pingidentity\_pingone | account\_change | 
| pingidentity\_pingone | authentication | 
| pingidentity\_pingone | entity\_management | 
| proofpoint\_tap | detection\_finding | 
| proofpoint\_tap | email\_activity | 
| proofpoint\_tap | osint\_inventory\_info | 
| qualys\_csam | device\_inventory\_info | 
| qualys\_csam | osint\_inventory\_info | 
| qualys\_csam | software\_inventory\_info | 
| qualys\_csam | vulnerability\_finding | 
| qualys\_policyaudit | compliance\_finding | 
| qualys\_vmdr | account\_change | 
| qualys\_vmdr | api\_activity | 
| qualys\_vmdr | authentication | 
| qualys\_vmdr | device\_inventory\_info | 
| qualys\_vmdr | entity\_management | 
| qualys\_vmdr | vulnerability\_finding | 
| sailpoint\_isc | account\_change | 
| sailpoint\_isc | authentication | 
| sailpoint\_isc | entity\_management | 
| sailpoint\_isc | user\_access\_management | 
| salesforce\_elf | account\_change | 
| salesforce\_elf | api\_activity | 
| salesforce\_elf | authentication | 
| salesforce\_elf | datastore\_activity | 
| salesforce\_elf | detection\_finding | 
| salesforce\_elf | entity\_management | 
| salesforce\_elf | file\_hosting\_activity | 
| salesforce\_elf | http\_activity | 
| salesforce\_rtem | api\_activity | 
| salesforce\_rtem | authentication | 
| salesforce\_rtem | datastore\_activity | 
| salesforce\_rtem | file\_hosting\_activity | 
| sentinelone\_endpointsecurity | dns\_activity | 
| sentinelone\_endpointsecurity | file\_system\_activity | 
| sentinelone\_endpointsecurity | http\_activity | 
| sentinelone\_endpointsecurity | process\_activity | 
| servicenow\_cmdb | api\_activity | 
| servicenow\_cmdb | datastore\_activity | 
| servicenow\_cmdb | entity\_management | 
| slack\_auditlogs | account\_change | 
| slack\_auditlogs | authentication | 
| slack\_auditlogs | detection\_finding | 
| slack\_auditlogs | entity\_management | 
| slack\_auditlogs | file\_hosting\_activity | 
| slack\_auditlogs | user\_access\_management | 
| slack\_auditlogs | web\_resources\_activity | 
| snowflake\_platform | authentication | 
| snowflake\_platform | datastore\_activity | 
| snowflake\_platform | entity\_management | 
| snowflake\_platform | group\_management | 
| snowflake\_platform | user\_access\_management | 
| snowflake\_platform | user\_inventory\_info | 
| tanium\_endpointmanagement | account\_change | 
| tanium\_endpointmanagement | authentication | 
| tanium\_endpointmanagement | compliance\_finding | 
| tanium\_endpointmanagement | detection\_finding | 
| tanium\_endpointmanagement | device\_inventory\_info | 
| tanium\_endpointmanagement | entity\_management | 
| tanium\_endpointmanagement | group\_management | 
| tanium\_endpointmanagement | vulnerability\_finding | 
| tenable\_vulnerabilitymanagement | account\_change | 
| tenable\_vulnerabilitymanagement | api\_activity | 
| tenable\_vulnerabilitymanagement | authentication | 
| tenable\_vulnerabilitymanagement | compliance\_finding | 
| tenable\_vulnerabilitymanagement | device\_inventory\_info | 
| tenable\_vulnerabilitymanagement | scan\_activity | 
| tenable\_vulnerabilitymanagement | vulnerability\_finding | 
| wazuh\_platform | api\_activity | 
| wazuh\_platform | application\_lifecycle | 
| wazuh\_platform | authentication | 
| wazuh\_platform | compliance\_finding | 
| wazuh\_platform | detection\_finding | 
| wazuh\_platform | device\_inventory\_info | 
| wazuh\_platform | file\_system\_activity | 
| wazuh\_platform | remediation\_activity | 
| wazuh\_platform | vulnerability\_finding | 
| wiz\_cnapp | api\_activity | 
| wiz\_cnapp | authentication | 
| wiz\_cnapp | compliance\_finding | 
| wiz\_cnapp | detection\_finding | 
| wiz\_cnapp | vulnerability\_finding | 
| zeek | authentication | 
| zeek | base\_event | 
| zeek | detection\_finding | 
| zeek | dhcp\_activity | 
| zeek | dns\_activity | 
| zeek | email\_activity | 
| zeek | ftp\_activity | 
| zeek | http\_activity | 
| zeek | network\_activity | 
| zeek | rdp\_activity | 
| zeek | smb\_activity | 
| zeek | software\_inventory\_info | 
| zeek | ssh\_activity | 
| zeek | tunnel\_activity | 
| zscaler\_internetaccess | authentication | 
| zscaler\_internetaccess | dns\_activity | 
| zscaler\_internetaccess | http\_activity | 
| zscaler\_internetaccess | network\_activity | 

## Additional third-party sources via AWS Security Hub CSPM
<a name="security-hub-cspm-third-party-sources"></a>

Additional third-party security findings are available through AWS Security Hub CSPM integration. The following partners send findings to Security Hub CSPM, which are then available as data sources in CloudWatch Logs. For comprehensive details about these integrations, see [Third-party product integrations with Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html) in the *AWS Security Hub User Guide*.


| Partner | Integration | 
| --- | --- | 
| 3CORESec – NTA | Sends findings via Security Hub CSPM | 
| Alert Logic – SIEMless Threat Management | Sends findings via Security Hub CSPM | 
| Aqua Security – Cloud Native Security Platform | Sends findings via Security Hub CSPM | 
| Aqua Security – Kube-bench | Sends findings via Security Hub CSPM | 
| Armor – Armor Anywhere | Sends findings via Security Hub CSPM | 
| AttackIQ | Sends findings via Security Hub CSPM | 
| Barracuda Networks – Cloud Security Guardian | Sends findings via Security Hub CSPM | 
| BigID – BigID Enterprise | Sends findings via Security Hub CSPM | 
| Blue Hexagon | Sends findings via Security Hub CSPM | 
| Check Point – CloudGuard IaaS | Sends findings via Security Hub CSPM | 
| Check Point – CloudGuard Posture Management | Sends findings via Security Hub CSPM | 
| Claroty – xDome | Sends findings via Security Hub CSPM | 
| Cloud Storage Security – Antivirus for Amazon S3 | Sends findings via Security Hub CSPM | 
| Contrast Security – Contrast Assess | Sends findings via Security Hub CSPM | 
| CrowdStrike – CrowdStrike Falcon | Sends findings via Security Hub CSPM | 
| CyberArk – Privileged Threat Analytics | Sends findings via Security Hub CSPM | 
| Data Theorem | Sends findings via Security Hub CSPM | 
| Drata | Sends findings via Security Hub CSPM | 
| Forcepoint – CASB | Sends findings via Security Hub CSPM | 
| Forcepoint – Cloud Security Gateway | Sends findings via Security Hub CSPM | 
| Forcepoint – DLP | Sends findings via Security Hub CSPM | 
| Forcepoint – NGFW | Sends findings via Security Hub CSPM | 
| Fugue | Sends findings via Security Hub CSPM | 
| Guardicore – Centra | Sends findings via Security Hub CSPM | 
| HackerOne – Vulnerability Intelligence | Sends findings via Security Hub CSPM | 
| JFrog – Xray | Sends findings via Security Hub CSPM | 
| Juniper Networks – vSRX Next Generation Firewall | Sends findings via Security Hub CSPM | 
| k9 Security – Access Analyzer | Sends findings via Security Hub CSPM | 
| Lacework | Sends findings via Security Hub CSPM | 
| McAfee – MVISION CNAPP | Sends findings via Security Hub CSPM | 
| NETSCOUT – Cyber Investigator | Sends findings via Security Hub CSPM | 
| Orca – Cloud Security Platform | Sends findings via Security Hub CSPM | 
| Palo Alto Networks – Prisma Cloud Compute | Sends findings via Security Hub CSPM | 
| Palo Alto Networks – Prisma Cloud Enterprise | Sends findings via Security Hub CSPM | 
| Plerion – Cloud Security Platform | Sends findings via Security Hub CSPM | 
| Prowler | Sends findings via Security Hub CSPM | 
| Qualys – Vulnerability Management | Sends findings via Security Hub CSPM | 
| Rapid7 – InsightVM | Sends findings via Security Hub CSPM | 
| SentinelOne | Sends findings via Security Hub CSPM | 
| Snyk | Sends findings via Security Hub CSPM | 
| Sonrai Security – Sonrai Dig | Sends findings via Security Hub CSPM | 
| Sophos – Server Protection | Sends findings via Security Hub CSPM | 
| StackRox – Kubernetes Security | Sends findings via Security Hub CSPM | 
| Sumo Logic – Machine Data Analytics | Sends findings via Security Hub CSPM | 
| Symantec – Cloud Workload Protection | Sends findings via Security Hub CSPM | 
| Tenable.io | Sends findings via Security Hub CSPM | 
| Trend Micro – Cloud One | Sends findings via Security Hub CSPM | 
| Vectra – Cognito Detect | Sends findings via Security Hub CSPM | 
| Wiz | Sends findings via Security Hub CSPM | 
| Caveonix – Caveonix Cloud | Sends and receives findings via Security Hub CSPM | 
| Cloud Custodian | Sends and receives findings via Security Hub CSPM | 
| DisruptOps | Sends and receives findings via Security Hub CSPM | 
| Kion | Sends and receives findings via Security Hub CSPM | 
| Turbot | Sends and receives findings via Security Hub CSPM | 

**Note**  
This list reflects the Security Hub partner integrations that send findings at the time of writing. Because AWS Security Hub regularly adds new partner integrations, refer to [Third-party product integrations with Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html) in the *AWS Security Hub User Guide* for the most up-to-date list of available partners.