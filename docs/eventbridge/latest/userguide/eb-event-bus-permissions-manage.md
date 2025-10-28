# Managing event bus permissions in Amazon EventBridge

Use the following procedure to modify the permissions for an existing event bus. For
information about how to use AWS CloudFormation to create an event bus policy, see [AWS::Events::EventBusPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md").

###### To manage permissions for an existing event bus

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation pane, choose **Event buses**.
3. In **Name**, choose the name of the event bus to manage permissions
   for.

If a resource policy is attached to the event bus, the policy displays. 4. Choose **Manage permissions**, and then do one of the
following:

    * Enter the policy that includes the permissions to grant for the event bus. You can
     paste in a policy from another source, or enter the JSON for the policy.
    * To use a template for the policy, choose **Load template**.
     Modify the policy as appropriate for your environment, and add additional actions that
     you authorize the principal in the policy to use.

5. Choose **Update**.
   The template provides example policy statements that you can customize for your account
   and environment. The template isn't a valid policy. You can modify the template for your use
   case, or you can copy one of the example policies and customize it.

The template loads policies that include an example of how to grant permissions to an
account to use the `PutEvents` action, how to grant permissions to an organization,
and how to grant permissions to the account to manage rules in the account. You can customize
the template for your specific account, and then delete the other sections from the template.
More example policies are included later in this section.

If you try to update the permissions for the bus but the policy contains an error, an
error message indicates the specific issue in the policy.

```

  ### Choose which sections to include in the policy to match your use case. ###
  ### Be sure to remove all lines that start with ###, including the ### at the end of the line. ###

  ### The policy must include the following: ###

  {
    "Version": "2012-10-17",
    "Statement": [

      ### To grant permissions for an account to use the PutEvents action, include the following, otherwise delete this section: ###

      {

        "Sid": "AllowAccountToPutEvents",
        "Effect": "Allow",
        "Principal": {
          "AWS": "<ACCOUNT_ID>"
        },
        "Action": "events:PutEvents",
        "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/default"
      },

      ### Include the following section to grant permissions to all members of your AWS Organizations to use the PutEvents action ###

      {
        "Sid": "AllowAllAccountsFromOrganizationToPutEvents",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "events:PutEvents",
        "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/default",
        "Condition": {
          "StringEquals": {
            "aws:PrincipalOrgID": "o-yourOrgID"
          }
        }
      },

      ### Include the following section to grant permissions to the account to manage the rules created in the account ###

      {
        "Sid": "AllowAccountToManageRulesTheyCreated",
        "Effect": "Allow",
        "Principal": {
          "AWS": "<ACCOUNT_ID>"
        },
        "Action": [
          "events:PutRule",
          "events:PutTargets",
          "events:DeleteRule",
          "events:RemoveTargets",
          "events:DisableRule",
          "events:EnableRule",
          "events:TagResource",
          "events:UntagResource",
          "events:DescribeRule",
          "events:ListTargetsByRule",
          "events:ListTagsForResource"],
        "Resource": "arn:aws:events:us-east-1:123456789012:rule/default",
        "Condition": {
          "StringEqualsIfExists": {
            "events:creatorAccount": "<ACCOUNT_ID>"
          }
        }
    }]
  }
```
