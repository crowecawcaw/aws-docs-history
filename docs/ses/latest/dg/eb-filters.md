

# Traffic policies and policy statements
<a name="eb-filters"></a>

A traffic policy is a container for policy statements that you assign to an ingress endpoint so that it can sort the incoming mail by allowing or blocking specific types of email when the conditions of the policy statements are met. A traffic policy can be used by multiple ingress endpoints.

**Tip**  
You can think of a traffic policy as a "filter set", and a policy statement as a "filter". The traffic policy (filter set) contains polices (filters) that you use to *filter* your incoming mail.

When you create a traffic policy, you have the option to set a maximum message size (in bytes). When a message exceeds that size, it is discarded. You can also set the default action of the policy to allow or block email that falls outside of the conditions of your policy statements—think of this as a “catch all” action for the traffic policy.

Policy statements are also created with either an allow or block action that is taken when the statements' conditions are met. You build the conditions by selecting an email property and a conditional operator for a value you enter that must be matched by the incoming message before the policy statement will allow or block it. Each policy statement can have multiple conditions. 

A traffic policy can contain multiple policy statements and executes them in an order that's based on the implicit hierarchy of how it evaluates email:
+ **Policy statements that block** – These statements are evaluated first and block any message that meets the statement's conditions.
+ **Policy statements that allow** – These statements are evaluated next and allow any message that meets the statement's conditions.
+ **Default action of traffic policy** – The remainder of messages that fall outside of the policy statements are allowed or blocked based on how you've defined this parameter.
+ **Maximum message size** – If this optional parameter is set, any message greater than this size is discarded.

A traffic policy is an independent resource which can be used by more than one ingress endpoint, but policy statements belong exclusively to the traffic policy in which they were created. Thus, you must first create a traffic policy, or edit an existing one, before you can create policy statements to evaluate the email coming into your ingress endpoint.

 The procedure in the next section explains how to create traffic policies and their policy statements in the SES console.

## Creating traffic policies and policy statements in the SES console
<a name="eb-filters-create-console"></a>

The following procedure shows you how to use the **Traffic policies** page in the SES console to create traffic policies and their policy statements, and manage the ones you've already created.

**To create and manage traffic policies and policy statements using the console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation panel, choose **Traffic policies** under **Mail Manager**.

1. On the **Traffic policies** page, select **Create traffic policy**.

1. On the **Create a traffic policy** page, enter a unique name for your traffic policy.

1. (Optional) If you want to discard any messages above a certain size, enter a value in bytes in the **Maximum message size** field.

1. In **Default action**, choose whether the traffic policy is to either **Allow** or **Deny** (block) messages that fall outside of (are not addressed by) the conditions of your policy statements.

1. Select **Add new policy statement** to create a statement for your traffic policy.

1. Choose either **Allow** or **Deny** (block) for the action to be taken when the statement's conditions are met.

1. Build a condition by selecting an email property and a conditional operator for the value you enter. Select **Add new condition** if you want to add more conditions to this policy statement. *To learn more about a condition property and its operators and valid values, see the [Policy statement conditions](#filter-conditions) reference.*
   + If you're subscribed to an [Email Add On](eb-addons.md), you'll be able to select it here as an email property.
   + Traffic policies associated with IPv6 or dual-stack ingress endpoints will not evaluate nor apply Email Add On conditions to messages received through IPv6 connections. Email Add On conditions will only apply to messages received through IPv4 connections on dual-stack endpoints.

1. If you want add more policy statements and conditions, repeat steps 7 - 9 above. 

1. When you're done creating policy statements and their conditions, select **Create traffic policy**.

1. You can view and manage the traffic policies you've already created from the **Traffic policies** page. If there's an traffic policy you want to remove, select it's radio button followed by **Delete**.

1. To edit a traffic policy's properties or any of its policy statements, select its name to open its overview page, from here, select **Edit**.

1. In **Traffic policy details**, you can change the maximum message size and default action.

1. In any of the **Policy statement** containers, you can change the allow/deny property and edit any of the conditions. You can also remove policy statements and conditions, as well as add new ones.

1. When you're done with all your edits, save your changes by selecting **Save changes**.

## Reference for policy statement conditions
<a name="eb-filters-reference"></a>

**Policy statement conditions**  
The following reference table lists all the policy statement properties that are available to build a policy statement condition. Selecting a property's expression type will take you to its reference page in the *SES Mail Manager API Reference* that lists all the available operators and valid values for that property.


**Policy statement conditions: Properties, operators, and values**  

| Property | Expression type | 
| --- | --- | 
| Recipient address<br />Abusix Mail Intelligence [*(if subscribed)*](eb-addons.md)+  Listed on <br />Spamhaus Domain Block List [*(if subscribed)*](eb-addons.md)+  Listed on  | [*Valid operators and values for string expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressStringExpression.html) | 
| Sender IP range | [*Valid operators and values for IP expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressIpv4Expression.html) | 
| TLS protocol version | [*Valid operators and values for TLS protocol expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressTlsProtocolExpression.html) | 
| Abusix Mail Intelligence [*(if subscribed)*](eb-addons.md)+  Is listed <br />Spamhaus Domain Block List [*(if subscribed)*](eb-addons.md)+  Is listed  | [*Valid operators and values for boolean expressions*](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressBooleanExpression.html) | 

**Recipient address matching and subaddressing**  
The *Recipient address* property uses the full SMTP envelope recipient address exactly as received, including any subaddress extension (also known as "plus addressing"). For example, if a message is sent to `user+tag@example.com`, the recipient address evaluated in the policy statement is `user+tag@example.com`, not `user@example.com`.  
This means that an `EQUALS` or `CONTAINS` rule targeting `user@example.com` will not match `user+tag@example.com`. If you need to match all subaddressed variants of an address, consider using an address list with wildcard entries (e.g., `user*@example.com`). Alternatively, `ENDS_WITH` with the domain (e.g., `@example.com`) can be used for broader domain-level matching.