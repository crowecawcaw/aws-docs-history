# Configuring an input transformer when creating a rule in EventBridge

As part of creating a rule, you can specify an input transformer for EventBridge
to use to process matching events prior to sending those event to the specified target.
You can configure input transformers for targets that are AWS services or API destinations.

###### To create a target input transformer as part of a rule

1. Follow the steps for creating a rule as detailed in [Creating rules that react to events in Amazon EventBridge](eb-create-rule.md "eb-create-rule.md").
2. In **Step 3 - Select target(s)**, expand **Additional settings**.
3. For **Configure target input**, choose **Input transformer** in the dropdown.

Click **Configure input transformer**.

EventBridge displays the **Configure input transformer** dialog box. 4. In the **Sample event** section, choose a
**Sample event type** against which you want to test your event pattern. You can choose an AWS event,
a partner event, or enter your own custom event.

AWS events
Select from events emitted from supported AWS services.

    1. Select **AWS events**.
    2. Under **Sample events**, choose the desired AWS event. Events are organized by AWS service.


    When you select an event, EventBridge populates the sample event.


    For example, if you choose **S3 Object Created**, EventBridge displays a sample S3 Object Created event.
    3. (Optional) You can also select **Copy** to copy the sample event to your device's clipboard.

Partner events
Select from events emitted from third-party services that support EventBridge, such as Salesforce.

    1. Select **EventBridge partner events**.
    2. Under **Sample events**, choose the desired partner event. Events are organized by partner.


    When you select an event, EventBridge populates the sample event.
    3. (Optional) You can also select **Copy** to copy the sample event to your device's clipboard.

Enter your own
Enter your own event in JSON text.

    1. Select **Enter your own**.
    2. EventBridge populates the sample event with a template of required event attributes.
    3. Edit and add to the sample event as desired. The sample event must be valid JSON.
    4. (Optional) You can also choose any of the following options:




    	* **Copy** – Copy the sample event to your device's clipboard.
    	* **Prettify** – Makes the
    	 JSON text easier to read by adding line breaks,
    	 tabs, and spaces.

5.  (Optional) Expand the **Example input paths, Templates and Outputs** section to see examples of:

        * How JSON paths are used to define variables that represent event data
        * How those variables can be used in an input transformer template
        * The resulting output that EventBridge sends to the target

    For more detailed examples of input transformations, see [Input transform examples](eb-transform-target-input.md#eb-transform-input-examples "eb-transform-target-input.md#eb-transform-input-examples").

6.  In the **Target input transformer** section, define any variables you want to use in the input template.

Variables use JSON path to reference values in the original event source.
You can then reference those variables in the input template in order to include data from the original source event in the transformed event
that EventBridge passes to the target. You can define up to 100 variables. The input transformer must be valid JSON.

For example, suppose you had chosen AWS event **S3 Object Created** as your sample event for this input transformer.
You could then define the following variables for use in your template:

```
{
  "requester": "$.detail.requester",
  "key": "$.detail.object.key",
  "bucket": "$.detail.bucket.name"
}
```

(Optional) You can also choose **Copy** to copy the input transformer to your device's clipboard. 7. In the **Template** section, compose the template you want to use to determine what EventBridge passes to the target.

You can use JSON, strings, static information, variables you've defined as well as reserved variables.
For more detailed examples of input transformations, see [Input transform examples](eb-transform-target-input.md#eb-transform-input-examples "eb-transform-target-input.md#eb-transform-input-examples").

For example, suppose you had defined the variables in the previous example. You could then compose the following template,
which references those variables, as well as reserved variables, and static information.

```
{
    "message": "<requester> has created the object \"<key>\" in the bucket \"<bucket>\"",
    "RuleName": <aws.events.rule-name>,
    "ruleArn" : <aws.events.rule-arn>,
    "Transformed": "Yes"
}
```

(Optional) You can also choose **Copy** to copy the template to your device's clipboard. 8. To test your template, select **Generate output**.

EventBridge processes the sample event based on the input template, and displays the
transformed output generated under **Output**. This is the
information that EventBridge will pass to the target in place of the original source
event.

The generated output for the example input template described above would be the
following:

```
{
    "message": "123456789012 has created the object "example-key" in the bucket "amzn-s3-demo-bucket"",
    "RuleName": rule-name,
    "ruleArn" : arn:aws:events:us-east-1:123456789012:rule/rule-name,
    "Transformed": "Yes"
}
```

(Optional) You can also choose **Copy** to copy the generated
output to your device's clipboard. 9. Select **Confirm** 10. Follow the rest of the steps for creating a rule as detailed in [Creating rules that react to events in Amazon EventBridge](eb-create-rule.md "eb-create-rule.md").
