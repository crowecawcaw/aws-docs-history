

# Create `aws_managedservices_onboarding_role` with CloudFormation for Accelerate
<a name="acc-onb-create-roles-with-cf"></a>

You can create the AWS Identity and Access Management role, `aws_managedservices_onboarding_role`, with CloudFormation from the AWS Management Console. Or, you can use commands from AWS CloudShell to deploy the role. 

## Use the AWS Management Console
<a name="create-role-cf-console"></a>

**Note**  
Before starting, have a JSON or YAML file for each role ready to upload. For more information, see [The template to create AMS roles](acc-onb-roles.md).

To create the role from the AWS Management Console, complete the following steps:

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

    ![CloudFormation console showing the Stacks page with options to create a new stack.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/image1.png)

1. Choose **Create Stack > With new resources (standard)**. You see the following page. 

   ![CloudFormation Stacks console showing empty state with Create stack and View getting started guide buttons.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/image2.png)

1. Choose **Upload a template file**, upload the JSON or YAML file of the IAM role, and then choose **Next**. You see the following page.

   ![Specify template step showing options to upload a template file or use Amazon S3 URL.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/image3.png)

1. Enter the stack name "**ams-onboarding-role**" in the **Stack Name** field. Enter a **DateOfExpiry** using the format "YYYY-MM-DDT00:00:00Z" (30 days from the current date is recommended). Continue scrolling down and selecting next until you reach this page: 

   ![Specify stack details page with Stack name field and Parameters section showing LocalUserName.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/image4.png)

1. Make sure the check box is selected and then select **Create Stack**.

1. Make sure the stack was created successfully.

## Use commands from AWS CloudShell
<a name="create-role-cf-cli"></a>

To deploy the `aws_managedservices_onboarding_role` IAM role, run the following command in [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html):

------
#### [ AWS CLI ]

```
curl -s "https://docs.aws.amazon.com/en_us/managedservices/latest/accelerate-guide/samples/onboarding_role_minimal.zip" -o "onboarding_role_minimal.zip"
unzip -q -o onboarding_role_minimal.zip
aws cloudformation create-stack \
    --stack-name "aws-managedservices-onboarding-role" \
    --capabilities CAPABILITY_NAMED_IAM \
    --template-body file://onboarding_role_minimal.json \
    --parameters ParameterKey=DateOfExpiry,ParameterValue="`date -d '+30 days' -u '+%Y-%m-%dT%H:%M:%SZ'`"
```

------
#### [ AWS Tools for PowerShell ]

```
Invoke-WebRequest -Uri 'https://docs.aws.amazon.com/en_us/managedservices/latest/accelerate-guide/samples/onboarding_role_minimal.zip' -OutFile 'onboarding_role_minimal.zip'
Expand-Archive -Path 'onboarding_role_minimal.zip' -DestinationPath . -Force
New-CFNStack `
    -StackName 'aws-managedservices-onboarding-role' `
    -Capability CAPABILITY_NAMED_IAM `
    -TemplateBody (Get-Content 'onboarding_role_minimal.json' -Raw) `
    -Parameter @{ParameterKey = "DateOfExpiry"; ParameterValue = (Get-Date).AddDays(30).ToString('yyyy-MM-ddTHH:mm:ssZ')}
```

------

After you create the role, work with your Cloud Architect (CA) to complete the [Step 2. Onboarding management resources in Accelerate](acc-get-mgmt-resource-onboard.md) process. After AMS informs you that your account is active, you're ready to onboard your instances.