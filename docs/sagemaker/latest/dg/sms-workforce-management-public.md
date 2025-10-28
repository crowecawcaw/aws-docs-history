# Using the Amazon Mechanical Turk Workforce

The Amazon Mechanical Turk (Mechanical Turk) workforce provides the most workers for your [Amazon SageMaker Ground Truth](a2i.md "a2i.md") labeling job
and [Amazon Augmented AI](a2i-use-augmented-ai-a2i-human-review-loops.md "a2i-use-augmented-ai-a2i-human-review-loops.md") human review task. The Amazon Mechanical Turk workforce is a world-wide resource.
Workers are available 24 hours a day, 7 days a week. You typically get the fastest
turnaround for your human review tasks and labeling jobs when you use the Amazon Mechanical Turk
workforce.

Any Amazon Mechanical Turk workforce billing is handled as part of your Ground Truth or Amazon Augmented AI billing. You
do not need to create a separate Mechanical Turk account to use the Amazon Mechanical Turk workforce.

###### Important

You should not share confidential information, personal information, or protected
health information with this workforce. You should not use the Amazon Mechanical Turk workforce when
you use Amazon A2I in conjunction with AWS HIPAA-eligible services, such as
Amazon Textract and Amazon Rekognition, for workloads containing protected health
information.

You can choose Mechanical Turk as your workforce when you create a Ground Truth labeling job or
Amazon A2I human review workflow (flow definition). You can create a labeling job and a
human review workflow using the SageMaker AI console and API.

When you use an API operation to create a labeling job or human review workflow, you use
the following ARN for the Amazon Mechanical Turk workforce for your `WorkteamArn`. Replace
`region` with the AWS Region you are using to
create the labeling job or human loops. For example, if you create a labeling job in
US West (Oregon), replace `region` with
`us-west-2`.

- `arn:aws:sagemaker:`region`:394669845002:workteam/public-crowd/default`
  Ground Truth and Amazon A2I _require_ that your input data is
  free of personally identifiable information (PII) when you use Mechanical Turk. If you use the Mechanical Turk
  workforce and do not specify that your input data is free of PII, your Ground Truth labeling jobs
  and Augmented AI tasks will fail. You specify that your input data is free of PII when you create a
  Ground Truth labeling job and when you create a Amazon A2I human loop using a built-in integration
  or the `StartHumanLoop` operation.

Use the following sections to learn how to use Mechanical Turk with these services.

###### Topics

