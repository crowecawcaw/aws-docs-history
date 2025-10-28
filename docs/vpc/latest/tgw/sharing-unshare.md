# Unshare a shared multicast domain in AWS Transit Gateway

When a shared multicast domain is unshared, the following happens to consumer multicast
domain resources:

- Consumer subnets are disassociated from the multicast domain. The subnets
  remain in the consumer account.
- Consumer group sources and group members are disassociated from the multicast
  domain, and then deleted from the consumer account.
  To unshare a multicast domain, you must remove it from the resource share. You can do
  this from the AWS RAM console or the AWS CLI.

To unshare a shared multicast domain that you own, you must remove it from the resource share. You
can do this using the Amazon Virtual Private Cloud, AWS RAM console, or the AWS CLI.

###### To unshare a shared multicast domain that you own using the \*Amazon Virtual Private Cloud Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Multicast Domains**.
3. Select your multicast domain, and then choose **Actions**,
   **Stop sharing**.

###### To unshare a shared multicast domain that you own using the AWS RAM console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared multicast domain that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.
