# Rule sets and rules

Rule sets are containers for rules that you assign to an ingress endpoint so that it can perform
actions on email allowed in from the ingress endpoint's traffic policy. A rule set can be used by
multiple ingress endpoints.

Rules tell your ingress endpoint how to handle incoming email by executing the actions
defined in the rule when messages meet the rule’s conditions. Each rule can have multiple
conditions and actions. The rules you create within a rule set are executed in the order you
specify within the rule set.

You build the rule's conditions by selecting an email property and a conditional operator
for a value you enter that must be matched by the message before the rule will execute its
actions—you define the actions to be taken as well as their order of
execution.

For greater granularity, your rules can also contain exceptions that are defined similar
to conditions, but here, you're defining a condition that the message must
_not_ match. Conditions and exceptions operate
independently—you could build a rule with just exceptions if you wanted, as well as
intermix conditions and exceptions.

Due to the fine granularity of how rules can be defined within a rule set, the following
list is provided to help illustrate the relationship of rule set components:

- Rule sets contain:

      + Rules – You can define the order in
       which the rules are executed within the rule set.


      **Rules contain:**




      	- Conditions – The rule applies
      	 if the message matches the evaluation of the condition(s); and if
      	 the rule has exceptions, see below.
      	- Exceptions – The rule applies
      	 if the message does not match the evaluation of the exception(s);
      	 and if the rule has conditions, see above.
      	- Actions – Actions are
      	 triggered when the rule applies—all of the conditions match
      	 and none of the exceptions.


      	You can define the order in which the actions are executed within
      	 the rule.

  Because each rule can have multiple conditions, exceptions, and actions, and the fact that
  you can define the order of how rules and actions are executed, this enables you to build a
  very customized and automated email handling solution tailored to your specific business
  requirements.

A rule set is an independent resource that can be used by more than one ingress endpoint, but
rules belong exclusively to the rule set in which they were created. Thus, you must first
create a rule set, or edit an existing one, before you can create rules to act upon the
email coming into your ingress endpoint.

The procedure in the next section will walk you through creating rule sets and their
rules in the SES console.

## Creating rule sets and rules in the SES

console

The following procedure shows you how to use the **Rule sets** page
in the SES console to create rule sets and their rules, and manage the ones
you've already created.

###### To create an manage rule sets and rules using the console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation panel, choose **Rule sets** under
   **Mail Manager**.
3. On the **Rule sets** page, choose **Create rule
   set** and enter a unique name for your rule set.
4. On the rule set's overview page, select **Edit** , and then
   select **Create new rule** on the edit page.
5. In the **Rule details** sidebar, enter a unique name for your
   rule.
6. Select **Add new condition** to create a condition that the
   message must match; or check the **EXCEPT in the case of:** box
   followed by **Add new exception** to create a condition that
   the message must _not_ match.
