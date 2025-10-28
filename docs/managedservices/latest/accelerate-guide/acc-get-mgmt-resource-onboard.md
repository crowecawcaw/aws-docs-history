# Step 2. Onboarding management resources in Accelerate

This is an overview of the process of onboarding management resources.

**You accept terms**

Your cloud services delivery manager (CSDM) guides you through the acceptance
process. You need to accept the Terms and Conditions, select AWS Regions, add-ons,
and a Service Level Agreement (SLA).

**You grant permissions to AMS roles**

You need to grant access to AMS
processes and to your Cloud Architect. You do this by creating a AWS CloudFormation stack for
each role. See
[The template to create AMS roles](acc-onb-roles.md "acc-onb-roles.md") and then
[Create aws_managedservices_onboarding_role with AWS CloudFormation for Accelerate](acc-onb-create-roles-with-cf.md "acc-onb-create-roles-with-cf.md").
For more details see
[Access management in AMS Accelerate](acc-access.md "acc-access.md").

**AMS reviews your configuration**

Your Cloud Architect (CA) also looks for possible configuration issues in your account, like Service Control Policies
(SCPs), and security findings that might prevent AMS from deploying the tools and resources required by AMS.
Your CA works with you to help you remediate findings and remove any
blockers to the deployment of AMS tools and resources.

**AMS reviews your AWS CloudTrail trail configurations**

Your Cloud Architect (CA) will review your CloudTrail trail configurations, and confirm if you want AMS to deploy a global CloudTrail trail, or integrate Accelerate
with your CloudTrail account or Organization trail resources. If you choose to have Accelerate integrate with your CloudTrail trail, your CA will guide you through required
updates to the configurations for your CloudTrail trail resources.

**AMS deploys management resources**

The AMS team deploys tools and AWS resources to provide the
different services of AMS Accelerate. After it's completed, AMS has built the
AWS Managed Services account and AMS notifies you that your account is active.

This concludes the _Onboarding management resources_ stage. You can proceed directly to the next step
of the onboarding process:
[Step 3. Onboarding AMS features with default policies](acc-get-feature-config.md "acc-get-feature-config.md").

###### Note

Now that your account is active, you have the option to perform any of these tasks:

- Create incidents and service requests for AWS infrastructure using the Support Center Console.
  See [Incident reports, service requests, and billing questions in AMS Accelerate](acc-supp-ex.md "acc-supp-ex.md").
- See the conformance status in your account of the AWS Config Rules deployed by AMS,
  [Configuration compliance in Accelerate](acc-sec-compliance.md "acc-sec-compliance.md").
- Locate and analyze GuardDuty and Macie (optional) findings. See
  [Monitor with GuardDuty](acc-sec-data-protect.md#acc-sec-data-protect-gd "acc-sec-data-protect.md#acc-sec-data-protect-gd").
- Access and audit CloudTrail logs
- Track changes in your AMS Accelerate account. See
  [Tracking changes in your AMS Accelerate accounts](acc-change-record.md "acc-change-record.md").
- Use Resource Tagger to create tags. See
  [Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md").
- Request Patch, Backup, and AWS Config Reports. See
  [Reports and options](ams-reporting.md "ams-reporting.md").
