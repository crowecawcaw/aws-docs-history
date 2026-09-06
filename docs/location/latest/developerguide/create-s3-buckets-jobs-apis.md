

# Create Amazon S3 buckets
<a name="create-s3-buckets-jobs-apis"></a>

The Amazon Location Jobs API requires input files to be stored in Amazon S3 and writes output files to a designated Amazon S3 location. You can use a single Amazon S3 bucket with different prefixes for input and output data, or use separate buckets.

**Important**  
When using the same bucket for input and output, use different prefixes for each. Do not use the same prefix for both input and output when running multiple jobs to avoid having one job’s output unintentionally read as input for other jobs.

**Note**  
The Amazon S3 input and output buckets you create must exist in the same AWS Region where you plan to run your jobs. The IAM resources you create must be created in the same account. Versioning must be enabled on your buckets.

**To create Amazon S3 buckets using the console**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/). 

1. Choose **Create bucket**. 

1. For **Bucket name**, enter a unique name for your input bucket, such as `my-jobs-input`. 

1. For **AWS Region**, select the Region where you plan to run your Amazon Location jobs.

1. Keep the default settings for the remaining options, or configure them according to your requirements.

1. Choose **Create bucket**. 

1. After the bucket is created, select the bucket name to open its details.

1. Choose the **Properties** tab.

1. In the **Bucket Versioning** section, choose **Edit**.

1. Select **Enable** and choose **Save changes**.

1. Repeat steps 2-10 to create a second bucket for output results, such as `my-jobs-output`. 

**To create Amazon S3 buckets using the AWS CLI**

1. Create the input bucket:

   ```
   aws s3api create-bucket \
       --bucket my-jobs-input \
       --region us-east-1
   ```
**Note**  
For Regions outside `us-east-1`, add the `--create-bucket-configuration` parameter:  

   ```
   aws s3api create-bucket \
       --bucket my-jobs-input \
       --region us-west-2 \
       --create-bucket-configuration LocationConstraint=us-west-2
   ```

1. Enable versioning on the input bucket:

   ```
   aws s3api put-bucket-versioning \
       --bucket my-jobs-input \
       --versioning-configuration Status=Enabled
   ```

1. Create the output bucket:

   ```
   aws s3api create-bucket \
       --bucket my-jobs-output \
       --region us-east-1
   ```

1. Enable versioning on the output bucket:

   ```
   aws s3api put-bucket-versioning \
       --bucket my-jobs-output \
       --versioning-configuration Status=Enabled
   ```

1. Verify the buckets were created:

   ```
   aws s3 ls | grep my-jobs
   ```

1. Verify versioning is enabled:

   ```
   aws s3api get-bucket-versioning --bucket my-jobs-input
   aws s3api get-bucket-versioning --bucket my-jobs-output
   ```

After creating your buckets, prepare your input data. For information about preparing input data, see [Prepare input data](preparing-input-data.md) .

**Example: Two separate buckets**  

```
my-jobs-input/
├── data-batch-1.parquet
├── data-batch-2.parquet
└── data-batch-3.parquet

my-jobs-output/
└── (results are written here by the service)
```

**Example: Single bucket with different prefixes**  

```
my-jobs-bucket/
├── input/
│   ├── data-batch-1.parquet
│   ├── data-batch-2.parquet
│   └── data-batch-3.parquet
└── output/
    └── (results are written here by the service)
```