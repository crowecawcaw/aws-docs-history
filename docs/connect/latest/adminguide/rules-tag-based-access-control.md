

# Granular access controls on rules
<a name="rules-tag-based-access-control"></a>

With granular access controls on rules, you can:
+ Restrict users from accessing the rules of another business line or function.
+ Control the scope of a rule, so that the rule doesn't apply to resources that the user doesn't have access to.
+ Show users only the rule-based contact categories that are relevant to them, on contacts and in analytics dashboards.

You can add tags to rules, for example `Department:Sales`. Then give users access to only the relevant rule tags in their security profiles. For example, a sales manager can view and edit sales rules, but not the rules that the customer service team uses.

When you configure a rule, you can select only the resources that you have tag-based access to. For example, a sales manager can select only the sales queues that they have access to. Pre-evaluation filters also enforce the scope of a rule, even if you don't select a condition for it. For more information, see [Pre-evaluation filters](#rules-tbac-pre-evaluation-filters).

Tag-based access control on rules also applies to the contact categories that rules create. For example, if you restrict a user to rules tagged `Function:Fraud`, then on the **Contact details** page and in dashboards, the user sees only the contact categories from rules tagged `Function:Fraud`.

## Tagging rules
<a name="rules-tbac-tagging-rules"></a>

You can tag a rule when you create it, or when you update an existing rule. You can add tags by using the Connect Customer admin website or the Connect Customer API. For more information about tagging, see [Add tags to resources in Connect Customer](tagging.md).

The tags that you can add to a rule depend on the tag-based access controls in your security profiles:
+ If your security profiles have no tag-based access controls on rules, you can create or update a rule with any tags.
+ If your security profiles have tag-based access controls on rules, you must add all of the tags from at least one of your security profiles to the rule. For example, if one security profile grants you access to `Department:Sales` and another grants you access to `Department:Retention`, you must add either the `Department:Sales` or the `Department:Retention` tag to the rule.

**Important**  
When you enable tag-based access control on rules, users lose access to any rule that doesn't have matching tags. Tag your existing rules before you enable tag-based access control on rules.

## Enabling tag-based access control on rules
<a name="rules-tbac-enable"></a>

Use the following procedure to restrict which rules the users of a security profile can view and manage, based on tags.

**Important**  
Before you start, tag your existing rules. After you enable tag-based access control on rules, users lose access to any rule that doesn't have matching tags.

**To enable tag-based access control on rules**

1. Log in to the Connect Customer admin website. In the following URL, replace {{instance name}} with the name of your instance: https://{{instance name}}.my.connect.aws/. Use an account with the **Security profiles - View** and **Security profiles - Edit** permissions.

1. In the navigation menu, choose **Users**, **Security profiles**, and then choose the security profile that you want to change.

1. Choose **Access control**.

1. Under **Tag-based access control**, choose **Edit**.

1. Under **Resources**, choose **Rules**.

1. Enter the tag key and value that users with this security profile can access.

1. Verify that the security profile has the **Rules - View** permission. Without it, users can't see any rules on the **Rules** page.

   Users without **Rules - View** can still see rule-based contact categories if they have the **Conversational analytics - View** permission. They see the categories on pages they have permissions for, such as **Contact details**, **Contact search**, **Real-time metrics**, and analytics dashboards. Tag-based access control on rules still applies to those categories.

1. Choose **Save**.

Users with this security profile can now view and manage only the rules that have the tags you entered.

For more information about tag-based access control, see [Apply tag-based access control in Connect Customer](tag-based-access-control.md).

## Tag-based access control on rules: What to expect
<a name="rules-tbac-what-to-expect"></a>

Tag-based access control applies when you configure or filter rules. It also applies when you view rule-based contact categories, including in analytics dashboards and contact details.

### Rule configuration
<a name="rules-tbac-what-to-expect-config"></a>
+ On the **Rules** page, you see only the rules that have all of the tags from at least one of your security profiles.
+ You can view, edit, and delete only those rules, based on your **Rules** permissions.

The same controls apply when you call the Rules APIs, such as `CreateRule`, `UpdateRule`, `DescribeRule`, and `SearchRules`.

### Rule-based contact categories
<a name="rules-tbac-what-to-expect-categories"></a>

You see a contact category only if you have access to the rule that creates it. This applies wherever contact categories appear, for example:
+ The **Contact details** page, including during an active contact.
+ The **Real-time metrics** page.
+ The **Contact search** page, when you search by contact category.
+ The conversational analytics dashboard. For more information about dashboards, see [Apply tag-based access controls to dashboards and reports in Connect Customer](dashboard-tag-based-access-control.md).
+ Evaluation forms, when you add a question that refers to a contact category.

In evaluation forms, you can refer only to the contact categories that you have access to.

To view contact categories, you also need the **Conversational analytics - View** permission.

## Controlling the scope of rules
<a name="rules-tbac-control-scope"></a>

When you configure a rule, you can select only the resources that you have access to in conditions and actions. For example, when you select queues in a rule condition, you can add only the queues that you have tag-based access to. This prevents you from running rules on departments or functions that you can't access.

Other commonly used resources that respect tag-based access control in rules include agents and evaluation forms. The agents that you can select in rules are also limited by [Apply hierarchy-based access control in Connect Customer](hierarchy-based-access-control.md). For more information about evaluation forms, see [Set up tag-based-access controls on performance evaluations](tag-based-access-control-performance-evaluations.md).

### Pre-evaluation filters
<a name="rules-tbac-pre-evaluation-filters"></a>

A pre-evaluation filter limits which resources a rule runs on, based on the tags on those resources. Connect Customer checks the pre-evaluation filters before it checks the rule conditions.

For rules that run when a contact evaluation is submitted, you can filter on the tags of the contact evaluation. If your security profile restricts you to evaluations that have a certain tag, for example `Department:Sales`, that tag is added as a pre-evaluation filter by default. An **Evaluation forms** rule requires `Department:Sales` in its pre-evaluation filters. This ensures that your rules notify on and act on only the data that you can access.

Note the following about pre-evaluation filters:
+ Each filter matches one tag key and value exactly.
+ If a rule has more than one filter, the resource must match all of them.
+ You can add pre-evaluation filters when you create or edit a rule on the Connect Customer admin website. You can also use the `PreEvaluationFilters` parameter of the [CreateRule](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateRule.html) and [UpdateRule](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateRule.html) APIs.

**Note**  
With conversational analytics rules, you can add contact tags as pre-evaluation filters. Currently, Connect Customer doesn't check your access to the contact tags that you add, because tag-based access control isn't yet supported on contacts. When it becomes available, you will need access to the contact tags that you add as filters.