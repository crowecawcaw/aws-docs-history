

# Recreate an API mapping using routing rules
<a name="rest-api-routing-rules-recreate-api-mapping"></a>

You can recreate an API mapping using routing rules. To recreate an API mapping, make sure to turn on base path striping. This preserves the behavior of API mappings. For more information, see [Strip the base path with base path conditions](rest-api-routing-rules.md#rest-api-routing-rules-condition-path-split).

The following tutorial shows how to recreate the API mapping `https:// {{api.example.com}}/orders/v2/items/categories/5` as a routing rule and how to update your access logs to log the routing rule ID API Gateway uses to send traffic to your API.

------
#### [ AWS Management Console ]

**To set the routing mode to ROUTING\_RULE\_THEN\_API\_MAPPING**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose **Custom domain names** from the main navigation pane. 

1. Choose your custom domain name.

1. For **Domain details**, choose **Edit**.

1. For **Routing mode**, choose **ROUTING\_RULE\_THEN\_API\_MAPPING**.

1. Choose **Save** 

After you set the routing mode, you create the routing rule.

**To create the routing rule**

1. On the **Routing details** tab, choose **Add routing rule**.

1. Choose **Add new condition** and then choose **Path**.

1. For **Path**, enter **orders/v2/items/categories/5**.

1. For **Strip base path**, choose **Active**.

1. For **Target API**, choose your target API.

1. For **Target stage**, choose your target stage.

1. Choose **Next**.

1. For priority, enter a priority.

   Even if you keep your existing API mapping, API Gateway will always use the new routing rule as routing rules always take priority over API mappings.

1. Choose **Save changes**.

After you create the routing rule, update the access log format for your stage or create a new log to confirm that API Gateway uses your routing rule to send traffic to your API.

**To update your access logs**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose your API.

1. In the main navigation pane, choose **Stages**.

1. For **Logs and tracing**, choose **Edit**.

   If you don't have a log group, see [Set up CloudWatch logging for REST APIs in API Gateway](set-up-logging.md).

1. Add **$context.customDomain.routingRuleIdMatched** to your log format.

   This log group records the routing rule ID that API Gateway used to send traffic to your API. For more information, see [I can't tell how API Gateway sent traffic to my APIs](rest-api-routing-rules-troubleshoot.md#rest-api-routing-rules-logging).

1. Choose **Save**.

After you update your access logs, invoke your custom domain name. The following is an example curl command to invoke the custom domain name `https://{{api.example.com}}` with the base path `orders/v2/items/categories/5`.

```
curl "https://{{api.example.com}}/orders/v2/items/categories/5"
```

After you have successfully invoked your custom domain name, confirm that CloudWatch Logs shows the `routingRuleIdMatched`. To learn how to use the CloudWatch Logs console to view a log group, see [View API Gateway log events in the CloudWatch console](view-cloudwatch-log-events-in-cloudwatch-console.md).

------
#### [ AWS CLI ]

1. Use the following [update-domain-name](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/update-domain-name.html) command to update the domain name `{{api.example.com}}` to use the routing mode `ROUTING_RULE_THEN_API_MAPPING`.

   ```
   aws apigatewayv2 update-domain-name \
     --domain-name '{{api.example.com}}' \
     --routing-mode ROUTING_RULE_THEN_API_MAPPING
   ```

1. Use the following [create-routing-rule](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/create-routing-rule.html) command to create a new routing rule to recreate the API mapping `https://{{api.example.com}}/orders/v2/items/categories/5`.

   ```
   aws apigatewayv2 create-routing-rule \
     --domain-name '{{api.example.com}}' \
     --priority 50 \
     --conditions '[
     {
       "MatchBasePaths": {
         "AnyOf": [
           "orders/v2/items/categories/5"
         ]
       }
     }
   ]' \
     --actions '[
     {
       "InvokeApi": {
         "ApiId": "a1b2c3",
         "Stage": "prod",
         "StripBasePath": true
       }
     }
   ]'
   ```

1. Use the following [update-stage](https://docs.aws.amazon.com/cli/latest/reference/apigateway/update-stage.html) command to update the access logs format to include the `$context.customDomain.routingRuleIdMatched` variable. This variable records the routing rule ID that API Gateway used to send traffic to your API. You use this log to confirm that API Gateway uses your routing rule to send traffic to your API. For more information, see [I can't tell how API Gateway sent traffic to my APIs](rest-api-routing-rules-troubleshoot.md#rest-api-routing-rules-logging).

   ```
   aws apigateway update-stage \
     --rest-api-id {{a1bc2c3}} \
     --stage-name prod \
     --patch-operations "op=replace,path=/accessLogSettings/format,value='\$context.path \$context.customDomain.routingRuleIdMatched \$context.requestId \$context.extendedRequestId'"
   ```

   If you don't have a log group, see [Set up CloudWatch logging for REST APIs in API Gateway](set-up-logging.md).

1. Use the following example curl command to invoke your custom domain name with the base path `orders/v2/items/categories/5`.

   ```
   curl "https://{{api.example.com}}/orders/v2/items/categories/5
   ```

1. Use the following [filter-log-events](https://docs.aws.amazon.com/cli/latest/reference/logs/filter-log-events.html) command to get the log events from the log group `access-log-group-orders` that contain routing rule ID `abc123`.

   ```
   aws logs filter-log-events --log-group-name access-log-group-orders --filter-pattern abc123
   ```

    This confirms that API Gateway used the routing rule to send traffic to your API.

------