

# Viewing replication metrics in S3 Storage Lens dashboards
<a name="viewing-replication-metrics-storage-lens"></a>

In addition to [S3 Replication metrics](repl-metrics.md), you can use the replication-related Data Protection metrics provided by S3 Storage Lens. S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide visibility into object-storage usage and activity. For more information, see [Using S3 Storage Lens to protect your data](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-data-protection.html#storage-lens-data-protection-replication-rule). 

S3 Storage Lens has two tiers of metrics: free metrics, and advanced metrics and recommendations, which you can upgrade to for an additional charge. With advanced metrics and recommendations, you can access additional metrics and features for gaining insight into your storage. For information about S3 Storage Lens pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing). 

If you use the free metrics in S3 Storage Lens, you can see metrics such as the total number of bytes that are replicated from the source bucket or the count of replicated objects from the source bucket. 

To audit your overall replication stance, you can enable advanced metrics in S3 Storage Lens. With advanced metrics in S3 Storage Lens, you can see how many replication rules you have of various types, including the count of replication rules with a replication destination that's not valid. 

For a complete list of S3 Storage Lens metrics, including which replication metrics are in each tier, see the [S3 Storage Lens metrics glossary](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html?icmpid=docs_s3_user_guide_replication.html). 

**Prerequisites**  
Create a [live replication configuration](replication-how-setup.md) or an [S3 Batch Replication job](s3-batch-replication-batch.md). 

**To view replication metrics in Amazon S3 Storage Lens**

1. Create an S3 Storage Lens dashboard. For step-by-step instructions, see [Using the S3 console](storage_lens_creating_dashboard.md#storage_lens_console_creating).

1. (Optional) During your dashboard setup, if you want to see all S3 Storage Lens replication metrics, select **Advanced metrics and recommendations** and then select **Advanced data protection metrics**. For a complete list of metrics, see the [S3 Storage Lens metrics glossary](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html?icmpid=docs_s3_user_guide_replication.html).

   If you enable advanced metrics and recommendations, you can gain further insights into your replication configurations. For example, you can use S3 Storage Lens replication rule count metrics to get detailed information about your buckets that are configured for replication. This information includes replication rules within and across buckets and Regions. For more information, see [Count the total number of replication rules for each bucket](storage-lens-data-protection.md#storage-lens-data-protection-replication-rule).

1. After you've created your dashboard, open the dashboard, and choose the **Buckets** tab.

1. Scroll down to the **Buckets** section. Under **Metrics categories**, choose **Data protection**. Then clear **Summary**.

1. To filter the **Buckets** list to display only replication metrics, choose the **Preferences** icon (![The Preferences icon in the S3 Storage Lens dashboard.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/preferences.png)).

1. Clear the toggles for all data-protection metrics until only the replication metrics remain selected.

1. (Optional) Under **Page size**, choose the number of buckets to display in the list.

1. Choose **Continue**.