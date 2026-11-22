

# Amazon Bedrock - Resource Tagging

Amazon Bedrock uses *application inference profiles* as the taggable resource for AWS Revenue Measurement. You must create an application inference profile, tag it with the `aws-apn-id-{{partner-central-aws-account-id}}` tag, and then use that profile for all model invocations. For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction).

We recommend Resource Tagging with application inference profiles. If you don't use application inference profiles, see [Attribution without application inference profiles](#bedrock-attribution-without-profiles).

All examples on this page use the account-suffixed tag key format. Replace `012345678901` with your Partner Central AWS account ID and `5ugbbrmu7ud3u5hsipfzug61p` with your product code. For how to construct your tag key, including backward compatibility with the legacy `aws-apn-id` key and how attribution appears in the dashboard, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction).

## Understanding inference profiles
<a name="bedrock-inference-profiles"></a>

An inference profile is an Amazon Bedrock resource that specifies a foundation model and its associated AWS Regions for model invocation. Inference profiles enable cost management and resource measurement through cost allocation tags.

Amazon Bedrock offers the following types of inference profiles:
+ **Cross-region (system-defined) inference profiles** – Predefined profiles that include multiple Regions to which requests for a model can be routed.
+ **Application inference profiles** – User-created profiles to measure costs and model usage. You can create a profile that routes requests to one Region or to multiple Regions.

**Warning**  
**System-defined inference profiles do not support tagging.** While system-defined (cross-region) inference profiles enhance flexibility in model usage by routing requests across multiple Regions, they do not support attaching custom tags for measuring, managing, and controlling costs across workloads and tenants. Only **application inference profiles** support the `aws-apn-id-{{partner-central-aws-account-id}}` tag required for AWS Revenue Measurement attribution. You must create an application inference profile to use Resource Tagging with Amazon Bedrock. If you can't use application inference profiles, see [Attribution without application inference profiles](#bedrock-attribution-without-profiles).

## Prerequisites
<a name="bedrock-prerequisites"></a>
+ Access to supported foundation models through the Amazon Bedrock console or API.
+ Your IAM role must have access to inference profile API actions. If your role has the `AmazonBedrockFullAccess` managed policy attached, you can skip this step. Otherwise, create a policy with the following permissions:

  ```json
  {
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "bedrock:InvokeModel*",
          "bedrock:CreateInferenceProfile"
        ],
        "Resource": [
          "arn:aws:bedrock:*::foundation-model/*",
          "arn:aws:bedrock:*:*:inference-profile/*",
          "arn:aws:bedrock:*:*:application-inference-profile/*"
        ]
      },
      {
        "Effect": "Allow",
        "Action": [
          "bedrock:GetInferenceProfile",
          "bedrock:ListInferenceProfiles",
          "bedrock:DeleteInferenceProfile",
          "bedrock:TagResource",
          "bedrock:UntagResource",
          "bedrock:ListTagsForResource"
        ],
        "Resource": [
          "arn:aws:bedrock:*:*:inference-profile/*",
          "arn:aws:bedrock:*:*:application-inference-profile/*"
        ]
      }
    ]
  }
  ```

## Tagging an application inference profile
<a name="bedrock-tagging-steps"></a>

Follow these steps to create and tag an application inference profile using the AWS CLI.

**Note**  
The tag value must use the format `pc:{{product-code}}`, where `{{product-code}}` is your AWS Marketplace product code. To retrieve your product code, see [Product Code Retrieval](product-code-retrieval.md). Do **NOT** use the Product ID or UUID formatted product ID.

1. **Create an application inference profile.**

   ```bash
   aws bedrock create-inference-profile \
     --inference-profile-name "my-partner-inference-profile" \
     --model-source "copyFrom=arn:aws:bedrock:us-east-1:{{123456789012}}:inference-profile/us.amazon.nova-pro-v1:0"
   ```

   Replace the Region, account ID, and inference profile ID with your values. The model source uses a `copyFrom` parameter that references a system-defined inference profile.

   The output returns the inference profile ARN and status:

   ```json
   {
     "inferenceProfileArn": "arn:aws:bedrock:us-east-1:{{123456789012}}:application-inference-profile/{{k1c3lwu20lem}}",
     "status": "ACTIVE"
   }
   ```

1. **Tag the inference profile with your partner identifier.**

   ```bash
   aws bedrock tag-resource \
     --resource-arn "arn:aws:bedrock:us-east-1:{{123456789012}}:application-inference-profile/{{k1c3lwu20lem}}" \
     --tags Key=aws-apn-id-012345678901,Value=pc:{{5ugbbrmu7ud3u5hsipfzug61p}}
   ```

   Use the ARN from the previous step. Replace `012345678901` with your Partner Central AWS account ID and `{{5ugbbrmu7ud3u5hsipfzug61p}}` with your AWS Marketplace product code. For details on the tag format, see [Resource Tagging](resource-tagging.md).

1. **Verify the tag.**

   ```bash
   aws bedrock list-tags-for-resource \
     --resource-arn "arn:aws:bedrock:us-east-1:{{123456789012}}:application-inference-profile/{{k1c3lwu20lem}}"
   ```

   The output confirms the tag:

   ```json
   {
     "tags": [
       {
         "key": "aws-apn-id-012345678901",
         "value": "pc:{{5ugbbrmu7ud3u5hsipfzug61p}}"
       }
     ]
   }
   ```

**Important**  
All subsequent model invocations must use the tagged application inference profile ARN to ensure proper AWS Revenue Measurement attribution.

## Listing application inference profiles
<a name="bedrock-listing-profiles"></a>

To list all application inference profiles in your account:

```bash
aws bedrock list-inference-profiles --type-equals "APPLICATION"
```

To get details for a specific profile:

```bash
aws bedrock get-inference-profile \
  --inference-profile-identifier "{{inference-profile-id}}"
```

## Attribution without application inference profiles
<a name="bedrock-attribution-without-profiles"></a>

If your Amazon Bedrock model invocations don't use a tagged application inference profile (for example, you invoke models through system-defined cross-Region inference profiles), use one of the following methods:
+ **[User Agent String](user-agent-string.md)** – Include your User Agent String in the AWS SDK or AWS CLI calls that invoke Amazon Bedrock models.
+ **[Identity Tagging](identity-tagging.md)** – If you meet the eligibility criteria, tag the IAM role or IAM user that invokes Amazon Bedrock models.
+ **[Account Tagging for SaaS products](account-tagging.md)** – If you meet the eligibility criteria and your AWS account is dedicated to a single SaaS product, tag the account.

## Considerations for Amazon Bedrock
<a name="bedrock-considerations"></a>
+ Attribution applies only to the Amazon Bedrock usage listed in the included services for each method.
+ To verify your implementation, confirm in AWS CloudTrail that Amazon Bedrock invocation calls use the tagged application inference profile ARN or include your User Agent String.