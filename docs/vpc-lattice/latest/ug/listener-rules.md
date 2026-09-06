

# Listener rules for your VPC Lattice service
<a name="listener-rules"></a>

Each listener has a default rule and additional rules that you can define. Each rule consists of a priority, one or more actions, and one or more conditions. You can add or edit rules at any time.

**Topics**
+ [Default rules](#listener-default-rule)
+ [Rule priority](#listener-rule-priority)
+ [Rule action](#listener-rule-actions)
+ [Rule conditions](#listener-rule-conditions)
+ [Add a rule](#add-rules)
+ [Update a rule](#update-rules)
+ [Delete a rule](#delete-rules)

## Default rules
<a name="listener-default-rule"></a>

When you create a listener, you define actions for the default rule. Default rules can't have conditions. If the conditions for none of a listener's rules are met, then the action for the default rule is performed.

## Rule priority
<a name="listener-rule-priority"></a>

Each rule has a priority. Rules are evaluated in priority order, from the lowest value to the highest value. The default rule is evaluated last. You can change the priority of a non-default rule at any time. You cannot change the priority of the default rule. 

## Rule action
<a name="listener-rule-actions"></a>

Listeners for VPC Lattice services support forward actions and fixed response actions.

### Forward actions
<a name="forward-actions"></a>

You can use `forward` actions to route requests to one or more VPC Lattice target groups. If you specify multiple target groups for a `forward` action, you must specify a weight for each target group. Each target group weight is a value from 0 to 999. Requests that match a listener rule with weighted target groups are distributed to these target groups based on their weights. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group.

### Fixed-response actions
<a name="fixed-response-actions"></a>

You can use `fixed-response` actions to drop client requests and return a custom HTTP response. You can use this action to return a 404 or a 500 response code.

**Example fixed response action for the AWS CLI**  
You can specify an action when you create or update a rule. The following action sends a fixed response with the specified status code.  

```
"action": { 
    "fixedResponse": { 
        "statusCode": 404
},
```

## Rule conditions
<a name="listener-rule-conditions"></a>

Each rule condition has a type and configuration information. When the conditions for a rule are met, then its actions are performed.

The following are the supported matching criteria for a rule:

**Header match**  
Routing is based on the HTTP headers for each request. You can use HTTP header conditions to configure rules that route requests based on the HTTP headers for the request. You can specify the names of standard or custom HTTP header fields. The header name and the match evaluation are not case sensitive. You can change this setting by turning on case-sensitivity. Wildcard characters are not supported in the header name. Prefix, exact, and contains matching are supported on header match.

**Method match**  
Routing is based on the HTTP request method of each request.   
You can use HTTP request method conditions to configure rules that route requests based on the HTTP request method of the request. You can specify standard or custom HTTP methods. The method match is case sensitive. The method name must be an exact match. Wildcard characters are not supported. 

**Path match**  
Routing is based on matching the path patterns in the request URLs.   
You can use path conditions to define rules that route requests based on the URL in the request. Wildcard characters are not supported. Prefix and exact matching on path are supported.

## Add a rule
<a name="add-rules"></a>

You can add a listener rule at any time.

**To add a listener rule using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Services**.

1. Select the name of the service to open its details page.

1. On the **Routing** tab, choose **Edit listener**.

1. Expand **Listener rules** and choose **Add rule**.

1. For **Rule name**, enter a name for the rule.

1. For **Priority**, enter a priority between 1 and 100. Rules are evaluated in priority order, from the lowest value to the highest value. The default rule is evaluated last.

1. For **Condition**, enter a path pattern for the path match condition. The maximum size of each string is 200 characters. The comparison is not case sensitive. Wildcard characters are not supported.

   To add a header match or method match rule condition, use the AWS CLI or an AWS SDK.

1. For **Action**, choose a VPC Lattice target group.

1. Choose **Save changes**.

**To add a rule using the AWS CLI**  
Use the [create-rule](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/create-rule.html) command.

## Update a rule
<a name="update-rules"></a>

You can update a listener rule at any time. You can modify its priority, condition, target group, and the weight of each target group. You can't modify the name of the rule.

**To update a listener rule using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Services**.

1. Select the name of the service to open its details page.

1. On the **Routing** tab, choose **Edit listener**.

1. Modify the rule priorities, conditions, and actions as needed.

1. Review your updates and choose **Save changes**.

**To update a rule using the AWS CLI**  
Use the [update-rule](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/update-rule.html) command.

## Delete a rule
<a name="delete-rules"></a>

You can delete the non-default rules for a listener at any time. You cannot delete the default rule for a listener. When you delete a listener, all of its rules are deleted.

**To delete a listener rule using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Services**.

1. Select the name of the service to open its details page.

1. On the **Routing** tab, choose **Edit listener**.

1. Find the rule and choose **Remove**.

1. Choose **Save changes**.

**To delete a rule using the AWS CLI**  
Use the [delete-rule](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-rule.html) command.