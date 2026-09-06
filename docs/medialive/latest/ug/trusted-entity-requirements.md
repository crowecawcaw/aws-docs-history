

# Access requirements for the trusted entity
<a name="trusted-entity-requirements"></a>

The following table shows all the types of permissions that the MediaLive trusted entity might need. Refer to this table when you [identify the access requirements for the MediaLive trusted entity](complex-scenario-create-trusted-entity-role-step1.md). 

Each row in the column describes a task or set of related tasks that the MediaLive trusted entity might need to perform for a user. The third column describes the type of access that the trusted entity requires to perform that task. The last column lists the IAM actions or policy that control that access. 




- **AWS Elemental MediaLive **
  - **Tasks:** Working with MediaLive features.
  - **Type of access required:** MediaLive doesn't need access to itself. Only the users need access.
  - **Suggested actions or policy:** 

- **AWS CloudTrail**
  - **Tasks:** Capturing MediaLive activity.
  - **Type of access required:** MediaLive doesn't need IAM access for this task.
  - **Suggested actions or policy:** 

- **CloudWatch **
  - **Tasks:** Displaying CloudWatch metrics information on the console, to monitor channel health.
  - **Type of access required:** MediaLive doesn't need IAM access for this task. Only the users need access.
  - **Suggested actions or policy:** 

- ** CloudWatch Events and Amazon SNS  **
  - **Tasks:** Setting up email notification so that users can be notified about MediaLive alerts that are sent to CloudWatch Events.
  - **Type of access required:** MediaLive doesn't need access for this task. Only the users need access.
  - **Suggested actions or policy:** 

- **CloudWatch Logs**
  - **Tasks:** Sending channel log information to CloudWatch Logs when a channel is running.
  - **Type of access required:** When the channel is running.MediaLive must be able to send log messages to CloudWatch Logs.
  - **Suggested actions or policy:** `CreateLogGroup`<br />`CreateLogStream`<br />`PutLogEvents`<br />`PutMetricFilter`<br />`PutRetentionPolicy`<br />`DescribeLogStreams`<br />`DescribeLogGroups`<br />And these resources:<br /> `arn:aws:logs:`\*<br /> `arn:aws:log-group:`\*

- **Amazon EC2**
  - **Tasks:** Creating a CDI VPC, an RTP VPC input, or an RTMP VPC push input. / **Type of access required:** When the user is creating a VPC input.MediaLive must have write access to Amazon EC2 in order to create network interfaces for the input. / **Suggested actions or policy:** `CreateNetworkInterface`<br />`CreateNetwork InterfacePermission`<br />`DescribeNetworkInterfaces`<br />`DescribeSecurityGroups`<br />`DescribeSubnets`
  - **Tasks:** Deleting a CDI VPC, an RTP VPC input, or an RTMP VPC push input. / **Type of access required:** When the user deletes a VPC input.MediaLive must have write access to Amazon Elastic Compute Cloud in order to delete the network interfaces for the input. / **Suggested actions or policy:** `DeleteNetworkInterface` <br />`DeleteNetworkInterfacePermission` <br />`DescribeNetworkInterfaces` <br />`DescribeSubnets`
  - **Tasks:** Setting up a channel for delivery of output via your VPC / **Type of access required:** Create and delete elastic network interfaces on your VPC. MediaLive creates these network interfaces in the subnet for the channel pipeline endpoints. / **Suggested actions or policy:** `CreateNetworkInterface`<br />`CreateNetworkInterfacePermission`<br />`DeleteNetworkInterface`<br />`DescribeSubnets`<br />`DescribeSecurityGroups`<br />`DescribeAddresses`
  - **Type of access required:** Associate Elastic IP addresses with the elastic network interfaces that MediaLive creates. Associating Elastic IP addresses is optional. There is no need to give access to `DisassociateAddress`. When MediaLive deletes any unnecessary network interfaces, the Elastic IP address will be automatically disassociated from the network interface. / **Suggested actions or policy:** AssociateAddress`DescribeAddresses`

- ** AWS Elemental Inference**
  - **Tasks:** Including Elemental Inference features in a channel. For a list of these features, see [AWS Elemental Inference](elemental-inference.md).
  - **Type of access required:** When the channel is running.MediaLive must be able to deliver source video to Elemental Inference and to obtain the metadata that Elemental Inference produces.
  - **Suggested actions or policy:** GetMetadata`PutMedia`

