

# Accessing cross-account AWS resources in Step Functions
<a name="tutorial-access-cross-acct-resources"></a>

With the cross-account access support in Step Functions, you can share resources configured in different AWS accounts. In this tutorial, we walk you through the process of accessing a cross-account Lambda function defined in an account called **Production**. This function is invoked from a state machine in an account called **Development**. In this tutorial, the **Development** account is referred to as the *source account* and the **Production** account is the *target account* containing the target IAM role.

To start, in your `Task` state’s definition, you specify the target IAM role the state machine must assume before invoking the cross-account Lambda function. Then, modify the trust policy in the target IAM role to allow the source account to assume the target role temporarily. Also, to call the AWS resource, define the appropriate permissions in the target IAM role. Finally, update the source account’s execution role to specify the required permission to assume the target role.

You can configure your state machine to assume an IAM role for accessing resources from multiple AWS accounts. However, a state machine can assume only one IAM role at a given time based on the `Task` state’s definition.

**Note**  
Cross-Region AWS SDK integration and cross-Region AWS resource access aren't available in Step Functions.

## Prerequisites
<a name="tutorial-access-cross-acct-resources-prereq"></a>
+ This tutorial uses the example of a Lambda function for demonstrating how to set up cross-account access. You can use any other AWS resource, but make sure you’ve configured the resource in a different account.
**Important**  
IAM roles and resource-based policies delegate access across accounts only within a single partition. For example, assume that you have an account in US West (N. California) in the standard `aws` partition. You also have an account in China (Beijing) in the `aws-cn` partition. You can't use an Amazon S3 resource-based policy in your account in China (Beijing) to allow access for users in your standard `aws` account.
+ Make a note of the cross-account resource's Amazon Resource Name (ARN) in a text file. Later in this tutorial, you'll provide this ARN in your state machine's `Task` state definition. The following is an example of a Lambda function ARN:

  ```
  arn:aws:lambda:us-east-2:{{account-id}}:function:{{functionName}}
  ```
+ Make sure you've created the target IAM role that the state machine needs to assume.

## Step 1: Update the Task state definition to specify the target role
<a name="tutorial-access-cross-acct-resources-update-task-def"></a>

In the `Task` state of your workflow, add a `Credentials` field containing the identity the state machine must assume before invoking the cross-account Lambda function.

The following procedure demonstrates how to access a cross-account Lambda function called `Echo`. You can call any AWS resource by following these steps.

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/) and choose **Create state machine**.

1. On the **Choose authoring method** page, choose **Design your workflow visually** and keep all the default selections.

1. To open Workflow Studio, choose **Next**.

1. On the **Actions** tab, drag and drop a `Task` state on the canvas. This invokes the cross-account Lambda function that's using this `Task` state.

1. On the **Configuration** tab, do the following:

   1. Rename the state to **Cross-account call**.

   1. For **Function name**, choose **Enter function name**, and then enter the Lambda function ARN in the box. For example, `arn:aws:lambda:us-east-2:111122223333:function:{{Echo}}`.

   1. For **Provide IAM role ARN**, specify the target IAM role ARN. For example, `arn:aws:iam::111122223333:role/LambdaRole`.
**Tip**  
Alternatively, you can also specify a [reference path](amazon-states-language-paths.md#amazon-states-language-reference-paths) to an existing key-value pair in the state’s JSON input that contains the IAM role ARN. To do this, choose **Get IAM role ARN at runtime from state input**. For an example of specifying a value by using a reference path, see [Specifying JSONPath as IAM role ARN](state-task.md#example-credentials-specify-dynamic-jsonpath).

1. Choose **Next**.

1. On the **Review generated code** page, choose **Next**.

1. On the **Specify state machine settings** page, specify details for the new state machine, such as a name, permissions, and logging level.

1. Choose **Create state machine**.

1. Make a note of the state machine's IAM role ARN and the state machine ARN in a text file. You'll need to provide these ARNs in the target account's trust policy.

Your `Task` state definition should now look similar to the following definition.

```
{
  "StartAt": "Cross-account call",
  "States": {
    "Cross-account call": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Credentials": {
        "RoleArn": "arn:aws:iam::111122223333:role/LambdaRole"
      },
      "Parameters": {
        "FunctionName": "arn:aws:lambda:us-east-2:111122223333:function:{{Echo}}",
      },
      "End": true
    }
  }
}
```

## Step 2: Update the target role's trust policy
<a name="tutorial-access-cross-acct-resources-update-target-trust-policy"></a>

The IAM role must exist in the target account and you must modify its trust policy to allow the source account to assume this role temporarily. Additionally, you can control who can assume the target IAM role.

After you create the trust relationship, a user from the source account can use the AWS Security Token Service (AWS STS) [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) API operation. This operation provides temporary security credentials that enable access to AWS resources in a target account.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. On the navigation pane of the console, choose **Roles** and then use the Search box to search for the target IAM role. For example, `{{LambdaRole}}`.

1. Choose the **Trust relationships** tab.

1. Choose **Edit trust policy** and paste the following trust policy. Make sure to replace the AWS account number and IAM role ARN. The `sts:ExternalId` field further controls who can assume the role. The state machine's name must include only characters that the AWS Security Token Service `AssumeRole` API supports. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "sts:AssumeRole",
         "Principal": {
           "AWS": "arn:aws:iam::{{account-id}}:role/ExecutionRole"  // The source account's state machine execution role ARN
         },
         "Condition": {  // Control which account and state machine can assume the target IAM role
           "StringEquals": {
             "sts:ExternalId": "arn:aws:states:{{region}}:{{account-id}}:stateMachine:testCrossAccount"   //// ARN of the state machine that will assume the role.
           }
         }
       }
     ]
   }
   ```

1. Keep this window open and proceed to the next step for further actions.

## Step 3: Add the required permission in the target role
<a name="tutorial-access-cross-acct-resources-add-permissions"></a>

Permissions in the IAM policies determine whether a specific request is allowed or denied. The target IAM role must have the correct permission to invoke the Lambda function.

1. Choose the **Permissions** tab.

1. Choose **Add permissions** and then choose **Create inline policy**.

1. Choose the **JSON** tab and replace the existing content with the following permission. Make sure to replace your Lambda function ARN.

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "lambda:InvokeFunction",
         "Resource": "arn:aws:lambda:us-east-2:111122223333:function:{{Echo}}"  // The cross-account AWS resource being accessed
       }
     ]
   }
   ```

1. Choose **Review policy**.

1. On the **Review policy** page, enter a name for the permission, and then choose **Create policy**.

## Step 4: Add permission in execution role to assume the target role
<a name="tutorial-access-cross-acct-resources-update-exec-role"></a>

Step Functions doesn’t automatically generate the [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) policy for all cross-account service integrations. You must add the required permission in the state machine's execution role to allow it to assume a target IAM role in one or more AWS accounts.

1. Open your state machine's execution role in the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). To do this:

   1. Open the state machine that you created in [Step 1 in the source account](#tutorial-access-cross-acct-resources-update-task-def).

   1. On the **State machine detail** page, choose **IAM role ARN**.

1. On the **Permissions** tab, choose **Add permissions** and then choose **Create inline policy**.

1. Choose the **JSON** tab and replace the existing content with the following permission. Make sure to replace your Lambda function ARN.

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "sts:AssumeRole",
         "Resource": "arn:aws:iam::111122223333:role/{{LambdaRole}}"  // The target role to be assumed
       }
     ]
   }
   ```

1. Choose **Review policy**.

1. On the **Review policy** page, enter a name for the permission, and then choose **Create policy**.