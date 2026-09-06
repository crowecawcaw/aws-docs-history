

# AwsAthena resources in ASFF
<a name="asff-resourcedetails-awsathena"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsAthena` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsAthenaWorkGroup
<a name="asff-resourcedetails-awsathenaworkgroup"></a>

`AwsAthenaWorkGroup` provides information about an Amazon Athena workgroup. A workgroup helps you separate users, teams, applications, or workloads. It also helps you set limits on data processing and track costs.

The following example shows the ASFF for the `AwsAthenaWorkGroup` object. To view descriptions of `AwsAthenaWorkGroup` attributes, see [AwsAthenaWorkGroup](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAthenaWorkGroupDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsAthenaWorkGroup": {
    "Description": "My workgroup for prod workloads",
    "Name": "MyWorkgroup",
    "WorkgroupConfiguration" {
        "ResultConfiguration": {
            "EncryptionConfiguration": {
                "EncryptionOption": "SSE_KMS",
                "KmsKey": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            }
        }
    },
        "State": "ENABLED"
}
```