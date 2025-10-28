# Set up cross-account hub sharing

SageMaker uses [AWS Resource Access Manager (AWS RAM)](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") to help
you securely share your private hubs across accounts. Set up cross-account hub
sharing using the following instructions along with the [Sharing your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") instructions in the _AWS RAM User Guide_.

###### Create a resource share

1. Select **Create resource share** through the [AWS RAM
   console](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. When specifying resource share details, choose the
   **SageMaker Hubs** resource type and select one more more
   private hubs that you want to share. When you share a hub with any other
   account, all of its contents are also shared implicitly.
3. Associate permissions with your resources share. For more information about managed permissions, see [Managed permissions for curated private hubs](jumpstart-curated-hubs-ram.md#jumpstart-curated-hubs-ram-permissions "jumpstart-curated-hubs-ram.md#jumpstart-curated-hubs-ram-permissions")
4. Use AWS account IDs to specify the accounts to which you want to grant
   access to your shared resources.
5. Review your resource share configuration and select **Create resource share**. It may take a few minutes for the
   resource share and principal associations to complete.
   For more information, see [Sharing your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS Resource Access Manager User Guide_.

After the resource share and principal associations are set, the specified AWS
accounts receive an invitation to join the resource share. The AWS accounts must
accept the invite to gain access to any shared resources.

For more information on accepting a resource share invite through AWS RAM, see
[Using shared AWS resources](../../../ram/latest/userguide/getting-started-shared.md "../../../ram/latest/userguide/getting-started-shared.md") in the _AWS Resource Access Manager User Guide_.
