

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# EC2 IAM instance profile
<a name="defaults-instance-profile"></a>

An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts.

------
#### [ MALZ ]

There are two AMS default instance profiles, `customer-mc-ec2-instance-profile` and `customer-mc-ec2-instance-profile-s3`. These instance profiles provide the permissions described in the following table.


**Policy descriptions**  
<a name="default-iam-profile-malz-table"></a>

- **`customer-mc-ec2-instance-profile`**
  - `AmazonSSMManagedInstanceCore`: Allows Ec2 instances to use the SSM agent.
  - `AMSInstanceProfileLoggingPolicy`: Allows Ec2 instances to push logs to S3 and CloudWatch.
  - `AMSInstanceProfileManagementPolicy`: Allows Ec2 instances to perform booting actions, like joining Active Directory.
  - `AMSInstanceProfileMonitoringPolicy`: Allows Ec2 instances to report findings to AMS monitoring services.
  - `AMSInstanceProfilePatchPolicy`: Allows Ec2 instances to receive patches.

- **`customer-mc-ec2-instance-profile-s3`**
  - `AMSInstanceProfileBYOEPSPolicy`: Allows Ec2 instances to use [AMS bring your own EPS](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-byoeps.html).
  - `AMSInstanceProfileLoggingPolicy`: Allows Ec2 instances to push logs to S3 and CloudWatch.
  - `AMSInstanceProfileManagementPolicy`: Allows Ec2 instances to perform booting actions, like joining Active Directory.
  - `AMSInstanceProfileMonitoringPolicy`: Allows Ec2 instances to report findings to AMS monitoring services.
  - `AMSInstanceProfilePatchPolicy`: Allows Ec2 instances to receive patches.
  - `AMSInstanceProfileS3WritePolicy`: Allows Ec2 instances to read/write to customer S3 buckets.



------
#### [ SALZ ]

There is one AMS default instance profile, `customer-mc-ec2-instance-profile`, that grants permissions from the IAM instance policy `customer_ec2_instance_profile_policy`. This instance profile provides the permissions described in the following table. The profile grants permissions to the applications running on the instance, not to users logging into the instance.

Policies often include multiple statements, where each statement grants permissions to a different set of resources or grants permissions under a specific condition.

CW = CloudWatch. ARN = Amazon Resource Name. \* = wildcard (any).


**EC2 default IAM instance profile permissions**  

