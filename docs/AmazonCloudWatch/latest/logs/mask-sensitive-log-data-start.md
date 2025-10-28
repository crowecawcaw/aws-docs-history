# Create a data protection policy for a single log group

You can use the CloudWatch Logs console or AWS CLI commands to create a data protection policy to mask sensitive data.

You can assign one data protection policy to each log group. Each data protection policy can audit for
multiple types of information. Each data protection policy can include one audit statement.

###### Topics

- [Console](#mask-sensitive-log-data-start-console "#mask-sensitive-log-data-start-console")
- [AWS CLI](#mask-sensitive-log-data-start-cli "#mask-sensitive-log-data-start-cli")

## Console

###### To use the console to create a data protection policy

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane,
   choose **Logs**, **Log groups**.
3. Choose the name of the log group.
4. Choose **Actions**, **Create data protection policy**.
5. For **Managed data identifiers**, select the types of data that you want to audit and mask
   in this log group. You can type in the selection box to find the identifiers that you want.

We recommend that you select only the data identifiers that are relevant for
your log data and your business. Choosing many types of data can lead to
false positives.

For details about which types of data that you can protect by using managed data identifiers, see
[Types of data that you can protect](protect-sensitive-log-data-types.md "protect-sensitive-log-data-types.md"). 6. (Optional) If you want to audit and mask other types of data by using custom data identifiers,
choose **Add custom data identifier**. Then enter a name for the data type and the regular expression
to use to search for that type of data in the log events. For more information, see
[Custom data identifiers](CWL-custom-data-identifiers.md "CWL-custom-data-identifiers.md").

A single data protection policy can include up to 10 custom data identifiers. Each regular expression
that defines a custom data identifier must be 200 characters or fewer. 7. (Optional) Choose one or more services to send the audit findings to. Even if you
choose not to send audit findings to any of these services, the sensitive data types that you
select will still be masked. 8. Choose **Activate data protection**.

## AWS CLI

###### To use the AWS CLI to create a data protection policy

1. Use a text editor to create a policy file named `DataProtectionPolicy.json`. For
   information about the policy syntax, see
   the following section.
2. Enter the following command:

```
aws logs put-data-protection-policy --log-group-identifier "`my-log-group`" --policy-document file:///Path/DataProtectionPolicy.json --region `us-west-2`
```

### Data protection policy syntax for AWS CLI or API operations

When you create a JSON data protection policy to use in an AWS CLI command
or API operation, the policy must include two JSON blocks:

- The first block must include both a `DataIdentifer` array and an
  `Operation` property with an `Audit` action. The `DataIdentifer` array lists the types of sensitive data that
  you want to mask. For more information about the available options, see
  [Types of data that you can protect](protect-sensitive-log-data-types.md "protect-sensitive-log-data-types.md").

The `Operation` property with an `Audit`
action is required to find the sensitive data terms. This
`Audit` action must contain a
`FindingsDestination` object. You can optionally use
that `FindingsDestination` object to list one or more
destinations to send audit findings reports to. If you specify destinations
such as log groups, Amazon Data Firehose streams, and S3 buckets, they must
already exist. For an example of an audit findins report,
see [Audit findings reports](mask-sensitive-log-data-audit-findings.md "mask-sensitive-log-data-audit-findings.md").

- The second block must include both a `DataIdentifer` array and an
  `Operation` property with an `Deidentify`
  action. The `DataIdentifer` array must exactly match the
  `DataIdentifer` array in the first block of the
  policy.

The `Operation` property with the `Deidentify` action is what actually masks the
data, and it must
contain the `"MaskConfig": {}` object. The `"MaskConfig": {}` object must be empty.

The following is an example of a data protection policy that masks email
addresses and United States driver's licenses.

```
{
    "Name": "data-protection-policy",
    "Description": "test description",
    "Version": "2021-06-01",
    "Statement": [{
            "Sid": "audit-policy",
            "DataIdentifier": [
                "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US"
            ],
            "Operation": {
                "Audit": {
                    "FindingsDestination": {
                        "CloudWatchLogs": {
                            "LogGroup": "`EXISTING_LOG_GROUP_IN_YOUR_ACCOUNT`,"
                        },
                        "Firehose": {
                            "DeliveryStream": "`EXISTING_STREAM_IN_YOUR_ACCOUNT`"
                        },
                        "S3": {
                            "Bucket": "`EXISTING_BUCKET`"
                        }
                    }
                }
            }
        },
        {
            "Sid": "redact-policy",
            "DataIdentifier": [
                "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US"
            ],
            "Operation": {
                "Deidentify": {
                    "MaskConfig": {}
                }
            }
        }
    ]
}
```
