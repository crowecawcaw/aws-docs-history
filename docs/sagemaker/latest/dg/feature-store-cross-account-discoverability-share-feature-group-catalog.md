# Share

your feature group catalog

The feature group catalog, `DefaultFeatureGroupCatalog`, contains _all_ feature group entities owned by the resource owner account. The
catalog can be shared by the resource owner account to grant discoverability to a single or
multiple resource consumer accounts. This is done by creating a resource share in AWS Resource Access Manager
(AWS RAM). A feature group is the main resource in Amazon SageMaker Feature Store and is composed of feature definitions
and records that are managed by Feature Store. For more information about feature groups, see [Feature Store concepts](feature-store-concepts.md "feature-store-concepts.md").

Discoverability means that the resource consumer accounts can search for the discoverable
resources. The discoverable resources are viewed as if they were in their own account (excluding
tags). When allowing the feature group catalog to be discoverable, the resource consumer accounts
by default are not granted access permissions (read-only, read-write, or admin). Access
permissions are granted at a resource level and not at the account level. For information about
granting access permissions, see [Enabling cross account access](feature-store-cross-account-access.md "feature-store-cross-account-access.md").

In order to enable cross account discoverability you will need to specify the SageMaker AI Resource
Catalog and the feature group catalog while using the [AWS RAM
Create a resources share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") instructions in the AWS RAM developer guide. In the following we
give the specifications for using the AWS RAM console instructions.

1.  **Specify resource share details**:
    - Resource type: Choose **SageMaker AI Resource Catalogs**.
    - ARN: Choose the feature group catalog ARN with the format:
      `arn:aws:sagemaker:`us-east-1`:`111122223333`:sagemaker-catalog/DefaultFeatureGroupCatalog`

    `us-east-1` is the region of the
    resource and `111122223333` is the resource
    owner account ID.
    - Resource ID: Choose `DefaultFeatureGroupCatalog`.

2.  **Associate managed permissions**:
    - Managed permission: Choose
      `AWSRAMPermissionSageMakerCatalogResourceSearch`.

3.  **Grant access to principals**:
    - Choose the principal types (AWS account, Organization, or Organizational unit) and
      enter the appropriate ID.

    If you are an organization, you may want to take advantage of AWS Organizations. With Organizations you can
    share resources with individual AWS accounts, all accounts in your organization, or with an
    Organization Unit (OU). This simplifies applying permissions, without having to apply
    permissions to each account. For more information about sharing your resources and granting
    permissions within AWS, see [Enable
    resource sharing within AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the AWS Resource Access Manager Developer Guide.

4.  **Review and create**:

        * Review then choose **Create resource share**.

    It may take a few minutes for the resource share and principal, or resource consumer account,
    associations to complete. Once the resource share and principal associations are set, the
    specified resource consumer accounts receive an invitation to join the resource share. The
    resource consumer accounts can view and accept the invitations by opening the [Shared with me: Resource shares](https://console.aws.amazon.com/ram/home#SharedResourceShares "https://console.aws.amazon.com/ram/home#SharedResourceShares") page
    in the AWS RAM console. For more information on accepting and viewing resources in AWS RAM, see [Access AWS resources
    shared with you](../../../ram/latest/userguide/working-with-shared.md "../../../ram/latest/userguide/working-with-shared.md"). Invitations are not sent in these cases:

- If you are part of an organization in AWS Organizations and sharing in your organization is enabled.
  In this case principals in the organization automatically get access to the shared resources
  without invitations.
- If you share with the AWS account that owns the resource, then the principals in that
  account automatically get access to the shared resources without invitations.
  For more information about accepting and using a resource share, see [Search discoverable
  resources](feature-store-cross-account-discoverability-use.md "feature-store-cross-account-discoverability-use.md").

## Share the feature group catalog using the AWS SDK for Python (Boto3)

You can use the AWS SDK for Python (Boto3) for AWS RAM APIs to create a resource share. The following code
is an example of a resource owner account ID
`111122223333` within the region
`us-east-1`. The resource owner is creating a resource share
named `test-cross-account-catalog`. They are sharing the
feature group catalog with the resource consumer account ID
`444455556666`. To use the Python SDK for AWS RAM
APIs, attach the `AWSRAMPermissionSageMakerCatalogResourceSearch` policy with the
execution role. See [AWS RAM APIs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/create_resource_share.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/create_resource_share.html") for more details.

```
#Call list resource catalogs as a prerequisite for RAM share
sagemaker_client.list_resource_catalogs()

# Share DefaultFeatureGroupCatalog with other account
ram_client = boto3.client("ram")
response = ram_client.create_resource_share(
    name='`test-cross-account-catalog`', # Change to your custom resource share name
    resourceArns=[
        'arn:aws:sagemaker:`us-east-1`:`111122223333`:sagemaker-catalog/' + 'DefaultFeatureGroupCatalog', # Change `111122223333` to the resource owner account ID
    ],
    principals=[
        '`444455556666`', # Change `444455556666` to the resource consumer account ID
    ],
    permissionArns = ["arn:aws:ram::aws:permission/AWSRAMPermissionSageMakerCatalogResourceSearch"] # AWSRAMPermissionSageMakerCatalogResourceSearch is the only policy allowed for SageMaker Catalog
)
```

Principals are actors in a security system. In a resource-based policy, the allowed
principals are IAM users, IAM roles, the root account, or another AWS service.
