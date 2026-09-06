

# Use EventBridge with Image Builder pipelines
<a name="ev-rules-for-pipeline"></a>

AWS and partner services stream events to Amazon EventBridge event buses in near real time. You can also send your own custom events. Event buses use rules to route each event to one or more targets.

Image Builder works with EventBridge in two independent directions:
+ **Start a pipeline build from a rule.** You can set an Image Builder pipeline as a rule target, so EventBridge runs the pipeline when an event matches the rule or when a schedule fires. See [Trigger a pipeline build on a schedule](#ev-rules-schedule-pipeline) and [Trigger a pipeline build from an event pattern](#ev-trigger-pipeline-pattern).
+ **React to events that Image Builder sends.** Image Builder publishes events to the default event bus when significant changes occur—for example, when an image becomes `AVAILABLE` or a scan detects CVEs. You can match these events with a rule and route them to targets such as a Lambda function or an Amazon SNS topic to start your own automations. See [React to events that Image Builder sends](#ev-create-reaction-rule).

For more information about the events that Image Builder sends and the fields in each event, see [Event messages that Image Builder sends](integ-eventbridge.md#integ-eb-event-summary).

**Note**  
Event buses are Region-specific. A rule and the resources it invokes are typically in the same Region; to route across Regions, target an event bus in the destination Region. Image Builder publishes its events to the default event bus in the Region where the build runs.

**Topics**
+ [EventBridge terms](#ev-terms)
+ [View EventBridge rules for your Image Builder pipeline](#ev-rules-pipeline-tab)
+ [Trigger a pipeline build on a schedule](#ev-rules-schedule-pipeline)
+ [Trigger a pipeline build from an event pattern](#ev-trigger-pipeline-pattern)
+ [React to events that Image Builder sends](#ev-create-reaction-rule)

## EventBridge terms
<a name="ev-terms"></a>

The following terms help you understand how EventBridge integrates with your Image Builder pipelines.

Event  
Describes a change in an environment that might affect one or more application resources. The environment can be an AWS environment, a SaaS partner service or application, or one of your applications or services. You can also set up scheduled events on a timeline.

Event bus  
A pipeline that receives event data from applications and services.

Source  
The service or application that sent the event to the event bus.

Target  
A resource or endpoint that EventBridge invokes when it matches a rule, delivering data from the event to the target.

Rule  
A rule matches incoming events and sends them to targets for processing. A single rule can send an event to multiple targets, which can then run in parallel. Rules are based either on an event pattern or a schedule.

Pattern  
An event pattern defines the event structure and the fields that a rule matches in order to initiate the target action.

Schedule  
Schedule rules perform an action on a schedule, such as running an Image Builder pipeline to refresh an image on a quarterly basis. There are two types of schedule expressions:   
+ **Cron expressions** – Match specific scheduling criteria using the cron syntax that can outline simple criteria; for example, running weekly on a specific day. You can also establish more complex criteria, such as running quarterly on the fifth day of the month, between 2 AM and 4 AM.
+ **Rate expressions** – Specify a regular interval when the target is invoked, such as every 12 hours.

## View EventBridge rules for your Image Builder pipeline
<a name="ev-rules-pipeline-tab"></a>

The **EventBridge rules** tab in the Image Builder **Image pipelines** detail page displays EventBridge event buses that your account has access to, and the rules for the selected event bus that apply to the current pipeline. This tab also links directly to the EventBridge console for creating new resources.

**Actions that link to the EventBridge console**
+ **Create event bus**
+ **Create rule**

To learn more about EventBridge, see the following topics in the *Amazon EventBridge User Guide*.
+ [What is Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
+ [Amazon EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
+ [Amazon EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html)
+ [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)

## Trigger a pipeline build on a schedule
<a name="ev-rules-schedule-pipeline"></a>

Set an Image Builder pipeline as the target of an EventBridge schedule rule to refresh an image on a regular cadence. The following example creates a rule that starts a pipeline build every 90 days.

**Note**  
A pipeline can also carry its own built-in **schedule** (a cron or rate expression stored on the pipeline). That schedule is managed by Image Builder and is separate from any EventBridge rule:  
Use the **pipeline schedule** for a simple recurring rebuild. It can also gate builds on dependency updates and auto-disable a failing pipeline. See `Schedule` in the *EC2 Image Builder API Reference*.
Use an **EventBridge rule** to start a build from an event pattern, or to fan one trigger out to multiple targets.

------
#### [ AWS Management Console ]

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. To see a list of the image pipelines created under your account, choose **Image pipelines** from the navigation pane.
**Note**  
The list of image pipelines includes an indicator for the type of output image that is created by the pipeline – AMI or Docker.

1. To view details or edit a pipeline, choose the **Pipeline name** link. This opens the detail view for the pipeline.
**Note**  
You can also select the check box next to the **Pipeline name**, then choose **View detail**.

1. Open the **EventBridge rules** tab.

1. Keep the default event bus that is pre-selected in the **Event Bus** panel.

1. Choose **Create rule**. This takes you to the **Create rule** page in the Amazon EventBridge console.

1. Enter a name and description for the rule. The rule name must be unique within the event bus for the selected Region.

1. In the **Define pattern** panel, choose the **Schedule** option. This expands the panel, with the **Fixed rate every** option selected.

1. Enter `90` in the first box, and select **Days** from the drop-down list.

1. Perform the following actions in the **Select targets** panel:

   1. Select `EC2 Image Builder` from the **Target** drop-down list.

   1. To apply the rule to an Image Builder pipeline, select the target pipeline from the **Image Pipeline** drop-down list.

   1. EventBridge needs permission to initiate a build for the selected pipeline. For this example, keep the default option to **Create a new role for this specific resource**.

   1. Choose **Add target**.

1. Choose **Create**

**Note**  
The current EventBridge console may create schedules through EventBridge Scheduler, and the exact labels and steps can change over time. The linked *Amazon EventBridge User Guide* is authoritative for the current console experience.

------
#### [ AWS CLI ]

These steps create a schedule rule that starts a pipeline build every 90 days. EventBridge needs an IAM role that it can assume to call `imagebuilder:StartImagePipelineExecution` on your pipeline.

1. Create a rule with a rate expression:

   ```
   aws events put-rule \
     --name refresh-image-every-90-days \
     --schedule-expression "rate(90 days)"
   ```

1. Create an IAM role that EventBridge can assume, with this trust policy:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [{
           "Effect": "Allow",
           "Principal": { "Service": "events.amazonaws.com" },
           "Action": "sts:AssumeRole"
       }]
   }
   ```

   Attach a permissions policy that allows the pipeline to start:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [{
           "Effect": "Allow",
           "Action": "imagebuilder:StartImagePipelineExecution",
           "Resource": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-pipeline/{{my-pipeline}}"
       }]
   }
   ```

1. Add the pipeline as the rule's target, referencing the role from the previous step:

   ```
   aws events put-targets \
     --rule refresh-image-every-90-days \
     --targets '[{
       "Id": "1",
       "Arn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-pipeline/{{my-pipeline}}",
       "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{EventBridgeImageBuilderRole}}"
     }]'
   ```

1. Confirm the target is attached:

   ```
   aws events list-targets-by-rule --rule refresh-image-every-90-days
   ```

------

**Note**  
To learn more about settings for rate expression rules that are not covered in this example, see [Rate expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-rate-expressions) in the *Amazon EventBridge User Guide*.

## Trigger a pipeline build from an event pattern
<a name="ev-trigger-pipeline-pattern"></a>

Instead of a schedule, you can start a pipeline build when an event matches a pattern. Create a rule with an event pattern, then add your pipeline as the target (with the same IAM role described in [Trigger a pipeline build on a schedule](#ev-rules-schedule-pipeline)).

The following example starts a build whenever a specific base image becomes `AVAILABLE`—for example, to chain a dependent image build after its base image finishes. The `resources` prefix scopes the rule to the base image so that it matches only that image, and not the dependent pipeline's own output:

```
{
    "source": ["aws.imagebuilder"],
    "detail-type": ["EC2 Image Builder Image State Change"],
    "detail": {
        "state": { "status": ["AVAILABLE"] }
    },
    "resources": [{
        "prefix": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image/{{my-base-image}}/"
    }]
}
```

**Important**  
Scope the event pattern to the base image, as shown by the `resources` prefix in this example. A pattern that matches every `AVAILABLE` image in the account also matches the dependent pipeline's own output image, which starts the pipeline again and can create an endless build loop. Filter on the specific base image name or ARN prefix so the rule matches only the image you intend.

------
#### [ AWS Management Console ]

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose **Rules**, then **Create rule**. Keep the **default** event bus.

1. Enter a name and description. Under **Rule type**, choose **Rule with an event pattern**.

1. For the event source, choose **Other**, and paste the event pattern above into the **Event pattern** box.

1. In the **Select targets** panel, choose `EC2 Image Builder` from the **Target** drop-down list, then choose the pipeline to build from the **Image Pipeline** drop-down list.

1. EventBridge needs permission to start the pipeline. Keep the default option to **Create a new role for this specific resource**.

1. Choose **Create rule**.

------
#### [ AWS CLI ]

Create the rule and add the pipeline as the target:

```
aws events put-rule \
  --name rebuild-on-base-available \
  --event-pattern '{"source":["aws.imagebuilder"],"detail-type":["EC2 Image Builder Image State Change"],"detail":{"state":{"status":["AVAILABLE"]}},"resources":[{"prefix":"arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image/{{my-base-image}}/"}]}'

aws events put-targets \
  --rule rebuild-on-base-available \
  --targets '[{"Id":"1","Arn":"arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-pipeline/{{dependent-pipeline}}","RoleArn":"arn:aws:iam::{{111122223333}}:role/{{EventBridgeImageBuilderRole}}"}]'
```

------

For the events you can match and their fields, see [Event messages that Image Builder sends](integ-eventbridge.md#integ-eb-event-summary).

## React to events that Image Builder sends
<a name="ev-create-reaction-rule"></a>

Image Builder publishes events to the default event bus when your resources reach significant points—for example, when an image changes state, a scan completes, a workflow step pauses for input, or a pipeline is automatically disabled. You can match these events with a rule and route them to a target to start your own automation. Common patterns include:
+ Notify a team through an Amazon SNS topic when an image becomes `AVAILABLE` or `FAILED`.
+ Invoke a Lambda function to register a new AMI in a parameter store, start external compliance tests, or update a deployment pipeline.
+ Alert on security findings when a scan reports critical CVEs.
+ Drive an approval workflow when a `WaitForAction` workflow step pauses a build.

To act on an event that Image Builder sends, create a rule whose event pattern matches the event `source` (`aws.imagebuilder`) and `detail-type`, and optionally narrows on fields inside `detail`. Then add the target that runs your automation.

**Example: Notify on image completion (`AVAILABLE` or `FAILED`)**

```
{
    "source": ["aws.imagebuilder"],
    "detail-type": ["EC2 Image Builder Image State Change"],
    "detail": {
        "state": { "status": ["AVAILABLE", "FAILED"] }
    }
}
```

**Example: Alert only when a scan finds critical CVEs**

Use a numeric matcher so that clean scans don't trigger the rule:

```
{
    "source": ["aws.imagebuilder"],
    "detail-type": ["EC2 Image Builder CVE Detected"],
    "detail": {
        "finding-severity-counts": {
            "critical": [{ "numeric": [">", 0] }]
        }
    }
}
```

------
#### [ AWS Management Console ]

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose **Rules**, then **Create rule**. Keep the **default** event bus.

1. Enter a name and description. Under **Rule type**, choose **Rule with an event pattern**.

1. For the event source, choose **Other**, and paste one of the event patterns above into the **Event pattern** box.

1. Choose your target—for example, an Amazon SNS topic or a Lambda function—and complete the target settings.

1. Choose **Create rule**.

------
#### [ AWS CLI ]

Create the rule and send matching events to an Amazon SNS topic:

```
aws events put-rule \
  --name image-available-or-failed \
  --event-pattern '{"source":["aws.imagebuilder"],"detail-type":["EC2 Image Builder Image State Change"],"detail":{"state":{"status":["AVAILABLE","FAILED"]}}}'

aws events put-targets \
  --rule image-available-or-failed \
  --targets '[{"Id":"1","Arn":"arn:aws:sns:{{us-west-2}}:{{111122223333}}:{{image-status}}"}]'
```

EventBridge also needs permission to send events to your target. For more information about the permissions that each target type requires, see [Permissions for sending events to targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html#targets-permissions) and [Using resource-based policies for Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html) in the *Amazon EventBridge User Guide*.

------

**Note**  
When you match the `EC2 Image Builder Workflow Step Waiting` event, your target can call `SendWorkflowStepAction` with the `workflow-step-execution-id` from the event and an `action` of `RESUME` or `STOP`. See [WaitForAction](wfdoc-step-actions.md#wfdoc-step-action-waitfor).