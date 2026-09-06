

# Rule sets and rules
<a name="eb-rules"></a>

Rule sets are containers for rules that you assign to an ingress endpoint so that it can perform actions on email allowed in from the ingress endpoint's traffic policy. A rule set can be used by multiple ingress endpoints.

Rules tell your ingress endpoint how to handle incoming email by executing the actions defined in the rule when messages meet the rule’s conditions. Each rule can have multiple conditions and actions. The rules you create within a rule set are executed in the order you specify within the rule set.

You build the rule's conditions by selecting an email property and a conditional operator for a value you enter that must be matched by the message before the rule will execute its actions—you define the actions to be taken as well as their order of execution.

For greater granularity, your rules can also contain exceptions that are defined similar to conditions, but here, you're defining a condition that the message must *not* match. Conditions and exceptions operate independently—you could build a rule with just exceptions if you wanted, as well as intermix conditions and exceptions.

Due to the fine granularity of how rules can be defined within a rule set, the following list is provided to help illustrate the relationship of rule set components:
+ **Rule sets contain:**
  + **Rules** – You can define the order in which the rules are executed within the rule set.

    **Rules contain:**
    + **Conditions** – The rule applies if the message matches the evaluation of the condition(s); and if the rule has exceptions, see below.
    + **Exceptions** – The rule applies if the message does not match the evaluation of the exception(s); and if the rule has conditions, see above.
    + **Actions** – Actions are triggered when the rule applies—all of the conditions match and none of the exceptions.

      You can define the order in which the actions are executed within the rule.

Because each rule can have multiple conditions, exceptions, and actions, and the fact that you can define the order of how rules and actions are executed, this enables you to build a very customized and automated email handling solution tailored to your specific business requirements.

A rule set is an independent resource that can be used by more than one ingress endpoint, but rules belong exclusively to the rule set in which they were created. Thus, you must first create a rule set, or edit an existing one, before you can create rules to act upon the email coming into your ingress endpoint.

 The procedure in the next section will walk you through creating rule sets and their rules in the SES console.

## Creating rule sets and rules in the SES console
<a name="eb-rules-create-console"></a>

The following procedure shows you how to use the **Rule sets** page in the SES console to create rule sets and their rules, and manage the ones you've already created.

**To create an manage rule sets and rules using the console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation panel, choose **Rule sets** under **Mail Manager**.

1. On the **Rule sets** page, choose **Create rule set** and enter a unique name for your rule set.

1. On the rule set's overview page, select **Edit **, and then select **Create new rule** on the edit page.

1. In the **Rule details** sidebar, enter a unique name for your rule.

1. Select **Add new condition** to create a condition that the message must match; or check the **EXCEPT in the case of:** box followed by **Add new exception** to create a condition that the message must *not* match.

