

# Set up Amazon Q Developer for your users
<a name="studio-updated-amazon-q-admin-guide-set-up"></a>

Amazon Q Developer is a generative AI conversational assistant. You can set up Amazon Q Developer within a new domain or an existing domain. Use the following information to set up Amazon Q Developer.

With Amazon Q Developer, your users can:
+ Receive step-by-step guidance on using SageMaker AI features independently or in combination with other AWS services.
+ Get sample code to get started on your ML tasks such as data preparation, training, inference, and MLOps.
+ Receive troubleshooting assistance to debug and resolve errors encountered while running code.

**Note**  
Amazon Q Developer in Studio doesn't use user content to improve the service, regardless of whether you use the Free-tier or Pro-tier subscription. For IDE-level telemetry sharing, Amazon Q might track your users' usage, such as the number of questions asked and whether recommendations were accepted or rejected. This telemetry data doesn't include personally identifiable information such as the users' IP address. For more information on data protection and instructions for opting out, see [Opt out of data sharing in the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/opt-out-IDE.html).

You can set up Amazon Q Developer with either a Pro or Free tier subscription. The Pro tier is a paid subscription service with higher usage limits and other features. For more information about the differences between the tiers, see [Understanding tiers of service for Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-tiers.html).

For information about subscribing to Amazon Q Developer Pro, see [Subscribing to Amazon Q Developer Pro](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.html).

## Set up instructions for Amazon Q Developer Free Tier:
<a name="studio-updated-amazon-q-developer-free-tier-set-up"></a>

To set up Amazon Q Developer Free Tier, use the following procedure:

**To set up Amazon Q Developer Free Tier**

1. Add the following policy to the IAM role that you've used to create your JupyterLab or Code Editor space:

------
#### [ JSON ]

****  

   ```
   {
   	"Version":"2012-10-17",		 	 	 
   	"Statement": [
   		{
   			"Effect": "Allow",
   			"Action": [
   				"q:SendMessage"
   			],
   			"Resource": [
   				"*"
   			]
   		},
   		{
   			"Sid": "AmazonQDeveloperPermissions",
   			"Effect": "Allow",
   			"Action": [
   				"codewhisperer:GenerateRecommendations"
   			],
   			"Resource": "*"
   		}
   	]
   }
   ```

------

1. Navigate to Amazon SageMaker Studio.

1. Open your JupyterLab or Code Editor space.

1. Navigate to the **Launcher** and choose **Terminal**.

1. In JupyterLab, do the following:

   1. Specify `restart-jupyter-server`.

   1. Restart your browser and navigate back to Amazon SageMaker Studio.

## Set up instructions for Amazon Q Developer Pro tier:
<a name="studio-updated-amazon-q-developer-pro-set-up"></a>

**Prerequisites**  
To set up Amazon Q Pro, you must have:  
An Amazon SageMaker AI domain set up for your organization with IAM Identity Center configured as the means of access.
An Amazon Q Developer Pro subscription.

If you're updating a domain that you've already set up for your organization, you need to update it to use Amazon Q Developer. You can use either the AWS Management Console or the AWS Command Line Interface to update a domain.

You must use the ARN of your Amazon Q Developer profile. You can find the Q Profile ARN on the [Q Developer Settings](https://console.aws.amazon.com/amazonq/developer/settings) page.

You can use the following AWS Command Line Interface command to update your domain:

```
aws --region {{AWS Region}} sagemaker update-domain --domain-id {{domain-id}} --domain-settings-for-update "AmazonQSettings={Status=ENABLED,QProfileArn={{Q-Profile-ARN}}}"           
```

You can also use the following procedure to update the domain within the AWS Management Console.

1. Navigate to the [Amazon SageMaker AI](https://console.aws.amazon.com/sagemaker) console.

1. Choose domains.

1. Select **App Configurations**.

1. For **Amazon Q Developer for SageMaker AI Applications**, choose **Edit**.

1. Select **Enable Amazon Q Developer on this domain**.

1. Provide the Q Profile ARN.

1. Choose **Submit**.

You must use the ARN of your Amazon Q Developer profile. You can find the ARN of the Q Profile on the **Amazon Q account details** page of the [Amazon Q Developer](https://console.aws.amazon.com/amazonq/developer) console.

The **Set up for organizations** is an advanced setup for the Amazon SageMaker AI domain that lets you use IAM Identity Center. For information about how you can set up the domain and information about setting up IAM Identity Center, see [Use custom setup for Amazon SageMaker AI](onboard-custom.md).

When setting up Amazon Q Developer in a new domain, you can either use the AWS Management Console or the following AWS Command Line Interface command from your local machine:

```
                    
aws --region {{AWS Region}} sagemaker create-domain --domain-id {{domain-id}} --domain-name {{"example-domain-name"}} --vpc-id {{example-vpc-id}} --subnet-ids {{example-subnet-ids}} --auth-mode SSO --default-user-settings "ExecutionRole=arn:aws:iam::{{111122223333}}:role/{{IAM-role}}",--domain-settings "AmazonQSettings={status=ENABLED,qProfileArn={{Q-profile-ARN}}" --query {{example-domain-ARN}}--output text
```

You can use the following AWS CLI command to disable Amazon Q Developer:

```
aws --region {{AWS Region}} sagemaker update-domain --domain-id {{domain-id}} --domain-settings-for-update "AmazonQSettings={Status=DISABLED,QProfileArn={{Q-Profile-ARN}}}"           
```

We recommend using the latest version of the AWS Command Line Interface. For information about updating the AWS CLI, see [Install or update to the latest version of the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

If you need to establish a connection between Amazon Q Developer and your VPC, see [Creating an interface VPC endpoint for Amazon Q ](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/vpc-interface-endpoints.html#vpc-endpoint-create).

**Note**  
Amazon Q Developer has the following limitations:  
It doesn't support shared spaces.
Amazon Q Developer detects whether a code suggestion might be too similar to publicly available code. The reference tracker can flag suggestions with repository URLs and licenses, or filter them out. This allows you to review the referenced code and its usage before you adopt it. All references are logged for you to review later to ensure that your code flow is not disturbed and that you can keep coding without interruption.  
For more information about code references, see [Using code references - Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-reference.html) and [AI Coding Assistant - Amazon Q Developer FAQs](https://aws.amazon.com/q/developer/faqs/?refid=255ccf7b-4a76-4dcb-9b07-68709e2b636b#:~:text=Can%20I%20prevent%20Amazon%20Q%20Developer%20from%20recommending%20code%20with%20code%20references%3F).
Amazon Q processes all user interaction data within the US East (N. Virginia) AWS Region. For more information about how Amazon Q processes data and the AWS Regions it supports, see [Supported Regions for Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/regions.html).
Amazon Q only works within Amazon SageMaker Studio. It is not supported within Amazon SageMaker Studio Classic.
On JupyterLab, Amazon Q works within SageMaker AI Distribution Images version 2.0 and above. On Code Editor, Amazon Q works within SageMaker AI Distribution Images version 2.2.1 and above.
Amazon Q Developer in JupyterLab works within the Jupyter AI extension. You can't use other 3P models within the extension while you're using Amazon Q.

## Amazon Q customizations in Amazon SageMaker AI
<a name="q-customizations-in-sagemaker"></a>

If you use Amazon Q Developer Pro, you have the option to create *customizations*. With customizations, Amazon Q Developer provides suggestions based on your company's codebase. If you create customizations in Amazon Q Developer, they become available for you to use in JupyterLab and Code Editor in Amazon SageMaker Studio. For more information about setting up customizations, see [Customizing suggestions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/customizations.html) in the *Amazon Q Developer User Guide*.