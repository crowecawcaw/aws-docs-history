

# Create and manage rule sets

An ingress endpoint receives email for Mail Manager. After its traffic policy accepts a recipient, its assigned rule set processes the email. A rule set contains ordered rules. Each rule can use `Conditions` and `Unless` entries to select recipients, then run ordered `Actions`.

Use this page to create and manage rule sets, and to assign a rule set to an ingress endpoint. For condition properties, operators, and `Unless` behavior, see [Rule conditions](eb-rules-conditions.md). For action parameters, ordering, resources, and permissions, see [Rule actions](eb-rules-actions.md). After you assign a rule set, use [Monitor and troubleshoot rule sets](eb-rules-monitoring.md) to confirm successful processing and investigate individual messages.

## Before you begin
<a name="eb-rules-setup-before-you-begin"></a>

Before you create a rule set, create any resources required by its actions. For example, an action can require an archive, SMTP relay, Amazon S3 bucket, Amazon SNS topic, or Lambda function. See [Rule actions](eb-rules-actions.md) for each action's resources and permissions.

The IAM user or role that follows these procedures needs permission for the rule-set operations it uses. These operations can include `ses:CreateRuleSet`, `ses:GetRuleSet`, `ses:ListRuleSets`, `ses:UpdateRuleSet`, and `ses:DeleteRuleSet`. Assigning a rule set also requires `ses:CreateIngressPoint` or `ses:UpdateIngressPoint`. When an action uses an IAM role, the user or role that creates or updates the rule set also needs `iam:PassRole` permission for that role.

Before you create an ingress endpoint, create both the rule set and the traffic policy that you will assign to it. For traffic policy instructions, see [Traffic policies and policy statements](eb-filters.md).

**Note**  
A rule set can contain up to 40 rules. Each rule can contain up to 10 `Conditions` entries, up to 10 `Unless` entries, and from 1 through 10 `Actions`.

## Create and manage rule sets in the SES console
<a name="eb-rules-create-console"></a>

**To create a rule set and add rules**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, under **Mail Manager**, choose **Rule sets**.

1. Choose **Create rule set**.

1. Enter a rule-set name, and then choose **Create rule set**.

1. On the rule set's details page, choose **Edit**.

1. Choose **Create new rule**.

1. In **Rule details**, enter a rule name.

1. To add a `Conditions` entry, choose **Add new condition**, and then select a property, operator, and value. See [Rule conditions](eb-rules-conditions.md) for supported properties, operators, and values.

1. To add an `Unless` entry, select **EXCEPT in the case of:**, and then choose **Add new exception**. An `Unless` match prevents the current rule's actions from running for the matching recipient.

1. Choose **Add new action**, and then configure the action. See [Rule actions](eb-rules-actions.md) for action parameters and required permissions.

1. To add another action, choose **Add new action**. Use the arrow controls to put the actions in execution order.

1. Repeat the preceding steps for each rule. Use the controls in the **Reorder** column to put the rules in execution order.

1. Choose **Save rule set**.

**To update and reorder rules**

1. On the **Rule sets** page, choose the rule-set name.

1. Choose **Edit**.

1. To add a rule, choose **Create new rule**.

1. To update a rule, select it and change its `Conditions`, `Unless`, or `Actions` entries in **Rule details**.

1. To remove a rule, select it and choose **Delete**.

1. Use the arrow controls to reorder rules or actions.

1. Choose **Save rule set**.

**Assign a rule set to an ingress endpoint**  
When you create an ingress endpoint, select the rule set in **Rule set**. You must also select a traffic policy. For the complete procedure, see [Creating and managing ingress points](eb-ingress.md#eb-ingress-create-console).

**To change the rule set assigned to an existing ingress endpoint**

1. In the navigation pane, under **Mail Manager**, choose **Ingress endpoints**.

1. Choose the ingress endpoint name.

1. Choose **Edit rule set**.

1. In **Rule set**, select the replacement rule set.

1. Choose **Save changes**.

You cannot delete a rule set while an ingress endpoint references it. First assign a different rule set to each ingress endpoint that references the rule set.

**To delete a rule set**

1. In the navigation pane, under **Mail Manager**, choose **Rule sets**.

1. Select the rule set and choose **Delete**.

1. In the **Delete rule set** dialog, enter **confirm**.

1. Choose **Delete**.

## Create and manage rule sets with the AWS CLI
<a name="eb-rules-setup-cli"></a>

The following commands use rule set IDs `rs-0123456789abcdef01234567` and `rs-fedcba9876543210fedcba98`, traffic policy ID `tp-0123456789abcdef01234567`, and ingress endpoint ID `inp-0123456789abcdef01234567`. Replace these IDs and the AWS Region with your own values.

### Create a rule set
<a name="eb-rules-setup-cli-create"></a>

`CreateRuleSet` requires a rule-set name and a `Rules` list. The following command creates a rule set with one rule. The rule adds the `X-Route: orders` header when a recipient ends with `@example.com`, except for `test@example.com`:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{inbound-routing}} \
  --rules '[{
    "Name": "route-orders",
    "Conditions": [{
      "StringExpression": {
        "Evaluate": {"Attribute": "RECIPIENT"},
        "Operator": "ENDS_WITH",
        "Values": ["@example.com"]
      }
    }],
    "Unless": [{
      "StringExpression": {
        "Evaluate": {"Attribute": "RECIPIENT"},
        "Operator": "EQUALS",
        "Values": ["test@example.com"]
      }
    }],
    "Actions": [{
      "AddHeader": {
        "HeaderName": "X-Route",
        "HeaderValue": "orders"
      }
    }]
  }]'
