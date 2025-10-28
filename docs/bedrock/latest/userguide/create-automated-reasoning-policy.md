# Create your Automated Reasoning policy

When you create an Automated Reasoning policy, [your input source document](#source-document-step "#source-document-step") is translated into a set of formal logic rules and a schema of variables and types.

Amazon Bedrock encrypts your Automated Reasoning policy using AWS Key Management Service (KMS). By default, Amazon Bedrock uses a service-owned key. You can optionally specify a customer managed KMS key for additional control over the encryption of your policy data.

**Example:** If your source document contains an HR policy stating "Full-time employees who have worked for at least 1 year are eligible for parental leave," Automated Reasoning would extract variables like `is_full_time` (boolean), `years_of_service` (integer), and `eligible_for_parental_leave` (boolean), along with a rule that connects them.

###### Note

**Tutorial video:** For a step-by-step walkthrough of creating an Automated Reasoning policy, watch the following tutorial:

[Tutorial Demo 1 - Policy creation in Automated Reasoning checks](https://youtu.be/8Y4kKv6F0JY "https://youtu.be/8Y4kKv6F0JY")

## Create your Automated Reasoning policy in the console

1. In the left navigation, choose **Automated Reasoning**, and then choose **Create policy**.
2. Enter a **Name** for the policy.
3. (Optional) Enter a **Description** for the policy.
4. For **Source**, you need to provide a document that describes the rules and policies of your knowledge domain. This document should contain the business rules, policies, or guidelines that you want Automated Reasoning to validate against. For example, you might upload an HR policy document that defines employee benefits eligibility, a compliance manual that outlines regulatory requirements, or a technical specification that describes system constraints. The document should be comprehensive and clearly written, as Automated Reasoning will extract formal logic rules from this content.

###### Note

**Best practice:** For complex policies, it's better to split the content into digestible chunks and progressively import new content into a policy to make it more complex. Start with a focused subset of your rules, create and test the policy thoroughly, then gradually add more content in subsequent iterations. This approach helps you identify and resolve issues early, ensures each addition works correctly with existing rules, and makes troubleshooting easier when problems arise.

Do the following:

    1. For **Ingest method**, do one of the following:


    	1. Select **Upload document**, then select **Choose file**. Upload a PDF document of the source content that will serve as the basis for your policy.
    	2. Select **Enter text**. Paste or enter your source content that will serve as the basis for your policy.
    2. (Recommended) For **Instructions**, specify additional information on how to process your source document. While optional, providing information on how the policy will be used and what parts of the document to focus on or ignore help the logic extraction process.


    ###### Note

    Instructions should explain what type of questions the policy will be validating, describe the structure of the input document, and give an example of the type of questions users will ask. For example: "This policy will validate HR questions about leave eligibility. The document has sections on different leave types. Users will ask questions like 'Am I eligible for parental leave if I've worked here for 9 months?'"

5. (Optional) For **Tags**, choose **Add new tag** to tag your policy. Tags can help you manage, filter, and search for your AWS resources.
6. (Optional) For **Encryption**, choose a KMS key to encrypt your policy. You can use the default service-owned key or select a customer managed key from your account.
7. Choose **Create policy**.

## Create your Automated Reasoning policy using the API

You can use the `CreateAutomatedReasoningPolicy` API operation to create an Automated Reasoning policy programmatically.

### Request parameters

The following parameters are required or optional when creating an Automated Reasoning policy:

`name` (required)

The name of the Automated Reasoning policy. The name must be unique within your AWS account and Region.

`description` (optional)

A description of the Automated Reasoning policy. Use this to provide context about the policy's purpose and the types of validations it performs.

`clientRequestToken` (optional)

A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.

`policyDefinition` (optional)

The policy definition that contains the formal logic rules, variables, and custom variable types used to validate foundation model responses in your application.

`tags` (optional)

A list of tags to associate with the Automated Reasoning policy. Tags help you organize and manage your policies.

`kmsKeyId` (optional)

The KMS key identifier for encrypting the Automated Reasoning policy. You can use the key ID, key ARN, alias name, or alias ARN. If you don't specify a KMS key, Amazon Bedrock uses a service-owned key to encrypt your policy.

### Response elements

The API returns the following information:

`policyArn`

The Amazon Resource Name (ARN) of the Automated Reasoning policy that you created.

`version`

The version of the Automated Reasoning policy. The initial version is `DRAFT`.

`name`

The name of the Automated Reasoning policy.

### Example

The following example shows how to create an Automated Reasoning policy using the
AWS CLI:

```
aws bedrock create-automated-reasoning-policy \
  --name "DeleteMe" \
  --description "A Test AR Policy" \
  --source-document file://policy-document.pdf \
  --kms-key-id arn:aws:kms:`us-east-1`:`111122223333`:key/`12345678-1234-1234-1234-123456789012`
```

Example response:

```
{
  "createdAt": "2025-07-21T14:43:52.692Z",
  "definitionHash": "f16ba1ceca36e1d21adce559481add6a4998b79ae203d933fd0206a28d5c2896513dd62f57b293cba282441269a72063b1d9da02fcf2b421e9bf8495ff8c87af",
  "description": "A Test AR Policy",
  "name": "DeleteMe",
  "policyArn": "arn:aws:bedrock:us-east-1:286352875722:automated-reasoning-policy/lnq5hhz70wgk",
  "updatedAt": "2025-07-21T14:43:52.692Z",
  "version": "DRAFT"
}
```

## KMS permissions for Automated Reasoning policies

If you specify a customer managed KMS key to encrypt your Automated Reasoning policy, you must configure permissions that allow Amazon Bedrock to use the key on your behalf.

### Key policy permissions

Add the following statement to your KMS key policy to allow Amazon Bedrock to use the key for Automated Reasoning policies:

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

Your IAM principal must have the following permissions to use a customer managed KMS key with Automated Reasoning policies:

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

### Encryption context

Amazon Bedrock uses encryption context to provide additional security for your Automated Reasoning policies. The encryption context is a set of key-value pairs that Amazon Bedrock uses as additional authenticated data when encrypting and decrypting your policy.

For Automated Reasoning policies, Amazon Bedrock uses the following encryption context:

- **Key:** `aws:bedrock:automated-reasoning-policy`
- **Value:** The ARN of your Automated Reasoning policy

## View Automated Reasoning policy details

After you create your policy, you can view its the translated logic and variables on the policy's **Definitions** page.

## Policy creation best practices

Good Automated Reasoning policies capture all the information necessary to validate content from your application. At a high level, the policy should return a validation result of VALID when you deem you LLM's answer to be valid and complete.

### Create variables that capture user intent and use implications (=>) to structure relationships

Use boolean variables to capture the conclusion a user is driving towards, such as "can I submit this form," or "is this payment compliant," and then use the variables to create rules that follow an if/then "implicative form." You can use the content description field while creating a policy to give examples of the type of questions users will ask or give direct guidance on what these variables should be.

**Example:**

```
✓ Good: (=> isPaymentCompliant (<= paymentAmount 10000))

✗ Poor: (<= paymentAmount 10000)
```

### Use booleans instead of enums for non-exclusive states

Represent characteristics that can co-exist as separate boolean variables rather than as mutually exclusive enum values. This prevents logical contradictions when multiple conditions can apply simultaneously. For example, a user can be both a veteran and a teacher. Two boolean variables allow both to be set true. Using enum values to set customerType to TEACHER and customerType to VETERAN causes a contradiction since a variable can only have a single value.

**Example:**

```
✓ Good: isTeacher, isVeteran

✗ Poor: customerType = {TEACHER, VETERAN, OTHER}
```

### Specify units and formats explicitly in variable descriptions

Clearly document the unit and format for all numerical values in their descriptions. This reduces variance when interpreting text with different formats and prevents unit conversion errors, leading to more predictable validation results.

**Examples:**

- "discountRate: Decimal representation of percentage (0.15 means 15%)"
- "refundTimeframeInDays: Number of days allowed for refund requests"
- "temperatureInCelsius: Integer value in degrees Celsius"

### Validate ranges for numerical values

Use rules to validate variable values to ensure they are valid. Setting these constraints for numerical variables can guard against non-sensical inputs and highlight them as "impossible" when they occur.

**Example:**

```
✓ Good: (> patientAge 0)

✓ Good: (and (> creditScore 300) (< creditScore 1100))
```

### Use intermediate variables to model different levels and create abstractions

Use meaningful intermediate variables to represent complex concepts and connect them explicitly to implementation details. Using conceptual variables instead of explicit expressions creates modularity and makes the logical flow from policy concepts to specific outcomes clear. This also allows validation on generic cases where the explicit inputs are not present, for example: "Do premium benefits include free upgrades?"

**Example:**

```
(=> (or (> membershipDurationYears 10)
        lifeTimeStatusGranted)
    hasLifetimeStatus)

(= qualifiesForPremiumBenefits
   (or isPlatinumMember hasLifetimeStatus))

(=> qualifiesForPremiumBenefits freeUpgrade)
```

### Use enums for categorization and subjective assessments

Define enumerated types for categorizing issues or representing subjective judgments rather than using numerical scales. Discrete categories allow clear definitions to be assigned for each severity. Numerical scales do not provide a consistent means of categorization. If it's possible for a variable not to have a value from the enum, include an `OTHER` or `NONE` among the possible values.

**Example:**

```
type "Severity" with values "CRITICAL", "MAJOR", "MINOR"
```

### Logic must be declarative and not procedural

Standard computer code executes in a given order but policies specify rules that do not execute in a given order. Design rules and variables to allow if/then/else logic within a single rule. This approach allows rules to remain decoupled and avoids rule conflicts while still clearly representing the logical structure of the policy.

**Example:**

```
✗ Poor: (=> conditionA (= outcome VALUE_1))
✗ Poor: (=> conditionB (= outcome VALUE_2))

✓ Good: (=> (and conditionA conditionB) (= outcome VALUE_1))  // A takes precedence when both apply
✓ Good: (=> (and (not conditionA) conditionB) (= outcome VALUE_2))
✓ Good: (=> (and (not conditionA) (not conditionB)) (= outcome DEFAULT_VALUE))
```

### Use clear and consistent naming conventions

Apply predictable patterns in variable naming to enhance readability and consistent interpretation.

**Examples:**

- Boolean variables: use "is" or "has" prefix
- Categorical variables: use substantive nouns
- Numerical variables: include units when appropriate
