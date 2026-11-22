

# Enabling AWS Billing and Cost Management publishing

Enable AWS Billing and Cost Management publishing for new or existing S3 Storage Lens dashboard configurations by using the Amazon S3 console, AWS CLI, AWS SDKs, or Amazon S3 REST API. To view prefix costs, you must also enable split cost allocation data for Amazon S3 in AWS Billing and Cost Management. For more information, see [Next step: Enable split cost allocation data](#storage-lens-cur-next-steps).

## Using the S3 console
<a name="storage-lens-cur-enable-console"></a>

Use the following procedures to enable AWS Billing and Cost Management publishing for a new or existing S3 Storage Lens dashboard by using the Amazon S3 console.

**Before you begin** – In the console, AWS Billing and Cost Management publishing is available only for dashboards that use the advanced tier and the default prefix delimiter, `/` (forward slash). You set the prefix delimiter in the **Storage Lens tier** section of the dashboard configuration. If the dashboard uses a different delimiter, the option isn't available.

**To enable AWS Billing and Cost Management publishing for a new dashboard**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, under **S3 Storage Lens**, choose **Dashboards**.

1. Choose **Create dashboard**, and configure the general settings and dashboard scope. In the **Storage Lens tier** section, choose **Advanced tier**. For more information, see [Using the S3 console](storage_lens_creating_dashboard.md#storage_lens_console_creating).

1. On the metrics export and publishing step, under **Metrics publishing**, select **Billing and Cost Management publishing**.

1. In the **Publish to AWS Cost and Usage Reports (CUR)** panel, for **Minimum prefix level** and **Maximum prefix level**, enter the range of prefix levels that you want costs reported for. The default range is 1 through 3.

1. Choose **Next**, review the **Prefix levels** range, and then choose **Submit**.

**To enable AWS Billing and Cost Management publishing for an existing dashboard**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, under **S3 Storage Lens**, choose **Dashboards**.

1. Choose the dashboard that you want to update, choose **View dashboard configuration**, and then choose **Edit**.

1. If the dashboard uses the free tier, in the **Storage Lens tier** section, choose **Advanced tier**.

1. On the metrics export and publishing step, under **Metrics publishing**, select **Billing and Cost Management publishing**.

1. In the **Publish to AWS Cost and Usage Reports (CUR)** panel, enter the **Minimum prefix level** and **Maximum prefix level**.

1. Choose **Next**, review the **Prefix levels** range, and then choose **Submit**.

**Note**  
Each prefix level must be a whole number from 1 through 15. The maximum prefix level must be no less than the minimum prefix level, and the range can include at most 5 prefix levels.

After you complete either procedure, you've enabled AWS Billing and Cost Management publishing for the dashboard. To finish the setup, see [Next step: Enable split cost allocation data](#storage-lens-cur-next-steps).

## Using the AWS CLI
<a name="storage-lens-cur-enable-cli"></a>

The following AWS CLI example enables AWS Billing and Cost Management publishing for an S3 Storage Lens configuration. The `CostAndUsageReportsPublish` block enables the feature, and `PrefixDelimiter` must be `/`. To use this example, replace the `{{user input placeholders}}` with your own information.

```
aws s3control put-storage-lens-configuration --account-id={{111122223333}} --config-id={{your-configuration-id}} --region={{us-east-1}} --storage-lens-configuration=file://./config.json
```

The following example shows the contents of the `config.json` file:

```json
{
  "Id": "{{SampleS3StorageLensConfiguration}}",
  "AccountLevel": {
    "BucketLevel": {}
  },
  "PrefixDelimiter": "/",
  "CostAndUsageReportsPublish": {
    "PrefixLevel": {
      "IsEnabled": {{true}},
      "SelectionCriteria": {
        "MinDepth": {{1}},
        "MaxDepth": {{3}}
      }
    }
  },
  "IsEnabled": true
}
```

To use the default range (minimum depth 1 and maximum depth 3), omit `SelectionCriteria`, as shown in the following example:

```json
{
  "Id": "{{SampleS3StorageLensConfiguration}}",
  "AccountLevel": {
    "BucketLevel": {}
  },
  "PrefixDelimiter": "/",
  "CostAndUsageReportsPublish": {
    "PrefixLevel": {
      "IsEnabled": {{true}}
    }
  },
  "IsEnabled": true
}
```

## Using the AWS SDK for Java
<a name="storage-lens-cur-enable-sdk"></a>

The following AWS SDK for Java 2.x example enables AWS Billing and Cost Management publishing for an S3 Storage Lens configuration. The `CostAndUsageReportsPublish` configuration enables the feature, and the S3 Storage Lens configuration's `PrefixDelimiter` must be `/`. To use this example, replace the `{{user input placeholders}}` with your own information.

```JAVA
package aws.example.s3control;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.core.exception.SdkClientException;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.AccountLevel;
import software.amazon.awssdk.services.s3control.model.BucketLevel;
import software.amazon.awssdk.services.s3control.model.PutStorageLensConfigurationRequest;
import software.amazon.awssdk.services.s3control.model.StorageLensConfiguration;
import software.amazon.awssdk.services.s3control.model.StorageLensCostAndUsageReportsPrefixLevel;
import software.amazon.awssdk.services.s3control.model.StorageLensCostAndUsageReportsPublish;
import software.amazon.awssdk.services.s3control.model.StorageLensCostAndUsageReportsSelectionCriteria;

public class EnableBillingAndCostManagementPublishing {

    public static void main(String[] args) {
        String configurationId = "{{ConfigurationId}}";
        String sourceAccountId = "{{111122223333}}";

        try {
            AccountLevel accountLevel = AccountLevel.builder()
                    .bucketLevel(BucketLevel.builder().build())
                    .build();

            // Report costs for prefix levels 1 through 3. To use the default range
            // (MinDepth 1, MaxDepth 3), omit selectionCriteria.
            StorageLensCostAndUsageReportsSelectionCriteria selectionCriteria =
                    StorageLensCostAndUsageReportsSelectionCriteria.builder()
                            .minDepth({{1}})
                            .maxDepth({{3}})
                            .build();

            StorageLensCostAndUsageReportsPublish costAndUsageReportsPublish =
                    StorageLensCostAndUsageReportsPublish.builder()
                            .prefixLevel(StorageLensCostAndUsageReportsPrefixLevel.builder()
                                    .isEnabled({{true}})
                                    .selectionCriteria(selectionCriteria)
                                    .build())
                            .build();

            StorageLensConfiguration configuration = StorageLensConfiguration.builder()
                    .id(configurationId)
                    .accountLevel(accountLevel)
                    .prefixDelimiter("/") // Must be "/" for AWS Billing and Cost Management publishing.
                    .costAndUsageReportsPublish(costAndUsageReportsPublish)
                    .isEnabled({{true}})
                    .build();

            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.{{US_WEST_2}})
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();

            s3ControlClient.putStorageLensConfiguration(PutStorageLensConfigurationRequest.builder()
                    .accountId(sourceAccountId)
                    .configId(configurationId)
                    .storageLensConfiguration(configuration)
                    .build());

        } catch (AwsServiceException e) {
            // The call was transmitted successfully, but Amazon S3 couldn't process
            // it and returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3.
            e.printStackTrace();
        }
    }
}
```

## Using the REST API
<a name="storage-lens-cur-enable-api"></a>

To enable AWS Billing and Cost Management publishing by using the Amazon S3 REST API, include a `CostAndUsageReportsPublish` member in the `StorageLensConfiguration` of a `PutStorageLensConfiguration` request. For more information, see [PutStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfiguration.html) and [StorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensConfiguration.html) in the *Amazon S3 API Reference*.
<a name="storage-lens-cur-turning-off"></a>
**Disabling AWS Billing and Cost Management publishing**  
To disable AWS Billing and Cost Management publishing in the console, edit the dashboard and clear **Billing and Cost Management publishing**. With the AWS CLI or Amazon S3 REST API, set `IsEnabled` to `false` in `CostAndUsageReportsPublish` `PrefixLevel`. Prefix line items that already appear in the current month's Cost and Usage Report remain, but they don't receive new data.
<a name="storage-lens-cur-next-steps"></a>
**Next step: Enable split cost allocation data**  
After you enable AWS Billing and Cost Management publishing in S3 Storage Lens, enable split cost allocation data for Amazon S3 in your Cost and Usage Report in AWS Billing and Cost Management. For more information about enabling split cost allocation data, see [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) in the *AWS Data Exports User Guide*.