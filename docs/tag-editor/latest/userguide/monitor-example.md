# Tutorial: Automatically stopping Amazon EC2 instances that

are missing required tags

As your pool of AWS resources and AWS accounts that you manage grows, you can use
tags to make it easier to categorize your resources. Tags are commonly used for critical
use cases such as cost allocation and security. To effectively manage AWS resources,
your resources need to be consistently tagged. Often, when a resource is provisioned, it
gets all the appropriate tags. However, a later process can result in a tag change that
results in drift from the corporate tag policy. By monitoring changes to your tags, you
can spot tag drift and immediately respond. This gives you more confidence that the
processes that depend on your resources being properly categorized will produce the
desired results.

The following example demonstrates how to monitor for tag changes on Amazon EC2 instances
to verify that a specified instance continues to have the required tags. If the
instance's tags change and the instance no longer has the required tags, a Lambda
function is invoked to shut down the instance automatically. Why would you want to do
this? It ensures that all resources are tagged according to your corporate tag policy,
for effective cost allocation, or to be able to trust security based on [attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md").

###### Important

We strongly recommend that you perform this tutorial in a non-production account
where you can't inadvertently shut down important instances.

The example code in this tutorial intentionally limits the impact of this scenario
to only the instances on a list of instance IDs. You must update the list with
instance IDs that you are willing to shut down for the test. This helps ensure that
you can't accidentally shut down every instance in a Region in your AWS account.

After testing, make sure that all of your instances are tagged according to your
company's tagging strategy. Then, you can remove the code that limits the function
to only the instance IDs on the list.

This example uses JavaScript and the 16.x version of
Node.js. The example uses example AWS account ID
123456789012 and the AWS Region US East (N. Virginia) (`us-east-1`).
Replace these with your own test account ID and Region.

###### Note

If your console uses a different Region for its default, ensure that you switch
the Region you're using in this tutorial whenever you change consoles. A common
cause of this tutorial failing is having the instance and function in two different
Regions.

If you use a different Region than `us-east-1`, ensure that you
change all references in the following code examples to your chosen Region.

###### Topics

- [Step 1. Create the Lambda function](#monitor-example-step-1 "#monitor-example-step-1")
- [Step 2. Set up the required IAM
  permissions](#monitor-example-step-2 "#monitor-example-step-2")
- [Step 3. Do a preliminary test of your Lambda
  function](#monitor-example-step-3 "#monitor-example-step-3")
- [Step 4. Create the EventBridge rule that launches
  the function](#monitor-example-step-4 "#monitor-example-step-4")
- [Step 5. Test the complete solution](#monitor-example-step-6 "#monitor-example-step-6")
- [Tutorial summary](#summary "#summary")

## Step 1. Create the Lambda function

###### To create the Lambda function

1. Open the [AWS Lambda management
   console](https://console.aws.amazon.com/lambda/home "https://console.aws.amazon.com/lambda/home").
2. Choose **Create function** and then choose
   **Author from scratch**.
3. For **Function name**, type
   `AutoEC2Termination`.
4. For **Runtime**, choose **Node.js
   16.x**.
5. Keep all other fields at their default values, and choose **Create
   function**.
6. On the **Code** tab of the
   `AutoEC2Termination` detail page, open the
   **index.js** file to view its code.
   - If a tab with **index.js** is open, you can
     choose the edit box in that tab to edit its code.
   - If a tab with **index.js** isn't open,
     secondary-click the **index.js** file under the
     **AutoEC2Terminator** folder in the navigation
     pane. Then choose **Open**.

7. In the **index.js** tab, paste the following code in the
   editor box, replacing anything that is already present.

Replace the value `RegionToMonitor` with the Region that you
want to run this function in.

```
// Set the following line to specify which Region's instances you want to monitor
// Only instances in this Region are succesfully stopped on a match

const RegionToMonitor = "us-east-1"

// Specify the instance ARNs to check.
// This limits the function for safety to avoid the tutorial shutting down all instances in account
// The first ARN is a "dummy" that matches the test event you create in Step 3.
// Replace the second ARN with one that matches a real instance that you want to monitor and that you can
// safely stop

const InstanceList = [
    "i-0000000aaaaaaaaaa",
    "i-05db4466d02744f07"
];

// The tag key name and value that marks a "valid" instance. Instances in the previous list that
// do NOT have the following tag key and value are stopped by this function

const ValidKeyName = "valid-key";
const ValidKeyValue = "valid-value";

// Load and configure the AWS SDK
const AWS = require('aws-sdk');
// Set the AWS Region
AWS.config.update({region: RegionToMonitor});
// Create EC2 service object.
const ec2 = new AWS.EC2({apiVersion: '2016-11-15'});

exports.handler = (event, context, callback) => {

  // Retrieve the details of the reported event.
  var detail = event.detail;
  var tags = detail["tags"];
  var service = detail["service"];
  var resourceType = detail["resource-type"];
  var resource = event.resources[0];
  var resourceSplit = resource.split("/");
  var instanceId = resourceSplit[resourceSplit.length - 1];

  // If this event is not for an EC2 resource, then do nothing.
  if (!(service === "ec2")) {
    console.log("Event not for correct service -- no action (", service, ")" );
    return;
  }

  // If this event is not about an instance, then do nothing.
  if (!(resourceType === "instance")) {
    console.log("Event not for correct resource type -- no action (", resourceType, ")" );
    return;
  }

  // CAUTION - Removing the following 'if' statement causes the function to run against
  //           every EC2 instance in the specified Region in the calling AWS account.
  //           If you do this and an instance is not tagged with the approved tag key
  //           and value, this function stops that instance.

  // If this event is not for the ARN of an instance in our include list, then do nothing.
  if (InstanceList.indexOf(instanceId)<0) {
    console.log("Event not for one of the monitored instances -- no action (", resource, ")");
    return;
  }

  console.log("Tags changed on monitored EC2 instance (",instanceId,")");

  // Check attached tags for expected tag key and value pair
  if ( tags.hasOwnProperty(ValidKeyName) && tags[ValidKeyName] == "valid-value"){
    // Required tags ARE present
    console.log("The instance has the required tag key and value -- no action");
    callback(null, "no action");
    return;
  }

  // Required tags NOT present
  console.log("This instance is missing the required tag key or value -- attempting to stop the instance");

  var params = {
    InstanceIds: [instanceId],
    DryRun: true
  };

  // call EC2 to stop the selected instances
  ec2.stopInstances(params, function(err, data) {
    if (err && err.code === 'DryRunOperation') {
      // dryrun succeeded, so proceed with "real" stop operation
      params.DryRun = false;
      ec2.stopInstances(params, function(err, data) {
        if (err) {
          console.log("Failed to stop instance");
          callback(err, "fail");
        } else if (data) {
          console.log("Successfully stopped instance", data.StoppingInstances);
          callback(null, "Success");
        }
      });
    } else {
      console.log("Dryrun attempt failed");
      callback(err);
    }
  });
};
```

8. Choose **Deploy** to save your changes and make the new
   version of the function active.

This Lambda function checks the tags of an Amazon EC2 instance, as reported by the tag
change event in EventBridge. In this example, if the instance in the event is missing the
required tag key `valid-key` or if that tag doesn't have the value
`valid-value`, then the function tries to stop the instance. You can
change this logical check or the tag requirements for your own specific use
cases.

Keep the Lambda console window open in your browser.

## Step 2. Set up the required IAM

permissions

Before the function can successfully run, you must grant the function the
permission to stop an EC2 instance. The AWS provided role [lambda_basic_execution](https://console.aws.amazon.com/iamv2/home#/roles/details/lambda_basic_execution "https://console.aws.amazon.com/iamv2/home#/roles/details/lambda_basic_execution") doesn't have that permission.
In this tutorial, you modify the default IAM permission policy that is attached to
the function's execution role named
`AutoEC2Termination-role-`uniqueid``.
 The minimum additional permission required for this tutorial is
 `ec2:StopInstances`.

For more information about creating Amazon EC2 specific IAM policies, see [Amazon EC2: Allows starting or stopping an EC2 Instance and modifying a security
group, programmatically and in the console](../../../IAM/latest/UserGuide/reference_policies_examples_ec2_instance-securitygroup.md "../../../IAM/latest/UserGuide/reference_policies_examples_ec2_instance-securitygroup.md") in the _IAM User Guide_.

###### To create an IAM permission policy and attach it to the Lambda function's

execution role

1. In a different browser tab or window, open the [Roles](https://console.aws.amazon.com/iamv2/home#/roles "https://console.aws.amazon.com/iamv2/home#/roles") page of the IAM console.
2. Start typing the role name `AutoEC2Termination`, and
   when it appears in the list, choose the role name.
3. On the role's **Summary** page, choose the
   **Permissions** tab and choose the name of the one
   policy that is already attached.
4. On the policy's **Summary** page, choose **Edit
   policy**.
5. On the **Visual Editor** tab, choose **Add
   additional permissions**.
6. For **Service**, choose **EC2**.
7. For **Actions**, choose
   **StopInstances**. You can type
   `Stop` in the search bar, and then choose
   `StopInstances` when it appears.
8. For **Resources**, choose **All
   resources**, choose **Review policy**, and
   then choose **Save changes**.

This automatically creates a new version of the policy and sets that
version as the default.

Your final policy should look similar to the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "ec2:StopInstances",
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": "logs:CreateLogGroup",
 "Resource": "arn:aws:logs:us-east-1:123456789012:*"
 },
 {
 "Sid": "VisualEditor2",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/lambda/AutoEC2Termination:*"
 }
 ]
}`

```

## Step 3. Do a preliminary test of your Lambda

function

In this step, you submit a test event to your function. The Lambda test
functionality works by submitting a manually provided test event. The function
processes the test event just as if the event had come from EventBridge. You can define
multiple test events with different values to exercise all of the different parts of
your code. In this step, you submit a test event that indicates that an Amazon EC2
instance's tags changed, and the new tags don't include the required tag key and
value.

###### To test your Lambda function

1. Return to the window or tab with the Lambda console and open the
   **Test** tab for your
   **AutoEC2Termination** function.
2. Choose **Create new event**.
3. For **Event name**, enter
   `SampleBadTagChangeEvent`.
4. In the **Event JSON**, replace the text with the sample
   event shown in the following example text. You don't need to modify the
   accounts, Region, or instance ID for this test event to work
   correctly.

```
{
  "version": "0",
  "id": "bddcf1d6-0251-35a1-aab0-adc1fb47c11c",
  "detail-type": "Tag Change on Resource",
  "source": "aws.tag",
  "account": "123456789012",
  "time": "2018-09-18T20:41:38Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ec2:us-east-1:123456789012:instance/i-0000000aaaaaaaaaa"
  ],
  "detail": {
    "changed-tag-keys": [
      "valid-key"
    ],
    "tags": {
      "valid-key": "NOT-valid-value"
    },
    "service": "ec2",
    "resource-type": "instance",
    "version": 3
  }
}
```

5. Choose **Save**, and then choose
   **Test**.

The test appears to fail, but that's OK.

You should see the following error in the **Execution
results** tab under **Response**.

```
{
  "errorType": "InvalidInstanceID.NotFound",
  "errorMessage": "The instance ID 'i-0000000aaaaaaaaaa' does not exist",
  ...
}
```

The error occurs because the instance specified in the test event doesn't
exist.

The information on the **Execution results** tab, in the
**Function Logs** section , demonstrates that your
Lambda function successfully attempted to stop an EC2 instance. However, it
failed because the code initially attempts a [`DryRun`](../../../AWSEC2/latest/APIReference/API_StartInstances.md#API_StartInstances_RequestParameters "../../../AWSEC2/latest/APIReference/API_StartInstances.md#API_StartInstances_RequestParameters") operation to stop the instance, which
indicated that the instance ID was not valid.

```
START RequestId: 390c1f8d-0d9b-4b44-b087-8de64479ab44 Version: $LATEST
2022-11-30T20:17:30.427Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    INFO    Tags changed on monitored EC2 instance ( i-0000000aaaaaaaaaa )
2022-11-30T20:17:30.427Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    INFO    This instance is missing the required tag key or value -- attempting to stop the instance
2022-11-30T20:17:31.206Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    INFO    Dryrun attempt failed
2022-11-30T20:17:31.207Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    ERROR   Invoke Error     {"errorType":"InvalidInstanceID.NotFound","errorMessage":"The instance ID 'i-0000000aaaaaaaaaa' does not exist","code":"InvalidInstanceID.NotFound","message":"The instance ID 'i-0000000aaaaaaaaaa' does not exist","time":"2022-11-30T20:17:31.205Z","requestId":"a5192c3b-142d-4cec-bdbc-685a9b7c7abf","statusCode":400,"retryable":false,"retryDelay":36.87870631147607,"stack":["InvalidInstanceID.NotFound: The instance ID 'i-0000000aaaaaaaaaa' does not exist","    at Request.extractError (/var/runtime/node_modules/aws-sdk/lib/services/ec2.js:50:35)","    at Request.callListeners (/var/runtime/node_modules/aws-sdk/lib/sequential_executor.js:106:20)","    at Request.emit (/var/runtime/node_modules/aws-sdk/lib/sequential_executor.js:78:10)","    at Request.emit (/var/runtime/node_modules/aws-sdk/lib/request.js:686:14)","    at Request.transition (/var/runtime/node_modules/aws-sdk/lib/request.js:22:10)","    at AcceptorStateMachine.runTo (/var/runtime/node_modules/aws-sdk/lib/state_machine.js:14:12)","    at /var/runtime/node_modules/aws-sdk/lib/state_machine.js:26:10","    at Request.<anonymous> (/var/runtime/node_modules/aws-sdk/lib/request.js:38:9)","    at Request.<anonymous> (/var/runtime/node_modules/aws-sdk/lib/request.js:688:12)","    at Request.callListeners (/var/runtime/node_modules/aws-sdk/lib/sequential_executor.js:116:18)"]}
END RequestId: 390c1f8d-0d9b-4b44-b087-8de64479ab44
```

6. To prove that the code doesn't try to stop the instance when the correct
   tag is used, you can create and submit another test event.

Choose the **Test** tab above **Code
source**. The console displays your existing
**SampleBadTagChangeEvent** test event. 7. Choose **Create new event**. 8. For **Event name**, type
`SampleGoodTagChangeEvent`. 9. In line 17, delete `NOT-` to change the value to
`valid-value`. 10. At the top of the **Test event** window, choose
**Save**, and then choose
**Test**.

The output displays the following, which demonstrates that the function
recognizes the valid tag and doesn't attempt to shut down the
instance.

```
START RequestId: 53631a49-2b54-42fe-bf61-85b9e91e86c4 Version: $LATEST
2022-12-01T23:24:12.244Z    53631a49-2b54-42fe-bf61-85b9e91e86c4    INFO    Tags changed on monitored EC2 instance ( i-0000000aaaaaaaaaa )
2022-12-01T23:24:12.244Z    53631a49-2b54-42fe-bf61-85b9e91e86c4    INFO    The instance has the required tag key and value -- no action
END RequestId: 53631a49-2b54-42fe-bf61-85b9e91e86c4
```

Keep the Lambda console open in your browser.

## Step 4. Create the EventBridge rule that launches

the function

Now you can create an EventBridge rule that matches the event and points to your Lambda
function.

###### To create the EventBridge rule

1. In a different browser tab or window, open the [EventBridge console](https://console.aws.amazon.com/events/home#/rules/create "https://console.aws.amazon.com/events/home#/rules/create") to the
   **Create Rule** page.
2. For **Name**, enter
   `ec2-instance-rule`, and then choose
   **Next**.
3. Scroll down to **Creation method** and choose
   **Custom pattern (JSON editor)**.
4. In the editing box, paste the following pattern text, and then choose
   **Next**.

```
{
  "source": [
    "aws.tag"
  ],
  "detail-type": [
    "Tag Change on Resource"
  ],
  "detail": {
    "service": [
      "ec2"
    ],
    "resource-type": [
      "instance"
    ]
  }
}
```

This rule matches `Tag Change on Resource` events for Amazon EC2
instances and invokes whatever you specify as the
**Target** in the next step. 5. Next, add your Lambda function as the target. In the **Target
1** box, under **Select a target**, choose
**Lambda function**. 6. Under **Function**, choose the
**AutoEC2Termination** function that you created
previously, and then choose **Next**. 7. On the **Configure tags** page, choose
**Next**. Then on the **Review and
create** page, choose **Create rule**. This
also automatically grants permission for EventBridge to invoke the specified Lambda
function.

## Step 5. Test the complete solution

You can test your final result by creating an EC2 instance and watching what
happens when you change its tags.

###### To test the monitoring solution with a real instance

1. Open the [Amazon EC2
   console](https://console.aws.amazon.com/ec2/v2/home#Instances: "https://console.aws.amazon.com/ec2/v2/home#Instances:") to the **Instances** page.
2. Create an Amazon EC2 instance. Before you launch it, attach a tag with the key
   `valid-key` and the value `valid-value`. For
   information about how to create and launch an instance,see [Step 1: Launch an instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance") in the _Amazon EC2 User Guide_. In the procedure _To launch an instance_, in step 3, where you enter the
   **Name** tag, also choose **Add additional
   tags**, choose **Add tag**, and then enter the
   **Key** of `valid-key` and
   **Value** of `valid-value`. You
   can **Proceed without a key pair** if this instance is
   solely for the purposes of this tutorial and you plan on deleting this
   instance after you complete it. Return to this tutorial when you reach the
   end of **Step 1**; you don't need to do **Step 2:
   Connect to your instance**.
3. Copy the **InstanceId** from the console.
4. Switch from the Amazon EC2 console to the Lambda console. Choose your
   **AutoEC2Termination** function, choose the
   **Code** tab, and then choose the
   **index.js** tab to edit your code.
5. Change the second entry in the `InstanceList` by pasting the
   value you copied from the Amazon EC2 console. Ensure that the
   `RegionToMonitor` value matches the Region that contains the
   instance you pasted.
6. Choose **Deploy** to make your changes active. The
   function is now ready to be activated by tag changes to that instance in the
   specified Region.
7. Switch from the Lambda console to the Amazon EC2 console.
8. Change the **Tags** attached to the instance by either
   deleting the **valid-key** tag or by changing that key's
   value.

###### Note

For information about how to change the tags on a running Amazon EC2
instance, see [Add and delete tags on an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags") in the
_Amazon EC2 User Guide_. 9. Wait a few seconds, and then refresh the console. The instance should
change its **Instance state** to
**Stopping** and then to
**Stopped**. 10. Switch from the Amazon EC2 console to the Lambda console with your function, and
choose the **Monitor** tab. 11. Choose the **Logs** tab, and in the **Recent
invocations** table, choose the most recent entry in the
**LogStream** column.

The Amazon CloudWatch console opens to the **Log events** page for
the last invocation of your Lambda function. The last entry should look
similar to the following example.

```
2022-11-30T12:03:57.544-08:00    START RequestId: b5befd18-2c41-43c8-a320-3a4b2317cdac Version: $LATEST
2022-11-30T12:03:57.548-08:00    2022-11-30T20:03:57.548Z b5befd18-2c41-43c8-a320-3a4b2317cdac INFO Tags changed on monitored EC2 instance ( arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0 )
2022-11-30T12:03:57.548-08:00    2022-11-30T20:03:57.548Z b5befd18-2c41-43c8-a320-3a4b2317cdac INFO This instance is missing the required tag key or value -- attempting to stop the instance
2022-11-30T12:03:58.488-08:00    2022-11-30T20:03:58.488Z b5befd18-2c41-43c8-a320-3a4b2317cdac INFO Successfully stopped instance [ { CurrentState: { Code: 64, Name: 'stopping' }, InstanceId: 'i-1234567890abcdef0', PreviousState: { Code: 16, Name: 'running' } } ]
2022-11-30T12:03:58.546-08:00    END RequestId: b5befd18-2c41-43c8-a320-3a4b2317cdac
```

## Tutorial summary

This tutorial demonstrated how to create an EventBridge rule to match against a tag
change on a resource event for Amazon EC2 instances. The rule pointed to a Lambda function
that automatically shuts down the instance if it doesn't have the required
tag.

The Amazon EventBridge support for tag changes on AWS resources opens possibilities to
build event-driven automation across many AWS services. Combining this capability
with AWS Lambda provides you with tools to build serverless solutions that access
AWS resources securely, scale on demand, and are cost effective.

Other possible use cases for the tag-change-on-resource EventBridge event include:

- **Launch a warning if someone accesses your resource
  from an unusual IP address** – Use a tag to store the
  source IP address of each visitor that accesses your resource. Changes to
  the tag generates a CloudWatch event. You can use that event to compare the source
  IP address to a list of valid IP addresses and activate a warning email if
  the source IP address isn't valid.
- **Monitor if there are changes to your tag-based
  access control for a resource** – If you have set up
  access to a resource using [attribute (tag) based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"), you can use EventBridge
  events generated by any changes to the tag to prompt an audit by your
  security team.
