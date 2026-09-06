

# Viewing grants
<a name="grant-view"></a>

To view the grant, use the [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html) operation. You must specify the KMS key to which the grants apply. You can also filter the grant list by grant ID, grantee principal, or grantee service principal. For more examples, see [Use `ListGrants` with an AWS SDK or CLI](example_kms_ListGrants_section.md).

To view all grants in the AWS account and Region with a particular [retiring principal](grants.md#terms-retiring-principal) or [retiring service principal](grants.md#terms-retiring-service-principal), use [ListRetirableGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListRetirableGrants.html). The responses include details about each grant.

**Note**  
The `GranteePrincipal` field in the `ListGrants` response usually contains the grantee principal of the grant. However, when the grantee principal in the grant is an AWS service, the `GranteePrincipal` field contains the [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services), which might represent several different grantee principals.

**Note**  
When a grant is created with the [`GranteeServicePrincipal`](grants.md#terms-grantee-service-principal) parameter, the `ListGrants` response includes a `GranteeServicePrincipal` field instead of `GranteePrincipal`. This distinguishes grants that were explicitly created with `GranteeServicePrincipal` for an AWS [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) from grants where an AWS service is represented in the `GranteePrincipal` field.

For example, the following command lists all of the grants for a KMS key.

```
$  aws kms list-grants --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
{
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
}
```

The following example shows a `ListGrants` response for a grant created with `GranteeServicePrincipal`. Notice that the response includes a `GranteeServicePrincipal` field instead of `GranteePrincipal`, and the `Constraints` field contains a `SourceArn` value.

```
$  aws kms list-grants --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
{
    "Grants": [
        {
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "CreationDate": 1718567315.0,
            "GrantId": "abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514a",
            "Constraints": {
                "EncryptionContextSubset": {
                    "Department": "IT"
                },
                "SourceArn": "arn:aws:dynamodb:us-east-1:111122223333:table/ExampleTable"
            },
            "RetiringServicePrincipal": "{{service-name}}.amazonaws.com",
            "Name": "",
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "GranteeServicePrincipal": "{{service-name}}.amazonaws.com",
            "Operations": [
                "Encrypt",
                "Decrypt",
                "GenerateDataKey"
            ]
        }
    ]
}
```