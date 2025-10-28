# Can't see shared resources in the destination

account

## Scenario

Users can't see the resources that they believe are shared with them from other
AWS accounts.

## Possible causes and

solutions

### Sharing with AWS Organizations was turned on

by using Organizations instead of AWS RAM

If AWS Organizations was turned on by using Organizations instead of AWS RAM, then sharing within
the organization fails. To check if this is the cause of the problem, navigate
to the [Settings page in the AWS RAM
console](https://console.aws.amazon.com/ram/home#Settings: "https://console.aws.amazon.com/ram/home#Settings:") and verify that the **Enable sharing with
AWS Organizations** checkbox is selected.

- If the checkbox is selected, then this is not the cause.
- If the checkbox is not selected, then this might be the cause.
  _Don't select the checkbox yet_.
  Perform the following steps to correct the situation.

###### Important

When you disable trusted access to AWS Organizations, principals within your organization are removed from all resource shares and
lose access to those shared resources.

1. Sign in to your the management account of your organization using an IAM role
   or user with administrative permissions.
2. Navigate to the [Services page in the AWS Organizations console](https://console.aws.amazon.com/organizations/v2/home/services "https://console.aws.amazon.com/organizations/v2/home/services").
3. Choose **RAM**.
4. Choose **Disable trusted access**.
5. Navigate to the [Settings page
   in the AWS RAM console](https://console.aws.amazon.com/ram/home#Settings: "https://console.aws.amazon.com/ram/home#Settings:").
6. Select the box **Enable sharing with AWS Organizations**, and then
   choose **Save settings**.

You might need to [update the share
and specify the accounts or organizational units](working-with-sharing-update.md "working-with-sharing-update.md") within the
organization to share with.

### The resource share doesn't specify

this account as a principal

In the AWS account that created the resource share, [view the resource share](working-with-sharing-view-sr.md "working-with-sharing-view-sr.md") in the
[AWS RAM console](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home"). Verify that the account that can't access the resources is
listed as a **Principal**. If it isn't, then [update the share to add the account as
a principal](working-with-sharing-update.md "working-with-sharing-update.md").

### The role or user in the account

doesn't have required minimum permissions

When you share a resource in account A to another account B, roles and users
in account B don't automatically get access to the resources in the share. The
administrator of account B must first grant permission to the IAM roles and
users in account B who need to access the resource. As an example, the following
policy shows how you might grant read-only access to roles and users in account
B for a resource from account A. The policy specifies the resource by its
[Amazon Resource Name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ram:Get*",
 "ram:List*"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:`<service>`:`us-east-1`:`<Account-A-ID>`:`<resource-id>`"
 }
 ]
}`

```

### The resource is in a different

AWS Region than the current console setting

AWS RAM is a Regional service. Resources exist in a specific AWS Region, and
to see them, the AWS Management Console must be configured to view the resources in that
Region.

The AWS Region that the console is currently accessing is displayed in the
upper-right corner of the console. To change it, choose the current Region name
and from the dropdown menu, choose the Region whose resources you want to
see.
