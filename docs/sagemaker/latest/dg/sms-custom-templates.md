# Custom labeling workflows

These topics help you set up a Ground Truth labeling job that uses a custom labeling template. A
custom labeling template allows you to create a custom worker portal UI that workers will
use to label data. Template can be created using HTML, CSS, JavaScript, [Liquid template language](https://shopify.github.io/liquid/ "https://shopify.github.io/liquid/"), and [Crowd HTML
Elements](sms-ui-template-reference.md "sms-ui-template-reference.md").

## Overview

If this is your first time creating a custom labeling workflow in Ground Truth, the following list is a high-level summary of the steps required.

1. _Set up your workforce_ – To create a custom labeling workflow you need a workforce. This topic teaches you about configuring a workforce.
2. _Creating a custom template_ – To create a custom template you must map the data from your input manifest file correctly to the variables in your template.
3. _Using optional processing Lambda functions_ – To control how data from your input manifest is added to your worker template, and how worker annotations are logged in your job's output file.

This topic also has three end-to-end demos to help you better understand how to use custom labeling templates.

###### Note

The examples in the links below all include pre-annotation and post-annotation Lambda functions. These Lambda functions are optional.

- [Demo template: Annotation of images with crowd-bounding-box](sms-custom-templates-step2-demo1.md "sms-custom-templates-step2-demo1.md")
- [Demo Template: Labeling Intents with crowd-classifier](sms-custom-templates-step2-demo2.md "sms-custom-templates-step2-demo2.md")
- [Build a custom data labeling workflow with Amazon SageMaker Ground Truth](https://aws.amazon.com/blogs/machine-learning/build-a-custom-data-labeling-workflow-with-amazon-sagemaker-ground-truth/ "https://aws.amazon.com/blogs/machine-learning/build-a-custom-data-labeling-workflow-with-amazon-sagemaker-ground-truth/")

###### Topics

- [Set up your workforce](sms-custom-templates-step1.md "sms-custom-templates-step1.md")
- [Creating a custom worker task template](sms-custom-templates-step2.md "sms-custom-templates-step2.md")
- [Adding automation with Liquid](sms-custom-templates-step2-automate.md "sms-custom-templates-step2-automate.md")
- [Processing data in a custom labeling workflow with AWS Lambda](sms-custom-templates-step3.md "sms-custom-templates-step3.md")
- [Demo template: Annotation of images with crowd-bounding-box](sms-custom-templates-step2-demo1.md "sms-custom-templates-step2-demo1.md")
- [Demo Template: Labeling Intents with crowd-classifier](sms-custom-templates-step2-demo2.md "sms-custom-templates-step2-demo2.md")
- [Create a custom workflow using the
  API](sms-custom-templates-step4.md "sms-custom-templates-step4.md")
