

# Amazon Bedrock troubleshooting
<a name="bedrock-troubleshooting"></a>

## Problem: Bedrock invocation returns AccessDenied
<a name="problem-bedrock-access-denied"></a>

A Lambda function or ECS task invoking a Bedrock model returns an `AccessDeniedException`. This most commonly occurs when the IAM policy for a cross-region inference profile uses the wrong ARN format.

### Diagnosis
<a name="diagnosis-6"></a>

Check the Lambda or ECS task CloudWatch logs for the full error:

```
STAGE=staging
aws logs tail /aws/lambda/cms-$STAGE-bedrock-supervisor \
  --since 15m --filter-pattern "AccessDeniedException"
```

The error message typically identifies whether the failing ARN is the inference profile or the underlying foundation model.

### Resolution
<a name="resolution-24"></a>

Bedrock cross-region inference profiles require **two** separate IAM policy statements with different ARN formats:

1.  **Inference profile ARN** — includes the AWS account ID and uses a geographic prefix on the model ID:

   ```
   {
     "Effect": "Allow",
     "Action": ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
     "Resource": "arn:aws:bedrock:*:<account-id>:inference-profile/us.anthropic.claude-sonnet-4-*"
   }
   ```

1.  **Foundation model ARN** — does NOT include an account ID (the account field is empty):

   ```
   {
     "Effect": "Allow",
     "Action": ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
     "Resource": "arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-*"
   }
   ```

Common mistakes:
+ Adding an account ID to the foundation-model ARN — the ARN will never match and all invocations fail.
+ Omitting the account ID from the inference-profile ARN — the ARN is malformed and access is denied.
+ Using `bedrock:InvokeModel` only without `bedrock:InvokeModelWithResponseStream` — streaming calls (used by the Strands agent framework) require the streaming action.

After correcting the IAM policy, redeploy the affected stack:

```
cd deployment
cdk deploy cms-$STAGE-bedrock-agents \
  --require-approval never
```