# Viewing Aggregators for AWS Config

You can use the AWS Config console or the AWS CLI to view your aggregators.

Viewing Aggregators (Console)
To view your conformance packs in the AWS Management Console, see [Aggregator
Dashboard](viewing-the-aggregate-dashboard.md "viewing-the-aggregate-dashboard.md").

Viewing Aggregators (AWS CLI)

1. Enter the following command:

```
aws configservice describe-configuration-aggregators
```

2. Depending on your source account you should see output similar to the
   following:

**For individuals accounts**

```
{
    "ConfigurationAggregators": [
        {
            "ConfigurationAggregatorArn": "arn:aws:config:`Region`:`AccountID`:config-aggregator/config-aggregator-floqpus3",
            "CreationTime": 1517942461.442,
            "ConfigurationAggregatorName": "MyAggregator",
            "AccountAggregationSources": [
                {
                    "AllAwsRegions": true,
                    "AccountIds": [
                        "AccountID1",
                        "AccountID2",
                        "AccountID3"
                    ]
                }
            ],
            "LastUpdatedTime": 1517942461.455
        }
    ]
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
