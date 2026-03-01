# Tutorial for Audit Owners: Creating an assessment

This tutorial provides an introduction to AWS Audit Manager. In this tutorial, you create an
assessment using the [AWS Audit Manager Sample Framework](Sample.md "Sample.md"). By creating an
assessment, you start the ongoing process of automated evidence collection for the controls in
that framework.

###### Note

AWS Audit Manager assists in collecting evidence that's relevant for verifying compliance with
specific compliance frameworks and regulations. However, it doesn't assess your compliance
itself. The evidence that's collected through AWS Audit Manager therefore might not include all the
information about your AWS usage that's needed for audits. AWS Audit Manager isn't a substitute for
legal counsel or compliance experts.

## Prerequisites

###### Before you start this tutorial, make sure that you meet the following conditions:

- You completed all the prerequisites that are described in [Setting up AWS Audit Manager with the recommended settings](setting-up.md "setting-up.md"). You must use your AWS account and the AWS Audit Manager console
  to complete this tutorial.
- Your IAM identity is granted with the appropriate permissions to create and manage
  an assessment in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").
- You're familiar with Audit Manager terminology and functionality. For a general overview, see
  [What is AWS Audit Manager?](what-is.md "what-is.md") and [Understanding AWS Audit Manager concepts and terminology](concepts.md "concepts.md").

## Procedure

###### Tasks

- [Step 1: Specify assessment details](#select-framework "#select-framework")
- [Step 2: Specify AWS accounts in scope](#specifyaccounts "#specifyaccounts")
- [Step 3: Specify audit owners](#chooseauditowners "#chooseauditowners")
- [Step 4: Review and create](#reviewcreate "#reviewcreate")

### Step 1: Specify assessment details

For the first step, select a framework and provide basic information for your
assessment.

###### To specify assessment details

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. Choose **Launch AWS Audit Manager**.
3. In the green banner at the top of the screen, choose **Start with a
   framework**.
4. Choose the framework that you want, and then choose **Create assessment
   from framework**. For this tutorial, use the **AWS Audit Manager Sample
   Framework**.
5. Under **Assessment name**, enter a name for your assessment.
6. (Optional) Under **Assessment description**, enter a description
   for your assessment.
7. Under **Assessment reports destination**, choose the S3 bucket
   where you want to save your assessment reports.
8. Under **Frameworks**, confirm that **AWS Audit Manager Sample
   Framework** is selected.
9. (Optional) Under **Tags**, choose **Add new
   tag** to associate a tag with your assessment. You can specify a key and a
   value for each tag. The tag key is mandatory and can be used as a search criteria when
   you search for this assessment.
10. Choose **Next**.

### Step 2: Specify AWS accounts in scope

Next, specify the AWS accounts that you want to include in the scope of your
assessment.

AWS Audit Manager integrates with AWS Organizations, so you can run an Audit Manager assessment across multiple
accounts and consolidate evidence into a delegated administrator account. To enable Organizations
in Audit Manager (if you didn't do so already), see [Enable and set up AWS Organizations](setup-recommendations.md#enabling-orgs "setup-recommendations.md#enabling-orgs") on the _Setting up_
page of this guide.

###### Note

Audit Manager can support up to 200 accounts in the scope of an assessment. If you try to
include over 200 accounts, the assessment creation will fail.

Additionally, if you try to add over 250 unique accounts across all of your
assessments, the assessment creation will fail.

###### To specify accounts in scope

1. Under **AWS accounts**, select the AWS accounts that you
   want to include in the scope of your assessment.
   - If you enabled Organizations in Audit Manager, multiple accounts are listed.
   - If you didn't enable Organizations in Audit Manager, only your current account is listed.

2. Choose **Next**.

### Step 3: Specify audit owners

In this step, you specify the audit owners for your assessment. Audit owners are the
individuals in your workplace—usually from GRC, SecOps, or DevOps teams—who
are responsible for managing the Audit Manager assessment. We recommend that they use the [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") policy.

###### To specify audit owners

1. Under **Audit owners**, choose the audit owners for your
   assessment. To find additional audit owners, use the search bar to search by name or
   AWS account.
2. Choose **Next**.

### Step 4: Review and create

Review the information for your assessment. To change the information for a step,
choose **Edit**. When you're finished, choose **Create
assessment** to start the ongoing collection of evidence.

After you create an assessment, evidence collection continues until you [change
the assessment status](change-assessment-status-to-inactive.md "change-assessment-status-to-inactive.md") to _inactive_.
Alternatively, you can stop evidence collection for a specific control by [changing the
control status](change-assessment-control-status.md "change-assessment-control-status.md") to _inactive_.

###### Note

Automated evidence is available 24 hours after you create the assessment. Audit Manager
automatically collects evidence from multiple data sources, and the frequency of that
evidence collection is based on the evidence type. For more information, see [Evidence collection frequency](how-evidence-is-collected.md#frequency "how-evidence-is-collected.md#frequency") in this guide.

## Additional resources

We recommend that you continue to learn more about the concepts and tools that are
introduced in this tutorial. You can do so by reviewing the following resources:

- **[Reviewing assessment details in AWS Audit Manager](review-assessments.md "review-assessments.md") –** Introduces you to the
  assessment details page where you can explore the different components of your
  assessment.
- **[Managing assessments in AWS Audit Manager](assessments.md "assessments.md")
  –** Builds upon this tutorial and provides in-depth information about
  the concepts and tasks for managing an assessment. In this chapter, we particularly
  recommend you check out the following topics:
  - How to [create an
    assessment](create-assessments.md "create-assessments.md") from a different framework
  - How to [review the evidence in
    an assessment](review-evidence.md "review-evidence.md") and [generate an
    assessment report](generate-assessment-report.md "generate-assessment-report.md")
  - How to [change the status of
    an assessment](complete-assessment.md "complete-assessment.md") or [delete an
    assessment](delete-assessment.md "delete-assessment.md")

- **[Using the framework library to manage frameworks in AWS Audit Manager](framework-library.md "framework-library.md") –** Introduces the framework
  library and explains how to [create a custom
  framework](custom-frameworks.md "custom-frameworks.md") for your own specific compliance needs.
- **[Using the control library to manage controls in AWS Audit Manager](control-library.md "control-library.md") –** Introduces the control library
  and explains how to [create a custom
  control](create-controls.md "create-controls.md") for use in your custom framework.
- **[Understanding AWS Audit Manager concepts and terminology](concepts.md "concepts.md") –** Provides definitions for the concepts and terminology used in Audit Manager.
- [Video] Collect Evidence and Manage Audit Data Using AWS Audit Manager
  – Shows the assessment creation process that's described in this tutorial, and
  other tasks such as reviewing a control and generating an assessment report.
