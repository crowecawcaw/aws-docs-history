# Maintain a usage plan for REST APIs in API Gateway

Maintaining a usage plan involves monitoring the used and remaining quotas over a
given time period and, if needed, extending the remaining quotas by a specified
amount. The following procedures describe how to monitor quotas.

AWS Management Console

###### To monitor used and remaining quotas

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. In the API Gateway main navigation pane, choose **Usage
   plans**.
3. Select a usage plan.
4. Choose the **Associated API keys** tab to see the number of request remaining for the time period for each key.
5. (Optional) Choose **Export usage data**, and then choose a
   **From** date and a **To** date. Then
   choose **JSON** or **CSV** for the
   exported data format, and then choose **Export**.

The following example shows an exported file.

```
{
    "px1KW6...qBazOJH": [
      [
        0,
        5000
      ],
      [
        0,
        5000
      ],
      [
        0,
        10
      ]
    ]
  }
```

The usage data in the example shows the daily usage data for an API
client, as identified by the API key (`px1KW6...qBazOJH`),
between August 1, 2016 and August 3, 2016. Each daily usage data shows used
and remaining quotas. In this example, the subscriber hasn't used any
allotted quotas yet, and the API owner or administrator has reduced the
remaining quota from 5000 to 10 on the third day.

The following procedures describe how to modify quotas.

###### To extend the remaining quotas

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. In the API Gateway main navigation pane, choose **Usage
   plans**.
3. Select a usage plan.
4. Choose the **Associated API keys** tab to see the number of request remaining for the time period for each key.
5. Select an API key, and then choose **Grant usage extension**.
6. Enter a number for the **Remaining requests** quota. You can increase the renaming requests or decrease the remaining requests for the time period of your usage plan.
7. Choose **Update quota**.

AWS CLIThe following [update-usage-plan](../../../cli/latest/reference/apigateway/update-usage-plan.md "../../../cli/latest/reference/apigateway/update-usage-plan.md") examples add, remove, or modify the method-level
throttling settings in a usage plan.

###### Note

Be sure to change `us-east-1` to the appropriate Region value for
your API.

To add or replace a rate limit for throttling an individual resource and
method:

```
aws apigateway --region us-east-1 update-usage-plan --usage-plan-id `planId` --patch-operations op="replace",path="/apiStages/`apiId`:`stage`/throttle/`resourcePath`/`httpMethod`/rateLimit",value="0.1"
```

To add or replace a burst limit for throttling an individual resource and
method:

```
aws apigateway --region us-east-1 update-usage-plan --usage-plan-id `planId` --patch-operations op="replace",path="/apiStages/`apiId`:`stage`/throttle/`resourcePath`/`httpMethod`/burstLimit",value="1"
```

To remove the method-level throttling settings for an individual resource and
method:

```
aws apigateway --region us-east-1 update-usage-plan --usage-plan-id `planId` --patch-operations op="remove",path="/apiStages/`apiId`:`stage`/throttle/`resourcePath`/`httpMethod`",value=""
```

To remove all method-level throttling settings for an API:

```
aws apigateway --region us-east-1 update-usage-plan --usage-plan-id `planId` --patch-operations op="remove",path="/apiStages/`apiId`:`stage`/throttle ",value=""
```

Here is an example using the Pet Store sample API:

```
aws apigateway --region us-east-1 update-usage-plan --usage-plan-id `planId` --patch-operations op="replace",path="/apiStages/`apiId`:`stage`/throttle",value='"{\"/pets/GET\":{\"rateLimit\":1.0,\"burstLimit\":1},\"//GET\":{\"rateLimit\":1.0,\"burstLimit\":1}}"'
```

REST APICall [`usageplan:update`](../api/API_UpdateUsagePlan.md "../api/API_UpdateUsagePlan.md") to maintain a usage plan.
