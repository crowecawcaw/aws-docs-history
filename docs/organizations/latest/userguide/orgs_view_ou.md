# Viewing details of an organizational unit (OU) with AWS Organizations

When you sign in to the organization's management account in the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"), you
can view details of the OUs in your organization.

###### Minimum permissions

To view the details of an organizational unit (OU), you must have the following
permissions:

- `organizations:DescribeOrganizationalUnit`
- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:ListOrganizationsUnitsForParent`– required only when using the Organizations console
- `organizations:ListRoots` – required only when using the Organizations console

AWS Management Console

###### To view details of an OU

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, choose the name of the OU (not its radio
   button) that you want to examine. If the OU that you want is a child
   of another OU, choose the triangle icon next to its parent OU to
   expand it and see those in the next level of the hierarchy. Repeat
   until you find the OU that you want.

The **Organizational unit details** box shows the
information about the OU.

AWS CLI & AWS SDKs

###### To view details of an OU

You can use the following commands to view details of an OU:

- AWS CLI, AWS SDKs:

      + [list-roots](../../../cli/latest/reference/organizations/list-roots.md "../../../cli/latest/reference/organizations/list-roots.md")
      + [list-children](../../../cli/latest/reference/organizations/list-children.md "../../../cli/latest/reference/organizations/list-children.md")
      + [describe-organizational-unit](../../../cli/latest/reference/organizations/describe-organizational-unit.md "../../../cli/latest/reference/organizations/describe-organizational-unit.md")

  The following example shows how to find the ID of on OU using the
  AWS CLI. You find the OU ID by traversing the hierarchy starting with
  the `list-roots` command and then performing
  `list-children` on the root and iteratively on each
  of its children until you find the one you want.

```
`$` **aws organizations list-roots**`{
 "Roots": [
 {
 "Id": "r-a1b2",
 "Arn": "arn:aws:organizations::123456789012:root/o-aa111bb222/r-a1b2",
 "Name": "Root",
 "PolicyTypes": []
 }
 ]
}`
`$` **aws organizations list-children --parent-id r-a1b2 --child-type ORGANIZATIONAL\_UNIT**`{
 "Children": [
 {
 "Id": "ou-a1b2-f6g7h111",
 "Type": "ORGANIZATIONAL_UNIT"
 }
 ]
}`
```

After you have the OU's ID, the following example shows how to
retrieve the details about the OU.

```
`$` **aws organizations describe-organizational-unit --organizational-unit-id ou-a1b2-f6g7h111**`{
 "OrganizationalUnit": {
 "Id": "ou-a1b2-f6g7h111",
 "Arn": "arn:aws:organizations::123456789012:ou/o-aa111bb222/ou-a1b2-f6g7h111",
 "Name": "Production-Apps"
 }
}`
```

- AWS SDKs:
  - [ListRoots](../APIReference/API_ListRoots.md "../APIReference/API_ListRoots.md")
  - [ListChildren](../APIReference/API_ListChildren.md "../APIReference/API_ListChildren.md")
  - [DescribeOrganizationalUnit](../APIReference/API_DescribeOrganizationalUnit.md "../APIReference/API_DescribeOrganizationalUnit.md")
