# `AWSSupport-TroubleshootSAMLIssues`

**Description**

The **AWSSupport-TroubleshootSAMLIssues** automation
runbook helps diagnose Security Assertion Markup Language (SAML) related issues by analyzing
SAML response files stored in Amazon Simple Storage Service (Amazon S3). It performs comprehensive validation
including schema verification, signature validation, audience restriction checking, and
expiration time verification. The runbook decodes and extracts key SAML elements including
issuer, assertions, subject, conditions, signatures, and attributes from the SAML response.
For environments where SAML is used to access AWS resources (such as Amazon Connect or Amazon WorkSpaces Applications)
through an IAM Identity Provider, it verifies whether the certificates in the SAML
response signatures match the certificates configured in the IAM Identity Provider.

**How does it work?**

The runbook performs the following steps:

- Validates SAML response format and required elements.
- Decodes and extracts SAML response components (issuer, assertions, subject,
  conditions, signatures, attributes).
- Verifies digital signatures against IAM Identity Provider certificates when
  provided.
- Checks audience restrictions and time validity.
- Provides detailed diagnostic information showing the parsed SAML structure and
  validation results.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSAMLIssues "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSAMLIssues")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `s3:GetBucketLocation`
- `s3:ListBucket`
- `s3:GetBucketPublicAccessBlock`
- `s3:GetAccountPublicAccessBlock`
- `s3:GetObject`
- `s3:GetBucketPolicyStatus`
- `s3:GetEncryptionConfiguration`
- `s3:GetBucketOwnershipControls`
- `s3:GetBucketAcl`
- `s3:GetBucketPolicy`
- `s3:PutObject`
- `iam:GetSAMLProvider`
- `sts:AssumeRole`
  Example Policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetAccountPublicAccessBlock",
 "s3:GetObject",
 "s3:GetBucketPolicyStatus",
 "s3:GetEncryptionConfiguration",
 "s3:GetBucketOwnershipControls",
 "s3:GetBucketAcl",
 "s3:GetBucketPolicy",
 "s3:PutObject",
 "iam:GetSAMLProvider",
 "sts:AssumeRole"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
 }`

```

**Instructions**

Follow these steps to configure the automation:

1. Before using this runbook, you need to capture and store a Base64-encoded SAML
   response (txt file) in an S3 bucket. Instructions for capturing SAML responses can
   be found in [this
   document](../../../IAM/latest/UserGuide/troubleshoot_saml_view-saml-response.md "../../../IAM/latest/UserGuide/troubleshoot_saml_view-saml-response.md")
2. Navigate to [`AWSSupport-TroubleshootSAMLIssues`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootSAMLIssues/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootSAMLIssues/description") in Systems Manager under
   Documents.
3. Select **Execute automation.**
4. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
       (IAM) role that allows SSM Automation to perform the actions on
       your behalf. If no role is specified, Systems Manager Automation uses the
       permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **InputFileS3URI (Required):**
     - Description: (Required) Amazon Simple Storage Service (Amazon S3) URI of SAML Response txt
       file (e.g., s3://bucket-name/path/to/file.txt).
     - Type: String
     - Allow Pattern:
       `^s3://[a-z0-9][a-z0-9.-][a-z0-9](/.)?$`

   - **S3OutputPrefix (Optional):**
     - Description: (Optional) The analysis output files are stored in
       the input bucket under the name 'saml_analysis\_<executionID of
       the runbook>.json'. You can use this parameter if you want to
       output a file with a specific prefix. The default value is
       "output/", in which case the file URI that output the result will be
       's3://bucket-name/output/saml_analysis\_<executionID of the
       runbook>.json'.
     - Type: String
     - Allow Pattern: `^[a-zA-Z0-9+=,.@\\-_/]*/$`

   - **ExpectedAudience (Optional):**
     - Description: (Optional) Expected audience value in the SAML
       response. If not specified, we use
       `urn:amazon:webservices`. If you have configured a
       specific audience value in your IdP and SP setup, please provide the
       exact format (e.g., `urn:amazon:webservices`,
       `https://signin.aws.amazon.com/saml`).
     - Type: String
     - Default: urn:amazon:webservices

   - **IamIdProviderArn (Optional):**
     - Description: (Optional) If you are using an IAM ID Provider
       entity to directly link your IdP with AWS IAM, please provide
       its ARN (e.g.,
       `arn:aws:iam::<account-id>:saml-provider/<provider-name>`).
     - Type: String
     - Allow Pattern:
       `^$|^arn:aws:iam::[0-9]{12}:saml-provider/[a-zA-Z0-9_-]+$`

   - **SAMLAuthenticationTime (Optional):**
     - Description: (Optional) The date and time when SAML authentication
       was performed. Timezone must be UTC. Must be in YYYY-MM-DDThh:mm:ss
       format (e.g., 2025-02-01T10:00:00). If this parameter is not
       provided, expiration checks will be performed against the current
       timestamp.
     - Type: String
     - Allow Pattern:
       `^$|^\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\d|3[01])T(?:[01]\\d|2[0-3]):[0-5]\\d:[0-5]\\d$`

   - **S3BucketOwnerRoleArn (Optional):**
     - Description: (Optional) IAM Role ARN to access the Amazon S3 buckets.
       The ARN of the IAM role with permissions to get the Amazon S3 bucket
       and account block public access settings, bucket encryption
       configuration, the bucket ACLs, the bucket policy status, and upload
       objects to the bucket. If this parameter is not specified, the
       runbook uses the `AutomationAssumeRole` (if specified) or user that
       starts this runbook (if `AutomationAssumeRole` is not
       specified).
     - Type: `AWS::IAM::Role::Arn`

5. Select **Execute**.
6. The automation initiates.
7. The document performs the following steps:
   - **ValidateIAMIDProvider**

   Validates the provided IAM ID Provider ARN by checking if it exists and
   is accessible. If no ARN is provided, the validation is skipped and the step
   completes successfully.
   - **CheckS3BucketPublicStatus**

   Checks if the Amazon S3 bucket allows anonymous, or public read or write access
   permissions. If the bucket allows these permissions, the automation stops at
   this step.
   - **CheckS3ObjectExistence**

   Validates access to the Amazon S3 buckets. Checks if the bucket and the object
   exist and if the automation has necessary permissions to read from source
   and write to destination.
   - **AnalyzeSAMLResponse**

   Analyzes the SAML response file by performing the checks (schema
   validation, signature verification, audience validation, expiration
   checking). Generates a detailed JSON report and saves it to the specified
   Amazon S3 location.

8. After completed, review the **Outputs** section for
   the detailed results of the execution:
   - **Outputs** section contains information
     about the Amazon S3 object where the analysis results are described.

9. The Amazon S3 object in the analysis results is a Json file containing the following
   information:
   - **validation_result**: contains basic
     validation results of the SAML response.
     - **saml_info**: key SAML information
       including issuer, signatures, and assertions.
     - **schema_validation**: results of
       SAML schema validation.

   - **verification_result**: provides more
     detailed diagnostic results.
     - **signature**: results of signature
       verification.
     - **audience**: results of audience
       restriction validation.
     - **expiration**: results of expiration
       time verification.

**References**

Systems Manager Automation

- [Run
  this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSAMLIssues "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootSAMLIssues")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
