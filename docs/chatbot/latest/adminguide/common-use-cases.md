AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Using CLI commands with Amazon Q Developer in chat applications - Common

use
cases

Common use cases for using Amazon Q Developer in chat applications in your chat channels involve running CLI commands.
This topic also includes an example use case for invoking a Lambda
function in your chat channel, written in Python 3.8.

For more information about running CLI commands in chat channels see [Running AWS CLI commands from chat channels using Amazon Q Developer in chat applications](chatbot-cli-commands.md "chatbot-cli-commands.md").

For a tutorial that walks you
through how to invoke Lambda functions from Amazon Q Developer in chat applications, see the [Tutorial: Using Amazon Q Developer in chat applications to run
an AWS Lambda function remotely](chatbot-run-lambda-function-remotely-tutorial.md "chatbot-run-lambda-function-remotely-tutorial.md").

###### Topics

- [Restart an Amazon EC2 instance](#reboot-instances "#reboot-instances")
- [Change Auto Scaling limits](#change-autoscale "#change-autoscale")
- [Run an Automation runbook](#run-book "#run-book")
- [Use a Lambda function to approve an
  AWS CodePipeline
  action](#create-pipeline "#create-pipeline")

## Restart an Amazon EC2 instance

The following example shows how CLI commands can be used to restart your specified Amazon EC2 instance from your chat channel.
The parameters you include here are your instance id, min, and max size.
For more information about restarting Amazon EC2 instances, see the [reboot-instances](../../../cli/latest/reference/ec2/reboot-instances.md#reboot-instances "../../../cli/latest/reference/ec2/reboot-instances.md#reboot-instances") command in the _AWS CLI Command Reference_.

`@Amazon Q ec2 reboot-instances --instance-ids i-1234567890abcdef5`

## Change Auto Scaling limits

The following example shows how CLI commands can be used to change your Auto Scaling limits directly from your chat channel.
The parameters you include are the name of your Auto Scaling group and the minimum and maximum sizes.
For more information about changing autoscaling limits, see [update-autoscaling-group](../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md "../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md") command in the _AWS CLI Command Reference_.

`@Amazon Q autoscaling update-auto-scaling-group 
 --auto-scaling-group-name my-asg 
 --min-size 2 
 --max-size 10`

## Run an Automation runbook

The following example shows how CLI commands can be used to run an Automation runbook. In this command you specify your document name and your parameters.
For more information, see the [start-automation-execution](../../../cli/latest/reference/ssm/start-automation-execution.md "../../../cli/latest/reference/ssm/start-automation-execution.md") command in the _AWS CLI Command Reference_.

`@Amazon Q ssm start-automation-execution 
 --document-name "AWS-UpdateLinuxAmi" 
 --parameters "AutomationAssumeRole=arn:aws:iam::123456789012:role/SSMAutomationRole,SourceAmiId=ami-EXAMPLE,IamInstanceProfileName=EC2InstanceRole"`

## Use a Lambda function to approve an

AWS CodePipeline
action

The code example in this section demonstrates how you can use a Lambda function to
perform activities, spefically how you can manually approve a pipeline action. This function
enables
you to approve or reject a pipeline action from your chat channel by entering the status and a
summary. The function gets the required token using the get_pipeline_status method. It
then uses the token value when applying the approval decision by using the
put_approval_result method. For more information about these methods, see the [CodePipeline section](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html") of the _Boto3 docs 1.14.10
documentation_. The Lambda code uses Python 3.8.

```
import boto3

def lambda_handler(event, context):
    client = boto3.client('codepipeline')

    getToken = client.get_pipeline_state(
        name = 'mypipeline1'
    )

    myToken=getToken['stageStates']['actionStates']['latestExecution']['token']

    response = client.put_approval_result(
        pipelineName='mypipeline1',
        stageName='beta',
        actionName='Approval',
        result={
            'summary': ['summary'],
            'status': ['status']
        },
        token=myToken

    )

```

The following Amazon Q Developer in chat applications command invokes the Lambda function. For more information about
CodePipeline and pipeline actions, see the [_AWS CodePipeline User
Guide_](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md").

`@Amazon Q invoke mypipeline1-beta-Approval --payload {"summary": "the design looks good, ready to release",“status”: "Approved"}`
