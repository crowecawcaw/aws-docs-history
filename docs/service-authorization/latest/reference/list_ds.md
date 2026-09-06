

# Actions, resources, and condition keys for AWS Directory Service
<a name="list_ds"></a>

AWS Directory Service (service prefix: `ds`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/directoryservice/latest/devguide/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_auth_access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ds/ds.json) for this service.

**Topics**
+ [API operations defined by AWS Directory Service](#list_ds-operations)
+ [Actions defined by AWS Directory Service](#list_ds-actions-as-permissions)
+ [Permission-only actions for AWS Directory Service](#list_ds-permission-only-actions)
+ [Resource types defined by AWS Directory Service](#list_ds-resources-for-iam-policies)
+ [Condition keys for AWS Directory Service](#list_ds-policy-keys)

## API operations defined by AWS Directory Service
<a name="list_ds-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ds-actions-as-permissions).




- **   AcceptSharedDirectory  **
  - **IAM action:**  [ds:AcceptSharedDirectory](#list_ds-action-AcceptSharedDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddIpRoutes  **
  - **IAM action:**  [ds:AddIpRoutes](#list_ds-action-AddIpRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddRegion  **
  - **IAM action:**  [ds:AddRegion](#list_ds-action-AddRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTagsToResource  **
  - **IAM action:**  [ds:AddTagsToResource](#list_ds-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CancelSchemaExtension  **
  - **IAM action:**  [ds:CancelSchemaExtension](#list_ds-action-CancelSchemaExtension) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConnectDirectory  **
  - **IAM action:**  [ds:AddTagsToResource](#list_ds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ds:ConnectDirectory](#list_ds-action-ConnectDirectory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAlias  **
  - **IAM action:**  [ds:CreateAlias](#list_ds-action-CreateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateComputer  **
  - **IAM action:**  [ds:CreateComputer](#list_ds-action-CreateComputer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConditionalForwarder  **
  - **IAM action:**  [ds:CreateConditionalForwarder](#list_ds-action-CreateConditionalForwarder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDirectory  **
  - **IAM action:**  [ds:AddTagsToResource](#list_ds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ds:CreateDirectory](#list_ds-action-CreateDirectory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateHybridAD  **
  - **IAM action:**  [ds:AddTagsToResource](#list_ds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ds:CreateHybridAD](#list_ds-action-CreateHybridAD)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateLogSubscription  **
  - **IAM action:**  [ds:CreateLogSubscription](#list_ds-action-CreateLogSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMicrosoftAD  **
  - **IAM action:**  [ds:AddTagsToResource](#list_ds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ds:CreateMicrosoftAD](#list_ds-action-CreateMicrosoftAD)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSnapshot  **
  - **IAM action:**  [ds:CreateSnapshot](#list_ds-action-CreateSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTrust  **
  - **IAM action:**  [ds:CreateTrust](#list_ds-action-CreateTrust) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteADAssessment  **
  - **IAM action:**  [ds:DeleteADAssessment](#list_ds-action-DeleteADAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConditionalForwarder  **
  - **IAM action:**  [ds:DeleteConditionalForwarder](#list_ds-action-DeleteConditionalForwarder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectory  **
  - **IAM action:**  [ds:DeleteDirectory](#list_ds-action-DeleteDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLogSubscription  **
  - **IAM action:**  [ds:DeleteLogSubscription](#list_ds-action-DeleteLogSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshot  **
  - **IAM action:**  [ds:DeleteSnapshot](#list_ds-action-DeleteSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrust  **
  - **IAM action:**  [ds:DeleteTrust](#list_ds-action-DeleteTrust) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterCertificate  **
  - **IAM action:**  [ds:DeregisterCertificate](#list_ds-action-DeregisterCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterEventTopic  **
  - **IAM action:**  [ds:DeregisterEventTopic](#list_ds-action-DeregisterEventTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeADAssessment  **
  - **IAM action:**  [ds:DescribeADAssessment](#list_ds-action-DescribeADAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCAEnrollmentPolicy  **
  - **IAM action:**  [ds:DescribeCAEnrollmentPolicy](#list_ds-action-DescribeCAEnrollmentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCertificate  **
  - **IAM action:**  [ds:DescribeCertificate](#list_ds-action-DescribeCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClientAuthenticationSettings  **
  - **IAM action:**  [ds:DescribeClientAuthenticationSettings](#list_ds-action-DescribeClientAuthenticationSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConditionalForwarders  **
  - **IAM action:**  [ds:DescribeConditionalForwarders](#list_ds-action-DescribeConditionalForwarders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDirectories  **
  - **IAM action:**  [ds:DescribeDirectories](#list_ds-action-DescribeDirectories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDirectoryDataAccess  **
  - **IAM action:**  [ds:DescribeDirectoryDataAccess](#list_ds-action-DescribeDirectoryDataAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomainControllers  **
  - **IAM action:**  [ds:DescribeDomainControllers](#list_ds-action-DescribeDomainControllers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventTopics  **
  - **IAM action:**  [ds:DescribeEventTopics](#list_ds-action-DescribeEventTopics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHybridADUpdate  **
  - **IAM action:**  [ds:DescribeHybridADUpdate](#list_ds-action-DescribeHybridADUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLDAPSSettings  **
  - **IAM action:**  [ds:DescribeLDAPSSettings](#list_ds-action-DescribeLDAPSSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegions  **
  - **IAM action:**  [ds:DescribeRegions](#list_ds-action-DescribeRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSettings  **
  - **IAM action:**  [ds:DescribeSettings](#list_ds-action-DescribeSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSharedDirectories  **
  - **IAM action:**  [ds:DescribeSharedDirectories](#list_ds-action-DescribeSharedDirectories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshots  **
  - **IAM action:**  [ds:DescribeSnapshots](#list_ds-action-DescribeSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrusts  **
  - **IAM action:**  [ds:DescribeTrusts](#list_ds-action-DescribeTrusts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUpdateDirectory  **
  - **IAM action:**  [ds:DescribeUpdateDirectory](#list_ds-action-DescribeUpdateDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableCAEnrollmentPolicy  **
  - **IAM action:**  [ds:DisableCAEnrollmentPolicy](#list_ds-action-DisableCAEnrollmentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableClientAuthentication  **
  - **IAM action:**  [ds:DisableClientAuthentication](#list_ds-action-DisableClientAuthentication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableDirectoryDataAccess  **
  - **IAM action:**  [ds:DisableDirectoryDataAccess](#list_ds-action-DisableDirectoryDataAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableLDAPS  **
  - **IAM action:**  [ds:DisableLDAPS](#list_ds-action-DisableLDAPS) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableRadius  **
  - **IAM action:**  [ds:DisableRadius](#list_ds-action-DisableRadius) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableSso  **
  - **IAM action:**  [ds:DisableSso](#list_ds-action-DisableSso) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableCAEnrollmentPolicy  **
  - **IAM action:**  [ds:EnableCAEnrollmentPolicy](#list_ds-action-EnableCAEnrollmentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableClientAuthentication  **
  - **IAM action:**  [ds:EnableClientAuthentication](#list_ds-action-EnableClientAuthentication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableDirectoryDataAccess  **
  - **IAM action:**  [ds:EnableDirectoryDataAccess](#list_ds-action-EnableDirectoryDataAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableLDAPS  **
  - **IAM action:**  [ds:EnableLDAPS](#list_ds-action-EnableLDAPS) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableRadius  **
  - **IAM action:**  [ds:EnableRadius](#list_ds-action-EnableRadius) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableSso  **
  - **IAM action:**  [ds:EnableSso](#list_ds-action-EnableSso) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDirectoryLimits  **
  - **IAM action:**  [ds:GetDirectoryLimits](#list_ds-action-GetDirectoryLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSnapshotLimits  **
  - **IAM action:**  [ds:GetSnapshotLimits](#list_ds-action-GetSnapshotLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListADAssessments  **
  - **IAM action:**  [ds:ListADAssessments](#list_ds-action-ListADAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCertificates  **
  - **IAM action:**  [ds:ListCertificates](#list_ds-action-ListCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIpRoutes  **
  - **IAM action:**  [ds:ListIpRoutes](#list_ds-action-ListIpRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLogSubscriptions  **
  - **IAM action:**  [ds:ListLogSubscriptions](#list_ds-action-ListLogSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSchemaExtensions  **
  - **IAM action:**  [ds:ListSchemaExtensions](#list_ds-action-ListSchemaExtensions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ds:ListTagsForResource](#list_ds-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterCertificate  **
  - **IAM action:**  [ds:RegisterCertificate](#list_ds-action-RegisterCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterEventTopic  **
  - **IAM action:**  [ds:RegisterEventTopic](#list_ds-action-RegisterEventTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectSharedDirectory  **
  - **IAM action:**  [ds:RejectSharedDirectory](#list_ds-action-RejectSharedDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveIpRoutes  **
  - **IAM action:**  [ds:RemoveIpRoutes](#list_ds-action-RemoveIpRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveRegion  **
  - **IAM action:**  [ds:RemoveRegion](#list_ds-action-RemoveRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromResource  **
  - **IAM action:**  [ds:RemoveTagsFromResource](#list_ds-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ResetUserPassword  **
  - **IAM action:**  [ds:ResetUserPassword](#list_ds-action-ResetUserPassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreFromSnapshot  **
  - **IAM action:**  [ds:RestoreFromSnapshot](#list_ds-action-RestoreFromSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ShareDirectory  **
  - **IAM action:**  [ds:ShareDirectory](#list_ds-action-ShareDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartADAssessment  **
  - **IAM action:**  [ds:StartADAssessment](#list_ds-action-StartADAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSchemaExtension  **
  - **IAM action:**  [ds:StartSchemaExtension](#list_ds-action-StartSchemaExtension) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UnshareDirectory  **
  - **IAM action:**  [ds:UnshareDirectory](#list_ds-action-UnshareDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConditionalForwarder  **
  - **IAM action:**  [ds:UpdateConditionalForwarder](#list_ds-action-UpdateConditionalForwarder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDirectorySetup  **
  - **IAM action:**  [ds:UpdateDirectorySetup](#list_ds-action-UpdateDirectorySetup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHybridAD  **
  - **IAM action:**  [ds:UpdateHybridAD](#list_ds-action-UpdateHybridAD) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNumberOfDomainControllers  **
  - **IAM action:**  [ds:UpdateNumberOfDomainControllers](#list_ds-action-UpdateNumberOfDomainControllers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRadius  **
  - **IAM action:**  [ds:UpdateRadius](#list_ds-action-UpdateRadius) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSettings  **
  - **IAM action:**  [ds:UpdateSettings](#list_ds-action-UpdateSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTrust  **
  - **IAM action:**  [ds:UpdateTrust](#list_ds-action-UpdateTrust) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyTrust  **
  - **IAM action:**  [ds:VerifyTrust](#list_ds-action-VerifyTrust) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Directory Service
<a name="list_ds-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptSharedDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_AcceptSharedDirectory.html)  **
  - **Description:** Grants permission to accept a directory sharing request that was sent from the directory owner account
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddIpRoutes](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_AddIpRoutes.html)  **
  - **Description:** Grants permission to add a CIDR address block to correctly route traffic to and from your Microsoft AD on Amazon Web Services
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddRegion](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_AddRegion.html)  **
  - **Description:** Grants permission to add two domain controllers in the specified Region for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddTagsToResource](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_AddTagsToResource.html)  **
  - **Description:** Grants permission to add or overwrite one or more tags for the specified Amazon Directory Services directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ds-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [CancelSchemaExtension](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CancelSchemaExtension.html)  **
  - **Description:** Grants permission to cancel an in-progress schema extension to a Microsoft AD directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConnectDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ConnectDirectory.html)  **
  - **Description:** Grants permission to create an AD Connector to connect to an on-premises directory
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ds-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAlias](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateAlias.html)  **
  - **Description:** Grants permission to create an alias for a directory and assigns the alias to the directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateComputer](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateComputer.html)  **
  - **Description:** Grants permission to create a computer account in the specified directory, and joins the computer to the directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateConditionalForwarder](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateConditionalForwarder.html)  **
  - **Description:** Grants permission to create a conditional forwarder associated with your AWS directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html)  **
  - **Description:** Grants permission to create a Simple AD directory
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ds-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHybridAD](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateHybridAD.html)  **
  - **Description:** Grants permission to create a Hybrid Managed AD directory
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ds-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ds-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLogSubscription](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateLogSubscription.html)  **
  - **Description:** Grants permission to create a subscription to forward real time Directory Service domain controller security logs to the specified CloudWatch log group in your AWS account
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMicrosoftAD](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html)  **
  - **Description:** Grants permission to create a Microsoft AD in the AWS cloud
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ds-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSnapshot](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateSnapshot.html)  **
  - **Description:** Grants permission to create a snapshot of a Simple AD or Microsoft AD directory in the AWS cloud
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateTrust.html)  **
  - **Description:** Grants permission to initiate the creation of the AWS side of a trust relationship between a Microsoft AD in the AWS cloud and an external domain
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteADAssessment](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteADAssessment.html)  **
  - **Description:** Grants permission to delete a directory assessment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConditionalForwarder](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteConditionalForwarder.html)  **
  - **Description:** Grants permission to delete a conditional forwarder that has been set up for your AWS directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteDirectory.html)  **
  - **Description:** Grants permission to delete an AWS Directory Service directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLogSubscription](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteLogSubscription.html)  **
  - **Description:** Grants permission to delete the specified log subscription
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSnapshot](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteSnapshot.html)  **
  - **Description:** Grants permission to delete a directory snapshot
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteTrust.html)  **
  - **Description:** Grants permission to delete an existing trust relationship between your Microsoft AD in the AWS cloud and an external domain
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterCertificate](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeregisterCertificate.html)  **
  - **Description:** Grants permission to delete from the system the certificate that was registered for a secured LDAP connection
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterEventTopic](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeregisterEventTopic.html)  **
  - **Description:** Grants permission to remove the specified directory as a publisher to the specified SNS topic
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeADAssessment](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeADAssessment.html)  **
  - **Description:** Grants permission to describe a directory assessment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCAEnrollmentPolicy](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeCAEnrollmentPolicy.html)  **
  - **Description:** Grants permission to describe the ca enrollment status of a specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCertificate](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeCertificate.html)  **
  - **Description:** Grants permission to display information about the certificate registered for a secured LDAP connection
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClientAuthenticationSettings](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeClientAuthenticationSettings.html)  **
  - **Description:** Grants permission to retrieve information about the type of client authentication for the specified directory, if the type is specified. If no type is specified, information about all client authentication types that are supported for the specified directory is retrieved. Currently, only SmartCard is supported
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConditionalForwarders](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeConditionalForwarders.html)  **
  - **Description:** Grants permission to obtain information about the conditional forwarders for this account
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDirectories](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDirectories.html)  **
  - **Description:** Grants permission to obtain information about the directories that belong to this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDirectoryDataAccess](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDirectoryDataAccess.html)  **
  - **Description:** Grants permission to describe the Directory Service Data API status for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomainControllers](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDomainControllers.html)  **
  - **Description:** Grants permission to provide information about any domain controllers in your directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEventTopics](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeEventTopics.html)  **
  - **Description:** Grants permission to obtain information about which SNS topics receive status messages from the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHybridADUpdate](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeHybridADUpdate.html)  **
  - **Description:** Grants permission to describe the updates of a specified hybrid directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLDAPSSettings](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeLDAPSSettings.html)  **
  - **Description:** Grants permission to describe the status of LDAP security for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeRegions.html)  **
  - **Description:** Grants permission to provide information about the Regions that are configured for multi-Region replication
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSettings](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSettings.html)  **
  - **Description:** Grants permission to retrieve information about the configurable settings for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSharedDirectories](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSharedDirectories.html)  **
  - **Description:** Grants permission to return the shared directories in your account
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSnapshots](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSnapshots.html)  **
  - **Description:** Grants permission to obtain information about the directory snapshots that belong to this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTrusts](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeTrusts.html)  **
  - **Description:** Grants permission to obtain information about the trust relationships for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeUpdateDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeUpdateDirectory.html)  **
  - **Description:** Grants permission to describe the updates of a directory for a particular update type
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableCAEnrollmentPolicy](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableCAEnrollmentPolicy.html)  **
  - **Description:** Grants permission to disable the ca enrollment of a specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableClientAuthentication](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableClientAuthentication.html)  **
  - **Description:** Grants permission to disable alternative client authentication methods for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableDirectoryDataAccess](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableDirectoryDataAccess.html)  **
  - **Description:** Grants permission to disable the Directory Service Data API for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableLDAPS](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableLDAPS.html)  **
  - **Description:** Grants permission to deactivate LDAP secure calls for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableRadius](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableRadius.html)  **
  - **Description:** Grants permission to disable multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableSso](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableSso.html)  **
  - **Description:** Grants permission to disable single-sign on for a directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableCAEnrollmentPolicy](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableCAEnrollmentPolicy.html)  **
  - **Description:** Grants permission to enable the ca enrollment of a specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableClientAuthentication](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableClientAuthentication.html)  **
  - **Description:** Grants permission to enable alternative client authentication methods for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableDirectoryDataAccess](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableDirectoryDataAccess.html)  **
  - **Description:** Grants permission to enable the Directory Service Data API for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableLDAPS](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableLDAPS.html)  **
  - **Description:** Grants permission to activate the switch for the specific directory to always use LDAP secure calls
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableRadius](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableRadius.html)  **
  - **Description:** Grants permission to enable multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableSso](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableSso.html)  **
  - **Description:** Grants permission to enable single-sign on for a directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDirectoryLimits](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_GetDirectoryLimits.html)  **
  - **Description:** Grants permission to obtain directory limit information for the current region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSnapshotLimits](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_GetSnapshotLimits.html)  **
  - **Description:** Grants permission to obtain the manual snapshot limits for a directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListADAssessments](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListADAssessments.html)  **
  - **Description:** Grants permission to list directory assessments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCertificates](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListCertificates.html)  **
  - **Description:** Grants permission to list all the certificates registered for a secured LDAP connection, for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIpRoutes](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListIpRoutes.html)  **
  - **Description:** Grants permission to list the address blocks that you have added to a directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListLogSubscriptions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListLogSubscriptions.html)  **
  - **Description:** Grants permission to list the active log subscriptions for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSchemaExtensions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListSchemaExtensions.html)  **
  - **Description:** Grants permission to list all schema extensions applied to a Microsoft AD Directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags on an Amazon Directory Services directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RegisterCertificate](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RegisterCertificate.html)  **
  - **Description:** Grants permission to register a certificate for secured LDAP connection
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterEventTopic](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RegisterEventTopic.html)  **
  - **Description:** Grants permission to associate a directory with an SNS topic
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RejectSharedDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RejectSharedDirectory.html)  **
  - **Description:** Grants permission to reject a directory sharing request that was sent from the directory owner account
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveIpRoutes](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RemoveIpRoutes.html)  **
  - **Description:** Grants permission to remove IP address blocks from a directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveRegion](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RemoveRegion.html)  **
  - **Description:** Grants permission to stop all replication and removes the domain controllers from the specified Region. You cannot remove the primary Region with this operation
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveTagsFromResource](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RemoveTagsFromResource.html)  **
  - **Description:** Grants permission to remove tags from an Amazon Directory Services directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ds-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html)  **
  - **Description:** Grants permission to reset the password for any user in your AWS Managed Microsoft AD or Simple AD directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreFromSnapshot](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RestoreFromSnapshot.html)  **
  - **Description:** Grants permission to restore a directory using an existing directory snapshot
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ShareDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ShareDirectory.html)  **
  - **Description:** Grants permission to share a specified directory in your AWS account (directory owner) with another AWS account (directory consumer). With this operation you can use your directory from any AWS account and from any Amazon VPC within an AWS Region
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartADAssessment](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_StartADAssessment.html)  **
  - **Description:** Grants permission to start a directory assessment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartSchemaExtension](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_StartSchemaExtension.html)  **
  - **Description:** Grants permission to apply a schema extension to a Microsoft AD directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UnshareDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UnshareDirectory.html)  **
  - **Description:** Grants permission to stop the directory sharing between the directory owner and consumer accounts
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConditionalForwarder](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateConditionalForwarder.html)  **
  - **Description:** Grants permission to update a conditional forwarder that has been set up for your AWS directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDirectorySetup](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateDirectorySetup.html)  **
  - **Description:** Grants permission to update the directory for a particular update type
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHybridAD](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateHybridAD.html)  **
  - **Description:** Grants permission to update configurations for a specified hybrid directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNumberOfDomainControllers](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateNumberOfDomainControllers.html)  **
  - **Description:** Grants permission to add or remove domain controllers to or from the directory. Based on the difference between current value and new value (provided through this API call), domain controllers will be added or removed. It may take up to 45 minutes for any new domain controllers to become fully active once the requested number of domain controllers is updated. During this time, you cannot make another update request
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRadius](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateRadius.html)  **
  - **Description:** Grants permission to update the Remote Authentication Dial In User Service (RADIUS) server information for an AD Connector directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSettings](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateSettings.html)  **
  - **Description:** Grants permission to update the configurable settings for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateTrust.html)  **
  - **Description:** Grants permission to update the trust that has been set up between your AWS Managed Microsoft AD directory and an on-premises Active Directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_VerifyTrust.html)  **
  - **Description:** Grants permission to verify a trust relationship between your Microsoft AD in the AWS cloud and an external domain
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Permission-only actions for AWS Directory Service
<a name="list_ds-permission-only-actions"></a>

The following actions are defined by AWS Directory Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to access directory data using the Directory Service Data API
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [AuthorizeApplication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to authorize an application for your AWS Directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CheckAlias](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to verify that the alias is available for use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateIdentityPoolDirectory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to create an IdentityPool Directory in the AWS cloud
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ds-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ds-aws_TagKeys)
  - **Access level:** Write

- **   [DisableRoleAccess](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to disable AWS Management Console access for identity in your AWS Directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableRoleAccess](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to enable AWS Management Console access for identity in your AWS Directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAuthorizedApplicationDetails](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to retrieve the details of the authorized applications on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAuthorizedApplications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to obtain the AWS applications authorized for a directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UnauthorizeApplication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to unauthorize an application from your AWS Directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAuthorizedApplication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to update an authorized application for your AWS Directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDirectory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  **
  - **Description:** Grants permission to update the configurations like service account credentials or DNS server IP addresses for the specified directory
  - **Resource types (\*required):** [directory\*](#list_ds-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Directory Service
<a name="list_ds-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [directory](https://docs.aws.amazon.com/directoryservice/latest/devguide/welcome.html)  | arn:${Partition}:ds:${Region}:${Account}:directory/${DirectoryId} | [aws:ResourceTag/${TagKey}](#list_ds-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Directory Service
<a name="list_ds-policy-keys"></a>

AWS Directory Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_Tag.html)  | Filters access by the value of the request to AWS DS | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_Tag.html)  | Filters access by the AWS DS Resource being acted upon | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_Tag.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 