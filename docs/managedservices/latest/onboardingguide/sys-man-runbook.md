# Use AMS SSP to provision AWS Systems Manager Automation in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Systems Manager Automation capabilities directly in your AMS managed account. AWS Systems Manager Automation simplifies common maintenance and deployment tasks of Amazon Elastic Compute Cloud instances and other AWS resources
using runbooks, actions and service quotas. It enables you to build, execute and monitor automations at scale. A Systems Manager
Automation is a type of Systems Manager document that defines the actions that
Systems Manager performs on your managed instances. A runbook you use to perform common maintenance and deployment tasks
such as running commands or automation scripts within your managed instances. Systems Manager includes features that
help you target large groups of instances by using Amazon Elastic Compute Cloud tags, and velocity controls that help you roll out changes
according to the limits you define. The runbooks are written using JavaScript Object Notation (JSON) or YAML. Using the
Document Builder in the Systems Manager Automation console, however, you can create a runbook without having to author
in native JSON or YAML. Alternatively you can use Systems Manager-provided runbooks with pre-defined steps that suits your
needs. To learn more, see
[Working with runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md")
in AWS Systems Manager documentation.

###### Note

Although Systems Manager Automation supports 20 action types that can be used in the runbook, a limited number of actions
you can use while authoring runbook to be used in your AMS Advanced account. Similarly, a limited number of
Systems Manager-provided runbook can be used either directly or from within your own runbook. For details, see
the restrictions in the following FAQ.

## AWS Systems Manager Automation in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Systems Manager Automation in my AMS account?**

Request access to AWS Systems Manager Automation by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account:
`customer_systemsmanager_automation_console_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the limitations to using AWS Systems Manager Automation in my AMS account?**

You are required to author your runbook, with limited set of Systems Manager supported actions for
automation, only to run commands and/or scripts within your managed instances. The actions that are available
to you along with any restrictions are outlined as below.

| AWS Systems Manager Automation Limitations | Action                                      | Description                                                                                     | Limitation |
| ------------------------------------------ | ------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| aws:assertAwsResourceProperty –            | Assert an AWS resource state or event state | Only EC2 instances                                                                              |
| aws:aws:branch –                           | Run conditional automation steps            | No limitation                                                                                   |
| aws:createTags –                           | Create tags for AWS resources               | Only to SSM automation runbooks that you author                                                 |
| aws:executeAutomation –                    | Run another automation                      | Only the automation runbook that you author                                                     |
| aws:executeScript –                        | Run a script                                | Only script that does not make any API call to any services                                     |
| aws:pause –                                | Pause an automation                         | No limitation                                                                                   |
| aws:runCommand –                           | Run a command on a managed instance         | Only using System Manager provided document<br>• AWS-RunShellScript and AWS-RunPowerShellScript |
| aws:sleep –                                | Delay an automation                         | No limitation                                                                                   |
| aws:waitForAwsResourceProperty –           | Wait on an AWS resource property            | Only EC2 instances                                                                              |

You can also chose to run command or script directly with Systems Manager provided runbook
AWS-RunShellScript and AWS-RunPowerShellScript using the 'Run Command' feature from within the Systems Manager
console. You can also nest these runbooks within your runbook that caters for additional pre and/or post
validation or any complex automation logic.

The role adheres to least privilege principle and only provides permission required to author, execute and
retrieve execution details of runbooks aimed to executing command and/or scripts within your managed
instances. It does not provide permission for any other capabilities that AWS Systems Manager service
provides. While the feature allows you to author automation runbooks, execution of the runbooks can not be
targeted for AMS owned resources.

**Q: What are the prerequisites or dependencies to using AWS Systems Manager Automation in my
AMS account?**

There are no prerequisites; however, you must ensure your internal process and/or compliance controls are
adhered to while authoring runbooks. We also recommend to thoroughly test runbooks before executing them
against production resources.

**Q: Can the Systems Manager policy `customer_systemsmanager_automation_policy` be
attached to other IAM roles?**

No, unlike other self-provision enabled services, this policy can only be assigned to the provisioned default
role `customer_systemsmanager_automation_console_role`.

Unlike the policies of other SSPS roles, this SSM SSPS policy cannot be shared with other custom IAM roles, because this
AMS service is only for running commands or automation scripts within your managed instances.
If these permissions were allowed to be attached to other custom IAM roles, potentially with permissions on other
services, the scope of allowed actions could extend to managed services, and potentially lower the security
posture of your account.

To evaluate any requests for change (RFCs) against our AMS technical standards, work with your respective
Cloud Architect or Service Delivery Manager, see
[RFC security reviews](../ctref/rfc-security.md "../ctref/rfc-security.md").

###### Note

AWS Systems Manager allows you to use runbooks that are shared with your account. We recommend you exercise caution and perform
a due-diligence check when using shared runbooks and make sure to review the content to understand the command/scripts they
run before executing the runbooks. For details refer to
[Best practices for shared SSM documents](../../../systems-manager/latest/userguide/ssm-before-you-share.md "../../../systems-manager/latest/userguide/ssm-before-you-share.md").
