# Complete the prerequisites

The following topic describes the prerequisites that you must complete before
creating a serverless endpoint. These prerequisites include properly storing your model
artifacts, configuring an AWS IAM with the correct permissions, and selecting a
container image.

###### To complete the prerequisites

1. **Set up an AWS account.** You first need an AWS account
   and an AWS Identity and Access Management administrator user. For instructions on how to set up an AWS account, see
   [How do I create and activate a new AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/ "https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/"). For instructions on how to secure
   your account with an IAM administrator user, see [Creating your first IAM admin user and user group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _IAM User Guide_.
2. **Create an Amazon S3 bucket.** You use an Amazon S3 bucket to store
   your model artifacts. To learn how to create a bucket, see [Create your first S3 bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md") in
   the _Amazon S3 User Guide_.
3. **Upload your model artifacts to your S3 bucket.** For
   instructions on how to upload your model to your bucket, see [Upload an object to your bucket](../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md "../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md") in the _Amazon S3 User Guide_.
4. **Create an IAM role for Amazon SageMaker AI.** Amazon SageMaker AI needs access
   to the S3 bucket that stores your model. Create an IAM role with a policy that gives SageMaker AI
   read access to your bucket. The following procedure shows how to create a role in the console,
   but you can also use the [CreateRole](../../../IAM/latest/APIReference/API_CreateRole.md "../../../IAM/latest/APIReference/API_CreateRole.md") API from the _IAM User Guide_. For information on giving your role more granular
   permissions based on your use case, see [How to use SageMaker AI execution roles](sagemaker-roles.md#sagemaker-roles-createmodel-perms "sagemaker-roles.md#sagemaker-roles-createmodel-perms").
   1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. In the navigation tab, choose **Roles**.
   3. Choose **Create Role**.
   4. For **Select type of trusted entity**, choose **AWS
      service** and then choose **SageMaker AI**.
   5. Choose **Next: Permissions** and then choose **Next:
      Tags**.
   6. (Optional) Add tags as key-value pairs if you want to have metadata for the role.
   7. Choose **Next: Review**.
   8. For **Role name**, enter a name for the new role that is unique within
      your AWS account. You cannot edit the role name after creating the role.
   9. (Optional) For **Role description**, enter a description for the new
      role.
   10. Choose **Create role**.

5. **Attach S3 bucket permissions to your SageMaker AI role.** After
   creating an IAM role, attach a policy that gives SageMaker AI permission to access the S3 bucket
   containing your model artifacts.
   1. In the IAM console navigation tab, choose **Roles**.
   2. From the list of roles, search for the role you created in the previous step by
      name.
   3. Choose your role, and then choose **Attach policies**.
   4. For **Attach permissions**, choose **Create
      policy**.
   5. In the **Create policy** view, select the **JSON**
      tab.
   6. Add the following policy statement into the JSON editor. Make sure to replace
      `<your-bucket-name>` with the name of the S3
      bucket that stores your model artifacts. If you want to restrict the access to a specific
      folder or file in your bucket, you can also specify the Amazon S3 folder path, for example,
      ``<your-bucket-name>`/`<model-folder>``.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "VisualEditor0",
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::`<your-bucket-name>`/*"
    }
    ]
   }`

   ```

   7. Choose **Next: Tags**.
   8. (Optional) Add tags in key-value pairs to the policy.
   9. Choose **Next: Review**.
   10. For **Name**, enter a name for the new policy.
   11. (Optional) Add a **Description** for the policy.
   12. Choose **Create policy**.
   13. After creating the policy, return to **Roles** in the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") and select your SageMaker AI
       role.
   14. Choose **Attach policies**.
   15. For **Attach permissions**, search for the policy you created by name.
       Select it and choose **Attach policy**.

6. **Select a prebuilt Docker container image or bring your
   own.** The container you choose serves inference on your endpoint. SageMaker AI provides
   containers for built-in algorithms and prebuilt Docker images for some of the most common
   machine learning frameworks, such as Apache MXNet, TensorFlow, PyTorch, and Chainer. For a full
   list of the available SageMaker images, see [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md").

If none of the existing SageMaker AI containers meet your needs, you may need to create your own
Docker container. For information about how to create your Docker image and make it compatible
with SageMaker AI, see [Containers with custom inference code](your-algorithms-inference-main.md "your-algorithms-inference-main.md"). To use your container with a serverless
endpoint, the container image must reside in an Amazon ECR repository within the same AWS account
that creates the endpoint. 7. **(Optional) Register your model with Model Registry.**
[SageMaker Model Registry](model-registry.md "model-registry.md") helps you catalog and manage versions of
your models for use in ML pipelines. For more information about registering a version of your
model, see [Create a Model Group](model-registry-model-group.md "model-registry-model-group.md") and [Register a Model Version](model-registry-version.md "model-registry-version.md"). For an example of a Model Registry and Serverless Inference workflow,
see the following [example notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/serverless-inference/serverless-model-registry.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/serverless-inference/serverless-model-registry.ipynb"). 8. **(Optional) Bring an AWS KMS key.** When setting up a
serverless endpoint, you have the option to specify a KMS key that SageMaker AI uses to encrypt your
Amazon ECR image. Note that the key policy for the KMS key must grant access to the IAM role you
specify when setting up your endpoint. To learn more about KMS keys, see the [AWS Key Management Service Developer
Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
