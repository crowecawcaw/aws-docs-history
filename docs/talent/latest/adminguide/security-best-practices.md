

# Security best practices for Amazon Connect Talent
<a name="security-best-practices"></a>

Amazon Connect Talent provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

**Topics**
+ [Detective](#security-best-practices-detective)
+ [Preventative](#security-best-practices-preventative)

## Detective
<a name="security-best-practices-detective"></a>

Use the following detective controls to monitor activity and detect potential security issues in Amazon Connect Talent.
+ Use CloudTrail to log and review administrative and evaluation actions in your account. For more information, see [Logging Amazon Connect Talent API calls using AWS CloudTrail](logging-using-cloudtrail.md).
+ Use the AWS Security Hub CSPM integration to review security findings for Amazon Connect Talent alongside findings from your other AWS resources. For more information, see [Integration with AWS Security Hub CSPM](securityhub-integration.md).

## Preventative
<a name="security-best-practices-preventative"></a>

Use the following preventative controls to reduce security risk in Amazon Connect Talent.
+ Apply least-privilege security profiles, and restrict who can review candidate results and interview transcripts. For more information, see [Identity and access management for Amazon Connect Talent](security-iam.md).
+ If your organization requires it, opt out of the use of your content to improve Amazon Connect Talent and other AWS AI services. For more information, see [Opting out of data use for service improvement](data-opt-out.md).