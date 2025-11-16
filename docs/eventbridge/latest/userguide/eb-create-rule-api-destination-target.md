# Creating rules that send events

to an API destination in EventBridge

After you create an API destination, you can select it as the target of a [rule](eb-rules.md "eb-rules.md"). To use an API destination as a target, you must
provide an IAM role with the correct permissions. For more information, see [Permissions required for EventBridge to access targets using IAM roles](eb-events-iam-roles.md#eb-target-permissions "eb-events-iam-roles.md#eb-target-permissions")

Selecting an API destination as a target is part of creating the rule.

###### To create a rule that sends events to an API destination using the

console

1. Follow the steps in the [Creating rules in Amazon EventBridge](eb-create-rule-visual.md "eb-create-rule-visual.md") procedure.
2. In the [Select targets](eb-create-rule-wizard.md#eb-create-rule-target "eb-create-rule-wizard.md#eb-create-rule-target") step, when prompted to choose
   an API destination as the target type:
   1. Select **EventBridge API destination**.
   2. Do one of the following:
      - Choose **Use an existing API destination**
        and select an existing API destination
      - Choose **Create a new API destination** and
        specify the necessary setting to define your new API
        destination.

      For more information on specifying the required settings, see
      [Create an API destination in Amazon EventBridge](eb-api-destination-create.md "eb-api-destination-create.md").

   3. (Optional): To specify header parameters for the event, under
      **Header Parameters** choose **Add header
      parameter**.

   Next, specify the key and value for the header parameter. 4. (Optional): To specify query string parameters for the event, under
   **Query string parameters** choose **Add
   query string parameter**.

   Next, specify the key and value for the query string parameter.

3. Complete creating the rule following the [procedure steps](eb-create-rule-visual.md "eb-create-rule-visual.md").
