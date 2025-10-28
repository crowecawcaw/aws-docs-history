# Storing a user script and virtual environment in

S3

The following procedure explains how to store a user script and optional virtual
environment in Amazon S3. Complete this step before creating a PySpark analysis template.

###### Important

Do not modify or remove artifacts (user scripts or virtual environments) after
creating an analysis template.

Doing so will:

- Cause all future analysis jobs using this template to fail.
- Require creation of a new analysis template with new artifacts.
- Not affect previously completed analysis jobs
  **Prerequisites**

- An AWS account with appropriate permissions
- A user script file (such as `my_analysis.py`)
- (Optional, if one exists) A virtual environment package (`.tar.gz` file)
- Access to create or modify IAM roles

Console

###### To store a user script and virtual environment in S3 using the console:

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Create a new S3 bucket or use an existing one.
3. Enable versioning for the bucket.
   1. Select your bucket.
   2. Choose **Properties**.
   3. In the **Bucket Versioning** section, choose
      **Edit**.
   4. Select **Enable** and save changes.

4. Upload your artifacts and enable SHA-256 hash.
   1. Navigate to your bucket.
   2. Choose **Upload**.
   3. Choose **Add files** and add your user script
      file.
   4. (Optional, if one exists) Add your **.tar.gz**
      file.
   5. Expand **Properties**.
   6. Under **Checksums**, for **Checksum
      function**, select **SHA256**.
   7. Choose **Upload**.

5. You are now ready to create a PySpark analysis template.

CLI

###### To store the user script and virtual environment in S3 using the AWS CLI:

1. Run the following command:

```
aws s3 cp --checksum-algorithm sha256 pyspark_venv.tar.gz s3://ARTIFACT-BUCKET/EXAMPLE-PREFIX/
```

2. You are now ready to create a PySpark analysis template.

###### Note

If you need to update script or virtual environment:

1. Upload the new version as a separate object.
2. Create a new analysis template using the new artifacts.
3. Deprecate the old template.
4. Keep the original artifacts in S3 if the old template might still be
   needed.
