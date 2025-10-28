# Use Mechanical Turk notifications

Amazon Mechanical Turk (Mechanical Turk) has a notifications capability that can be used to trigger actions when your
HITs reach various stages. Using notifications, you can process the results of assignments and
HITs immediately after they are submitted to evaluate worker submissions or begin downstream
processing of data. This allows you to integrate Mechanical Turk more easily into your processes and can
support moving from batch processing of data to a real-time approach.

Common use cases include:

- Immediately add more assignments to a HIT when there is disagreement between workers
  that have responded.
- Update a database with the results of the HIT.
- Evaluate worker submissions as soon as they are submitted so you can take action if
  workers are consistently making errors.
- Chain multiple Mechanical Turk steps together by triggering the next step when a HIT is completed.

## Notification event types

Notifications are associated with a HIT Type. You can request that Mechanical Turk send a
notification when any of the following events occur for HITs using a given HIT Type.

- `AssignmentAccepted`: A worker has accepted a HIT and has an assignment.
- `AssignmentAbandoned`: An assignment has been abandoned because the assignment
  duration has elapsed.
- `AssignmentReturned`: A worker has chosen to return an assignment rather than
  complete the task.
- `AssignmentSubmitted`: A worker has submitted an assignment.
- `AssignmentRejected`: You have rejected an assignment.
- `AssignmentApproved`: An assignment has been approved.
- `HITCreated`: A HIT has been created using the HIT Type.
- `HITExtended`: Assignments have been added to a HIT.
- `HITDisposed`: A HIT has been disposed.
- `HITReviewable`: A HIT has reached the `Reviewable` state, either
  because all of the assignments have been submitted or the HIT has expired.
- `HITExpired`: The HIT has expired (the lifetime has elapsed) before all of the
  available assignments have been submitted.
- `Ping`: Is only be sent when using the [`SendTestEventNotification`](../AWSMturkAPI/ApiReference_SendTestEventNotificationOperation.md "../AWSMturkAPI/ApiReference_SendTestEventNotificationOperation.md") operation.

The `AssignmentSubmitted` and `HITReviewable` events are the most
commonly used event notifications because they allow you to setup processes that can be
triggered as soon as an assignment or HIT is complete. Using the `HITReviewable`
notification, you can immediately update a database or other system with the values returned
by the HIT. The `HITExpired` event is also useful because it can be treated as a
dead letter queue, letting you act on tasks that weren't completed by workers. Using the
`HITExpired` notification, you might sideline tasks to be completed by members of
your team, or attempt to repost them at a higher reward amount.

## Notification destination

Notifications can be sent to either an Amazon Simple Queue Service (Amazon SQS) queue or an Amazon Simple Notification Service (Amazon SNS)
topic. In both cases, multiple events may be batched into a single message if appropriate.

To set up an Amazon SQS queue for use with Mechanical Turk, follow the setup instructions found in [Notification Handling Using Amazon SQS](../AWSMturkAPI/ApiReference_NotificationReceptorAPI_SQSTransportArticle.md "../AWSMturkAPI/ApiReference_NotificationReceptorAPI_SQSTransportArticle.md"). To set up an Amazon SNS topic, follow the steps
in [Notification Handling Using Amazon SNS](../AWSMturkAPI/ApiReference_NotificationReceptorAPI_SNSTransportArticle.md "../AWSMturkAPI/ApiReference_NotificationReceptorAPI_SNSTransportArticle.md"). Note that in both cases, you need to
configure permissions properly to allow Mechanical Turk to send messages to your topic or queue.

**Enabling Notifications**

Notifications can be enabled for a HIT Type using the [`UpdateNotificationSettings`](../AWSMturkAPI/ApiReference_UpdateNotificationSettingsOperation.md "../AWSMturkAPI/ApiReference_UpdateNotificationSettingsOperation.md") operation. The following is an example of
a request to receive a message on an Amazon SNS topic when HITs become
_reviewable_.

```

     {
       'HITTypeId': '3AKE04YHPN13791QQA6EXAMPLE',
       'Notification': {
         'Destination': 'arn:aws:sns:us-east-1:7429088EXAMPLE:my_mturk_topic',
         'Transport': 'SNS',
         'Version': '2014-08-15',
         'EventTypes': ['HITReviewable']
       },
       'Active': True
      }
 

```

The notification data structure specifies the ARN of the destination you want to receive
the messages, specifies that the Transport is either Amazon SNS or Amazon SQS, and includes a list of
the event types about which you want to be notified. The only valid value for
`Version` is '2014-08-15'. The `Active` value indicates if the
notification should be enabled.

Because only one notification configuration can be assigned to a HIT Type, calling
`UpdateNotificationSettings` with a new value for notification replaces any
existing notifications. You can call `UpdateNotificationSettings` with just the
`HITTypeId` and a value for `Active` if you want to enable or disable
notifications on the HIT Type.

## Handling notifications using AWS Lambda

There are a wide range of approaches for using Mechanical Turk notifications, but the most common one
is to use Amazon SNS with AWS Lambda. AWS Lambda provides a straightforward way to set up code that
processes the event and attaches a trigger to kick off processing when new Amazon SNS messages are
received.

Start by creating an Amazon SNS topic you can use for Mechanical Turk notifications. The instructions in
[Notification Handling Using Amazon SNS](../AWSMturkAPI/ApiReference_NotificationReceptorAPI_SNSTransportArticle.md "../AWSMturkAPI/ApiReference_NotificationReceptorAPI_SNSTransportArticle.md") can be used to set it up and configure
permissions to allow Mechanical Turk to send messages to the topic. Then, use the following procedure to
create a lambda function to process your Amazon SNS messages.

###### To create a Lambda function to handle your Mechanical Turk events:

