

# Controlling access in AWS Marketplace Vendor Insights
<a name="vendor-insights-seller-controlling-access"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps you control access to AWS resources. IAM is an AWS service that you can use with no additional charge. If you're an administrator, you control who can be *authenticated* (signed in) and *authorized* (have permissions) to use AWS Marketplace resources. AWS Marketplace Vendor Insights uses IAM to control access to seller data, assessments, seller self-attestation, and industry standard audit reports.

The recommended way to control who can do what in AWS Marketplace Management Portal is to use IAM to create users and groups. Then you add the users to the groups, and manage the groups. You can assign a policy or permissions to the group that provide read-only permissions. If you have other users that need read-only access, you can add them to the group you created rather than adding permissions for the user.

A *policy* is a document that defines the permissions that apply to a user, group, or role. The permissions determine what users can do in AWS. A policy typically allows access to specific actions, and can optionally grant that the actions are allowed for specific resources, like Amazon EC2 instances, Amazon S3 buckets, and so on. Policies can also explicitly deny access. A *permission* is a statement within a policy that allows or denies access to a particular resource. 

**Important**  
All of the users that you create authenticate by using their credentials. However, they use the same AWS account. Any change that a user makes can impact the whole account. 

 AWS Marketplace has permissions defined to control the actions that someone with those permissions can take in the AWS Marketplace Management Portal. There are also policies that AWS Marketplace created and manages that combine several permissions. The `AWSMarketplaceSellerProductsFullAccess` policy gives the user full access to products in the AWS Marketplace Management Portal. 

For more information about the actions, resources, and condition keys that are available, see [Actions, resources, and condition keys for AWS Marketplace Vendor Insights](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html) in the *Service Authorization Reference*. 

## Permissions for AWS Marketplace Vendor Insights sellers
<a name="permissions-aws-vendor-insights-sellers"></a>

You can use the following permissions in IAM policies for AWS Marketplace Vendor Insights. You can combine permissions into a single IAM policy to grant the permissions you want. 

## `CreateDataSource`
<a name="create-data-source"></a>

`CreateDataSource` allows the user to create a new data source resource. Supported data sources are:
+ SOC2Type2AuditReport
+ ISO27001AuditReport
+ AWSAuditManagerSecurityAutomatedAssessment
+ FedRAMPCertification
+ GDPRComplianceReport
+ HIPAAComplianceReport
+ PCIDSSAuditReport
+ SecuritySelfAssessment

Action groups: Read-write

Required resources: None

Creates resources: `DataSource`

## `DeleteDataSource`
<a name="delete-data-source"></a>

