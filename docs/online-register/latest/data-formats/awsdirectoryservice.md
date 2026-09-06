

# Data retrieval APIs for AWS Directory Service
<a name="awsdirectoryservice"></a>

AWS Directory Service provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="ds-CheckAlias"></a>[CheckAlias](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html) | Verify that the alias is available for use | Read | 
| <a name="ds-DescribeADAssessment"></a>[DescribeADAssessment](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeADAssessment.html) | Describe a directory assessment | Read | 
| <a name="ds-DescribeCAEnrollmentPolicy"></a>[DescribeCAEnrollmentPolicy](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeCAEnrollmentPolicy.html) | Describe the ca enrollment status of a specified directory | Read | 
| <a name="ds-DescribeCertificate"></a>[DescribeCertificate](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeCertificate.html) | Display information about the certificate registered for a secured LDAP connection | Read | 
| <a name="ds-DescribeClientAuthenticationSettings"></a>[DescribeClientAuthenticationSettings](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeClientAuthenticationSettings.html) | Retrieve information about the type of client authentication for the specified directory, if the type is specified. If no type is specified, information about all client authentication types that are supported for the specified directory is retrieved. Currently, only SmartCard is supported | Read | 
| <a name="ds-DescribeConditionalForwarders"></a>[DescribeConditionalForwarders](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeConditionalForwarders.html) | Obtain information about the conditional forwarders for this account | Read | 
| <a name="ds-DescribeDirectories"></a>[DescribeDirectories](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDirectories.html) | Obtain information about the directories that belong to this account | List | 
| <a name="ds-DescribeDirectoryDataAccess"></a>[DescribeDirectoryDataAccess](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDirectoryDataAccess.html) | Describe the Directory Service Data API status for the specified directory | Read | 
| <a name="ds-DescribeDomainControllers"></a>[DescribeDomainControllers](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDomainControllers.html) | Provide information about any domain controllers in your directory | Read | 
| <a name="ds-DescribeEventTopics"></a>[DescribeEventTopics](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeEventTopics.html) | Obtain information about which SNS topics receive status messages from the specified directory | Read | 
| <a name="ds-DescribeHybridADUpdate"></a>[DescribeHybridADUpdate](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeHybridADUpdate.html) | Describe the updates of a specified hybrid directory | Read | 
| <a name="ds-DescribeLDAPSSettings"></a>[DescribeLDAPSSettings](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeLDAPSSettings.html) | Describe the status of LDAP security for the specified directory | Read | 
| <a name="ds-DescribeRegions"></a>[DescribeRegions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeRegions.html) | Provide information about the Regions that are configured for multi-Region replication | Read | 
| <a name="ds-DescribeSettings"></a>[DescribeSettings](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSettings.html) | Retrieve information about the configurable settings for the specified directory | Read | 
| <a name="ds-DescribeSharedDirectories"></a>[DescribeSharedDirectories](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSharedDirectories.html) | Return the shared directories in your account | Read | 
| <a name="ds-DescribeSnapshots"></a>[DescribeSnapshots](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSnapshots.html) | Obtain information about the directory snapshots that belong to this account | Read | 
| <a name="ds-DescribeTrusts"></a>[DescribeTrusts](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeTrusts.html) | Obtain information about the trust relationships for this account | Read | 
| <a name="ds-DescribeUpdateDirectory"></a>[DescribeUpdateDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeUpdateDirectory.html) | Describe the updates of a directory for a particular update type | Read | 
| <a name="ds-GetAuthorizedApplicationDetails"></a>[GetAuthorizedApplicationDetails](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html) | Retrieve the details of the authorized applications on a directory | Read | 
| <a name="ds-GetDirectoryLimits"></a>[GetDirectoryLimits](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_GetDirectoryLimits.html) | Obtain directory limit information for the current region | Read | 
| <a name="ds-GetSnapshotLimits"></a>[GetSnapshotLimits](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_GetSnapshotLimits.html) | Obtain the manual snapshot limits for a directory | Read | 
| <a name="ds-ListADAssessments"></a>[ListADAssessments](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListADAssessments.html) | List directory assessments | List | 
| <a name="ds-ListAuthorizedApplications"></a>[ListAuthorizedApplications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html) | Obtain the AWS applications authorized for a directory | Read | 
| <a name="ds-ListCertificates"></a>[ListCertificates](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListCertificates.html) | List all the certificates registered for a secured LDAP connection, for the specified directory | List | 
| <a name="ds-ListIpRoutes"></a>[ListIpRoutes](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListIpRoutes.html) | List the address blocks that you have added to a directory | Read | 
| <a name="ds-ListLogSubscriptions"></a>[ListLogSubscriptions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListLogSubscriptions.html) | List the active log subscriptions for the AWS account | Read | 
| <a name="ds-ListSchemaExtensions"></a>[ListSchemaExtensions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListSchemaExtensions.html) | List all schema extensions applied to a Microsoft AD Directory | List | 
| <a name="ds-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListTagsForResource.html) | List all tags on an Amazon Directory Services directory | Read | 
| <a name="ds-VerifyTrust"></a>[VerifyTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_VerifyTrust.html) | Verify a trust relationship between your Microsoft AD in the AWS cloud and an external domain | Read | 