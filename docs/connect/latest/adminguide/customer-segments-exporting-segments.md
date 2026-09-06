

# Export customer segments to a CSV file in Connect Customer
<a name="customer-segments-exporting-segments"></a>

 From the **Customer segments** page in the Connect Customer admin website, you can export an existing segment to a file on your computer. When you do, Customer Profiles exports all of the profile attributes that's associated with the profiles in the customer segment to a CSV file. 

**To export a customer segment**

1.  On Customer segments page, choose **Export CSV** in the actions dropdown.

![The Customer segments page, the Export CSV option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-exporting-segments-1.png)


Alternatively, you can navigate to the **View details** page, and choose **Next actions**, **Download**.

![The segment details page for a segment, the Next actions option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-exporting-segments-2.png)


**Note**  
The Connect Customer admin website supports exporting a customer segment that contains up to 350,000 profiles. If you need to export a segment that contains a large number of profiles, use the `CreateSegmentSnapshot` operation in Customer Profiles API. The `CreateSegmentSnapshot` operation supports exporting a segment in ORC, JSONL, and CSV files to an S3 bucket. Note that the API outputs a test file in addition to the exported segment in the bucket.

1. After the export job begins, keep the window or tab containing the download open until the process completes.

![A message that the segment is being exported.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-exporting-segments-3.png)


1. After the export job completes, the Connect Customer admin website automatically starts downloading the file. 

![A message that the segment has been successfully downloaded.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-exporting-segments-4.png)


 The exported CSV file contains all [standard and customer profile attributes](https://docs.aws.amazon.com/connect/latest/adminguide/standard-profile-definition.html) populated across the exported profiles.