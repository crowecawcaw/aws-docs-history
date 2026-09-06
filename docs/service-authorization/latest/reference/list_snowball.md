

# Actions, resources, and condition keys for AWS Snowball
<a name="list_snowball"></a>

AWS Snowball (service prefix: `snowball`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/snowball/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/snowball/latest/api-reference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/snowball/latest/ug/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/snowball/snowball.json) for this service.

**Topics**
+ [API operations defined by AWS Snowball](#list_snowball-operations)
+ [Actions defined by AWS Snowball](#list_snowball-actions-as-permissions)
+ [Resource types defined by AWS Snowball](#list_snowball-resources-for-iam-policies)
+ [Condition keys for AWS Snowball](#list_snowball-policy-keys)

## API operations defined by AWS Snowball
<a name="list_snowball-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_snowball-actions-as-permissions).




- **   CancelCluster  **
  - **IAM action:**  [snowball:CancelCluster](#list_snowball-action-CancelCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelJob  **
  - **IAM action:**  [snowball:CancelJob](#list_snowball-action-CancelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAddress  **
  - **IAM action:**  [snowball:CreateAddress](#list_snowball-action-CreateAddress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCluster  **
  - **IAM action:**  [snowball:CreateCluster](#list_snowball-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** importexport.amazonaws.com / **Access level:** Write

- **   CreateJob  **
  - **IAM action:**  [snowball:CreateJob](#list_snowball-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** importexport.amazonaws.com / **Access level:** Write

- **   CreateLongTermPricing  **
  - **IAM action:**  [snowball:CreateLongTermPricing](#list_snowball-action-CreateLongTermPricing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReturnShippingLabel  **
  - **IAM action:**  [snowball:CreateReturnShippingLabel](#list_snowball-action-CreateReturnShippingLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAddress  **
  - **IAM action:**  [snowball:DescribeAddress](#list_snowball-action-DescribeAddress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAddresses  **
  - **IAM action:**  [snowball:DescribeAddresses](#list_snowball-action-DescribeAddresses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCluster  **
  - **IAM action:**  [snowball:DescribeCluster](#list_snowball-action-DescribeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJob  **
  - **IAM action:**  [snowball:DescribeJob](#list_snowball-action-DescribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReturnShippingLabel  **
  - **IAM action:**  [snowball:DescribeReturnShippingLabel](#list_snowball-action-DescribeReturnShippingLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobManifest  **
  - **IAM action:**  [snowball:GetJobManifest](#list_snowball-action-GetJobManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobUnlockCode  **
  - **IAM action:**  [snowball:GetJobUnlockCode](#list_snowball-action-GetJobUnlockCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSnowballUsage  **
  - **IAM action:**  [snowball:GetSnowballUsage](#list_snowball-action-GetSnowballUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSoftwareUpdates  **
  - **IAM action:**  [snowball:GetSoftwareUpdates](#list_snowball-action-GetSoftwareUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListClusterJobs  **
  - **IAM action:**  [snowball:ListClusterJobs](#list_snowball-action-ListClusterJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **IAM action:**  [snowball:ListClusters](#list_snowball-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCompatibleImages  **
  - **IAM action:**  [snowball:ListCompatibleImages](#list_snowball-action-ListCompatibleImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [snowball:ListJobs](#list_snowball-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLongTermPricing  **
  - **IAM action:**  [snowball:ListLongTermPricing](#list_snowball-action-ListLongTermPricing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPickupLocations  **
  - **IAM action:**  [snowball:ListPickupLocations](#list_snowball-action-ListPickupLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceVersions  **
  - **IAM action:**  [snowball:ListServiceVersions](#list_snowball-action-ListServiceVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   UpdateCluster  **
  - **IAM action:**  [snowball:UpdateCluster](#list_snowball-action-UpdateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** importexport.amazonaws.com / **Access level:** Write

- **   UpdateJob  **
  - **IAM action:**  [snowball:UpdateJob](#list_snowball-action-UpdateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** importexport.amazonaws.com / **Access level:** Write

- **   UpdateJobShipmentState  **
  - **IAM action:**  [snowball:UpdateJobShipmentState](#list_snowball-action-UpdateJobShipmentState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLongTermPricing  **
  - **IAM action:**  [snowball:UpdateLongTermPricing](#list_snowball-action-UpdateLongTermPricing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Snowball
<a name="list_snowball-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CancelCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CancelCluster.html)  | Grants permission to cancel a cluster job |  |   | Write | 
|   [CancelJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CancelJob.html)  | Grants permission to cancel the specified job |  |   | Write | 
|   [CreateAddress](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateAddress.html)  | Grants permission to create an address for a Snowball to be shipped to |  |   | Write | 
|   [CreateCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateCluster.html)  | Grants permission to create an empty cluster |  |   | Write | 
|   [CreateJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateJob.html)  | Grants permission to creates a job to import or export data between Amazon S3 and your on-premises data center |  |   | Write | 
|   [CreateLongTermPricing](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateLongTermPricing.html)  | Grants permission to creates a LongTermPricingListEntry for allowing customers to add an upfront billing contract for a job |  |   | Write | 
|   [CreateReturnShippingLabel](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateReturnShippingLabel.html)  | Grants permission to create a shipping label that will be used to return the Snow device to AWS |  |   | Write | 
|   [DescribeAddress](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeAddress.html)  | Grants permission to get specific details about that address in the form of an Address object |  |   | Read | 
|   [DescribeAddresses](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeAddresses.html)  | Grants permission to describe a specified number of ADDRESS objects |  |   | List | 
|   [DescribeCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeCluster.html)  | Grants permission to describe information about a specific cluster including shipping information, cluster status, and other important metadata |  |   | Read | 
|   [DescribeJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeJob.html)  | Grants permission to describe information about a specific job including shipping information, job status, and other important metadata |  |   | Read | 
|   [DescribeReturnShippingLabel](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeReturnShippingLabel.html)  | Grants permission to describe information on the shipping label of a Snow device that is being returned to AWS |  |   | Read | 
|   [GetJobManifest](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobManifest.html)  | Grants permission to get a link to an Amazon S3 presigned URL for the manifest file associated with the specified JobId value |  |   | Read | 
|   [GetJobUnlockCode](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobUnlockCode.html)  | Grants permission to get the UnlockCode code value for the specified job |  |   | Read | 
|   [GetSnowballUsage](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSnowballUsage.html)  | Grants permission to get information about the Snowball service limit for your account, and also the number of Snowballs your account has in use |  |   | Read | 
|   [GetSoftwareUpdates](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSoftwareUpdates.html)  | Grants permission to return an Amazon S3 presigned URL for an update file associated with a specified JobId |  |   | Read | 
|   [ListClusterJobs](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusterJobs.html)  | Grants permission to list JobListEntry objects of the specified length |  |   | List | 
|   [ListClusters](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusters.html)  | Grants permission to list ClusterListEntry objects of the specified length |  |   | List | 
|   [ListCompatibleImages](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListCompatibleImages.html)  | Grants permission to return a list of the different Amazon EC2 Amazon Machine Images (AMIs) that are owned by your AWS account that would be supported for use on a Snow device |  |   | List | 
|   [ListJobs](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListJobs.html)  | Grants permission to list JobListEntry objects of the specified length |  |   | List | 
|   [ListLongTermPricing](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListLongTermPricing.html)  | Grants permission to list LongTermPricingListEntry objects for the account making the request |  |   | Read | 
|   [ListPickupLocations](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListPickupLocations.html)  | Grants permission to list Address objects where pickup is available, of the specified length |  |   | List | 
|   [ListServiceVersions](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListServiceVersions.html)  | Grants permission to list all supported versions for Snow on-device services |  |   | List | 
|   [UpdateCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateCluster.html)  | Grants permission to update while a cluster's ClusterState value is in the AwaitingQuorum state, you can update some of the information associated with a cluster |  |   | Write | 
|   [UpdateJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateJob.html)  | Grants permission to update while a job's JobState value is New, you can update some of the information associated with a job |  |   | Write | 
|   [UpdateJobShipmentState](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateJobShipmentState.html)  | Grants permission to update the state when a the shipment states changes to a different state |  |   | Write | 
|   [UpdateLongTermPricing](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateLongTermPricing.html)  | Grants permission to update a specific upfront billing contract for a job |  |   | Write | 

## Resource types defined by AWS Snowball
<a name="list_snowball-resources-for-iam-policies"></a>

AWS Snowball does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Snowball
<a name="list_snowball-policy-keys"></a>

AWS Snowball has no service-specific condition keys that can be used in the `Condition` element of policy statements.