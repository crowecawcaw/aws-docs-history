

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# Automating with CloudFormation
<a name="tutorial-cloudformation"></a>

In this tutorial, you use an AWS CloudFormation automation stack to launch an Amazon Forecast pipeline and generate forecasts using a demonstration dataset.

The AWS Forecast CloudFormation stack: 
+ Deploys the [Improving Forecast Accuracy with Machine Learning Solution](https://docs.aws.amazon.com/solutions/latest/improving-forecast-accuracy-with-machine-learning/automated-deployment.html) CloudFormation template. 
+ Deploys the [NYC Taxi Datasets](https://registry.opendata.aws/nyc-tlc-trip-records-pds/) to the Forecast Data Amazon S3 bucket. 
+ Automatically starts the demo NYC taxi forecast pipeline in Forecast. 

The CloudFormation template is preloaded with target time-series, related time-series, and item metadata demonstration datasets. Relevant fields in the console are pre-filled with their respective S3 locations. 

After completing this tutorial using the demonstration datasets, you can use the same automation stack to generate forecasts with your own datasets. 

The following diagram shows the components used in this tutorial. 

![Architecture diagram showing data flow from preparation through ingestion, forecasting, and evaluation stages.](http://docs.aws.amazon.com/forecast/latest/dg/images/cloudformationautomation-architecture.png)


## Prerequisites
<a name="tutorial-cloudformation-prerequisites"></a>

Before starting the tutorial, make sure you have logged into your AWS account and installed the CloudFormation template: 

1. Log in to your AWS account. If you do not already have one, [create an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). 

1. Install the AWS CloudFormation template. Choose the Region closest to you: 
   +  Tokyo: [ap-northeast-1](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template)
   +  Seoul: [ap-northeast-2](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  Mumbai: [ap-south-1](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  Singapore: [ap-southeast-1](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  Sydney: [ap-southeast-2](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  Frankfurt: [eu-cental-1](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  Ireland: [eu-west-1](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  N. Virginia: [us-east-1](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  Ohio: [us-east-2](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 
   +  Oregon: [us-west-2](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=forecast-stack&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fimproving-forecast-accuracy-with-machine-learning%2Flatest%2Fimproving-forecast-accuracy-with-machine-learning-demo.template) 

This deploys a demonstration stack using the [NYC Taxi Dataset](https://registry.opendata.aws/nyc-tlc-trip-records-pds/). 

## Deploying an CloudFormation Template for Forecast automation
<a name="tutorial-clouformation-steps"></a>

To deploy the CloudFormation template using the NYC Taxi Dataset

**Step 1**: Accept the defaults and choose **Next**.

![Create stack wizard showing template preparation options and Amazon S3 URL field.](http://docs.aws.amazon.com/forecast/latest/dg/images/cloudformationautomation-step1.png)


**Step 2**: Provide an email address for notifications and choose **Next**.

![Datasets Configuration page showing email field with youremail@sample.com entered.](http://docs.aws.amazon.com/forecast/latest/dg/images/cloudformationautomation-step2.png)


**Step 3**: Accept defaults and choose **Next**.

**Step 4**: For Capabilities, select both check boxes to allow CloudFormation to create AWS Identity and Access Management (IAM) resources and nested stacks. Choose **Create stack**.

![Capabilities section with two checkboxes selected for IAM resources and CAPABILITY_AUTO_EXPAND.](http://docs.aws.amazon.com/forecast/latest/dg/images/cloudformationautomation-step4.png)


You have deployed an CloudFormation template in Forecast.

## Clean Up
<a name="tutorial-clouformation-cleanup"></a>

After deploying this CloudFormation template, you can clean up newly created resources, deploy the CloudFormation stack using your own datasets, and explore other deployment options.
+ **Cleaning up**: Deleting the demo stack retains the "Improving Forecast Accuracy with Machine Learning" stack. Deleting the "Improving Forecast Accuracy with Machine Learning" stack retains all S3, Athena, QuickSight, and Forecast data.
+ **Using your own datasets**: To deploy this CloudFormation template with your own time-series data, enter the S3 locations of your datasets in the Datasets Configuration section in **Step 2**.
+ **Other deployment options**: For more deployment options, see [Automated Deployment](https://docs.aws.amazon.com/solutions/latest/improving-forecast-accuracy-with-machine-learning/automated-deployment.html). If data is already available, you can deploy the stack without the demo data.