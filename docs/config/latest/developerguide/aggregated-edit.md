# Editing Aggregators for AWS Config

You can use the AWS Config console or the AWS CLI to edit your aggregators.

Editing Aggregators (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Navigate to the **Aggregator** page, and choose the
   aggregator name.
3. Choose **Actions** and then choose
   **Edit**.
4. Use the sections on the **Edit aggregator** page to
   change the source accounts, IAM roles, or regions for the
   aggregator.

###### Note

You cannot change source type from individual account(s) to
organization and vice versa. 5. Choose **Save**.

Editing Aggregators (AWS CLI)

1. You can use the `put-configuration-aggregator` command to
   update or edit a configuration aggregator.

Enter the following command to add a new account ID to
`MyAggregator`:

```
aws configservice put-configuration-aggregator --configuration-aggregator-name MyAggregator --account-aggregation-sources "[{\"AccountIds\": [\"`AccountID1`\",\"`AccountID2`\",\"`AccountID3`\"],\"AllAwsRegions\": true}]"
```

2. Depending on your source account you should see output similar to the
   following:

**For individuals accounts**

```
{
    "ConfigurationAggregator": {
        "ConfigurationAggregatorArn": "arn:aws:config:`Region`:`AccountID`:config-aggregator/config-aggregator-xz2upuu6",
        "CreationTime": 1517952090.769,
        "ConfigurationAggregatorName": "MyAggregator",
        "AccountAggregationSources": [
            {
                "AllAwsRegions": true,
                "AccountIds": [
                    "AccountID1",
                    "AccountID2",
                    "AccountID3",
                    "AccountID4"
                ]
            }
        ],
        "LastUpdatedTime": 1517952566.445
    }
}
```

OR

**For an organization**

```
{
    "ConfigurationAggregator": {
        "ConfigurationAggregatorArn": "arn:aws:config:`Region`:`AccountID`:config-aggregator/config-aggregator-floqpus3",
        "CreationTime": 1517942461.442,
        "ConfigurationAggregatorName": "MyAggregator",
        "OrganizationAggregationSource": {
                "AllAwsRegions": true,
                "RoleArn": "arn:aws:iam::`account-of-role-to-assume`:role/`name-of-role`"
         },
        "LastUpdatedTime": 1517942461.442
    }
}
```
