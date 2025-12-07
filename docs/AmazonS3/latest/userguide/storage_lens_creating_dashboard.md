# Create an Amazon S3 Storage Lens dashboard

You can create additional S3 Storage Lens custom dashboards that can be scoped to your organization
in AWS Organizations or to specific AWS Regions or buckets within an account.

###### Note

Any updates to your dashboard configuration can take up to 48 hours to accurately display
or visualize.

Use the following steps to create an Amazon S3 Storage Lens dashboard on the Amazon S3 console.

###### Step 1: Configure general settings

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently
   displayed AWS Region. Next, choose the Region that you want to switch to.
3. In the left navigation pane, under **S3 Storage Lens**, choose
   **Dashboards**.
4. Choose **Create dashboard**.
5. On the **Dashboard** page, in the **General**
   section, do the following:
   1. View the **Home Region** for your dashboard. The home Region is
      the AWS Region where the configuration and metrics for this Storage Lens dashboard
      are stored.
   2. Enter a dashboard name.

   Dashboard names must be fewer than 65 characters and must not contain special
   characters or spaces.

   ###### Note

   You can't change this dashboard name after the dashboard is created. 3. Choose **Enabled** to display updated daily metrics in your
   dashboard. 4. (Optional) You can choose to add **Tags** to your dashboard.
   You can use tags to manage permissions for your dashboard and track costs for
   S3 Storage Lens. For more information, see [Controlling access to AWS resources
   using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_ and
   [Using AWS-generated tags](../../../awsaccountbilling/latest/aboutv2/aws-tags.md "../../../awsaccountbilling/latest/aboutv2/aws-tags.md") in the _AWS Billing User Guide_.

   ###### Note

   You can add up to 50 tags to your dashboard configuration.

6. Choose **Next** to save your changes and proceed.

###### Step 2: Define the dashboard scope

1. In the **Dashboard scope** section, choose the Regions and buckets
   that you want S3 Storage Lens to include or exclude in the dashboard.
2. Choose the buckets in your selected Regions that you want S3 Storage Lens to include or
   exclude. You can either include or exclude buckets, but not both. This option isn't
   available when you create organization-level dashboards.

###### Note

    * You can either include or exclude Regions and buckets. This option is limited to
     Regions only when creating organization-level dashboards across member accounts in
     your organization.
    * You can choose up to 50 buckets to include or exclude.

3. Choose **Next** to save your changes and proceed.

###### Step 3: Choose your Storage Lens tier

1.  In the **Storage Lens tier** section, choose the tier of features
    that you want to aggregate for this dashboard.
    1. To include free metrics aggregated at the bucket level and available for queries
       for 14 days, choose **Free tier**.
    2. To enable advanced metrics, choose **Advanced tier**. These
       options include prefix or Storage Lens groups aggregation, Amazon CloudWatch publishing, the
       expanded prefixes report, and contextual recommendations. Data is available for
       queries for 15 months. Advanced metrics and recommendations have an additional cost.
       For more information, see [Amazon S3
       pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

    For more information about advanced metrics and free metrics, see [Metrics selection](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection").

2.  Under **Advanced metric categories**, select the category of
    metrics that you want to enable:

        * **Activity metrics**
        * **Detailed status code metrics**
        * **Cost optimization metrics**
        * **Data protection metrics**
        * **Performance metrics**

    To preview which metrics are included in each category, use the drop-down arrow
    button below the metrics category checkbox list. For more information about metrics
    categories, see [Metrics categories](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types"). For a complete list of metrics,
    see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

3.  Choose or specify a **Prefix delimiter** to distinguish levels
    within each prefix. This value is used to identify each prefix level. The default value
    in Amazon S3 is the "`/`" character, but your storage structure might use other
    delimiter characters.
4.  Choose **Next** to save your changes and proceed.

###### Step 4: (Optional) Choose your metrics aggregation

1. Under **Additional metrics aggregation**, choose which metrics you
   want to aggregate:
   - Prefix aggregation
   - Storage Lens group aggregation

2. If you've enabled **Prefix aggregation**, specify the minimum
   **Prefix threshold** for your dashboard and **Prefix
   depth**. Then, choose **Next** to save and proceed.

###### Note

The **Prefix depth** setting determines how many hierarchical
levels deep S3 Storage Lens will analyze your object prefixes, with a maximum limit of 10
levels. The **Prefix threshold** specifies the minimum percentage of
total storage that a prefix must represent before it's included in Storage Lens
metrics. 3. If you've enabled **Storage Lens group aggregation**, choose one of
the following:

    * **Include Storage Lens groups**
    * **Exclude Storage Lens groups**

4. When you include Storage Lens groups in your aggregation, you can either
   **Include all Storage Lens groups in your home Region** or specify
   Storage Lens groups to include.
5. Choose **Next** to save your changes and proceed.

###### Step 5: (Optional) Choose your metrics export and publishing settings

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
   export the report to either a general purpose Amazon S3 bucket or AWS-managed S3 table
   bucket. Based on the selected bucket type, update the **General purpose bucket
   destination settings** or **Table bucket destination
   settings** options.

###### Note

The **default metrics report** only includes prefixes within the
set threshold and depth set in prefix aggregation settings.

If you choose to specify an encryption key, you must choose an AWS KMS key (SSE-KMS)
or Amazon S3 managed key (SSE-S3). If your destination bucket policy requires encryption,
you must provide an encryption key for your metrics export. Without the encryption
key, the export to S3 fails. For more information, see [Using an AWS KMS key to encrypt your
metrics exports](storage_lens_encrypt_permissions.md "storage_lens_encrypt_permissions.md"). 4. (Optional) If you chose **Expanded prefixes metrics report**, in
the **Expanded prefixes metrics report** settings, choose the bucket
type. You can export the report to either a general purpose Amazon S3 bucket or a read-only
S3 table bucket. Based on the selected bucket type, update the **General purpose
bucket destination settings** or **Table bucket destination
settings**.

###### Note

The **Expanded prefixes metrics report** includes all prefixes up
to prefix depth 50 in all selected buckets that are specified in your dashboard
scope.

If you choose to specify an encryption key, you must choose an AWS KMS key (SSE-KMS)
or Amazon S3 managed key (SSE-S3). If your destination bucket policy requires encryption,
you must provide an encryption key for your metrics export. Without the encryption
key, the export to S3 fails. For more information, see [Using an AWS KMS key to encrypt your
metrics exports](storage_lens_encrypt_permissions.md "storage_lens_encrypt_permissions.md"). 5. Choose **Next** to save your changes and proceed. 6. Review everything on the **Review and Create** page. If there are
no additional changes, choose **Next** to save your changes and to
create your dashboard.

###### Step 6: Review your dashboard configuration and create your dashboard

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
   **Submit** to create your dashboard.
   After you've successfully created your new Storage Lens dashboard, you can view your new
   dashboard listed under your Storage Lens **Dashboard** page.

The following example command creates a Amazon S3 Storage Lens configuration with tags. To use
these examples, replace the `user input
 placeholders` with your own information.

```
aws s3control put-storage-lens-configuration --account-id=`111122223333` --config-id=`example-dashboard-configuration-id` --region=`us-east-1` --storage-lens-configuration=`file://./config.json` --tags=`file://./tags.json`
```

The following example command creates a Amazon S3 Storage Lens configuration without tags. To
use these examples, replace the `user input
 placeholders` with your own information.

```
aws s3control put-storage-lens-configuration --account-id=`222222222222` --config-id=`your-configuration-id` --region=`us-east-1` --storage-lens-configuration=`file://./config.json`
```

###### Example – Create and update an Amazon S3 Storage Lens configuration

The following example creates and updates an Amazon S3 Storage Lens configuration in
SDK for Java:

```
package aws.example.s3control;

import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.core.exception.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.AccountLevel;
import software.amazon.awssdk.services.s3control.model.ActivityMetrics;
import software.amazon.awssdk.services.s3control.model.AdvancedCostOptimizationMetrics;
import software.amazon.awssdk.services.s3control.model.AdvancedDataProtectionMetrics;
import software.amazon.awssdk.services.s3control.model.AdvancedPerformanceMetrics;
import software.amazon.awssdk.services.s3control.model.BucketLevel;
import software.amazon.awssdk.services.s3control.model.CloudWatchMetrics;
import software.amazon.awssdk.services.s3control.model.DetailedStatusCodesMetrics;
import software.amazon.awssdk.services.s3control.model.Format;
import software.amazon.awssdk.services.s3control.model.Include;
import software.amazon.awssdk.services.s3control.model.OutputSchemaVersion;
import software.amazon.awssdk.services.s3control.model.PrefixLevel;
import software.amazon.awssdk.services.s3control.model.PrefixLevelStorageMetrics;
import software.amazon.awssdk.services.s3control.model.PutStorageLensConfigurationRequest;
import software.amazon.awssdk.services.s3control.model.S3BucketDestination;
import software.amazon.awssdk.services.s3control.model.SSES3;
import software.amazon.awssdk.services.s3control.model.SelectionCriteria;
import software.amazon.awssdk.services.s3control.model.StorageLensAwsOrg;
import software.amazon.awssdk.services.s3control.model.StorageLensConfiguration;
import software.amazon.awssdk.services.s3control.model.StorageLensDataExport;
import software.amazon.awssdk.services.s3control.model.StorageLensDataExportEncryption;
import software.amazon.awssdk.services.s3control.model.StorageLensExpandedPrefixesDataExport;
import software.amazon.awssdk.services.s3control.model.StorageLensTableDestination;
import software.amazon.awssdk.services.s3control.model.StorageLensTag;

import java.util.Arrays;
import java.util.List;

public class CreateAndUpdateDashboard {

    public static void main(String[] args) {
        String configurationId = "`ConfigurationId`";
        String sourceAccountId = "`111122223333`";
        String exportAccountId = "`Destination Account ID`";
        String exportBucketArn = "arn:aws:s3:::`destBucketName`"; // The destination bucket for your metrics export must be in the same Region as your S3 Storage Lens configuration.
        String awsOrgARN = "arn:aws:organizations::`123456789012`:organization/`o-abcdefgh`";
        Format exportFormat = Format.CSV;

        try {
            SelectionCriteria selectionCriteria = SelectionCriteria.builder()
                    .delimiter("`/`")
                    .maxDepth(`5`)
                    .minStorageBytesPercentage(`10.0`)
                    .build();

            PrefixLevelStorageMetrics prefixStorageMetrics = PrefixLevelStorageMetrics.builder()
                    .isEnabled(`true`)
                    .selectionCriteria(selectionCriteria)
                    .build();

            BucketLevel bucketLevel = BucketLevel.builder()
                    .activityMetrics(ActivityMetrics.builder().isEnabled(`true`).build())
                    .advancedCostOptimizationMetrics(AdvancedCostOptimizationMetrics.builder().isEnabled(`true`).build())
                    .advancedDataProtectionMetrics(AdvancedDataProtectionMetrics.builder().isEnabled(`true`).build())
                    .advancedPerformanceMetrics(AdvancedPerformanceMetrics.builder().isEnabled(`true`).build())
                    .detailedStatusCodesMetrics(DetailedStatusCodesMetrics.builder().isEnabled(`true`).build())
                    .prefixLevel(PrefixLevel.builder().storageMetrics(prefixStorageMetrics).build())
                    .build();

            AccountLevel accountLevel = AccountLevel.builder()
                    .activityMetrics(ActivityMetrics.builder().isEnabled(`true`).build())
                    .advancedCostOptimizationMetrics(AdvancedCostOptimizationMetrics.builder().isEnabled(`true`).build())
                    .advancedPerformanceMetrics(AdvancedPerformanceMetrics.builder().isEnabled(`true`).build())
                    .advancedDataProtectionMetrics(AdvancedDataProtectionMetrics.builder().isEnabled(`true`).build())
                    .detailedStatusCodesMetrics(DetailedStatusCodesMetrics.builder().isEnabled(`true`).build())
                    .bucketLevel(bucketLevel)
                    .build();

            Include include = Include.builder()
                    .buckets(Arrays.asList("arn:aws:s3:::`bucketName`"))
                    .regions(Arrays.asList("`us-west-2`"))
                    .build();

            StorageLensDataExportEncryption exportEncryption = StorageLensDataExportEncryption.builder()
                    .sses3(SSES3.builder().build())
                    .build();

            S3BucketDestination s3BucketDestination = S3BucketDestination.builder()
                    .accountId(exportAccountId)
                    .arn(exportBucketArn)
                    .encryption(exportEncryption)
                    .format(exportFormat)
                    .outputSchemaVersion(OutputSchemaVersion.V_1)
                    .prefix("`Prefix`")
                    .build();

            StorageLensTableDestination s3TablesDestination = StorageLensTableDestination.builder()
                    .encryption(exportEncryption)
                    .isEnabled(`true`)
                    .build();

            CloudWatchMetrics cloudWatchMetrics = CloudWatchMetrics.builder()
                    .isEnabled(`true`)
                    .build();

            StorageLensDataExport dataExport = StorageLensDataExport.builder()
                    .cloudWatchMetrics(cloudWatchMetrics)
                    .s3BucketDestination(s3BucketDestination)
                    .storageLensTableDestination(s3TablesDestination)
                    .build();

            StorageLensAwsOrg awsOrg = StorageLensAwsOrg.builder()
                    .arn(awsOrgARN)
                    .build();

            StorageLensExpandedPrefixesDataExport expandedPrefixesDataExport = StorageLensExpandedPrefixesDataExport.builder()
                    .s3BucketDestination(s3BucketDestination)
                    .storageLensTableDestination(s3TablesDestination)
                    .build();

            StorageLensConfiguration configuration = StorageLensConfiguration.builder()
                    .id(configurationId)
                    .accountLevel(accountLevel)
                    .include(include)
                    .dataExport(dataExport)
                    .awsOrg(awsOrg)
                    .expandedPrefixesDataExport(expandedPrefixesDataExport)
                    .prefixDelimiter("`/`")
                    .isEnabled(`true`)
                    .build();

            List<StorageLensTag> tags = Arrays.asList(
                    StorageLensTag.builder().key("`key-1`").value("`value-1`").build(),
                    StorageLensTag.builder().key("`key-2`").value("`value-2`").build()
            );

            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();

            s3ControlClient.putStorageLensConfiguration(PutStorageLensConfigurationRequest.builder()
                    .accountId(sourceAccountId)
                    .configId(configurationId)
                    .storageLensConfiguration(configuration)
                    .tags(tags)
                    .build()
            );

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

For access to S3 Storage Lens groups or expanded prefixes, you must upgrade your dashboard to use
the advanced tier. Additional charges apply. For more information about the
free and advanced tiers, see [Metrics selection](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection"). For more information about S3 Storage Lens
groups, see [Working with S3 Storage Lens groups to filter and aggregate metrics](storage-lens-groups-overview.md "storage-lens-groups-overview.md").
