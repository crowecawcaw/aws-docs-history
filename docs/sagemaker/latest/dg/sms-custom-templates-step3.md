# Processing data in a custom labeling workflow with AWS Lambda

In this topic, you can learn how to deploy optional [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") functions when creating a custom labeling workflow. You can specify two types of Lambda functions to use with your custom labeling workflow.

- _Pre-annotation Lambda_: This function pre-processes each data object sent to your labeling job prior to sending it to workers.
- _Post-annotation Lambda_: This function processes the results once workers submit a task. If you specify multiple workers per data object, this function may include logic to consolidate annotations.
  If you are a new user of Lambda and Ground Truth, we recommend that you use the pages in this
  section as follows:

1. First, review [Using pre-annotation and post-annotation Lambda functions](sms-custom-templates-step3-lambda-requirements.md "sms-custom-templates-step3-lambda-requirements.md").
2. Then, use the page [Add required permissions to use
   AWS Lambda with Ground Truth](sms-custom-templates-step3-lambda-permissions.md "sms-custom-templates-step3-lambda-permissions.md") to learn
   about security and permission requirements to use your pre-annotation and
   post-annotation Lambda functions in a Ground Truth custom labeling job.
3. Next, you need to visit the Lambda console or use Lambda's APIs to create your
   functions. Use the section [Create Lambda functions using Ground Truth
   templates](sms-custom-templates-step3-lambda-create.md "sms-custom-templates-step3-lambda-create.md") to learn how to
   create Lambda functions.
4. To learn how to test your Lambda functions, see [Test pre-annotation and post-annotation
   Lambda functions](sms-custom-templates-step3-lambda-test.md "sms-custom-templates-step3-lambda-test.md").
5. After you create pre-processing and post-processing Lambda functions, select
   them from the **Lambda functions** section that comes after the
   code editor for your custom HTML in the Ground Truth console. To learn how to use these
   functions in a `CreateLabelingJob` API request, see [Create a Labeling Job (API)](sms-create-labeling-job-api.md "sms-create-labeling-job-api.md").
   For a custom labeling workflow tutorial that includes example pre-annotation and post-annotation Lambda functions, see [Demo template: Annotation of images with crowd-bounding-box](sms-custom-templates-step2-demo1.md "sms-custom-templates-step2-demo1.md").

###### Topics

- [Using pre-annotation and post-annotation Lambda functions](sms-custom-templates-step3-lambda-requirements.md "sms-custom-templates-step3-lambda-requirements.md")
- [Add required permissions to use
  AWS Lambda with Ground Truth](sms-custom-templates-step3-lambda-permissions.md "sms-custom-templates-step3-lambda-permissions.md")
- [Create Lambda functions using Ground Truth
  templates](sms-custom-templates-step3-lambda-create.md "sms-custom-templates-step3-lambda-create.md")
- [Test pre-annotation and post-annotation
  Lambda functions](sms-custom-templates-step3-lambda-test.md "sms-custom-templates-step3-lambda-test.md")
