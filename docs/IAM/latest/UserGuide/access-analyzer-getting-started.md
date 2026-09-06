

# Getting started with AWS Identity and Access Management Access Analyzer
<a name="access-analyzer-getting-started"></a>

Use the information in this topic to learn about the requirements necessary to use and manage AWS Identity and Access Management Access Analyzer.

If you are using IAM Access Analyzer within an AWS Organizations organization, you can [Add a delegated administrator for IAM Access Analyzer](access-analyzer-delegated-administrator-add.md). For information about service limits, see [IAM Access Analyzer quotas](access-analyzer-quotas.md).

## Permissions required to use IAM Access Analyzer
<a name="access-analyzer-permissions"></a>

To successfully configure and use IAM Access Analyzer, the account you use must be granted the required permissions. 

### AWS managed policies for IAM Access Analyzer
<a name="access-analyzer-permissions-awsmanpol"></a>

AWS Identity and Access Management Access Analyzer provides AWS managed policies to help you get started quickly.
+ [IAMAccessAnalyzerFullAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMAccessAnalyzerFullAccess) - Allows full access to IAM Access Analyzer for administrators. This policy also allows creating the service-linked roles that are required to allow IAM Access Analyzer to analyze resources in your account or AWS organization.
+ [IAMAccessAnalyzerReadOnlyAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMAccessAnalyzerReadOnlyAccess) - Allows read-only access to IAM Access Analyzer. You must add additional policies to your IAM identities (users, groups of users, or roles) to allow them to view their findings.

### Resources defined by IAM Access Analyzer
<a name="permission-resources"></a>

To view the resources defined by IAM Access Analyzer, see [Resource types defined by IAM Access Analyzer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamaccessanalyzer.html#awsiamaccessanalyzer-resources-for-iam-policies) in the *Service Authorization Reference*.

### Required IAM Access Analyzer service permissions
<a name="access-analyzer-permissions-service"></a>

IAM Access Analyzer uses a service-linked role (SLR) named `AWSServiceRoleForAccessAnalyzer`. This SLR grants the service read-only access to analyze AWS resources with resource-based policies and analyze unused access on your behalf. The service creates the role in your account in the following scenarios:
+ You create an external access analyzer with your account as the zone of trust.
+ You create an unused access analyzer with your account as the selected account.
+ You create an internal access analyzer with your account as the zone of trust.

For more information, see [Using service-linked roles for AWS Identity and Access Management Access Analyzer](access-analyzer-using-service-linked-roles.md).

**Note**  
IAM Access Analyzer is Regional. For external and internal access, you must enable IAM Access Analyzer in each Region independently.  
For unused access, findings for the analyzer do not change based on Region. Creating an analyzer in each Region where you have resources is not required.

In some cases, after you create an analyzer in IAM Access Analyzer, the **Findings** page or dashboard loads with no findings or summary. This might be due to a delay in the console for populating your findings. You might need to manually refresh the browser or check back later to view your findings or summary. If you still don't see any findings for an external access analyzer, it's because you have no supported resources in your account that can be accessed by an external entity. If a policy that grants access to an external entity is applied to a resource, IAM Access Analyzer generates a finding.

**Note**  
For external access analyzers, it may take up to 30 minutes after a policy is modified for IAM Access Analyzer to analyze the resource and then either generate a new finding or update an existing finding for the access to the resource.  
When you create an internal access analyzer, it might take several minutes or hours before findings are available. After the initial scan, IAM Access Analyzer automatically rescans all policies every 24 hours.  
For all types of access analyzers, updates for findings might not be reflected in the dashboard immediately.

### Required IAM Access Analyzer permissions to view the findings dashboard
<a name="access-analyzer-permissions-dashboard"></a>

To view the [IAM Access Analyzer findings dashboard](access-analyzer-dashboard.md), the account you use must be granted access to perform the following required actions:
+ [`GetAnalyzer`](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html)
+ [`ListAnalyzers`](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html)
+ [`GetFindingsStatistics`](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingsStatistics.html)

To view all of the actions defined by IAM Access Analyzer, see [Actions defined by IAM Access Analyzer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamaccessanalyzer.html#awsiamaccessanalyzer-actions-as-permissions) in the *Service Authorization Reference*.

## IAM Access Analyzer status
<a name="access-analyzer-status"></a>

To view the status of your analyzers, choose **Analyzers**. Analyzers created for an organization or account can have the following status:


| Status | Description | 
| --- | --- | 
| Active | For external and internal access analyzers, the analyzer is actively monitoring resources within its zone of trust. The analyzer actively generates new findings and updates existing findings.<br />For unused access analyzers, the analyzer is actively monitoring unused access within the selected organization or AWS account in the specified tracking period. The analyzer actively generates new findings and updates existing findings. | 
| Creating | The creation of the analyzer is still in progress. The analyzer becomes active once creation is complete. | 
| Disabled | The analyzer is disabled due to an action taken by the AWS Organizations administrator. For example, removing the analyzer’s account as the delegated administrator for IAM Access Analyzer. When the analyzer is in a disabled state, it does not generate new findings or update existing findings. | 
| Failed | The creation of the analyzer failed due to a configuration issue. The analyzer won't generate any findings. Delete the analyzer and create a new analyzer. | 