# Prerequisites

Before you can manage datasets, make sure the following are in place.

## AWS credentials and permissions

AWS credentials configured with permissions for `bedrock-agentcore` dataset operations.

### Required IAM permissions

The following IAM policy grants the minimum permissions needed to manage datasets:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:CreateDataset",
                "bedrock-agentcore:GetDataset",
                "bedrock-agentcore:ListDatasets",
                "bedrock-agentcore:UpdateDataset",
                "bedrock-agentcore:DeleteDataset",
                "bedrock-agentcore:CreateDatasetVersion",
                "bedrock-agentcore:ListDatasetVersions",
                "bedrock-agentcore:AddDatasetExamples",
                "bedrock-agentcore:UpdateDatasetExamples",
                "bedrock-agentcore:DeleteDatasetExamples",
                "bedrock-agentcore:ListDatasetExamples"
            ],
            "Resource": "arn:aws:bedrock-agentcore:*:*:dataset/*"
        }
    ]
}
```

## SDK requirements

- **AgentCore SDK:**
  `pip install bedrock-agentcore` (Python 3.10 or later)
- **AWS SDK (boto3):** Python 3.10 or later with `boto3` installed
