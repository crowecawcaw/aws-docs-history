

# Filtering findings in GuardDuty
<a name="guardduty_filter-findings"></a>

A finding filter allows you to view findings that match the criteria you specify and filter out any unmatched findings. You can easily create finding filters using the Amazon GuardDuty console, or you can create them with the [CreateFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateFilter.html) API using JSON. Review the following sections to understand how to create a filter in the console. To use these filters to automatically archive incoming findings, see [Suppression rules in GuardDuty](findings_suppression-rule.md).

When you create filters, take the following list into consideration:
+ You can specify a minimum of one attribute and up to a maximum of 50 attributes as the criteria for a particular filter. 
+ When you use the **Equals** or **Does not equals** operator to filter on an attribute value, such as Account ID, you can specify a maximum of 50 values.
+ Each filter criteria attribute is evaluated as an `AND` operator. Multiple values for the same attribute are evaluated as `AND/OR`.
+ For information about the maximum number of saved filters that you can create in an AWS account in each AWS Region, see [GuardDuty quotas](guardduty_limits.md).
+ Fields under `service.additionalInfo` are specified using their full JSON path, the same as any other field. For example: `{ "service.additionalInfo.sample": { "Equals": ["true"] } }`.
+ Timestamp fields accept values in Unix Epoch millisecond format (for example, `1486685375000`). For a full list of timestamp fields, see the note below.

The following sections provide instructions on how to create and save filters using GuardDuty console, and API and CLI commands. Choose your preferred access method to proceed.

## Creating and saving filter set in the GuardDuty console
<a name="filter_console"></a>

Finding filters can be created and tested through the GuardDuty console. You can save filters created through the console for use in suppression rules or future filter operations. A filter is made up of at least one filter criteria, which consists of one filter attribute paired with at least one value.

**To create and save filter criteria (console)**

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the left navigation pane, choose **Findings**.

