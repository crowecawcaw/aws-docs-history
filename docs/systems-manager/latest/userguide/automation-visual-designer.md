AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Visual design experience for Automation runbooks

AWS Systems Manager Automation provides a low-code visual design experience that helps you create automation
runbooks. The visual design experience provides a drag-and-drop interface with the option to add your own
code so you can create and edit runbooks more easily. With the visual design experience, you can do the
following:

- Control conditional statements.
- Control how input and output is filtered or transformed for each action.
- Configure error handling.
- Prototype new runbooks.
- Use your prototype runbooks as the starting point for local development with the
  AWS Toolkit for Visual Studio Code.
  When you create or edit a runbook, you can access the visual design experience from the [Automation console](https://console.aws.amazon.com/systems-manager/automation/home?region=us-east-1#/ "https://console.aws.amazon.com/systems-manager/automation/home?region=us-east-1#/"). As you create a runbook, the visual design experience validates your work and
  auto-generates code. You can review the generated code, or export it for local development. When
  you're finished, you can save your runbook, run it, and examine the results in the Systems Manager
  Automation console.

## Before you begin

To use the visual design experience, you need an AWS account, and credentials that provide the
correct permissions for any resources that you want to use.

In the visual design experience, Automation integrates with Amazon CodeGuru Security to help you detect
security policy violations and vulnerabilities in your Python scripts. To use
this feature for `aws:executeScript` actions, your AWS Identity and Access Management (IAM) policy must
include the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeguru-security:CreateUploadUrl",
 "codeguru-security:CreateScan",
 "codeguru-security:GetScan",
 "codeguru-security:GetFindings"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Topics

- [Interface overview](visual-designer-interface-overview.md "visual-designer-interface-overview.md")
- [Using the visual design experience](visual-designer-use.md "visual-designer-use.md")
- [Configure inputs and outputs](visual-designer-action-inputs-outputs.md "visual-designer-action-inputs-outputs.md")
- [Error handling with the visual design
  experience](visual-designer-error-handling.md "visual-designer-error-handling.md")
- [Tutorial: Create a runbook using the
  visual design experience](visual-designer-tutorial.md "visual-designer-tutorial.md")