1. Build the condition or exception by selecting an email property and a conditional operator for the value you enter. Select **Add new condition** or **Add new exception** if you want to add more conditions or exceptions to this rule. *To learn more about a condition property and its operators and valid values, see the [Rule conditions](#rule-conditions) reference.*
   + If you're subscribed to an [Email Add On](eb-addons.md), you'll be able to select it here as an email property.

1. Select **Add new action** to define the action to be taken when the rule's conditions are matched and/or exceptions are not matched. To add more actions to be taken, select **Add new action**. *When you create two or more actions, up/down arrows are displayed so that you can set the order of execution.* 
**Note**  
To execute any of these [Rule actions](#rule-actions), you'll need to have their respective permission policy enabled for your account; otherwise, the rule action will fail. 

1. Apply the permission policy for any of these actions directly from the **Rule details** panel after selecting the action:

   1. Choose **Create new role** in the **IAM role** field and enter a name followed by **Create role**. (The IAM trust policy for this role will automatically be generated in the background.)

   1. Because the IAM trust policy was automatically generated, you'll only need to add the action's permission policy to the role—select** View role** under the **IAM role** field to open the IAM console.

   1. Under the **Permissions** tab, choose **Add permissions** and select **Create inline policy**.

   1. On the **Specify permissions** page, select **JSON** in the **Policy editor**.

   1. Copy and paste the respective policy from [Permission policies for Mail Manager](eb-policies.md) into the **Policy editor** and replace the data in red text with your own. (Be sure to delete any example code in the editor.)

   1. Choose **Next**.

   1. Review and create your permission policy for the IAM role by choosing **Create policy**.

   1. Select your browser's tab where you have the SES Mail Manager **Edit rule set** page open and continue with the remaining steps for creating rules.

1. When you're done creating the conditions, exceptions, and actions for the rule, you save it to its rule set by choosing **Save rule set** located in the **Edit rule set** panel on the left.

1. If you want add more rules to the rule set, repeat steps 4 - 9 above.
   + When you create two or more rules, up/down arrows are displayed in the rule set's **Reorder** column so that you can set the order of execution.

1. You can view and manage the rule sets you've already created from the **Rule sets** page. If there's a rule set you want to remove, select it's radio button followed by **Delete**.

1. To edit a rule set, select its name to open its overview page, from here, select **Edit** where you can reorder the execution of its rules, add more rules by choosing **Create new rule**, or delete a rule by selecting it's radio button followed by **Delete**.

1. To edit a rule, select its radio button. In any of the containers on the **Rule details** sidebar, you can edit any of the conditions or exceptions and change or reorder any of the actions. You can also remove conditions, exceptions, and actions, as well as add new ones.

1. When you're done with all your edits, save your changes by selecting **Save rule set** located in the **Edit rule set** panel on the left.

## Reference for rule conditions and actions
<a name="eb-rules-reference"></a>

**Rule conditions**  
The following reference table lists all the rule properties that are available to build a rule condition (or exception) and are categorized by their expression type. Rule properties that share the same expression type also share the same operators and values. Selecting a property's expression type will take you to its reference page in the *SES Mail Manager API Reference* that lists all the available operators and valid values for that property.


**Rule conditions: Properties, operators, and values**  

| Property | Expression type | 
| --- | --- | 
| From address<br />To address<br />CC address<br />Mail from<br />Recipient address<br />Subject<br />Helo<br />MIME header<br />Client certificate attribute *(mTLS ingress endpoints only)*+  Serial number <br />+  Common name <br />+  Country <br />+  Locality <br />+  Organization <br />+  Organizational unit <br />+  State <br />+  Subject alternative name <br />Vade Advanced Email Security [*(if subscribed)*](eb-addons.md)+  Category <br />+  Verdict <br />Trend Micro Virus Scanning [*(if subscribed)*](eb-addons.md)+  Category  | [*Valid operators and values for string expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) | 
| IP range | [*Valid operators and values for IP expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleIpExpression.html) | 
| Message max size | [*Valid operators and values for number expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleNumberExpression.html) | 
| DKIM<br />SPF | [*Valid operators and values for verdict expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleVerdictExpression.html) | 
| TLS<br />TLS wrapped<br />Read receipt<br />Vade Advanced Email Security [*(if subscribed)*](eb-addons.md)+  Is passed <br />Trend Micro Virus Scanning [*(if subscribed)*](eb-addons.md)+  Is passed  | [*Valid operators and values for boolean expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleBooleanExpression.html) | 
| DMARC policy | [*Valid operators and values for DMARC expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleDmarcExpression.html) | 

**Recipient address matching and subaddressing**  
The *Recipient address* property uses the full SMTP envelope recipient address exactly as received, including any subaddress extension (also known as "plus addressing"). For example, if a message is sent to `user+tag@example.com`, the recipient address evaluated in the rule condition is `user+tag@example.com`, not `user@example.com`.  
This means that an `EQUALS` or `CONTAINS` rule targeting `user@example.com` will not match `user+tag@example.com`. If you need to match all subaddressed variants of an address, consider using an address list with wildcard entries (e.g., `user*@example.com`). Alternatively, `ENDS_WITH` with the domain (e.g., `@example.com`) can be used for broader domain-level matching.

**Rule actions**  
The following reference table lists all the rule actions that can be taken when a rule's conditions are met or its exceptions are not met. By selecting an action, you'll be taken to the action's reference page in the *SES Mail Manager API Reference* that lists the parameters and their formats for the action. The table uses the action names adopted in the Mail Manager console—the API names may differ slightly.

**Note**  
In some of the API references, there will be an `ActionFailurePolicy` parameter that can be set to either *Continue* or *Drop* if the action fails—this only applies when using the API; when using the console, `ActionFailurePolicy` has been set to the default value of *Continue*.


**Rule actions: Actions and parameters**  

| Actions & their parameters | Description | 
| --- | --- | 
| [*Write to S3*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_S3Action.html) | Writes the MIME content of the email to an S3 bucket. | 
| [*SMTP relay*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RelayAction.html) | Relays the email via SMTP to another specific SMTP server. | 
| [*Archive*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveAction.html) | Archives the email by delivering it to an Amazon SES archive. | 
| [*Add header*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddHeaderAction.html) | Adds a custom header to the received email. | 
| [*Email recipients rewrite*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ReplaceRecipientAction.html) | Replaces the email envelope recipients with the given list of recipients. If the condition of this action applies only to a subset of recipients, only those recipients are replaced. | 
| [*Deliver to WorkMail mailbox*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeliverToMailboxAction.html) | Delivers the email to an Amazon WorkMail mailbox. | 
| [*Deliver to Q Business*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeliverToQBusinessAction.html) | Delivers an email to an Amazon Q Business application for ingestion into its knowledge base. | 
| [*Publish to SNS*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_SnsAction.html) | Publishes the email content to an Amazon SNS topic. | 
| [*Send to internet*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_SendAction.html) | Uses SES to send the email to the recipient(s) on the email's recipient list. | 
| [*Bounce*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_BounceAction.html) | Bounces the email by returning a bounce response to the sender. | 
| [*Invoke Lambda function*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_InvokeLambdaAction.html) | Invokes an AWS Lambda function to process the email. The Lambda payload format is the same as Amazon SES Email Receiving, as described in [Notification contents](receiving-email-notifications-contents.md). For more information, see [Use case examples](receiving-email-action-lambda-example-use-cases.md). For code examples, see [Lambda function examples](receiving-email-action-lambda-example-functions.md). | 
| [*Drop*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DropAction.html) | For email with multiple recipients, if this action applies to one or more (but not all) of those recipients, they will be dropped from the email’s recipient list, and continued processing of rules will apply to remaining recipients. If this action applies to all recipient(s), rules processing stops as all recipients are dropped from the recipient list and will not receive the email. | 