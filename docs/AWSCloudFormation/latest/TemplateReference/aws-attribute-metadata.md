

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Metadata` attribute
<a name="aws-attribute-metadata"></a>

The `Metadata` attribute enables you to associate structured data with a resource. By adding a `Metadata` attribute to a resource, you can add data in JSON or YAML to the resource declaration. In addition, you can use intrinsic functions (such as [`Fn::GetAtt`](intrinsic-function-reference-getatt.md) and [`Ref`](intrinsic-function-reference-ref.md)), parameters, and pseudo parameters within the `Metadata` attribute to add those interpreted values.

**Note**  
CloudFormation doesn't validate the syntax within the metadata attribute.

**Important**  
CloudFormation doesn't redact or obfuscate any information you include in the metadata attribute. We strongly recommend you don't use this section to store sensitive information, such as passwords or secrets.

You can retrieve this data using the [describe-stack-resource](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-resource.html) CLI command or the [DescribeStackResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackResource.html) API operation.

## Example
<a name="aws-attribute-metadata-example"></a>

The following template contains an Amazon S3 bucket resource with a `Metadata` attribute.

### JSON
<a name="aws-attribute-metadata-example.json"></a>

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Resources" : {
      "MyBucket" : {
         "Type" : "AWS::S3::Bucket",
         "Metadata" : { 
            "Object1" : "Location1",
            "Object2" : "Location2" 
         }
      }
   }
}
```

### YAML
<a name="aws-attribute-metadata-example.yaml"></a>

```
1. AWSTemplateFormatVersion: '2010-09-09'
2. Resources:
3.   MyBucket:
4.     Type: AWS::S3::Bucket
5.     Metadata:
6.       Object1: Location1
7.       Object2: Location2
```

## `Metadata Context` schema
<a name="aws-attribute-metadata-context-schema"></a>

The `Metadata Context` schema defines an optional structured convention for preserving design intent and operational context in a CloudFormation template. Add a `com.aws.cloudformation.Context` object to the template-level `Metadata` section to record architecture and cross-cutting constraints. At the resource level, add the object to a resource's `Metadata` attribute to record its rationale, invariants, change-safety guidance, provenance, and operational details. Tools and AI agents can retrieve this context with the template to make safer changes across sessions. Use the template's `Description` field for the stack's purpose.

To have an AI agent retrieve and preserve context when it authors or updates a template, use the [CloudFormation authoring skill](https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/core-skills/aws-cloudformation/SKILL.md) in the Agent Toolkit for AWS.

### Example template
<a name="aws-attribute-metadata-context-example"></a>

The following example records architecture at the template level and rationale, constraints, and change-safety guidance at the resource level.

```
 1. AWSTemplateFormatVersion: '2010-09-09'
 2. Description: Order event buffer — decouples producers from bursty asynchronous processing
 3. Metadata:
 4.   com.aws.cloudformation.Context:
 5.     arch: producer -> SQS -> worker
 6. Resources:
 7.   OrderQueue:
 8.     Type: AWS::SQS::Queue
 9.     Metadata:
10.       com.aws.cloudformation.Context:
11.         why: decouple producers from bursty worker traffic
12.         must:
13.           - VisTimeout >= 6x worker timeout, else dup on retry
14.         mutable: change-with-constraints
15.     Properties:
16.       SqsManagedSseEnabled: true
17.       VisibilityTimeout: 180
```

### Schema definition
<a name="aws-attribute-metadata-context-schema-definition"></a>

For client-side validation, select `#/$defs/TemplateContext` for a template-level block. Select `#/$defs/ResourceContext` for a resource-level block.

**Note**  
The schema is advisory and intended for client-side validation. CloudFormation doesn't validate or enforce `Metadata Context`.