1. On the **Findings** page, select the *Filter findings* bar next to **Saved rules** menu. This will display an expanded list of **Property filters**.  
![Selecting property filters to filter findings in the GuardDuty console.](http://docs.aws.amazon.com/guardduty/latest/ug/images/guardduty-findings-page-console.png)

1. From the expanded list of filters, select an attribute based on which you want to filter the findings table.

   For example, to view findings for which the potentially impacted resource is an **S3Bucket**, choose **Resource type**. 

1. For **Operators**, choose one that will help you filter the findings to get the desired result. To continue the example from the previous step, choose **Resource type =**. This will display a list of resource types in GuardDuty.   
![Selecting the equals or does not equals operator to filter findings in GuardDuty console.](http://docs.aws.amazon.com/guardduty/latest/ug/images/guardduty-findings-page-filters-operator-console.png)

   If your use case requires excluding specific findings, you can choose **Does not equal** or **\!=** operator.

1. Specify the value for the selected property filter. If needed, choose **Apply**. To continue the example from the previous step, you can choose **S3Bucket**.

   This will display the findings that match with the applied filters.

1. To add more than one filter criteria, repeat steps 3-6. 

   For a complete list of attributes, see [Property filters in GuardDuty](#filter_criteria).

1. 

**(Optional) save the specified attributes and values as filters**

   To apply this filter combination again in the future, you can save the specified attributes and their values as a filter set.

   1. After you have created a filter criteria with one or more property filters, select the *arrow* in the **Clear filters** menu.  
![Saving a filter set in GuardDuty console to be able to filter the findings again.](http://docs.aws.amazon.com/guardduty/latest/ug/images/guardduty-findings-page-filters-console.png)

   1. Enter the filter set **Name**. The name must be 3-64 characters. Valid characters are a-z, A-Z, 0-9, period (.), hyphen (-), and underscore (\_).

   1. The **Description** is optional. If you enter a description, it can have up to 512 characters.

   1. Choose **Create**.

## Creating and saving filter set by using GuardDuty API and CLI
<a name="guardduty-creating-filters-using-api-cli"></a>

You can create and test the finding filters by using either API or CLI commands. A filter is made up of at least one filter criteria, which consists of one filter attribute paired with at least one value. You can save filters to create [Suppression rules](findings_suppression-rule.md) or to perform other filter operations later. 

**To create finding filters using API/CLI**
+ Run [CreateFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateFilter.html) API by using the regional detector ID of the AWS account where you want to create a filter. 

  To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
+ Alternatively, you can use the [create-filter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html) CLI to create and save the filter. You can use one or more filter criteria from [Property filters in GuardDuty](#filter_criteria).

  Use the following examples by replacing the placeholder values shown in red.  
**Example 1**: Create a new filter to view all the findings that match a specific finding type  
The following example creates a filter that matches all `PortScan` findings for an instance created from a specific image. The placeholder values are shown in red. Replace these values with suitable values for your account. For example, replace {{12abc34d567e8fa901bc2d34EXAMPLE}} with your regional detector ID.  

  ```
  aws guardduty create-filter \
  --detector-id {{12abc34d567e8fa901bc2d34EXAMPLE}} \
  --name {{FilterExampleName}} \
  --finding-criteria '{"Criterion": {{{"type": {"Equals": ["{{Recon:EC2/Portscan}}"]}}}, "{{resource.instanceDetails.imageId": {"Equals":["ami-0a7a207083example"]}}}} }'
  ```  
**Example 2**: Create a new filter to view all the findings that match severity levels  
The following example creates a filter that matches all findings associated with the `HIGH` severity levels. The placeholder values are shown in red. Replace these values with suitable values for your account. For example, replace {{12abc34d567e8fa901bc2d34EXAMPLE}} with your regional detector ID.  

  ```
  aws guardduty create-filter \
  --detector-id {{12abc34d567e8fa901bc2d34EXAMPLE}} \
  --name {{FilterExampleName}} \
  --finding-criteria '{"Criterion": {{{"severity": {"Equals": ["{{7}}", "{{8}}"]}}}} }'
  ```
+ For API/CLI, the [Findings severity levels](guardduty_findings-severity.md) are represented as numerals. To filter the findings based on the severity levels, use the following values:
  + For `LOW` severity levels, use `{ "severity": { "Equals": ["1", "2", "3"] } }`
  + For `MEDIUM` severity levels, use `{ "severity": { "Equals": ["4", "5", "6"] } }`
  + For `HIGH` severity levels, use `{ "severity": { "Equals": ["7", "8"] } }`
  + For `CRITICAL` severity levels, use `{ "severity": { "Equals": ["9", "10"] } }`
  + For findings with multiple severity levels, use placeholder values similar to the following example: `{ "severity": { "Equals": ["7", "8", "9", "10"] } }`

    This example will show the findings that have either `HIGH` or `CRITICAL` severity levels.
**Note**  
If you specify an example with only one numeric value instead of all the numeric values associated with a severity level, the API and CLI might show the filtered findings. When you use this saved filter set in the GuardDuty console, it will not work as expected. This is because the GuardDuty console considers the filter values as `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW`. For example, a filter created with a CLI command that includes `{ "severity": { "Equals": ["9"] } }` is expected to show an appropriate output in API/CLI. However, this saved filter includes partial severity level when used in the GuardDuty console and will not show an expected output. This makes it necessary for the API and CLI to specify all the values associated with each severity level.

## Property filters in GuardDuty
<a name="filter_criteria"></a>

When you create filters or sort findings using the API operations, you must specify filter criteria in JSON. These filter criteria correlate to a finding's details JSON. The following table contains a list of the console display names for filter attributes and their equivalent JSON field names.


| Console field name | JSON field name | 
| --- | --- | 
| Account ID | accountId | 
| Finding ID | id | 
| Region | region | 
| Severity | severity<br />You can filter the finding types based on the severity level of the finding types. For more information about severity values, see [Severity levels of GuardDuty findings](guardduty_findings-severity.md). If you use `severity` with API, AWS CLI, or CloudFormation, it is assigned a numeric value. For more information, see [findingCriteria](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateFilter.html#guardduty-CreateFilter-request-findingCriteria) in the *Amazon GuardDuty API Reference*. | 
| Finding type | type | 
| Updated at | updatedAt | 
| Access Key ID | resource.accessKeyDetails.accessKeyId | 
| Principal ID | resource.accessKeyDetails.principalId | 
| Username | resource.accessKeyDetails.userName | 
| User type | resource.accessKeyDetails.userType | 
| IAM instance profile ID | resource.instanceDetails.iamInstanceProfile.id | 
| Instance ID | resource.instanceDetails.instanceId | 
| Instance image ID | resource.instanceDetails.imageId | 
| Instance tag key | resource.instanceDetails.tags.key | 
| Instance tag value | resource.instanceDetails.tags.value | 
| IPv6 address | resource.instanceDetails.networkInterfaces.ipv6Addresses | 
| Private IPv4 address | resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress | 
| Public DNS name | resource.instanceDetails.networkInterfaces.publicDnsName | 
| Public IP | resource.instanceDetails.networkInterfaces.publicIp | 
| Security group ID | resource.instanceDetails.networkInterfaces.securityGroups.groupId | 
| Security group name | resource.instanceDetails.networkInterfaces.securityGroups.groupName | 
| Subnet ID | resource.instanceDetails.networkInterfaces.subnetId | 
| VPC ID | resource.instanceDetails.networkInterfaces.vpcId | 
| Outpost ARN | resource.instanceDetails.outpostARN | 
| Resource type | resource.resourceType | 
| Bucket permissions | resource.s3BucketDetails.publicAccess.effectivePermission | 
| Bucket name  | resource.s3BucketDetails.name | 
| Bucket tag key | resource.s3BucketDetails.tags.key | 
| Bucket tag value | resource.s3BucketDetails.tags.value | 
| Bucket type | resource.s3BucketDetails.type | 
| Action type | service.action.actionType | 
| API called | service.action.awsApiCallAction.api | 
| API caller type | service.action.awsApiCallAction.callerType | 
| API Error Code | service.action.awsApiCallAction.errorCode | 
| API caller city | service.action.awsApiCallAction.remoteIpDetails.city.cityName | 
| API caller country | service.action.awsApiCallAction.remoteIpDetails.country.countryName | 
| API caller IPv4 address | service.action.awsApiCallAction.remoteIpDetails.ipAddressV4 | 
| API caller IPv6 address | service.action.awsApiCallAction.remoteIpDetails.ipAddressV6 | 
| API caller ASN ID | service.action.awsApiCallAction.remoteIpDetails.organization.asn | 
| API caller ASN name | service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg | 
| API caller service name | service.action.awsApiCallAction.serviceName | 
| DNS request domain | service.action.dnsRequestAction.domain | 
| DNS request domain suffix | service.action.dnsRequestAction.domainWithSuffix | 
| Network connection blocked | service.action.networkConnectionAction.blocked | 
| Network connection direction | service.action.networkConnectionAction.connectionDirection | 
| Network connection local port | service.action.networkConnectionAction.localPortDetails.port | 
| Network connection protocol | service.action.networkConnectionAction.protocol | 
| Network connection city | service.action.networkConnectionAction.remoteIpDetails.city.cityName | 
| Network connection country | service.action.networkConnectionAction.remoteIpDetails.country.countryName | 
| Network connection remote IPv4 address | service.action.networkConnectionAction.remoteIpDetails.ipAddressV4 | 
| Network connection remote IPv6 address | service.action.networkConnectionAction.remoteIpDetails.ipAddressV6 | 
| Network connection remote IP ASN ID | service.action.networkConnectionAction.remoteIpDetails.organization.asn | 
| Network connection remote IP ASN name | service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg | 
| Network connection remote port | service.action.networkConnectionAction.remotePortDetails.port | 
| Remote account affiliated | service.action.awsApiCallAction.remoteAccountDetails.affiliated | 
| Kubernetes API caller IPv4 address | service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV4 | 
| Kubernetes API caller IPv6 address | service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV6 | 
| Kubernetes namespace | service.action.kubernetesApiCallAction.namespace | 
| Kubernetes API caller ASN ID | service.action.kubernetesApiCallAction.remoteIpDetails.organization.asn | 
| Kubernetes API call request URI | service.action.kubernetesApiCallAction.requestUri | 
| Kubernetes API status code | service.action.kubernetesApiCallAction.statusCode | 
| Network connection local IPv4 address | service.action.networkConnectionAction.localIpDetails.ipAddressV4 | 
| Network connection local IPv6 address | service.action.networkConnectionAction.localIpDetails.ipAddressV6 | 
| Protocol | service.action.networkConnectionAction.protocol | 
| API call service name | service.action.awsApiCallAction.serviceName | 
| API caller account ID | service.action.awsApiCallAction.remoteAccountDetails.accountId | 
| Threat list name | service.additionalInfo.threatListName | 
| Resource role | service.resourceRole | 
| EKS cluster name | resource.eksClusterDetails.name | 
| Kubernetes workload name | resource.kubernetesDetails.kubernetesWorkloadDetails.name | 
| Kubernetes workload namespace | resource.kubernetesDetails.kubernetesWorkloadDetails.namespace | 
| Kubernetes user name | resource.kubernetesDetails.kubernetesUserDetails.username | 
| Kubernetes container image | resource.kubernetesDetails.kubernetesWorkloadDetails.containers.image | 
| Kubernetes container image prefix | resource.kubernetesDetails.kubernetesWorkloadDetails.containers.imagePrefix | 
| Scan ID | service.ebsVolumeScanDetails.scanId | 
| EBS volume scan threat name | service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.name | 
| S3 object scan threat name | service.malwareScanDetails.threats.name | 
| Threat severity | service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.severity | 
| File SHA | service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash | 
| ECS cluster name | resource.ecsClusterDetails.name | 
| ECS container image | resource.ecsClusterDetails.taskDetails.containers.image | 
| ECS task definition ARN | resource.ecsClusterDetails.taskDetails.definitionArn | 
| Standalone container image | resource.containerDetails.image | 
| Database Instance Id | resource.rdsDbInstanceDetails.dbInstanceIdentifier | 
| Database Cluster Id | resource.rdsDbInstanceDetails.dbClusterIdentifier | 
| Database Engine | resource.rdsDbInstanceDetails.engine | 
| Database user | resource.rdsDbUserDetails.user | 
| Executable SHA-256 | service.runtimeDetails.process.executableSha256 | 
| Process name | service.runtimeDetails.process.name | 
| Executable path | service.runtimeDetails.process.executablePath | 
| Lambda function name | resource.lambdaDetails.functionName | 
| Lambda function ARN | resource.lambdaDetails.functionArn | 
| Lambda function tag key | resource.lambdaDetails.tags.key | 
| Lambda function tag value | resource.lambdaDetails.tags.value | 
| DNS request domain | service.action.dnsRequestAction.domainWithSuffix | 

All other finding fields (listed below) are available as suppression rule filter criteria only (using [CreateFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateFilter.html) and [UpdateFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateFilter.html)). These fields are not supported by other API operations. Suppression rules that use these fields must be created or updated through the API. These fields can only be applied for filters with an `ARCHIVE` action.

**Note**  
The following fields accept timestamp values in Unix Epoch millisecond format (for example, `1262309025000` represents Friday, January 1, 2010 at 1:23:45 AM GMT):  
createdAt
updatedAt
service.eventFirstSeen
service.eventLastSeen
resource.instanceDetails.launchTime
resource.lambdaDetails.lastModifiedAt
resource.s3BucketDetails.createdAt
resource.eksClusterDetails.createdAt
resource.ecsClusterDetails.taskDetails.createdAt
resource.ecsClusterDetails.taskDetails.startedAt
service.ebsVolumeScanDetails.scanStartedAt
service.ebsVolumeScanDetails.scanCompletedAt
service.runtimeDetails.context.modifiedAt
service.runtimeDetails.context.modifyingProcess.startTime
service.runtimeDetails.context.modifyingProcess.lineage.startTime
service.runtimeDetails.context.targetProcess.startTime
service.runtimeDetails.context.targetProcess.lineage.startTime
service.runtimeDetails.process.startTime
service.runtimeDetails.process.lineage.startTime
service.detection.sequence.actors.session.createdTime
service.detection.sequence.signals.createdAt
service.detection.sequence.signals.updatedAt
service.detection.sequence.signals.firstSeenAt
service.detection.sequence.signals.lastSeenAt
service.detection.sequence.resources.data.s3Bucket.createdAt
service.detection.sequence.resources.data.ecsTask.createdAt
service.detection.sequence.resources.data.eksCluster.createdAt


| JSON field name | 
| --- | 
| arn | 
| associatedAttackSequenceArn | 
| createdAt | 
| partition | 
| resource.accessKeyDetails.userIdentity.accessKeyId | 
| resource.accessKeyDetails.userIdentity.accountId | 
| resource.accessKeyDetails.userIdentity.arn | 
| resource.accessKeyDetails.userIdentity.principalId | 
| resource.accessKeyDetails.userIdentity.sessionContext.attributes.mfaAuthenticated | 
| resource.accessKeyDetails.userIdentity.sessionContext.ec2RoleDelivery | 
| resource.accessKeyDetails.userIdentity.sessionContext.invokedBy | 
| resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.accountId | 
| resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.arn | 
| resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.principalId | 
| resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.type | 
| resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.userName | 
| resource.accessKeyDetails.userIdentity.sessionContext.sourceIdentity | 
| resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.attributes | 
| resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.federatedProvider | 
| resource.accessKeyDetails.userIdentity.type | 
| resource.accessKeyDetails.userIdentity.userName | 
| resource.bedrockGuardrailDetails.guardrailArn | 
| resource.bedrockGuardrailDetails.guardrailVersion | 
| resource.containerDetails.containerRuntime | 
| resource.containerDetails.imagePrefix | 
| resource.containerDetails.securityContext.allowPrivilegeEscalation | 
| resource.containerDetails.securityContext.privileged | 
| resource.containerDetails.volumeMounts.mountPath | 
| resource.containerDetails.volumeMounts.name | 
| resource.ebsVolumeDetails.scannedVolumeDetails.deviceName | 
| resource.ebsVolumeDetails.scannedVolumeDetails.encryptionType | 
| resource.ebsVolumeDetails.scannedVolumeDetails.kmsKeyArn | 
| resource.ebsVolumeDetails.scannedVolumeDetails.snapshotArn | 
| resource.ebsVolumeDetails.scannedVolumeDetails.volumeArn | 
| resource.ebsVolumeDetails.scannedVolumeDetails.volumeSizeInGB | 
| resource.ebsVolumeDetails.scannedVolumeDetails.volumeType | 
| resource.ebsVolumeDetails.skippedVolumeDetails.deviceName | 
| resource.ebsVolumeDetails.skippedVolumeDetails.encryptionType | 
| resource.ebsVolumeDetails.skippedVolumeDetails.kmsKeyArn | 
| resource.ebsVolumeDetails.skippedVolumeDetails.snapshotArn | 
| resource.ebsVolumeDetails.skippedVolumeDetails.volumeArn | 
| resource.ebsVolumeDetails.skippedVolumeDetails.volumeSizeInGB | 
| resource.ebsVolumeDetails.skippedVolumeDetails.volumeType | 
| resource.ecsClusterDetails.activeServicesCount | 
| resource.ecsClusterDetails.arn | 
| resource.ecsClusterDetails.registeredContainerInstancesCount | 
| resource.ecsClusterDetails.runningTasksCount | 
| resource.ecsClusterDetails.status | 
| resource.ecsClusterDetails.tags.key | 
| resource.ecsClusterDetails.tags.value | 
| resource.ecsClusterDetails.taskDetails.arn | 
| resource.ecsClusterDetails.taskDetails.containers.containerRuntime | 
| resource.ecsClusterDetails.taskDetails.containers.id | 
| resource.ecsClusterDetails.taskDetails.containers.imagePrefix | 
| resource.ecsClusterDetails.taskDetails.containers.name | 
| resource.ecsClusterDetails.taskDetails.containers.securityContext.allowPrivilegeEscalation | 
| resource.ecsClusterDetails.taskDetails.containers.securityContext.privileged | 
| resource.ecsClusterDetails.taskDetails.containers.volumeMounts.mountPath | 
| resource.ecsClusterDetails.taskDetails.containers.volumeMounts.name | 
| resource.ecsClusterDetails.taskDetails.createdAt | 
| resource.ecsClusterDetails.taskDetails.group | 
| resource.ecsClusterDetails.taskDetails.launchType | 
| resource.ecsClusterDetails.taskDetails.startedAt | 
| resource.ecsClusterDetails.taskDetails.startedBy | 
| resource.ecsClusterDetails.taskDetails.tags.key | 
| resource.ecsClusterDetails.taskDetails.tags.value | 
| resource.ecsClusterDetails.taskDetails.version | 
| resource.ecsClusterDetails.taskDetails.volumes.hostPath.path | 
| resource.ecsClusterDetails.taskDetails.volumes.name | 
| resource.eksClusterDetails.arn | 
| resource.eksClusterDetails.createdAt | 
| resource.eksClusterDetails.status | 
| resource.eksClusterDetails.tags.key | 
| resource.eksClusterDetails.tags.value | 
| resource.eksClusterDetails.vpcId | 
| resource.instanceDetails.iamInstanceProfile.arn | 
| resource.instanceDetails.instanceState | 
| resource.instanceDetails.instanceType | 
| resource.instanceDetails.launchTime | 
| resource.instanceDetails.networkInterfaces.networkInterfaceId | 
| resource.instanceDetails.networkInterfaces.privateDnsName | 
| resource.instanceDetails.networkInterfaces.privateIpAddress | 
| resource.instanceDetails.networkInterfaces.privateIpAddresses.privateDnsName | 
| resource.instanceDetails.platform | 
| resource.instanceDetails.productCodes.productCodeId | 
| resource.instanceDetails.productCodes.productCodeType | 
| resource.kubernetesDetails.kubernetesUserDetails.groups | 
| resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.groups | 
| resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.username | 
| resource.kubernetesDetails.kubernetesUserDetails.sessionName | 
| resource.kubernetesDetails.kubernetesUserDetails.uid | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.containers.containerRuntime | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.containers.id | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.containers.name | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.allowPrivilegeEscalation | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.privileged | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.mountPath | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.name | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.hostIpc | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.hostNetwork | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.hostPid | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.serviceAccountName | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.type | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.uid | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.hostPath.path | 
| resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.name | 
| resource.lambdaDetails.description | 
| resource.lambdaDetails.lastModifiedAt | 
| resource.lambdaDetails.revisionId | 
| resource.lambdaDetails.vpcConfig.securityGroups.groupId | 
| resource.lambdaDetails.vpcConfig.securityGroups.groupName | 
| resource.lambdaDetails.vpcConfig.subnetIds | 
| resource.lambdaDetails.vpcConfig.vpcId | 
| resource.rdsDbInstanceDetails.dbInstanceArn | 
| resource.rdsDbInstanceDetails.dbiResourceId | 
| resource.rdsDbInstanceDetails.dbSecurityGroups.name | 
| resource.rdsDbInstanceDetails.dbSecurityGroups.status | 
| resource.rdsDbInstanceDetails.engineVersion | 
| resource.rdsDbInstanceDetails.iamDatabaseAuthenticationEnabled | 
| resource.rdsDbInstanceDetails.publiclyAccessible | 
| resource.rdsDbInstanceDetails.vpcId | 
| resource.rdsDbInstanceDetails.vpcSecurityGroups.status | 
| resource.rdsDbInstanceDetails.vpcSecurityGroups.vpcSecurityGroupId | 
| resource.rdsDbUserDetails.application | 
| resource.rdsDbUserDetails.authMethod | 
| resource.rdsDbUserDetails.database | 
| resource.rdsDbUserDetails.ssl | 
| resource.rdsLimitlessDbDetails.dbClusterIdentifier | 
| resource.rdsLimitlessDbDetails.dbShardGroupArn | 
| resource.rdsLimitlessDbDetails.dbShardGroupIdentifier | 
| resource.rdsLimitlessDbDetails.dbShardGroupResourceId | 
| resource.rdsLimitlessDbDetails.engine | 
| resource.rdsLimitlessDbDetails.engineVersion | 
| resource.rdsLimitlessDbDetails.tags.key | 
| resource.rdsLimitlessDbDetails.tags.value | 
| resource.s3BucketDetails.arn | 
| resource.s3BucketDetails.createdAt | 
| resource.s3BucketDetails.defaultServerSideEncryption.encryptionType | 
| resource.s3BucketDetails.defaultServerSideEncryption.kmsMasterKeyArn | 
| resource.s3BucketDetails.owner.id | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicAcls | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicPolicy | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.ignorePublicAcls | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.restrictPublicBuckets | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicReadAccess | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicWriteAccess | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicAcls | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicPolicy | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.ignorePublicAcls | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.restrictPublicBuckets | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicReadAccess | 
| resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicWriteAccess | 
| resource.s3BucketDetails.s3ObjectDetails.eTag | 
| resource.s3BucketDetails.s3ObjectDetails.hash | 
| resource.s3BucketDetails.s3ObjectDetails.key | 
| resource.s3BucketDetails.s3ObjectDetails.objectArn | 
| resource.s3BucketDetails.s3ObjectDetails.versionId | 
| schemaVersion | 
| service.action.awsApiCallAction.domainDetails.domain | 
| service.action.awsApiCallAction.remoteIpDetails.country.countryCode | 
| service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat | 
| service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon | 
| service.action.awsApiCallAction.remoteIpDetails.organization.isp | 
| service.action.awsApiCallAction.remoteIpDetails.organization.org | 
| service.action.awsApiCallAction.userAgent | 
| service.action.dnsRequestAction.blocked | 
| service.action.dnsRequestAction.protocol | 
| service.action.kubernetesApiCallAction.parameters | 
| service.action.kubernetesApiCallAction.remoteIpDetails.country.countryCode | 
| service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lat | 
| service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lon | 
| service.action.kubernetesApiCallAction.resource | 
| service.action.kubernetesApiCallAction.resourceName | 
| service.action.kubernetesApiCallAction.sourceIPs | 
| service.action.kubernetesApiCallAction.subresource | 
| service.action.kubernetesApiCallAction.userAgent | 
| service.action.kubernetesApiCallAction.verb | 
| service.action.kubernetesPermissionCheckedDetails.allowed | 
| service.action.kubernetesPermissionCheckedDetails.namespace | 
| service.action.kubernetesPermissionCheckedDetails.resource | 
| service.action.kubernetesPermissionCheckedDetails.verb | 
| service.action.kubernetesRoleBindingDetails.kind | 
| service.action.kubernetesRoleBindingDetails.name | 
| service.action.kubernetesRoleBindingDetails.roleRefKind | 
| service.action.kubernetesRoleBindingDetails.roleRefName | 
| service.action.kubernetesRoleBindingDetails.uid | 
| service.action.kubernetesRoleDetails.kind | 
| service.action.kubernetesRoleDetails.name | 
| service.action.kubernetesRoleDetails.uid | 
| service.action.networkConnectionAction.localNetworkInterface | 
| service.action.networkConnectionAction.localPortDetails.portName | 
| service.action.networkConnectionAction.remoteIpDetails.country.countryCode | 
| service.action.networkConnectionAction.remoteIpDetails.geoLocation.lat | 
| service.action.networkConnectionAction.remoteIpDetails.geoLocation.lon | 
| service.action.networkConnectionAction.remoteIpDetails.organization.isp | 
| service.action.networkConnectionAction.remoteIpDetails.organization.org | 
| service.action.networkConnectionAction.remotePortDetails.portName | 
| service.action.portProbeAction.blocked | 
| service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV4 | 
| service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV6 | 
| service.action.portProbeAction.portProbeDetails.localPortDetails.port | 
| service.action.portProbeAction.portProbeDetails.localPortDetails.portName | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.city.cityName | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryCode | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryName | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lat | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lon | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV4 | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV6 | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asn | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asnOrg | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.isp | 
| service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.org | 
| service.action.rdsLoginAttemptAction.loginAttributes.application | 
| service.action.rdsLoginAttemptAction.loginAttributes.failedLoginAttempts | 
| service.action.rdsLoginAttemptAction.loginAttributes.successfulLoginAttempts | 
| service.action.rdsLoginAttemptAction.loginAttributes.user | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.city.cityName | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryCode | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryName | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lat | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lon | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV4 | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV6 | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asn | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asnOrg | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.organization.isp | 
| service.action.rdsLoginAttemptAction.remoteIpDetails.organization.org | 
| service.additionalInfo.agentDetails.agentId | 
| service.additionalInfo.agentDetails.agentVersion | 
| service.additionalInfo.anomalies.anomalousAPIs | 
| service.additionalInfo.authenticationMethod | 
| service.additionalInfo.averagePacketSizeIn | 
| service.additionalInfo.averagePacketSizeOut | 
| service.additionalInfo.context | 
| service.additionalInfo.domain | 
| service.additionalInfo.inBytes | 
| service.additionalInfo.localNetworkInterfaceOwner | 
| service.additionalInfo.localPort | 
| service.additionalInfo.outBytes | 
| service.additionalInfo.packetsIn | 
| service.additionalInfo.packetsOut | 
| service.additionalInfo.policyArn | 
| service.additionalInfo.policyName | 
| service.additionalInfo.remotePort | 
| service.additionalInfo.sample | 
| service.additionalInfo.scannedPort | 
| service.additionalInfo.threatFileSha256 | 
| service.additionalInfo.threatName | 
| service.additionalInfo.totalBytesIn | 
| service.additionalInfo.totalBytesOut | 
| service.additionalInfo.type | 
| service.additionalInfo.unusual.asnOrg | 
| service.additionalInfo.unusual.port | 
| service.additionalInfo.unusualProtocol | 
| service.additionalInfo.userAgent.fullUserAgent | 
| service.additionalInfo.userAgent.userAgentCategory | 
| service.additionalInfo.value | 
| service.additionalInfo.vpcOwnerAccountId | 
| service.count | 
| service.detection.sequence.actors.id | 
| service.detection.sequence.actors.process.name | 
| service.detection.sequence.actors.process.path | 
| service.detection.sequence.actors.process.sha256 | 
| service.detection.sequence.actors.session.createdTime | 
| service.detection.sequence.actors.session.issuer | 
| service.detection.sequence.actors.session.mfaStatus | 
| service.detection.sequence.actors.session.uid | 
| service.detection.sequence.actors.user.account.account | 
| service.detection.sequence.actors.user.account.uid | 
| service.detection.sequence.actors.user.credentialUid | 
| service.detection.sequence.actors.user.name | 
| service.detection.sequence.actors.user.type | 
| service.detection.sequence.actors.user.uid | 
| service.detection.sequence.additionalSequenceTypes | 
| service.detection.sequence.description | 
| service.detection.sequence.endpoints.autonomousSystem.name | 
| service.detection.sequence.endpoints.autonomousSystem.number | 
| service.detection.sequence.endpoints.connection.direction | 
| service.detection.sequence.endpoints.domain | 
| service.detection.sequence.endpoints.id | 
| service.detection.sequence.endpoints.ip | 
| service.detection.sequence.endpoints.location.city | 
| service.detection.sequence.endpoints.location.country | 
| service.detection.sequence.endpoints.location.lat | 
| service.detection.sequence.endpoints.location.lon | 
| service.detection.sequence.endpoints.port | 
| service.detection.sequence.resources.accountId | 
| service.detection.sequence.resources.cloudPartition | 
| service.detection.sequence.resources.data.accessKey.principalId | 
| service.detection.sequence.resources.data.accessKey.userName | 
| service.detection.sequence.resources.data.accessKey.userType | 
| service.detection.sequence.resources.data.autoscalingAutoScalingGroup.ec2InstanceUids | 
| service.detection.sequence.resources.data.cloudformationStack.ec2InstanceUids | 
| service.detection.sequence.resources.data.container.image | 
| service.detection.sequence.resources.data.container.imageUid | 
| service.detection.sequence.resources.data.ec2Image.ec2InstanceUids | 
| service.detection.sequence.resources.data.ec2Instance.availabilityZone | 
| service.detection.sequence.resources.data.ec2Instance.ec2NetworkInterfaceUids | 
| service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.arn | 
| service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.id | 
| service.detection.sequence.resources.data.ec2Instance.imageDescription | 
| service.detection.sequence.resources.data.ec2Instance.instanceState | 
| service.detection.sequence.resources.data.ec2Instance.instanceType | 
| service.detection.sequence.resources.data.ec2Instance.outpostArn | 
| service.detection.sequence.resources.data.ec2Instance.platform | 
| service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeId | 
| service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeType | 
| service.detection.sequence.resources.data.ec2LaunchTemplate.ec2InstanceUids | 
| service.detection.sequence.resources.data.ec2LaunchTemplate.version | 
| service.detection.sequence.resources.data.ec2NetworkInterface.ipv6Addresses | 
| service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateDnsName | 
| service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateIpAddress | 
| service.detection.sequence.resources.data.ec2NetworkInterface.publicIp | 
| service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupId | 
| service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupName | 
| service.detection.sequence.resources.data.ec2NetworkInterface.subNetId | 
| service.detection.sequence.resources.data.ec2NetworkInterface.vpcId | 
| service.detection.sequence.resources.data.ec2Vpc.ec2InstanceUids | 
| service.detection.sequence.resources.data.ecsCluster.ec2InstanceUids | 
| service.detection.sequence.resources.data.ecsCluster.status | 
| service.detection.sequence.resources.data.ecsTask.containerUids | 
| service.detection.sequence.resources.data.ecsTask.createdAt | 
| service.detection.sequence.resources.data.ecsTask.launchType | 
| service.detection.sequence.resources.data.ecsTask.taskDefinitionArn | 
| service.detection.sequence.resources.data.eksCluster.arn | 
| service.detection.sequence.resources.data.eksCluster.createdAt | 
| service.detection.sequence.resources.data.eksCluster.ec2InstanceUids | 
| service.detection.sequence.resources.data.eksCluster.status | 
| service.detection.sequence.resources.data.eksCluster.vpcId | 
| service.detection.sequence.resources.data.iamInstanceProfile.ec2InstanceUids | 
| service.detection.sequence.resources.data.iamInstanceProfile.id | 
| service.detection.sequence.resources.data.kubernetesWorkload.containerUids | 
| service.detection.sequence.resources.data.kubernetesWorkload.namespace | 
| service.detection.sequence.resources.data.kubernetesWorkload.type | 
| service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclAccess | 
| service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclIgnoreBehavior | 
| service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicBucketRestrictBehavior | 
| service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicPolicyAccess | 
| service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclAccess | 
| service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclIgnoreBehavior | 
| service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicBucketRestrictBehavior | 
| service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicPolicyAccess | 
| service.detection.sequence.resources.data.s3Bucket.createdAt | 
| service.detection.sequence.resources.data.s3Bucket.effectivePermission | 
| service.detection.sequence.resources.data.s3Bucket.encryptionKeyArn | 
| service.detection.sequence.resources.data.s3Bucket.encryptionType | 
| service.detection.sequence.resources.data.s3Bucket.ownerId | 
| service.detection.sequence.resources.data.s3Bucket.publicReadAccess | 
| service.detection.sequence.resources.data.s3Bucket.publicWriteAccess | 
| service.detection.sequence.resources.data.s3Bucket.s3ObjectUids | 
| service.detection.sequence.resources.data.s3Object.eTag | 
| service.detection.sequence.resources.data.s3Object.key | 
| service.detection.sequence.resources.data.s3Object.versionId | 
| service.detection.sequence.resources.name | 
| service.detection.sequence.resources.region | 
| service.detection.sequence.resources.resourceType | 
| service.detection.sequence.resources.service | 
| service.detection.sequence.resources.tags.key | 
| service.detection.sequence.resources.tags.value | 
| service.detection.sequence.resources.uid | 
| service.detection.sequence.sequenceIndicators.key | 
| service.detection.sequence.sequenceIndicators.title | 
| service.detection.sequence.sequenceIndicators.values | 
| service.detection.sequence.signals.actorIds | 
| service.detection.sequence.signals.count | 
| service.detection.sequence.signals.createdAt | 
| service.detection.sequence.signals.description | 
| service.detection.sequence.signals.endpointIds | 
| service.detection.sequence.signals.firstSeenAt | 
| service.detection.sequence.signals.lastSeenAt | 
| service.detection.sequence.signals.name | 
| service.detection.sequence.signals.resourceUids | 
| service.detection.sequence.signals.severity | 
| service.detection.sequence.signals.signalIndicators.key | 
| service.detection.sequence.signals.signalIndicators.title | 
| service.detection.sequence.signals.signalIndicators.values | 
| service.detection.sequence.signals.type | 
| service.detection.sequence.signals.uid | 
| service.detection.sequence.signals.updatedAt | 
| service.detection.sequence.uid | 
| service.detectorId | 
| service.ebsVolumeScanDetails.scanCompletedAt | 
| service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.count | 
| service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.severity | 
| service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.threatName | 
| service.ebsVolumeScanDetails.scanDetections.scannedItemCount.files | 
| service.ebsVolumeScanDetails.scanDetections.scannedItemCount.totalGb | 
| service.ebsVolumeScanDetails.scanDetections.scannedItemCount.volumes | 
| service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.itemCount | 
| service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.shortened | 
| service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.fileName | 
| service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.filePath | 
| service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.volumeArn | 
| service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.itemCount | 
| service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.uniqueThreatNameCount | 
| service.ebsVolumeScanDetails.scanDetections.threatsDetectedItemCount.files | 
| service.ebsVolumeScanDetails.scanStartedAt | 
| service.ebsVolumeScanDetails.scanType | 
| service.ebsVolumeScanDetails.sources | 
| service.eventFirstSeen | 
| service.eventLastSeen | 
| service.malwareScanDetails.scanCategory | 
| service.malwareScanDetails.scanConfiguration.incrementalScanDetails.baselineResourceArn | 
| service.malwareScanDetails.scanConfiguration.triggerType | 
| service.malwareScanDetails.threats.count | 
| service.malwareScanDetails.threats.hash | 
| service.malwareScanDetails.threats.itemDetails.additionalInfo.deviceName | 
| service.malwareScanDetails.threats.itemDetails.additionalInfo.versionId | 
| service.malwareScanDetails.threats.itemDetails.hash | 
| service.malwareScanDetails.threats.itemDetails.itemPath | 
| service.malwareScanDetails.threats.itemDetails.resourceArn | 
| service.malwareScanDetails.threats.itemPaths.hash | 
| service.malwareScanDetails.threats.itemPaths.nestedItemPath | 
| service.malwareScanDetails.threats.source | 
| service.malwareScanDetails.uniqueThreatCount | 
| service.runtimeDetails.context.addressFamily | 
| service.runtimeDetails.context.commandLineExample | 
| service.runtimeDetails.context.fileSystemType | 
| service.runtimeDetails.context.flags | 
| service.runtimeDetails.context.ianaProtocolNumber | 
| service.runtimeDetails.context.ldPreloadValue | 
| service.runtimeDetails.context.libraryPath | 
| service.runtimeDetails.context.memoryRegions | 
| service.runtimeDetails.context.modifiedAt | 
| service.runtimeDetails.context.modifyingProcess.euid | 
| service.runtimeDetails.context.modifyingProcess.executablePath | 
| service.runtimeDetails.context.modifyingProcess.executableSha256 | 
| service.runtimeDetails.context.modifyingProcess.lineage.euid | 
| service.runtimeDetails.context.modifyingProcess.lineage.executablePath | 
| service.runtimeDetails.context.modifyingProcess.lineage.name | 
| service.runtimeDetails.context.modifyingProcess.lineage.namespacePid | 
| service.runtimeDetails.context.modifyingProcess.lineage.parentUuid | 
| service.runtimeDetails.context.modifyingProcess.lineage.pid | 
| service.runtimeDetails.context.modifyingProcess.lineage.startTime | 
| service.runtimeDetails.context.modifyingProcess.lineage.userId | 
| service.runtimeDetails.context.modifyingProcess.lineage.uuid | 
| service.runtimeDetails.context.modifyingProcess.name | 
| service.runtimeDetails.context.modifyingProcess.namespacePid | 
| service.runtimeDetails.context.modifyingProcess.parentUuid | 
| service.runtimeDetails.context.modifyingProcess.pid | 
| service.runtimeDetails.context.modifyingProcess.pwd | 
| service.runtimeDetails.context.modifyingProcess.startTime | 
| service.runtimeDetails.context.modifyingProcess.user | 
| service.runtimeDetails.context.modifyingProcess.userId | 
| service.runtimeDetails.context.modifyingProcess.uuid | 
| service.runtimeDetails.context.mountSource | 
| service.runtimeDetails.context.mountTarget | 
| service.runtimeDetails.context.relatedFilePaths | 
| service.runtimeDetails.context.releaseAgentPath | 
| service.runtimeDetails.context.runcBinaryPath | 
| service.runtimeDetails.context.scriptPath | 
| service.runtimeDetails.context.serviceName | 
| service.runtimeDetails.context.shellHistoryFilePath | 
| service.runtimeDetails.context.socketPath | 
| service.runtimeDetails.context.targetProcess.euid | 
| service.runtimeDetails.context.targetProcess.executablePath | 
| service.runtimeDetails.context.targetProcess.executableSha256 | 
| service.runtimeDetails.context.targetProcess.lineage.euid | 
| service.runtimeDetails.context.targetProcess.lineage.executablePath | 
| service.runtimeDetails.context.targetProcess.lineage.name | 
| service.runtimeDetails.context.targetProcess.lineage.namespacePid | 
| service.runtimeDetails.context.targetProcess.lineage.parentUuid | 
| service.runtimeDetails.context.targetProcess.lineage.pid | 
| service.runtimeDetails.context.targetProcess.lineage.startTime | 
| service.runtimeDetails.context.targetProcess.lineage.userId | 
| service.runtimeDetails.context.targetProcess.lineage.uuid | 
| service.runtimeDetails.context.targetProcess.name | 
| service.runtimeDetails.context.targetProcess.namespacePid | 
| service.runtimeDetails.context.targetProcess.parentUuid | 
| service.runtimeDetails.context.targetProcess.pid | 
| service.runtimeDetails.context.targetProcess.pwd | 
| service.runtimeDetails.context.targetProcess.startTime | 
| service.runtimeDetails.context.targetProcess.user | 
| service.runtimeDetails.context.targetProcess.userId | 
| service.runtimeDetails.context.targetProcess.uuid | 
| service.runtimeDetails.context.threatFilePath | 
| service.runtimeDetails.context.toolCategory | 
| service.runtimeDetails.context.toolName | 
| service.runtimeDetails.process.euid | 
| service.runtimeDetails.process.lineage.euid | 
| service.runtimeDetails.process.lineage.executablePath | 
| service.runtimeDetails.process.lineage.name | 
| service.runtimeDetails.process.lineage.namespacePid | 
| service.runtimeDetails.process.lineage.parentUuid | 
| service.runtimeDetails.process.lineage.pid | 
| service.runtimeDetails.process.lineage.startTime | 
| service.runtimeDetails.process.lineage.userId | 
| service.runtimeDetails.process.lineage.uuid | 
| service.runtimeDetails.process.namespacePid | 
| service.runtimeDetails.process.parentUuid | 
| service.runtimeDetails.process.pid | 
| service.runtimeDetails.process.pwd | 
| service.runtimeDetails.process.startTime | 
| service.runtimeDetails.process.user | 
| service.runtimeDetails.process.userId | 
| service.runtimeDetails.process.uuid | 
| service.userFeedback | 