# Getting started with AWS Audit Manager

Use the step-by-step tutorials in this section to learn how to perform tasks using AWS Audit Manager.

###### Tip

The following tutorials are categorized by audience. Choose the tutorial that's
appropriate for you based on your role as an _audit owner_ or
_delegate_.

- **Audit owners** are Audit Manager users who are responsible for
  creating and managing assessments. In the business world, audit owners are typically
  governance, risk management, and compliance (GRC) professionals. In the context of Audit Manager,
  however, individuals from SecOps or DevOps teams might also assume the user persona of an
  audit owner. Audit owners can request assistance from a subject matter expert—also
  known as a delegate—to review specific controls and validate evidence. Audit owners
  must have the necessary permissions to manage an assessment.
- **Delegates** are subject matter experts with specialized
  technical or business expertise. Although they don't own or manage Audit Manager assessments, they
  can still contribute to them. Delegates assist audit owners with tasks such as validating
  evidence for the controls that fall under their area of expertise. Delegates have limited
  permissions in Audit Manager. This is because audit owners delegate specific control sets for
  review, and not entire assessments.
  For more information about these personas and other Audit Manager concepts, see [audit owner](concepts.md#audit-owner "concepts.md#audit-owner") and [delegate](concepts.md#delegate-persona "concepts.md#delegate-persona") in the [Understanding AWS Audit Manager concepts and terminology](concepts.md "concepts.md") section of this guide.

For more information about the recommended IAM permissions for each persona, see [Recommended policies for user personas in AWS Audit Manager](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas").

## Audit Manager tutorials

**[Creating an
assessment](tutorial-for-audit-owners.md "tutorial-for-audit-owners.md")**

**Audience:** Audit owners

**Overview:** Follow step-by-step instructions to
create your first assessment and get up and running fast. This tutorial walks you
through how you can use a standard framework to create an assessment and begin the
automated collection of evidence.

**[Reviewing a control
set](tutorial-for-delegates.md "tutorial-for-delegates.md")**

**Audience:** Delegates

**Overview:** Assist an audit owner by reviewing
evidence for controls that fall under your area of expertise. Learn to review control
sets and their related evidence, add comments, upload evidence, and update the status of
a control.