```

The response contains the `RuleSetId`. Use this ID to retrieve, update, assign, or delete the rule set.

### Update, add, remove, and reorder rules
<a name="eb-rules-setup-cli-update"></a>

In the following command, replace the AWS Region and rule set ID with your own values. Run `get-rule-set` to retrieve the current rule list before you replace it:

```bash
PROMPT> aws mailmanager get-rule-set \
  --region {{us-east-1}} \
  --rule-set-id {{rs-0123456789abcdef01234567}}
```

When you include `--rules` in `update-rule-set`, the supplied list replaces all current rules. Include every rule that the rule set must retain. The position of each rule in the list controls rule order. The position of each action in `Actions` controls action order.

In the following command, replace the AWS Region and rule set ID with your own values. The command renames the rule set and replaces its rules with the displayed order:

```bash
PROMPT> aws mailmanager update-rule-set \
  --region {{us-east-1}} \
  --rule-set-id {{rs-0123456789abcdef01234567}} \
  --rule-set-name {{inbound-routing-v2}} \
  --rules '[
    {
      "Name": "route-priority-orders",
      "Conditions": [{
        "StringExpression": {
          "Evaluate": {"Attribute": "RECIPIENT"},
          "Operator": "EQUALS",
          "Values": ["priority-orders@example.com"]
        }
      }],
      "Actions": [
        {"AddHeader": {"HeaderName": "X-Priority", "HeaderValue": "high"}},
        {"AddHeader": {"HeaderName": "X-Route", "HeaderValue": "orders"}}
      ]
    },
    {
      "Name": "route-orders",
      "Conditions": [{
        "StringExpression": {
          "Evaluate": {"Attribute": "RECIPIENT"},
          "Operator": "ENDS_WITH",
          "Values": ["@example.com"]
        }
      }],
      "Unless": [{
        "StringExpression": {
          "Evaluate": {"Attribute": "RECIPIENT"},
          "Operator": "EQUALS",
          "Values": ["test@example.com"]
        }
      }],
      "Actions": [
        {"AddHeader": {"HeaderName": "X-Route", "HeaderValue": "orders"}}
      ]
    }
  ]'
```

To add a rule or action, add it to the complete list. To remove one, omit it from the complete list. To reorder rules or actions, change their positions in the corresponding lists.

### Assign a rule set to an ingress endpoint
<a name="eb-rules-setup-cli-assign"></a>

An ingress endpoint requires an existing rule set and traffic policy. In the following command, replace the AWS Region, ingress endpoint name, rule set ID, and traffic policy ID with your own values. The command creates an open ingress endpoint and assigns both resources:

```bash
PROMPT> aws mailmanager create-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-name {{orders-ingress}} \
  --type OPEN \
  --rule-set-id {{rs-0123456789abcdef01234567}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}} \
  --tls-policy REQUIRED
```

For other ingress endpoint types and settings, see [Ingress endpoints](eb-ingress.md).

In the following command, replace the AWS Region, ingress endpoint ID, and replacement rule set ID with your own values. The command replaces the rule set assigned to an existing ingress endpoint. Other ingress endpoint properties remain unchanged:

```bash
PROMPT> aws mailmanager update-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-id {{inp-0123456789abcdef01234567}} \
  --rule-set-id {{rs-fedcba9876543210fedcba98}}
```

### Delete a rule set
<a name="eb-rules-setup-cli-delete"></a>

Before you delete `rs-0123456789abcdef01234567`, assign a different rule set to every ingress endpoint that references it. In the following commands, replace the AWS Region and resource IDs with your own values. The commands replace the assignment on one ingress endpoint and then delete the unassigned rule set:

```bash
PROMPT> aws mailmanager update-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-id {{inp-0123456789abcdef01234567}} \
  --rule-set-id {{rs-fedcba9876543210fedcba98}}

PROMPT> aws mailmanager delete-rule-set \
  --region {{us-east-1}} \
  --rule-set-id {{rs-0123456789abcdef01234567}}
```