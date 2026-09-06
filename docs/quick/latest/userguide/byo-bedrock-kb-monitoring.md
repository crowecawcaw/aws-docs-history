

# Monitoring and observability
<a name="byo-bedrock-kb-monitoring"></a>

Amazon Bedrock emits AWS CloudTrail data events for `Retrieve` and `GetDocumentContent` API calls on your managed knowledge base. You can use these events to monitor successful usage and detect access failures. The following walkthrough sets up a CloudTrail trail that delivers data events to a Amazon CloudWatch Logs log group, then creates metric filters and alarms to alert on errors.

## Step 1: Enable CloudTrail to Amazon CloudWatch for Amazon Bedrock knowledge base events
<a name="byo-bedrock-kb-monitoring-trail"></a>

Set up a CloudTrail trail that captures Amazon Bedrock knowledge base data events and delivers them to a Amazon CloudWatch Logs log group. Create the trail and log group in the same Region as your managed knowledge base. You can also do this through the CloudTrail console, which creates the log group and IAM role automatically.

Create the S3 bucket, apply a bucket policy that allows CloudTrail to write, and create the Amazon CloudWatch Logs log group:

```
aws s3 mb s3://{{YOUR_TRAIL_BUCKET}}

aws s3api put-bucket-policy --bucket {{YOUR_TRAIL_BUCKET}} --policy '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"Service": "cloudtrail.amazonaws.com"},
      "Action": "s3:GetBucketAcl",
      "Resource": "arn:aws:s3:::{{YOUR_TRAIL_BUCKET}}"
    },
    {
      "Effect": "Allow",
      "Principal": {"Service": "cloudtrail.amazonaws.com"},
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::{{YOUR_TRAIL_BUCKET}}/AWSLogs/{{ACCOUNT_ID}}/*",
      "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
    }
  ]
}'

aws logs create-log-group --log-group-name bedrock-kb-cloudtrail
```

Create an IAM role that allows CloudTrail to deliver logs to the log group:

```
aws iam create-role \
  --role-name CloudTrail-CWLogs-Role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "cloudtrail.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

aws iam put-role-policy \
  --role-name CloudTrail-CWLogs-Role \
  --policy-name CWLogsPolicy \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
      "Resource": "arn:aws:logs:{{REGION}}:{{ACCOUNT_ID}}:log-group:bedrock-kb-cloudtrail:*"
    }]
  }'
```

Create the trail, configure it to capture Amazon Bedrock knowledge base data events, and start logging:

```
aws cloudtrail create-trail \
  --name bedrock-kb-data-events \
  --s3-bucket-name {{YOUR_TRAIL_BUCKET}} \
  --cloud-watch-logs-log-group-arn "arn:aws:logs:{{REGION}}:{{ACCOUNT_ID}}:log-group:bedrock-kb-cloudtrail:*" \
  --cloud-watch-logs-role-arn "arn:aws:iam::{{ACCOUNT_ID}}:role/CloudTrail-CWLogs-Role"

aws cloudtrail put-event-selectors \
  --trail-name bedrock-kb-data-events \
  --advanced-event-selectors '[{
    "Name": "BedrockKBDataEvents",
    "FieldSelectors": [
      {"Field": "eventCategory", "Equals": ["Data"]},
      {"Field": "resources.type", "Equals": ["AWS::Bedrock::KnowledgeBase"]}
    ]
  }]'

aws cloudtrail start-logging --name bedrock-kb-data-events
```

## Step 2: Create metric filters for Amazon Quick retrieval calls
<a name="byo-bedrock-kb-monitoring-metrics"></a>

Create metric filters to track retrieval calls and errors when Amazon Quick invokes your managed knowledge base.

**Call volume metric** — tracks retrieval call volume to your managed knowledge base.

```
aws logs put-metric-filter \
  --log-group-name bedrock-kb-cloudtrail \
  --filter-name QuickSight-Retrieve-CallCount-{{KB_ID}} \
  --filter-pattern '{ $.eventSource = "bedrock.amazonaws.com" && $.eventName = "Retrieve" && $.userIdentity.invokedBy = "quicksight.amazonaws.com" && $.resources[0].ARN = "*{{KB_ID}}*" }' \
  --metric-transformations '[{
    "metricName": "RetrieveCallCount",
    "metricNamespace": "QuickSight/BedrockKB",
    "metricValue": "1",
    "dimensions": {"KnowledgeBaseId": "$.resources[0].ARN"}
  }]'
```

**Error metric** — the following example counts `Retrieve` calls from Amazon Quick that fail with `AccessDenied`. This alarm fires when the Amazon Quick service role is missing permissions or when a cross-account resource policy is misconfigured. You can create additional metric filters for other error codes such as `ThrottlingException` depending on your monitoring needs.

```
aws logs put-metric-filter \
  --log-group-name bedrock-kb-cloudtrail \
  --filter-name QuickSight-Retrieve-AccessDenied-{{KB_ID}} \
  --filter-pattern '{ $.eventSource = "bedrock.amazonaws.com" && $.eventName = "Retrieve" && $.userIdentity.invokedBy = "quicksight.amazonaws.com" && $.resources[0].ARN = "*{{KB_ID}}*" && $.errorCode = "AccessDenied" }' \
  --metric-transformations '[{
    "metricName": "RetrieveAccessDeniedCount",
    "metricNamespace": "QuickSight/BedrockKB",
    "metricValue": "1",
    "dimensions": {"KnowledgeBaseId": "$.resources[0].ARN"}
  }]'
```

## Step 3: Create a CloudWatch alarm
<a name="byo-bedrock-kb-monitoring-alarm"></a>

Create an alarm that triggers when access denied errors occur. Optionally add an SNS topic ARN to `--alarm-actions` for notifications.

```
aws cloudwatch put-metric-alarm \
  --alarm-name QuickSight-Retrieve-AccessDenied-{{KB_ID}} \
  --metric-name RetrieveAccessDeniedCount \
  --namespace "QuickSight/BedrockKB" \
  --dimensions Name=KnowledgeBaseId,Value="arn:aws:bedrock:{{REGION}}:{{ACCOUNT_ID}}:knowledge-base/{{KB_ID}}" \
  --statistic Sum \
  --period 300 \
  --threshold 1 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --evaluation-periods 1 \
  --treat-missing-data notBreaching
```