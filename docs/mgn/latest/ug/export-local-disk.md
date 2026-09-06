

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Exporting your data inventory to a local disk
<a name="export-local-disk"></a>

To export your inventory to a local disk, take the following steps:

1. Select **Export** from the left-hand navigation menu (under** Import and export**) and you’ll be navigated to the **Export inventory** tab.

1. Select **Export to a local disk**.

1. Specify the name of the CSV file into which you want to download the data.
**Note**  
The file will also be automatically downloaded to an S3 bucket created by AWS Transform MGN. 
You must have the required permissions to perform this action.
It is highly recommended that you [apply S3 bucket security practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) where your CSV files are stored.

1. Choose **Export**.