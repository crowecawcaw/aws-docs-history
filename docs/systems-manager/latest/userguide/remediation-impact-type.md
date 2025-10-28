# Remediation impact types of runbook

actions

Systems Manager can run diagnosis operations that discover certain types of failed deployments
and drifted configurations, as well as certain types of configuration issues that are
preventing Systems Manager from managing EC2 instances. The results of the diagnosis might include
recommendations for Automation runbooks that you can execute to attempt to remedy a
problem. For more information about these diagnosis operations, see the following
topics:

- [Diagnosing and remediating failed
  deployments](remediating-deployment-issues.md "remediating-deployment-issues.md")
- [Diagnosing and remediating drifted
  configurations](remediating-configuration-drift.md "remediating-configuration-drift.md")
- [Diagnosing and remediating unmanaged
  Amazon EC2 instances in Systems Manager](remediating-unmanaged-instances.md "remediating-unmanaged-instances.md")
  When Systems Manager identifies an issue that might be fixed by running an Automation runbook on
  the affected resources, it provides you with an _execution
  preview_. The execution preview provides information about the _types_ of changes the runbook execution would make to your
  targets. This information includes how many of each of three types of changes the
  diagnosis identified.

These change types are as follows:

- `Mutating`: A runbook step would make changes to the targets
  through actions that create, modify, or delete resources.
- `Non-Mutating`: A runbook step would retrieve data about resources
  but not make changes to them. This category generally includes
  `Describe*`, `List*`, `Get*`, and similar
  read-only API actions.
- `Undetermined`: An undetermined step invokes executions performed
  by another orchestration service like AWS Lambda, AWS Step Functions, or Run Command, a tool
  in AWS Systems Manager. An undetermined step might also call a third-party API or run a
  Python or PowerShell script. Systems Manager Automation can't detect what the outcome
  would be of the orchestration processes or third-party API executions, and
  therefore can't evaluate them. The results of those steps would have to be
  manually reviewed to determine their impact.

See the following table for information about the impact type of supported
Automation actions.

## Impact types of supported remediation

actions

The table presents the impact type—Mutating, Non-mutating, and
Undetermined—of various actions that can be included in a remediation
runbook.

| Action¹                        | Impact type                                 |
| ------------------------------ | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| aws:approve                    | Non-mutating                                |
| aws:assertAwsResourceProperty  | Non-mutating                                |
| aws:branch                     | Non-mutating                                |
| aws:changeInstanceState        | Mutating                                    |
| aws:copyImage                  | Mutating                                    |
| aws:createImage                | Mutating                                    |
| aws:createStack                | Mutating                                    |
| aws:createTags                 | Mutating                                    |
| aws:deleteImage                | Mutating                                    |
| aws:deleteStack                | Mutating                                    |
| aws:executeAutomation          | Undetermined                                |
| aws:executeAwsApi              | Undetermined                                |
| aws:executeScript              | Undetermined                                |
| aws:executeStateMachine        | Undetermined                                |
| aws:invokeLambdaFunction       | Undetermined                                |
| aws:invokeWebhook              | Undetermined                                |
| aws:loop                       | Varies. Depends on the actions in the loop. |
| aws:pause                      | Non-mutating                                |
| aws:runCommand                 | Undetermined                                |
| aws:runInstances               | Mutating                                    |
| aws:sleep                      | Non-mutating                                |
| aws:updateVariable             | Mutating                                    |
| aws:waitForAwsResourceProperty | Non-mutating                                | ¹ For more information about Automation actions, see [Systems Manager Automation actions reference](automation-actions.md "automation-actions.md"). |
