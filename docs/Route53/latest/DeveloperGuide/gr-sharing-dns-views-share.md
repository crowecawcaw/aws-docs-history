# Sharing a DNS view that you own

To share a DNS view, you create a resource share in AWS RAM. A resource share specifies the
resources to share, the to apply, and the principals (the AWS accounts, organizational
units, or organization) to share with.

You can share a DNS view only if you own it. You can't share a DNS view that's shared with
you.

- [Console](#gr-sharing-dns-views-share-console "#gr-sharing-dns-views-share-console")
- [CLI](#gr-sharing-dns-views-share-cli "#gr-sharing-dns-views-share-cli")

## Sharing a DNS view (console)

###### To share a DNS view with another AWS account

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/ "https://console.aws.amazon.com/ram/").

###### Note

Because a DNS view is a global resource, you create the resource share in the
US East (N. Virginia) (`us-east-1`) Region. 2. Choose **Create resource share**. 3. For **Name**, enter a descriptive name for the resource share. 4. Under **Resources**, choose the **Route 53 Global Resolver DNS
Views** resource type, and then select the DNS view that you want to share. 5. For **Managed permissions**, choose the permission that grants the
access that you want the consumer to have. For more information, see the
_Permissions that the owner grants to the consumer_ list earlier in this
topic. 6. For **Principals**, enter the AWS account ID, OU, or organization that
you want to share the DNS view with, and then choose **Add**. 7. Choose **Create resource share**.

If you share the DNS view with an account that's outside your organization in AWS Organizations, the
consumer receives an invitation to the resource share and must accept it before the consumer can
use the shared DNS view.

## Sharing a DNS view (CLI)

To share a DNS view, use the AWS RAM `create-resource-share` command. Specify the
of the DNS view and the consumer account, and run the command in the
US East (N. Virginia) (`us-east-1`) Region. The following example shares a DNS view
with the account `222233334444` by using the default .

`aws ram create-resource-share --region us-east-1 --name
 `MyDNSViewShare`--resource-arns
`arn:aws:route53globalresolver::111122223333:dns-view/dnsv-abcdef1234567890` --principals`222233334444``

To grant additional access, include the `--permission-arns` parameter with the
of the `AWSRAMPermissionDNSViewLifecycleManagement` or
`AWSRAMPermissionDNSViewFullAccess` . To find a permission's , use the
AWS RAM `list-permissions` command.
