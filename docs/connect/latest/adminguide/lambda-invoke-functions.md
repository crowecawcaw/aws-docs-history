

# Invoke Lambda functions
<a name="lambda-invoke-functions"></a>

## Step 1: Create a Lambda function
<a name="lambda-create-function"></a>

During campaign execution, outbound campaigns will invoke your Lambda function with a batch of profiles and expects a response containing results for each.

### Request Payload
<a name="lambda-request-payload"></a>

When your Lambda function is invoked, it will receive a JSON payload with the following structure:

#### Payload Structure
<a name="lambda-payload-structure"></a>

```
{
  "InvocationMetadata": {
    "CampaignContext": {
      "CampaignId": "string",
      "RunId": "string",
      "ActionId": "string",
      "CampaignName": "string"
    }
  },
  "Items": {
    "CustomerProfiles": [
      {
        "ProfileId": "string",
        "CustomerData": "string",
        "IdempotencyToken": "string"
      }
    ]
  }
}
```

#### Field Descriptions
<a name="lambda-field-descriptions"></a>

##### InvocationMetadata
<a name="lambda-invocation-metadata"></a>
+ **CampaignContext**: Contains metadata about the campaign execution
+ **CampaignId**: Unique identifier for the campaign
+ **RunId**: Unique identifier for this specific campaign run
+ **ActionId**: The identifier of the flow action being executed by outbound campaigns
+ **CampaignName**: Human-readable name of the campaign

##### Items
<a name="lambda-items"></a>
+ **CustomerProfiles**: Array of customer profiles to process (batched for efficiency)
+ **ProfileId**: Unique identifier for the customer profile
+ **CustomerData**: JSON string of the customer profile
+ **IdempotencyToken**: Unique token for this specific invocation to ensure idempotent processing

#### Example Request Payload
<a name="lambda-example-request"></a>

```
{
  "InvocationMetadata": {
    "CampaignContext": {
      "CampaignId": "campaign-12345",
      "RunId": "run-67890",
      "ActionId": "activity-abc123",
      "CampaignName": "Welcome Campaign"
    }
  },
  "Items": {
    "CustomerProfiles": [
      {
        "ProfileId": "customer-001",
        "CustomerData": "{\"firstName\":\"John\",\"lastName\":\"Doe\",\"email\":\"john.doe@example.com\"}",
        "IdempotencyToken": "token-xyz789"
      },
      {
        "ProfileId": "customer-002",
        "CustomerData": "{\"firstName\":\"Jane\",\"lastName\":\"Smith\",\"email\":\"jane.smith@example.com\"}",
        "IdempotencyToken": "token-abc456"
      }
    ]
  }
}
```

### Expected Response Payload
<a name="lambda-response-payload"></a>

Your Lambda function must return a JSON response with the following structure:

#### Response Structure
<a name="lambda-response-structure"></a>

```
{
  "Items": {
    "CustomerProfiles": [
      {
        "Id": "string",
        "ResultData": {}
      }
    ]
  }
}
```

#### Field Descriptions
<a name="lambda-response-field-descriptions"></a>

##### Items
<a name="lambda-response-items"></a>
+ **CustomerProfiles**: Array of results corresponding to each customer profile in the request
+ **Id**: Must match the `ProfileId` from the request
+ **ResultData**: Custom JSON object containing your processing results (optional)

#### Example Response Payload
<a name="lambda-example-response"></a>

```
{
  "Items": {
    "CustomerProfiles": [
      {
        "Id": "customer-001",
        "ResultData": {
          "recommendedProduct": "Premium Plan",
          "score": 85,
          "nextAction": "send_email"
        }
      },
      {
        "Id": "customer-002",
        "ResultData": {
          "error": "Invalid customer data",
          "errorCode": "VALIDATION_ERROR"
        }
      }
    ]
  }
}
```

## Important Constraints
<a name="lambda-constraints"></a>

### Payload Size Limits
<a name="lambda-payload-size-limits"></a>
+ **Maximum Response Payload Size**: 32 KB per customer profile
+ If your `ResultData` exceeds this limit, the invocation will be marked as invalid

### Response Requirements
<a name="lambda-response-requirements"></a>
+ You must provide a response for every `ProfileId` included in the request
+ Missing responses will be treated as errors
+ The `Id` field in the response must exactly match the `ProfileId` from the request

### Error Handling
<a name="lambda-error-handling"></a>
+ If your Lambda function throws an exception, all profiles in the batch will be marked as failed
+ Include error details in `ResultData` for debugging purposes

### Invocation Type
<a name="lambda-invocation-type"></a>
+ **Invocation Type**: `REQUEST_RESPONSE` (synchronous)
+ Your function should return results within 30 seconds rather than processing asynchronously. Responses taking longer than 30 seconds will result in action failure

## Step 2: Grant Outbound Campaigns access to your Lambda function
<a name="lambda-grant-access"></a>

1. Open the Amazon Connect console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose your instance name in the **Instance Alias** column. This instance name appears in the URL you use to access Amazon Connect.

1. In the navigation pane under **Channels and communications**, choose **Outbound campaigns**.

1. Under the **Set up custom actions** section, use the **Lambda functions** drop-down box to select the function to add to your outbound campaigns instance.

1. Choose **Add Lambda Function**. Confirm that the ARN of the function is added under **Lambda Functions**.

**Important**  
The preceding console procedure automatically adds the required resource-based policy to the Lambda function. If you use the AWS CLI or SDK, you can call the [PutConnectInstanceIntegration](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_PutConnectInstanceIntegration.html) API with the `lambda` integration configuration. This API automatically adds the required resource-based policy to your Lambda function, just as the console does.  
If you need to add the resource-based policy manually (for example, for cross-account invocations), add a policy statement that grants the `connect-campaigns.amazonaws.com` service principal permission to invoke your function. You can optionally add a `Condition` element with `AWS:SourceAccount` and `AWS:SourceArn` to restrict access to your account and Connect Customer instance. We recommend including both conditions. The following example shows the required policy statement.  

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "connect-campaigns.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:{{region}}:{{account-id}}:function:{{function-name}}",
      "Condition": {
        "StringEquals": {
          "AWS:SourceAccount": "{{account-id}}"
        },
        "ArnLike": {
          "AWS:SourceArn": "arn:aws:connect:{{region}}:{{account-id}}:instance/{{instance-id}}"
        }
      }
    }
  ]
}
```
For more information about resource-based policies, see [Using resource-based policies for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the *Lambda Developer Guide*.

## Step 3: Invoke a Lambda from a Campaign
<a name="lambda-invoke-from-journey"></a>

1. Open or create a **Journey** flow.

1. Add a **Custom action** block (in the **Integrate** group) to the grid. Connect the branches to and from the block.

1. Choose the title of the **Custom action** block to open its properties page.

1. Under **Function ARN**, choose from the list of functions you've added to your outbound campaigns instance.

## Step 4: Consume the Lambda function response
<a name="lambda-consume-response"></a>

### Access variables directly
<a name="lambda-access-variables"></a>

To access these variables directly in a flow block, add the block after the **Custom action** block, and then reference the attributes as shown in the following example:

```
RecommendedProduct - $.LambdaInvocation.ResultData.recommendedProduct
Score - $.LambdaInvocation.ResultData.score
```

Make sure that the name specified for the source attribute matches the key name in the `ResultData` returned from the Lambda.