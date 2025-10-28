# Create a Labeling Job (API)

To create a labeling job using the Amazon SageMaker API, you use the [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") operation. For specific instructions on
creating a labeling job for a built-in task type, see that [task type page](sms-task-types.md "sms-task-types.md"). To learn how to
create a streaming labeling job, which is a labeling job that runs perpetually, see [Create a streaming labeling job](sms-streaming-create-job.md "sms-streaming-create-job.md").

To use the `CreateLabelingJob` operation, you need the following:

- A worker task template (`UiTemplateS3Uri`) or human task UI ARN
  (`HumanTaskUiArn`) in Amazon S3.
  - For 3D point cloud jobs, video object detection and tracking jobs, and NER jobs, use the ARN listed in `HumanTaskUiArn` for your task type.
  - If you are using a built-in task type other than 3D point cloud tasks, you
    can add your worker instructions to one of the pre-built templates and save
    the template (using a .html or .liquid extension) in your S3 bucket. Find
    the pre-build templates on your [task type
    page](sms-task-types.md "sms-task-types.md").
  - If you are using a custom labeling workflow, you can create a custom
    template and save the template in your S3 bucket. To learn how to built a
    custom worker template, see [Creating a custom worker task template](sms-custom-templates-step2.md "sms-custom-templates-step2.md"). For custom HTML elements
    that you can use to customize your template, see [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md"). For a repository of demo
    templates for a variety of labeling tasks, see [Amazon SageMaker Ground Truth Sample Task UIs](https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis "https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis") .

- An input manifest file that specifies your input data in Amazon S3. Specify the
  location of your input manifest file in `ManifestS3Uri`. For information
  about creating an input manifest, see [Input data](sms-data-input.md "sms-data-input.md"). If you create a streaming labeling job, this
  is optional. To learn how to create a streaming labeling job, see [Create a streaming labeling job](sms-streaming-create-job.md "sms-streaming-create-job.md").
- An Amazon S3 bucket to store your output data. You specify this bucket, and optionally,
  a prefix in `S3OutputPath`.
- A label category configuration file. Each label category name must be unique.
  Specify the location of this file in Amazon S3 using the
  `LabelCategoryConfigS3Uri` parameter. The format and label categories
  for this file depend on the task type you use:
  - For image classification and text classification (single and multi-label)
    you must specify at least two label categories. For all other task types,
    the minimum number of label categories required is one.
  - For named entity recognition tasks, you must provide worker instructions
    in this file. See [Provide Worker Instructions in a Label
    Category Configuration File](sms-named-entity-recg.md#worker-instructions-ner "sms-named-entity-recg.md#worker-instructions-ner") for details and an example.
  - For 3D point cloud and video frame task type, use the format in [Labeling category configuration file with
    label category and frame attributes reference](sms-label-cat-config-attributes.md "sms-label-cat-config-attributes.md").
  - For all other built-in task types and custom tasks, your label category
    configuration file must be a JSON file in the following format. Identify the
    labels you want to use by replacing `label_1`,
    `label_2`,`...`,`label_n` with your
    label categories.

  ```
  {
      "document-version": "2018-11-28",
      "labels": [
          {"label": "`label_1`"},
          {"label": "`label_2`"},
          ...
          {"label": "`label_n`"}
      ]
  }
  ```

- An AWS Identity and Access Management (IAM) role with the [AmazonSageMakerGroundTruthExecution](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerGroundTruthExecution "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerGroundTruthExecution") managed IAM policy attached and
  with permissions to access your S3 buckets. Specify this role in
  `RoleArn`. To learn more about this policy, see [Use IAM Managed Policies with Ground Truth](sms-security-permissions-get-started.md "sms-security-permissions-get-started.md"). If you require more
  granular permissions, see [Assign IAM Permissions to Use Ground Truth](sms-security-permission.md "sms-security-permission.md").

If your input or output bucket name does not contain `sagemaker`, you
can attach a policy similar to the following to the role that is passed to the
`CreateLabelingJob` operation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`my_input_bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`my_output_bucket`/*"
 ]
 }
 ]
}`

```

- A pre-annotation and post-annotation (or annotation-consolidation) AWS Lambda
  function Amazon Resource Name (ARN) to process your input and output data.
  - Lambda functions are predefined in each AWS Region for built-in task types.
    To find the pre-annotation Lambda ARN for your Region, see [PreHumanTaskLambdaArn](API_HumanTaskConfig.md#SageMaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn "API_HumanTaskConfig.md#SageMaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn"). To find the annotation-consolidation
    Lambda ARN for your Region, see [AnnotationConsolidationLambdaArn](API_AnnotationConsolidationConfig.md#SageMaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn "API_AnnotationConsolidationConfig.md#SageMaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn").
  - For custom labeling workflows, you must provide a custom pre- and
    post-annotation Lambda ARN. To learn how to create these Lambda functions, see
    [Processing data in a custom labeling workflow with AWS Lambda](sms-custom-templates-step3.md "sms-custom-templates-step3.md").

- A work team ARN that you specify in `WorkteamArn`. You receive a work
  team ARN when you subscribe to a vendor workforce or create a private workteam. If
  you are creating a labeling job for a video frame or point cloud task type, you
  cannot use the Amazon Mechanical Turk workforce. For all other task types,
  to use the Mechanical Turk workforce, use the following ARN. Replace
  `region` with the AWS Region you are
  using to create the labeling job.

`arn:aws:sagemaker:`region`:394669845002:workteam/public-crowd/default`

If you use the [Amazon Mechanical Turk workforce](sms-workforce-management-public.md "sms-workforce-management-public.md"), use the
`ContentClassifiers` parameter in `DataAttributes` of
`InputConfig` to declare that your content is free of personally
identifiable information and adult content.

Ground Truth _requires_ that your input data is free of personally
identifiable information (PII) if you use the Mechanical Turk workforce. If you use
Mechanical Turk and do not specify that your input data is free of PII using the
`FreeOfPersonallyIdentifiableInformation` flag, your labeling job
will fail. Use the `FreeOfAdultContent` flag to declare that your input
data is free of adult content. SageMaker AI may restrict the Amazon Mechanical Turk workers
that can view your task if it contains adult content.

To learn more about work teams and workforces, see [Workforces](sms-workforce-management.md "sms-workforce-management.md").

- If you use the Mechanical Turk workforce, you must specify the price you'll pay workers for
  performing a single task in `**PublicWorkforceTaskPrice**`.
- To configure the task, you must provide a task description and title using
  `TaskDescription` and `**TaskTitle**` respectively. Optionally, you can provide time
  limits that control how long the workers have to work on an individual task
  (`**TaskTimeLimitInSeconds**`) and
  how long tasks remain in the worker portal, available to workers
  (`TaskAvailabilityLifetimeInSeconds`).
- (Optional) For [some task
  types](sms-annotation-consolidation.md "sms-annotation-consolidation.md"), you can have multiple workers label a single data object by
  inputting a number greater than one for the
  `NumberOfHumanWorkersPerDataObject` parameter. For more information
  about annotation consolidation, see [Annotation consolidation](sms-annotation-consolidation.md "sms-annotation-consolidation.md").
- (Optional) To create an automated data labeling job, specify one of the ARNs
  listed in [LabelingJobAlgorithmSpecificationArn](../APIReference/API_LabelingJobAlgorithmsConfig.md "../APIReference/API_LabelingJobAlgorithmsConfig.md") in
  `LabelingJobAlgorithmsConfig`. This ARN identifies the algorithm used
  in the automated data labeling job. The task type associated with this ARN must
  match the task type of the `PreHumanTaskLambdaArn` and
  `AnnotationConsolidationLambdaArn` you specify. Automated data
  labeling is supported for the following task types: image classification, bounding
  box, semantic segmentation, and text classification. The minimum number of objects
  allowed for automated data labeling is 1,250, and we strongly suggest providing a
  minimum of 5,000 objects. To learn more about automated data labeling jobs, see
  [Automate data labeling](sms-automated-labeling.md "sms-automated-labeling.md").
- (Optional) You can provide [`StoppingConditions`](../APIReference/API_CreateLabelingJob.md#API_CreateLabelingJob_RequestSyntax "../APIReference/API_CreateLabelingJob.md#API_CreateLabelingJob_RequestSyntax") that cause the labeling job to stop
  if one the conditions is met. You can use stopping conditions to control the cost of
  the labeling job.

## Examples

The following code examples demonstrate how to create a labeling job using
`CreateLabelingJob`. You can also see these example notebooks on GitHub
in the [SageMaker AI Examples repository](https://github.com/aws/amazon-sagemaker-examples/tree/master/ground_truth_labeling_jobs "https://github.com/aws/amazon-sagemaker-examples/tree/master/ground_truth_labeling_jobs").

AWS SDK for Python (Boto3)
The following is an example of an [AWS Python SDK (Boto3) request](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job") to create a labeling job for a
built-in task type in the US East (N. Virginia) Region using a private
workforce. Replace all `red-italized text` with
your labeling job resources and specifications.

```
response = client.create_labeling_job(
    LabelingJobName=`"example-labeling-job"`,
    LabelAttributeName=`"label"`,
    InputConfig={
        'DataSource': {
            'S3DataSource': {
                'ManifestS3Uri': `"s3://bucket/path/manifest-with-input-data.json"`
            }
        },
        'DataAttributes': {
            'ContentClassifiers': [
                `"FreeOfPersonallyIdentifiableInformation"|"FreeOfAdultContent"`,
            ]
        }
    },
    OutputConfig={
        'S3OutputPath': `"s3://bucket/path/file-to-store-output-data"`,
        'KmsKeyId': `"string"`
    },
    RoleArn="`arn:aws:iam::*:role/*`",
    LabelCategoryConfigS3Uri=`"s3://bucket/path/label-categories.json"`,
    StoppingConditions={
        'MaxHumanLabeledObjectCount': `123`,
        'MaxPercentageOfInputDatasetLabeled': `123`
    },
    HumanTaskConfig={
        'WorkteamArn': `"arn:aws:sagemaker:region:*:workteam/private-crowd/*"`,
        'UiConfig': {
            'UiTemplateS3Uri': `"s3://bucket/path/custom-worker-task-template.html"`
        },
        'PreHumanTaskLambdaArn': "arn:aws:lambda:`us-east-1:432418664414`:function:PRE-`tasktype`",
        'TaskKeywords': [
            "`Images`",
            "`Classification`",
            "`Multi-label`"
        ],
        'TaskTitle': `"Multi-label image classification task"`,
        'TaskDescription': `"Select all labels that apply to the images shown"`,
        'NumberOfHumanWorkersPerDataObject': `1`,
        'TaskTimeLimitInSeconds': `3600`,
        'TaskAvailabilityLifetimeInSeconds': `21600`,
        'MaxConcurrentTaskCount': `1000`,
        'AnnotationConsolidationConfig': {
            'AnnotationConsolidationLambdaArn': "arn:aws:lambda:`us-east-1:432418664414`:function:ACS-"
        },
    Tags=[
        {
            'Key': `"string"`,
            'Value': `"string"`        },
    ]
)
```

AWS CLI
The following is an example of an AWS CLI request to create a labeling job
for a built-in task type in the US East (N. Virginia) Region using the
[Amazon Mechanical Turk workforce](sms-workforce-management-public.md "sms-workforce-management-public.md"). For more information, see [start-human-loop](../../../cli/latest/reference/sagemaker/create-labeling-job.md "../../../cli/latest/reference/sagemaker/create-labeling-job.md") in the _[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")_. Replace all `red-italized
 text` with your labeling job resources and specifications.

```
`$` aws --region us-east-1 sagemaker create-labeling-job \
--labeling-job-name `"example-labeling-job"` \
--label-attribute-name `"label"` \
--role-arn "arn:aws:iam::`account-id`:role/`role-name`" \
--input-config '{
        "DataAttributes": {
            "ContentClassifiers": [
                `"FreeOfPersonallyIdentifiableInformation"`,
                `"FreeOfAdultContent"`
            ]
        },
        "DataSource": {
            "S3DataSource": {
                "ManifestS3Uri": `"s3://bucket/path/manifest-with-input-data.json"`
            }
        }
    }' \
--output-config '{
        "KmsKeyId": "",
        "S3OutputPath": `"s3://bucket/path/file-to-store-output-data"`
    }' \
--human-task-config '{
        "AnnotationConsolidationConfig": {
            "AnnotationConsolidationLambdaArn": "arn:aws:lambda:`us-east-1:432418664414`:function:ACS-"
        },
        "TaskAvailabilityLifetimeInSeconds": `21600`,
        "TaskTimeLimitInSeconds": `3600`,
        "NumberOfHumanWorkersPerDataObject": `1`,
        "PreHumanTaskLambdaArn":  "arn:aws:lambda:`us-east-1:432418664414`:function:PRE-`tasktype`",
        "WorkteamArn": `"arn:aws:sagemaker:us-east-1:394669845002:workteam/public-crowd/default"`,
        "PublicWorkforceTaskPrice": {
            "AmountInUsd": {
                "Dollars": `0`,
                "TenthFractionsOfACent": `6`,
                "Cents": `3`            }
        },
        "TaskDescription": `"Select all labels that apply to the images shown"`,
        "MaxConcurrentTaskCount": `1000`,
        "TaskTitle": `"Multi-label image classification task"`,,
        "TaskKeywords": [
            "`Images`",
            "`Classification`",
            "`Multi-label`"
        ],
        "UiConfig": {
            "UiTemplateS3Uri": `"s3://bucket/path/custom-worker-task-template.html"`
        }
    }'
```

For more information about this operation, see [CreateLabelingJob](API_CreateLabelingJob.md "API_CreateLabelingJob.md"). For
information about how to use other language-specific SDKs, see [See
Also](API_CreateLabelingJob.md#API_CreateLabelingJob_SeeAlso "API_CreateLabelingJob.md#API_CreateLabelingJob_SeeAlso") in the `CreateLabelingJobs`
topic.
