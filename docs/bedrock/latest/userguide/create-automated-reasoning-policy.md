# Create your Automated Reasoning policy

When you create an Automated Reasoning policy, your source document is translated into a
set of formal logic rules and a schema of variables and types. This page walks you through
preparing your document, creating the policy, and reviewing the results.

Amazon Bedrock encrypts your Automated Reasoning policy using AWS Key Management Service
(KMS). By default, Amazon Bedrock uses a service-owned key. You can optionally specify a
customer managed KMS key for additional control over the encryption of your policy data.

To test and use your Automated Reasoning policy, ensure you have [the appropriate permissions](guardrail-automated-reasoning-permissions.md "guardrail-automated-reasoning-permissions.md").

## Prepare your source document

Before you open the console or call the API, prepare the document that Automated
Reasoning will use to extract rules and variables. The quality of your policy depends
directly on the quality of this input.

### Document structure and clarity

Automated Reasoning checks work best with documents that contain clear, unambiguous rules.
Each rule should state a condition and an outcome. Avoid vague language, subjective
criteria, or rules that depend on external context not present in the document.

**Example: Clear vs. vague rules**

| Clear (good for extraction)                                                                             | Vague (poor for extraction)                                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| "Full-time employees with at least 12 months of continuous service are<br>eligible for parental leave." | "Eligible employees may apply for parental leave subject to manager<br>approval." |
| "Refund requests must be submitted within 30 days of purchase. Items must<br>be in original packaging." | "Refunds are handled on a case-by-case basis."                                    |

### Size limits and splitting large

documents

Source documents are limited to 5 MB in size and 50,000 characters. Images and tables
in documents also count toward the character limit.

If your document exceeds these limits, or if it covers multiple unrelated domains,
split it into focused sections. For example, split an employee handbook into separate
documents for leave policies, benefits eligibility, and expense reimbursement. Create
your policy with the first section, then use iterative policy building (described later
on this page) to merge additional sections into the same policy.

### Pre-process complex documents

Documents that contain a lot of boilerplate, legal disclaimers, or content unrelated
to the rules you want to enforce will produce noisy policies with unnecessary variables
and rules. Before uploading, consider:

- Removing headers, footers, table of contents, and appendices that don't contain
  rules.
- Extracting only the sections that contain the rules relevant to your use
  case.
- Simplifying complex tables into plain text statements where possible.

###### Tip

Start with a focused subset of your rules. Create and test the policy thoroughly,
then gradually add more content in subsequent iterations. This approach helps you
identify and resolve issues early and makes troubleshooting easier.

## Write effective instructions

When creating a policy, you can provide optional instructions that guide how Automated
Reasoning processes your source document. While optional, good instructions significantly
improve the quality of the extracted rules and variables.

Effective instructions should cover three things:

1. **Describe the use case.** Explain what your
   application does and what type of content the policy will validate. For example:
   "This policy will validate an HR chatbot that answers employee questions about leave
   of absence eligibility."
2. **Describe the types of questions users will ask.**
   Give examples of realistic user questions. For example: "Users will ask questions
   like 'Am I eligible for parental leave if I've worked here for 9 months?' or 'How
   many days of bereavement leave can I take?'"
3. **Focus the extraction.** If your document covers
   multiple topics, tell Automated Reasoning checks which parts to focus on and which to ignore.
   For example: "Focus on sections 3 through 5 which cover leave policies. Ignore the
   general company overview in section 1 and the organizational chart in section 2."

**Example instruction:**

```
This policy will validate HR questions about leave eligibility. The document
has sections on different leave types (parental, medical, bereavement, personal).
Users will ask questions like "Am I eligible for parental leave if I've worked
here for 9 months?" or "Can part-time employees take bereavement leave?"
Focus on the eligibility criteria for each leave type. Capture variables that
help determine whether an employee is eligible for a specific type of leave.
```

## Create a policy in the

console

1. In the left navigation, choose **Automated Reasoning**, and then
   choose **Create policy**.