1. Navigate to Lambda in the AWS Console: [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Select **Create Function**.
3. Select the **Author from scratch** option.
4. Under **Function name**, provide a name for your function.
5. You can select the language runtime you wish to use; in this example we use a Python 3
   runtime.
6. You can keep the default permission configuration, which creates a new role for this
   function. If you want to use an existing role, or create a role from AWS policy templates,
   select the arrow next to **Change default execution role** to expand that
   section. Select one of the options. If you select another option, make sure that role you
   use has required permissions described in [AWS Lambda execution
   role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") in the AWS Lambda Developer Guide.

Note down the name of your execution role – you will use it in the following
procedure. 7. Select **Create function** to create the lambda function.

Next, you must add the `AmazonMechanicalTurkFullAccess` policy to the execution
role you created or used in step 6 of the preceding procedure so your Lambda function can
retrieve the results of the HIT. The following procedure assumes that you are already in the
Lambda console. If you are on the summary page for your new lambda function, you can skip the
first step.

###### To add required permissions to your Lambda execution role:

1. Select the lambda function you want to use to process Amazon SNS requests. This brings you
   to the summary page for that function. You should see the function name at the top of the
   page.
2. Select the **Permissions** tab.
3. Select the **Role name**. This redirects you to summary page for that
   role in the IAM console.
4. Choose **Attach Policies**.
5. In the search field, enter AmazonMechanicalTurkFullAccess and select the check box
   next to that policy.
6. Select **Attach policy**.

Now that you have created a lambda function with permission to process Amazon SNS notifications
send from Amazon Mechanical Turk, you can create a trigger for your Amazon SNS topic. A trigger is used to
configure the conditions under which your function is called.

The following procedure assumes you are in the Lambda console.

###### To create a lambda trigger for your Amazon SNS topic:

1. On the lambda function summary page, select the **Configuration**
   tab.
2. Choose **Add trigger** to add your Amazon SNS topic as a trigger for your
   Lambda function.
3. When prompted to select a trigger service, search for and select
   **SNS**, then select the topic you created for notifications.
4. Enter the code that you want to use to process Amazon SNS messages. The following Python
   code provides a template for getting started.

```

import json
import boto3
import xml.etree.ElementTree as ET
 
def lambda_handler(event, context):
    for record in event['Records']:
        notification = json.loads(record['Sns']['Message'])
 
        for mturk_event in notification['Events']:
            mturk = boto3.client('mturk', region_name='us-east-1')
 
            if mturk_event['EventType'] == 'HITReviewable':
                # Retrieve the answers that were provided by Workers
                response = mturk.list_assignments_for_hit(HITId=mturk_event['HITId'])
                assignments = response['Assignments']
                answers = []
                for assignment in assignments:
                    answers.append(parse_answers(assignment))
 
                # Do something with the answers
                # ...
 
# Function to parse the Answer XML object
def parse_answers(assignment):
    result = {
        'WorkerId': assignment['WorkerId'],
        'Answer': []
    }
 
    ns = {'mt': 'http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionFormAnswers.xsd'}
    root = ET.fromstring(assignment['Answer'])
 
    for a in root.findall('mt:Answer', ns):
        name = a.find('mt:QuestionIdentifier', ns).text
        value = a.find('mt:FreeText', ns).text
        result['Answer'].append({name: value})
    return result
 

```

5. After you've added the code to your Lambda function and edited it to meet your needs,
   you can select **Deploy** and begin using it.

It is recommended that you test your trigger to make sure it works as expected.

###### To test your Amazon SNS trigger on your Lambda function summary page:

1. In the **Function code** section, select the arrow next to
   **Test**.
2. Select **Configure test event**.
3. Select the **Create new test event** radio button.
4. Enter a name for your event in the text box.
5. Enter the test event. The following can be used for your test parameters after
   replacing the `HITId` with a completed HIT in your account.

```

{
  "Records": [
    {
      "Sns": {
        "Message": "{\"Events\":[{\"EventType\":\"HITReviewable\",\"`HITId`\":\"31ANT7FQN71LA48IQEXAMPLE\"}]}"
      }
    }
  ]
}

```

## Sending test events

To test the configuration of your Amazon SNS topic or Amazon SQS queue and any handlers you have in
place, you can use the [`SendTestEventNotification`](../AWSMturkAPI/ApiReference_SendTestEventNotificationOperation.md "../AWSMturkAPI/ApiReference_SendTestEventNotificationOperation.md") operation. Provide the notification
configuration you want to use and the event you would like to test.

```

{
       'Notification': {
         'Destination': 'arn:aws:sns:us-east-1:7429088EXAMPLE:my_mturk_topic',
         'Transport': 'SNS',
         'Version': '2014-08-15',
         'EventTypes': ['HITReviewable']
       },
       'TestEventType': 'HITReviewable'
}

```

## HIT references using requester

annotation

When building processes that leverage Amazon Mechanical Turk (Mechanical Turk), it's often valuable to keep track
of identifiers associated with the data in each HIT, particularly when handling HIT responses
via notifications. For example, you might want to associate your HITs with a record in a
database such as Amazon DynamoDB, and would like your HIT to reference the primary key of the
record.

The `RequesterAnnotation` attribute is a useful option for tracking these
references. When you create a HIT using `CreateHIT` or `CreateHITWithHITType`, you can provide a `RequesterAnnotation`
field that contains arbitrary data about each HIT. Although it is limited to 255 ASCII
characters, this is generally adequate to capture identifiers that denote the origin of your
data. The data provided here is only visible to the requester who created the HIT.

When you receive a notification that a HIT has been completed, you can use the
`GetHIT` operation to retrieve the `RequesterAnnotation`. The
identifier captured in the `RequesterAnnotation` can then be used to make updates
in your database or other systems.
