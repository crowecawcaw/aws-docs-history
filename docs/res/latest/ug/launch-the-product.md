

# Step 1: Launch the product
<a name="launch-the-product"></a>

Follow the step-by-step instructions in this section to configure and deploy the product into your account.

**Time to deploy:** Approximately 60 minutes 

You can [ download the CloudFormation template](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/latest/ResearchAndEngineeringStudio.template.json) for this product before deploying it. 

If you are deploying in AWS GovCloud (US-West), use this [ template](https://research-engineering-studio-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/releases/latest/ResearchAndEngineeringStudio.template.json).

**res-stack** - Use this template to launch the product and all associated components. The default configuration deploys the RES main stack and authentication, frontend, and backend resources. 

**Note**  
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) (AWS CDK) constructs. 

The AWS CloudFormation template deploys Research and Engineering Studio on AWS in the AWS Cloud. You must meet the [prerequisites](prerequisites.md) before launching the stack. 

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Launch the [ template ](https://console.aws.amazon.com/cloudformation/home#/stacks/quickcreate?templateURL=https%3A%2F%2Fresearch-engineering-studio-us-east-1.s3.amazonaws.com%2Freleases%2Flatest%2FResearchAndEngineeringStudio.template.json).

   To deploy in AWS GovCloud (US-West), launch this [ template](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/quickcreate?templateURL=https://research-engineering-studio-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/releases/latest/ResearchAndEngineeringStudio.template.json).

1. The template launches in the US East (N. Virginia) Region by default. To launch the product in a different AWS Region, use the Region selector in the console navigation bar.
**Note**  
This product uses the Amazon Cognito service, which is not currently available in all AWS Regions. You must launch this product in an AWS Region where Amazon Cognito is available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). 

1. Under **Parameters**, review the parameters for this product template and modify them as necessary. If you deployed the automated external resources, you can find these parameters in the **Outputs** tab of the external resources stack.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/res/latest/ug/launch-the-product.html)

1. Under **Configure stack options → Tags - *optional***, add the tags (key-value pairs) you want to apply to RES deployed resources. Tag key `Name` and `res:*` are preserved by RES and cannot be used as tag keys.

1. Choose **Create stack** to deploy the stack. 

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You receive a CREATE\_COMPLETE status in approximately 60 minutes. 

**Important**  
You are responsible for patching your infrastructure/VDI hosts after deployment.