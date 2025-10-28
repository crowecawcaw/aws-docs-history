# Set up execution roles with Workflow Studio in Step Functions

You can use Workflow Studio to set up execution roles for your workflows. Every Step Functions
state machine requires an AWS Identity and Access Management (IAM) role which grants the state
machine permission to perform actions on AWS services and resources or call
HTTPS APIs. This role is called an _execution
role_.

The execution role must contain IAM policies for each action, for
example, policies that allow the state machine to invoke an AWS Lambda
function, run an AWS Batch job, or call the Stripe API.
Step Functions requires you to provide an execution role in the following
cases:

- You create a state machine in the console, AWS SDKs or AWS CLI using the [CreateStateMachine](../apireference/API_CreateStateMachine.md "../apireference/API_CreateStateMachine.md") API.
- You [test](test-state-isolation.md "test-state-isolation.md") a state in the console, AWS SDKs, or AWS CLI using the [TestState](../apireference/API_TestState.md "../apireference/API_TestState.md") API.

###### Topics

- [About auto-generated roles](#wfs-auto-gen-roles "#wfs-auto-gen-roles")
- [Automatically generating roles](#auto-generating-roles "#auto-generating-roles")
- [Resolving role generation problems](#resolve-role-gen-problem "#resolve-role-gen-problem")
- [Role for testing HTTP Tasks in Workflow Studio](#test-state-role-http "#test-state-role-http")
- [Role for testing an optimized service integration in Workflow Studio](#test-state-role-optimized "#test-state-role-optimized")
- [Role for testing an AWS SDK service integration in Workflow Studio](#test-state-role-aws-sdk "#test-state-role-aws-sdk")
- [Role for testing flow states in Workflow Studio](#test-state-role-flow "#test-state-role-flow")

## About auto-generated roles

When you create a state machine in the Step Functions console, [Workflow Studio](workflow-studio.md "workflow-studio.md") can automatically create an execution role for you which contains the necessary IAM policies. Workflow Studio analyzes your state machine definition and generates policies with the least privileges necessary to execute your workflow.

Workflow Studio can generate IAM policies for the following:

- [HTTP Tasks](call-https-apis.md "call-https-apis.md") that call HTTPS APIs.
- Task states that call other AWS services using [optimized integrations](integrate-optimized.md "integrate-optimized.md"), such as [Lambda Invoke](connect-lambda.md "connect-lambda.md"), [DynamoDB GetItem](connect-batch.md "connect-batch.md"), or [AWS Glue StartJobRun](connect-glue.md "connect-glue.md").
- Task states that run [nested workflows](connect-stepfunctions.md "connect-stepfunctions.md").
- [Distributed Map states](state-map-distributed.md "state-map-distributed.md"), including [policies](iam-policies-eg-dist-map.md "iam-policies-eg-dist-map.md") to start child workflow executions, list Amazon S3 buckets, and read or write S3 objects.
- [X-Ray](concepts-xray-tracing.md "concepts-xray-tracing.md") tracing. Every role that is auto-generated in Workflow Studio contains a [policy](concepts-xray-tracing.md#xray-iam "concepts-xray-tracing.md#xray-iam") which grants permissions for the state machine to send traces to X-Ray.
- [Using CloudWatch Logs to log execution history in Step Functions](cw-logs.md "cw-logs.md") when logging is enabled on the state machine.

Workflow Studio can't generate IAM policies for Task states that call other AWS services using [AWS SDK integrations](supported-services-awssdk.md "supported-services-awssdk.md").

## Automatically generating roles

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home "https://console.aws.amazon.com/states/home"), choose **State machines** from the menu, then choose **Create state machine**.

You can also update an existing state machine. Refer Step 4 if you're updating a state machine. 2. Choose **Create from blank**. 3. Name your state machine, then choose **Continue** to edit your state machine in Workflow Studio. 4. Choose the **Config** tab. 5. Scroll down to the **Permissions** section, and do the following:

    1. For **Execution role**, make sure you keep the default selection of **Create new role**.


    Workflow Studio automatically generates all the required IAM policies for every valid state in your state machine definition. It displays a banner in with the message, **An execution role will be created with full permissions.**



    ![Illustrative screenshot of the Config tab with preview of auto-generated permissions.](images/wfs-full-permissions-role.png)

    ###### Tip

    To review the permissions that Workflow Studio automatically generates for your state machine, choose **Review auto-generated permissions**.


    ###### Note

    If you delete the IAM role that Step Functions creates, Step Functions can't
     recreate it later. Similarly, if you modify the role (for example, by
     removing Step Functions from the principals in the IAM policy), Step Functions can't
     restore its original settings later.


    If Workflow Studio can't generate all the required IAM policies, it displays a banner with the message **Permissions for certain actions cannot be auto-generated. An IAM role will be created with partial permissions only.** For information about how to add the missing permissions, see [Resolving role generation problems](#resolve-role-gen-problem "#resolve-role-gen-problem").
    2. Choose **Create** if you're creating a state machine. Otherwise, choose **Save**.
    3. Choose **Confirm** in the dialog box that appears.


    Workflow Studio saves your state machine and creates the new execution role.

## Resolving role generation problems

Workflow Studio can't automatically generate an execution role with all the required permissions in the following cases:

- There are errors in your state machine. Make sure to resolve all validation errors in Workflow Studio. Also, make sure that you address any server-side errors you encounter in the course of saving.
- Your state machine contains tasks use AWS SDK integrations. Workflow Studio can't [auto-generate](#auto-generating-roles "#auto-generating-roles") IAM policies in this case. Workflow Studio displays a banner with the message, **Permissions for certain actions cannot be auto-generated. An IAM role will be created with partial permissions only.** In the **Review auto-generated permissions** table, choose the content in **Status** for more information about the policies your execution role is missing. Workflow Studio can still generate an execution role, but this role will not contain IAM policies for all actions. See the links under **Documentation links** to write your own policies and add them to the role after it is generated. These links are available even after you save the state machine.

## Role for testing HTTP Tasks in Workflow Studio

[Testing](call-https-apis.md#http-task-test "call-https-apis.md#http-task-test") an HTTP Task state requires an execution role. If you don’t have a role with sufficient permissions, use one of the following options to create a role:

- **Auto-generate a role with Workflow Studio (recommended)** – This is the secure option. Close the **Test state** dialog box and follow the instructions in [Automatically generating roles](#auto-generating-roles "#auto-generating-roles"). This will require you to create or update your state machine first, then go back into Workflow Studio to test your state.
- **Use a role with Administrator access** – If you have permissions to create a role with full access to all services and resources in AWS, you can use that role to test any type of state in your workflow. To do this, you can create a Step Functions service role and add the [AdministratorAccess policy](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator") to it in the IAM console [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

## Role for testing an optimized service integration in Workflow Studio

Task states that call [optimized service integrations](integrate-optimized.md "integrate-optimized.md") require an execution role. If you don’t have a role with sufficient permissions, use one of the following options to create a role:

- **Auto-generate a role with Workflow Studio (recommended)** – This is the secure option. Close the **Test state** dialog box and follow the instructions in [Automatically generating roles](#auto-generating-roles "#auto-generating-roles"). This will require you to create or update your state machine first, then go back into Workflow Studio to test your state.
- **Use a role with Administrator access** – If you have permissions to create a role with full access to all services and resources in AWS, you can use that role to test any type of state in your workflow. To do this, you can create a Step Functions service role and add the [AdministratorAccess policy](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator") to it in the IAM console [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

## Role for testing an AWS SDK service integration in Workflow Studio

Task states that call [AWS SDK integrations](supported-services-awssdk.md "supported-services-awssdk.md") require an execution role. If you don’t have a role with sufficient permissions, use one of the following options to create a role:

- **Auto-generate a role with Workflow Studio (recommended)** – This is the secure option. Close the **Test state** dialog box and follow the instructions in [Automatically generating roles](#auto-generating-roles "#auto-generating-roles"). This will require you to create or update your state machine first, then go back into Workflow Studio to test your state. Do the following:
  1.  Close the **Test state** dialog box
  2.  Choose the **Config** tab to view the Config mode.
  3.  Scroll down to the **Permissions** section.
  4.  Workflow Studio displays a banner with the message, **Permissions for certain actions cannot be auto-generated. An IAM role will be created with partial permissions only.** Choose **Review auto-generated permissions**.
  5.  The **Review auto-generated permissions** table displays a row that shows the action corresponding to the task state you want to test. See the links under **Documentation links** to write your own IAM policies into a custom role.

- **Use a role with Administrator access** – If you have permissions to create a role with full access to all services and resources in AWS, you can use that role to test any type of state in your workflow. To do this, you can create a Step Functions service role and add the [AdministratorAccess policy](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator") to it in the IAM console [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

## Role for testing flow states in Workflow Studio

You require an execution role to test flow states in Workflow Studio. Flow states are those states that direct execution flow, such as [Choice workflow state](state-choice.md "state-choice.md"), [Parallel workflow state](state-parallel.md "state-parallel.md"), [Map workflow state](state-map.md "state-map.md"), [Pass workflow state](state-pass.md "state-pass.md"), [Wait workflow state](state-wait.md "state-wait.md"), [Succeed workflow state](state-succeed.md "state-succeed.md"), or [Fail workflow state](state-fail.md "state-fail.md"). The [TestState](../apireference/API_TestState.md "../apireference/API_TestState.md") API doesn't work with Map or Parallel states. Use one of the following options to create a role for testing a flow state:

- **Use any role in your AWS account (recommended)** – Flow states do not require any specific IAM policies, because they don’t call AWS actions or resources. Therefore, you can use any IAM role in your AWS account.
  1.  In the **Test state** dialog box, select any role from the **Execution role** dropdown list.
  2.  If no roles appear in the dropdown list, do the following:
      1. In the IAM console [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), choose **Roles**.
      2. Choose a role from the list, and copy its ARN from the role details page. You will need to provide this ARN in the **Test state** dialog box.
      3. In the **Test state** dialog box, select **Enter a role ARN** from the **Execution role** dropdown list.
      4. Paste the ARN in **Role ARN**.

- **Use a role with Administrator access** – If you have permissions to create a role with full access to all services and resources in AWS, you can use that role to test any type of state in your workflow. To do this, you can create a Step Functions service role and add the [AdministratorAccess policy](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator") to it in the IAM console [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
