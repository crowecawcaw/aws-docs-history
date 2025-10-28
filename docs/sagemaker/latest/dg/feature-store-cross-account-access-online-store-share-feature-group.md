# Share

your feature group entities

As the resource owner account you can use the feature group resource type for Amazon SageMaker Feature Store to
share feature group entities, by creating a resource share in AWS Resource Access Manager (AWS RAM).

Use the following instructions along with the [Sharing your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") instructions in the AWS RAM User Guide.

When sharing the feature group resource type using the AWS RAM console, you need to make the
following choices.

1.  **Specify resource share details**:
    - Resource type: Choose **SageMaker AI Feature Groups**.
    - ARN: Choose your feature group ARN with the format:
      `arn:aws:sagemaker:us-east-1:111122223333:feature-group/`your-feature-group-name``.

    `us-east-1` is the region of the resource,
    `111122223333` is the resource owner account ID,
    and `your-feature-group-name` is the
    feature group you are sharing.
    - Resource ID: Choose the feature group,
      `your-feature-group-name`, to
      which you want to grant access permissions.

2.  **Associate managed permissions**:
    - Managed permission: Choose the access permission. For more information
      about access permissions, see [Enabling cross account access](feature-store-cross-account-access.md "feature-store-cross-account-access.md").

3.  **Grant access to principals**:
    - Choose the principal type (AWS account, Organization, Organizational
      unit, IAM role, or IAM user) and enter the appropriate ID or ARN.

4.  **Review and create**:

        * Review then choose **Create resource share**.

    Granting any access permission does not grant resource consumer accounts the
    discoverability permission, so the resource consumer accounts with access permissions cannot
    search and discover those feature groups. To allow for resource consumer accounts to search
    and discover feature groups from the resource owner account, the resource owner account must
    grant the discoverability permission to the resource consumer accounts, where _all_ of the feature groups within the resource owner account are
    discoverable by the resource consumer accounts. For more information about granting the
    discoverability permission, see [Enabling cross account
    discoverability](feature-store-cross-account-discoverability.md "feature-store-cross-account-discoverability.md").

If the resource consumer accounts are only granted access permissions, the feature group
entities can still be viewed on AWS RAM. To view resources on AWS RAM, see [Access AWS
resources shared with you](../../../ram/latest/userguide/working-with-shared.md "../../../ram/latest/userguide/working-with-shared.md") in the AWS RAM User Guide.

It may take a few minutes for the resource share and principal, or resource consumer
account, associations to complete. Once the resource share and principal associations are
set, the specified resource consumer accounts receive an invitation to join the resource
share. The resource consumer accounts can view and accept the invitations by opening the
[Shared with me: Resource
shares](https://console.aws.amazon.com/ram/home#SharedResourceShares "https://console.aws.amazon.com/ram/home#SharedResourceShares") page in the AWS RAM console. Invitations are not sent in these
cases:

- If you are part of an organization in AWS Organizations and sharing in your organization is
  enabled, then principals in the organization automatically get access to the shared
  resources without invitations.
- If you share with the AWS account that owns the resource, then the principals in
  that account automatically get access to the shared resources without
  invitations.
  For more information about accepting and using a resource share in AWS RAM, see [Using shared
  AWS resources](../../../ram/latest/userguide/getting-started-shared.md "../../../ram/latest/userguide/getting-started-shared.md") in the AWS RAM User Guide.

## Share online store feature groups using the AWS SDK for Python (Boto3)

You can use the AWS SDK for Python (Boto3) for AWS RAM APIs to create a resource share. The following
code is an example of a resource owner account ID `111122223333`
creating a resource share named `'test-cross-account-fg'`, sharing the
feature group named `'my-feature-group'` with the resource consumer account
ID `444455556666` while granting the
`AWSRAMPermissionSageMakerFeatureGroupReadOnly` permission. For more
information about access permissions, see [Enabling cross account access](feature-store-cross-account-access.md "feature-store-cross-account-access.md"). To use the Python SDK for
AWS RAM APIs, you need to attach AWS RAM full access managed policy with execution role. See
[create_resource_share](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/create_resource_share.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/create_resource_share.html") AWS RAM API for more details.

```
import boto3

# Choose feature group name
feature_group_name = 'my-feature-group' # Change to your feature group name

# Share 'my-feature-group' with other account
ram_client = boto3.client("ram")
response = ram_client.create_resource_share(
    name='test-cross-account-fg', # Change to your custom resource share name
    resourceArns=[
        'arn:aws:sagemaker:us-east-1:111122223333:feature-group/' + feature_group_name, # Change 111122223333 to the resource owner account ID
    ],
    principals=[
        '444455556666', # Change 444455556666 to the resource consumer account ID
    ],
    permissionArns = ["arn:aws:ram::aws:permission/AWSRAMPermissionSageMakerFeatureGroupReadOnly"]
)
```

Principals are actors in a security system. In a resource-based policy, the allowed
principals are IAM users, IAM roles, the root account, or another
AWS service.
