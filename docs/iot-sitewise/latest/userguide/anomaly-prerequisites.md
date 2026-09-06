

# Prerequisites
<a name="anomaly-prerequisites"></a>

To complete these steps, you must have an asset model and at least one asset created. For more information, see [ Create an asset model (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-asset-models.html#create-asset-model-cli), and [ Create an asset (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html#create-asset-cli). We do not support external IDs at this time.

If you are new to AWS IoT SiteWise (and do not have historical data), you must call the [ CreateBulkImportJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateBulkImportJob.html) API to import asset property values into AWS IoT SiteWise. This is used to train the model. For more information, see [ Create an AWS IoT SiteWise bulk import job (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html).

## Setup AWS CLI for Computation Model APIs
<a name="cli-setup"></a>

Follow these steps to update your AWS CLI configuration, and access the computation model APIs:
+ Install the latest awscli version `aws-cli`.
+ Verify the installation by checking for the new APIs:

  ```
  aws iotsitewise help
  ```

The command output displays the complete list of AWS IoT SiteWise APIs, including the newly added computation model operations.

## Property requirements
<a name="prop-requirements"></a>

To set up anomaly detection, you must have the following requirements and the [UpdateAssetModel (AWS CLI)](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/update-asset-model.html):
+ At least one input property that is of either `DOUBLE` or `INTEGER` data type. It is either a measurement or transform property, and is used to train the model.
+ A result property of `STRING` data type. It must be a measurement property, and stores the anomaly detection results.

## Labeling prerequisites
<a name="label-data"></a>
+ Upload your data labels to an Amazon S3 bucket.
+ Update the bucket policy of this bucket to allow AWS IoT SiteWise to read your labels.

  On console, go to **Permissions -> Bucket policy**. Replace the bucket ARN with ARN of your bucket.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "SiteWiseS3ReadAccess",
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject",
                  "s3:ListBucket"
              ],
              "Resource": [
                  "arn:aws:s3:::{{amzn-s3-demo-bucket}}{{bucket-name}}",
                  "arn:aws:s3:::{{amzn-s3-demo-bucket}}{{bucket-name}}/*"
              ]
          }
      ]
  }
  ```

------

## Model evaluation prerequisites
<a name="prerequisites-model-evaluation"></a>
+ Model evaluation generates pointwise model diagnostics in the Amazon S3 bucket location provided by you.
+ In order for the pointwise diagnostic results to be written to your Amazon S3 bucket, update the bucket policy of this bucket to allow AWS IoT SiteWise to write the results.

  On console, go to `Permissions -> Bucket policy`. Replace the bucket ARN with ARN of your bucket.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "SiteWiseS3Access",
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject",
                  "s3:ListBucket",
                  "s3:PutObject"
              ],
              "Resource": [
                  "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                  "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
              ]
          }
      ]
  }
  ```

------

## Model metrics prerequisites
<a name="prerequisites-model-metrics"></a>
+ Model metrics provide comprehensive performance insights including model quality assessment, event detection statistics, and comparison metrics between model versions in the Amazon S3 bucket location provided.
+ In order for the model metrics json file to be written to your Amazon S3 bucket, update the bucket policy to allow AWS IoT SiteWise to write the results.

  On console, go to `Permissions -> Bucket policy`. Replace the bucket ARN with ARN of your bucket.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "SiteWiseS3Access",
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject",
                  "s3:ListBucket",
                  "s3:PutObject"
              ],
              "Resource": [
              "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
              "arn:aws:s3:::{{amzn-s3-demo-bucket}}-s3-bucket;/*"
              ]
          }
      ]
  }
  ```

------