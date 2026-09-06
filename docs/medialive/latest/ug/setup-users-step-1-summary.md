

# Reference: summary of non-administrator user access requirements
<a name="setup-users-step-1-summary"></a>

The following table shows all the types of permissions that you might need to assign to users. Each row in the column describes an activity or set of related activities that you might want to allow the user to perform. The last column lists the IAM actions that control access to those activities. 

If this table doesn't provide enough information for you to determine which permissions to assign to users, see the alphabetical list of services that follow this section. 



- **Use the features of MediaLive**
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Create, modify, and delete channels, devices, inputs, and input security groups / **Actions to include in the policy:** CreateChannel`CreateInput`<br />`CreateInputSecurityGroup`<br />`DeleteChannel`<br />`DeleteInput`<br />`DeleteInputSecurityGroup`<br />`UpdateChannel`<br />`UpdateInput`<br />`UpdateInputDevice`<br />`UpdateInputSecurityGroup`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** View channels, devices, inputs, and input security groups / **Actions to include in the policy:** `ListChannels`<br />`ListInputDevices`<br />`ListInputs`<br />`ListInputSecurityGroups`<br />`DescribeChannel`<br />`DescribeInput`<br />`DescribeInputDevice`<br />`DescribeInputDeviceThumbnail`<br />`DescribeInputSecurityGroup`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Perform a batch operation on several channels or inputs or multiplexes or input security groups / **Actions to include in the policy:** `BatchDelete`BatchStart<br />`BatchStop`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Create or cancel an outgoing device transfer, or accept or reject an incoming device transfer, and view pending device transfers / **Actions to include in the policy:** `AcceptInputDeviceTransfer`<br />`CancelInputDeviceTransfer`<br />`ListInputDeviceTransfers`<br />`RejectInputDeviceTransfer`<br />`TransferInputDevice`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Work with schedules / **Actions to include in the policy:** DescribeSchedule`BatchUpdateSchedule`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Create or modify multiplexes / **Actions to include in the policy:** CreateMultiplex`DescribeMultiplex`<br />`ListMultiplexes`<br />`UpdateMultiplex`
  - **Corresponding service in IAM:** Amazon EC2 / **Actions to include in the policy:** DescribeAvailabilityZonesYou need this operation to view the list of Availability Zones on the MediaLive console, so that you can choose two for the multiplex.
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Delete multiplexes / **Actions to include in the policy:** `DeleteMultiplex`<br />`DescribeMultiplex`<br />`ListMultiplexes`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** View multiplexes / **Actions to include in the policy:** `DescribeMultiplex`<br />`ListMultiplexes`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Change the class for a channel / **Actions to include in the policy:** UpdateChannelClass
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Run channels / **Actions to include in the policy:** StartChannel`StopChannel`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Pause channels / **Actions to include in the policy:** Pause is an activity within the schedule feature, shown earlier in this table.
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Run multiplexes / **Actions to include in the policy:** StartMultiplex`StopMultiplex`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Attach tags to channels, inputs, and input security groups when creating those resources / **Actions to include in the policy:** CreateTag`DeleteTags`<br />`ListTagsForResources`
  - **Corresponding service in IAM:** MediaLive / **Specific activities the user can perform:** Create, modify, delete, and view reservations and offerings / **Actions to include in the policy:** `DeleteReservation`<br />`DescribeOffering`<br />`DescribeReservation`<br />`ListOfferings`<br />`ListReservations`<br />`PurchaseOffering`
  - **Corresponding service in IAM:** CloudFormation / **Specific activities the user can perform:** Create and delete the CloudFormation stack. These permissions are always required. For example, if a user is using the workflow wizard and doesn't have CreateStack access, MediaLive will fail to create the workflow. / **Actions to include in the policy:** `ListStacks`<br />`DescribeStacks`<br />`DescribeStackResources`<br />`CreateStack`<br />`DeleteStack`
  - **Corresponding service in IAM:** CloudFront / **Specific activities the user can perform:** Create and delete a CloudFront distribution, if your organization supports MediaPackage as an output destination.Note how the required permissions here are very different from the permissions because the workflow wizard actually creates the distribution. / **Actions to include in the policy:** ListDistributions`DescribeDistribution`<br />`CreateDistribution`<br />`DeleteDistribution`
  - **Corresponding service in IAM:** Amazon EC2 / **Specific activities the user can perform:** Create a VPC input – View the VPC subnets and VPC security groups on the MediaLive console  / **Actions to include in the policy:** DescribeSubnets`DescribeSecurityGroups`
  - **Corresponding service in IAM:** Amazon EC2 / **Specific activities the user can perform:** Set up a channel for delivery of output via your VPC – View the VPC subnets and VPC security groups on the MediaLive console. / **Actions to include in the policy:** DescribeSubnets`DescribeSecurityGroups`
  - **Corresponding service in IAM:** Amazon EC2 / **Specific activities the user can perform:** Set up a channel for delivery of output via your VPC – View the Elastic IP addresses on the console. The console finds the Elastic IP addresses that have been allocated for use in your AWS account. / **Actions to include in the policy:** DescribeAddresses
  - **Corresponding service in IAM:** MediaConnect / **Specific activities the user can perform:** Use the workflow wizard to create a MediaConnect flow, if your organization supports sources from MediaConnect.Use the workflow wizard to delete a workflow that includes a source from MediaConnect. / **Actions to include in the policy:** List\*`Describe*`<br />`Create*`<br />`Delete*`
  - **Corresponding service in IAM:** MediaPackage / **Specific activities the user can perform:** On the MediaLive console, view the MediaPackage channels in the dropdown list on the MediaLive channel. / **Actions to include in the policy:** Describe\*
  - **Specific activities the user can perform:** Use the workflow wizard to create a MediaPackage channel, if your organization supports MediaPackage as an output destination.Use the workflow wizard to delete a workflow that includes a MediaPackage output. / **Actions to include in the policy:** List\*`Describe*`<br />`Create*`<br />`Delete*`
  - **Corresponding service in IAM:** MediaStore / **Specific activities the user can perform:** Use the workflow wizard to create a MediaStore container, if your organization supports MediaStore as an output destination.Use the workflow wizard to delete a workflow that includes a MediaStore output. / **Actions to include in the policy:** List\*`Describe*`<br />`Create*`<br />`Delete*`
  - **Corresponding service in IAM:** Secrets Manager / **Specific activities the user can perform:** On the MediaLive console, when creating an SRT Caller input or an SRT Caller output, to view Secrets Manager secrets in the dropdown list in the **Passphrase secret arn** field. / **Actions to include in the policy:** ListSecrets

