

# Security in WorkSpaces Advisor

Security is a shared responsibility between AWS and you. This page describes, for each WorkSpaces Advisor capability, what data it uses and why, how that data is protected, the permissions it needs, and how activity is logged.

WorkSpaces Advisor uses operational data, such as health, performance, and configuration data. It doesn't read the content of your users' sessions, such as what's on the screen, keystrokes, files, or clipboard contents.

## Security for Investigate a WorkSpace
<a name="workspaces-advisor-security-investigate"></a>

### Data accessed by WorkSpaces Advisor
<a name="workspaces-advisor-data"></a>

WorkSpaces Advisor accesses the following data to perform investigations:
+ [Amazon CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html) (for example, CPU usage, memory usage, and disk usage)
+ WorkSpaces resource configuration (WorkSpace ID, VPC, subnet, bundle type)
+ Service telemetry
+ Application names running on the WorkSpace, including their CPU and memory usage
+ AWS documentation and knowledge bases
+ Issue description

### Required permissions
<a name="workspaces-advisor-permissions"></a>

Investigate a WorkSpace uses [Forward access sessions (FAS)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) to perform actions using your IAM identity and permissions.

#### Permissions for investigations
<a name="workspaces-advisor-permissions-read"></a>

Your IAM role must have the following [permissions for WorkSpaces Advisor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspaces.html) to initiate investigations and retrieve recommendations. These include `workspaces:InvokeTroubleshootingInvestigation`, `workspaces:GetTroubleshootingRecommendation`, and `workspaces:ListTroubleshootingRecommendations`.

Your IAM role must have read permissions for WorkSpaces and Amazon CloudWatch APIs, such as `workspaces:DescribeWorkSpaces` and `cloudwatch:GetMetricData`. If your role is missing permissions for specific checks, WorkSpaces Advisor skips those checks and displays a message so you can update your permissions.

#### Permissions for remediation actions
<a name="workspaces-advisor-permissions-write"></a>

Your IAM role must have permission to perform the specific action (for example, `workspaces:RebootWorkSpaces` or `workspaces:ModifyWorkSpaceProperties`). If your role does not have the required permission, WorkSpaces Advisor returns an error.

## Security for proactive troubleshooting for your WorkSpaces fleet
<a name="workspaces-advisor-security-fleet"></a>

### What data it uses, and why
<a name="workspaces-advisor-security-fleet-data"></a>

Advisor uses the following data to detect issues that affect groups of WorkSpaces and to diagnose their likely cause:
+ **Health and performance signals**: WorkSpace health and connection status, sign-in and session setup outcomes, and CPU, memory, and disk use. Used to detect when WorkSpaces behave differently from your fleet's baseline, and to forecast when they'll run short of resources.
+ **Configuration**: directory, subnet, bundle, and compute type. Used to group WorkSpaces that share a configuration, so a shared cause is reported as one issue.
+ **Process names**: when a resource is running out, the names of the processes using the most of it. Used to point you to the likely cause.
+ **Certificate metadata**: expiry dates and status for trusted device certificates and for AWS Private CA certificates used for certificate-based authentication. Used to warn you before sign-in breaks. Advisor doesn't read private keys.
+ **No session content**: Advisor doesn't read what's on the screen, keystrokes, files, or clipboard contents.

### Data protection
<a name="workspaces-advisor-security-fleet-protection"></a>
+ Data is encrypted in transit with TLS 1.2 or later.
+ Data at rest is encrypted with AWS Key Management Service (AWS KMS).
+ Detected issues are visible only in your AWS account, to IAM principals that have permission to view them.

### Permissions
<a name="workspaces-advisor-security-fleet-permissions"></a>

To view the issues that Advisor detects, your IAM identity needs the following permissions: `workspaces:ListWorkspaceProactiveRecommendations`, `workspaces:GetWorkspaceProactiveRecommendation`, and `workspaces:ListWorkspaceProactiveRecommendationResources`. Without them, you can't view detected issues. You decide whether to take a recommended action, and you take it with your own permissions.

### Logging
<a name="workspaces-advisor-security-fleet-logging"></a>
+ Taking a recommended action calls the related WorkSpaces API, which is recorded in AWS CloudTrail like any other API call.

### Availability
<a name="workspaces-advisor-security-fleet-availability"></a>
+ Proactive troubleshooting doesn't affect how your WorkSpaces run or how users connect. If it's unavailable, your WorkSpaces work as usual, and new issues aren't shown until it recovers.

