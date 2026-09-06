

# Sharing Oracle Database@AWS resources across accounts
<a name="sharing-resources-task"></a>

To enable collaboration while optimizing costs, share Oracle Database@AWS resources with other AWS accounts within the same AWS organization. This topic explains how to share resources using AWS Resource Access Manager (AWS RAM).

**Topics**
+ [Prerequisites for sharing resources](#sharing-resources-prerequisites)
+ [Sharing Oracle Database@AWS resources with another account using AWS RAM](#sharing-exadata-infrastructure)
+ [Viewing your resource shares](#viewing-resource-shares)
+ [Updating or deleting resource shares using AWS RAM](#unsharing-resources)

## Prerequisites for sharing resources
<a name="sharing-resources-prerequisites"></a>

Before you share Oracle Database@AWS resources, make sure that you have the following:
+ An active Oracle Database@AWS subscription (you must be the buyer account that accepted a private offer or public offer through AWS Marketplace)
+ The IDs or names of the resources you want to share, such as Exadata infrastructure or ODB networks
+ The IDs of the AWS accounts in your organization that you want to share resources with
+ Necessary permissions to create resource shares in AWS RAM
+ The ability to share resources with AWS Organizations using AWS RAM (for more information, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS Resource Access Manager User Guide*)

## Sharing Oracle Database@AWS resources with another account using AWS RAM
<a name="sharing-exadata-infrastructure"></a>

To share an Exadata infrastructure or ODB network with another AWS account, you create a resource share using AWS RAM. This allows the trusted account to create VM clusters on your Exadata infrastructure.

### Console
<a name="sharing-exadata-infrastructure.CON"></a>

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/).

1. Choose **Create resource share**.

1. For **Name**, enter a descriptive name for your resource share.

1. Under **Select resource type**, choose either of the following resources:
   + **Oracle Database@AWS ODB network**
   + **Oracle Database@AWS Exadata Infrastructure**

1. Select the Exadata infrastructure resources you want to share. Choose Next until you get to **Grant access to principals**.

1. Under **Principals**, choose **AWS accounts**, and then enter the AWS account IDs you want to share with.

1. Under **Managed permissions**, select the following permissions to allow the trusted account to create VM clusters on the shared Exadata infrastructure:
   + **AWSRAMDefaultPermissionODBNetwork**
   + **AWSRAMDefaultPermissionODBCloudExadataInfrastructure**

1. Choose **Create resource share**.

### AWS CLI
<a name="sharing-exadata-infrastructure.CLI"></a>

To share resources using the AWS CLI, use the `aws ram create-resource-share` command. The following example creates a resource share named `ExadataInfraShare` that shares the specified Exadata infrastructure with account 222222222222, allowing this account to create VM clusters on the shared infrastructure.

```
aws ram create-resource-share --region {{us-east-1}} \
    --name "{{ExadataInfraShare}}" \
    --resource-arns arn:aws:odb:{{us-east-1:111111111111:cloud-exadata-infrastructure/exa_infra_1}} \
    --principals {{222222222222}}
```

## Viewing your resource shares
<a name="viewing-resource-shares"></a>

To view the resources you've shared and the accounts you've shared them with:

### Console
<a name="viewing-resource-shares.CON"></a>

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/).

1. Choose **Shared resources** to view resources you've shared with other accounts.

1. Select a resource share to view its details, including the resources shared and the principals they're shared with.

### AWS CLI
<a name="viewing-resource-shares.CLI"></a>

To view your resource shares using the AWS CLI, use the `get-resource-shares` command:

```
aws ram get-resource-shares --resource-owner SELF
```

To view the resources in a specific resource share, use the `list-resources` command:

```
aws ram list-resources \
    --resource-owner {{SELF}} \
    --resource-share-arns {{arn:aws:ram:us-east-1:111111111111:resource-share/12345678-abcd-1234-efgh-111111111111}}
```

To view the principals (accounts) that a resource share is shared with, use the `list-principals` command:

```
aws ram list-principals \
    --resource-owner {{SELF}} \
    --resource-share-arns {{arn:aws:ram:us-east-1:111111111111:resource-share/12345678-abcd-1234-efgh-111111111111}}
```

## Updating or deleting resource shares using AWS RAM
<a name="unsharing-resources"></a>

To stop sharing a resource with a trusted account using AWS RAM, take any of the following actions:
+ Remove the resource from the resource share.
+ Remove the trusted account from the resource share.
+ Delete the resource share.

Before you revoke access to or delete a shared resource, consider the following implications:
+ Trusted accounts can no longer create new resources on the unshared infrastructure.
+ Existing resources created by trusted accounts on the shared Exadata infrastructure continue to function and remain accessible to those AWS accounts.
+ You can't delete Exadata infrastructure that has VM clusters created by trusted accounts until those VM clusters are removed.

Before unsharing resources, we recommend that you coordinate with the trusted accounts to ensure a smooth transition.

For more information, see [Update a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) and [Deleting a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-delete.html) in the *AWS Resource Access Manager User Guide*.