

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Integrating Audit Manager evidence into your GRC system
<a name="tutorial-for-grc-integration"></a>



As an enterprise customer, you likely have resources across multiple data centers, including other cloud vendors and on-premises environments. To collect evidence from these environments, you might use third-party GRC (Governance, Risk, and Compliance) solutions such as MetricStream CyberGRC or RSA Archer. Or, you might use a proprietary GRC system that you developed in-house.

This tutorial shows you how you can integrate your internal or external GRC system with Audit Manager. This integration enables vendors to collect evidence about their customers' AWS usage and configurations, and send that evidence directly from Audit Manager into the GRC application. By doing this, you can centralize your compliance reporting across multiple environments.

For the purpose of this tutorial:

1. A **vendor** is the entity or company who owns the GRC application that's being integrated with Audit Manager. 

1. A **customer** is the entity or company who uses AWS, and who also uses an internal or external GRC application.

**Note**  
In some cases, the GRC application is owned and used by same company. In this scenario, the **vendor** is the group or team who owns the GRC application, and the **customer** is the team or group that uses the GRC application.

**This tutorial shows you how to do the following:**
+ [Step 1: Enable Audit Manager](#tutorial-for-grc-integration-step1)
+ [Step 2: Set up permissions](#tutorial-for-grc-integration-step2)
+ [Step 3. Map your enterprise controls to Audit Manager controls](#tutorial-for-grc-integration-step3)
+ [Step 4. Keep your control mappings updated](#tutorial-for-grc-integration-step4)
+ [Step 5: Create an assessment](#tutorial-for-grc-integration-step5)
+ [Step 6. Start collecting evidence](#tutorial-for-grc-integration-step6)

## Prerequisites
<a name="tutorial-for-grc-integration-prerequisites"></a>

**Before you get started, make sure that you meet the following conditions:**
+ You have an infrastructure running in AWS.
+ You use an in-house GRC system, or you use third-party GRC software that’s provided by a vendor.
+ You completed all the [prerequisites](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-prerequisites.html) that are needed to [set up Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/setting-up.html). 
+ You're familiar with [Understanding AWS Audit Manager concepts and terminology](concepts.md). 

**Some restrictions to keep in mind:**
+ Audit Manager is a Regional AWS service. You must set up Audit Manager separately in each Region where you run your AWS workloads.
+ Audit Manager doesn’t support the aggregation of evidence from multiple Regions into a single Region. If your resources span across multiple AWS Regions, you must aggregate the evidence within your GRC system.
+ Audit Manager has default quotas for the number of resources you can create. You can request an increase to these default quotas if needed. For more information, see [Quotas and restrictions for AWS Audit Manager.](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html)

## Step 1: Enable Audit Manager
<a name="tutorial-for-grc-integration-step1"></a>

### Who completes this step
<a name="tutorial-for-grc-integration-step1-who"></a>

Customer

### What you need to do
<a name="tutorial-for-grc-integration-step1-what"></a>

Start by enabling Audit Manager for your AWS account. If your account is part of an organization, you can enable Audit Manager using your management account and then specify a delegated administrator for Audit Manager. 

### Procedure
<a name="tutorial-for-grc-integration-step1-procedure"></a>

**To enable Audit Manager**  
Follow the instructions to [Enable Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-audit-manager.html). Repeat the setup procedure for all Regions where you want to collect evidence.

**Tip**  
If you use AWS Organizations, we strongly recommend that you set up a delegated administrator during this step. When you use a delegated administrator account in Audit Manager, you can use evidence finder to search for evidence across all member accounts in your organization.

## Step 2: Set up permissions
<a name="tutorial-for-grc-integration-step2"></a>

### Who completes this step
<a name="tutorial-for-grc-integration-step2-who"></a>

Customer

### What you need to do
<a name="tutorial-for-grc-integration-step2-what"></a>

In this step, the customer creates an IAM role for their account. The customer then gives the vendor permissions to assume the role. 

![A diagram that shows how the IAM role grants access for the vendor account.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/vendor-role-access.png)


### Procedure
<a name="tutorial-for-grc-integration-step2-procedure"></a>

**To create a role for the customer account**  
Follow the instructions in [Creating a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide.*
+ In step 8 of the role creation workflow, choose **Create policy** and enter a policy for the role. 

  At minimum, the role must have the following permissions:

------
#### [ JSON ]

****  

  ```
  {
    "Version":"2012-10-17",		 	 	 
    "Statement" : [
      {
        "Sid" : "AuditManagerAccess",
        "Effect" : "Allow",
        "Action" : [
          "auditmanager:*"
        ],
        "Resource" : "*"
      },
      {
        "Sid" : "OrganizationsAccess",
        "Effect" : "Allow",
        "Action" : [
          "organizations:ListAccountsForParent",
          "organizations:ListAccounts",
          "organizations:DescribeOrganization",
          "organizations:DescribeOrganizationalUnit",
          "organizations:DescribeAccount",
          "organizations:ListParents",
          "organizations:ListChildren"
        ],
        "Resource" : "*"
      },
      {
        "Sid" : "IAMAccess",
        "Effect" : "Allow",
        "Action" : [
          "iam:GetUser",
          "iam:ListUsers",
          "iam:ListRoles"
        ],
        "Resource" : "*"
      },        
      {
        "Sid" : "S3Access",
        "Effect" : "Allow",
        "Action" : [
          "s3:ListAllMyBuckets"
        ],
        "Resource" : "*"
      },
      {
        "Sid" : "KmsAccess",
        "Effect" : "Allow",
        "Action" : [
          "kms:DescribeKey",
          "kms:ListKeys",
          "kms:ListAliases"
        ],
        "Resource" : "*"
      },
      {
        "Sid" : "KmsCreateGrantAccess",
        "Effect" : "Allow",
        "Action" : [
          "kms:CreateGrant"
        ],
        "Resource" : "*",
        "Condition" : {
          "Bool" : {
            "kms:GrantIsForAWSResource" : "true"
          },
          "StringLike" : {
            "kms:ViaService" : "auditmanager.*.amazonaws.com"
          }
        }
      },
      {
        "Sid" : "SNSAccess",
        "Effect" : "Allow",
        "Action" : [
          "sns:ListTopics"
        ],
        "Resource" : "*"
      }, 
      {
        "Sid" : "TagAccess",
        "Effect" : "Allow",
        "Action" : [
          "tag:GetResources"
        ],
        "Resource" : "*"
      }
    ]
  }
  ```

------
+ In step 11 of the role creation workflow, enter `vendor-auditmanager` as the **Role name**. 

**To allow the vendor account to assume the role**  
Follow the instructions in [Granting users permission to switch roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html) in the *IAM User Guide.*
+ The policy statement must include the `Allow` effect on the `sts:AssumeRole action`. 
+ It must also include the Amazon Resource Name (ARN) of the role in a Resource element. 
+ Here is an example policy statement you can use.

  In this policy, replace the {{placeholder text}} with your vendor’s AWS account ID.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": "arn:aws:iam::{{111122223333}}:role/vendor-auditmanager"
      }
  }
  ```

------

## Step 3. Map your enterprise controls to Audit Manager controls
<a name="tutorial-for-grc-integration-step3"></a>

### Who completes this step
<a name="tutorial-for-grc-integration-step3-who"></a>

Customer

### What you need to do
<a name="tutorial-for-grc-integration-step3-what"></a>

Vendors maintain a curated list of enterprise controls that customers can use in an assessment. To integrate with Audit Manager, vendors must create an interface that enables customers to map their enterprise controls to the corresponding Audit Manager controls. You can map to [](concepts.md#common-control)s (preferred), or [](concepts.md#standard-control)s. You must complete this mapping before you start any assessments in the vendor’s GRC application.

![A diagram that shows how enterprise controls are mapped to Audit Manager controls.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/control-mapping.png)


### Option 1: Map enterprise controls to common controls (recommended)
<a name="mapping-to-common-controls"></a>

This is the recommended way to map your enterprise controls to Audit Manager. This is because common controls closely align with common industry standards. This makes it easier to map them to your enterprise controls. 

With this approach, the vendor creates an interface that enables the customer to perform a one-time mapping between their enterprise controls and the corresponding common controls that Audit Manager provides. Vendors can use the [ListControls](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html), [ListCommonControls](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html), and [GetControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html) API operations to surface this information to customers. After the customer completes the mapping exercise, the vendor can then use these mappings to [create custom controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-controls.html) in Audit Manager. 

Here is an example of a common control mapping: 

Let’s say that you have an enterprise control named `Asset Management`. This enterprise control maps to two common controls in Audit Manager (`Asset performance management` and `Asset maintenance scheduling`). In this case, you must create a custom control in Audit Manager (we’ll name it `enterprise-asset-management`). Then, and add `Asset performance management` and `Asset maintenance scheduling` as evidence sources to the new custom control. These evidence sources collect supporting evidence from a predefined group of AWS data sources. This provides you with an efficient way to identify the AWS data sources that map to the requirements of your enterprise control.

#### Procedure
<a name="mapping-to-common-controls-procedure"></a>

**To find the available common controls that you can map to**  
Follow the steps to [find the list of available common controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html) in Audit Manager. 

**To create a custom control**

1. Follow the steps to [create a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-controls.html) that aligns with your enterprise control. 

   When you specify evidence sources in step 2 of the custom control creation workflow, do the following:
   + Choose **AWS managed sources **as the evidence source. 
   + Select **Use a common control that matches your compliance goal**.
   + Choose up to five common controls as evidence sources for your enterprise control.

1. Repeat this task for all of your enterprise controls, and create corresponding custom controls in Audit Manager for each one.

### Option 2: Map enterprise controls to standard controls
<a name="mapping-to-standard-controls"></a>

Audit Manager provides a large number of prebuilt standard controls. You can perform a one-time mapping between your enterprise controls and these standard controls. After you’ve identified the standard controls that correspond to your enterprise controls, you can add these standard controls directly to a custom framework. If you choose this option, you don’t need to create any custom controls in Audit Manager.

#### Procedure
<a name="mapping-to-common-controls-procedure"></a>

**To find the available standard controls that you can map to**  
Follow the steps to [find the list of available standard controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html) in Audit Manager. 

**To create a custom framework**

1. Follow the steps to [create a custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-custom-frameworks-from-scratch.html) in Audit Manager. 

   When you specify a control set in step 2 of the framework creation procedure, include the standard controls that map to your enterprise controls.

1. Repeat this task for all of your enterprise controls until you have included all of the corresponding standard controls in your custom framework.

## Step 4. Keep your control mappings updated
<a name="tutorial-for-grc-integration-step4"></a>

### Who completes this step
<a name="tutorial-for-grc-integration-step4-who"></a>

Vendor, customer

### What you need to do
<a name="tutorial-for-grc-integration-step4-what"></a>

Audit Manager continuously updates common controls and standard controls to ensure that they use the latest available AWS data sources. This means that mapping controls is a one-off task: you don’t need to manage standard controls after you add them to a custom framework, and you don’t need to manage common controls after you add them as an evidence source in your custom control. Whenever a common control is updated, the same updates are automatically applied to all custom controls that use that common control as an evidence source.

However, over time it’s possible that new common controls and standard controls will become available for you to use as evidence sources. With this in mind, vendors and customers should create a workflow to periodically fetch the latest common controls and standard controls from Audit Manager. You can then review the mappings between the enterprise controls and Audit Manager controls, and update the mappings as needed.

### If your enterprise controls are mapped to common controls
<a name="if-your-enterprise-controls-are-mapped-to-common-controls"></a>

During the mapping process, you created custom controls. You can use Audit Manager to edit those custom controls so that they use the latest available common controls as evidence sources. After the custom control updates take effect, your existing assessments will automatically collect evidence against the updated custom controls. There's no need to create a new framework or assessment.

#### Procedure
<a name="if-your-enterprise-controls-are-mapped-to-common-controls-procedure"></a>

**To find the latest common controls that you can map to**  
Follow the steps to [find the available common controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html) in Audit Manager. 

**To edit a custom control**

1. Follow the steps to [edit a custom control](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-controls.html) in Audit Manager. 

   When you update the evidence sources in step 2 of the editing workflow, do the following:
   + Choose **AWS managed sources **as the evidence source. 
   + Select **Use a common control that matches your compliance goal**.
   + Choose the new common control that you want to use as an evidence source for your custom control.

1. Repeat this task for all of your enterprise controls that you want to update.

### If your enterprise controls are mapped to standard controls
<a name="if-your-enterprise-controls-are-mapped-to-standard-controls"></a>

In this case, vendors must create a new custom framework that includes the latest available standard controls, and then create a new assessment using this new framework. After creating the new assessment, you can mark your old assessment as inactive.

#### Procedure
<a name="if-your-enterprise-controls-are-mapped-to-standard-controls-procedure"></a>

**To find the latest standard controls that you can map to**  
Follow the steps to [find the available standard controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/access-available-controls.html) in Audit Manager. 

**To create a custom framework and add the latest standard controls**  
Follow the steps to [create a custom framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-custom-frameworks-from-scratch.html) in Audit Manager. 

When you specify a control set in step 2 of the framework creation workflow, include the new standard controls.

**To create an assessment**  
Create an assessment in the GRC application. 

**To change the status of an assessment to inactive**  
Follow the steps to [change the status of an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-assessment-status-to-inactive.html) in Audit Manager. 

## Step 5: Create an assessment
<a name="tutorial-for-grc-integration-step5"></a>

**Who completes this step**  
GRC application, with input from the vendor 

**What you need to do**  
As a customer, you don’t need to create an assessment directly in Audit Manager. When you start an assessment for certain controls in the GRC application, the GRC application creates the corresponding resources for you in Audit Manager. Firstly, the GRC application uses the mappings that you created to identify the relevant Audit Manager controls. Next, it uses the control information to create a custom framework for you. Lastly, it uses the newly-created custom framework to create an assessment in Audit Manager.

Creating an assessment in Audit Manager also requires a [scope](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-assessments.html#specify-accounts). This scope takes a list of the AWS accounts where the customer wants to run the assessment and collect evidence. Customers must define this scope directly in the GRC application.

As a vendor, you need to store the `assessmentId` that’s mapped to the assessment that was started in the GRC application. This `assessmentId` is required to fetch evidence from Audit Manager.

**To find an assessment ID**

1. Use the [ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html) operation to view your assessments in Audit Manager. You can use the [status](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html#auditmanager-ListAssessments-request-status) parameter to view assessments that are active. 

   ```
   aws auditmanager list-assessments --status ACTIVE
   ```

1. In the response, identify the assessment that you want to store in the GRC application, and take note of the `assessmentId`.

## Step 6. Start collecting evidence
<a name="tutorial-for-grc-integration-step6"></a>

**Who completes this step**  
AWS Audit Manager, with input from the vendor

**What you need to do**  
After you create an assessment, it takes up to 24 hours to start collecting evidence. At this point, your enterprise controls are now actively collecting evidence for your Audit Manager assessment.

We recommend that you use the [evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder.html) feature to quickly query and find evidence in Audit Manager. If you use evidence finder as a delegated administrator, you can search for evidence across all member accounts in your organization. Using a combination of filters and groupings, you can progressively narrow the scope of your search query. For example, if you want a high-level view of your system health, perform a broad search and filter by assessment, date range, and resource compliance. If your goal is to remediate a specific resource, you can perform a narrow search to target evidence for a specific control or resource ID. After you define your filters, you can group and then preview the matching search results before creating an assessment report.

**To enable evidence finder**
+ Follow the instructions to [enable evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-settings-enable.html) from your Audit Manager settings.

After you enable evidence finder, you can decide on a cadence to fetch evidence from Audit Manager for your assessment. You can also fetch evidence for a specific control in an assessment, and store the evidence in the GRC application that’s mapped to the enterprise control. You can use the following Audit Manager API operations to fetch evidence:
+ [GetEvidence](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidence.html)
+ [GetEvidenceByEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceByEvidenceFolder.html)
+ [GetEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFolder.html)
+ [GetEvidenceFoldersByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFoldersByAssessment.html)
+ [GetEvidenceFoldersByAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFoldersByAssessmentControl.html)

## Pricing
<a name="tutorial-for-grc-integration-pricing"></a>

You won't incur any additional cost for this integration setup, whether you're a vendor or a customer. Customers are charged for the evidence that's collected in Audit Manager. For more information about pricing, see [AWS Audit Manager Pricing](https://aws.amazon.com/audit-manager/pricing/).

## Additional resources
<a name="tutorial-for-grc-integration-whatnow"></a>

You can learn more about the concepts that are introduced in this tutorial by reviewing the following resources:
+ [Assessments](https://docs.aws.amazon.com/audit-manager/latest/userguide/assessments.html) – Learn about the concepts and tasks for managing an assessment.
+ [Control library](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-library.html) – Learn about the concepts and tasks for managing a custom control. 
+ [Framework library](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-library.html) – Learn about the concepts and tasks for managing a custom framework.
+ [Evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder.html) - Learn how to export a CSV file or generate an assessment report from your query results. 
+ [Download center](https://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html) - Learn how to download assessment reports and CSV exports from Audit Manager.