

# Custom labeling workflows
<a name="sms-custom-templates"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

These topics help you set up a Ground Truth labeling job that uses a custom labeling template. A custom labeling template allows you to create a custom worker portal UI that workers will use to label data. Template can be created using HTML, CSS, JavaScript, [Liquid template language](https://shopify.github.io/liquid/), and [Crowd HTML Elements](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html).

## Overview
<a name="sms-custom-templates-overview"></a>

If this is your first time creating a custom labeling workflow in Ground Truth, the following list is a high-level summary of the steps required.

1. *Set up your workforce* – To create a custom labeling workflow you need a workforce. This topic teaches you about configuring a workforce.

1. *Creating a custom template* – To create a custom template you must map the data from your input manifest file correctly to the variables in your template.

1. *Using optional processing Lambda functions* – To control how data from your input manifest is added to your worker template, and how worker annotations are logged in your job's output file.

This topic also has three end-to-end demos to help you better understand how to use custom labeling templates.

**Note**  
The examples in the links below all include pre-annotation and post-annotation Lambda functions. These Lambda functions are optional.
+ [Demo template: Annotation of images with `crowd-bounding-box`](sms-custom-templates-step2-demo1.md)
+ [Demo Template: Labeling Intents with `crowd-classifier`](sms-custom-templates-step2-demo2.md)
+ [Build a custom data labeling workflow with Amazon SageMaker Ground Truth](https://aws.amazon.com/blogs/machine-learning/build-a-custom-data-labeling-workflow-with-amazon-sagemaker-ground-truth/)

**Topics**
+ [Overview](#sms-custom-templates-overview)
+ [Set up your workforce](sms-custom-templates-step1.md)
+ [Creating a custom worker task template](sms-custom-templates-step2.md)
+ [Adding automation with Liquid](sms-custom-templates-step2-automate.md)
+ [Processing data in a custom labeling workflow with AWS Lambda](sms-custom-templates-step3.md)
+ [Demo template: Annotation of images with `crowd-bounding-box`](sms-custom-templates-step2-demo1.md)
+ [Demo Template: Labeling Intents with `crowd-classifier`](sms-custom-templates-step2-demo2.md)
+ [Create a custom workflow using the API](sms-custom-templates-step4.md)