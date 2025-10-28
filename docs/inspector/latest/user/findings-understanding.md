# Understanding Amazon Inspector findings

Amazon Inspector generates a finding when it detects a vulnerability with a fix or pending fix in Amazon EC2 instances, Amazon ECR containers images, and Lambda functions.
It also generates findings for code vulnerabilities detected in first-party application source code, third-party application dependencies, and Infrastructure as Code.
A finding is a detailed report about a vulnerability impacting one of your AWS resources.

Findings are named after vulnerabilities and provide severity ratings, information about impacted AWS resources and non AWS resources, and details that describe how to remediate detected vulnerabilities.
Amazon Inspector stores all of your active findings until you remediate them.

When a resource is deleted, terminated, or no longer eligible for scanning, Amazon Inspector automatically closes findings associated with the resource and then deletes the findings after 3 days.
If findings are closed for any other reason, they are deleted after 30 days.

###### Note

Amazon Inspector will reopen a remediated finding within seven days of closing the finding if the issue that caused the vulnerability reoccurs.

If you disable Amazon Inspector, findings are removed after 24 hours.
If a resource is terminated, any finding related to the resource is removed after 3 days.
The same occurs for any finding attached to a resource where scanning is no longer eligible.
If AWS suspends your account, findings are removed after 90 days.
Findings for stopped instances remain active.

###### Findings states

Amazon Inspector categorizes findings in the following states.

**Active**

Amazon Inspector categorizes a finding that hasn't been remediated as **Active**.

**Suppressed**

Amazon Inspector categorizes a finding subject to one or more [suppression rules](findings-managing-supression-rules.md "findings-managing-supression-rules.md") as **Suppressed**.

**Closed**

When a finding has been remediated, Amazon Inspector categorizes the finding as **Closed**.

###### Topics

- [Amazon Inspector finding types](findings-types.md "findings-types.md")
- [Viewing Amazon Inspector findings](findings-understanding-locating-analyzing.md "findings-understanding-locating-analyzing.md")
- [Viewing details for your Amazon Inspector findings](findings-understanding-details.md "findings-understanding-details.md")
- [Viewing the Amazon Inspector score and understanding vulnerability intelligence details](findings-understanding-score.md "findings-understanding-score.md")
- [Understanding severity levels for your Amazon Inspector findings](findings-understanding-severity.md "findings-understanding-severity.md")
