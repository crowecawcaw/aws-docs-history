# Invoke Lambda functions

## Step 1: Create a Lambda function

During campaign execution, outbound campaigns will invoke your Lambda function with a batch of profiles and expects a response
containing results for each.

### Request Payload

When your Lambda function is invoked, it will receive a JSON payload with the following
structure:

#### Payload Structure

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

##### InvocationMetadata

- **CampaignContext**: Contains metadata about the campaign
  execution
- **CampaignId**: Unique identifier for the campaign
- **RunId**: Unique identifier for this specific campaign
  run
- **ActionId**: The identifier of the flow action being executed by
  outbound campaigns
- **CampaignName**: Human-readable name of the
  campaign

##### Items

- **CustomerProfiles**: Array of customer profiles to
  process (batched for efficiency)
- **ProfileId**: Unique identifier for the customer
  profile
- **CustomerData**: JSON string of the customer
  profile
- **IdempotencyToken**: Unique token for this specific
  invocation to ensure idempotent processing

#### Example Request Payload

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

Your Lambda function must return a JSON response with the following structure:

#### Response Structure

```
{
  "Items": {
    "CustomerProfiles": [
      {
        "Id": "string",
        "Result": "SUCCESS" | "FAILURE",
        "ResultData": {}
      }
    ]
  }
}
```

#### Field Descriptions

##### Items

- **CustomerProfiles**: Array of results corresponding to
  each customer profile in the request
- **Id**: Must match the `ProfileId` from the
  request
- **Result**: Processing result - either
  `SUCCESS` or `FAILURE`
- **ResultData**: Custom JSON object containing your
  processing results (optional)

#### Example Response Payload

```
{
  "Items": {
    "CustomerProfiles": [
      {
        "Id": "customer-001",
        "Result": "SUCCESS",
        "ResultData": {
          "recommendedProduct": "Premium Plan",
          "score": 85,
          "nextAction": "send_email"
        }
      },
      {
        "Id": "customer-002",
        "Result": "FAILURE",
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

### Payload Size Limits

- **Maximum Response Payload Size**: 32 KB per customer
  profile
- If your `ResultData` exceeds this limit, the invocation will be marked as
  invalid

### Response Requirements

- You must provide a response for every `ProfileId` included in the
  request
- Missing responses will be treated as errors
- The `Id` field in the response must exactly match the
  `ProfileId` from the request

### Error Handling

- If your Lambda function throws an exception, all profiles in the batch will be marked
  as failed
- Use the `Result: "FAILURE"` field to indicate individual profile processing
  failures
- Include error details in `ResultData` for debugging purposes

### Invocation Type

- **Invocation Type**: `REQUEST_RESPONSE`
  (synchronous)
- Your function should return results within 30 seconds rather than processing
  asynchronously. Responses taking longer than 30 seconds will result in action failure

## Step 2: Grant Outbound Campaigns access to your Lambda

function

1. Open the Amazon Connect console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. On the instances page, choose your instance name in the **Instance
   Alias** column. This instance name appears in the URL you use to access Amazon
   Connect.
3. In the navigation pane under **Channels and communications**, choose
   **Outbound campaigns**.
4. Under the **Set up custom actions** section, use the **Lambda
   functions** drop-down box to select the function to add to your outbound campaigns
   instance.
5. Choose **Add Lambda Function**. Confirm that the ARN of the function is
   added under **Lambda Functions**.

## Step 3: Invoke a Lambda from a Campaign

1. Open or create a **Journey** flow.
2. Add a **Custom action** block (in the **Integrate**
   group) to the grid. Connect the branches to and from the block.
3. Choose the title of the **Custom action** block to open its properties
   page.
4. Under **Function ARN**, choose from the list of functions you've added
   to your outbound campaigns instance.

## Step 4: Consume the Lambda function response

### Access variables directly

To access these variables directly in a flow block, add the block after the
**Custom action** block, and then reference the attributes as shown in the
following example:

```
RecommendedProduct - $.LambdaInvocation.ResultData.recommendedProduct
Score - $.LambdaInvocation.ResultData.score
```

Make sure that the name specified for the source attribute matches the key name in the
`ResultData` returned from the Lambda.
