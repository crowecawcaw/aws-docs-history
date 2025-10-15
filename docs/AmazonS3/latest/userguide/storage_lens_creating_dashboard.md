# Create an Amazon S3 Storage Lens
 dashboard

You can create additional S3 Storage Lens custom dashboards that can be scoped to your
 organization in AWS Organizations or to specific AWS Regions or buckets within an account. 

###### Note

Any updates to your dashboard configuration can take up to 48 hours to accurately display or visualize.

Use the following steps to create an Amazon S3 Storage Lens dashboard on the Amazon S3 console.

###### Step 1: Define the dashboard scope

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed
 AWS Region. Next, choose the Region that you want to switch to.
3. In the left navigation pane, under **S3 Storage Lens**, choose
 **Dashboards**.
4. Choose **Create dashboard**.
5. On the **Dashboard** page, in the **General**
 section, do the following:


	1. View the **Home Region** for your dashboard. The
	 home Region is the AWS Region where the configuration and metrics for this Storage Lens dashboard are stored.
	2. Enter a dashboard name. 
	
	
	Dashboard names must be fewer than 65 characters and must not contain special
	 characters or spaces. 
	
	
	###### Note
	
	You can't change this dashboard name after the dashboard is created.
	3. You can optionally choose to add **Tags** to your dashboard.
	 You can use tags to manage permissions for your dashboard and track costs for
	 S3 Storage Lens. 
	
	
	For more information, see [Controlling access using resource
	 tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html") in the *IAM User Guide* and [AWS-Generated Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html") in the *AWS Billing User Guide*.
	
	
	###### Note
	
	You can add up to 50 tags to your dashboard configuration.
6. In the **Dashboard scope** section, do the following:


	1. Choose the Regions and buckets that you want S3 Storage Lens to include or exclude in
	 the dashboard.
	2. Choose the buckets in your selected Regions that you want S3 Storage Lens to include or
	 exclude. You can either include or exclude buckets, but not both. This option is not
	 available when you create organization-level dashboards.###### Note



	* You can either include or exclude Regions and buckets. This option is limited to
	 Regions only when creating organization-level dashboards across member accounts in
	 your organization.
	* You can choose up to 50 buckets to include or exclude.
###### Step 2: Configure the metrics selection

