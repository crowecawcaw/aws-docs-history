# Step 3: Importing data into a S3 Express One Zone directory

bucket

To complete this step, you must have a general purpose bucket that contains objects and is located in the same AWS Region as your
directory bucket.

After you create a directory bucket in Amazon S3, you can populate the new bucket
with data by using the Import action in the Amazon S3 console. Import simplifies copying
data into directory buckets by letting you choose a prefix or a general purpose bucket
to Import data from without having to specify all of the objects to copy individually.
Import uses S3 Batch Operations which copies the objects in the selected prefix or
general purpose bucket. You can monitor the progress of the Import copy job through the
S3 Batch Operations job details page.

###### To use the Import action

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed
   AWS Region. Next, choose the Region associated with the Availability Zone in
   which your directory bucket is located.
3. In the left navigation pane, choose **Directory buckets**.
4. Choose the option button next to the name of the bucket that you want to import objects into.
5. Choose **Import**.
6. For **Source**, enter the general purpose bucket (or bucket path
   including prefix) that contains the objects that you want to import. To choose an existing
   general purpose bucket from a list, choose **Browse S3**.
7. In the **Permissions** section, you can choose to have an IAM role auto-generated. Alternatively, you
   can select an IAM role from a list, or directly enter an IAM role ARN.
   - To allow Amazon S3 to create a new IAM role on your behalf, choose **Create
     new IAM role**.

   ###### Note

   If your source objects are encrypted with server-side encryption with AWS Key Management Service
   (AWS KMS) keys (SSE-KMS), don't choose the **Create new IAM role**
   option. Instead, specify an existing IAM role that has the
   `kms:Decrypt` permission.

   Amazon S3 will use this permission to decrypt your objects. During the import
   process, Amazon S3 will then re-encrypt those objects by using server-side encryption
   with Amazon S3 managed keys (SSE-S3).
   - To choose an existing IAM role from a list, choose **Choose from
     existing IAM roles**.
   - To specify an existing IAM role by entering its Amazon Resource Name (ARN),
     choose **Enter IAM role ARN**, then enter the ARN in the
     corresponding field.

8. Review the information that's displayed in the **Destination** and
   **Copied object settings** sections. If the information in the
   **Destination** section is correct, choose **Import**
   to start the copy job.

The Amazon S3 console displays the status of your new job on the **Batch
Operations** page. For more information about the job, choose the option button
next to the job name, and then on the **Actions** menu, choose
**View details**. To open the directory bucket that the objects will be
imported into, choose **View import destination**.
