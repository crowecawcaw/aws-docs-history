

# Find the KMS keys in an AWS CloudHSM key store
<a name="find-cmk-in-keystore"></a>

If you manage an AWS CloudHSM key store, you might need to identify the KMS keys in each AWS CloudHSM key store. You can use this information to track the KMS key operations in AWS CloudTrail logs, predict the effect of disconnecting a custom key store on KMS keys, or schedule deletion of KMS keys before you delete an AWS CloudHSM key store. 

## To find the KMS keys in an AWS CloudHSM key store (console)
<a name="find-cmk-in-keystore-console"></a>

To find the KMS keys in a particular AWS CloudHSM key store, on the **Customer managed keys** page, view the values in the **Custom Key Store Name** or **Custom Key Store ID** fields. To identify KMS keys in any AWS CloudHSM key store, look for KMS keys with an **Origin** value of **AWS CloudHSM**. To add optional columns to the display, choose the gear icon in the upper right corner of the page.

## To find the KMS keys in an AWS CloudHSM key store (API)
<a name="find-cmk-in-keystore-api"></a>

To find the KMS keys in an AWS CloudHSM key store, use the [ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) and [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) operations and then filter by `CustomKeyStoreId` value. Before running the following examples, replace the fictitious custom key store ID values with a valid value.

------
#### [ Bash ]

To find KMS keys in a particular AWS CloudHSM key store, get all of your KMS keys in the account and Region. Then filter by the custom key store ID. 

```
for key in $(aws kms list-keys --query 'Keys[*].KeyId' --output text) ; 
do aws kms describe-key --key-id $key | 
grep '"CustomKeyStoreId": "{{cks-1234567890abcdef0}}"' --context 100; done
```

To get KMS keys in any AWS CloudHSM key store in the account and Region, search for `CustomKeyStoreType` with a value of `AWS_CloudHSM`.

```
for key in $(aws kms list-keys --query 'Keys[*].KeyId' --output text) ; 
do aws kms describe-key --key-id $key | 
grep '"CustomKeyStoreType": "AWS_CloudHSM"' --context 100; done
```

------
#### [ PowerShell ]

To find KMS keys in a particular AWS CloudHSM key store, use the [Get-KmsKeyList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-KMSKeyList.html) and [Get-KmsKey](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-KMSKey.html) cmdlets to get all of your KMS keys in the account and Region. Then filter by the custom key store ID. 

```
PS C:\> Get-KMSKeyList | Get-KMSKey | where CustomKeyStoreId -eq '{{cks-1234567890abcdef0}}'
```

To get KMS keys in any AWS CloudHSM key store in the account and Region, filter for the CustomKeyStoreType value of `AWS_CLOUDHSM`.

```
PS C:\> Get-KMSKeyList | Get-KMSKey | where CustomKeyStoreType -eq 'AWS_CLOUDHSM'
```

------