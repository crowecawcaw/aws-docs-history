

# Storing a user script and virtual environment in S3
<a name="store-artifacts-in-s3"></a>

The following procedure explains how to store a user script and optional virtual environment in Amazon S3. Complete this step before creating a PySpark analysis template. 

**Important**  
Do not modify or remove artifacts (user scripts or virtual environments) after creating an analysis template.  
Doing so will:  
Cause all future analysis jobs using this template to fail.
Require creation of a new analysis template with new artifacts.
Not affect previously completed analysis jobs

**Prerequisites**
+ An AWS account with appropriate permissions
+ A user script file (such as `my_analysis.py`)
+ (Optional, if one exists) A virtual environment package (`.tar.gz` file) 
+ Access to create or modify IAM roles

------
#### [ Console ]

**To store a user script and virtual environment in S3 using the console:**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Create a new S3 bucket or use an existing one.

1. Enable versioning for the bucket.

   1. Select your bucket.

   1. Choose **Properties**.

   1. In the **Bucket Versioning** section, choose **Edit**.

   1. Select **Enable** and save changes.

1. Upload your artifacts and enable SHA-256 hash. 

   1. Navigate to your bucket.

   1. Choose **Upload**.

   1. Choose **Add files** and add your user script file.

   1. (Optional, if one exists) Add your **.tar.gz** file.

   1. Expand **Properties**.

   1. Under **Checksums**, for **Checksum function**, select **SHA256**.

   1. Choose **Upload**.

1. You are now ready to create a PySpark analysis template.

------
#### [ CLI ]

**To store the user script and virtual environment in S3 using the AWS CLI:**

1. Run the following command:

   ```
   aws s3 cp --checksum-algorithm sha256 pyspark_venv.tar.gz s3://ARTIFACT-BUCKET/EXAMPLE-PREFIX/
   ```

1. You are now ready to create a PySpark analysis template.

------

**Note**  
If you need to update script or virtual environment:   
Upload the new version as a separate object.
Create a new analysis template using the new artifacts.
Deprecate the old template.
Keep the original artifacts in S3 if the old template might still be needed.