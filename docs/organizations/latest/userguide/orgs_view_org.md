# Viewing details of an organization from the

management account

When you sign in to the organization's management account in the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"), you
can view details of the organization.

###### Minimum permissions

To view the details of an organization, you must have the following
permission:

- `organizations:DescribeOrganization`

AWS Management Console

###### To view the details for your organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Navigate to the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings "https://console.aws.amazon.com/organizations/v2/home/settings")** page. This page displays details
   about the organization, including the organization ID and the
   account name and email address assigned to the organization's
   management account.

AWS CLI & AWS SDKs

###### To view the details for your organization

You can use one of the following commands to view details of an
organization:

- AWS CLI: [describe-organization](../../../cli/latest/reference/organizations/describe-organization.md "../../../cli/latest/reference/organizations/describe-organization.md")

The following example shows the information included in the output
of this command.

```
`$` **aws organizations describe-organization**`{
 "Organization": {
 "Id": "o-aa111bb222",
 "Arn": "arn:aws:organizations::123456789012:organization/o-aa111bb222",
 "FeatureSet": "ALL",
 "MasterAccountArn": "arn:aws:organizations::128716708097:account/o-aa111bb222/123456789012",
 "MasterAccountId": "123456789012",
 "MasterAccountEmail": "admin@example.com",
 "AvailablePolicyTypes": [ ...DEPRECATED - DO NOT USE... ]
 }
}`
```

###### Important

The `AvailablePolicyTypes` field is deprecated and
doesn't contain accurate information about the policies enabled
in your organization. To see the accurate and complete list of
policy types that are actually enabled for the organization, use
the `ListRoots` command, as described in the AWS CLI
portion of the following section.

- AWS SDKs: [DescribeOrganization](../APIReference/API_DescribeOrganization.md "../APIReference/API_DescribeOrganization.md")
