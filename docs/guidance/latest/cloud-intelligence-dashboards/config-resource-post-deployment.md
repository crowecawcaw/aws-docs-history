

# Optional post-deployment activities and FAQ
<a name="config-resource-post-deployment"></a>

## Post-deployment configuration
<a name="post-deployment-configuration"></a>

### Back Filling AWS Config data
<a name="back-filling-aws-config-data"></a>

After deployment, you will probably start seeing data in a couple of days, depending on when the configuration snapshot files are generated and when the Quick Sight datasets are refreshed. Only new AWS Config files will be partitioned by the solution and displayed on the dashboard. The backfill feature processes historical AWS Config records that already exist in your bucket and creates the necessary Athena/Glue partitions. This is essential to show your historical compliance on the dashboard when you have existing AWS Config records at the time the dashboard was first deployed.

The backfill process will generate partitions for these AWS Config records:

1. All AWS Config history records for the previous 12 months.

1. AWS Config snapshot records on all accounts and Regions whose date is the last day of the month, for the previous 5 months.

1. AWS Config snapshot records on all accounts and Regions whose date is within the last 5 days.

Follow [this process](https://github.com/aws-samples/config-resource-compliance-dashboard/tree/main/backfill) to deploy the necessary resources.

### Lambda Partitioner function
<a name="lambda-partitioner-function"></a>

#### Amazon CloudWatch Log Group Retention
<a name="amazon-cloudwatch-log-group-retention"></a>

The logs of the Partitioner function are kept for 14 days. If needed, [change the retention period](https://docs.aws.amazon.com/solutions/latest/security-insights-on-aws/change-the-cloudwatch-log-group-retention-period.html) directly on the Amazon CloudWatch console.

### Quick Sight
<a name="quick-sight"></a>

#### Configure dataset refresh schedule
<a name="configure-dataset-refresh-schedule"></a>

By default, the datasets for the CRCD dashboard are refreshed once a day. You can optionally configure the Refresh Schedule in Quick Sight with a different frequency:

1. Navigate to Quick Sight and then `Datasets`.

1. All the datasets for this dashboard have the prefix `config_`.

1. Click on a dataset, and then open the `Refresh` tab.

1. Click on `ADD NEW SCHEDULE`, and configure as needed.

## FAQ
<a name="config-resource-post-deployment-faq"></a>

### How can I see which tags I use in my organization?
<a name="how-can-i-see-which-tags-i-use-in-my-organization"></a>

Run this query in Athena, on the account and Region where you installed the CloudFormation stack.

```
WITH resource_info AS (
    SELECT
        "accountId" "AccountId",
        "region" "Region",
        "configurationItem"."resourceId" "ResourceId",
        MAX_BY("configurationItem"."tags", "configurationItem"."configurationitemcapturetime") "AllTags",
        "configurationItem"."resourcetype" "ResourceType"
    FROM cid_crcd_config
    CROSS JOIN UNNEST("configurationitems") t (configurationItem)
    WHERE CAST(date_parse("dt", '%Y-%m-%d') AS DATE) = date_add('day', -1, current_date)
        AND datasource = 'ConfigSnapshot'
    GROUP BY "accountId", "region", "configurationItem"."resourcetype", "configurationItem"."resourceId"
)
SELECT
    TagKey,
    COUNT(*) AS nr_tags
FROM resource_info
CROSS JOIN UNNEST(map_keys(AllTags)) AS t(TagKey)
GROUP BY TagKey
ORDER BY 2 DESC
```

### I installed the dashboard successfully, but there’s no data
<a name="i-installed-the-dashboard-successfully-but-theres-no-data"></a>

If you followed our recommendations in the [prerequisites](config-resource-prerequisites.md), AWS Config delivers a configuration snapshot file every 24 hours, so you will probably start seeing data in a couple of days, depending on when the configuration snapshot files are generated and when the Quick Sight datasets are refreshed.

AWS Config generates history records approximately 6 hours after a resource is changed. These records will be loaded on the dashboard faster, and be visible on the **Configuration Item Events** tab.

Follow these steps to have AWS Config generate a configuration snapshot and visualize its data on the dashboard:

1. Log into the AWS Management Console of an account of your organization.

1. Open [AWS CloudShell](https://console.aws.amazon.com/cloudshell) in the AWS Region whose data you want to export.

1. Run the following command:

   ```
   aws configservice describe-delivery-channels
   ```

1. This command will provide information about your current delivery channel configuration, including the S3 bucket where configuration updates are sent and the configuration snapshot delivery properties. The output of the CLI command should look like this:

   ```
   {
        "DeliveryChannels": [
            {
                "name": "[YOUR-DELIVERY-CHANNEL-NAME]",
                "s3BucketName": "[YOUR-AWS-CONFIG-LOGS-BUCKET-NAME]",
                "s3KeyPrefix": "[OPTIONAL-S3-PREFIX-FOR-AWS-CONFIG-FILES]",
                "configSnapshotDeliveryProperties": {
                    "deliveryFrequency": "TwentyFour_Hours"
                }
            }
        ]
    }
   ```

1. Note down the name of your delivery channel.

1. Run this command to generate an AWS Config snapshot (replace `"YOUR-DELIVERY-CHANNEL-NAME"` with the name reported above):

   ```
   aws configservice deliver-config-snapshot --delivery-channel-name "YOUR-DELIVERY-CHANNEL-NAME"
   ```

   The snapshot file will be delivered to the AWS Config Logs bucket, optionally replicated to the Dashboard bucket, and indexed by the Lambda Partitioner function.

1. Optionally repeat these steps on other AWS accounts/Regions. We recommend doing this only for test purposes, or for rapidly checking the AWS Config data of a few accounts of your interest. AWS Config will deliver a snapshot file for all your resources within 24 hours.

1. Open Athena and query the table (or any view) to see if the data has been indexed. Mind that some dashboards elements will still need time to visualize your data.

```
SELECT * FROM "cid_crcd_database"."cid_crcd_config" limit 10;
```

1. Log onto Quick Sight and [refresh](https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html) your datasets before opening the dashboard.