# Create an automatic model evaluation job in Studio

The wizard available in Studio guides you through choosing a model to
evaluate, selecting a task type, choosing metrics and datasets, and configuring any
required resources. The following topics show you how to format an optional custom
input dataset, set up your environment, and create the model evaluation job in
Studio.

To use your own custom prompt dataset, it
must be a `jsonlines` file, where each line is a valid JSON
object. Each JSON object _must_ contain a
single prompt.

To help ensure that the JumpStart model you select performs well,
SageMaker Clarify automatically formats all prompt datasets to be in format
that works best for the **Model**
**Evaluation dimensions** you select. For
built-in prompt datasets, SageMaker Clarify will also augment your prompt with
additional instructional text. To see how SageMaker Clarify will modify the prompts,
choose **prompt template** under an **Evaluation dimensions** you have added to the model
evaluation job. To see an example of how you can modify a prompt template,
see [Prompt template
example](clarify-foundation-model-evaluate-whatis.md#clarify-prompt-template "clarify-foundation-model-evaluate-whatis.md#clarify-prompt-template").

The toggle allows you to turn off or to turn on the automatic prompt
templating support that SageMaker Clarify provides for built-in datasets. Turning off the automatic prompt
templating allows, you to specify your own custom prompt templates that will be
applied to all prompts in your dataset.

To learn which keys are available for a custom dataset in the UI, refer to
the following task lists.

- `model_input` – Required to indicate the input
  for the following tasks.
  - The **prompt** that your
    model should response to in **open-ended
    generation**, **toxicity**, and **accuracy** tasks.
  - The **question** that your
    model should answer in **question
    answering**, and **factual
    knowledge** tasks.
  - The **text** that your model
    should summarize in **text
    summarization** tasks.
  - The **text** that your model
    should classify in **classification** tasks.
  - The **text** that you want
    your model to perturb in **semantic
    robustness** tasks.

- `target_output` – Required to indicate the
  response against which your model is evaluated for the following
  tasks.
  - The **answer** for **question**
    **answering**, **accuracy**, **semantic**
    **robustness**, and **factual**
    **evaluation** tasks.
  - For **accuracy**, and
    **semantic**
    **robustness** tasks, separate
    acceptable answers with an `<OR>`. The
    evaluation accepts any of the answers separated by a comma
    as correct. As an example, use
    `target_output="UK<OR>England<OR>United
 Kingdom"`, if you want to accept either
    `UK` or `England` or `United
 Kingdom` as acceptable answers.

- (Optional) `category` – Generates evaluation
  scores reported for each category.
- `sent_less_input` – Required to indicate the
  prompt that contains **less** bias for
  prompt stereotyping tasks.
- `sent_more_input` – Required to indicate the
  prompt that contains **more** bias for
  prompt stereotyping tasks.
  A factual knowledge evaluation requires both the question to ask and the
  answer to check the model response against. Use the key
  `model_input` with the value contained in the question, and
  the key `target_output` with the value contained in the answer as
  follows:

```
{"model_input": "Bobigny is the capital of", "target_output": "Seine-Saint-Denis", "category": "Capitals"}
```

The previous example is a single valid JSON object that makes up one
record in a`jsonlines` input file. Each JSON object is sent to
your model as a request. To make multiple requests, include multiple lines.
The following data input example is for a question answer task that uses an
optional `category` key for evaluation.

```
{"target_output":"Cantal","category":"Capitals","model_input":"Aurillac is the capital of"}
{"target_output":"Bamiyan Province","category":"Capitals","model_input":"Bamiyan city is the capital of"}
{"target_output":"Abkhazia","category":"Capitals","model_input":"Sokhumi is the capital of"}
```

If you evaluate your algorithm in the UI, the following defaults are set
for your input dataset:

- The
  number of records that the evaluation uses is fixed. The algorithm
  samples this number of requests randomly from your input
  dataset.
  - **To change this number:**
    Use the `fmeval` library as described in
    **Customize your work flow using the
    `fmeval` library**, and set the
    parameter `num_records` to your desired number of
    samples, or `-1` to specify the entire dataset.
    The default number of records that are evaluated is
    `100` for accuracy, prompt stereotyping,
    toxicity, classification, and semantic robustness tasks. The
    default number of records for a factual knowledge task is
    `300`.

- The target output delimiter as previously described in the
  `target_output` parameter is set to
  `<OR>` in the UI.
  - **To separate acceptable answers using
    another delimiter:** Use the
    `fmeval` library as described in **Customize your work flow using the
    `fmeval` library**, and set the
    parameter `target_output_delimiter` to your
    desired delimiter.

- You must use a text-based JumpStart language model that is
  available for model evaluation. These models have several data input
  configuration parameters that are passed automatically into the
  FMeval process.

      + **To use another kind of
       model:** Use the `fmeval` library to
       define the data configuration for your input dataset.

  To run an automatic evaluation for your large language model (LLM), you
  must set up your environment to have the correct permissions to run an
  evaluation. Then, you can use the UI to guide you through the steps in the
  work flow, and run an evaluation. The following sections show you how to use
  the UI to run an automatic evaluation.

###### Prerequisites

- To run a model evaluation in a Studio UI, your AWS Identity and Access Management
  (IAM) role and any input datasets must have the correct
  permissions. If you do not have a SageMaker AI Domain or IAM role, follow
  the steps in [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").

###### To set permissions for your S3 bucket

After your domain and role are created, use the following steps to add
the permissions needed to evaluate your model.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the navigation pane, enter `S3` into the
   search bar at the top of the page.
3. Choose **S3** under
   **Services**.
4. Choose **Buckets** from the navigation
   pane.
5. In the **General purpose buckets** section, under
   **Name**, choose the name of the Amazon S3 bucket
   that you want to use to store your custom prompt dataset, and where
   you want the results of your model evaluation job saved. Your
   Amazon S3 bucket must be in the same AWS Region as your
   Studio instance. If you don't have an Amazon S3 bucket, do the
   following.
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
8. To add the CORS permissions to your bucket copy the following code
   into the input box.

```
[
{
    "AllowedHeaders": [
        "*"
    ],
    "AllowedMethods": [
        "GET",
        "PUT",
        "POST",
        "DELETE"
    ],
    "AllowedOrigins": [
        "*"
    ],
    "ExposeHeaders": [
        "Access-Control-Allow-Origin"
    ]
}
]
```

9. Choose **Save changes**.

###### To add permissions to your IAM policy

1. In the search bar at the top of the page, enter
   `IAM`.
2. Under **Services**, select **Identity and
   Access Management (IAM)**.
3. Choose **Policies** from the navigation
   pane.
4. Choose **Create policy**. When the
   **Policy editor** opens, choose
   **JSON**.
5. Choose **Next**.
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
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
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
 "sagemaker:Search",
 "sagemaker:CreateProcessingJob",
 "sagemaker:DescribeProcessingJob"
 ],
 "Resource": "*"
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

1. Choose **Roles** in the navigation pane. Input
   the name of the role that you want to use.
2. Select the name of the role under **Role name**.
   The main window changes to show information about your role.
3. In the **Permissions** policies section, choose
   the down arrow next to **Add permissions**.
4. From the options that appear, choose **Attach
   policies**.
5. From the list of policies that appear, search for the policy that
   you created in Step 5. Select the check the box next to your
   policy's name.
6. Choose the down arrow next to **Actions**.
7. From the options that appear, select
   **Attach**.
8. Search for the name of the role that you created. Select the check
   box next to the name.
9. Choose **Add permissions**. A banner at the top
   of the page should state **Policy was successfully attached
   to role**.

- .
  When you create an automatic model evaluation job, you can choose from
  available text-based JumpStart models or you can use a text based
  JumpStart model that you've previous deployed to an endpoint.

To create a automatic model evaluation job use the following
procedure.

###### To launch an automatic model evaluation job in Studio.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the search bar at the top of the page, enter
   `SageMaker AI`.
3. Under **Services**, select
   **Amazon SageMaker AI**.
4. Choose **Studio** from the navigation
   pane.
5. Choose your domain from the **Get Started**
   section, after expanding the down arrow under **Select
   Domain**.
6. Choose your user profile from the **Get Started**
   section after expanding the down arrow under **Select user
   profile**.
7. Choose **Open Studio** to open the landing
   page for Studio.
8. Choose **Jobs** from the primary navigation
   pane.
9. Then, choose **Model evaluation**.

###### To set up an evaluation job

1.  Next, choose **Evaluate a model,**.
2.  In **Step 1: Specify job details** do the
    following:
    1. Enter the **Name** of your model
       evaluation. This name helps you identify your model
       evaluation job after it is submitted.
    2. Enter a **Description** to add more
       context to the name.
    3. Choose **Next**.

3.  In **Step 2: Set up evaluation** do the
    following:
    1. Under **Evaluation type** choose
       **Automatic**.
    2. Then, choose **Add model to
       evaluation**
    3. In the **Add model** modal you can choose
       to use either a **Pre-trained Jumpstart foundation
       model** or **SageMaker AI endpoint**.
       If you've already deployed JumpStart model choose
       **SageMaker AI endpoint** otherwise choose
       **Pre-trained Jumpstart foundation
       model**.
    4. Then, choose **Save**.
    5. (_Optional_) After adding your model
       choose **Prompt template** to see the
       expected input format for prompts based on the model you
       selected. For information about how to configure a prompt
       template for a dataset, see [Prompt templates](clarify-foundation-model-evaluate-whatis.md#clarify-automatic-jobs-summary-prompt-templates "clarify-foundation-model-evaluate-whatis.md#clarify-automatic-jobs-summary-prompt-templates").
       - To use the default prompt template, complete the following steps:
         1. Toggle on **Use the default prompt templates provided by the
            datasets**.
         2. (Optional) For each dataset, review the prompt supplied by Clarify.
         3. Choose **Save**.

       - To use a custom prompt template, complete the following steps:
         1. Toggle off **Use the default prompt templates provided by the
            datasets**.
         2. If Clarify displays a default prompt, you can customize it or remove it and supply
            your own. You must include the `$model_input` variable in the prompt template.
         3. Choose **Save**.

    6. Then, under **Task type** choose a task
       type.

    For more information about tasks types and the associated
    evaluation dimensions, see the **Automatic evaluation** in **[Using prompt datasets and available evaluation dimensions in model evaluation jobs](clarify-foundation-model-evaluate-overview.md "clarify-foundation-model-evaluate-overview.md")** . 7. In the **Evaluation metrics** section,
    choose an **Evaluation dimension**. The
    text box under **Description** contains
    additional context about the dimension.

    After you select a task, the metrics associated with the
    task appear under **Metrics**. In this
    section, do the following. 8. Select an evaluation dimension from the down arrow under
    **Evaluation dimension**. 9. Choose an evaluation dataset. You can choose to use your
    own dataset or use a built-in dataset. If you want to use
    your own dataset to evaluate the model, it must be formatted
    in a way that FMEval can use. It must also be located in an
    S3 bucket that has the CORS permissions referenced in the
    previous [Set up your environment](#clarify-foundation-model-evaluate-auto-ui-setup "#clarify-foundation-model-evaluate-auto-ui-setup") section. For more information about how to format a
    custom dataset see [Use a
    custom input dataset](clarify-foundation-model-evaluate-auto-lib-custom.md#clarify-foundation-model-evaluate-auto-lib-custom-input "clarify-foundation-model-evaluate-auto-lib-custom.md#clarify-foundation-model-evaluate-auto-lib-custom-input"). 10. Input an S3 bucket location where you want to save the
    output evaluation results. This file is in jsonlines
    (.jsonl) format. 11. Configure your processor in the **Processor
    configuration** section using the following
    parameters:

        * Use **Instance count** to specify
         the number of compute instances you want to use to
         run your model. If you use more than `1`
         instance, your model is run in parallel
         instances.
        * Use **Instance type** to choose
         the kind of compute instance you want to use to run
         your model. For more information about instance
         types, see [Instance Types Available for Use With
         Amazon SageMaker Studio Classic Notebooks](notebooks-available-instance-types.md "notebooks-available-instance-types.md").
        * Use **Volume KMS** key to specify
         your AWS Key Management Service (AWS KMS) encryption key. SageMaker AI uses
         your AWS KMS key to encrypt incoming traffic from the
         model and your Amazon S3 bucket. For more information
         about keys, see [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
        * Use **Output KMS key** to specify
         your AWS KMS encryption key for outgoing
         traffic.
        * Use **IAM Role** to specify the
         access and permissions for the default processor.
         Enter the IAM role that you set up in [Set up your environment](#clarify-foundation-model-evaluate-auto-ui-setup "#clarify-foundation-model-evaluate-auto-ui-setup")

    12. After you specify your model and criteria, choose
        **Next**. The main window skips to
        **Step 5 Review and Save**.

###### Review and run your evaluation job

1. Review all of the parameters, model, and data that you selected
   for your evaluation.
2. Choose **Create resource** to run your
   evaluation.
3. To check your job status, go to the top of the **Model
   Evaluations** section on the page.