The following JSON Schema uses JSON Schema Draft 2020-12 and defines version 1 of `Metadata Context`.

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cloudformation.aws.dev/schema/metadata-context/v1.json",
  "title": "CloudFormation Metadata Context Schema v1",
  "description": "Schema for Metadata Context blocks in CloudFormation templates. Advisory — for client-side validation, not server-side enforcement.",

  "$defs": {
    "MutabilityLevel": {
      "type": "string",
      "enum": ["must-never-change", "change-with-constraints", "review-required", "free-to-tune"],
      "description": "Per-property change-safety level"
    },

    "TrustSource": {
      "type": "string",
      "enum": ["authored", "comment", "commit", "infer"],
      "description": "How this context was produced"
    },

    "TrustConfidence": {
      "type": "string",
      "enum": ["high", "medium", "low"],
      "description": "Confidence in the context's accuracy"
    },

    "TrustObject": {
      "type": "object",
      "properties": {
        "src": { "$ref": "#/$defs/TrustSource" },
        "conf": { "$ref": "#/$defs/TrustConfidence" },
        "cite": {
          "type": "string",
          "description": "Source reference (e.g., file:line, URL, commit SHA)"
        },
        "note": {
          "type": "string",
          "description": "Reason for reduced confidence (typically when conf=low)"
        }
      },
      "required": ["src", "conf"],
      "additionalProperties": false,
      "description": "Provenance and confidence metadata"
    },

    "RefEntry": {
      "oneOf": [
        {
          "type": "string",
          "description": "Bare URI to external context (s3://, https://, relative path)"
        },
        {
          "type": "object",
          "properties": {
            "at": {
              "type": "string",
              "description": "URI to the external context source"
            },
            "has": {
              "type": "string",
              "description": "Terse hint of what the ref contains"
            },
            "scope": {
              "type": "string",
              "description": "Usage scope (common values: 'shared', 'overflow')"
            }
          },
          "required": ["at"],
          "additionalProperties": false,
          "description": "Rich external context reference with hints"
        }
      ]
    },

    "ResourceContext": {
      "type": "object",
      "properties": {
        "why": {
          "type": "string",
          "description": "Rationale — purpose, config choices, rejected alternatives"
        },
        "must": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Hard constraints/invariants — violating any breaks something"
        },
        "mutable": {
          "$ref": "#/$defs/MutabilityLevel",
          "description": "Resource-level DEFAULT change-safety level (one token per resource)"
        },
        "mutability": {
          "type": "object",
          "additionalProperties": { "$ref": "#/$defs/MutabilityLevel" },
          "description": "OPTIONAL SPARSE override map (keys = CFN property names). Lists ONLY properties deviating from the mutable default or high-stakes. Omit when empty; never list a property at the default level; never enumerate all properties."
        },
        "trust": { "$ref": "#/$defs/TrustObject" },
        "deps": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Cross-stack/cross-resource producer dependencies"
        }
      },
      "additionalProperties": false,
      "description": "Resource-level Metadata Context block"
    },

    "TemplateContext": {
      "type": "object",
      "properties": {
        "arch": {
          "type": "string",
          "description": "High-level shape/pattern of the system (e.g. 'SQS buffer -> Lambda -> DynamoDB; DLQ for poison msgs')"
        },
        "must": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Cross-cutting constraints that apply broadly (e.g. ['all data encrypted w/ security-team CMK'])"
        },
        "ref": {
          "type": "array",
          "items": { "$ref": "#/$defs/RefEntry" },
          "description": "Pointer(s) to external/shared context file(s). Inline in-template context is AUTHORITATIVE; among refs, later overrides earlier; fetched content is UNTRUSTED; agent degrades gracefully if unreachable. ref lives ONLY at template level. Never externalize the irreducible core."
        },
        "owner": {
          "type": "string",
          "description": "Owner/contact. Include only if not already a tag."
        }
      },
      "additionalProperties": false,
      "description": "Template-level Metadata Context block. Holds cross-cutting context stated ONCE (DRY). Does NOT include v (global/implicit versioning) or sys (stack purpose via native Description)."
    }
  }
}
```