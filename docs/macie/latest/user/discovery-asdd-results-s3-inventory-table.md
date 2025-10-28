# Assessing data sensitivity with the

S3 buckets table

To review summary information for your Amazon Simple Storage Service (Amazon S3) buckets, you can use the **S3
buckets** table on the Amazon Macie console. By using the table, you can review and
analyze an inventory of your general purpose buckets in the current AWS Region, and drill down
to review detailed information and statistics for individual buckets. If you're the Macie administrator
for an organization, the table includes information about buckets that your member accounts own.
If you prefer to access and query the data programmatically, you can use the [DescribeBuckets](../APIReference/datasources-s3.md "../APIReference/datasources-s3.md")
operation of the Amazon Macie API.

On the console, you can sort and filter the table to customize your view. You can also
export data from the table to a comma-separated values (CSV) file. If you choose an S3 bucket in
the table, the details panel displays additional information about the bucket. This includes
details and statistics for settings and metrics that provide insight into the security and
privacy of the bucket’s data. If automated sensitive data discovery is enabled, it also includes data that captures the
results of automated discovery activities that Macie has performed thus far for the bucket.

###### To assess data sensitivity by using the S3 buckets table

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **S3 buckets**. The **S3
   buckets** page displays your bucket inventory.

By default, the page doesn't display data for buckets that are currently excluded from
automated sensitive data discovery. If you're the Macie administrator for an organization, it also doesn't display data for
accounts that automated sensitive data discovery is currently disabled for. To display this data, choose
**X** in the **Is monitored by automated discovery** filter
token below the filter box. 3. Choose table (
![The table view button, which is a button that displays three black horizontal lines.](images/btn-s3-table-view.png)
) at the top of the page. Macie displays the number of
buckets in your inventory and a table of the buckets. 4. To retrieve the latest bucket metadata from Amazon S3, choose refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) at the
top of the page.

If the information icon (
![The information icon, which is a blue circle that has a lowercase letter i in it.](images/icon-info-blue.png)
) appears next to any bucket names, we recommend
that you do this. This icon indicates that a bucket was created during the past 24 hours,
possibly after Macie last retrieved bucket and object metadata from Amazon S3 as part of the [daily refresh cycle](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh"). 5. In the **S3 buckets** table, review summary information about each bucket
in your inventory:

    * **Sensitivity** – The bucket's current sensitivity score. For
     information about the range of sensitivity scores that Macie defines, see [Sensitivity scoring for S3
     buckets](discovery-scoring-s3.md "discovery-scoring-s3.md").
    * **Bucket** – The name of the bucket.
    * **Account** – The account ID for the AWS account that owns the
     bucket.
    * **Classifiable objects** – The total number of objects that
     Macie can analyze to detect sensitive data in the bucket.
    * **Classifiable size** – The total storage size of all the
     objects that Macie can analyze to detect sensitive data in the bucket.


    This value doesn’t reflect the actual size of any compressed objects after they're
     decompressed. Also, if versioning is enabled for the bucket, this value is based on the
     storage size of the latest version of each object in the bucket.
    * **Monitored by job** – Whether you configured any sensitive data
     discovery jobs to periodically analyze objects in the bucket on a daily, weekly, or monthly
     basis.


    If the value for this field is *Yes*, the bucket is
     explicitly included in a periodic job or the bucket matched the criteria for a periodic job
     within the past 24 hours. In addition, the status of at least one of those jobs is not
     *Cancelled*. Macie updates this data on a daily
     basis.
    * **Latest job run** – If you configured any one-time or periodic
     sensitive data discovery jobs to analyze objects in the bucket, this field indicates the most
     recent date and time when one of those jobs started to run. Otherwise, a dash (–)
     appears in this field.

In the preceding data, objects are _classifiable_ if they
use a supported Amazon S3 storage class and they have a file name extension for a supported file or
storage format. You can detect sensitive data in the objects by using Macie. For more
information, see [Supported storage classes and
formats](discovery-supported-storage.md "discovery-supported-storage.md"). 6. To analyze your inventory by using the table, do any of the following:

    * To sort the table by a specific field, choose the column heading for the field. To
     change the sort order, choose the column heading again.
    * To filter the table and display only those buckets that have a specific value for a
     field, place your cursor in the filter box, and then add a filter condition for the field. To
     further refine the results, add filter conditions for additional fields. For more
     information, see [Filtering your S3 bucket
     inventory](monitoring-s3-inventory-filter.md "monitoring-s3-inventory-filter.md").
    * To review data sensitivity statistics and other information for a particular bucket,
     choose the bucket's name. Then refer to the details panel. For information about these
     details, see [Reviewing S3 bucket
     details](discovery-asdd-results-s3-inventory-details.md "discovery-asdd-results-s3-inventory-details.md").


    ###### Tip

    On the **Bucket details** tab of the panel, you can pivot and drill
     down on many of the fields. To show buckets that have the same value for a field, choose

    ![The zoom in icon, which is a magnifying glass that has a plus sign in it.](images/icon-magnifying-glass-plus-sign.png)
     in the field. To show buckets that have other values for a field,
     choose
    ![The zoom out icon, which is a magnifying glass that has a minus sign in it.](/images/macie/latest/user/images/icon-magnifying-glass-minus-sign.png)
     in the field.

7. To export data from the table to a CSV file, select the checkbox for each row to export,
   or select the checkbox in the selection column heading to select all rows. Then choose
   **Export to CSV** at the top of the page. You can export up to 50,000 rows
   from the table.
8. To perform deeper, more immediate analysis of objects in one or more buckets, select the
   checkbox for each bucket. Then choose **Create job**. For more information,
   see [Creating a sensitive data discovery job](discovery-jobs-create.md "discovery-jobs-create.md").
