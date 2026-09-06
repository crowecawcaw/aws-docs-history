

# Exception to controls for the Security OU
<a name="exception-to-controls-security-ou"></a>

For customers on LZ v4.0:

There is no longer a Security OU managed by AWS Control Tower so restrictions below do not apply.

For existing customers on LZ v3.3 and below:

AWS Control Tower deploys and manages resources in the Security OU, which are required so that AWS Control Tower can function properly. You can deploy certain preventive controls (SCP-based) and detective controls (based on AWS Config rules) to this OU. Most controls cannot be enabled for this OU.

**Controls that cannot be deployed to the Security OU**
+ You cannot deploy proactive controls to the Security OU.
+ You cannot deploy Security Hub controls to the Security OU.
+ You cannot deploy RCP-based controls to the Security OU.
+ You cannot deploy declarative policies to the Security OU.
+ Certain SCP-based controls cannot be deployed to the Security OU.

**Controls that are deployable to the Security OU**
+ All controls implemented by AWS Config rules
+ AWS-GR\_AUDIT\_BUCKET\_DELETION\_PROHIBITED (Mandatory)
+ AWS-GR\_AUDIT\_BUCKET\_ENCRYPTION\_ENABLED
+ AWS-GR\_AUDIT\_BUCKET\_LOGGING\_ENABLED
+ AWS-GR\_AUDIT\_BUCKET\_POLICY\_CHANGES\_PROHIBITED (Mandatory)
+ AWS-GR\_AUDIT\_BUCKET\_RETENTION\_POLICY
+ AWS-GR\_CLOUDTRAIL\_CHANGE\_PROHIBITED
+ AWS-GR\_CLOUDTRAIL\_CLOUDWATCH\_LOGS\_ENABLED
+ AWS-GR\_CLOUDTRAIL\_ENABLED
+ AWS-GR\_CLOUDTRAIL\_VALIDATION\_ENABLED
+ AWS-GR\_CLOUDWATCH\_EVENTS\_CHANGE\_PROHIBITED
+ AWS-GR\_CONFIG\_AGGREGATION\_AUTHORIZATION\_POLICY
+ AWS-GR\_CONFIG\_AGGREGATION\_CHANGE\_PROHIBITED
+ AWS-GR\_CONFIG\_CHANGE\_PROHIBITED
+ AWS-GR\_CONFIG\_ENABLED
+ AWS-GR\_CONFIG\_RULE\_CHANGE\_PROHIBITED
+ AWS-GR\_CT\_AUDIT\_BUCKET\_ENCRYPTION\_CHANGES\_PROHIBITED (Mandatory)
+ AWS-GR\_CT\_AUDIT\_BUCKET\_LIFECYCLE\_CONFIGURATION\_CHANGES\_PROHIBITED (Mandatory)
+ AWS-GR\_CT\_AUDIT\_BUCKET\_LOGGING\_CONFIGURATION\_CHANGES\_PROHIBITED (Mandatory)
+ AWS-GR\_CT\_AUDIT\_BUCKET\_POLICY\_CHANGES\_PROHIBITED
+ AWS-GR\_DISALLOW\_CROSS\_REGION\_NETWORKING
+ AWS-GR\_DISALLOW\_VPC\_INTERNET\_ACCESS
+ AWS-GR\_DISALLOW\_VPN\_CONNECTIONS
+ AWS-GR\_IAM\_ROLE\_CHANGE\_PROHIBITED
+ AWS-GR\_LAMBDA\_CHANGE\_PROHIBITED
+ AWS-GR\_LOG\_GROUP\_POLICY
+ AWS-GR\_REGION\_DENY
+ AWS-GR\_RESTRICT\_ROOT\_USER
+ AWS-GR\_RESTRICT\_ROOT\_USER\_ACCESS\_KEYS
+ AWS-GR\_RESTRICT\_S3\_CROSS\_REGION\_REPLICATION
+ AWS-GR\_RESTRICT\_S3\_DELETE\_WITHOUT\_MFA
+ AWS-GR\_SNS\_CHANGE\_PROHIBITED
+ AWS-GR\_SNS\_SUBSCRIPTION\_CHANGE\_PROHIBITED
+ CT.BACKUP.PV.1
+ CT.BACKUP.PV.2
+ CT.BACKUP.PV.3
+ CT.CLOUDFORMATION.PR.1
+ CT.IAM.PV.1
+ CT.S3.PV.1
+ CT.S3.PV.7
+ CT.S3.PV.8
+ CT.SNS.PV.1