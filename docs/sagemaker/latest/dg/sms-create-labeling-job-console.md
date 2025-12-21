# Create a Labeling Job (Console)

You can use the Amazon SageMaker AI console to create a labeling job for all of the Ground Truth built-in
task types and custom labeling workflows. For built-in task types, we recommend that you use
this page alongside the [page for your task type](sms-task-types.md "sms-task-types.md"). Each task
type page includes specific details on creating a labeling job using that task type.

You need to provide the following to create a labeling job in the SageMaker AI console:

- An input manifest file in Amazon S3. You can place your input dataset in Amazon S3 and
  automatically generate a manifest file using the Ground Truth console (not supported for 3D
  point cloud labeling jobs).

Alternatively, you can manually create an input manifest file. To learn how, see
[Input data](sms-data-input.md "sms-data-input.md").

- An Amazon S3 bucket to store your output data.
- An IAM role with permission to access your resources in Amazon S3 and with a SageMaker AI
  execution policy attached. For a general solution, you can attach the managed
  policy, AmazonSageMakerFullAccess, to an IAM role and include
  `sagemaker` in your bucket name.

For more granular policies, see [Assign IAM Permissions to Use Ground Truth](sms-security-permission.md "sms-security-permission.md").

3D point cloud task types have additional security considerations. [Learn more](sms-point-cloud-general-information.md#sms-security-permission-3d-point-cloud "sms-point-cloud-general-information.md#sms-security-permission-3d-point-cloud").

- A work team. You create a work team from a workforce made up of Amazon Mechanical Turk workers,
  vendors, or your own private workers.To lean more, see [Workforces](sms-workforce-management.md "sms-workforce-management.md").

You cannot use the Mechanical Turk workforce for 3D point cloud or video frame labeling jobs.

- If you are using a custom labeling workflow, you must save a worker task template
  in Amazon S3 and provide an Amazon S3 URI for that template. For more information, see
  [Creating a custom worker task template](sms-custom-templates-step2.md "sms-custom-templates-step2.md").
- (Optional) An AWS KMS key ARN if you want SageMaker AI to encrypt the output of your
  labeling job using your own AWS KMS encryption key instead of the default Amazon S3 service
  key.
- (Optional) Existing labels for the dataset you use for your labeling job. Use this
  option if you want workers to adjust, or approve and reject labels.
- If you want to create an adjustment or verification labeling job, you must have an
  output manifest file in Amazon S3 that contains the labels you want adjusted or verified.
  This option is only supported for bounding box and semantic segmentation image
  labeling jobs and 3D point cloud and video frame labeling jobs. It is recommended
  that you use the instructions on [Label verification and adjustment](sms-verification-data.md "sms-verification-data.md") to create a verification or adjustment
  labeling job.

###### Important

Your work team, input manifest file, output bucket, and other resources in Amazon S3 must
be in the same AWS Region you use to create your labeling job.

When you create a labeling job using the SageMaker AI console, you add worker instructions and
labels to the worker UI that Ground Truth provides. You can preview and interact with the worker UI
while creating your labeling job in the console. You can also see a preview of the worker UI
on your [built-in
task type page](sms-task-types.md "sms-task-types.md").

###### To create a labeling job (console)

1. Sign in to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose **Labeling jobs**.
3. On the **Labeling jobs** page, choose **Create labeling
   job**.
4. For **Job name**, enter a name for your labeling job.
5. (Optional) If you want to identify your labels with a key, select **I want
   to specify a label attribute name different from the labeling job
   name**. If you do not select this option, the labeling job name you
   specified in the previous step will be used to identify your labels in your output
   manifest file.
6. Choose a data setup to create a connection between your input dataset and Ground Truth.
   - For **Automated data setup**:
     - Follow the instructions in [Automate data setup for labeling jobs](sms-console-create-manifest-file.md "sms-console-create-manifest-file.md") for image,
       text, and video clip labeling jobs.
     - Follow the instructions in [Set up Automated Video Frame Input Data](sms-video-automated-data-setup.md "sms-video-automated-data-setup.md") for video frame
       labeling jobs.

   - For **Manual data setup**:
     - For **Input dataset location**, provide the
       location in Amazon S3 in which your input manifest file is located. For
       example, if your input manifest file, manifest.json, is located in
       **example-bucket**, enter
       **s3://example-bucket/manifest.json**.
     - For **Output dataset location**, provide the
       location in Amazon S3 where you want Ground Truth to store the output data from
       your labeling job.

7. For **IAM Role**, choose an existing IAM role or create an
   IAM role with permission to access your resources in Amazon S3, to write to the output
   Amazon S3 bucket specified above, and with a SageMaker AI execution policy attached.
8. (Optional) For **Additional configuration**, you can specify how
   much of your dataset you want workers to label, and if you want SageMaker AI to encrypt the
   output data for your labeling job using an AWS KMS encryption key. To encrypt your
   output data, you must have the required AWS KMS permissions attached to the IAM role
   you provided in the previous step. For more details, see [Assign IAM Permissions to Use Ground Truth](sms-security-permission.md "sms-security-permission.md").
9. In the **Task type** section, under **Task
   category**, use the dropdown list to select your task category.
10. In **Task selection**, choose your task type.
11. (Optional) Provide tags for your labeling job to make it easier to find in the
    console later.
12. Choose **Next**.
13. In the **Workers** section, choose the type of workforce you
    would like to use. For more details about your workforce options see [Workforces](sms-workforce-management.md "sms-workforce-management.md").
14. (Optional) After you've selected your workforce, specify the **Task
    timeout**. This is the maximum amount of time a worker has to work on a
    task.

For 3D point cloud annotation tasks, the default task timeout is 3 days. The
default timeout for text and image classification and label verification labeling
jobs is 5 minutes. The default timeout for all other labeling jobs is 60
minutes. 15. (Optional) For bounding box, semantic segmentation, video frame, and 3D point
cloud task types, you can select **Display existing labels** if
you want to display labels for your input data set for workers to verify or
adjust.

For bounding box and semantic segmentation labeling jobs, this will create an
adjustment labeling job.

For 3D point cloud and video frame labeling jobs:

    * Select **Adjustment** to create an adjustment
     labeling job. When you select this option, you can add new labels but
     you cannot remove or edit existing labels from the previous job.
     Optionally, you can choose label category attributes and frame
     attributes that you want workers to edit. To make an attribute editable,
     select the check box **Allow workers to edit this
     attribute** for that attribute.


    Optionally, you can add new label category and frame attributes.
    * Select **Verification** to create an adjustment
     labeling job. When you select this option, you cannot add, modify, or
     remove existing labels from the previous job. Optionally, you can choose
     label category attributes and frame attributes that you want workers to
     edit. To make an attribute editable, select the check box
     **Allow workers to edit this attribute** for that
     attribute.


    We recommend that you can add new label category attributes to the
     labels that you want workers to verify, or add one or more frame
     attributes to have workers provide information about the entire
     frame.

For more information, see [Label verification and adjustment](sms-verification-data.md "sms-verification-data.md"). 16. Configure your workers' UI:

    * If you are using a [built-in task
     type](sms-task-types.md "sms-task-types.md"), specify workers instructions and labels.




    	+ For image classification and text classification (single and
    	 multi-label) you must specify at least two label categories. For
    	 all other built-in task types, you must specify at least one
    	 label category.
    	+ (Optional) If you are creating a 3D point cloud or video frame
    	 labeling job, you can specify label category attributes (not
    	 supported for 3D point cloud semantic segmentation) and frame
    	 attributes. Label category attributes can be assigned to one or
    	 more labels. Frame attributes will appear on each point cloud or
    	 video frame workers label. To learn more, see [Worker user interface (UI)](sms-point-cloud-general-information.md#sms-point-cloud-worker-task-ui "sms-point-cloud-general-information.md#sms-point-cloud-worker-task-ui") for 3D
    	 point cloud and [Worker user interface (UI)](sms-video-overview.md#sms-video-worker-task-ui "sms-video-overview.md#sms-video-worker-task-ui") for video frame.
    	+ (Optional) Add **Additional instructions** to
    	 help your worker complete your task.
    * If you are creating a custom labeling workflow you must :




    	+ Enter a [custom template](sms-custom-templates-step2.md "sms-custom-templates-step2.md") in the code box. Custom templates
    	 can be created using a combination of HTML, the Liquid
    	 templating language and our pre-built web components.
    	 Optionally, you can choose a base-template from the drop-down
    	 menu to get started.
    	+ Specify pre-annotation and post-annotation lambda functions.
    	 To learn how to create these functions, see [Processing data in a custom labeling workflow with AWS Lambda](sms-custom-templates-step3.md "sms-custom-templates-step3.md").

17. (Optional) You can select **See preview** to preview your worker
    instructions, labels, and interact with the worker UI. Make sure the pop-up blocker
    of the browser is disabled before generating the preview.
18. Choose **Create**.
    After you've successfully created your labeling job, you are redirected to the
    **Labeling jobs** page. The status of the labeling job you just created
    is **In progress**. This status progressively updates as workers complete
    your tasks. When all tasks are successfully completed, the status changes to
    **Completed**.

If an issue occurs while creating the labeling job, its status changes to
**Failed**.

To view more details about the job, choose the labeling job name.

## Next Steps

After your labeling job status changes to **Completed**, you can view
your output data in the Amazon S3 bucket that you specified while creating that labeling job.
For details about the format of your output data, see [Labeling job output data](sms-data-output.md "sms-data-output.md").
