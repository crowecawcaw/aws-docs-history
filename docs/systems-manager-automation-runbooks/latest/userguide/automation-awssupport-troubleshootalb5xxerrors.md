

# `AWSSupport-TroubleshootALB5XXErrors`
<a name="automation-awssupport-troubleshootalb5xxerrors"></a>

The `AWSSupport-TroubleshootALB5XXErrors` runbook diagnoses and troubleshoots HTTP 5XX errors on an Application Load Balancer. It analyzes Amazon CloudWatch (CloudWatch) metrics and Application Load Balancer access logs to identify root causes and provide actionable recommendations. The runbook covers the following capabilities:
+ **Traffic pattern analysis:** Identifies hotspotting and single Availability Zone anomalies by using CloudWatch metrics to detect uneven traffic distribution across Availability Zones.
+ **Access log diagnosis:** Processes Application Load Balancer access logs by retrieving log files from the configured Amazon S3 bucket to extract specific error patterns, error reasons, and detailed diagnostic information for granular troubleshooting.
+ **Error-specific analysis:** Provides targeted diagnosis for each HTTP 5XX error type:
  + **HTTP 500:** Authentication failures, WAF connectivity issues, and IDP endpoint problems.
  + **HTTP 502:** Target connection issues, AWS Lambda (Lambda) function errors, TLS negotiation failures, and target deregistration scenarios.
  + **HTTP 503:** Empty target groups and target registration issues.
  + **HTTP 504:** Connection timeouts, target response time anomalies with historical baseline comparison, and comprehensive network connectivity evaluation.
  + **Other 5XX errors:** Comprehensive analysis of uncommon 5XX status codes and edge cases that aren't covered by standard error categories.
+ **Network connectivity deep dive:** For HTTP 504 errors, evaluates security group rules, network ACLs, and route table configurations between the Application Load Balancer and its targets in the same AWS Region and account.
+ **Adaptive data source selection:** Prioritizes access log analysis when available for detailed error diagnosis, and automatically falls back to CloudWatch metrics when logs are unavailable or incomplete.

**Limitations**  
This runbook has the following limitations:  
**Connectivity check limitations:** Network connectivity evaluations are only performed for targets in the same AWS Region and account as the Application Load Balancer. Cross-account or on-premises targets receive general connectivity guidance.
**Access log processing time limits:** Access log analysis is limited to a 9-minute processing window. If exceeded, analysis stops and provides results based on the logs processed so far. Reduce the time frame for complete log analysis.
**Amazon S3 bucket security and location requirements:** Access log processing requires the Amazon S3 bucket to meet security and location criteria. The runbook skips access log processing when the Amazon S3 bucket is publicly accessible. Public bucket status is determined by the bucket policy or the public access block configuration. The runbook also skips processing when the Amazon S3 bucket is not in the same AWS account and Region as the Application Load Balancer. When these checks fail, the runbook automatically falls back to CloudWatch metrics-based analysis.
**Metrics as fallback:** When access logs are not enabled or log processing fails or is incomplete, the runbook automatically falls back to CloudWatch metrics-based analysis with less granular diagnostic information. Lack of access logs might affect root cause detection accuracy.
**Historical data dependency:** HTTP 504 response time anomaly detection requires 7 days of historical data for baseline comparison. Limited historical data might affect detection accuracy.