1. In the **Metrics selection** section, choose the type of metrics
 that you want to aggregate for this dashboard.




	* To include free metrics aggregated at the bucket level and available for queries
	 for 14 days, choose **Free metrics**.
	* To enable advanced metrics and other advanced options, choose **Advanced
	 metrics and recommendations**. These options include advanced prefix
	 aggregation, Amazon CloudWatch publishing, and contextual recommendations. Data is available
	 for queries for 15 months. Advanced metrics and recommendations have an additional
	 cost. For more information, see  [Amazon S3
	 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). 
	
	
	For more information about advanced metrics and free metrics, see [Metrics selection](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection").
2. Under **Advanced metrics and recommendations features**, select the
 options that you want to enable:




	* **Advanced metrics**
	* **CloudWatch publishing**
	* **Prefix aggregation**
###### Important

If you enable prefix aggregation for your S3 Storage Lens configuration, prefix-level
 metrics will not be published to CloudWatch. Only bucket, account, and organization-level
 S3 Storage Lens metrics are published to CloudWatch.
3. If you enabled **Advanced metrics**, select the **Advanced
 metrics categories** that you want to display in your S3 Storage Lens
 dashboard:




	* **Activity metrics**
	* **Detailed status code metrics**
	* **Advanced cost optimization metrics**
	* **Advanced data protection metrics**
For more information about metrics categories, see [Metrics categories](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types"). For a complete list of metrics,
 see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").
4. If you chose to enable prefix aggregation, configure the following:


	1. Choose the minimum prefix threshold size for this dashboard. 
	
	
	For example, a prefix threshold of 5 percent indicates that prefixes that make
	 up 5 percent or more of the bucket's total storage size will be aggregated.
	2. Choose the prefix depth. 
	
	
	This setting indicates the maximum number of levels up to which the prefixes are
	 evaluated. The prefix depth must be less than 10.
	3. Enter a prefix delimiter character. 
	
	
	This value is used to identify each prefix level. The default value in Amazon S3 is
	 the `/` character, but your storage structure might use other delimiter
	 characters.
###### (Optional) Step 3: Export metrics for the dashboard

1. In the **Metrics export** section, to create a metrics export that
 will be placed daily in a destination bucket of your choice, choose
 **Enable**.
2. If you enabled the metrics export, choose the output format of your daily metrics
 export: **CSV** or **Apache Parquet**. 


Parquet is an open source file format for Hadoop that stores nested
 data in a flat columnar format.
3. Choose the destination S3 bucket for your metrics export.
4. Choose the destination S3 bucket (format:
 `s3://`bucket-name`/`prefix``). 


The bucket must be in the home Region of your S3 Storage Lens dashboard. The S3 console
 shows you the **Destination bucket permission** that will be added by
 Amazon S3 to the destination bucket policy. Amazon S3 updates the bucket policy on the destination
 bucket to allow S3 to place data in that bucket.
5. (Optional) To enable server-side encryption for your metrics export, choose
 **Specify an encryption key**. Then, choose the **Encryption
 type**: **Amazon S3 managed keys (SSE-S3)** or
 **AWS Key Management Service key (SSE-KMS)**. 


You can choose between an [Amazon S3 managed
 key](UsingServerSideEncryption.md "UsingServerSideEncryption.md") (SSE-S3) and an [AWS Key Management Service (AWS KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md") key
 (SSE-KMS).
6. (Optional) To specify an AWS KMS key, you must choose a KMS key or enter a key
 Amazon Resource Name (ARN).


If you choose a customer managed key, you must grant S3 Storage Lens permission to encrypt in the
 AWS KMS key policy. For more information, see [Using an AWS KMS key to encrypt your
 metrics exports](storage_lens_encrypt_permissions.md "storage_lens_encrypt_permissions.md").
7. Choose **Create dashboard**.
The following example command creates a Amazon S3 Storage Lens configuration with tags. To use these
 examples, replace the ``user input placeholders`` with
 your own information.


```
aws s3control put-storage-lens-configuration --account-id=`111122223333` --config-id=`example-dashboard-configuration-id` --region=`us-east-1` --storage-lens-configuration=`file://./config.json` --tags=`file://./tags.json`
```
The following example command creates a Amazon S3 Storage Lens configuration without tags. To use these
 examples, replace the ``user input placeholders`` with
 your own information.


```
aws s3control put-storage-lens-configuration --account-id=`222222222222` --config-id=`your-configuration-id` --region=`us-east-1` --storage-lens-configuration=`file://./config.json`
```
###### Example – Create and update an Amazon S3 Storage Lens configuration

The following example creates and updates an Amazon S3 Storage Lens configuration in SDK for Java:


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
import com.amazonaws.services.s3control.model.CloudWatchMetrics;
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

public class CreateAndUpdateDashboard {

    public static void main(String[] args) {
        String configurationId = "`ConfigurationId`";
        String sourceAccountId = "`111122223333`";
        String exportAccountId = "`Destination Account ID`";
        String exportBucketArn = "arn:aws:s3:::`destBucketName`"; // The destination bucket for your metrics export must be in the same Region as your S3 Storage Lens configuration.
        String awsOrgARN = "arn:aws:organizations::`123456789012`:organization/`o-abcdefgh`";
        Format exportFormat = Format.CSV;

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
                    .withAdvancedCostOptimizationMetrics(new AdvancedCostOptimizationMetrics().withIsEnabled(`true`))
                    .withAdvancedDataProtectionMetrics(new AdvancedDataProtectionMetrics().withIsEnabled(`true`))
                    .withDetailedStatusCodesMetrics(new DetailedStatusCodesMetrics().withIsEnabled(`true`))
                    .withPrefixLevel(new PrefixLevel().withStorageMetrics(prefixStorageMetrics));
            AccountLevel accountLevel = new AccountLevel()
                    .withActivityMetrics(new ActivityMetrics().withIsEnabled(`true`))
                    .withAdvancedCostOptimizationMetrics(new AdvancedCostOptimizationMetrics().withIsEnabled(`true`))
                    .withAdvancedDataProtectionMetrics(new AdvancedDataProtectionMetrics().withIsEnabled(`true`))
                    .withDetailedStatusCodesMetrics(new DetailedStatusCodesMetrics().withIsEnabled(`true`))
                    .withBucketLevel(bucketLevel);

            Include include = new Include()
                    .withBuckets(Arrays.asList("arn:aws:s3:::`bucketName`"))
                    .withRegions(Arrays.asList("`us-west-2`"));

            StorageLensDataExportEncryption exportEncryption = new StorageLensDataExportEncryption()
                    .withSSES3(new SSES3());
            S3BucketDestination s3BucketDestination = new S3BucketDestination()
                    .withAccountId(exportAccountId)
                    .withArn(exportBucketArn)
                    .withEncryption(exportEncryption)
                    .withFormat(exportFormat)
                    .withOutputSchemaVersion(OutputSchemaVersion.V_1)
                    .withPrefix("Prefix");
            CloudWatchMetrics cloudWatchMetrics = new CloudWatchMetrics()
                    .withIsEnabled(`true`);
            StorageLensDataExport dataExport = new StorageLensDataExport()
                    .withCloudWatchMetrics(cloudWatchMetrics)
                    .withS3BucketDestination(s3BucketDestination);

            StorageLensAwsOrg awsOrg = new StorageLensAwsOrg()
                    .withArn(`awsOrgARN`);

            StorageLensConfiguration configuration = new StorageLensConfiguration()
                    .withId(configurationId)
                    .withAccountLevel(accountLevel)
                    .withInclude(include)
                    .withDataExport(dataExport)
                    .withAwsOrg(awsOrg)
                    .withIsEnabled(`true`);

            List<StorageLensTag> tags = Arrays.asList(
                    new StorageLensTag().withKey("`key-1`").withValue("`value-1`"),
                    new StorageLensTag().withKey("`key-2`").withValue("`value-2`")
            );

            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            s3ControlClient.putStorageLensConfiguration(new PutStorageLensConfigurationRequest()
                    .withAccountId(sourceAccountId)
                    .withConfigId(configurationId)
                    .withStorageLensConfiguration(configuration)
                    .withTags(tags)
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
To gain further visibility into your storage, you can create one or more S3 Storage Lens groups
 and attach them to your dashboard. An S3 Storage Lens group is a custom defined filter for objects based
 on prefixes, suffixes, object tags, object size, object age, or a combination of these
 filters. 

You can use S3 Storage Lens groups to gain granular visibility into large shared buckets, such
 as data lakes, to make better-informed business decisions. For example, you can streamline
 storage allocation and optimize cost reporting by breaking down storage usage to specific
 groups of objects for individual projects and cost centers within a bucket or across
 multiple buckets. 

To use S3 Storage Lens groups, you must upgrade your dashboard to use advanced metrics and
 recommendations. For more information about S3 Storage Lens groups, see [Working with S3 Storage Lens groups to filter and aggregate metrics](storage-lens-groups-overview.md "storage-lens-groups-overview.md").