- [Use Mechanical Turk with Ground Truth](#sms-workforce-management-public-unsupported "#sms-workforce-management-public-unsupported")
- [Use Mechanical Turk with Amazon A2I](#sms-workforce-management-public-gt "#sms-workforce-management-public-gt")
- [When is Mechanical Turk Not Supported?](#sms-workforce-management-public-a2i "#sms-workforce-management-public-a2i")

## Use Mechanical Turk with Ground Truth

You can use Mechanical Turk with Ground Truth when you create a labeling job using the console, or the
`CreateLabelingJob` operation.

When you create a labeling job, we recommend you adjust the number of workers that
annotate each data object based on the complexity of the job and the quality that you
need. Amazon SageMaker Ground Truth uses annotation consolidation to improve the quality of the labels. More
workers can make a difference in the quality of the labels for more complex labeling
jobs, but might not make a difference for simpler jobs. For more information, see [Annotation consolidation](sms-annotation-consolidation.md "sms-annotation-consolidation.md"). Note that annotation consolidation is not supported for Amazon A2I human review
workflows.

###### To use Mechanical Turk when you create a labeling job (console):

1. Use the following to create a labeling job using the Ground Truth area of the SageMaker AI
   console: [Create a Labeling Job (Console)](sms-create-labeling-job-console.md "sms-create-labeling-job-console.md").
2. When you are selecting **Worker types** in the
   **Workers** section, select
   **Amazon Mechanical Turk**.
3. Specify the total amount of time workers have to complete a task using
   **Task timeout**.
4. Specify the total amount of time a task remains available to workers in
   **Task expiration**. This is how long workers have to pick
   up a task before it fails.
5. Select the **Price per task** using the dropdown list. This
   is the amount of money a worker receives for completing a single task.
6. (Optional) If applicable, select **The dataset does not contain adult
   content**. SageMaker AI may restrict the Mechanical Turk workers that can view your
   task if it contains adult content.
7. You must read and confirm the following statement by selecting the check box
   to use the Mechanical Turk workforce. If your input data contains confidential information,
   personal information, or protected health information, you must select another
   workforce.

**You understand and agree that the Mechanical Turk workforce consists of
independent contractors located worldwide and that you should not share
confidential information, personal information, or protected health
information with this workforce.** 8. (Optional) Select the check box next to **Enable automated data
labeling** if you want to enable automated data labeling. To learn
more about this feature, see [Automate data labeling](sms-automated-labeling.md "sms-automated-labeling.md"). 9. You can specify the **Number of workers per dataset object**
under **Additional configuration**. For example, if you enter 3
in this field, each data object will be labeled by 3 workers.

When you create your labeling job by selecting **Create**, your
labeling tasks are sent to Mechanical Turk workers.

###### To use Mechanical Turk when you create a labeling job (API):

1. Use the following to create a labeling job using the `CreateLabelingJob` operation: [Create a Labeling Job (API)](sms-create-labeling-job-api.md "sms-create-labeling-job-api.md").
2. Use the following for the [`WorkteamArn`](../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-WorkteamArn "../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-WorkteamArn"). Replace
   `region` with the AWS Region you
   are using to create the labeling job.

`arn:aws:sagemaker:`region`:394669845002:workteam/public-crowd/default` 3. Use `TaskTimeLimitInSeconds` to specify the total amount of
time workers have to complete a task. 4. Use `TaskAvailabilityLifetimeInSeconds` to specify the total
amount of time a task remains available to workers. This is how long workers
have to pick up a task before it fails. 5. Use `NumberOfHumanWorkersPerDataObject` to specify
the number of workers per dataset object. 6. Use `PublicWorkforceTaskPrice` to set the price per task. This
is the amount of money a worker receives for completing a single task. 7. Use `DataAttributes` to specify that your input data is free
of confidential information, personal information, or protected health
information.

Ground Truth _requires_ that your input data is free of personally
identifiable information (PII) if you use the Mechanical Turk workforce. If you use Mechanical Turk
and do not specify that your input data is free of PII using the
`FreeOfPersonallyIdentifiableInformation` flag, your labeling job
will fail.

Use the `FreeOfAdultContent` flag to declare that your input data
is free of adult content. SageMaker AI may restrict the Mechanical Turk workers that can view your
task if it contains adult content.

You can see examples of how to use this API in the following notebooks, found on
GitHub: [Ground Truth Jupyter Notebook Examples](https://github.com/aws/amazon-sagemaker-examples/tree/master/ground_truth_labeling_jobs "https://github.com/aws/amazon-sagemaker-examples/tree/master/ground_truth_labeling_jobs").

## Use Mechanical Turk with Amazon A2I

You can specify that you want to use Mechanical Turk with Amazon A2I when you create a human
review workflow, also referred to as a _flow
definition_, in the console, or with the `CreateFlowDefinition`
API operation. When you use this human review workflow to configure human loops, you
must specify that your input data is free of PII.

###### To use Mechanical Turk when you create a human review workflow (console):

1. Use the following to create a human review workflow in the Augmented AI section of
   the SageMaker AI console: [Create a Human Review Workflow
   (Console)](a2i-create-flow-definition.md#a2i-create-human-review-console "a2i-create-flow-definition.md#a2i-create-human-review-console").
2. When you are selecting **Worker types** in the
   **Workers** section, select
   **Amazon Mechanical Turk**.
3. Select the **Price per task** using the dropdown list. This
   is the amount of money a worker receives for completing a single task.
4. (Optional) You can specify the **Number of workers per dataset
   object** under **Additional configuration**. For
   example, if you enter 3 in this field, each data object will be labeled by 3
   workers.
5. (Optional) Specify the total amount of time workers have to complete a task
   using **Task timeout**.
6. (Optional) Specify the total amount of time a task remains available to
   workers in **Task expiration**. This is how long workers have
   to pick up a task before it fails.
7. Once you have created your human review workflow, you can use it to configure
   a human loop by providing its Amazon Resource Name (ARN) in the parameter
   `FlowDefinitionArn`. You configure a human loop using one of the
   API operations of a built-in task type, or the Amazon A2I runtime API operation,
   `StartHumanLoop`. To learn more, see [Create and Start a Human Loop](a2i-start-human-loop.md "a2i-start-human-loop.md").

When you configure your human loop, you must specify that your input data is
free of personally identifiable information (PII) using the
`FreeOfPersonallyIdentifiableInformation` content classifier in
`DataAttributes`. If you use Mechanical Turk and do not specify that your
input data is free of PII, your human review tasks will fail.

Use the `FreeOfAdultContent` flag to declare that your input data
is free of adult content. SageMaker AI may restrict the Mechanical Turk workers that can view your
task if it contains adult content.

###### To use Mechanical Turk when you create a human review workflow (API):

1. Use the following to create a human review workflow using the
   `CreateFlowDefinition` operation: [Create a Human Review Workflow (API)](a2i-create-flow-definition.md#a2i-create-human-review-api "a2i-create-flow-definition.md#a2i-create-human-review-api").
2. Use the following for the [`WorkteamArn`](../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-WorkteamArn "../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-WorkteamArn"). Replace
   `region` with the AWS Region you
   are using to create the labeling job.

`arn:aws:sagemaker:`region`:394669845002:workteam/public-crowd/default` 3. Use `TaskTimeLimitInSeconds` to specify the total amount of
time workers have to complete a task. 4. Use `TaskAvailabilityLifetimeInSeconds` to specify the total
amount of time a task remains available to workers. This is how long workers
have to pick up a task before it fails. 5. Use `TaskCount` to specify the number of workers per dataset
object. For example, if you specify 3 for this parameter, each data object will
be labeled by 3 workers. 6. Use `PublicWorkforceTaskPrice` to set the price per task. This
is the amount of money a worker receives for completing a single task. 7. Once you have created your human review workflow, you can use it to configure
a human loop by providing its Amazon Resource Name (ARN) in the parameter
`FlowDefinitionArn`. You configure a human loop using one of the
API operations of a built-in task type, or the Amazon A2I runtime API operation,
`StartHumanLoop`. To learn more, see [Create and Start a Human Loop](a2i-start-human-loop.md "a2i-start-human-loop.md").

When you configure your human loop, you must specify that your input data is
free of personally identifiable information (PII) using the
`FreeOfPersonallyIdentifiableInformation` content classifier in
`DataAttributes`. If you use Mechanical Turk and do not specify that your
input data is free of PII, your human review tasks will fail.

Use the `FreeOfAdultContent` flag to declare that your input data
is free of adult content. SageMaker AI may restrict the Mechanical Turk workers that can view your
task if it contains adult content.

You can see examples of how to use this API in the following notebooks, found on
GitHub: [Amazon A2I Jupyter Notebook Examples](https://github.com/aws-samples/amazon-a2i-sample-jupyter-notebooks "https://github.com/aws-samples/amazon-a2i-sample-jupyter-notebooks").

## When is Mechanical Turk Not Supported?

This workforce is not supported under the following scenarios. In each scenario, you
must use a [private](sms-workforce-private.md "sms-workforce-private.md") or
[vendor](sms-workforce-management-vendor.md "sms-workforce-management-vendor.md") workforce.

- This workforce is not supported for Ground Truth video frame labeling jobs and 3D
  point cloud labeling jobs.
- You cannot use this workforce if your input data contains personally
  identifiable information (PII).
- Mechanical Turk is not available in some of the AWS special regions. If applicable, refer
  to the documentation for your special region for more information.
