# Using dependencies with CloudWatch Synthetics canaries

This section explains how to use `Dependencies` in CloudWatch Synthetics canaries. The `Dependencies` field allows you to specify dependencies for your canaries, enabling you to include additional libraries or custom code that your canary scripts can use.

## Overview

CloudWatch Synthetics canaries support specifying Lambda layers as dependencies. This feature allows you to:

- Share common code across multiple canaries
- Manage dependencies separately from your canary script code
- Reduce the size of your canary script by moving dependencies to a Lambda layer

## Supported APIs

The `Dependencies` field is supported in the following APIs:

- [CreateCanary](../../../AmazonSynthetics/latest/APIReference/API_CreateCanary.md "../../../AmazonSynthetics/latest/APIReference/API_CreateCanary.md")
- [UpdateCanary](../../../AmazonSynthetics/latest/APIReference/API_UpdateCanary.md "../../../AmazonSynthetics/latest/APIReference/API_UpdateCanary.md")
- [StartCanaryDryRun](../../../AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.md "../../../AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.md")

## Syntax

The `Dependencies` field is part of the code structure in the request syntax:

```

"Code": {
  "Handler": "string",
  "S3Bucket": "string",
  "S3Key": "string",
  "S3Version": "string",
  "ZipFile": blob,
  "Dependencies": [
    {
      "Type": "LambdaLayer",
      "Reference": "string"
    }
  ]
}

```

## Using dependencies

Here are some examples and instructions for using the `Dependencies` field in different scenarios.

### Creating a Canary with dependencies

When creating a canary, you can specify a Lambda layer as a dependency:

```

{
  "Name": "my-canary",
  "Code": {
    "Handler": "pageLoadBlueprint.handler",
    "S3Bucket": "my-bucket",
    "S3Key": "my-canary-script.zip",
    "Dependencies": [
      {
        "Type": "LambdaLayer",
        "Reference": "arn:aws:lambda:us-west-2:123456789012:layer:my-custom-layer:1"
      }
    ]
  },
  "ArtifactS3Location": "s3://my-bucket/artifacts/",
  "ExecutionRoleArn": "arn:aws:iam::123456789012:role/my-canary-role",
  "Schedule": {
    "Expression": "rate(5 minutes)"
  },
  "RuntimeVersion": "syn-nodejs-puppeteer-3.9"
}

```

### Updating a Canary's dependencies

You can update a canary's dependencies using the UpdateCanary API:

```

{
  "Name": "my-canary",
  "Code": {
    "Dependencies": [
      {
        "Type": "LambdaLayer",
        "Reference": "arn:aws:lambda:us-west-2:123456789012:layer:my-updated-layer:2"
      }
    ]
  }
}

```

### Removing dependencies

To remove dependencies from a canary, provide an empty array for the Dependencies field:

```

{
  "Name": "my-canary",
  "Code": {
    "Dependencies": []
  }
}

```

### Testing dependencies with StartCanaryDryRun

Before updating a canary with new dependencies, you can test them using the StartCanaryDryRun API:

```

{
  "Name": "my-canary",
  "Code": {
    "Dependencies": [
      {
        "Type": "LambdaLayer",
        "Reference": "arn:aws:lambda:us-west-2:123456789012:layer:my-test-layer:3"
      }
    ]
  }
}

```

## Limitations and considerations

- Only one Lambda layer can be specified as a dependency
- The role being used to create a canary with dependencies should have `lambda:GetLayerVersion` access to the dependency layer in addition to the [necessary roles and permissions](CloudWatch_Synthetics_Canaries_Roles.md "CloudWatch_Synthetics_Canaries_Roles.md")

## Creating compatible Lambda layers

For information on how to create and package layers, see [Managing Lambda dependencies with layers](../../../lambda/latest/dg/chapter-layers.md "../../../lambda/latest/dg/chapter-layers.md") and to understand the packaging structure of a canary check based on the canary packing structure, see [Writing a canary script](CloudWatch_Synthetics_Canaries_WritingCanary.md "CloudWatch_Synthetics_Canaries_WritingCanary.md").
