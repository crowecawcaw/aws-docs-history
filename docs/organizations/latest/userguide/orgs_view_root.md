# Viewing details of the root with AWS Organizations

When you sign in to the organization's management account in the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"), you
can view details of the administrative root.

###### Minimum permissions

To view the details of root, you must have the following permissions:

- `organizations:DescribeOrganization` (console only)
- `organizations:ListRoots`
  The root is the topmost container in the hierarchy of organizational units (OUs) and
  generally behaves as an OU. However, as the container at the very top of the hierarchy,
  changes to the root affect every other OU and every AWS account in the
  organization.

AWS Management Console

###### To view the details of the

root

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Navigate to the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, and choose the
   **Root** OU (its name, not the radio button).
3. The **Root** details page appears and displays
   the details of the root.

AWS CLI & AWS SDKs

###### To view the details of the root

You can use one of the following commands to view details of a root:

- AWS CLI: [list-roots](../../../cli/latest/reference/organizations/list-roots.md "../../../cli/latest/reference/organizations/list-roots.md")

The following example shows how to retrieve the details of the
root, including which policy types are currently enabled in the
organization:

```
`$` **aws organizations list-roots**`{
 "Roots": [
 {
 "Id": "r-a1b2",
 "Arn": "arn:aws:organizations::123456789012:root/o-aa111bb222/r-a1b2",
 "Name": "Root",
 "PolicyTypes": [
 {
 "Type": "BACKUP_POLICY",
 "Status": "ENABLED"
 }
 ]
 }
 ]
}`
```

- AWS SDKs: [ListRoots](../APIReference/API_ListRoots.md "../APIReference/API_ListRoots.md")
