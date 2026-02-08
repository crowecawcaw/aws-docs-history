# IAM actions and resources migration

AWS Security Agent is a frontier agent that proactively secures your applications throughout the development lifecycle across all your environments. If you onboarded to AWS Security Agent prior to February 9, 2026, you will be impacted by upcoming changes on March 9, 2026 to your existing Agent Instance resources and AWS Security Agent IAM actions. In preparation for releasing public API/SDK support, the Agent Instance resource is being renamed to Agent Space, and specific IAM actions are being renamed. These changes will affect any Application or Agent Instances IAM roles you have created prior to March 9, 2026. In order to avoid seeing authentication issues after March 9, 2026, you will need to follow the steps under Preparing for Migration.

###### Note

If you create any new Agent Instances after February 9, 2026, the new Agent Instance will be created as an Agent Space and no migration steps will be required.

## Planned Changes

AWS Security Agent is renaming the Agent Instance resource to Agent Space: `arn:aws:securityagent:us-east-1:{{accountId}}:agent-instance/*` renamed to `arn:aws:securityagent:us-east-1:{{accountId}}:agent-space/*`. Additionally, the following IAM actions are being renamed:

- `securityagent:ListAgentInstances` renamed to `securityagent:ListAgentSpaces`
- `securityagent:ListControls` renamed to `securityagent:ListSecurityRequirements`
- `securityagent:BatchGetAgentInstances` renamed to `securityagent:BatchGetAgentSpaces`
- `securityagent:BatchGetSecurityTestContentMetadata` renamed to `securityagent:BatchGetPentestJobContentMetadata`
- `securityagent:BatchGetTasks` renamed to `securityagent:BatchGetPentestJobTasks`
- `securityagent:CreateDocumentReview` renamed to `securityagent:CreateDesignReview`
- `securityagent:GetDocumentReview` renamed to `securityagent:GetDesignReview`
- `securityagent:GetDocumentReviewArtifact` renamed to `securityagent:GetDesignReviewArtifact`
- `securityagent:ListDocumentReviews` renamed to `securityagent:ListDesignReviews`
- `securityagent:ListDocumentReviewComments` renamed to `securityagent:ListDesignReviewComments`
- `securityagent:ListTasks` renamed to `securityagent:ListPentestJobTasks`
- `securityagent:StartPentestExecution` renamed to `securityagent:StartPentestJob`
- `securityagent:StopPentestExecution` renamed to `securityagent:StopPentestJob`
- `securityagent:DeleteDocumentReview` renamed to `securityagent:DeleteDesignReview`

## Preparing for Migration

In order to avoid seeing issues after March 9, 2026 while continuing to use AWS Security Agent prior to March 9, 2026, you will need to **trust both the new and old resources and IAM actions in your IAM roles/policies** until March 9, 2026. The below instructions will provide a guide for migrating to the new resource and action formats:

1. Log in to your AWS account and navigate to the **AWS Security Agent console**
2. In the left hand panel, select **Settings** and click the role under **Service role**
3. In the IAM console for the associated role, select **Add permissions** and **Attach policies**
4. Select **AWSSecurityAgentWebAppPolicy** and click **Add permissions**
   1. **Important Note:** Verify that you have selected **AWSSecurityAgentWebAppPolicy** as the new policy and not **SecurityAgentWebAppAPIPolicy**

5. Verify that your IAM role now has both **AWSSecurityAgentWebAppPolicy** and **SecurityAgentWebAppAPIPolicy** under **Permissions policies**
6. In the same IAM role console, select **Trust relationships** then **Edit trust policy**
7. Update your trust policy to the following format, replacing **{{accountId}}** with your AWS account ID

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:securityagent:us-east-1:{{accountId}}:application/*",
            "arn:aws:securityagent:us-east-1:{{accountId}}:agent-space/*",
            "arn:aws:securityagent:us-east-1:{{accountId}}:agent-instance/*"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:SetContext",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}"
        },
        "ForAllValues:ArnEquals": {
          "sts:RequestContextProviders": "arn:aws:iam::aws:contextProvider/IdentityCenter"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:securityagent:us-east-1:{{accountId}}:application/*",
            "arn:aws:securityagent:us-east-1:{{accountId}}:agent-space/*",
            "arn:aws:securityagent:us-east-1:{{accountId}}:agent-instance/*"
          ]
        }
      }
    }
  ]
}
```

1. Navigate back to the **AWS Security Agent console**. From the left-hand panel, select **Agent Spaces**
2. For each Agent Space you have with penetration testing enabled, perform the following steps
   1. Navigate to the Agent Space and select **Penetration test**
   2. Scroll down to **Service access** and click the role under **Service role name**
   3. In the IAM console for the associated role, select **Trust relationships** then **Edit trust policy**
   4. Update your trust policy to the following format, replacing **{{accountId}}** with your AWS account ID

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:securityagent:us-east-1:{{accountId}}:agent-space/*",
            "arn:aws:securityagent:us-east-1:{{accountId}}:agent-instance/*"
          ]
        }
      }
    }
  ]
}
```
