# Security for cost management capabilities in Amazon Q

Developer

The following provides an overview of permissions and data protection for the cost
management capabilities in Amazon Q Developer.

## Cost analysis permissions

All cost data provided by Amazon Q Developer is sourced from Cost Explorer. The IAM user who
accesses the cost analysis capability in Amazon Q Developer must have permissions to
use Amazon Q Developer and permissions to retrieve cost and usage data from Cost Explorer.
The quickest way for an administrator to grant users access to Amazon Q Developer is to use
the `AmazonQFullAccess` managed policy.

The following IAM policy statement grants users access to the cost analysis
capability in Amazon Q Developer:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnablesCostAnalysisInAmazonQ",
 "Effect": "Allow",
 "Action": [
 "q:StartConversation",
 "q:SendMessage",
 "q:GetConversation",
 "q:ListConversations",
 "q:PassRequest",
 "ce:GetCostAndUsage",
 "ce:GetCostForecast",
 "ce:GetDimensionValues",
 "ce:GetTags",
 "ce:GetCostCategories"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Cost optimization

permissions

The following IAM policy statement grants users access to the cost optimization
capability in Amazon Q Developer:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnablesCostOptimizationInAmazonQ",
 "Effect": "Allow",
 "Action": [
 "q:StartConversation",
 "q:SendMessage",
 "q:GetConversation",
 "q:ListConversations",
 "q:PassRequest",
 "cost-optimization-hub:GetRecommendation",
 "cost-optimization-hub:ListRecommendations",
 "cost-optimization-hub:ListRecommendationSummaries",
 "compute-optimizer:GetAutoScalingGroupRecommendations",
 "compute-optimizer:GetEBSVolumeRecommendations",
 "compute-optimizer:GetEC2InstanceRecommendations",
 "compute-optimizer:GetECSServiceRecommendations",
 "compute-optimizer:GetLambdaFunctionRecommendations",
 "compute-optimizer:GetRDSDatabaseRecommendations",
 "compute-optimizer:GetIdleRecommendations",
 "compute-optimizer:GetEffectiveRecommendationPreferences",
 "ce:GetReservationPurchaseRecommendation",
 "ce:GetSavingsPlansPurchaseRecommendation"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Pricing and cost estimation

permissions

The following IAM policy statement grants users access to the pricing and cost
estimation capability in Amazon Q Developer:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnablesCostOptimizationInAmazonQ",
 "Effect": "Allow",
 "Action": [
 "q:StartConversation",
 "q:SendMessage",
 "q:GetConversation",
 "q:ListConversations",
 "q:PassRequest",
 "pricing:DescribeServices",
 "pricing:GetAttributeValues",
 "pricing:GetProducts"
 ],
 "Resource": "*"
 }
 ]
}`

```

## q:PassRequest permission

`q:PassRequest` is an Amazon Q Developer permission that allows Amazon Q Developer to call AWS
APIs on your behalf. When you add the `q:PassRequest` permission to an
IAM identity, Amazon Q Developer gains permission to call any API that the IAM identity has
permission to call. For example, if an IAM role has the
`ce:GetCostAndUsage` permission and the `q:PassRequest`
permission, Amazon Q Developer can call the GetCostAndUsage API when a user assuming that
IAM role asks Amazon Q Developer to retrieve cost and usage data from Cost Explorer.

You can also allow IAM principals to access Cost Explorer and to use Amazon Q Developer,
but restrict them from using the cost analysis or cost optimization capabilities in
Amazon Q Developer, by using the `aws:CalledVia`
[global condition key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia"). The following IAM policy
provides an example of using this condition key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "q:StartConversation",
 "q:SendMessage",
 "q:GetConversation",
 "q:ListConversations",
 "q:PassRequest",
 "ce:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ce:*"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "q.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

For users of AWS Organizations, management account administrators can restrict member
account users’ access to Cost Explorer and Cost Optimization Hub data (including access to
discounts, credits, and refunds) using the Cost Management preferences in the AWS
Billing and Cost Management console. These preferences apply to Amazon Q Developer in the
same way that they apply to the management console, SDK, and CLI. Amazon Q Developer
respects the existing preferences of customers. Note that the pricing and cost
estimation capabilities in Amazon Q Developer only provide public pricing data;
customer-specific discounts are not reflected.

## Cross-region calls

Data from the Cost Optimization Hub and Cost Explorer services is hosted in the US East (N. Virginia) Region. Data
from AWS Compute Optimizer is hosted in the AWS Region where the underlying resources, such as
EC2 instances, are located. Data served from the AWS Price List APIs is hosted in
us-east-1, eu-central-1, and ap-south-1 (note that AWS Price List APIs do not
serve any customer-specific data). Cost management requests in Amazon Q Developer may
require cross-region calls. For more information, see [Cross-region processing in Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md "../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md") in the
_Amazon Q Developer User Guide_.

## Data protection

We may use certain content from Amazon Q Developer Free Tier for service improvement. Amazon Q Developer
may use this content, for example, to provide better responses to common questions,
fix Amazon Q Developer operational issues, for debugging, or for model training. Content
that AWS may use for service improvement includes, for example, your questions to
Amazon Q Developer and the responses and code that Amazon Q Developer generates. We do not use
content from Amazon Q Developer Pro or Amazon Q Business for service improvement.

The way you opt out of Amazon Q Developer Free Tier using content for service improvement depends
on the environment where you use Amazon Q. For the AWS Management Console, AWS
Console Mobile Application, AWS websites, and AWS Chatbot, configure an AI
services opt-out policy in AWS Organizations. For more information, see [AI services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS
Organizations User Guide_. In the IDE, for Amazon Q Developer Free Tier,
adjust your settings in the IDE. For more information, see [Opt out
of data sharing in the IDE](../../../amazonq/latest/qdeveloper-ug/opt-out-IDE.md "../../../amazonq/latest/qdeveloper-ug/opt-out-IDE.md") in the _Amazon Q Developer User
Guide_.