2. Enter a **Name** for the policy.
3. (Optional) Enter a **Description** for the policy.
4. For **Source**, provide the document that describes the rules and
   policies of your knowledge domain. Do the following:
   1. For **Ingest method**, do one of the following:
      1. Select **Upload document**, then select
         **Choose file**. Upload a PDF document of the source
         content.
      2. Select **Enter text**. Paste or enter your source
         content.

   2. (Recommended) For **Instructions**, provide guidance on how
      to process your source document. See [Write effective instructions](#write-effective-instructions "#write-effective-instructions") for what to include.

5. (Optional) For **Tags**, choose **Add new tag**
   to tag your policy.
6. (Optional) For **Encryption**, choose a KMS key to encrypt your
   policy. You can use the default service-owned key or select a customer managed
   key.
7. Choose **Create policy**.

###### Tip

If your application expects a specific set of variables, you can pre-define the
schema before importing content. Use the `CreateAutomatedReasoningPolicy`
API or CloudFormation to create a policy with a `policyDefinition` that contains
your desired variables and types but no rules. Then use [Iterative policy building](#iterative-policy-building "#iterative-policy-building") to
import your source document. Automated Reasoning will use your predefined schema as a
starting point and add rules that reference your variables.

## Create a policy using the

API

An Automated Reasoning policy is a resource in your AWS account identified by an Amazon
Resource Name (ARN). Creating a policy through the API is a two-step process: first create
the policy resource, then start a build workflow to extract rules from your document.

### Step 1: Create the policy

resource

Use the `CreateAutomatedReasoningPolicy` API to create the policy
resource.

`name` (required)

The name of the policy. Must be unique within your AWS account and
Region.

`description` (optional)

A description of the policy's purpose.

`policyDefinition` (optional)

An initial policy definition with rules, variables, and custom types. Use
this if you already have a schema you want to start from.

`kmsKeyId` (optional)

The KMS key identifier for encrypting the policy. If not specified, Amazon
Bedrock uses a service-owned key.

`tags` (optional)

Tags to associate with the policy.

`clientRequestToken` (optional)

An idempotency token to ensure the operation completes no more than
once.

**Example:**

```
aws bedrock create-automated-reasoning-policy \
  --name "`MyHRPolicy`" \
  --description "`Validates HR chatbot responses about leave eligibility`" \
  --kms-key-id arn:aws:kms:`us-east-1`:`111122223333`:key/`12345678-1234-1234-1234-123456789012`
```

Example response:

```
{
  "createdAt": "2025-07-21T14:43:52.692Z",
  "definitionHash": "f16ba1ceca36e1d21adce559481add6a...",
  "name": "MyHRPolicy",
  "policyArn": "arn:aws:bedrock:us-east-1:111122223333:automated-reasoning-policy/lnq5hhz70wgk",
  "updatedAt": "2025-07-21T14:43:52.692Z",
  "version": "DRAFT"
}
```

### Step 2: Start a build

workflow to extract rules

Use the `StartAutomatedReasoningPolicyBuildWorkflow` API with the policy
ARN from step 1 to extract rules and variables from your source document.

`policyArn` (required)

The ARN of the policy resource created in step 1.

`buildWorkflowType` (required)

Set to `INGEST_CONTENT` to extract rules from a document.

`sourceContent` (required)

Contains the document to process and an optional starting policy
definition.

**Example:**

```
# Encode your PDF to base64
PDF_BASE64=$(base64 -i `your-policy.pdf` | tr -d '\n')

# Start the build workflow
aws bedrock start-automated-reasoning-policy-build-workflow \
  --policy-arn arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`lnq5hhz70wgk` \
  --build-workflow-type INGEST_CONTENT \
  --source-content "{
    \"policyDefinition\": {
      \"version\": \"1.0\",
      \"types\": [],
      \"rules\": [],
      \"variables\": []
    },
    \"workflowContent\": {
      \"documents\": [
        {
          \"document\": \"$PDF_BASE64\",
          \"documentContentType\": \"pdf\",
          \"documentName\": \"`HR Leave Policy`\",
          \"documentDescription\": \"`Validates HR chatbot responses about leave eligibility. Users ask questions like 'Am I eligible for parental leave?'`\"
        }
      ]
    }
  }"
```

Example response:

```
{
  "policyArn": "arn:aws:bedrock:us-east-1:111122223333:automated-reasoning-policy/lnq5hhz70wgk",
  "buildWorkflowId": "d40fa7fc-351e-47d8-a338-53e4b3b1c690"
}
```

Check the build status with
`ListAutomatedReasoningPolicyBuildWorkflows`:

```
aws bedrock list-automated-reasoning-policy-build-workflows \
  --policy-arn arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`lnq5hhz70wgk`
```

## Review the extracted policy

After a build completes, review the extracted policy definition before you start
testing. Catching issues at this stage saves time compared to discovering them through
failed tests later.

In the console, open your policy and go to the **Definitions** page.
Via the API, use `GetAutomatedReasoningPolicyBuildWorkflowResultAssets` with
`--asset-type POLICY_DEFINITION` to retrieve the extracted definition, and
`--asset-type QUALITY_REPORT` to retrieve the quality report.

Check for the following issues:

1. **Unused variables.** In the console, look for
   warning indicators next to variables. These flag variables that aren't referenced by
   any rules. Delete unused variables — they add noise to the translation process and
   can cause `TRANSLATION_AMBIGUOUS` results. In the API, unused variables
   are listed in the `QUALITY_REPORT` asset.
2. **Duplicate or near-duplicate variables.** Scan the
   variable list for variables with overlapping meanings, such as
   `tenureMonths` and `monthsOfService`. Duplicate variables
   confuse the translation process because Automated Reasoning checks can't determine which
   one to use for a given concept. Merge or delete duplicates.
3. **Bare assertions (rules not in if-then format).**
   Skim the rules and look for rules that aren't in if-then format, such as
   `(= eligibleForParentalLeave true)`. Bare assertions create axioms —
   statements that are always true — which make certain conditions logically impossible
   and lead to unexpected `IMPOSSIBLE` results during validation. Rewrite
   them as conditionals (for example,
   `(=> (and isFullTime (> tenureMonths 12)) eligibleForParentalLeave)`)
   or delete them. Bare assertions are appropriate only for boundary conditions like
   `(>= accountBalance 0)`.
4. **Conflicting rules.** The quality report flags
   rules that contradict each other. Conflicting rules cause your policy to return
   `IMPOSSIBLE` for all validation requests that involve the conflicting
   rules. Resolve conflicts by merging the rules or deleting one of them.
5. **Missing rules or variables.** Compare the
   extracted policy against your source document. If important rules or concepts are
   missing, you can add them manually or re-create the policy with better
   instructions.

###### Tip

The quality report also identifies disjoint rule sets — groups of rules that don't
share any variables. Disjoint rule sets aren't necessarily a problem (your policy may
cover independent topics), but they can indicate that variables are missing connections
between related rules.

## Iterative policy building

For complex domains, build your policy incrementally rather than trying to capture
everything in a single document upload. Start with a focused subset of your rules, create
and test the policy, then add more content in subsequent iterations.

### Add content in the console

1. Open your Automated Reasoning policy in the console.
2. On the **Definitions** page, choose
   **Import**.
3. Select the option to merge the new content with the existing policy
   definition.
4. Upload or paste the additional source content.
5. Review the updated policy definition and resolve any new conflicts or
   duplicates.

### Add content using the API

Call `StartAutomatedReasoningPolicyBuildWorkflow` with
`INGEST_CONTENT`, passing the complete current policy definition alongside
the new document. You must include the full existing definition — rules, variables, and
types — so that the new content is merged with the existing policy rather than replacing
it.

```
# First, retrieve the current policy definition
aws bedrock get-automated-reasoning-policy \
  --policy-arn arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`lnq5hhz70wgk`

# Encode the new document
PDF_BASE64=$(base64 -i `additional-rules.pdf` | tr -d '\n')

# Start a build workflow with the existing definition + new document
aws bedrock start-automated-reasoning-policy-build-workflow \
  --policy-arn arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`lnq5hhz70wgk` \
  --build-workflow-type INGEST_CONTENT \
  --source-content "{
    \"policyDefinition\": `EXISTING_POLICY_DEFINITION_JSON`,
    \"workflowContent\": {
      \"documents\": [
        {
          \"document\": \"$PDF_BASE64\",
          \"documentContentType\": \"pdf\",
          \"documentName\": \"`Additional Benefits Rules`\",
          \"documentDescription\": \"`Additional rules covering medical and bereavement leave eligibility.`\"
        }
      ]
    }
  }"
```

###### Important

The API supports a maximum of 2 build workflows per policy, with only 1 allowed
to be `IN_PROGRESS` at any time. If you need to start a new build and
already have 2 workflows, delete an old one first using
`DeleteAutomatedReasoningPolicyBuildWorkflow`.

## KMS permissions for Automated

Reasoning policies

If you specify a customer managed KMS key to encrypt your Automated Reasoning policy,
you must configure permissions that allow Amazon Bedrock to use the key on your
behalf.

### Key policy permissions

Add the following statement to your KMS key policy to allow Amazon Bedrock to use
the key for Automated Reasoning policies:

```
{
  "Sid": "PermissionsForAutomatedReasoningPolicy",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::`111122223333`:user/`role`"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey",
    "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:aws:bedrock:automated-reasoning-policy": [
        "arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`policy-id`",
        "arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`policy-id`:*"
      ],
      "kms:ViaService": "bedrock.`us-east-1`.amazonaws.com"
    }
  }
}
```

### IAM permissions

Your IAM principal must have the following permissions to use a customer managed KMS
key with Automated Reasoning policies:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowKMSForAutomatedReasoningPolicy",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:bedrock:automated-reasoning-policy": [
            "arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`policy-id`",
            "arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`policy-id`:*"
          ],
          "kms:ViaService": "bedrock.`us-east-1`.amazonaws.com"
        }
      }
    }
  ]
}
```

### Encryption

context

Amazon Bedrock uses encryption context to provide additional security for your
Automated Reasoning policies. The encryption context is a set of key-value pairs used
as additional authenticated data when encrypting and decrypting your policy.

For Automated Reasoning policies, Amazon Bedrock uses the following encryption
context:

- **Key:**
  `aws:bedrock:automated-reasoning-policy`
- **Value:** The Amazon Resource Name (ARN) of your
  Automated Reasoning policy
