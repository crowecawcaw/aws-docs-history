# Create a model evaluation job that uses human workers

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

To create a model evaluation job that uses human workers you must set up your
environment to have the correct permissions. Then, you can use the model evaluation job
wizard in Studio to select the models you want to use, and then define the
parameters and the workforce you want to use in the model evaluation job.

When the job is complete you can, view a report to understand how your workforce
evaluated the models you selected. The results are also saved in Amazon S3 as a
`jsonlines` output
file.

In model evaluation job that uses human workers, you have the ability to bring
inference data from models hosted outside of SageMaker AI and models hosted outside of AWS. To
learn more, see [Using your own inference data in model evaluation jobs that use human workers](#outside-inference-studio "#outside-inference-studio").

When your jobs are completed the results are saved in the Amazon S3 bucket specified when the job was created. To learn how to interpret your results, see [Understand the results of your model
evaluation job](clarify-foundation-model-evaluate-results.md "clarify-foundation-model-evaluate-results.md").

### Prerequisites

To run a model evaluation in the Amazon SageMaker Studio UI, your AWS Identity and Access Management
(IAM) role and any input datasets must have the correct permissions. If
you do not have a SageMaker AI Domain or IAM role, follow the steps in
[Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").

### Setting

up your permissions

The following section shows you how to create a Amazon S3 bucket and how to
specify the correct Cross-origin resource sharing (CORS) permissions.

###### To create a Amazon S3 bucket and specify the CORS permissions

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the navigation pane, enter `S3` into the
   search bar at the top of the page.
3. Choose **S3** under
   **Services**.
4. Choose **Buckets** from the navigation
   pane.
5. In the **General purpose buckets** section, under
   **Name**, choose the name of the S3 bucket that
   you want to use to store your model input and output in the console.
   If you do not have an S3 bucket, do the following.
   1. Select **Create bucket** to open a new
      **Create bucket** page.
   2. In the **General configuration** section,
      under **AWS Region**, select the AWS
      region where your foundation model is located.
   3. Name your S3 bucket in the input box under
      **Bucket name**.
   4. Accept all of the default choices.
   5. Select **Create bucket**.
   6. In the **General purpose buckets**
      section, under **Name**, select the name of
      the S3 bucket that you created.

6. Choose the **Permissions** tab.
7. Scroll to the **Cross-origin resource sharing
   (CORS)** section at the bottom of the window. Choose
   **Edit**.
8. The following is the minimum required CORS policy that you
   _must_ add to your Amazon S3 bucket.
   Copy and paste the following into the input box.

```
[
{
    "AllowedHeaders": ["*"],
    "AllowedMethods": [
        "GET",
        "HEAD",
        "PUT"
    ],
    "AllowedOrigins": [
        "*"
    ],
    "ExposeHeaders": [
      "Access-Control-Allow-Origin"
    ],
    "MaxAgeSeconds": 3000
}
]
```

9. Choose **Save changes**.

###### To add permissions to your IAM policy

You may want to consider the level of permissions to attach to your
IAM role.

- You can create a custom IAM policy that allows the minimum
  required permissions tailored to this service.
- You can attach the existing [`AmazonSageMakerFullAccess`](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") and
  [`AmazonS3FullAccess`](../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md") policies to
  your existing IAM role, which is more permissive. For more
  information about the `AmazonSageMakerFullAccess`
  policy, see [AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess").
  If you wish to attach the existing policies to your IAM role, you
  may skip the instructions set here and continue following the
  instructions under **To add permissions to your
  IAM role**.

The following instructions creates a custom IAM policy that is
tailored to this service with minimum permissions.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the search bar at the top of the page, enter
   `IAM`.
3. Under **Services**, select **Identity and
   Access Management (IAM)**.
4. Choose **Policies** from the navigation
   pane.
5. Choose **Create policy**. When the
   **Policy editor** opens, choose
   **JSON**.
6. Ensure that the following permissions appear in the
   **Policy editor**. You can also copy and paste
   the following into the **Policy editor**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::{input_bucket}/*",
 "arn:aws:s3:::{input_bucket}",
 "arn:aws:s3:::{output_bucket}/*",
 "arn:aws:s3:::{output_bucket}",
 "arn:aws:s3:::jumpstart-cache-prod-{region}/*",
 "arn:aws:s3:::jumpstart-cache-prod-{region}"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateEndpoint",
 "sagemaker:DeleteEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:DeleteEndpointConfig"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:endpoint/sm-margaret-*",
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:endpoint-config/sm-margaret-*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "sagemaker-sdk:jumpstart-model-id"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeProcessingJob",
 "sagemaker:DescribeEndpoint",
 "sagemaker:InvokeEndpoint"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeInferenceComponent",
 "sagemaker:AddTags",
 "sagemaker:CreateModel",
 "sagemaker:DeleteModel"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:model/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "sagemaker-sdk:jumpstart-model-id"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeFlowDefinition",
 "sagemaker:StartHumanLoop",
 "sagemaker:DescribeHumanLoop"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/sagemaker/ProcessingJobs:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:GetPublicKey",
 "kms:Decrypt",
 "kms:Encrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/{kms-key-id}"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/{this-role-created-by-customer}",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalAccount": [
 "111122223333"
 ]
 }
 }
 }
 ]
}`

```

7. Choose **Next**.
8. Enter a policy name in the **Policy details**
   section, under **Policy name**. You can also enter
   an optional description. You will search for this policy name when
   you assign it to a role.
9. Choose **Create policy**.

###### To add permissions to your IAM role

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the search bar at the top of the page, enter
   `IAM`.
3. Under **Services**, select **Identity and
   Access Management (IAM)**.
4. Choose **Roles** in the navigation pane.
5. If you are creating a new role:
   1. Choose **Create role**.
   2. On the **Select trusted entity** step,
      under **Trusted entity type** choose
      **Custom trust policy**.
   3. In the **Custom trust policy** editor,
      next to **Add principal** choose
      **Add**.
   4. On the **Add principal** pop-up box,
      under **Principal type** select
      **AWS services** from the dropdown
      list of options.
   5. Under **ARN** replace
      `{ServiceName}` with
      `sagemaker`.
   6. Choose **Add principal**.
   7. Choose **Next**.
   8. (Optional) Under **Permissions policies**
      select the policies you would like to add to your
      role.
   9. (Optional) Under **Set permissions boundary -
      _optional_** choose your permission
      boundary setting.
   10. Choose **Next**.
   11. On the **Name, review, and create** step,
       under **Role details** fill in your
       **Role name** and
       **Description**.
   12. (Optional) **Under Add tags - _optional_**, you
       can add tags by choosing **Add new tag**
       and enter a **Key** and **Value -
       _optional_** pair.
   13. Review your settings.
   14. Choose **Create role**.

6. If you are adding the policy to an existing role:
   1. Select the name of the role under **Role
      name**. The main window changes to show
      information about your role.
   2. In the **Permissions** policies section,
      choose the down arrow next to **Add
      permissions**.
   3. From the options that appear, choose **Attach
      policies**.
   4. From the list of policies that appear, search for and
      select the policy that you created under **To add permissions to your IAM
      policy** and select the check the box next to
      your policy's name. If you did not create a custom IAM
      policy, search for and select the check boxes next to the
      AWS provided [`AmazonSageMakerFullAccess`](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") and
      [`AmazonS3FullAccess`](../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md") policies.
      You may want to consider the level of permissions to attach
      to your IAM role. The instructions for the custom IAM
      policy is less permissive, while the latter is more
      permissive. For more information about the
      `AmazonSageMakerFullAccess` policy, see
      [AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess").
   5. Choose **Add permissions**. A
      banner at the top of the page should state **Policy
      was successfully attached to role.** when
      completed.

###### To add trust policy to your IAM role

The following trust policy makes it so administrators can allow SageMaker AI
to assume the role. You need to add the policy to your IAM role. Use
the following steps to do so.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the search bar at the top of the page, enter
   `IAM`.
3. Under **Services**, select **Identity and
   Access Management (IAM)**.
4. Choose **Roles** in the navigation pane.
5. Select the name of the role under **Role name**.
   The main window changes to show information about your role.
6. Choose the **Trust relationship** tab.
7. Choose **Edit trust policy**.
8. Ensure that the following policy appears under **Edit
   trust policy**. You can also copy and paste the
   following into the editor.

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "sagemaker.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
]
}`

```

9. Choose **Update policy**. A banner at the top of
   the page should state **Trust policy updated.**
   when completed.

You can create a human evaluation job using a text-based model that is
available in JumpStart or you can use a JumpStart model that you've
previously deployed to an endpoint.

###### To launch JumpStart

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the search bar at the top of the page, enter
   `SageMaker AI`.
3. Under **Services**, select
   **Amazon SageMaker AI**.
4. Choose **Studio** from the navigation
   pane.
5. Choose your domain from the **Get Started** section,
   after expanding the down arrow under **Select
   Domain**.
6. Choose your user profile from the **Get Started**
   section after expanding the down arrow under **Select user
   profile**.
7. Choose **Open Studio** to open the landing page
   for Studio.
8. Choose **Jobs**from the navigation
   pane.

###### To set up an evaluation job

1.  On the Model evaluation home page, choose **Evaluate a model**
2.  Specify job details.
    1. Enter the **Evaluation name** of your model
       evaluation. This name helps you identify your model evaluation
       job after it is submitted.
    2. Enter a **Description** to add more context
       to the name.
    3. Choose **Next**.

3.  Set up evaluation

        1. Under **Choose an evaluation type**, select
         the radio button next to **Human**.
        2. Under **Choose the model(s) you want to
         evaluate**, choose **Add model
         to evaluation**. You can evaluate up to two models
         for each evaluation.




        	1. To use a pre-trained JumpStart model, choose
        	 **Pre-trained**
        	**JumpStart foundation
        	 model**. If you want to use a JumpStart
        	 model that you have previously deployed to an endpoint,
        	 choose **Endpoints with JumpStart
        	 foundation models.**
        	2. If the model requires a legal agreement, select the
        	 check box to confirm that you agree.
        	3. If you want to add another model, repeat the previous
        	 step.
        3. To change how the model behave during inference choose,
         **Set parameters**.


        Set parameters contains a list of inference parameters that
         affect the degree of randomness in your model's output, the
         length of your model's output, and what words the model will
         choose next.
        4. Next, select an **Task type**. You can select
         any of the following:




        	* **Text Summarization**
        	* **Question Answering
        	 (Q&A)**
        	* **Text classification**
        	* **Open-ended Generation**
        	* **Custom**
        5. In the **Evaluation metrics** section, choose
         an **Evaluation dimension** and enter
         additional context about the dimension in the text box under
         **Description**. You can choose from the
         following dimensions:




        	* **Fluency** – Measures the
        	 linguistic quality of a generated text.
        	* **Coherence** – Measures the
        	 organization and structure of a generated text.
        	* **Toxicity** – Measures the
        	 harmfulness of a generated text.
        	* **Accuracy**– Indicates the
        	 accuracy of a generated text.
        	* A custom evaluation dimension that you can define the
        	 name and description of for your work team.


        	To add a custom evaluation dimension, do the
        	 following:




        		+ Choose **Add an evaluation
        		 dimension**.
        		+ In the text box containing **Provide
        		 evaluation dimension**, input the name of
        		 your custom dimension.
        		+ In the text box containing **Provide
        		 description for this evaluation
        		 dimension**, input a description so that
        		 your work team understands how to evaluate your
        		 custom dimension.
        Under each of these metrics are reporting metrics that you can
         choose from the **Choose a metric type** down
         arrow. If you have two models to evaluate, you can choose either
         comparative or individual reporting metrics. If you have one
         model to evaluate, you can choose only individual reporting
         metrics. You can choose the following reporting metrics types
         for each of the above metrics.




        	* (Comparative) **Likert scale - comparison**  – A human evaluator will indicate
        	 their preference between two responses on a 5-point
        	 Likert scale according to your instructions. The results
        	 in the final report will be shown as a histogram of
        	 preference strength ratings from the evaluators over
        	 your whole dataset. Define the important points of the
        	 5-point scale in your instructions so that your
        	 evaluators know how to rate the responses according to
        	 your expectations. In the JSON output saved in Amazon S3 this choice is represented as `ComparisonLikertScale` the key value pair `"evaluationResults":"ComparisonLikertScale"`.
        	* (Comparative) **Choice buttons**
        	 – Allows a human evaluator to indicate their one
        	 preferred response over another response. Evaluators
        	 indicate their preference between two responses
        	 according to your instructions using radio buttons. The
        	 results in the final report will be shown as a
        	 percentage of responses that workers preferred for each
        	 model. Explain your evaluation method clearly in your
        	 instructions. In the JSON output saved in Amazon S3 this choice is represented as `ComparisonChoice` the key value pair `"evaluationResults":"ComparisonChoice"`.
        	* (Comparative) **Ordinal Rank**
        	 – Allows a human evaluator to rank their
        	 preferred responses to a prompt in order, starting at
        	 `1`, according to your instructions. The
        	 results in the final report will be shown as a histogram
        	 of the rankings from the evaluators over the whole
        	 dataset. Define the what a rank of `1` means
        	 in your instructions. In the JSON output saved in Amazon S3 this choice is represented as `ComparisonRank` the key value pair `"evaluationResults":"ComparisonRank"`.
        	* (Individual) **Thumbs up/down**
        	 – Allows a human evaluator to rate each response
        	 from a model as acceptable or unacceptable according to
        	 your instructions. The results in the final report will
        	 be shown as a percentage of the total number of ratings
        	 by evaluators that received a thumbs up rating for each
        	 model. You may use this rating method for an evaluation
        	 one or more models. If you use this in an evaluation
        	 that contains two models, a thumbs up or down will be
        	 presented to your work team for each model response and
        	 the final report will show the aggregated results for
        	 each model individually. Define what is acceptable as a
        	 thumbs up or thumbs down rating in your
        	 instructions. In the JSON output saved in Amazon S3 this choice is represented as `ThumbsUpDown` the key value pair `"evaluationResults":"ThumbsUpDown"`.
        	* (Individual) **Likert scale -
        	 individual** – Allows a human
        	 evaluator to indicate how strongly they approve of the
        	 model response based on your instructions on a 5-point
        	 Likert scale. The results in the final report will be
        	 shown as a histogram of the 5-point ratings from the
        	 evaluators over your whole dataset. You may use this
        	 scale for an evaluation containing one or more models.
        	 If you select this rating method in an evaluation that
        	 contains more than one model, a 5-point Likert scale
        	 will be presented to your work team for each model
        	 response and the final report will show the aggregated
        	 results for each model individually. Define the
        	 important points on the 5-point scale in your
        	 instructions so that your evaluators know how to rate
        	 the responses according to your expectations. In the JSON output saved in Amazon S3 this choice is represented as `IndividualLikertScale` the key value pair `"evaluationResults":"IndividualLikertScale"`.
        6. Choose a **Prompt dataset**. This dataset is
         required and will be used by your human work team to evaluate
         responses from your model. Provide the S3 URI to an Amazon S3 bucket
         that contains your prompt dataset in the text box under
         **S3 URI for your input dataset file**. Your dataset must be in
         `jsonlines` format and contain the following keys
         to identify which parts of your dataset the UI will use to
         evaluate your model:




        	* `prompt` – The request that you want
        	 your model to generate a response to.
        	* (Optional) `category` – - The
        	 category labels for your prompt. The
        	 `category` key is used to categorize your
        	 prompts so you can filter your evaluation results later
        	 by category for a deeper understanding of the evaluation
        	 results. It does not participate in the evaluation
        	 itself, and workers do not see it on the evaluation
        	 UI.
        	* (Optional) `referenceResponse` – The
        	 reference answer for your human evaluators. The
        	 reference answer is not rated by your workers, but can
        	 be used to understand what responses are acceptable or
        	 unacceptable, based on your instructions.
        	* (Optional) `responses` – Used to
        	 specify inferences from a model outside of SageMaker AI or
        	 outside of AWS.


        	This object *requires* two additional key value pairs
        	 `"modelIdentifier` which is a string that
        	 identifies the model, and `"text"` which is
        	 the model's inference.


        	If you specify a `"responses"` key in any
        	 input of the of custom prompt dataset it must be specified
        	 in all inputs.
        	* The following `json` code example shows the accepted key-value pairs in a custom prompt dataset. The **Bring your own inference** check box must be checked if a responses key is provided. If checked, the `responses` key must always be specified in each prompt. The following example could be used in a question and answer scenario.



        	```
        	{
        	    "prompt": {
        	        "text": "Aurillac is the capital of"
        	    },
        	    "category": "Capitals",
        	    "referenceResponse": {
        	        "text": "Cantal"
        	    },
        	    "responses": [
        	        // All responses must come from a single model. If specified it must be present in all JSON objects. modelIdentifier and text are then also required.
        	        {
        	            "modelIdentifier": `"meta-textgeneration-llama-codellama-7b"`,
        	            "text": `"The capital of Aurillac is Cantal."`
        	        }
        	    ]
        	}
        	```
        7. Input an S3 bucket location where you want to save the output evaluation results in the text box under **Choose an S3 location to save your evaluation results**. The output file written to this S3 location will be in `JSON` format, ending in the extension,`.json`.
        8. ###### Note

        If you want to include bring your own inference data in
         the model evaluation job, you can only use a single
         model.


        (Optional) Choose the check box under **Bring your
         own inference** to indicate that your prompt
         dataset contains the `responses` key. If you specify
         the `responses` key as part of
         *any* prompts it must be present in all
         of them.
        9. Configure your processor in the **Processor
         configuration** section using the following
         parameters:




        	* Use **Instance count** to specify the
        	 number of compute instances to use to run your model. If
        	 you use more than `1` instance, your model
        	 will run in parallel instances.
        	* Use **Instance type** to choose the
        	 kind of compute instance you want to use to run your
        	 model. AWS has general compute instances and instances
        	 that are optimized for computing and memory. For more
        	 information about instance types, see [Instance Types Available for Use With
        	 Amazon SageMaker Studio Classic Notebooks](notebooks-available-instance-types.md "notebooks-available-instance-types.md")
        	 .
        	* If you want SageMaker AI to use your own AWS Key Management Service (AWS KMS)
        	 encryption key instead of the default AWS managed
        	 service key, toggle to select **On**
        	 under **Volume KMS key**, and input the
        	 AWS KMS key. SageMaker AI will use your AWS KMS key to encrypt data
        	 on the storage volume. For more information about keys,
        	 see [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
        	* If you want SageMaker AI to use your own AWS Key Management Service (AWS KMS)
        	 encryption key instead of the default AWS managed
        	 service key, toggle to select **On**
        	 under **Output KMS key** and input the
        	 AWS KMS key. SageMaker AI will use your AWS KMS key to encrypt the
        	 processing job output.
        	* Use an IAM role to specify the access and
        	 permissions for the default processor. Input the IAM
        	 role that you set up in the section **Set up your IAM role** in
        	 this **Run a human
        	 evaluation** section.
        10. After you specify your model and criteria, select
         **Next**.

    Your work team consists of the people that are evaluating your model. After
    your work team is created, it persists indefinitely and you cannot change its
    attributes. The following shows how to get started with your work team.

###### Set up your work team

1. Choose an existing team or **Create a new team** in
   the **Select team** input text box.
2. Specify a name of your organization in **Organization
   name**. This field only appears when you create the first
   work team in the account.
3. Specify a **contact email**. Your workers will use
   this email to communicate with you about the evaluation task that you
   will provide to them. This field only appears when you create the first
   work team in the account.
4. Specify a **Team name**. You cannot change this name
   later.
5. Specify a list of **Email addresses** for each of
   your human workers that will evaluate your large language model (LLM).
   When you specify the email addresses for your team, they are notified of
   a new job only when they are newly added to a work team. If you use the
   same team for a subsequent job, you must notify them manually.
6. Then, specify the **Number of workers per prompt**

###### Provide instructions for your work team

1. Provide detailed instructions to your human workforce so that they can
   evaluate your model to your metrics and standards. A template in the
   main window shows sample instructions that you can provide. For more
   information about how to give instructions, see [Creating good worker instructions](../../../bedrock/latest/userguide/worker-job.md "../../../bedrock/latest/userguide/worker-job.md").
2. To minimize bias in your human evaluation, select the check box next to
   **Randomize response positions**.
3. Select **Next**.
   You can review the summary of the selections that you have made for your human
   job. If you must change your job, choose **Previous** to go
   back to an earlier selection.

###### Submit your evaluation job request and view job progress

1. To submit your evaluation job request, choose **Create
   resource**.
2. To see the status of all of your jobs, choose
   **Jobs** in the navigation pane. Then, choose
   **Model evaluation**. The evaluation status
   displays as **Completed**, **Failed**,
   or **In progress**.

The following also displays:

    * Sample notebooks to run a model evaluation in SageMaker AI and
     Amazon Bedrock.
    * Links to additional information including documentation,
     videos, news, and blogs about the model evaluation
     process.
    * The URL to your **Private worker portal** is also available.

3. Select your model evaluation under **Name** to view a
   summary of your evaluation.
   - The summary gives information about the status of the job,
     what kind of evaluation task you ran on which model, and when it
     ran. Following the summary, the human evaluation scores are
     sorted and summarized by metric.

###### View the report card of you model evaluation job that uses human workers

1. To see the report for your jobs, choose
   **Jobs** in the navigation pane.
2. Then, choose
   **Model evaluation**. One the **Model evaluations** home page, use the table to find your model evaluation job. Once the job status has changed to **Completed** you can view your report card.
3. Choose the name of the model evaluation job to it's report card.
   When you create a model evaluation job that uses human workers you have the
   option to bring your own inference data, and have your human workers compare
   that inference data to data produced by one other JumpStart model or a
   JumpStart model that you have deployed to an endpoint.

This topic describes the format required for the inference data, and a
simplified procedure for how to add that data to your model evaluation
job.

Choose a **Prompt dataset**. This dataset is required and
will be used by your human work team to evaluate responses from your model.
Provide the S3 URI to an Amazon S3 bucket that contains your prompt dataset in the text
box under **Choose an S3 location to save your evaluation results**. Your dataset must be in
`.jsonl` format. Each record must be a valid JSON object, and
contain the following required keys:

- `prompt` – A JSON object that contains the text to
  be passed into the model.
- (Optional) `category` – - The category labels for
  your prompt. The `category` key is used to categorize your
  prompts so you can filter your evaluation results later by category for
  a deeper understanding of the evaluation results. It does not
  participate in the evaluation itself, and workers do not see it on the
  evaluation UI.
- (Optional) `referenceResponse` – a JSON object that
  contains the reference answer for your human evaluators. The reference
  answer is not rated by your workers, but can be used to understand what
  responses are acceptable or unacceptable, based on your
  instructions.
- `responses` – Used to specify individual inferences
  from a model outside of SageMaker AI or outside of AWS.

This object requires to additional key value pairs
`"modelIdentifier` which is a string that identifies the
model, and `"text"` which is the model's inference.

If you specify a `"responses"` key in any input of the of
custom prompt dataset it must be specified in all inputs.
The following `json` code example shows the accepted key-value
pairs in a custom prompt dataset that contains your own inference data.

```
{
    "prompt": {
        "text": "Who invented the airplane?"
    },
    "category": "Airplanes",
    "referenceResponse": {
        "text": "Orville and Wilbur Wright"
    },
    "responses":
        // All inference must come from a single model
        [{
            "modelIdentifier": `"meta-textgeneration-llama-codellama-7b"` ,
            "text": "The Wright brothers, Orville and Wilbur Wright are widely credited with inventing and manufacturing the world's first successful airplane."
        }]

}
```

To get started launch Studio, and under choose **Model
evaluation** under **Jobs** in the primary
navigation.

###### To add your own inference data to a human model evaluation job.

1. In **Step 1: Specify job details** add the name of
   your model evaluation job, and an optional description.
2. In **Step 2: Set up evaluation** choose
   **Human**.
3. Next, under **Choose the model(s) you want to
   evaluate** you can choose the model that you want to use.
   You can use either a JumpStart model that has already deployed or
   you can choose a **Pre-trained Jumpstart foundation
   model**.
4. Then, choose a **Task type**.
5. Next, you can add **Evaluation metrics**.
6. Next, under **Prompt dataset** choose the check box under **Bring your own inference** to indicate that your prompts have response keys in it.
7. Then continue setting up your model evaluation job.
   To learn more about how the responses from your model evaluation job that uses
   human workers are saved, see [Understand the results
   of a human evaluation job](clarify-foundation-model-evaluate-results-human.md "clarify-foundation-model-evaluate-results-human.md")
