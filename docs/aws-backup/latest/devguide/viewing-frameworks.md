# Viewing framework compliance status

Once you create an audit framework, it appears in your **Frameworks**
table. You can view this table by choosing **Frameworks** in the left
navigation pane of the AWS Backup console. To view the audit results for your framework, choose
its **Framework name**. Doing so takes you to the **Framework
detail** page, which has two sections: **Summary** and
**Controls**.

The **Summary** section lists the following statuses from left to
right:

- **Compliance status** is your audit framework’s overall compliance
  status as determined by the compliance status of each of its controls. Each control’s
  compliance status is determined by the compliance status of each resource it
  evaluates.

Framework compliance status is `Compliant` only if all resources in the
scope of your control evaluations have passed those evaluations. If one or more
resources failed a control evaluation, the compliance status will be
`Non-Compliant`. For information on how to find your non-compliant
resources, see [Finding
non-compliant resources](finding-non-compliant-resources.md "finding-non-compliant-resources.md"). For information on how to bring your resources into
compliance, see the remediation section of [AWS Backup Audit Manager
controls and remediation](controls-and-remediation.md "controls-and-remediation.md").

- **Framework status** refers to whether you have turned on resource
  tracking for all of your resources. The possible statuses are:
  - `Active` when recording is turned on for all resources the framework
    evaluates.
  - `Partially active` when recording is turned off for at least one
    resource the framework evaluates.
  - `Inactive` when recording is turned off for all resources that the
    framework evaluates.
  - `Unavailable` when AWS Backup Audit Manager is unable to validate
    recording status at this time.

###### To correct a `Partially active` or `Inactive`

status

    1. Choose **Frameworks** from the left navigation pane.
    2. Choose **Manage resource tracking**.
    3. Follow the instructions in the pop-up to enable recording that were previously
     not enabled for your resource types.

For more information about which resource types require resource tracking based on
the controls you included in your frameworks, see the resource component of [AWS Backup Audit Manager controls and remediation](controls-and-remediation.md "controls-and-remediation.md").

- **Deployment status** refers to your framework’s deployment status.
  This status should most often be `Completed`, but can also be `Create in
progress`, `Update in progress`, `Delete in progress`, and
  `Failed`.
  - A status of `Failed` means the framework didn't deploy correctly.
    [Delete the framework](deleting-frameworks.md "deleting-frameworks.md"),
    then recreate the framework through the [AWS Backup console](creating-frameworks-console.md "creating-frameworks-console.md") or through [AWS Backup API](creating-frameworks-api.md "creating-frameworks-api.md").

- **Compliant controls** show a count of framework controls with all
  evaluations passing.
- **Non-compliant controls** show a count of framework controls with
  at least one evaluation not passing.
  The **Controls** section shows you the following information:

- **Control status** refers to each control's compliance status. A
  control can be `Compliant`, meaning all resources pass that evaluation;
  `Non-compliant`, meaning that at least one resource did not pass that
  evaluation, or `Insufficient data`, meaning the control found no resources
  within the evaluation scope to evaluate.
- **Evaluation scope** might limit each control to one or more
  **Resource types**, one **Resource ID**, or one
  **Tag key** and **Tag value**, based on how you
  customized your control when creating your audit framework. If all fields are empty (as
  shown by a dash, "-"), then the control evaluates all applicable resources.
