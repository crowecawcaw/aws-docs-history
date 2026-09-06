

# Security Hub CSPM controls for Amazon Detective
<a name="detective-controls"></a>

This AWS Security Hub CSPM control evaluates the Amazon Detective service and resources. The control might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [Detective.1] Detective behavior graphs should be tagged
<a name="detective-1"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::Detective::Graph`

**AWS Config rule:** `tagged-detective-graph` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an Amazon Detective behavior graph has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the behavior graph doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the behavior graph isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="detective-1-remediation"></a>

To add tags to a Detective behavior graph, see [Adding tags to a behavior graph](https://docs.aws.amazon.com/detective/latest/adminguide/graph-tags.html#graph-tags-add-console) in the *Amazon Detective Administration Guide*.