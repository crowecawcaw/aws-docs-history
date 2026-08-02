# Sharing a DNS view that you own

To share a DNS view, you create a resource share in AWS RAM. A resource share specifies the
resources to share, the managed permission to apply, and the principals (accounts, organizational units, or
organization) to share with.

You can share a DNS view only if you own it. You can't share a DNS view that was shared with
you.

- [Console](#gr-sharing-dns-views-share-console "#gr-sharing-dns-views-share-console")
- [CLI](#gr-sharing-dns-views-share-cli "#gr-sharing-dns-views-share-cli")

## Sharing a DNS view (console)

###### To share a DNS view with another AWS account

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/ "https://console.aws.amazon.com/ram/").

###### Note

A DNS view is a global resource. You must create the resource share in the
US East (N. Virginia) (`us-east-1`) Region. 2. Choose **Create resource share**. 3. For **Name**, enter a descriptive name for the resource share. 4. Under **Resources**, choose the **Route 53 Global Resolver DNS
Views** resource type, and then select the DNS view that you want to share. 5. For **Managed permissions**, choose the permission that grants the
access you want. For more information, see the
_Permissions that the owner grants to the consumer_ list earlier in this
topic. 6. For **Principals**, enter the AWS account ID, OU, or organization to
share the DNS view with, and then choose **Add**. 7. Choose **Create resource share**.

If you share the DNS view with an account outside your organization in AWS Organizations, the
consumer gets an invitation to the resource share. The consumer must accept the invitation before
it can use the shared DNS view.

## Sharing a DNS view (CLI)

To share a DNS view, use the AWS RAM `create-resource-share` command. Specify the
ARN of the DNS view and the consumer account. Run the command in the
US East (N. Virginia) (`us-east-1`) Region. The following example shares a DNS view
with the account `222233334444` using the default managed permission.

`aws ram create-resource-share --region us-east-1 --name
 `MyDNSViewShare`--resource-arns
`arn:aws:route53globalresolver::111122223333:dns-view/dnsv-abcdef1234567890` --principals`222233334444``

To grant more access, include the `--permission-arns` parameter with the
ARN of the `AWSRAMPermissionDNSViewLifecycleManagement` or
`AWSRAMPermissionDNSViewFullAccess` managed permission. To find a permission's ARN, use the
AWS RAM `list-permissions` command.
