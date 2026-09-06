

# SageMaker Edge Manager end of life
<a name="edge-eol"></a>

 Starting in April 26, 2024, you can no longer access Amazon SageMaker Edge Manager through the AWS management console, make edge packaging jobs, and manage edge device fleets. 

## FAQs
<a name="edge-eol-faqs"></a>

 Use the following sections to get answers to commonly asked questions about the SageMaker Edge Manager end of life (EOL). 

### Q: What happens to my Amazon SageMaker Edge Manager after the EOL date?
<a name="edge-eol-faqs-1"></a>

 A: After April 26, 2024, all references to edge packaging jobs, devices, and device fleets are deleted from the Edge Manager service. You can no longer discover or access the Edge Manager service from your AWS console and applications that call on the Edge Manager service APIs no longer work. 

### Q: Will I be billed for Edge Manager resources remaining in my account after the EOL date?
<a name="edge-eol-faqs-2"></a>

 A: Resources created by Edge Manager, such as edge packages inside Amazon S3 buckets, AWS IoT things, and AWS IAM roles, continue to exist on their respective services after April 26, 2024. To avoid being billed after Edge Manager is no longer supported, delete your resources. For more information on deleting your resources, see [Delete Edge Manager resources](#edge-eol-delete-resources). 

### Q: How do I delete my Amazon SageMaker Edge Manager resources?
<a name="edge-eol-faqs-3"></a>

 A: Resources created by Edge Manager, such as edge packages inside Amazon S3 buckets, AWS IoT things, and AWS IAM roles, continue to exist on their respective services after April 26, 2024. To avoid being billed after Edge Manager is no longer supported, delete your resources. For more information on deleting your resources, see [Delete Edge Manager resources](#edge-eol-delete-resources). 

### Q: How can I continue deploying models on the edge?
<a name="edge-eol-faqs-4"></a>

 A: We suggest you try one the following machine learning tools. For a cross-platform edge runtime, use [ONNX](https://onnxruntime.ai/). ONNX is a popular, well-maintained open-source solution that translates your models into instructions that many types of hardware can run, and is compatible with the latest ML frameworks. ONNX can be integrated into your SageMaker AI workflows as an automated step for your edge deployments. 

 For edge deployments and monitoring use AWS IoT Greengrass V2. AWS IoT Greengrass V2 has an extensible packaging and deployment mechanism that can fit models and applications at the edge. You can use the built-in MQTT channels to send model telemetry back for Amazon SageMaker Model Monitor or use the built-in permissions system to send data captured from the model back to Amazon Simple Storage Service (Amazon S3). If you don't or can't use AWS IoT Greengrass V2, we suggest using MQTT and IoT Jobs (C/C\+\+ library) to create a lightweight OTA mechanism to deliver models. 

 We have prepared [sample code available at this GitHub repository](https://github.com/aws-samples/ml-edge-getting-started) to help you transition to these suggested tools. 

## Delete Edge Manager resources
<a name="edge-eol-delete-resources"></a>

 Resources created by Edge Manager continue to exist after April 26, 2024. To avoid billing, delete these resources. 

 To delete AWS IoT Greengrass resources, do the following: 

1.  In the AWS IoT Core console, choose **Greengrass devices** under **Manage**. 

1.  Choose **Components**. 

1.  Under **My components**, Edge Manager created components are in the format * SageMaker AIEdge (EdgePackagingJobName)*. Select the component you want to delete. 

1.  Then choose **Delete version**. 

 To delete a AWS IoT role alias, do the following: 

1.  In the AWS IoT Core console, choose **Security** under **Manage**. 

1.  Choose **Role aliases**. 

1.  Edge Manager created role aliases are in the format *SageMaker AIEdge-{DeviceFleetName}*. Select the role you want to delete. 

1.  Choose **Delete**. 

 To delete packaging jobs in Amazon S3 buckets, do the following: 

1.  In the SageMaker AI console, choose **Edge Inference**. 

1.  Choose **Edge packaging jobs**. 

1.  Select one of the edge packaging jobs. Copy the Amazon S3 URI under **Model artifact** in the **Output configuration** section. 

1.  In the Amazon S3 console, navigate to the corresponding location, and check if you need to delete the model artifact. To delete the model artifact, select the Amazon S3 object and choose **Delete**. 