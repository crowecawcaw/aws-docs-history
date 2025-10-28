# Working with S3 Access Grants on an IAM Identity Center enabled

EMR cluster

You can integrate [S3 Access Grants](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md")
with your AWS IAM Identity Center enabled EMR cluster.

Use S3 Access Grants to authorize access to your data sets from clusters that use
Identity Center. Create grants to augment the permissions that you set for IAM users,
groups, roles, or for a corporate directory. For more information, see [Using S3 Access Grants with Amazon EMR](emr-access-grants.md "emr-access-grants.md").

###### Topics

- [Create an S3 Access Grants instance and
  location](#emr-idc-s3ag-instance "#emr-idc-s3ag-instance")
- [Create grants for Identity Center
  identities](#emr-idc-s3ag-identities "#emr-idc-s3ag-identities")

## Create an S3 Access Grants instance and

location

If you don't already have one, create an S3 Access Grants instance in the AWS Region
where you want to launch your EMR cluster.

Use the following AWS CLI command to create a new instance named
`MyInstance`:

```
aws s3control-access-grants create-access-grants-instance \
--account-id `12345678912` \
--identity-center-arn "`identity-center-instance-arn`" \
```

Then, create an S3 Access Grants location, replacing the red values with your
own:

```
aws s3control-access-grants create-access-grants-location \
--account-id `12345678912` \
--location-scope s3:// \
--iam-role-arn "`access-grant-role-arn`" \
--region `aa-example-1`
```

###### Note

Define the `iam-role-arn` parameter as the
`accessGrantRole` ARN.

## Create grants for Identity Center

identities

Finally, create the grants for the identities that have access to your
cluster:

```

aws s3control-access-grants create-access-grant \
--account-id `12345678912` \
--access-grants-location-id "default" \
--access-grants-location-configuration S3SubPrefix="`s3-bucket-prefix`"
--permission READ \
--grantee GranteeType=DIRECTORY_USER,GranteeIdentifier="`your-identity-center-user-id`"
```

Example Output:

```
{
"CreatedAt": "2023-09-21T23:47:24.870000+00:00",
"AccessGrantId": "1234-12345-1234-1234567",
"AccessGrantArn": "arn:aws:s3:aa-example-1-1:123456789012:access-grants/default/grant/xxxx1234-1234-5678-1234-1234567890",
"Grantee": {
"GranteeType": "DIRECTORY_USER",
"GranteeIdentifier": "5678-56789-5678-567890"
},
"AccessGrantsLocationId": "default",
"AccessGrantsLocationConfiguration": {
"S3SubPrefix": "myprefix/*"
},
"Permission": "READ",
"GrantScope": "s3://myprefix/*"
}
```
