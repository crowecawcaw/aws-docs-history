

# Use attribute-based access control (ABAC) for multi-tenancy training
<a name="model-access-training-data-abac"></a>

In a multi-tenant environment, it is crucial to ensure that each tenant's data is isolated and accessible only to authorized entities. SageMaker AI supports the use of [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) to achieve this isolation for training jobs. Instead of creating multiple IAM roles for each tenant, you can use the same IAM role for all tenants by configuring a session chaining configuration that uses AWS Security Token Service (AWS STS) session tags to request temporary, limited-privilege credentials for your training job to access specific tenants. For more information about session tags, see [Passing session tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html).

When creating a training job, your session chaining configuration uses AWS STS to request temporary security credentials. This request generates a session, which is tagged. Each SageMaker training job can only access a specific tenant using a single role shared by all training jobs. By implementing ABAC with session chaining, you can ensure that each training job has access only to the tenant specified by the session tag, effectively isolating and securing each tenant. The following section guides you through the steps to set up and use ABAC for multi-tenant training job isolation using the SageMaker Python SDK. 

## Prerequisites
<a name="model-access-training-data-abac-prerequisites"></a>

To get started with ABAC for multi-tenant training job isolation, you must have the following:
+ Tenants with consistent naming across locations. For example, if an input data Amazon S3 URI for a tenant is `s3://your-input-s3-bucket/{{example-tenant}}`, the Amazon FSx directory for that same tenant should be `/fsx-train/train/{{example-tenant}}` and the output data Amazon S3 URI should be `s3://your-output-s3-bucket/{{example-tenant}}`.
+ A SageMaker AI job creation role. You can create a SageMaker AI job creation role using Amazon SageMaker AI Role Manager. For information, see [Using the role manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager-tutorial.html).
+ A SageMaker AI execution role that has `sts:AssumeRole`, and `sts:TagSession` permissions in its trust policy. For more information on SageMaker AI execution roles, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html). 

  The execution role should also have a policy that allows tenants in any attribute-based multi-tenancy architecture to read from the prefix attached to a principal tag. The following is an example policy that limits the SageMaker AI execution role to have access to the value associated with the `tenant-id` key. For more information on naming tag keys, see [Rules for tagging in IAM and STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html#id_tags_rules).

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Action": [
                  "s3:GetObject",
                  "s3:PutObject"
              ],
              "Resource": [
                  "arn:aws:s3:::{{your-input-s3-bucket}}/${aws:PrincipalTag/{{tenant-id}}}/*"
              ],
              "Effect": "Allow"
          },
          {
              "Action": [
                  "s3:PutObject"
              ],
              "Resource": "arn:aws:s3:::{{your-output-s3-bucket}}/${aws:PrincipalTag/{{tenant-id}}}/*",
              "Effect": "Allow"
          },
          {
              "Action": "s3:ListBucket",
              "Resource": "*",
              "Effect": "Allow"
          }
      ]
  }
  ```

------

## Create a training job with session tag chaining enabled
<a name="model-access-training-data-abac-create-training-job"></a>

The following procedure shows you how to create a training job with session tag chaining using the SageMaker Python SDK for ABAC-enabled multi-tenancy training.

**Note**  
In addition to multi-tenancy data storage, you can also use the ABAC workflow to pass session tags to your execution role for Amazon VPC, AWS Key Management Service, and any other services you allow SageMaker AI to call

**Enable session tag chaining for ABAC**

1. Import `boto3` and the SageMaker Python SDK. ABAC-enabled training job isolation is only available in version [2.217](https://pypi.org/project/sagemaker/2.217.0/) or later of the SageMaker AI Python SDK. 

   ```
   import boto3
   
   from sagemaker.train import ModelTrainer
   from sagemaker.train.configs import InputData, CheckpointConfig
   from sagemaker.core.helper.session_helper import Session
   from sagemaker.core.shapes import OutputDataConfig
   from sagemaker.train.configs import Compute
   ```

1. Set up an AWS STS and SageMaker AI client to use the tenant-labeled session tags. You can change the tag value to specify a different tenant.

   ```
   # Start an AWS STS client
   sts_client = boto3.client('sts')
   
   # Define your tenants using tags
   # The session tag key must match the principal tag key in your execution role policy
   tags = []
   tag = {}
   tag['Key'] = {{"tenant-id"}}
   tag['Value'] = {{"example-tenant"}}
   tags.append(tag)
   
   # Have AWS STS assume your ABAC-enabled job creation role
   response = sts_client.assume_role(
       RoleArn="arn:aws:iam::<account-id>:role/<your-training-job-creation-role>",
       RoleSessionName="SessionName",
       Tags=tags)
   credentials = response['Credentials']
   
   # Create a client with your job creation role (which was assumed with tags)
   sagemaker_client = boto3.client(
       'sagemaker',
       aws_access_key_id=credentials['AccessKeyId'],
       aws_secret_access_key=credentials['SecretAccessKey'],
       aws_session_token=credentials['SessionToken']
   )
   sagemaker_session = Session(sagemaker_client=sagemaker_client)
   ```

    When appending the tags `"tenant-id=example-tenant"` to the job creation role, these tags are extracted by the execution role to use the following policy: 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "s3:GetObject",
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::{{your-input-s3-bucket}}/{{example-tenant}}/*"
               ],
               "Effect": "Allow"
           },
           {
               "Action": [
                   "s3:PutObject"
               ],
               "Resource": "arn:aws:s3:::{{your-output-s3-bucket}}/{{example-tenant}}/*",
               "Effect": "Allow"
           },
           {
               "Action": "s3:ListBucket",
               "Resource": "*",
               "Effect": "Allow"
           }
       ]
   }
   ```

------

1. Define a ModelTrainer to create a training job using the SageMaker Python SDK. Set `enable_session_tag_chaining` to `True` to allow your SageMaker AI training execution role to retrieve the tags from your job creation role.

   ```
   # Specify your training input
   trainingInput = InputData(
       channel_name='{{training}}',
       data_source={{'s3://<your-input-bucket>/example-tenant'}}
   )
   
   # Specify your training job execution role 
   execution_role_arn = {{"arn:aws:iam::<account-id>:role/<your-training-job-execution-role>"}}
   
   # Define your model trainer with session tag chaining enabled
   model_trainer = ModelTrainer(
       training_image={{"<your-training-image-uri>"}},
       role=execution_role_arn,
       compute=Compute(
           instance_type='ml.m4.xlarge',
           instance_count=1,
           volume_size_in_gb=20
       ),
       sagemaker_session=sagemaker_session,
       output_data_config=OutputDataConfig(s3_output_path={{"s3://<your-output-bucket>/example-tenant"}}),
       tags=[{"Key": "sagemaker:EnableSessionTagChaining", "Value": "true"}]
   )
   
   model_trainer.train(input_data_config=[trainingInput])
   ```

SageMaker AI can only read tags provided in the training job request and does not add any tags to resources on your behalf.

ABAC for SageMaker training is compatible with SageMaker AI managed warm pools. To use ABAC with warm pools, matching training jobs must have identical session tags. For more information, see [Matching training jobs](train-warm-pools.md#train-warm-pools-matching-criteria).