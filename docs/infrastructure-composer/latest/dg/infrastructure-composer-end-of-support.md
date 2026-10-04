

# AWS Infrastructure Composer end of support
<a name="infrastructure-composer-end-of-support"></a>

After careful consideration, we decided to end support for AWS Infrastructure Composer, effective December 7, 2026. Infrastructure Composer will no longer accept new customers beginning October 29, 2026. As an existing customer with an account signed up for the service before October 29, 2026, you can continue to use Infrastructure Composer features. After December 7, 2026, you will no longer be able to use Infrastructure Composer.

## What continues before the console is shut down
<a name="infrastructure-composer-end-of-support-continues"></a>
+ If you are an existing customer, you can continue using the standalone console until December 7, 2026.
+ The AWS Toolkit for Visual Studio Code retains the full Infrastructure Composer visual authoring experience with no changes.

## What is not affected
<a name="infrastructure-composer-end-of-support-not-affected"></a>
+ CloudFormation templates stored in Amazon S3 or on local file systems.
+ Existing CloudFormation stacks, deployments, and workflows continue to work normally.
+ The Infrastructure Composer visual authoring experience in the AWS Toolkit for Visual Studio Code.

## Recommended alternative
<a name="infrastructure-composer-end-of-support-alternative"></a>

We recommend the following alternative:

AWS Toolkit for Visual Studio Code  
The Infrastructure Composer visual authoring experience remains available locally in your IDE. Continue designing templates with the same drag-and-drop canvas and code editor.

## How to transition
<a name="infrastructure-composer-end-of-support-transition"></a>

1. Download and install the [AWS Toolkit for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode).

1. Open any CloudFormation or AWS SAM template in VS Code, and then choose the Infrastructure Composer button in the upper-right corner of the editor.

1. Alternatively, open the context (right-click) menu for a template file and choose **Open with Infrastructure Composer**, or use the Command Palette (Cmd\+Shift\+P / Ctrl\+Shift\+P) and search for **AWS Infrastructure Composer**.

**Note**  
The standalone Infrastructure Composer console will be shut down on December 7, 2026. Transition before this date.

If you have additional questions, contact [AWS Support](https://console.aws.amazon.com/support/).

## Frequently asked questions
<a name="infrastructure-composer-end-of-support-faq"></a>

What is happening to AWS Infrastructure Composer?  
The standalone AWS Infrastructure Composer console is ending support on December 7, 2026. You can continue using the same visual authoring experience through the Infrastructure Composer integration in the AWS Toolkit for Visual Studio Code.

Do I need to take any action?  
If you use Infrastructure Composer through the AWS Toolkit for Visual Studio Code, no action is required. The integration continues to work. If you use the standalone web console, you must transition to the AWS Toolkit for Visual Studio Code before December 7, 2026, when the standalone console will be shut down.

What happens to the standalone Infrastructure Composer URL?  
The standalone URL (`console.aws.amazon.com/composer`) will no longer be accessible after December 7, 2026. Transition to the AWS Toolkit for Visual Studio Code before that date.

When will Infrastructure Composer stop accepting new customers?  
New customer sign-ups will be blocked via allowlist 30 days after the public announcement (target: October 29, 2026). If you are an existing customer, you retain access during the transition period.

Is there a blog post about this change?  
No. Per AWS policy, blog posts are not used to communicate service availability changes. All official information is available on the documentation page and through AWS Health notifications.

How does this affect the AWS Toolkit IDE extension?  
The AWS Toolkit for Visual Studio Code retains the Infrastructure Composer visual authoring experience. No changes are planned for the Toolkit integration at this time.

Will I lose my saved projects or templates?  
No. You have two options: (1) save templates to your local machine, or (2) save them in an Amazon S3 bucket. Templates stored in Amazon S3 or on your local file system are not affected by this change.

Does Infrastructure Composer have any customer-facing APIs?  
No. Infrastructure Composer does not expose any customer-facing APIs, SDKs, CLI commands, or backend service endpoints. There are no API integrations to decommission.

What changes in the CloudFormation console?  
Infrastructure Composer was available in the CloudFormation console as a visual tool for composing and visualizing CloudFormation templates during stack creation and updates. This embedded experience is being replaced with an improved visual editor component integrated directly into the CloudFormation console. Your stacks and templates are not affected.

What changes in the Lambda console?  
The **Export to Infrastructure Composer** button in the Lambda console will be removed. Your Lambda functions and their configurations are not affected.

What changes in the Step Functions console?  
The **Export to Infrastructure Composer** option in the **Actions** dropdown on the state machine details page will be removed. All other Step Functions console functionality remains fully available.