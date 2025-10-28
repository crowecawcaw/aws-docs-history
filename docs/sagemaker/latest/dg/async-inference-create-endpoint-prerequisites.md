# Complete the prerequisites

The following topic describes the prerequisites that you must complete before
creating an asyncrhonous endpoint. These prerequisites include properly storing your model
artifacts, configuring an AWS IAM with the correct permissions, and selecting a
container image.

###### To complete the prerequisites

1. **Create an IAM role for Amazon SageMaker AI.**

Asynchronous Inference needs access to your Amazon S3 bucket URI. To facilitate this, create an
IAM role that can run SageMaker AI and has permission to access Amazon S3 and Amazon SNS. Using
this role, SageMaker AI can run under your account and access your Amazon S3 bucket and Amazon SNS
topics.

You can create an IAM role by using the IAM console, AWS SDK for Python (Boto3),
or AWS CLI. The following is an example of how to create an IAM role
and attach the necessary policies with the IAM console.

    1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. In the navigation pane of the IAM console, choose
     **Roles**, and then choose **Create
     role**.
    3. For **Select type of trusted entity**, choose
     **AWS service**.
    4. Choose the service that you want to allow to assume this role. In this
     case, choose **SageMaker AI**. Then choose **Next:
     Permissions**.




    	* This automatically creates an IAM policy that grants access
    	 to related services such as Amazon S3, Amazon ECR, and CloudWatch Logs.
    5. Choose **Next: Tags**.
    6. (Optional) Add metadata to the role by attaching tags as key–value
     pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md").
    7. Choose **Next: Review**.
    8. Type in a **Role name**.
    9. If possible, type a role name or role name suffix. Role names must be
     unique within your AWS account. They are not distinguished by case. For
     example, you cannot create roles named both `PRODROLE` and
     `prodrole`. Because other AWS resources might reference
     the role, you cannot edit the name of the role after it has been
     created.
    10. (Optional) For **Role description**, type a
     description for the new role.
    11. Review the role and then choose **Create
     role**.


    Note the SageMaker AI role ARN. To find the role ARN using the console, do the
     following:


    	1. Go to the IAM console: [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")
    	2. Select **Roles**.
    	3. Search for the role you just created by typing in the name of
    	 the role in the search field.
    	4. Select the role.
    	5. The role ARN is at the top of the **Summary**
    	 page.

2. **Add Amazon SageMaker AI, Amazon S3 and Amazon SNS Permissions to your IAM Role.**

Once the role is created, grant SageMaker AI, Amazon S3, and optionally Amazon SNS permissions to your IAM role.

Choose **Roles** in the IAM
console. Search for the role you created by typing in your role name in the
**Search** field.

    1. Choose your role.
    2. Next, choose **Attach Policies**.
    3. Amazon SageMaker Asynchronous Inference needs permission to perform the following actions:
     `"sagemaker:CreateModel"`,
     `"sagemaker:CreateEndpointConfig"`,
     `"sagemaker:CreateEndpoint"`, and
     `"sagemaker:InvokeEndpointAsync"`.



    These actions are included in the `AmazonSageMakerFullAccess` policy.
     Add this policy to your IAM role. Search for `AmazonSageMakerFullAccess`
     in the **Search** field. Select `AmazonSageMakerFullAccess`.
    4. Choose **Attach policy**.
    5. Next, choose **Attach Policies** to add Amazon S3 permissions.
    6. Select **Create policy**.
    7. Select the `JSON` tab.
    8. Add the following policy statement:



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Action": [
     "s3:GetObject",
     "s3:PutObject",
     "s3:AbortMultipartUpload",
     "s3:ListBucket"
     ],
     "Effect": "Allow",
     "Resource": "arn:aws:s3:::`bucket_name/*`"
     }
     ]
    }`

    ```
    9. Choose **Next: Tags**.
    10. Type in a **Policy name**.
    11. Choose **Create policy**.
    12. Repeat the same steps you completed to add Amazon S3 permissions
     in order to add Amazon SNS permissions. For the policy statement,
     attach the following:



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Action": [
     "sns:Publish"
     ],
     "Effect": "Allow",
    "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`SNS_Topic`"
     }
     ]
    }`

    ```

3. **Upload your inference data (e.g., machine learning
   model, sample data) to **Amazon S3**.**
4. **Select a prebuilt Docker inference image or create your
   own Inference Docker Image.**

SageMaker AI provides containers for its built-in algorithms and prebuilt Docker
images for some of the most common machine learning frameworks, such as Apache
MXNet, TensorFlow, PyTorch, and Chainer. For a full list of the available SageMaker AI
images, see [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md"). If you choose to use a
SageMaker AI provided container, you can increase the endpoint timeout and payload sizes
from the default by setting the environment variables in the container. To learn
how to set the different environment variables for each framework, see the
Create a Model step of creating an asynchronous endpoint.

If none of the existing SageMaker AI containers meet your needs and you don't have an existing
container of your own, you may need to create a new Docker container.
See [Containers with custom inference code](your-algorithms-inference-main.md "your-algorithms-inference-main.md")
for information on how to create your Docker image. 5. **Create an Amazon SNS topic (optional)**

Create an Amazon Simple Notification Service (Amazon SNS) topic that sends notifications about requests that have completed processing.
Amazon SNS is a notification service for messaging-oriented applications, with multiple subscribers
requesting and receiving "push" notifications of time-critical messages
via a choice of transport protocols, including HTTP, Amazon SQS, and email.
You can specify Amazon SNS topics when you create an
`EndpointConfig` object when you specify `AsyncInferenceConfig` using the `EndpointConfig` API.

Follow the steps to create and subscribe to an Amazon SNS topic.

    1. Using Amazon SNS console, create a topic. For instructions, see [Creating an Amazon SNS topic](../../../sns/latest/dg/CreateTopic.md "../../../sns/latest/dg/CreateTopic.md") in the *Amazon Simple Notification Service*
    *Developer Guide*.
    2. Subscribe to the topic. For
     instructions, see [Subscribing to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md") in the *Amazon Simple Notification Service* *Developer
     Guide*.
    3. When you receive email requesting that you confirm your subscription
     to the topic, confirm the subscription.
    4. Note the topic Amazon Resource Name (ARN). The Amazon SNS topic you created is another resource in
     your AWS account, and it has a unique ARN. The ARN is in the following
     format:



    ```
    arn:aws:sns:`aws-region:account-id:topic-name`
    ```For more information about Amazon SNS, see the [Amazon SNS Developer Guide](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").
