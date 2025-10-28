# Viewing grants

To view the grant, use the [ListGrants](../APIReference/API_ListGrants.md "../APIReference/API_ListGrants.md") operation. You must specify the KMS key to which the grants apply. You
can also filter the grant list by grant ID or grantee principal. For more examples, see [Use ListGrants with an AWS SDK or CLI](example_kms_ListGrants_section.md "example_kms_ListGrants_section.md").

To view all grants in the AWS account and Region with a particular [retiring principal](grants.md#terms-retiring-principal "grants.md#terms-retiring-principal"), use [ListRetirableGrants](../APIReference/API_ListRetirableGrants.md "../APIReference/API_ListRetirableGrants.md"). The responses
include details about each grant.

###### Note

The `GranteePrincipal` field in the `ListGrants` response usually
contains the grantee principal of the grant. However, when the grantee principal in the
grant is an AWS service, the `GranteePrincipal` field contains the [service
principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), which might represent several different grantee principals.

For example, the following command lists all of the grants for a KMS key.

```
`$`  `aws kms list-grants --key-id 1234abcd-12ab-34cd-56ef-1234567890ab`
`{
 "Grants": [
 {
 "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "CreationDate": 1572216195.0,
 "GrantId": "abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514a",
 "Constraints": {
 "EncryptionContextSubset": {
 "Department": "IT"
 }
 },
 "RetiringPrincipal": "arn:aws:iam::111122223333:role/adminRole",
 "Name": "",
 "IssuingAccount": "arn:aws:iam::111122223333:root",
 "GranteePrincipal": "arn:aws:iam::111122223333:user/exampleUser",
 "Operations": [
 "Decrypt"
 ]
 }
 ]
}`
```
