

# Tutorial: Create an EventBridge pipe that filters source events
<a name="pipes-tutorial-create-dynamodb-sqs"></a>

In this tutorial, you'll create a pipe that connects a DynamoDB stream source to an Amazon SQS queue target. This includes specifying an event pattern for the pipe to use when filtering events to deliver to the queue. You'll then test the pipe to ensure that only the desired events are being delivered.

## Prerequisites: Create the source and target
<a name="pipes-tutorial-create-dynamodb-sqs-prereqs"></a>

Before you create the pipe, you'll need to create the source and target that the pipe is to connect. In this case, an Amazon DynamoDB data stream to act as the pipe source, and an Amazon SQS queue as the pipe target.

To simplify this step, you can use AWS CloudFormation to deploy the source and target resources. To do this, you'll create a CloudFormation template defining the following resources:
+ The pipe source 

  An Amazon DynamoDB table, named `pipe-tutorial-source`, with a stream enabled to provide an ordered flow of information about changes to items in the DynamoDB table.
+ The pipe target 

  An Amazon SQS queue, named `pipe-tutorial-target`, to receive the DynamoDB stream of events from your pipe.

**To create the CloudFormation template for provisioning pipe resources**

1. Copy the JSON template text in the [CloudFormation template for generating prerequisites](#pipes-tutorial-create-cfn-template) section, below.

1. Save the template as a JSON file (for example, `~/pipe-tutorial-resources.json`).

Next, use the template file you just created to provision a CloudFormation stack.

**Note**  
Once you create your CloudFormation stack, you will be charged for the AWS resources it provisions.

**Provision the tutorial prerequisites using the AWS CLI**
+ Run the following CLI command, where `--template-body` specifies the location of your template file:

  ```
  aws cloudformation create-stack --stack-name {{pipe-tuturial-resources}} --template-body file://~/{{pipe-tutorial-resources.json}}
  ```

**Provision tutorial prerequisites using the CloudFormation console**

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Select **Stacks**, then select **Create stack**, and choose **with new resources (standard)**.

   CloudFormation displays the **Create stack** wizard.

1. For **Prerequisite - Prepare template**, leave the default, **Template is ready**, selected.

1. Under **Specify template**, select **Upload a template file**, and then choose the file and select **Next**.

1. Configure the stack and the resources it will provision:
   + For **Stack name**, enter `pipe-tuturial-resources`.
   + For **Parameters**, leave the default names for the DynamoDB table and Amazon SQS queue.
   + Choose **Next**.

1. Choose **Next**, then choose **Submit**.

   CloudFormation creates the stack and provisions the resources defined in the template.

For more information about CloudFormation, see [What is CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) in the *CloudFormation User Guide*.

## Step 1: Create the pipe
<a name="pipes-tutorial-create-dynamodb-sqs-create-pipe"></a>

With the pipe source and target provisioned, you can now create the pipe to connect the two services.

**Create the pipe using the EventBridge console**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. On the navigation pane, choose **Pipes**.

1. Choose **Create pipe**.

1. For **Name**, name your pipe `pipe-tutorial`.

1. Specify the DynamoDB data stream source:

   1. Under **Details**, for **Source**, select **DynamoDB data stream** .

      EventBridge displays DynamoDB-specific source configuration settings.

   1. For **DynamoDB stream**, select `pipe-tutorial-source`.

      Leave **Starting position** set to the default, `Latest`.

   1. Choose **Next**.

1. Specify and test an event pattern to filter events:

   Filtering enables you to control which events the pipes sends to enrichment or the target. The pipe only sends events that match the event pattern on to enrichment or the target.

   For more information, see [Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md).
**Note**  
You are only billed for those events sent to enrichment or the target.

   1. Under **Sample event - *optional***, leave **AWS events** selected, and make sure that **DynamoDB Stream Sample event 1** is selected.

      This is the sample event which you'll use to test our event pattern.

   1. Under **Event pattern**, enter the following event pattern:

      ```
      {
        "eventName": ["INSERT", "MODIFY"]
      }
      ```

   1. Choose **Test pattern**.

      EventBridge displays a message that the sample event matches the event pattern. This is because the sample event has an `eventName` value of `INSERT`.

   1. Choose **Next**.

1. Choose **Next** to skip specifying an enrichment. 

   In this example, you won’t select an enrichment. Enrichments enable you to select a service to enhance the data from the source before sending it to the target. For more details, see [Event enrichment in Amazon EventBridge Pipes](pipes-enrichment.md).

1. Specify your Amazon SQS queue as the pipe target:

   1. Under **Details**, for **Target service**, select **Amazon SQS queue**.

   1. For **Queue**, select `pipe-tutorial-target`.

   1. Leave the **Target Input transformer** section empty.

      For more information, see [Amazon EventBridge Pipes input transformation](eb-pipes-input-transformation.md).

1. Choose **Create Pipe**

   EventBridge creates the pipe and displays the pipe detail page. The pipe is ready once its status updates to `Running`.

## Step 2: Confirm the pipe filters events
<a name="pipes-tutorial-create-dynamodb-sqs-test"></a>

Pipe is set up, but has yet to receive events from table.

To test the pipe, you'll update entries in the DynamoDB table. Each update will generate events that the DynamoDB stream sends to our pipe. Some will match the event pattern you specified, some will not. You can then examine the Amazon SQS queue to ensure that the pipe only delivered those event that matched our event pattern.

**Update table items to generate events**

1. Open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. From the left navigation, select **Tables**. Select the `pipe-tutorial-source` table.

   DynamoDB displays the table details page for `pipe-tutorial-source`.

1. Select **Explore table items**, and then choose **Create item**.

   DynamoDB displays the **Create item** page.

1. Under **Attributes**, create a new table item:

   1. For **Album** enter `Album A`.

   1. For **Artist** enter `Artist A`.

   1. Choose **Create item**.

1. Update the table item:

   1. Under **Items returned**, choose **Album A**.

   1. Select **Add new attribute**, then select **String**.

   1. Enter a new value of `Song`, with a value of `Song A`.

   1. Choose **Save changes**.

1. Delete the table item:

   1. Under **Items returned**, check **Album A**.

   1. From the **Actions** menu, select **Delete items**.

You have made three updates to the table item; this generates three events for the DynamoDB data stream:
+ An `INSERT` event when you created the item.
+ A `MODIFY` event when you added an attribute to the item.
+ A `REMOVE` event when you deleted the item.

However, the event pattern you specified for the pipe should filter out any events that are not `INSERT` or `MODIFY` events. Next, confirm that the pipe delivered the expected events to the queue.

**Confirm the expected events were delivered to the queue**

1. Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. Choose the `pipe-tutorial-target` queue.

   Amazon SQS displays the queue details page.

1. Select **Send and receive messages**, then under **Receive messages** choose **Poll for messages**.

   The queue polls the pipe and then lists the events it receives.

1. Choose the event name to see the event JSON that was delivered.

 There should be two events in the queue: one with an `eventName` of `INSERT`, and one with an `eventName` of `MODIFY`. However, the pipe did not deliver the event for deleting the table item, since that event had an `eventName` of `REMOVE`, which did not match the event pattern you specified in the pipe.

## Step 3: Clean up your resources
<a name="pipes-tutorial-create-dynamodb-sqs-cleanup"></a>

First, delete the pipe itself.

**Delete the pipe using the EventBridge console**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. On the navigation pane, choose **Pipes**.

1. Select the `pipe-tutorial` pipe, and choose **Delete**.

Then, delete the CloudFormation stack, to prevent being billed for the continued usage of the resources provisioned within it.

**Delete the tutorial prerequisites using the AWS CLI**
+ Run the following CLI command, where `--stack-name` specifies the name of your stack:

  ```
  aws cloudformation delete-stack --stack-name {{pipe-tuturial-resources}}
  ```

**Delete the tutorial prerequisites using the CloudFormation console**

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the **Stacks** page, select the stack and then select **Delete**.

1. Select **Delete** to confirm your action.

## CloudFormation template for generating prerequisites
<a name="pipes-tutorial-create-cfn-template"></a>

Use the JSON below to create a CloudFormation template for provisioning the source and target resources necessary for this tutorial.

```
{
  "AWSTemplateFormatVersion": "2010-09-09",

  "Description" : "Provisions resources to use with the EventBridge Pipes tutorial. You will be billed for the AWS resources used if you create a stack from this template.",

  "Parameters" : {
    "SourceTableName" : {
      "Type" : "String",
      "Default" : "pipe-tutorial-source",
      "Description" : "Specify the name of the table to provision as the pipe source, or accept the default."
    },
    "TargetQueueName" : {
      "Type" : "String",
      "Default" : "pipe-tutorial-target",
      "Description" : "Specify the name of the queue to provision as the pipe target, or accept the default."
    }
  },
  "Resources": {
    "PipeTutorialSourceDynamoDBTable": {
      "Type": "AWS::DynamoDB::Table",
      "Properties": {
        "AttributeDefinitions": [{
            "AttributeName": "Album",
            "AttributeType": "S"
          },
          {
            "AttributeName": "Artist",
            "AttributeType": "S"
          }

        ],
        "KeySchema": [{
            "AttributeName": "Album",
            "KeyType": "HASH"

          },
          {
            "AttributeName": "Artist",
            "KeyType": "RANGE"
          }
        ],
        "ProvisionedThroughput": {
          "ReadCapacityUnits": 10,
          "WriteCapacityUnits": 10
        },
        "StreamSpecification": {
          "StreamViewType": "NEW_AND_OLD_IMAGES"
        },
        "TableName": { "Ref" : "SourceTableName" }
      }
    },
    "PipeTutorialTargetQueue": {
      "Type": "AWS::SQS::Queue",
      "Properties": {
        "QueueName": { "Ref" : "TargetQueueName" }
      }
    }
  }
}
```