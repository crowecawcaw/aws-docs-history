

# Enable logging from third-party sources
<a name="enable-logging-third-party"></a>

CloudWatch Logs supports ingesting logs from third-party sources through direct API integrations and Amazon S3 bucket integrations. You can also receive additional third-party security findings through AWS Security Hub CSPM.

## Direct third-party integrations
<a name="direct-third-party-integrations"></a>

CloudWatch Logs provides direct integrations with the following third-party sources. These integrations use either direct API connections or Amazon S3 bucket integrations to ingest logs into CloudWatch Logs:
+ CrowdStrike Falcon
+ Microsoft Office 365
+ Okta Auth0
+ Microsoft Entra ID
+ Palo Alto Networks NGFW
+ Microsoft Windows Events
+ Wiz
+ Zscaler Internet Access
+ Okta SSO
+ SentinelOne Endpoint Security
+ GitHub Audit Logs
+ ServiceNow CMDB
+ Cisco Umbrella

For setup instructions, see the [third-party integration setup guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/third-party-integration-setup.html) in the *Amazon CloudWatch User Guide*.

## Additional sources via AWS Security Hub CSPM
<a name="security-hub-cspm-integrations"></a>

In addition to the direct integrations, third-party security partners send findings to AWS Security Hub CSPM, which are then available as data sources in CloudWatch Logs. The following table lists the Security Hub CSPM partner integrations and their integration type.

To enable Security Hub CSPM findings as a data source in CloudWatch Logs, create a telemetry enablement rule for AWS Security Hub in the CloudWatch console. The enablement rule configures CloudWatch to automatically ingest findings from Security Hub CSPM into a managed log group. For step-by-step instructions, see [Telemetry enablement rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-rules.html) in the *Amazon CloudWatch User Guide*.


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