## Security for proactive troubleshooting for your WorkSpaces users
<a name="workspaces-advisor-security-users"></a>

In the console and the API, this capability is the End User Advisor self-service permission. It's turned on by default.

### What data it uses, and why
<a name="workspaces-advisor-security-users-data"></a>

To work out where a problem is, on the user's computer, on their network, or on the WorkSpace, and to recommend the right next step, Advisor uses the following data. For example, if a user's WorkSpace seems slow, the CPU, memory, and disk status of both the user's computer and the WorkSpace shows which one is causing it.
+ **Resource status on the user's computer and on the WorkSpace**: CPU, memory, and disk use (for the WorkSpace, root volume use). Used to tell whether a slow or frozen session is caused by the user's computer or by the WorkSpace.
+ **Network and streaming quality**: latency, packet loss, frame rate, and dropped frames. Used to tell whether the network is causing the problem.
+ **Process names**: when the WorkSpace is short of CPU or memory, the names of the processes using the most of it. Shown to the user in the recommendation, so they know which apps to close.
+ **Connection events**: registration, sign-in, session setup, connection, and disconnection outcomes. Used to explain why a user can't connect or why a session ended.
+ **No session content**: Advisor doesn't read what's on the screen, keystrokes, files, or clipboard contents.

### Data protection
<a name="workspaces-advisor-security-users-protection"></a>
+ All traffic between the WorkSpaces client and Advisor is encrypted with TLS 1.2 or later.
+ Advisor data at rest is encrypted with AWS KMS.
+ Each user can see only the recommendations for their own session. The client presents a session-specific token, which Advisor validates before it returns any recommendation.

### Permissions
<a name="workspaces-advisor-security-users-permissions"></a>

Users don't need IAM permissions to see recommendations. To let an administrator turn End User Advisor on or off, grant only the permission they need, scoped to the directory:

```json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": "workspaces:ModifySelfservicePermissions",
        "Resource": "arn:aws:workspaces:{{us-east-1}}:{{123456789012}}:directory/{{d-1234567890}}"
    }]
}
```

To view the setting, the administrator also needs `workspaces:DescribeWorkspaceDirectories`.

### Logging
<a name="workspaces-advisor-security-users-logging"></a>
+ Changes to the End User Advisor setting are recorded in AWS CloudTrail as ModifySelfservicePermissions events.

### Availability
<a name="workspaces-advisor-security-users-availability"></a>
+ If End User Advisor is turned off or unavailable, users connect to and use their WorkSpaces as usual. They don't see recommendations.

## Cross-Region Inference
<a name="workspaces-advisor-cross-region-inference"></a>

Model inference is the process of a model generating an output (response) from a given input (prompt). To use an optimal model for each feature, WorkSpaces Advisor might use [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for data processing. This means WorkSpaces Advisor will automatically select the optimal AWS Region to process inference requests. The available AWS Regions vary based on the region of your WorkSpaces resource. All data is transmitted encrypted across Amazon's secure network and does not traverse the public internet.

The following table lists the inference regions that WorkSpaces Advisor might use:


| Amazon WorkSpaces resource Region | Inference Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Africa (Cape Town) (af-south-1) | Africa (Cape Town) (af-south-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Malaysia) (ap-southeast-5) | Asia Pacific (Malaysia) (ap-southeast-5)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Mumbai) (ap-south-1) | Asia Pacific (Mumbai) (ap-south-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Seoul) (ap-northeast-2) | Asia Pacific (Seoul) (ap-northeast-2)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Singapore) (ap-southeast-1) | Asia Pacific (Singapore) (ap-southeast-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Canada (Central) (ca-central-1) | Canada (Central) (ca-central-1)<br />US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Paris) (eu-west-3) | Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2)<br />Europe (Stockholm) (eu-north-1) | 
| Europe (London) (eu-west-2) | Europe (London) (eu-west-2)<br />Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2)<br />Europe (Stockholm) (eu-north-1) | 
| Israel (Tel Aviv) (il-central-1) | Israel (Tel Aviv) (il-central-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| South America (Sao Paulo) (sa-east-1) | South America (Sao Paulo) (sa-east-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 

## Opting out of using your content for service improvement
<a name="workspaces-advisor-opt-out"></a>

As described in the AWS Service Terms, AWS may use and store WorkSpaces AI Content to develop and improve Amazon WorkSpaces and its underlying technologies. You can opt out of having your WorkSpaces AI Content used for this purpose by configuring an AI services opt-out policy in AWS Organizations. For more information, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.