- **Monitor channel health**
  - **Corresponding service in IAM:** CloudWatch
  - **Specific activities the user can perform:** 
  - **Actions to include in the policy:** `ListMetrics`<br />`GetMetricData`<br />`GetMetricStatistics`

- **Set up events**
  - **Corresponding service in IAM:** CloudWatch Events
  - **Specific activities the user can perform:** 
  - **Actions to include in the policy:** All actionsThe managed policy `CloudWatchEventsFullAccess` provides these permissions

- **Set up channel logging**
  - **Corresponding service in IAM:** Amazon CloudWatch Logs
  - **Specific activities the user can perform:** View logs / **Actions to include in the policy:** FilterLogEvents`GetLogEvents`
  - **Specific activities the user can perform:** Set retention policy / **Actions to include in the policy:** DeleteRetentionPolicy`PutRetentionPolicy`

- **Simple option for the trusted entity role**
  - **Corresponding service in IAM:** IAM
  - **Specific activities the user can perform:** Create the MediaLiveAccessRole / **Actions to include in the policy:** `CreateRole`<br />`PutRolePolicy`<br />`AttachRolePolicy`
  - **Specific activities the user can perform:** Choose the MediaLiveAccessRole / **Actions to include in the policy:** `ListRole`<br />`PassRole` 
  - **Specific activities the user can perform:** Update the MediaLiveAccessRole / **Actions to include in the policy:** `GetRolePolicy`<br />`PutRolePolicy`<br />`AttachRolePolicy`

