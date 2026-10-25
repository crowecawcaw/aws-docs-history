

# Creating rules that send events to an API destination in EventBridge
<a name="eb-create-rule-api-destination-target"></a>

You can use an API destination as the target of a [rule](eb-rules.md). First, create the API destination. Then choose it as the target when you create the rule. You also need an IAM role with the correct permissions. For more information, see [Permissions to access targets](eb-events-iam-roles.md#eb-target-permissions).

You set the target as part of the rule.

**To create a rule that sends events to an API destination using the console**

1. Follow the steps in the [Creating rules using the Enhanced Builder](eb-create-rule-visual.md) procedure.

1. In the [Select targets](eb-create-rule-wizard.md#eb-create-rule-target) step, choose an API destination as the target type. Then do the following:

   1. Select **EventBridge API destination**.

   1. Do one of the following:
      + Choose **Use an existing API destination**. Then select the one you want.
      + Choose **Create a new API destination**. Then set up the new one.

        For more information, see [Create an API destination in Amazon EventBridge](eb-api-destination-create.md).

   1. (Optional) To add header values, under **Header Parameters** choose **Add header parameter**. Then enter a key and a value.

   1. (Optional) To add query string values, under **Query string parameters** choose **Add query string parameter**. Then enter a key and a value.

1. To finish, follow the rest of the [steps](eb-create-rule-visual.md).