- **AWS Elemental MediaConnect**
  - **Tasks:** Creating a MediaConnect input. / **Type of access required:** When the user creates a MediaConnect input.MediaLive must have read/write access to the MediaConnect flow, in order to add an output to that flow. / **Suggested actions or policy:** ManagedDescribeFlow`ManagedAddOutput`<br />To include these actions that start with "Managed" in a policy, you must view the policy in the **JSON** tab and enter the names of the actions. You can't use the **visual editor** to choose these actions. 
  - **Tasks:** Deleting a MediaConnect input. / **Type of access required:** When the user deletes a MediaConnect input.MediaLive should have read/write access to the MediaConnect flow, in order to delete the outputs on the flow, because the outputs are no longer needed. / **Suggested actions or policy:** ManagedDescribeFlow`ManagedRemoveOutput`<br />To include these actions that start with "Managed" in a policy, you must view the policy in the **JSON** tab and enter the names of the actions. You can't use the **visual editor** to choose these actions. 
  - **Tasks:** Creating a MediaConnect entitlement. When the user creates a multiplex, MediaLive automatically creates an entitlement as the destination for the MPTS. / **Type of access required:** MediaLive doesn't need access for this task.  / **Suggested actions or policy:** 

- **AWS Elemental MediaPackage**
  - **Tasks:** Sending channel output to MediaPackage when a channel is running, if your deployment uses this service. / **Type of access required:** When the user creates a MediaPackage output group.MediaLive must have read access to the AWS Elemental MediaPackage channel, in order to obtain the credentials required to send to that channel. / **Suggested actions or policy:** DescribeChannel
  - **Tasks:** Sending channel output to MediaPackage v2 when a channel is running, if your deployment uses version 2 of that service. To deliver in this way, you create an HLS output group, not a MediaPackage output group. / **Type of access required:** When the channel is running.When the channel includes an HLS output that is delivering to a MediaPackage channel that uses MediaPackage v2. MediaLive must have write access to the AWS Elemental MediaPackage channel. / **Suggested actions or policy:** mediapackagev2:PutObject

- **AWS Elemental MediaStore**
  - **Tasks:** Sending and retrieving assets from a MediaStore container when a channel is running, if your deployment uses this service.
  - **Type of access required:** When the channel is running.MediaLive must have read access (for a source) or read/write access (for a destination).
  - **Suggested actions or policy:** `ListContainers`<br />`DescribeObject`<br />`PutObject`<br />`GetObject`<br />`DeleteObject`

- **Resource Group Tagging**
  - **Tasks:** Attaching tags when creating resources—channels, inputs, and input security groups—and revising tags on existing resources.
  - **Type of access required:** MediaLive doesn't need IAM access for this task. Only the users need access.
  - **Suggested actions or policy:** 

- **Amazon S3**
  - **Tasks:** Sending and retrieving assets from an Amazon S3 bucket when a channel is running, if your deployment uses this service. / **Type of access required:** When the channel is running.MediaLive must have read access (for a source) or read/write access (for a destination) to the buckets. / **Suggested actions or policy:** `ListBucket`<br />`PutObject`<br />`GetObject`<br />`DeleteObject`
  - **Tasks:** Sending thumbnails to an Amazon S3 bucket when a channel is running, if a channel has input thumbnails enabled / **Type of access required:** When the channel is running.MediaLive must have read/write access. / **Suggested actions or policy:** PutObject

- **AWS Secrets Manager**
  - **Tasks:** Sending an SRT caller output when a channel is running. SRT caller outputs are always encrypted using a passphrase that is stored in a Secrets Manager secret. / **Type of access required:** When the channel is running.MediaLive must be able to read the value (the passphrase) stored in the secret. / **Suggested actions or policy:** GetSecretValue
  - **Tasks:** Reading the Irdeto A/B watermarking license when a channel is running, if the output group uses Irdeto A/B watermarking. The license is stored in a Secrets Manager secret. / **Type of access required:** When the channel is running.MediaLive must be able to read the license stored in the secret. / **Suggested actions or policy:** GetSecretValue

- **AWS Systems Manager**
  - **Tasks:** Creating a password parameter on the MediaLive console. / **Type of access required:** MediaLive doesn't need IAM access for this task. Only the users need access. / **Suggested actions or policy:** 
  - **Tasks:** Using a password parameter in the channel configuration. See [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md). / **Type of access required:** When the channel is running.MediaLive must have read access to the AWS Systems Manager Parameter Store. / **Suggested actions or policy:** The managed policy AmazonSSMRead OnlyAccess