**Additional costs**  
Running this runbook queries metrics from Amazon CloudWatch and, when access logs are enabled, retrieves objects from Amazon S3. Standard CloudWatch and Amazon S3 charges might apply to your AWS account for the data queried during the analysis. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) and [Amazon Simple Storage Service Pricing](https://aws.amazon.com/s3/pricing/).

The runbook performs the following validation and analysis steps:
+ Verifies that the specified Application Load Balancer exists, and collects Application Load Balancer attributes such as idle timeout and access log configuration.
+ Detects hotspotting and single Availability Zone error anomalies by using CloudWatch metrics.
+ Retrieves and processes Application Load Balancer access logs from the configured Amazon S3 bucket when access logs are enabled and the bucket meets the security and location requirements.
+ Diagnoses each HTTP 5XX error code (500, 502, 503, 504, and other) by using access log entries when available, or by using CloudWatch metrics as a fallback.
+ For HTTP 504 errors, evaluates security group rules, network ACLs, and route table configurations between the Application Load Balancer and its targets.
+ Consolidates the findings into a report with recommendations and relevant references.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootALB5XXErrors) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `s3:ListBucket`
+ `s3:GetObject`
+ `s3:GetBucketPolicyStatus`
+ `s3:GetBucketPublicAccessBlock`
+ `s3:ListAllMyBuckets`
+ `elasticloadbalancing:DescribeTargetGroups`
+ `elasticloadbalancing:DescribeTargetHealth`
+ `elasticloadbalancing:DescribeLoadBalancers`
+ `elasticloadbalancing:DescribeTargetGroupAttributes`
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:DescribeListeners`
+ `elasticloadbalancing:DescribeRules`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeInstances`
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:DescribeSecurityGroups`
+ `ec2:DescribeNetworkAcls`
+ `ec2:DescribeRouteTables`
+ `cloudwatch:GetMetricData`
+ `cloudtrail:LookupEvents`
+ `wafv2:ListWebACLs`
+ `wafv2:ListResourcesForWebACL`
+ `lambda:GetFunctionConfiguration`

Example IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3ReadAccess",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketPublicAccessBlock",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ELBReadAccess",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeTargetGroupAttributes",
                "elasticloadbalancing:DescribeLoadBalancerAttributes",
                "elasticloadbalancing:DescribeListeners",
                "elasticloadbalancing:DescribeRules"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EC2ReadAccess",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSubnets",
                "ec2:DescribeInstances",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeRouteTables"
            ],
            "Resource": "*"
        },
        {
            "Sid": "MonitoringReadAccess",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricData",
                "cloudtrail:LookupEvents"
            ],
            "Resource": "*"
        },
        {
            "Sid": "WAFReadAccess",
            "Effect": "Allow",
            "Action": [
                "wafv2:ListWebACLs",
                "wafv2:ListResourcesForWebACL"
            ],
            "Resource": "*"
        },
        {
            "Sid": "LambdaReadAccess",
            "Effect": "Allow",
            "Action": [
                "lambda:GetFunctionConfiguration"
            ],
            "Resource": "*"
        }
    ]
}
```

Follow these steps to configure the automation:

1. Open [AWSSupport-TroubleshootALB5XXErrors](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootALB5XXErrors/description) in Systems Manager under Documents.

1. Choose **Execute automation**.

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Required):**

     The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
   + **ALBArn (Required):**

     The ARN of the Application Load Balancer to be investigated. For example, `arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-alb/50dc6c495c0c9188`.
   + **IssueStartTime (Required):**

     The start time of the issue in UTC. Use the ISO 8601 timestamp format (`YYYY-MM-DDTHH:MM:SSZ`). For example, `1970-01-01T00:00:00Z`.
   + **IssueEndTime (Required):**

     The end time of the issue in UTC. Use the ISO 8601 timestamp format (`YYYY-MM-DDTHH:MM:SSZ`). For example, `1970-01-01T00:00:00Z`.

1. Choose **Execute**.

1. The automation initiates.

1. The document performs the following steps:
   + **`RunInitialChecks`**:

     Runs initial checks on the Application Load Balancer. Initial checks include verifying the existence of the Application Load Balancer, detecting hotspotting and single Availability Zone errors, gathering HTTP error details, and checking the access log configuration.
   + **`ProcessAccessLogs`**:

     Retrieves the relevant Application Load Balancer access log files from the Amazon S3 bucket and processes them to identify unique error reasons and codes. Only a subset of access log files is processed for the identified time range. If the processing time exceeds the 9-minute limit, the remaining logs are not processed.
   + **`HTTP500ErrorIdentification`**:

     Identifies the error reason for Application Load Balancer-generated HTTP 500 errors by using either CloudWatch metrics or the parsed access logs if available.
   + **`HTTP502ErrorIdentification`**:

     Identifies the error reason for Application Load Balancer-generated HTTP 502 errors by using either CloudWatch metrics or the parsed access logs if available.
   + **`HTTP503ErrorIdentification`**:

     Identifies the error reason for Application Load Balancer-generated HTTP 503 errors by using CloudWatch metrics.
   + **`HTTP504ErrorIdentification`**:

     Identifies the error reason for Application Load Balancer-generated HTTP 504 errors by using either CloudWatch metrics or the parsed access logs if available. For HTTP 504 errors, the step also evaluates security group rules, network ACLs, and route table configurations between the Application Load Balancer and its targets.
   + **`OtherHTTPErrorIdentification`**:

     Identifies the error reason for unclassified HTTP errors generated by the Application Load Balancer by using either CloudWatch metrics or the parsed access logs if available.
   + **`GenerateReport`**:

     Generates a consolidated report from the findings of the previous steps, including hotspotting status, single Availability Zone anomalies, error diagnoses, and recommendations.

1. After completion, review the **Outputs** section for the detailed results of the execution.

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootALB5XXErrors/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)