`DeleteDataSource` allows the user to delete a data source that they own. A data source must be disassociated from any profile to be deleted. For more information, see [`AssociateDataSource`](#assoc-data-source). 

Action groups: Read-write

Required resources: `DataSource`

## `GetDataSource`
<a name="get-data-source"></a>

`GetDataSource` allows the user to retrieve the details of a data source. Details of a data source include metadata information such as associated timestamps, original creation parameters, and processing information, if any.

Action groups: Read-only, read-write

Required resources: `DataSource`

## `UpdateDataSource`
<a name="update-data-source"></a>

`UpdateDataSource` allows the user to update the details of a data source. Details include metadata information, such as the name and source information (for example, roles, source Amazon Resource Name (ARN), and source content).

Action groups: Read-only, read-write

Required resources: `DataSource`

## `ListDataSources`
<a name="list-data-source"></a>

`ListDataSources` allows the user to list the data sources that they own.

Action groups: Read-only, read-write, list-only

Required resources: None

## `CreateSecurityProfile`
<a name="list-data-source"></a>

`CreateSecurityProfile` allows the user to create a new security profile. A security profile is a resource to manage how and when a snapshot is generated. Users can also control how buyers can access snapshots by controlling the status and applicable terms of the profile.

Action groups: Read-only, read-write, list-only

Required resources: None

Creates resources: `SecurityProfile`

## `ListSecurityProfiles`
<a name="list-sec-profile"></a>

`ListSecurityProfiles` allows the user to list the security profiles that they own.

Action groups: Read-only, read-write, list-only

Required resources: None

## `GetSecurityProfile`
<a name="create-sec-profile"></a>

`CreateSecurityProfile` allows users to get the details of a security profile. 

Action groups: Read-only and read-write

Required resources: `SecurityProfile`

## `AssociateDataSource`
<a name="assoc-data-source"></a>

`AssociateDataSource` allows users to associate an existing `DataSource` with an AWS Marketplace Vendor Insights profile. Users can control the content of the snapshot by associating or disassociating a data source to a profile.

Action groups: Read-write

Required resources: `SecurityProfile` and `DataSource`

## `DisassociateDataSource`
<a name="disassociate-data-source"></a>

`DisassociateDataSource` allows users to disassociate an existing `DataSource` with an AWS Marketplace Vendor Insights profile. Users can control the content of the snapshot by associating or disassociating a data source to a profile.

Action groups: Read-write

Required resources: `SecurityProfile` and `DataSource`

## `UpdateSecurityProfile`
<a name="update-security-profile"></a>

`UpdateSecurityProfile` allows users to modify security profile attributes such as name and description. 

Action groups: Read-write

Required resources: `SecurityProfile`

## `ActivateSecurityProfile`
<a name="activate-sec-profile"></a>

`ActivateSecurityProfile` allows users to set an `Active` status for a security profile. After a security profile is activated, new snapshots can be created in a `Staged` state which makes it possible to release them if other conditions are met. For more information, see [`UpdateSecurityProfileSnapshotReleaseConfiguration`](#update-sec-profile-snapshot-release-config).

An `Active` security profile with at least one `Released` snapshot is eligible for AWS Marketplace Vendor Insights discovery for end users.

Action groups: Read-write

Required resources: `SecurityProfile`

## `DeactivateSecurityProfile`
<a name="deactivate-sec-profile"></a>

`DeactivateSecurityProfile` allows users to set an `Inactive` status for a security profile. This terminal state for a security profile is equivalent to taking down the profile from shared state. Users can only deactivate a security profile if there are no active subscribers to the profile.

Action groups: Read-write

Required resources: `SecurityProfile`

## `UpdateSecurityProfileSnapshotCreationConfiguration`
<a name="update-sec-profile-snapshot-creation-config"></a>

`UpdateSecurityProfileSnapshotCreationConfiguration` allows users to define custom schedules for the snapshot creation configuration. The default creation configuration of weekly creation can be overridden with this action.

Users can use this action to change the schedule including to cancel a schedule, postpone the schedule to a future date, or initiate a new snapshot creation for an earlier time.

Action groups: Read-write

Required resources: `SecurityProfile`

## `UpdateSecurityProfileSnapshotReleaseConfiguration`
<a name="update-sec-profile-snapshot-release-config"></a>

`UpdateSecurityProfileSnapshotReleaseConfiguration` allows users to define custom schedules for the snapshot release configuration. The default creation configuration of weekly releases with a two-day staging period to review can be overridden with this action.

Users can use this action to change the schedule including to cancel a schedule or postpone the schedule to a future date.

Action groups: Read-write

Required resources: `SecurityProfile`

## `ListSecurityProfileSnapshots`
<a name="list-sec-profile-snapshots"></a>

`ListSecurityProfileSnapshots` allows users to list the snapshots for a security profile that they own.

Action groups: Read-only, list-only, and read-write

Required resources: `SecurityProfile`

## `GetSecurityProfileSnapshot`
<a name="get-sec-profile-snapshots"></a>

`GetSecurityProfileSnapshot` allows users to get the snapshots for a security profile that they own.

Action groups: Read-only and read-write

Required resources: `SecurityProfile`

## `TagResource`
<a name="tag-resource"></a>

`TagResource` allows users to add new tags to a resource. Supported resources are `SecurityProfile` and `DataSource`.

Action groups: Tagging

Optional resources: `SecurityProfile` and `DataSource`

## `UntagResource`
<a name="untag-resource"></a>

`UntagResource` allows users to remove tags from a resource. Supported resources are `SecurityProfile` and `DataSource`.

Action groups: Tagging

Optional resources: `SecurityProfile` and `DataSource`

## `ListTagsForResource`
<a name="list-tags-for-resource"></a>

`ListTagsForResource` allows users to list resource tags for a resource. Supported resources are `SecurityProfile` and `DataSource`.

Action groups: Read-only

Optional resources: `SecurityProfile` and `DataSource`

## Additional resources
<a name="additional-resources"></a>

 The following resources in the *IAM User Guide* provide more information about getting started and using IAM:
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) 
+  [Attach a policy to an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html) 
+  [ IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) 
+  [Create an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) 
+  [Create IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html) 
+  [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html)