# Sharing Oracle Database@AWS resources across

accounts

To enable collaboration while optimizing costs, share Oracle Database@AWS resources with other
AWS accounts within the same AWS organization. This topic explains how to share
resources using AWS Resource Access Manager (AWS RAM).

###### Topics

- [Prerequisites for sharing
  resources](#sharing-resources-prerequisites "#sharing-resources-prerequisites")
- [Sharing Oracle Database@AWS resources with another
  account using AWS RAM](#sharing-exadata-infrastructure "#sharing-exadata-infrastructure")
- [Viewing your resource shares](#viewing-resource-shares "#viewing-resource-shares")
- [Updating or deleting resource shares using
  AWS RAM](#unsharing-resources "#unsharing-resources")

## Prerequisites for sharing

resources

Before you share Oracle Database@AWS resources, make sure that you have the
following:

- An active Oracle Database@AWS subscription (you must be the buyer account that
  accepted the private offer through AWS Marketplace)
- The IDs or names of the resources you want to share, such as Exadata infrastructure or
  ODB networks
- The IDs of the AWS accounts in your organization that you want to share
  resources with
- Necessary permissions to create resource shares in AWS RAM
- The ability to share resources with AWS Organizations using AWS RAM (for more
  information, see [Enable resource sharing within AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS Resource Access Manager User Guide_)

## Sharing Oracle Database@AWS resources with another

account using AWS RAM

To share an Exadata infrastructure or ODB network with another AWS account, you create a resource share
using AWS RAM. This allows the trusted account to create VM clusters on your Exadata infrastructure.

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/ "https://console.aws.amazon.com/ram/").
2. Choose **Create resource share**.
3. For **Name**, enter a descriptive name for your
   resource share.
4. Under **Select resource type**, either of the
   following resources:
   - **Oracle Database@AWS ODB network**
   - **Oracle Database@AWS Exadata
     Infrastructure**

5. Select the Exadata infrastructure resources you want to share. Choose Next until you
   get to **Grant access to principals**.
6. Under **Principals**, choose
   **AWS accounts**, and then enter the AWS
   account IDs you want to share with.
7. Under **Managed permissions**, select the following
   permissions to allow the trusted account to create VM clusters on the shared
   Exadata infrastructure:
   - **AWSRAMDefaultPermissionODBNetwork**
   - **AWSRAMDefaultPermissionODBCloudExadataInfrastructure**

8. Choose **Create resource share**.
   To share resources using the AWS CLI, use the `aws ram
 create-resource-share` command. The following example creates a
   resource share named `ExadataInfraShare` that shares the specified
   Exadata infrastructure with account 222222222222, allowing this account to create VM clusters on the
   shared infrastructure.

```
aws ram create-resource-share --region `us-east-1` \
    --name "`ExadataInfraShare`" \
    --resource-arns arn:aws:odb:`us-east-1:111111111111:cloud-exadata-infrastructure/exa_infra_1` \
    --principals `222222222222`
```

## Viewing your resource shares

To view the resources you've shared and the accounts you've shared them with:

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/ "https://console.aws.amazon.com/ram/").
2. Choose **Shared resources** to view resources you've
   shared with other accounts.
3. Select a resource share to view its details, including the resources shared and the principals they're shared with.
   To view your resource shares using the AWS CLI, use the `get-resource-shares` command:

```
aws ram get-resource-shares --resource-owner SELF
```

To view the resources in a specific resource share, use the `list-resources` command:

```
aws ram list-resources \
    --resource-owner `SELF` \
    --resource-share-arns `arn:aws:ram:us-east-1:111111111111:resource-share/12345678-abcd-1234-efgh-111111111111`
```

To view the principals (accounts) that a resource share is shared with, use the `list-principals` command:

```
aws ram list-principals \
    --resource-owner `SELF` \
    --resource-share-arns `arn:aws:ram:us-east-1:111111111111:resource-share/12345678-abcd-1234-efgh-111111111111`
```

## Updating or deleting resource shares using

AWS RAM

To stop sharing a resource with a trusted account using AWS RAM, take any of the
following actions:

- Remove the resource from the resource share.
- Remove the trusted account from the resource share.
- Delete the resource share.

Before you revoke access to or delete a shared resource, consider the following
implications:

- Trusted accounts can no longer create new resources on the unshared
  infrastructure.
- Existing resources created by trusted accounts on the shared Exadata infrastructure continue
  to function and remain accessible to those AWS accounts.
- You can't delete Exadata infrastructure that has VM clusters created by trusted accounts until
  those VM clusters are removed.

Before unsharing resources, we recommend that you coordinate with the trusted accounts
to ensure a smooth transition.

For more information, see [Update a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") and [Deleting a resource
share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") in the _AWS Resource Access Manager User Guide_.
