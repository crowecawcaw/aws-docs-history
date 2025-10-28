# Setting up AWS Marketplace Vendor Insights

The following procedure describes the high-level steps for setting up AWS Marketplace Vendor Insights on your AWS Marketplace
software as a service (SaaS) listing.

###### To set up AWS Marketplace Vendor Insights on your SaaS listing

1. [Create a security profile](#create-security-profile "#create-security-profile").
2. (Optional) [Upload a certification](#upload-certification "#upload-certification").
3. [Upload a self-assessment](#upload-self-assessment "#upload-self-assessment").
4. (Optional) [Enable AWS Audit Manager automated
   assessments](#enable-audit-manager-assessments "#enable-audit-manager-assessments").

## Create a security profile

A security profile provide your buyers with detailed insight into the security posture of
your software product. A security profile uses associated data sources, including
self-assessments, certifications, and AWS Audit Manager automated assessments.

###### Note

You can create a limited number of security profiles. To create more security profiles,
request a quota increase. For more information, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the
_AWS General Reference_.

###### To create a security profile

1. Sign in using an IAM user or role with access to the AWS Marketplace seller account.
2. Choose **Products** and select **SaaS** to navigate
   to the **SaaS products** page.
3. Choose a **product**.
4. Choose the **Vendor Insights** tab, and then choose **Contact
   Support for adding security profile**.
5. Complete the form, and then choose **Submit**.

The AWS Marketplace Seller Operations team will create the security profile. When the security
profile is ready, they will send a notification email message to the recipients identified
on the form.

## Upload a certification

A certification is a data source that provides evidence of your product’s security posture
across multiple dimensions. AWS Marketplace Vendor Insights supports the following certifications:

- FedRAMP certification – Validates compliance with U.S. government cloud
  security standards
- GDPR compliance report – Demonstrates adherence to General Data Protection
  Regulation (GDPR) requirements, protecting personal data and individuals' rights to
  privacy
- HIPAA compliance report – Demonstrates adherence to Health Insurance
  Portability and Accountability Act (HIPAA) regulations, safeguarding protected health
  information
- ISO/IEC 27001 audit report – Confirms compliance with International
  Organization for Standardization (ISO)/International Electrotechnical Commission (IEC)
  27001, emphasizing information security standards
- PCI DSS audit report – Demonstrates compliance with security standards set by
  the PCI Security Standards Council
- SOC 2 Type 2 audit report – Confirms compliance with Service Organizational
  Control (SOC) data privacy and security controls

###### To upload a certification

1. On the **Vendor Insights** tab, navigate to the **Data
   sources** section.
2. Under **Certifications**, choose **Upload
   certification**.
3. Under **Certification details**, provide the requested information
   and upload the certification.
4. (Optional) Under **Tags**, add new tags.

###### Note

For information about tags, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in
the _Tagging AWS Resources User Guide_. 5. Choose **Upload certification**.

###### Note

The certification is automatically associated with the current security profile. You
can also associate certifications that you've already uploaded. On the product detail
page, choose **Associate certification** under
**Certifications**, select a certification from the list, and choose
**Associate certification**.

After you upload the certification, you can download it using the **Download
certification** button on the product detail page. You can also update the
certification details using the **Update certification** button.

The certification status changes to **ValidationPending** until the
certification details are validated. An alternate status appears during and after the data
source is processed:

    * **Available** – The data source was uploaded and system
     validations completed successfully.
    * **AccessDenied** – The data source's external source
     reference is no longer accessible for AWS Marketplace Vendor Insights to read.
    * **ResourceNotFound** – The data source's external source
     reference is no longer available for VendorInsights to read.
    * **ResourceNotSupported** – The data source was uploaded
     but the provided source isn't supported, yet. For details about the validation error,
     refer to the status message.
    * **ValidationPending** – The data source was uploaded but
     system validations are still running. There's no action item for you at this stage.
     The status is updated to Available, ResourceNotSupported, or ValidationFailed.
    * **ValidationFailed** – The data source was uploaded, but
     the system validation failed for one or more reasons. For details about the validation
     error, refer to the status message.

## Upload a self-assessment

A self-assessment is a type of data source that provides evidence of your product’s
security posture. AWS Marketplace Vendor Insights supports the following self-assessments:

- AWS Marketplace Vendor Insights self-assessment
- Consensus Assessment Initiative Questionnaire (CAIQ). For more information, see
  [What is CAIQ](https://cloudsecurityalliance.org/blog/2021/09/01/what-is-caiq "https://cloudsecurityalliance.org/blog/2021/09/01/what-is-caiq"), on the Cloud Security Alliance web site.

###### To upload a self-assessment

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. On the **Vendor Insights** tab, navigate to the **Data
   sources** section.
3. Under **Self-assessments**, choose **Upload
   self-assessment**.
4. Under **Self-assessment details**, complete the following
   information:
   1. **Name** – Enter a name for the self-assessment.
   2. **Type** – Choose an assessment type from the list.

   ###### Note

   If you chose **Vendor Insights Security Self-Assessment**, then
   choose **Download template** to download the self-assessment.
   Choose **Yes**, **No**, or
   **N/A** for each answer in the spreadsheet.

5. To upload the completed assessment, choose **Upload
   self-assessment**.
6. (Optional) Under **Tags**, add new tags.

###### Note

For information about tags, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in
the _Tagging AWS Resources User Guide_. 7. Choose **Upload self-assessment**.

###### Note

The self-assessment is automatically associated with the current security profile.
You can also associate self-assessments that you've already uploaded. On the product
detail page, choose **Associate self-assessment** under
**Self-assessments**, select a self-assessment from the list, and
choose **Associate self-assessment**.

After you upload a self-assessment, you can download it using the **Download
self-assessment** button on the product detail page. You can also update the
self-assessment details using the **Update self-assessment**
button.

The status is updated to one of the following:

    * **Available** – The data source was uploaded and system
     validations completed successfully.
    * **AccessDenied** – The data source's external source
     reference is no longer available for VendorInsights to read.
    * **ResourceNotFound** – The data source's external source
     reference is no longer available for VendorInsights to read.
    * **ResourceNotSupported** – The data source was uploaded
     but the provided source isn't supported, yet. For details about the validation error,
     refer to the status message.
    * **ValidationPending** – The data source was uploaded, but
     system validations are still running. There's no action item for you at this stage.
     The status is updated to Available, ResourceNotSupported, or ValidationFailed.
    * **ValidationFailed** – The data source was uploaded, but
     the system validation failed for one or more reasons. For details about the validation
     error, refer to the status message.

## Enable AWS Audit Manager automated

assessments

AWS Marketplace Vendor Insights uses multiple AWS services to automatically gather evidence for your security
profile.

You need the following AWS services and resources for automated assessments:

- **AWS Audit Manager** – To simplify AWS Marketplace Vendor Insights setup, we use
  AWS CloudFormation Stacks and StackSets, which take care of provisioning and configuring the necessary
  resources. The stack set creates an automated assessment containing controls that are
  automatically populated by AWS Config.

For more information about AWS Audit Manager, see the [AWS Audit Manager User Guide](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md").

- **AWS Config** – The stack set deploys an AWS Config
  conformance pack to set up the necessary AWS Config rules. These rules allow the Audit Manager automated
  assessment to gather live evidence for other AWS services deployed in that
  AWS account. For more information about AWS Config features, see the [AWS Config Developer
  Guide](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md").

###### Note

You might notice increased activity in your account during your initial month of
recording with AWS Config when compared to subsequent months. During the initial bootstrapping
process, AWS Config reviews all the resources in your account that you have selected for AWS Config
to record.

If you run ephemeral workloads, you might see increased activity from AWS Config as it
records configuration changes associated with creating and deleting these temporary
resources. An _ephemeral workload_ is a temporary use
of computing resources that are loaded and run when needed.

Examples of ephemeral
workloads include Amazon Elastic Compute Cloud (Amazon EC2) spot instances, Amazon EMR jobs, AWS Auto Scaling, and
AWS Lambda. To avoid the increased activity from running ephemeral workloads, you can run
these types of workloads in a separate account with AWS Config turned off. This approach
avoids increased configuration recording and rule evaluations.

- **Amazon S3** – The stack set creates the following two
  Amazon Simple Storage Service buckets:
  - **vendor-insights-stack-set-output-bucket-{account number}**
    – This bucket contains outputs from the stack set run. The AWS Marketplace Seller
    Operations team uses the outputs to complete your automated data source creation
    process.
  - **vendor-insights-assessment-reports-bucket-{account number}**
    – AWS Audit Manager publishes assessment reports to this Amazon S3 bucket. For more
    information about publishing assessment reports, see [Assessment
    reports](../../../audit-manager/latest/userguide/assessment-reports.md "../../../audit-manager/latest/userguide/assessment-reports.md") in the _AWS Audit Manager User
    Guide_.

  For more information about Amazon S3 features, see the [Amazon S3 User Guide](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md").

- **IAM** – The onboarding stack set provisions
  the following AWS Identity and Access Management (IAM) roles in your account:
  - When the `VendorInsightsPrerequisiteCFT.yml` template is
    deployed, it creates the administrator role
    `AWSVendorInsightsOnboardingStackSetsAdmin` and the run role
    `AWSVendorInsightsOnboardingStackSetsExecution`. The stack set uses the
    administrator role to deploy the required stacks into multiple AWS Regions
    simultaneously. The administrator role assumes the execution role to deploy the
    necessary parent and nested stacks as part of the AWS Marketplace Vendor Insights setup process. For more
    information about self-managed permissions, see [Grant
    self-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md") in the _AWS CloudFormation User
    Guide_.
  - The `AWSVendorInsightsRole` role provides AWS Marketplace Vendor Insights with access to read
    the assessments in AWS Audit Manager resources. AWS Marketplace Vendor Insights displays the evidence found on the
    assessments on your AWS Marketplace Vendor Insights profile.
  - The `AWSVendorInsightsOnboardingDelegationRole` provides AWS Marketplace Vendor Insights with
    access to list and read objects in the
    `vendor-insights-stack-set-output-bucket` bucket. This capability allows
    the AWS Marketplace Catalog Operations team to assist you with setting up an AWS Marketplace Vendor Insights
    profile.
  - The `AWSAuditManagerAdministratorAccess` role provides administrative
    access to enable or disable AWS Audit Manager, update settings, and manage assessments,
    controls, and frameworks. You or your team can assume this role to take actions for
    automated assessments in AWS Audit Manager.

To enable AWS Audit Manager automated assessments, you must deploy the onboarding stacks.

### Deploy the onboarding stacks

To simplify AWS Marketplace Vendor Insights setup, we use AWS CloudFormation Stacks and StackSets, which take care of
provisioning and configuring the necessary resources. If you have a multiple account or
multiple AWS Region SaaS solution, StackSets allow you to deploy the onboarding stacks
from a central management account.

For more information about CloudFormation StackSets, see [Working with AWS CloudFormation
StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md") in the _AWS CloudFormation User Guide_.

AWS Marketplace Vendor Insights setup requires that you use the following CloudFormation templates:

- `VendorInsightsPrerequisiteCFT` – Sets up the necessary
  administrator role and permissions to run CloudFormation StackSets in your account. Create
  this stack in your seller account.
- `VendorInsightsOnboardingCFT` – Sets up the required
  AWS services and configures the appropriate IAM permissions. These permissions allow
  AWS Marketplace Vendor Insights to gather data for the SaaS product running in your AWS accounts and display
  the data on your AWS Marketplace Vendor Insights profile. Create this stack in both your seller account and
  production accounts that are hosting your SaaS solution through StackSets.

#### Create the

VendorInsightsPrerequisiteCFT stack

By running the `VendorInsightsPrerequisiteCFT` CloudFormation stack, you set up
IAM permissions to start onboarding stack sets.

###### To create the VendorInsightsPrerequisiteCFT stack

1. Review and download the latest
   `VendorInsightsPrerequisiteCFT.yml` file from the [AWS Samples Repo for Vendor Insights templates folder](https://github.com/aws-samples/aws-marketplace-vendor-assessment-onboarding "https://github.com/aws-samples/aws-marketplace-vendor-assessment-onboarding") on the GitHub
   website.
2. Sign in to the AWS Management Console using your AWS Marketplace seller account, and then open the AWS CloudFormation
   console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. In the CloudFormation console navigation pane, choose **Stacks**, and
   then choose **Create stack** and **With new resources
   (standard)** from the dropdown. (If the navigation pane is not visible, in
   the upper left corner, select and expand the navigation pane.)
4. Under **Specify template**, choose **Upload a template
   file**. To upload the
   `VendorInsightsPrerequisiteCFT.yml` file that you downloaded, use
   **Choose file**. Then choose **Next**.
5. Enter a name for the stack, and then choose **Next**.
6. (Optional) Configure the stack options as you want.

Choose **Next**. 7. On the **Review** page, review your choices. To make changes,
choose **Edit** in the area in which you want to change. Before you
can create the stack, you must select the acknowledgement check boxes in the
**Capabilities** area.

Choose **Submit**. 8. After the stack is created, choose the **Resources** tab and make
note of the following roles that are created:

    * `AWSVendorInsightsOnboardingStackSetsAdmin`
    * `AWSVendorInsightsOnboardingStackSetsExecution`

#### Create the

VendorInsightsOnboardingCFT stack set

By running the `VendorInsightsOnboardingCFT` CloudFormation stack set, you set
up the required AWS services and configure the appropriate IAM permissions. This
allows AWS Marketplace Vendor Insights to gather data for the SaaS product running in your AWS account and
display it in your AWS Marketplace Vendor Insights profile.

If you have a multiple account solution or if you have separate seller and production
accounts, you must deploy this stack across multiple accounts. StackSets allow you to do
this from the management account that you created the prerequisites stack on.

The stack set is deployed using self-managed permissions. For more information, see
[Create a stack set with self-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#stacksets-getting-started-create-self-managed "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#stacksets-getting-started-create-self-managed") in the
_AWS CloudFormation User Guide_.

###### To create the VendorInsightsOnboardingCFT stack set

1. Review and download the latest
   `VendorInsightsOnboardingCFT.yml` file from the [AWS Samples Repo for Vendor Insights templates folder](https://github.com/aws-samples/aws-marketplace-vendor-assessment-onboarding "https://github.com/aws-samples/aws-marketplace-vendor-assessment-onboarding") on the GitHub
   website.
2. Sign in to the AWS Management Console using your AWS Marketplace seller account, and then open the AWS CloudFormation
   console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/")..
3. In the CloudFormation console navigation pane, choose **Create
   StackSet**. (If the navigation pane is not visible, in the upper left
   corner, select and expand the navigation pane.)
4. Under **Permissions**, for the administrator role choose
   **IAM role name**, and then choose
   **AWSVendorInsightsOnboardingStackSetsAdmin** for the role name
   from the dropdown.
5. Enter `AWSVendorInsightsOnboardingStackSetsExecution` as the
   **IAM execution role name**.
6. Under **Specify template**, choose **Upload a template
   file**. To upload the `VendorInsightsOnboardingCFT.yml`
   file that you downloaded, use **Choose file** and then choose
   **Next**.
7. Provide the following StackSet parameters, and then choose
   **Next**.
   - `CreateVendorInsightsAutomatedAssessment` – This parameter
     sets up the AWS Audit Manager automated assessment in your AWS account. If you have
     separate management and production accounts, this option should only be selected
     for production accounts and _not_ for the
     management account.
   - `CreateVendorInsightsIAMRoles` – This parameter provisions
     an IAM role that allows AWS Marketplace Vendor Insights to read the assessment data in your
     AWS account.
   - `PrimaryRegion` – This parameter sets the primary
     AWS Region for your SaaS deployment. This is the Region where the Amazon S3 bucket is
     created in your AWS account. If your SaaS product is deployed to only one
     Region, that Region is the primary Region.

8. Configure the StackSet options as you want. Keep the
   **Execution** configuration as **Inactive**, and
   then choose **Next**.
9. Configure the deployment options. If you have a multiple account solution, you can
   configure the stack set to deploy across multiple accounts and Regions as a single
   operation. Choose **Next**.

###### Note

If you have a multiple account solution, we do _not_ recommend deploying to all accounts as a single stack set. Pay
close attention to the parameters defined in step 7. You might want to enable or
disable some parameters, depending on the type of accounts that you're deploying to.
StackSets apply the same parameters to all specified accounts in a single
deployment. You can reduce deployment time by grouping accounts in a stack set, but
you still need to deploy multiple times for a multiple account solution.

###### Important

If you're deploying to multiple Regions, the first Region that you list must be
the `PrimaryRegion`. Leave the **Region Concurrency**
option as the default setting of **Sequential**. 10. On the **Review** page, review your choices. To make changes,
choose **Edit** in the area in which you want to change. Before you
can create the stack set, you must select the acknowledgement check box in the
**Capabilities** area.

Choose **Submit**.

The stack set takes about 5 minutes per Region to complete.