<table>
<thead>
  <tr><th colspan="4">CW = CloudWatch. ARN = Amazon Resource Name. * = wildcard (any).</th></tr>
  <tr><th>Policy statement</th><th>Effect</th><th>Actions</th><th>Description and resource (ARN)</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Amazon Elastic Compute Cloud (Amazon EC2)</b></td></tr>
  <tr><td>EC2 Message Actions</td><td>Allow</td><td>AcknowledgeMessage,<br />DeleteMessage,<br />FailMessage,<br />GetEndpoint,<br />GetMessages,<br />SendReply</td><td>Allows EC2 Systems Manager messaging actions in your account.</td></tr>
  <tr><td>Ec2 Describe</td><td>Allow</td><td>* (All)</td><td>Allows the console to display configuration details of an EC2 in your account.</td></tr>
  <tr><td>Iam Get Role ID</td><td>Allow</td><td>GetRole</td><td>Allows EC2 to get your IAM ID from <code>aws:iam::*:role/customer-*</code> and <code>aws:iam::*:role/customer_*</code>.</td></tr>
  <tr><td rowspan="2">Instance To Upload Log Events</td><td rowspan="2">Allow</td><td>Create Log Group</td><td>Allows logs to be created in: <code>aws:logs:*:*:log-group:i-*</code></td></tr>
  <tr><td>Create Log Stream</td><td>Allows logs to be streamed to: <code>aws:logs:*:*:log-group:i-*</code></td></tr>
  <tr><td>CW For MMS</td><td>Allow</td><td>DescribeAlarms,<br />PutMetricAlarm,<br />PutMetricData</td><td>Allows CloudWatch to retrieve alarms in your account.<br />Allows CW to create or update an alarm and associate it with the specified metric.<br />Allows CW to publish metric data points to your account.</td></tr>
  <tr><td>Ec2 Tags</td><td>Allow</td><td>CreateTags,<br />DescribeTags,</td><td>Allows tags to be added, overwritten, and described on the specified instances in your account.</td></tr>
  <tr><td>Explicitly Deny CW Logs</td><td>Deny</td><td>DescribeLogStreams,<br />FilterLogEvents,<br />GetLogEvents</td><td>Disallows listing, filtering, or getting the log streams for: <code>aws:logs:*:*:log-group:/mc/*</code></td></tr>
  <tr><td colspan="4"><b>Amazon EC2 Simple Systems Manager (SSM)</b></td></tr>
  <tr><td>SSM Actions</td><td>Allow</td><td>DescribeAssociation,<br />GetDocument,<br />ListAssociations,<br />UpdateAssociationStatus,<br />UpdateInstanceInformation</td><td>Allows a variety of SSM functions in your account.</td></tr>
  <tr><td>SSM Access In S3</td><td>Allow</td><td>GetObject,<br />PutObject,<br />AbortMultipartUpload,<br />ListMultipartUploadPorts,<br />ListBucketMultipartUploads</td><td>Allows the SSM on the EC2 to get and update objects in, and to abort a multi-part object upload to, and list ports and buckets available for, multi-part uploads in <code>aws:s3:::mc-*-internal-*/aws/ssm*</code>.</td></tr>
  <tr><td colspan="4"><b>Amazon EC2 Simple Storage Service (S3)</b></td></tr>
  <tr><td>Get Object In S3</td><td>Allow</td><td>Get<br />List</td><td>Allows EC2 applications to retrieve and list objects in S3 buckets in your account.</td></tr>
  <tr><td>Customer Encrypted Log S3 Access</td><td>Allow</td><td>PutObject</td><td>Allows EC2 applications to update objects in <code>aws:s3:::mc-*-logs-*/encrypted/app/*</code></td></tr>
  <tr><td>Patch Data Put Object S3</td><td>Allow</td><td>PutObject</td><td>Allows EC2 applications to upload patching data to your S3 buckets at <code>aws:s3:::awsms-a*-patch-data-*</code></td></tr>
  <tr><td>Uploading Own Logs To S3</td><td>Allow</td><td>PutObject</td><td>Allows EC2 applications to upload custom logs to: <code>aws:s3:::mc-a*-logs-*/aws/instances/*/${aws:userid}/*</code></td></tr>
  <tr><td>Explicitly Deny MC Namespace S3 Logs</td><td>Deny</td><td>GetObject*<br />Put*</td><td>Disallows EC2 applications getting or putting any objects from or to:<br /><code>aws:s3:::mc-*-logs-*/encrypted/mc*</code>,<br /><code>aws:s3:::mc-*-logs-*/mc/*</code>,<br /><code>aws:s3:::mc-a*-logs-*-audit/*</code></td></tr>
  <tr><td>Explicitly Deny S3 Delete</td><td>Deny</td><td>* (all)</td><td>Disallows EC2 applications taking any action on objects in:<br /><code>aws:s3:::mc-a*-logs-*/*</code>,<br /><code>aws:s3:::mc-a*-internal-*/*</code>,</td></tr>
  <tr><td>Explicitly Deny S3 CFN Bucket</td><td>Deny</td><td>Delete*</td><td>Disallows EC2 applications deleting any objects from: <code>aws:s3:::cf-templates-*</code></td></tr>
  <tr><td>Explicitly Deny List Bucket S3</td><td>Deny</td><td>ListBucket</td><td>Disallows you listing any encrypted, audit log, or reserved (mc) objects from: <code>aws:s3:::mc-*-logs-*</code></td></tr>
  <tr><td colspan="4"><b>AWS Secrets Manager in Amazon EC2</b></td></tr>
  <tr><td>Trend Cloud One Secrets Access</td><td>Allow</td><td>GetSecretValue</td><td>Allows Amazon EC2 to access secrets for Trend Cloud One migration:<br /><code>aws:secretsmanager:*:*:secret:/ams/eps/cloud-one-agent-tenant-id*</code>,<br /><code>arn:aws:secretsmanager:*:*:secret:/ams/eps/cloud-one-agent-activation-token*</code>,<br /><code>aws:secretsmanager:*:*:secret:/ams/eps/cloud-one-agent-tenant-id*</code>,<br /><code>aws:secretsmanager:*:*:secret:/ams/eps/cloud-one-agent-tenant-guid*</code></td></tr>
  <tr><td colspan="4"><b>AWS Key Management Service in Amazon EC2</b></td></tr>
  <tr><td>Trend Cloud One Decryption Key</td><td>Allow</td><td>Decrypt</td><td>Allow Amazon EC2 to decrypt the AWS KMS key with alias name /ams/eps/cloudone-migration<br /><code>arn:aws:kms:*:*:alias/ams/eps/cloudone-migration</code></td></tr>
</tbody>
</table>


------

If you're unfamiliar with Amazon IAM policies, see [Overview of IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for important information.

**Note**  
Policies often include multiple statements, where each statement grants permissions to a different set of resources or grants permissions under a specific condition.