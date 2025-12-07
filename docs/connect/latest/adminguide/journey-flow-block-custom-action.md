# Custom action

## Description

Use this block to call Lambda functions that fetch, validate, or transform data for use in the journey.

## How to configure this block

You can configure the **Custom action** block in the admin website or using the InvokeLambda action.

### Common properties

| Property     | Description                          |
| ------------ | ------------------------------------ |
| Action       | Select Invoke Lambda action          |
| Function ARN | Select a registered Lambda function. |

**Example**

Invoke a Lambda to check offer eligibility, store the result in eligibilityStatus, and branch accordingly.

## Configuration

Before you can invoke a Lambda using this block, you need to set up your Lambda functions
at your Amazon Connect instance at AWS admin console. For similar information, see [Grant Amazon Connect access to your AWS Lambda
functions](connect-lambda-functions.md "connect-lambda-functions.md").

When you do
this for a journey flow block, you use the **Outbound campaigns** under the
**Channels and communications** section, and to choose your Lambda function,
you use the **Set up custom actions** section and then the **Lambda
Functions** drop down.
