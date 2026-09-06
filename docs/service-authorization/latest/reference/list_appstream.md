

# Actions, resources, and condition keys for Amazon AppStream 2.0
<a name="list_appstream"></a>

Amazon AppStream 2.0 (service prefix: `appstream`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/appstream2/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appstream2/latest/developerguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appstream/appstream.json) for this service.

**Topics**
+ [API operations defined by Amazon AppStream 2.0](#list_appstream-operations)
+ [Actions defined by Amazon AppStream 2.0](#list_appstream-actions-as-permissions)
+ [Resource types defined by Amazon AppStream 2.0](#list_appstream-resources-for-iam-policies)
+ [Condition keys for Amazon AppStream 2.0](#list_appstream-policy-keys)

## API operations defined by Amazon AppStream 2.0
<a name="list_appstream-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_appstream-actions-as-permissions).




- **   AssociateApplicationFleet  **
  - **IAM action:**  [appstream:AssociateApplicationFleet](#list_appstream-action-AssociateApplicationFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateFleet  **
  - **IAM action:**  [appstream:AssociateFleet](#list_appstream-action-AssociateFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateUserStack  **
  - **IAM action:**  [appstream:BatchAssociateUserStack](#list_appstream-action-BatchAssociateUserStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateUserStack  **
  - **IAM action:**  [appstream:BatchDisassociateUserStack](#list_appstream-action-BatchDisassociateUserStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyImage  **
  - **IAM action:**  [appstream:CopyImage](#list_appstream-action-CopyImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAppBlock  **
  - **IAM action:**  [appstream:CreateAppBlock](#list_appstream-action-CreateAppBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [appstream:CreateApplication](#list_appstream-action-CreateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDirectoryConfig  **
  - **IAM action:**  [appstream:CreateDirectoryConfig](#list_appstream-action-CreateDirectoryConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEntitlement  **
  - **IAM action:**  [appstream:CreateEntitlement](#list_appstream-action-CreateEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateFleet  **
  - **IAM action:**  [appstream:CreateFleet](#list_appstream-action-CreateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appstream:TagResource](#list_appstream-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appstream.amazonaws.com / **Access level:** Write

- **   CreateImageBuilder  **
  - **IAM action:**  [appstream:CreateImageBuilder](#list_appstream-action-CreateImageBuilder)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appstream:TagResource](#list_appstream-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appstream.amazonaws.com / **Access level:** Write

- **   CreateImageBuilderStreamingURL  **
  - **IAM action:**  [appstream:CreateImageBuilderStreamingURL](#list_appstream-action-CreateImageBuilderStreamingURL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStack  **
  - **IAM action:**  [appstream:CreateStack](#list_appstream-action-CreateStack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appstream:TagResource](#list_appstream-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStreamingURL  **
  - **IAM action:**  [appstream:CreateStreamingURL](#list_appstream-action-CreateStreamingURL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUpdatedImage  **
  - **IAM action:**  [appstream:CreateUpdatedImage](#list_appstream-action-CreateUpdatedImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appstream:TagResource](#list_appstream-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateUsageReportSubscription  **
  - **IAM action:**  [appstream:CreateUsageReportSubscription](#list_appstream-action-CreateUsageReportSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUser  **
  - **IAM action:**  [appstream:CreateUser](#list_appstream-action-CreateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [appstream:DeleteApplication](#list_appstream-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectoryConfig  **
  - **IAM action:**  [appstream:DeleteDirectoryConfig](#list_appstream-action-DeleteDirectoryConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEntitlement  **
  - **IAM action:**  [appstream:DeleteEntitlement](#list_appstream-action-DeleteEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleet  **
  - **IAM action:**  [appstream:DeleteFleet](#list_appstream-action-DeleteFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImage  **
  - **IAM action:**  [appstream:DeleteImage](#list_appstream-action-DeleteImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImageBuilder  **
  - **IAM action:**  [appstream:DeleteImageBuilder](#list_appstream-action-DeleteImageBuilder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImagePermissions  **
  - **IAM action:**  [appstream:DeleteImagePermissions](#list_appstream-action-DeleteImagePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStack  **
  - **IAM action:**  [appstream:DeleteStack](#list_appstream-action-DeleteStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUsageReportSubscription  **
  - **IAM action:**  [appstream:DeleteUsageReportSubscription](#list_appstream-action-DeleteUsageReportSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [appstream:DeleteUser](#list_appstream-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAppBlockBuilderAppBlockAssociations  **
  - **IAM action:**  [appstream:DescribeAppBlockBuilderAppBlockAssociations](#list_appstream-action-DescribeAppBlockBuilderAppBlockAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeAppBlockBuilders  **
  - **IAM action:**  [appstream:DescribeAppBlockBuilders](#list_appstream-action-DescribeAppBlockBuilders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeAppBlocks  **
  - **IAM action:**  [appstream:DescribeAppBlocks](#list_appstream-action-DescribeAppBlocks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeApplicationFleetAssociations  **
  - **IAM action:**  [appstream:DescribeApplicationFleetAssociations](#list_appstream-action-DescribeApplicationFleetAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeApplications  **
  - **IAM action:**  [appstream:DescribeApplications](#list_appstream-action-DescribeApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDirectoryConfigs  **
  - **IAM action:**  [appstream:DescribeDirectoryConfigs](#list_appstream-action-DescribeDirectoryConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEntitlements  **
  - **IAM action:**  [appstream:DescribeEntitlements](#list_appstream-action-DescribeEntitlements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeFleets  **
  - **IAM action:**  [appstream:DescribeFleets](#list_appstream-action-DescribeFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeImageBuilders  **
  - **IAM action:**  [appstream:DescribeImageBuilders](#list_appstream-action-DescribeImageBuilders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeImagePermissions  **
  - **IAM action:**  [appstream:DescribeImagePermissions](#list_appstream-action-DescribeImagePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImages  **
  - **IAM action:**  [appstream:DescribeImages](#list_appstream-action-DescribeImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeSessions  **
  - **IAM action:**  [appstream:DescribeSessions](#list_appstream-action-DescribeSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeStacks  **
  - **IAM action:**  [appstream:DescribeStacks](#list_appstream-action-DescribeStacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeThemeForStack  **
  - **IAM action:**  [appstream:DescribeThemeForStack](#list_appstream-action-DescribeThemeForStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUsageReportSubscriptions  **
  - **IAM action:**  [appstream:DescribeUsageReportSubscriptions](#list_appstream-action-DescribeUsageReportSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeUserStackAssociations  **
  - **IAM action:**  [appstream:DescribeUserStackAssociations](#list_appstream-action-DescribeUserStackAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeUsers  **
  - **IAM action:**  [appstream:DescribeUsers](#list_appstream-action-DescribeUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisableUser  **
  - **IAM action:**  [appstream:DisableUser](#list_appstream-action-DisableUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateApplicationFleet  **
  - **IAM action:**  [appstream:DisassociateApplicationFleet](#list_appstream-action-DisassociateApplicationFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateApplicationFromEntitlement  **
  - **IAM action:**  [appstream:DisassociateApplicationFromEntitlement](#list_appstream-action-DisassociateApplicationFromEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFleet  **
  - **IAM action:**  [appstream:DisassociateFleet](#list_appstream-action-DisassociateFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableUser  **
  - **IAM action:**  [appstream:EnableUser](#list_appstream-action-EnableUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExpireSession  **
  - **IAM action:**  [appstream:ExpireSession](#list_appstream-action-ExpireSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAssociatedFleets  **
  - **IAM action:**  [appstream:ListAssociatedFleets](#list_appstream-action-ListAssociatedFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssociatedStacks  **
  - **IAM action:**  [appstream:ListAssociatedStacks](#list_appstream-action-ListAssociatedStacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEntitledApplications  **
  - **IAM action:**  [appstream:ListEntitledApplications](#list_appstream-action-ListEntitledApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [appstream:ListTagsForResource](#list_appstream-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartFleet  **
  - **IAM action:**  [appstream:StartFleet](#list_appstream-action-StartFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImageBuilder  **
  - **IAM action:**  [appstream:StartImageBuilder](#list_appstream-action-StartImageBuilder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopFleet  **
  - **IAM action:**  [appstream:StopFleet](#list_appstream-action-StopFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopImageBuilder  **
  - **IAM action:**  [appstream:StopImageBuilder](#list_appstream-action-StopImageBuilder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [appstream:TagResource](#list_appstream-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [appstream:UntagResource](#list_appstream-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDirectoryConfig  **
  - **IAM action:**  [appstream:UpdateDirectoryConfig](#list_appstream-action-UpdateDirectoryConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEntitlement  **
  - **IAM action:**  [appstream:UpdateEntitlement](#list_appstream-action-UpdateEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleet  **
  - **IAM action:**  [appstream:UpdateFleet](#list_appstream-action-UpdateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appstream.amazonaws.com / **Access level:** Write

- **   UpdateImagePermissions  **
  - **IAM action:**  [appstream:UpdateImagePermissions](#list_appstream-action-UpdateImagePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStack  **
  - **IAM action:**  [appstream:UpdateStack](#list_appstream-action-UpdateStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon AppStream 2.0
<a name="list_appstream-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAppBlockBuilderAppBlock](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateAppBlockBuilderAppBlock.html)  **
  - **Description:** Grants permission to associate the specified app block builder with the app block
  - **Resource types (\*required):** [app-block\*](#list_appstream-resource-app-block) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateApplicationFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateApplicationFleet.html)  **
  - **Description:** Grants permission to associate the specified application with the fleet
  - **Resource types (\*required):** [application\*](#list_appstream-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateApplicationToEntitlement](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateApplicationToEntitlement.html)  **
  - **Description:** Grants permission to associate the specified application to the specified entitlement
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateFleet.html)  **
  - **Description:** Grants permission to associate the specified fleet with the specified stack
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateSoftwareToImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateSoftwareToImageBuilder.html)  **
  - **Description:** Grants permission to associate license included application(s) with an existing image builder instance
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateUserStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_BatchAssociateUserStack.html)  **
  - **Description:** Grants permission to associate the specified users with the specified stacks. Users in a user pool cannot be assigned to stacks with fleets that are joined to an Active Directory domain
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateUserStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_BatchDisassociateUserStack.html)  **
  - **Description:** Grants permission to disassociate the specified users from the specified stacks
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopyImage](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CopyImage.html)  **
  - **Description:** Grants permission to copy the specified image within the same Region or to a new Region within the same AWS account
  - **Resource types (\*required):** [image\*](#list_appstream-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAppBlock](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlock.html)  **
  - **Description:** Grants permission to create an app block. App blocks store details about the virtual hard disk that contains the files for the application in an S3 bucket. It also stores the setup script with details about how to mount the virtual hard disk. App blocks are only supported for Elastic fleets
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAppBlockBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlockBuilder.html)  **
  - **Description:** Grants permission to create an app block builder. An app block builder is a virtual machine that is used to create an app block
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAppBlockBuilderStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlockBuilderStreamingURL.html)  **
  - **Description:** Grants permission to create a URL to start an app block builder streaming session
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application within customer account. Applications store the details about how to launch applications on streaming instances. This is only supported for Elastic fleets
  - **Resource types (\*required):** [app-block\*](#list_appstream-resource-app-block)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDirectoryConfig](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateDirectoryConfig.html)  **
  - **Description:** Grants permission to create a Directory Config object in AppStream 2.0. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEntitlement](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateEntitlement.html)  **
  - **Description:** Grants permission to create an entitlement to control access to applications based on user attributes
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateExportImageTask](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateExportImageTask.html)  **
  - **Description:** Grants permission to create an export task for an AppStream 2.0 image
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateFleet.html)  **
  - **Description:** Grants permission to create a fleet. A fleet is a group of streaming instances from which applications are launched and streamed to users
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [image](#list_appstream-resource-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilder.html)  **
  - **Description:** Grants permission to create an image builder. An image builder is a virtual machine that is used to create an image
  - **Resource types (\*required):** [image\*](#list_appstream-resource-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateImageBuilderStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilderStreamingURL.html)  **
  - **Description:** Grants permission to create a URL to start an image builder streaming session
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateImportedImage](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImportedImage.html)  **
  - **Description:** Grants permission to create an AppStream 2.0 image from an imported AMI
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStack.html)  **
  - **Description:** Grants permission to create a stack to start streaming applications to users. A stack consists of an associated fleet, user access policies, and storage configurations
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html)  **
  - **Description:** Grants permission to create a temporary URL to start an AppStream 2.0 streaming session for the specified user. A streaming URL enables application streaming to be tested without user setup
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateThemeForStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateThemeForStack.html)  **
  - **Description:** Grants permission to create a custom branding theme, which might includes a custom logo, website links, and other branding to display to your users
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUpdatedImage](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUpdatedImage.html)  **
  - **Description:** Grants permission to update an existing image within customer account
  - **Resource types (\*required):** [image\*](#list_appstream-resource-image)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUsageReportSubscription](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUsageReportSubscription.html)  **
  - **Description:** Grants permission to create a usage report subscription. Usage reports are generated daily
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a new user in the user pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAppBlock](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteAppBlock.html)  **
  - **Description:** Grants permission to delete the specified app block
  - **Resource types (\*required):** [app-block\*](#list_appstream-resource-app-block)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAppBlockBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteAppBlockBuilder.html)  **
  - **Description:** Grants permission to delete the specified app block builder and release capacity
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete the specified application
  - **Resource types (\*required):** [application\*](#list_appstream-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDirectoryConfig](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteDirectoryConfig.html)  **
  - **Description:** Grants permission to delete the specified Directory Config object from AppStream 2.0. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEntitlement](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteEntitlement.html)  **
  - **Description:** Grants permission to delete the specified entitlement
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteFleet.html)  **
  - **Description:** Grants permission to delete the specified fleet
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImage](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteImage.html)  **
  - **Description:** Grants permission to delete the specified image. An image cannot be deleted when it is in use
  - **Resource types (\*required):** [image\*](#list_appstream-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteImageBuilder.html)  **
  - **Description:** Grants permission to delete the specified image builder and release capacity
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteImagePermissions.html)  **
  - **Description:** Grants permission to delete permissions for the specified private image
  - **Resource types (\*required):** [image\*](#list_appstream-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteStack.html)  **
  - **Description:** Grants permission to delete the specified stack. After the stack is deleted, the application streaming environment provided by the stack is no longer available to users. Also, any reservations made for application streaming sessions for the stack are released
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteThemeForStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteThemeForStack.html)  **
  - **Description:** Grants permission to delete a custom branding theme, which might includes a custom logo, website links, and other branding to display to your users
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUsageReportSubscription](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteUsageReportSubscription.html)  **
  - **Description:** Grants permission to disable usage report generation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a user from the user pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAppBlockBuilderAppBlockAssociations](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppBlockBuilderAppBlockAssociations.html)  **
  - **Description:** Grants permission to retrieve the associations that are associated with the specified app block builder or app block
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAppBlockBuilders](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppBlockBuilders.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified app block builders, if the app block builder names are provided. Otherwise, all app block builders in the account are described
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAppBlocks](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppBlocks.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified app blocks, if the app block arns are provided. Otherwise, all app blocks in the account are described
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAppLicenseUsage](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppLicenseUsage.html)  **
  - **Description:** Grants permission to retrieve license included application usage information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeApplicationFleetAssociations](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeApplicationFleetAssociations.html)  **
  - **Description:** Grants permission to retrieve the associations that are associated with the specified application or fleet
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeApplications](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeApplications.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified applications, if the application arns are provided. Otherwise, all applications in the account are described
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDirectoryConfigs](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeDirectoryConfigs.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified Directory Config objects for AppStream 2.0, if the names for these objects are provided. Otherwise, all Directory Config objects in the account are described. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEntitlements](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeEntitlements.html)  **
  - **Description:** Grants permission to retrieve one or all entitlements for the specified stack
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeFleets](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeFleets.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified fleets, if the fleet names are provided. Otherwise, all fleets in the account are described
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeImageBuilders](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImageBuilders.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified image builders, if the image builder names are provided. Otherwise, all image builders in the account are described
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImagePermissions.html)  **
  - **Description:** Grants permission to retrieve a list that describes the permissions for shared AWS account IDs on a private image that you own
  - **Resource types (\*required):** [image\*](#list_appstream-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImages](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImages.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified images, if the image names or image ARNs are provided. Otherwise, all images in the account are described
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeSessions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeSessions.html)  **
  - **Description:** Grants permission to retrieve a list that describes the streaming sessions for the specified stack and fleet. If a user ID is provided for the stack and fleet, only the streaming sessions for that user are described
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeSoftwareAssociations](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeSoftwareAssociations.html)  **
  - **Description:** Grants permission to retrieve license included application associations for a specified resource
  - **Resource types (\*required):** [image](#list_appstream-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [image-builder](#list_appstream-resource-image-builder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeStacks](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeStacks.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more specified stacks, if the stack names are provided. Otherwise, all stacks in the account are described
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeThemeForStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeThemeForStack.html)  **
  - **Description:** Grants permission to get the custom branding theme information, which might includes a custom logo, website links, and other branding to display to your users
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUsageReportSubscriptions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUsageReportSubscriptions.html)  **
  - **Description:** Grants permission to retrieve a list that describes one or more usage report subscriptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeUserStackAssociations](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUserStackAssociations.html)  **
  - **Description:** Grants permission to retrieve a list that describes the UserStackAssociation objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeUsers](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUsers.html)  **
  - **Description:** Grants permission to retrieve a list that describes users in the user pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DisableUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DisableUser.html)  **
  - **Description:** Grants permission to disable the specified user in the user pool. This action does not delete the user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateAppBlockBuilderAppBlock](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DisassociateAppBlockBuilderAppBlock.html)  **
  - **Description:** Grants permission to disassociate the specified app block builder with the app block
  - **Resource types (\*required):** [app-block\*](#list_appstream-resource-app-block) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateApplicationFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DisassociateApplicationFleet.html)  **
  - **Description:** Grants permission to disassociate the specified application from the specified fleet
  - **Resource types (\*required):** [application\*](#list_appstream-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateApplicationFromEntitlement](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DisassociateApplicationFromEntitlement.html)  **
  - **Description:** Grants permission to disassociate the specified application from the specified entitlement
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DisassociateFleet.html)  **
  - **Description:** Grants permission to disassociate the specified fleet from the specified stack
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSoftwareFromImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DisassociateSoftwareFromImageBuilder.html)  **
  - **Description:** Grants permission to remove license included application(s) association(s) from an image builder instance
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_EnableUser.html)  **
  - **Description:** Grants permission to enable a user in the user pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ExpireSession](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ExpireSession.html)  **
  - **Description:** Grants permission to immediately stop the specified streaming session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetExportImageTask](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_GetExportImageTask.html)  **
  - **Description:** Grants permission to retrieve details of a specific export image task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAssociatedFleets](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListAssociatedFleets.html)  **
  - **Description:** Grants permission to retrieve the name of the fleet that is associated with the specified stack
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssociatedStacks](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListAssociatedStacks.html)  **
  - **Description:** Grants permission to retrieve the name of the stack with which the specified fleet is associated
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEntitledApplications](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListEntitledApplications.html)  **
  - **Description:** Grants permission to retrieve the applications that are associated with the specified entitlement
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExportImageTasks](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListExportImageTasks.html)  **
  - **Description:** Grants permission to list export image tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of all tags for the specified AppStream 2.0 resource. The following resources can be tagged: Image builders, images, fleets, and stacks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartAppBlockBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StartAppBlockBuilder.html)  **
  - **Description:** Grants permission to start the specified app block builder
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StartFleet.html)  **
  - **Description:** Grants permission to start the specified fleet
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StartImageBuilder.html)  **
  - **Description:** Grants permission to start the specified image builder
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSoftwareDeploymentToImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StartSoftwareDeploymentToImageBuilder.html)  **
  - **Description:** Grants permission to initiate license included applications deployment to an image builder instance
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAppBlockBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StopAppBlockBuilder.html)  **
  - **Description:** Grants permission to stop the specified app block builder
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StopFleet.html)  **
  - **Description:** Grants permission to stop the specified fleet
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StopImageBuilder.html)  **
  - **Description:** Grants permission to stop the specified image builder
  - **Resource types (\*required):** [image-builder\*](#list_appstream-resource-image-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Stream](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-setting-up-saml.html#external-identity-providers-embed-inline-policy-for-IAM-role)  **
  - **Description:** Grants permission to federated users to sign in by using their existing credentials and stream applications from the specified stack
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [appstream:userId](#list_appstream-appstream_userId)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite one or more tags for the specified AppStream 2.0 resource. The following resources can be tagged: Image builders, images, fleets, stacks, app blocks and applications
  - **Resource types (\*required):** [app-block](#list_appstream-resource-app-block) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [app-block-builder](#list_appstream-resource-app-block-builder) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [application](#list_appstream-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [fleet](#list_appstream-resource-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [image](#list_appstream-resource-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [image-builder](#list_appstream-resource-image-builder) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [stack](#list_appstream-resource-stack) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appstream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate one or more tags from the specified AppStream 2.0 resource
  - **Resource types (\*required):** [app-block](#list_appstream-resource-app-block) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [app-block-builder](#list_appstream-resource-app-block-builder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [application](#list_appstream-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [fleet](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [image](#list_appstream-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [image-builder](#list_appstream-resource-image-builder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Resource types (\*required):** [stack](#list_appstream-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appstream-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAppBlockBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateAppBlockBuilder.html)  **
  - **Description:** Grants permission to update a specific app block builder. An app block builder is a virtual machine that is used to create an app block
  - **Resource types (\*required):** [app-block-builder\*](#list_appstream-resource-app-block-builder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApplication](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update the specified fields for the specified application
  - **Resource types (\*required):** [app-block](#list_appstream-resource-app-block) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [application\*](#list_appstream-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDirectoryConfig](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateDirectoryConfig.html)  **
  - **Description:** Grants permission to update the specified Directory Config object in AppStream 2.0. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEntitlement](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateEntitlement.html)  **
  - **Description:** Grants permission to update the specified fields for the specified entitlement
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateFleet.html)  **
  - **Description:** Grants permission to update the specified fleet. All attributes except the fleet name can be updated when the fleet is in the STOPPED state
  - **Resource types (\*required):** [fleet\*](#list_appstream-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [image](#list_appstream-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImagePermissions.html)  **
  - **Description:** Grants permission to add or update permissions for the specified private image
  - **Resource types (\*required):** [image\*](#list_appstream-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateStack.html)  **
  - **Description:** Grants permission to update the specified fields for the specified stack
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThemeForStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateThemeForStack.html)  **
  - **Description:** Grants permission to update the custom branding theme information, which might includes a custom logo, website links, and other branding to display to your users
  - **Resource types (\*required):** [stack\*](#list_appstream-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon AppStream 2.0
<a name="list_appstream-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [app-block](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts)  | arn:${Partition}:appstream:${Region}:${Account}:app-block/${AppBlockName} | [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_) | 
|  [app-block-builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts)  | arn:${Partition}:appstream:${Region}:${Account}:app-block-builder/${AppBlockBuilderName} | [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_) | 
|  [application](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts)  | arn:${Partition}:appstream:${Region}:${Account}:application/${ApplicationName} | [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_) | 
|  [fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts)  | arn:${Partition}:appstream:${Region}:${Account}:fleet/${FleetName} | [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_) | 
|  [image](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts)  | arn:${Partition}:appstream:${Region}:${Account}:image/${ImageName} | [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_) | 
|  [image-builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts)  | arn:${Partition}:appstream:${Region}:${Account}:image-builder/${ImageBuilderName} | [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_) | 
|  [stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts)  | arn:${Partition}:appstream:${Region}:${Account}:stack/${StackName} | [aws:ResourceTag/${TagKey}](#list_appstream-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon AppStream 2.0
<a name="list_appstream-policy-keys"></a>

Amazon AppStream 2.0 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [appstream:userId](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-setting-up-saml.html#external-identity-providers-embed-inline-policy-for-IAM-role)  | Filters access by the ID of the AppStream 2.0 user | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 