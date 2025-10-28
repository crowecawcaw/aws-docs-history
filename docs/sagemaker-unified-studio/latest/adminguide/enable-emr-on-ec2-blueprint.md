# Specify PEM certificate for EmrOnEc2

blueprint

In order to successfully enable the EmrOnEc2 blueprint, you must specify the location
of your PEM certificate. To do this, complete the following procedure:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. Choose the **Project profiles** tab and then choose
   **All capabilities**.
4. Choose one of the following instance type configurations:
   - OnDemand Amazon EMR on EC2 General Purpose: this configuration uses Amazon EC2
     instances (like m5.xlarge) to provide balanced compute, memory, and
     network resources. Choose this option for standard data processing
     workloads.
   - OnDemand Amazon EMR on EC2 Memory-Optimized: this configuration uses Amazon EC2
     instances (like r5.xlarge) to provide more memory per vCPU. Choose this
     option for memory-intensive workloads such as in-memory databases or
     real-time analytics.

5. Choose the corresponding radio button for the EmrOnEc2 blueprint deployment
   setting and choose **Edit**.
6. Under the **Blueprint parameters** section, edit the
   **certificateLocation** parameter. Enter the S3 location of
   the ZIP file that contains PEM certificate file(s). You must enter the S3
   location URL using the correct format of
   `s3://<DomainBucketName>/<AmazonDataZoneDomainID>/certificate_location/`
   Make sure to replace <DomainBucketName>/<AmazonDataZoneDomainID>
   with the correct values for those for your domain.

For more information about PEM certificates, see [Using PEM certificates](../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-encryption-certificates "../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-encryption-certificates").
