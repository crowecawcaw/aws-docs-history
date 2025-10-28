# Share a self-managed license in

License Manager

You can use AWS Resource Access Manager to share your self-managed licenses with any AWS account or through
AWS Organizations. For more information, see [Sharing
your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS RAM User Guide_.

## Share a self-managed license with

your AWS Organization

###### Prerequisites

To complete this procedure, you must link your AWS Organization with License Manager. For more
information, see [Managed license settings in License Manager](settings-managed-licenses.md "settings-managed-licenses.md").

###### Share your license

To share a self-managed license with your AWS Organization, follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose
   **Self-managed licenses**.
3. Select the self-managed license.
4. Choose **Share with AWS organization accounts** from the
   **Actions** menu.

## Supported accounts quota

If you enabled license sharing in AWS License Manager before October 14, 2023, your quota for the
maximum number of accounts that License Manager supports within your organization will be less
than the new default maximum. You can increase this quota by using API operations
for AWS RAM that are provided in the following section. For more information about the
default quotas in License Manager, see [Quotas for
working with licenses](../../../general/latest/gr/licensemanager.md#limits_license-manager "../../../general/latest/gr/licensemanager.md#limits_license-manager") in the _AWS General Reference
guide_.

### Prerequisites

To complete the following procedure, you must sign in as a principal in the organization's
management account that has the following permissions:

- `ram:EnableSharingWithAwsOrganization`
- `iam:CreateServiceLinkedRole`
- `organizations:enableAWSServiceAccess`
- `organizations:DescribeOrganization`

### Increasing the supported accounts

quota

The following procedure will increase your current quota for `Number of accounts per
 organization for License Manager` to the current default maximum.

###### To increase the supported accounts quota for License Manager

1. Use the [describe-organization](../../../cli/latest/reference/organizations/describe-organization.md "../../../cli/latest/reference/organizations/describe-organization.md") AWS CLI command to determine your
   organization’s ARN by using the operation:

```
aws organizations describe-organization

`{
 "Organization": {
 "Id": "o-abcde12345",
 "Arn": "arn:aws:organizations::111122223333:organization/o-abcde12345",
 "FeatureSet": "ALL",
 "MasterAccountArn": "arn:aws:organizations::111122223333:account/o-abcde12345/111122223333",
 "MasterAccountId": "111122223333",
 "MasterAccountEmail": "name+orgsidentifier@example.com",
 "AvailablePolicyTypes": [
 {
 "Type": "SERVICE_CONTROL_POLICY",
 "Status": "ENABLED"
 }
 ]
 }
}`
```

2. Use the [get-resource-shares](../../../cli/latest/reference/ram/get-resource-shares.md "../../../cli/latest/reference/ram/get-resource-shares.md") AWS CLI command to determine your organization’s
   ARN by using the operation:

```
aws ram  get-resource-shares --resource-owner SELF --tag-filters tagKey=Service,tagValues=LicenseManager --region `us-east-1`

`{
 "resourceShares": [
 {
 "resourceShareArn": "arn:aws:ram:us-east-1:111122223333:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "name": "licenseManagerResourceShare-111122223333",
 "owningAccountId": "111122223333",
 "allowExternalPrincipals": true,
 "status": "ACTIVE",
 "tags": [
 {
 "key": "Service",
 "value": "LicenseManager"
 }
 ],
 "creationTime": "2023-10-04T12:52:10.021000-07:00",
 "lastUpdatedTime": "2023-10-04T12:52:10.021000-07:00",
 "featureSet": "STANDARD"
 }
 ]
}`
```

3. Use the [enable-sharing-with-aws-organization](../../../cli/latest/reference/ram/enable-sharing-with-aws-organization.md "../../../cli/latest/reference/ram/enable-sharing-with-aws-organization.md") AWS CLI command to enable
   resource sharing with AWS RAM:

```
aws ram enable-sharing-with-aws-organization
`{
 "returnValue": true
}`
```

You can use the [list-aws-service-access-for-organization](../../../cli/latest/reference/organizations/list-aws-service-access-for-organization.md "../../../cli/latest/reference/organizations/list-aws-service-access-for-organization.md") AWS CLI command to verify
that Organizations lists service principals are enabled for License Manager and AWS RAM:

```
aws organizations list-aws-service-access-for-organization

`{
 "EnabledServicePrincipals": [
 {
 "ServicePrincipal": "license-manager.amazonaws.com",
 "DateEnabled": "2023-10-04T12:50:59.814000-07:00"
 },
 {
 "ServicePrincipal": "license-manager.member-account.amazonaws.com",
 "DateEnabled": "2023-10-04T12:50:59.565000-07:00"
 },
 {
 "ServicePrincipal": "ram.amazonaws.com",
 "DateEnabled": "2023-10-04T13:06:34.771000-07:00"
 }
 ]
}`
```

###### Important

It can take up to six hours for AWS RAM to finish this operation for your organization.
This process must complete before you can proceed. 4. Use the [associate-resource-share](../../../cli/latest/reference/ram/associate-resource-share.md "../../../cli/latest/reference/ram/associate-resource-share.md") AWS CLI command to associate your License Manager
resources share with your organization:

```
aws ram associate-resource-share --resource-share-arn arn:aws:ram:`us-east-1`:`111122223333`:resource-share/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` --principals arn:aws:organizations::`111122223333`:organization/`o-abcde12345` --region `us-east-1`

`{
 "resourceShareAssociations": [
 {
 "resourceShareArn": "arn:aws:ram:us-east-1:111122223333:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "associatedEntity": "arn:aws:organizations::111122223333:organization/o-abcde12345",
 "associationType": "PRINCIPAL",
 "status": "ASSOCIATING",
 "external": false
 }
 ]
}`
```

You can use the [get-resource-share-associations](../../../cli/latest/reference/ram/get-resource-share-associations.md "../../../cli/latest/reference/ram/get-resource-share-associations.md") AWS CLI command to validate that the
resource share association's `status` is `ASSOCIATED`:

```
aws ram get-resource-share-associations --association-type "PRINCIPAL" --principal arn:aws:organizations::`111122223333`:organization/`o-abcde12345`--resource-share-arns arn:aws:ram:`us-east-1`:`111122223333`:resource-share/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` --region `us-east-1`

`{
 "resourceShareAssociations": [
 {
 "resourceShareArn": "arn:aws:ram:us-east-1:111122223333:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "resourceShareName": "licenseManagerResourceShare-111122223333",
 "associatedEntity": "arn:aws:organizations::111122223333:organization/o-abcde12345",
 "associationType": "PRINCIPAL",
 "status": "ASSOCIATED",
 "creationTime": "2023-10-04T13:12:33.422000-07:00",
 "lastUpdatedTime": "2023-10-04T13:12:34.663000-07:00",
 "external": false
 }
 ]
}`
```
