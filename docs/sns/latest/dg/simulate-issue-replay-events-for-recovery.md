# Step 4: Simulating an issue

and replay events for recovery

## Step 1: Enable the

simulated issue and send a second API request

1. Sign in to the [AWS Lambda
   console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. On the navigation panel, choose **Functions**.
3. Search for `serverlessrepo-fork-example` and choose
   `CheckoutFunction`.
4. On the
   **fork-example-ecommerce-`my-app`-CheckoutFunction-`ABCDEF`...**
   page, in the **Environment variables** section, set the
   **BUG_ENABLED** variable to **true**
   and then choose **Save**.
5. Copy the following JSON to a file named
   `test_event_2.json`.

```
{
	   "id": 9917,
	   "date": "2019-03-26T21:11:10-08:00",
	   "status": "confirmed",
	   "customer": {
	      "id": 56999,
"quantity": 1,
	      "price": 75.00,
	      "subtotal": 75.00
	   }]
	}
```

6. To send an HTTPS request to your API endpoint, pass the sample event
   payload as input by executing a `curl` command, for
   example:

```
curl -d "$(cat test_event_2.json)" https://abcdefghij.execute-api.us-east-2.amazonaws.com/Prod/checkout
```

The API returns the following empty response, indicating a successful
execution:

```
{ }
```

## Step 2: Verify simulated data

corruption

1. Sign in to the [Amazon DynamoDB
   console](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. On the navigation panel, choose **Tables**.
3. Search for `serverlessrepo-fork-example` and choose
   `CheckoutTable`.
4. On the table details page, choose **Items** and then
   choose the created item.

The stored attributes are displayed, some marked as
**CORRUPTED!**

## Step 3: Disable the simulated

issue

1. Sign in to the [AWS Lambda
   console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. On the navigation panel, choose **Functions**.
3. Search for `serverlessrepo-fork-example` and choose
   `CheckoutFunction`.
4. On the
   **fork-example-ecommerce-`my-app`-CheckoutFunction-`ABCDEF`...**
   page, in the **Environment variables** section, set the
   **BUG_ENABLED** variable to **false**
   and then choose **Save**.

## Step 4: Enable replay

to recover from the issue

1. In the AWS Lambda console, on the navigation panel, choose
   **Functions**.
2. Search for `serverlessrepo-fork-example` and choose
   `ReplayFunction`.
3. Expand the **Designer** section, choose the
   **SQS** tile and then, in the **SQS**
   section, choose **Enabled**.

###### Note

It takes approximately 1 minute for the Amazon SQS event source trigger to
become enabled. 4. Choose **Save**. 5. To view the recovered attributes, return to the Amazon DynamoDB console. 6. To disable replay, return to the AWS Lambda console and disable the Amazon SQS
event source trigger for `ReplayFunction`.
