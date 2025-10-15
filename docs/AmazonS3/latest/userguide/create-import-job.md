# Importing objects into a directory bucket

After you create a directory bucket in Amazon S3, you can populate the new bucket with data by
 using the import action. Import is a streamlined method for creating S3 Batch Operations jobs to copy
 objects from general purpose buckets to directory buckets. 

###### Note

The following limitations apply to import jobs:


* The source bucket and the destination bucket must be in the same AWS Region and
 account.
* The source bucket cannot be a directory bucket.
* Objects larger than 5GB are not supported and will be omitted from the copy
 operation.
* Objects in the Glacier Flexible Retrieval, Glacier Deep Archive, Intelligent-Tiering
 Archive Access tier, and Intelligent-Tiering Deep Archive tier storage classes must be
 restored before they can be imported.
* Imported objects with MD5 checksum algorithms are converted to use CRC32
 checksums.
* Imported objects use the Express One Zone storage class, which has a different pricing
 structure than the storage classes used by general purpose buckets. Consider this
 difference in cost when importing large numbers of objects.
When you configure an import job, you specify the source bucket or prefix where the existing
 objects will be copied from. You also provide an AWS Identity and Access Management (IAM) role that has permissions to
 access the source objects. Amazon S3 then starts a Batch Operations job that copies the objects and
 automatically applies appropriate storage class and checksum settings.

To configure import jobs, you use the Amazon S3 console.


## Using the Amazon S3 console


###### To import objects into a directory bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**, and then choose the
 **Directory** buckets tab. Choose the option button next to the
 directory bucket that you want to import objects into.
3. Choose **Import**.
4. For **Source**, enter the general purpose bucket (or bucket path
 including prefix) that contains the objects that you want to import. To choose an existing
 general purpose bucket from a list, choose **Browse S3**.
5. For **Permission to access and copy source objects**, do one of the
 following to specify an IAM role with the permissions necessary to import your source
 objects:




	* To allow Amazon S3 to create a new IAM role on your behalf, choose **Create
	 new IAM role**.
	* To choose an existing IAM role from a list, choose **Choose from
	 existing IAM roles**.
	* To specify an existing IAM role by entering its Amazon Resource Name (ARN),
	 choose **Enter IAM role ARN**, then enter the ARN in the
	 corresponding field.
6. Review the information that's displayed in the **Destination** and
 **Copied object settings** sections. If the information in the
 **Destination** section is correct, choose **Import**
 to start the copy job.


The Amazon S3 console displays the status of your new job on the **Batch
 Operations** page. For more information about the job, choose the option button
 next to the job name, and then on the **Actions** menu, choose
 **View details**. To open the directory bucket that the objects will be
 imported into, choose **View import destination**.
