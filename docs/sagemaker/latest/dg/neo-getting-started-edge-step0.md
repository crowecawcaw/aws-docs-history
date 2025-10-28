# Prerequisites

SageMaker Neo is a capability that allows you to train machine learning models once and run them anywhere in the cloud and at the edge.
Before you can compile and optimize your models with Neo, there are a few prerequisites you need to set up.
You must install the necessary Python libraries, configure your AWS credentials, create an IAM role with the required permissions, and set up an S3 bucket for storing model artifacts.
You must also have a trained machine learning model ready.
The following steps guide you through the setup:

1. **Install Boto3**

If you are running these commands on your edge device, you must install the
AWS SDK for Python (Boto3). Within a Python environment (preferably a virtual environment),
run the following locally on your edge device's terminal or within a Jupyter
notebook instance:

Terminal

```
pip install boto3
```

Jupyter Notebook

```
!pip install boto3
```

2. **Set Up AWS Credentials**

You need to set up Amazon Web Services credentials on your device in order to
run SDK for Python (Boto3). By default, the AWS credentials should be stored in the file
`~/.aws/credentials` on your edge device. Within the credentials
file, you should see two environment variables: `aws_access_key_id`
and `aws_secret_access_key`.

In your terminal, run:

```
$ more ~/.aws/credentials

[default]
aws_access_key_id = `YOUR_ACCESS_KEY`
aws_secret_access_key = `YOUR_SECRET_KEY`
```

The [AWS General Reference Guide](../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys") has instructions on how to get the
necessary `aws_access_key_id` and `aws_secret_access_key`.
For more information on how to set up credentials on your device, see the [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration") documentation. 3. **Set up an IAM Role and attach policies.**

Neo needs access to your S3 bucket URI. Create an IAM role that can run SageMaker AI
and has permission to access the S3 URI. You can create an IAM role either by
using SDK for Python (Boto3), the console, or the AWS CLI. The following example illustrates
how to create an IAM role using SDK for Python (Boto3):

```
import boto3

AWS_REGION = `'aws-region'`

# Create an IAM client to interact with IAM
iam_client = boto3.client('iam', region_name=AWS_REGION)
role_name = `'role-name'`

```

For more information on how to create an IAM role with the console, AWS CLI,
or through the AWS API, see
[Creating an IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_api "../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_api").

Create a dictionary describing the IAM policy you are attaching. This
policy is used to create a new IAM role.

```
policy = {
    'Statement': [
        {
            'Action': 'sts:AssumeRole',
            'Effect': 'Allow',
            'Principal': {'Service': 'sagemaker.amazonaws.com'},
        }],
     'Version': '2012-10-17		 	 	 '
}
```

Create a new IAM role using the policy you defined above:

```
import json

new_role = iam_client.create_role(
    AssumeRolePolicyDocument=json.dumps(policy),
    Path='/',
    RoleName=role_name
)
```

You need to know what your Amazon Resource Name (ARN) is when you create a
compilation job in a later step, so store it in a variable as well.

```
role_arn = new_role['Role']['Arn']
```

Now that you have created a new role, attach the permissions it needs to
interact with Amazon SageMaker AI and Amazon S3:

```
iam_client.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
)

iam_client.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
);
```

4. **Create an Amazon S3 bucket to store your model
   artifacts**

SageMaker Neo will access your model artifacts from Amazon S3

Boto3

```
# Create an S3 client
s3_client = boto3.client('s3', region_name=AWS_REGION)

# Name buckets
bucket='name-of-your-bucket'

# Check if bucket exists
if boto3.resource('s3').Bucket(bucket) not in boto3.resource('s3').buckets.all():
    s3_client.create_bucket(
        Bucket=bucket,
        CreateBucketConfiguration={
            'LocationConstraint': AWS_REGION
        }
    )
else:
    print(f'Bucket {bucket} already exists. No action needed.')
```

CLI

```
aws s3 mb s3://`'name-of-your-bucket'` --region `specify-your-region`

# Check your bucket exists
aws s3 ls s3://`'name-of-your-bucket'`/
```

5. **Train a machine learning model**

See [Train a Model with Amazon SageMaker AI](how-it-works-training.md "how-it-works-training.md")
for more information on how to train a machine learning
model using Amazon SageMaker AI. You can optionally upload your locally trained model
directly into an Amazon S3 URI bucket.

###### Note

Make sure the model is correctly formatted depending on the framework you
used. See [What input data shapes does SageMaker Neo expect?](neo-job-compilation.md#neo-job-compilation-expected-inputs "neo-job-compilation.md#neo-job-compilation-expected-inputs")

If you do not have a model yet, use the `curl` command to get a
local copy of the `coco_ssd_mobilenet` model from TensorFlow’s
website. The model you just copied is an object detection model trained from the
[COCO dataset](https://cocodataset.org/#home "https://cocodataset.org/#home"). Type the
following into your Jupyter notebook:

```
model_zip_filename = './coco_ssd_mobilenet_v1_1.0.zip'
!curl http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip \
    --output {model_zip_filename}
```

Note that this particular example was packaged in a .zip file. Unzip this file
and repackage it as a compressed tarfile (`.tar.gz`) before using it
in later steps. Type the following into your Jupyter notebook:

```
# Extract model from zip file
!unzip -u {model_zip_filename}

model_filename = 'detect.tflite'
model_name = model_filename.split('.')[0]

# Compress model into .tar.gz so SageMaker Neo can use it
model_tar = model_name + '.tar.gz'
!tar -czf {model_tar} {model_filename}
```

6. **Upload trained model to an S3 bucket**

Once you have trained your machine learning mode, store it in an S3 bucket.

Boto3

```
# Upload model
s3_client.upload_file(Filename=model_filename, Bucket=bucket, Key=model_filename)
```

CLI
Replace `your-model-filename` and
`amzn-s3-demo-bucket` with the name of your S3 bucket.

```
aws s3 cp `your-model-filename` s3://`amzn-s3-demo-bucket`
```