7. Build the condition or exception by selecting an email property and a
   conditional operator for the value you enter. Select **Add new
   condition** or **Add new exception** if you want
   to add more conditions or exceptions to this rule. _To learn more about
   a condition property and its operators and valid values, see the [Rule conditions](#rule-conditions "#rule-conditions")
   reference._
   - If you're subscribed to an [Email Add On](eb-addons.md "eb-addons.md"), you'll be able to select it here as an email
     property.

8. Select **Add new action** to define the action to be taken
   when the rule's conditions are matched and/or exceptions are not matched. To add
   more actions to be taken, select **Add new action**.
   _When you create two or more actions, up/down arrows are displayed
   so that you can set the order of execution._

###### Note

To execute any of these [Rule actions](#rule-actions "#rule-actions"),
you'll need to have their respective permission policy enabled for your
account; otherwise, the rule action will fail. 9. Apply the permission policy for any of these actions directly from the
**Rule details** panel after selecting the action:

    1. Choose **Create new role** in the **IAM
     role** field and enter a name followed by **Create
     role**. (The IAM trust policy for this role will
     automatically be generated in the background.)
    2. Because the IAM trust policy was automatically generated, you'll
     only need to add the action's permission policy to the
     role—select **View role** under the
     **IAM role** field to open the IAM
     console.
    3. Under the **Permissions** tab, choose **Add
     permissions** and select **Create inline
     policy**.
    4. On the **Specify permissions** page, select
     **JSON** in the **Policy
     editor**.
    5. Copy and paste the respective policy from [Permission policies for Mail Manager](eb-policies.md "eb-policies.md") into the **Policy
     editor** and replace the data in red text with your own.
     (Be sure to delete any example code in the editor.)
    6. Choose **Next**.
    7. Review and create your permission policy for the IAM role by
     choosing **Create policy**.
    8. Select your browser's tab where you have the SES Mail Manager
     **Edit rule set** page open and continue with the
     remaining steps for creating rules.

10. When you're done creating the conditions, exceptions, and actions for the
    rule, you save it to its rule set by choosing **Save rule set**
    located in the **Edit rule set** panel on the left.
11. If you want add more rules to the rule set, repeat steps 4 - 9 above.
    - When you create two or more rules, up/down arrows are displayed in the
      rule set's **Reorder** column so that you can set the
      order of execution.

12. You can view and manage the rule sets you've already created from the
    **Rule sets** page. If there's a rule set you want to
    remove, select it's radio button followed by **Delete**.
13. To edit a rule set, select its name to open its overview page, from here,
    select **Edit** where you can reorder the execution of its
    rules, add more rules by choosing **Create new rule**, or
    delete a rule by selecting it's radio button followed by
    **Delete**.
14. To edit a rule, select its radio button. In any of the containers on the
    **Rule details** sidebar, you can edit any of the
    conditions or exceptions and change or reorder any of the actions. You can also
    remove conditions, exceptions, and actions, as well as add new ones.
15. When you're done with all your edits, save your changes by selecting
    **Save rule set** located in the **Edit rule
    set** panel on the left.

## Reference for rule conditions and actions

###### Rule conditions

The following reference table lists all the rule properties that are available to
build a rule condition (or exception) and are categorized by their expression type.
Rule properties that share the same expression type also share the same operators
and values. Selecting a property's expression type will take you to its reference
page in the _SES Mail Manager API Reference_ that lists
all the available operators and valid values for that property.

| Rule conditions: Properties, operators, and values                                                                                                                                                                                                                                                                   | Property                                                                                                                                                                                                       | Expression type |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| From address<br>To address<br>CC address<br>Mail from<br>Recipient address<br>Subject<br>Helo<br>MIME header<br>Vade Advanced Email Security [(if subscribed)](eb-addons.md "eb-addons.md")<br>• Category<br>• Verdict<br>Trend Micro Virus Scanning [(if<br>subscribed)](eb-addons.md "eb-addons.md")<br>• Category | [_Valid operators and values for string<br>expressions_](../../../sesmailmanager/latest/APIReference/API_RuleStringExpression.md "../../../sesmailmanager/latest/APIReference/API_RuleStringExpression.md")    |
| IP range                                                                                                                                                                                                                                                                                                             | [_Valid operators and values for IP<br>expressions_](../../../sesmailmanager/latest/APIReference/API_RuleIpExpression.md "../../../sesmailmanager/latest/APIReference/API_RuleIpExpression.md")                |
| Message max size                                                                                                                                                                                                                                                                                                     | [_Valid operators and values for number<br>expressions_](../../../sesmailmanager/latest/APIReference/API_RuleNumberExpression.md "../../../sesmailmanager/latest/APIReference/API_RuleNumberExpression.md")    |
| DKIM<br>SPF                                                                                                                                                                                                                                                                                                          | [_Valid operators and values for verdict<br>expressions_](../../../sesmailmanager/latest/APIReference/API_RuleVerdictExpression.md "../../../sesmailmanager/latest/APIReference/API_RuleVerdictExpression.md") |
| TLS<br>TLS wrapped<br>Read receipt<br>Vade Advanced Email Security [(if subscribed)](eb-addons.md "eb-addons.md")<br>• Is passed<br>Trend Micro Virus Scanning [(if<br>subscribed)](eb-addons.md "eb-addons.md")<br>• Is passed                                                                                      | [_Valid operators and values for boolean<br>expressions_](../../../sesmailmanager/latest/APIReference/API_RuleBooleanExpression.md "../../../sesmailmanager/latest/APIReference/API_RuleBooleanExpression.md") |
| DMARC policy                                                                                                                                                                                                                                                                                                         | [_Valid operators and values for DMARC<br>expressions_](../../../sesmailmanager/latest/APIReference/API_RuleDmarcExpression.md "../../../sesmailmanager/latest/APIReference/API_RuleDmarcExpression.md")       |

###### Rule actions

The following reference table lists all the rule actions that can be taken when a
rule's conditions are met or its exceptions are not met. By selecting an action,
you'll be taken to the action's reference page in the _SES Mail
Manager API Reference_ that lists the parameters and their formats for
the action. The table uses the action names adopted in the Mail Manager console—the
API names may differ slightly.

###### Note

In some of the API references, there will be an `ActionFailurePolicy`
parameter that can be set to either _Continue_ or
_Drop_ if the action fails—this only applies when
using the API; when using the console, `ActionFailurePolicy` has been set
to the default value of _Continue_.

| Rule actions: Actions and parameters                                                                                                                                                   | Actions & their parameters                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [_Write to S3_](../../../sesmailmanager/latest/APIReference/API_S3Action.md "../../../sesmailmanager/latest/APIReference/API_S3Action.md")                                             | Writes the MIME content of the email to an S3<br>bucket.                                                                                                                                                                                                                                                                                                                                                         |
| [_SMTP relay_](../../../sesmailmanager/latest/APIReference/API_RelayAction.md "../../../sesmailmanager/latest/APIReference/API_RelayAction.md")                                        | Relays the email via SMTP to another specific SMTP server.                                                                                                                                                                                                                                                                                                                                                       |
| [_Archive_](../../../sesmailmanager/latest/APIReference/API_ArchiveAction.md "../../../sesmailmanager/latest/APIReference/API_ArchiveAction.md")                                       | Archives the email by delivering it to an Amazon SES<br>archive.                                                                                                                                                                                                                                                                                                                                                 |
| [_Add header_](../../../sesmailmanager/latest/APIReference/API_AddHeaderAction.md "../../../sesmailmanager/latest/APIReference/API_AddHeaderAction.md")                                | Adds a custom header to the received email.                                                                                                                                                                                                                                                                                                                                                                      |
| [_Email recipients<br>rewrite_](../../../sesmailmanager/latest/APIReference/API_ReplaceRecipientAction.md "../../../sesmailmanager/latest/APIReference/API_ReplaceRecipientAction.md") | Replaces the email envelope recipients with the given list of<br>recipients. If the condition of this action applies only to a subset<br>of recipients, only those recipients are replaced.                                                                                                                                                                                                                      |
| [_Deliver to WorkMail mailbox_](../../../sesmailmanager/latest/APIReference/API_DeliverToMailboxAction.md "../../../sesmailmanager/latest/APIReference/API_DeliverToMailboxAction.md") | Delivers the email to an Amazon WorkMail mailbox.                                                                                                                                                                                                                                                                                                                                                                |
| [_Deliver to Q Business_](../../../sesmailmanager/latest/APIReference/API_DeliverToQBusinessAction.md "../../../sesmailmanager/latest/APIReference/API_DeliverToQBusinessAction.md")   | Delivers an email to an Amazon Q Business application for ingestion into<br>its knowledge base.                                                                                                                                                                                                                                                                                                                  |
| [_Publish to SNS_](../../../sesmailmanager/latest/APIReference/API_SnsAction.md "../../../sesmailmanager/latest/APIReference/API_SnsAction.md")                                        | Publishes the email content to an Amazon SNS topic.                                                                                                                                                                                                                                                                                                                                                              |
| [_Send to internet_](../../../sesmailmanager/latest/APIReference/API_SendAction.md "../../../sesmailmanager/latest/APIReference/API_SendAction.md")                                    | Uses SES to send the email to the recipient(s) on the<br>email's recipient list.                                                                                                                                                                                                                                                                                                                                 |
| [_Drop_](../../../sesmailmanager/latest/APIReference/API_DropAction.md "../../../sesmailmanager/latest/APIReference/API_DropAction.md")                                                | For email with multiple recipients, if this action applies to one<br>or more (but not all) of those recipients, they will be dropped from<br>the email’s recipient list, and continued processing of rules will<br>apply to remaining recipients. If this action applies to all<br>recipient(s), rules processing stops as all recipients are dropped<br>from the recipient list and will not receive the email. |
