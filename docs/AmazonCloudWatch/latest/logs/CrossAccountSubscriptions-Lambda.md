

# Cross-account log data sharing using Lambda
<a name="CrossAccountSubscriptions-Lambda"></a>

In this example, a log data recipient (account **999999999999**) sets up a Lambda function as a cross-account subscription destination, and a log data sender (account **111111111111**) creates a subscription filter that delivers log events to it.

**Note**  
The log group and the destination must be in the same AWS Region.

**To deliver log events across accounts to a Lambda function**

1. In the recipient account, create an AWS Identity and Access Management (IAM) role named `CWLtoLambdaRole` that CloudWatch Logs assumes to invoke the function. Use the following trust policy, which allows the CloudWatch Logs service principal to assume the role:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": { "Service": "logs.us-east-1.amazonaws.com" },
               "Action": "sts:AssumeRole",
               "Condition": { "ArnLike": { "aws:SourceArn": ["arn:aws:logs:us-east-1:999999999999:*", "arn:aws:logs:us-east-1:111111111111:*"] } }
           }
       ]
   }
   ```

   Attach the following permissions policy to the role, which allows the role to invoke the function:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           { "Effect": "Allow", "Action": "lambda:InvokeFunction", "Resource": "arn:aws:lambda:us-east-1:999999999999:function:RecipientFunction" }
       ]
   }
   ```

1. In the recipient account, grant CloudWatch Logs permission to invoke the function:

   ```
   aws lambda add-permission \
       --function-name "RecipientFunction" \
       --statement-id "AllowCWLogsInvoke" \
       --principal "logs.us-east-1.amazonaws.com" \
       --action "lambda:InvokeFunction"
   ```

1. In the recipient account, create the destination that points to the function, using the role that you created in the first step:

   ```
   aws logs put-destination \
       --destination-name "testLambdaDestination" \
       --target-arn "arn:aws:lambda:us-east-1:999999999999:function:RecipientFunction" \
       --role-arn "arn:aws:iam::999999999999:role/CWLtoLambdaRole"
   ```

1. In the recipient account, attach a destination access policy that allows the sender account to create a subscription filter on the destination:

   ```
   aws logs put-destination-policy \
       --destination-name "testLambdaDestination" \
       --access-policy '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"111111111111"},"Action":"logs:PutSubscriptionFilter","Resource":"arn:aws:logs:us-east-1:999999999999:destination:testLambdaDestination"}]}'
   ```

1. In the sender account (**111111111111**), create the subscription filter that targets the destination:

   ```
   aws logs put-subscription-filter \
       --log-group-name "{{myLogGroup}}" \
       --filter-name "testFilter" \
       --filter-pattern "" \
       --destination-arn "arn:aws:logs:us-east-1:999999999999:destination:testLambdaDestination"
   ```

1. To validate the delivery, put a test log event into the source log group. For more information about generating a test event, see [PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html). After you put the event, confirm that the recipient Lambda function is invoked. The function's logs show the delivered log event.