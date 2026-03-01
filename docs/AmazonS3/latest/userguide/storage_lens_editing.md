# Update an Amazon S3 Storage Lens dashboard

The Amazon S3 Storage Lens default dashboard is `default-account-dashboard`. This
dashboard is preconfigured by Amazon S3 to help you visualize summarized insights and trends for your
entire account's aggregated free and advanced metrics on the console. You can't modify the
default dashboard's configuration scope, but you can upgrade the metrics selection from the free
metrics to the paid advanced metrics and recommendations, configure the optional metrics export,
or even disable the default dashboard. The default dashboard can't be deleted, and can only be
disabled. For more information, see [Using the S3 console](storage_lens_console_deleting.md "storage_lens_console_deleting.md").

Use the following steps to update an Amazon S3 Storage Lens dashboard on the Amazon S3 console.

###### Step 1: Update your dashboard and configure your general settings

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens,
   Dashboards**.
3. Choose the dashboard that you want to edit.
4. Choose **View dashboard configuration**.
5. Choose **Edit**. You can now review the dashboard configuration,
   step by step. To make changes to any of the steps, you can click directly on the step
   using the left navigation. For instructions on how to update those steps,

###### Note

You can't change the following:

    * The dashboard name
    * The home Region

6. On the **Dashboard** page, in the **General**
   section, you can make changes to the following:
   - Choose **Enabled** or **Disabled** to update
     whether you're receiving daily metrics in your dashboard.
   - (Optional) You can choose to add **Tags** to your dashboard.
     You can use tags to manage permissions for your dashboard and track costs for
     S3 Storage Lens. For more information, see [Controlling access to AWS resources
     using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_ and
     [Using AWS-generated tags](../../../awsaccountbilling/latest/aboutv2/aws-tags.md "../../../awsaccountbilling/latest/aboutv2/aws-tags.md") in the _AWS Billing User Guide_.

###### Note

You can add up to 50 tags to your dashboard configuration. 7. Choose **Next** to save your changes and proceed.

###### Step 2: Update the dashboard scope

1. In the **Dashboard scope** section, update the Regions and buckets
   that you want S3 Storage Lens to include or exclude in the dashboard.

###### Note

    * You can either include or exclude Regions and buckets. This option is limited to
     Regions only when creating organization-level dashboards across member accounts in
     your organization.
    * You can choose up to 50 buckets to include or exclude.

2. Choose the buckets in your selected Regions that you want S3 Storage Lens to include or
   exclude. You can either include or exclude buckets, but not both. This option isn't
   available when you create organization-level dashboards.

###### Note

    * You can either include or exclude Regions and buckets. This option is limited
     to Regions only when creating organization-level dashboards across member accounts
     in your organization.
    * You can choose up to 50 buckets to include or exclude.

3. Choose **Next** to save your changes and proceed.

###### Step 3: Update your Storage Lens tier Configure the metrics selection

1. In the **Storage Lens tier**
   **Metrics selection** section, update the tier of metrics that you want
   to aggregate for this dashboard.

###### Note

    * If you're updating from the **Free tier** to the
     **Advanced tier**, you'll need to update your **Metrics
     aggregation** settings. To update your **Metrics aggregation
     settings**, see **Step 4: Update your metrics
     aggregation**.
    * If you're updating your Storage Lens tier from the **Advanced
     tier** to the **Free tier**, you won't need to update
     any **Metrics aggregation** settings. The **Metrics
     aggregation** feature only applies to **Advanced
     tier** metric categories.

2. To include free metrics aggregated at the bucket level and available for queries for
   14 days, choose **Free tier**.
3. To enable advanced metrics, choose **Advanced tier**. These options
   include prefix aggregation, Amazon CloudWatch publishing, and contextual recommendations. Data is
   available for queries for 15 months. Advanced metrics and recommendations have an
   additional cost. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

For more information about advanced metrics and free metrics, see [Metrics selection](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection"). 4. Under **Advanced metric categories**, choose the category of
metrics that you want to enable:

    * **Activity metrics**
    * **Detailed status code metrics**
    * **Cost optimization metrics**
    * **Data protection metrics**
    * **Performance metrics**

To preview which metrics are included in each category, use the drop-down arrow
button below the metrics category checkbox list. For more information about metrics
categories, see [Metrics categories](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types"). For a complete list of metrics,
see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md"). 5. Choose or specify a **Prefix delimiter** to distinguish levels
within each prefix. This value is used to identify each prefix level. The default value
in Amazon S3 is the "`/`" character, but your storage structure might use other
delimiter characters. 6. Choose **Next** to save your changes and proceed.

###### Step 4: (Optional) Update your metrics aggregation

1. Under **Additional metrics aggregation**, update which metrics you
   want to aggregate by choosing one of the following:
   - Prefix aggregation
   - Storage Lens group aggregation

2. If you've enabled **Prefix aggregation**, specify the minimum
   **Prefix threshold** for your dashboard and **Prefix
   depth**. Then, choose **Next** to save and proceed.
3. If you've enabled **Storage Lens group aggregation**, choose one of
   the following:
   - **Include Storage Lens groups**
   - **Exclude Storage Lens groups**

4. When you include Storage Lens groups in your aggregation, you can either
   **Include all Storage Lens groups in your home Region** or specify
   Storage Lens groups to include.
5. Choose **Next** to save your changes and proceed.

###### Step 5: (Optional) Update your metrics export and publishing settings

1. Under **Metrics publishing**, choose **CloudWatch
   publishing** if you want to access your Storage Lens metrics in your CloudWatch
   dashboard.

###### Note

Prefix-level metrics aren't available in CloudWatch. 2. Under **Metrics export**, choose which Storage Lens dashboard data
you want exported daily:

    * **Default metrics report**
    * **Expanded prefixes metrics report**

3. (Optional) If you chose **Default metrics report**, in the
   **Default metrics report** settings, choose the bucket type. You can
   export the report to either a general purpose S3 bucket or a read-only S3 table bucket.
   Based on the selected bucket type, update the **General purpose bucket
   destination settings** or **Table bucket destination
   settings** options.

###### Note

    * The **default metrics report** only includes prefixes within
     the set threshold and depth set in prefix aggregation settings. If your prefix
     aggregation isn't already configured, the threshold includes up to the 100 largest
     prefixes by size.
    * If you choose to specify an encryption key, you must choose an AWS KMS key
     (SSE-KMS) or Amazon S3 managed key (SSE-S3). If your destination bucket policy requires
     encryption, you must provide an encryption key for your metrics export. Without
     the encryption key, the export to S3 fails. For more information, see [Using an AWS KMS key to encrypt your metrics exports](storage_lens_encrypt_permissions.md "storage_lens_encrypt_permissions.md").

4. Choose **Next** to save your changes and proceed.
5. (Optional) If you chose **Expanded prefixes metrics report**, in
   the **Expanded prefixes metrics report** settings, choose the bucket
   type. You can export the report to either a general purpose S3 bucket or a read-only S3
   table bucket. Based on the selected bucket type, update the **General purpose
   bucket destination settings** or **Table bucket destination
   settings**.

###### Note

    * The **Expanded prefixes metrics report** includes prefixes in
     all buckets that are specified in your dashboard scope.
    * If you choose to specify an encryption key, you must choose an AWS KMS key
     (SSE-KMS) or Amazon S3 managed key (SSE-S3). If your destination bucket policy requires
     encryption, you must provide an encryption key for your metrics export. Without
     the encryption key, the export to S3 fails. For more information, see [Using an AWS KMS key to encrypt your metrics exports](storage_lens_encrypt_permissions.md "storage_lens_encrypt_permissions.md").

6. Choose **Next** to save your changes and proceed.

###### Step 6: Review and update your dashboard configuration

1. In the **General** section, review your settings. Choose
   **Edit** to make any changes.
2. In the **Dashboard scope** section, review your settings. Choose
   **Edit** to make any changes.
3. In the **Storage Lens tier** section, review your settings. Choose
   **Edit** to make any changes.
4. In the **Metrics aggregation** section, review your settings.
   Choose **Edit** to make any changes.
5. In the **Metrics export** section, review your settings. Choose
   **Edit** to make any changes.
6. After reviewing and confirming all your dashboard configuration settings, choose
   **Submit** to update your dashboard.
   After you've successfully updated your new Storage Lens dashboard, you can view your
   updated dashboard configuration listed under your Storage Lens
   **Dashboard** page.

###### Example

The following example command updates a Amazon S3 Storage Lens dashboard configuration. To use
these examples, replace the `user input
 placeholders` with your own information.

```
aws s3control put-storage-lens-configuration --account-id=`111122223333` --config-id=`example-dashboard-configuration-id` --region=`us-east-1` --storage-lens-configuration=`file://./config.json` --tags=`file://./tags.json`
```

###### Example– Update a Amazon S3 Storage Lens configuration with advanced metrics and recommendations

The following examples shows you how to update the default S3 Storage Lens configuration with
advanced metrics and recommendations in SDK for Java:

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.AccountLevel;
import com.amazonaws.services.s3control.model.ActivityMetrics;
import com.amazonaws.services.s3control.model.BucketLevel;
import com.amazonaws.services.s3control.model.Format;
import com.amazonaws.services.s3control.model.Include;
import com.amazonaws.services.s3control.model.OutputSchemaVersion;
import com.amazonaws.services.s3control.model.PrefixLevel;
import com.amazonaws.services.s3control.model.PrefixLevelStorageMetrics;
import com.amazonaws.services.s3control.model.PutStorageLensConfigurationRequest;
import com.amazonaws.services.s3control.model.S3BucketDestination;
import com.amazonaws.services.s3control.model.SSES3;
import com.amazonaws.services.s3control.model.SelectionCriteria;
import com.amazonaws.services.s3control.model.StorageLensAwsOrg;
import com.amazonaws.services.s3control.model.StorageLensConfiguration;
import com.amazonaws.services.s3control.model.StorageLensDataExport;
import com.amazonaws.services.s3control.model.StorageLensDataExportEncryption;
import com.amazonaws.services.s3control.model.StorageLensTag;

import java.util.Arrays;
import java.util.List;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class UpdateDefaultConfigWithPaidFeatures {

    public static void main(String[] args) {
        String configurationId = "default-account-dashboard"; // This configuration ID cannot be modified.
        String sourceAccountId = "`111122223333`";

        try {
            SelectionCriteria selectionCriteria = new SelectionCriteria()
                    .withDelimiter("`/`")
                    .withMaxDepth(`5`)
                    .withMinStorageBytesPercentage(`10.0`);
            PrefixLevelStorageMetrics prefixStorageMetrics = new PrefixLevelStorageMetrics()
                    .withIsEnabled(`true`)
                    .withSelectionCriteria(selectionCriteria);
            BucketLevel bucketLevel = new BucketLevel()
                    .withActivityMetrics(new ActivityMetrics().withIsEnabled(`true`))
                    .withPrefixLevel(new PrefixLevel().withStorageMetrics(prefixStorageMetrics));
            AccountLevel accountLevel = new AccountLevel()
                    .withActivityMetrics(new ActivityMetrics().withIsEnabled(`true`))
                    .withBucketLevel(bucketLevel);

            StorageLensConfiguration configuration = new StorageLensConfiguration()
                    .withId(configurationId)
                    .withAccountLevel(accountLevel)
                    .withIsEnabled(`true`);

            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            s3ControlClient.putStorageLensConfiguration(new PutStorageLensConfigurationRequest()
                    .withAccountId(sourceAccountId)
                    .withConfigId(configurationId)
                    .withStorageLensConfiguration(configuration)
            );

        } catch (AmazonServiceException e) {
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

For access to S3 Storage Lens groups or expanded prefixes, you must upgrade your dashboard to use
the advanced tier. Additional charges apply. For more information about the free and advanced
tiers, see [Metrics selection](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection"). For more information about S3 Storage Lens
groups, see [Working with S3 Storage Lens groups to filter and aggregate metrics](storage-lens-groups-overview.md "storage-lens-groups-overview.md").
