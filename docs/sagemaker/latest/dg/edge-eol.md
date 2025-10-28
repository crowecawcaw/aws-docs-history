# SageMaker Edge Manager end of life

Starting in April 26, 2024, you can no longer access Amazon SageMaker Edge Manager through the AWS management console,
make edge packaging jobs, and manage edge device fleets.

## FAQs

Use the following sections to get answers to commonly asked questions about the SageMaker Edge Manager end of life (EOL).

A: After April 26, 2024, all references to edge packaging jobs, devices, and device fleets are deleted
from the Edge Manager service. You can no longer discover or access the Edge Manager service from your
AWS console and applications that call on the Edge Manager service APIs no longer work.

A: Resources created by Edge Manager, such as edge packages inside Amazon S3 buckets, AWS IoT things,
and AWS IAM roles, continue to exist on their respective services after April 26, 2024. To avoid
being billed after Edge Manager is no longer supported, delete your resources. For more information
on deleting your resources, see [Delete Edge Manager resources](#edge-eol-delete-resources "#edge-eol-delete-resources").

A: Resources created by Edge Manager, such as edge packages inside Amazon S3 buckets, AWS IoT things,
and AWS IAM roles, continue to exist on their respective services after April 26, 2024. To avoid
being billed after Edge Manager is no longer supported, delete your resources. For more information
on deleting your resources, see [Delete Edge Manager resources](#edge-eol-delete-resources "#edge-eol-delete-resources").

A: We suggest you try one the following machine learning tools.

For a cross-platform edge runtime, use [ONNX](https://onnxruntime.ai/ "https://onnxruntime.ai/"). ONNX is a
popular, well-maintained open-source solution that translates your models into instructions that
many types of hardware can run, and is compatible with the latest ML frameworks. ONNX can be
integrated into your SageMaker AI workflows as an automated step for your edge deployments.

For edge deployments and monitoring use AWS IoT Greengrass V2. AWS IoT Greengrass V2 has an extensible packaging and deployment
mechanism that can fit models and applications at the edge. You can use the built-in MQTT channels
to send model telemetry back for Amazon SageMaker Model Monitor or use the built-in permissions system to send data captured
from the model back to Amazon Simple Storage Service (Amazon S3). If you don't or can't use AWS IoT Greengrass V2, we suggest
using MQTT and IoT Jobs (C/C++ library) to create a lightweight OTA mechanism to deliver models.

We have prepared [sample code
available at this GitHub repository](https://github.com/aws-samples/ml-edge-getting-started "https://github.com/aws-samples/ml-edge-getting-started") to help you transition to these suggested tools.

## Delete Edge Manager resources

Resources created by Edge Manager continue to exist after April 26, 2024. To avoid billing, delete these
resources.

To delete AWS IoT Greengrass resources, do the following:

1. In the AWS IoT Core console, choose **Greengrass devices** under
   **Manage**.
2. Choose **Components**.
3. Under **My components**, Edge Manager created components are in the format
   _SageMaker AIEdge (EdgePackagingJobName)_. Select the component
   you want to delete.
4. Then choose **Delete version**.

To delete a AWS IoT role alias, do the following:

1. In the AWS IoT Core console, choose **Security** under
   **Manage**.
2. Choose **Role aliases**.
3. Edge Manager created role aliases are in the format _SageMaker AIEdge-{DeviceFleetName}_. Select the role you want to delete.
4. Choose **Delete**.

To delete packaging jobs in Amazon S3 buckets, do the following:

1. In the SageMaker AI console, choose **Edge Inference**.
2. Choose **Edge packaging jobs**.
3. Select one of the edge packaging jobs. Copy the Amazon S3 URI under **Model
   artifact** in the **Output configuration** section.
4. In the Amazon S3 console, navigate to the corresponding location, and check if you need to delete the
   model artifact. To delete the model artifact, select the Amazon S3 object and choose
   **Delete**.