- **Complex option for the trusted entity role**
  - **Corresponding service in IAM:** IAM
  - **Specific activities the user can perform:** Enter a role for the trusted entity
  - **Actions to include in the policy:** PassRole

- **Use features of AWS Elemental Inference**
  - **Corresponding service in IAM:** Elemental Inference
  - **Specific activities the user can perform:** When configuring a channel, so that MediaLive can work with the Elemental Inference feed
  - **Actions to include in the policy:** `CreateFeed`<br />`DeleteFeed`<br />`GetFeed`<br />`ListFeeds`<br />`UpdateFeed`

- **Let MediaLive use FAS**
  - **Corresponding service in IAM:** Elemental Inference
  - **Specific activities the user can perform:** So that MediaLive can use FAS to associate a newly configured channel with the Elemental Inference feed.
  - **Actions to include in the policy:** `AssociateFeed`<br />`DisassociateFeed`<br />`GetFeed`

- **Deploy and work with AWS Elemental Link devices**
  - **Corresponding service in IAM:** MediaLive
  - **Specific activities the user can perform:** Deploy, configure, and view an AWS Elemental Link device 
  - **Actions to include in the policy:** `DescribeInputDevice`<br />`DescribeInputDeviceThumbnail`<br />`ListInputDevices`<br />`RebootInputDevice`<br />`StartInputDeviceMaintenanceWindow`<br />`StartInputDevice`<br />`StopInputDevice`<br />`UpdateInputDevice`

- **Handle transfers of AWS Elemental Link devices**
  - **Corresponding service in IAM:** MediaLive
  - **Specific activities the user can perform:** Handle transfers of AWS Elemental Link devices
  - **Actions to include in the policy:** `AcceptInputDeviceTransfer`<br />`CancelInputDeviceTransfer`<br />`ClaimDevice`<br />`ListInputDeviceTransfers`<br />`RejectInputDeviceTransfer`<br />`TransferInputDevice`

- **Set up a AWS Elemental Link device as the source for a MediaConnect flow**
  - **Corresponding service in IAM:** MediaConnect / **Specific activities the user can perform:** On the MediaLive console, view MediaConnect flows in the dropdown list. This dropdown list appears in the **Flow ARN** field in the **Attachments** tab on the **Device details** page. / **Actions to include in the policy:** ListFlows
  - **Corresponding service in IAM:** IAM / **Specific activities the user can perform:** On the MediaLive console, view IAM roles in the dropdown list. This dropdown list appears in the **Role ARN** field in the **Attachments** tab on the **Device details** page. / **Actions to include in the policy:** ListRoles
  - **Corresponding service in IAM:** Secrets Manager / **Specific activities the user can perform:** On the MediaLive console, view Secrets Manager secrets in the dropdown list. This dropdown list appears in the **Secret ARN** field in the **Attachments** tab on the **Device details** page. / **Actions to include in the policy:** ListSecrets

- **Set up email notification**
  - **Corresponding service in IAM:** Amazon SNS
  - **Specific activities the user can perform:** 
  - **Actions to include in the policy:** All actionsThe managed policy `AmazonSNSFullAccess` provides these permissions

- **AWS Systems Manager**
  - **Corresponding service in IAM:** Systems Manager / **Specific activities the user can perform:** Create a password parameter using the MediaLive console or the AWS Systems Manager console / **Actions to include in the policy:** `DeleteParameter`<br />`DeleteParameters`<br />`DescribeParameters`<br />`GetParameter`<br />`GetParameterHistory`<br />`GetParameters`<br />`GetParametersByPath`<br />`PutParameter`
  - **Corresponding service in IAM:** Systems Manager / **Specific activities the user can perform:** Choose a password parameter from the dropdown list on the MediaLive console / **Actions to include in the policy:** DescribeParameters

