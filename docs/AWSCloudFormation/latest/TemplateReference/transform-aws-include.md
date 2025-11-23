This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `AWS::Include` transform

This topic describes how to use the `AWS::Include` transform to insert
boilerplate content into your CloudFormation templates.

The `AWS::Include` is a CloudFormation macro that, when referenced in your stack
template, inserts the contents of the specified file at the location of the transform in the
template when you create or update a stack using a change set. The `AWS::Include`
function behaves similarly to an `include`, `copy`, or `import`
directive in programming languages.

## Usage

You can use the `AWS::Include` transform anywhere within the CloudFormation
template except in the template parameters section or the template version. For example, you
can use `AWS::Include` in the mappings section.

### Syntax at the top level of a template

To declare this transform at the top level of your CloudFormation template, as the
`Transform` section, use the following syntax:

#### JSON

```
{
  "Transform":{
    "Name":"AWS::Include",
    "Parameters":{
      "Location":"s3://`amzn-s3-demo-bucket`/`MyFileName.json`"
    }
  },
  "Resources":{
    `...`
  }
}
```

#### YAML

```
Transform:
  Name: AWS::Include
  Parameters:
    Location: 's3://`amzn-s3-demo-bucket`/`MyFileName.yaml`'
Resources:
  `...`
```

### Syntax when the transform is embedded

within a section of a template

To declare this transform within a section of your CloudFormation template, use the
`Fn::Transform` intrinsic function and the following syntax:

#### JSON

```
{
  "Fn::Transform":{
    "Name":"AWS::Include",
    "Parameters":{
      "Location":"s3://`amzn-s3-demo-bucket`/`MyFileName.json`"
    }
  }
}
```

#### YAML

```
Fn::Transform:
  Name: AWS::Include
  Parameters:
    Location: s3://`amzn-s3-demo-bucket`/`MyFileName.yaml`
```

For more information, see [Fn::Transform](intrinsic-function-reference-transform.md "intrinsic-function-reference-transform.md").

### Parameters

`Location`

The location is an Amazon S3 URI, with a specific file name in an S3 bucket. For example,
`s3://`amzn-s3-demo-bucket`/`MyFile.yaml``.

## Considerations

When using `AWS::Include`, keep the following considerations in mind. For more
considerations about using macros, see [Macros
considerations](../UserGuide/template-macros-overview.md#template-macros-considerations "../UserGuide/template-macros-overview.md#template-macros-considerations") in the _AWS CloudFormation User Guide_.

- We currently support Amazon S3 URI, but no other Amazon S3 format (such as Amazon S3 ARN). It must be
  an Amazon S3 bucket, as opposed to something like a GitHub repository.
- Anyone with access to the Amazon S3 URL can include the snippet in their template.
- Your template snippets must be valid JSON.
- Your template snippets must be valid key-value objects, for example, `"KeyName":
"keyValue"`.
- You can't use `AWS::Include` to reference a template snippet that also uses
  `AWS::Include`.
- If your snippets change, your stack doesn't automatically pick up those changes. To
  get those changes, you must update the stack with the updated snippets. If you update your
  stack, make sure your included snippets haven't changed without your knowledge. To verify
  before updating the stack, check the change set.
- When creating templates and snippets, you can mix YAML and JSON template
  languages.
- We don't currently support using shorthand notations for YAML snippets.
- You can provide a cross-region replication Amazon S3 URI with `AWS::Include`.
  Make sure you check Amazon S3 bucket names when accessing cross-region replication objects. For
  more information, see [Replicating objects within and across
  Regions](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") in the _Amazon S3 User Guide_.

## Examples

The following examples show how to use the `AWS::Include` transform to execute
a wait condition handle. Replace `amzn-s3-demo-bucket` with your actual bucket name.

First, save a YAML file named `single_wait_condition.yaml` in your S3
bucket with the following contents:

```
`MyWaitCondition`:
  Type: AWS::CloudFormation::WaitCondition
  Properties:
    Handle: `!Ref MyWaitHandle`
    Timeout: `'4500'`
```

You can then reference this file using either JSON or YAML format.

### JSON

```
{
   "Resources": {
      "MyWaitHandle": {
         "Type": "AWS::CloudFormation::WaitConditionHandle"
      },
      "Fn::Transform": {
         "Name": "AWS::Include",
         "Parameters": {
            "Location": "s3://`amzn-s3-demo-bucket`/single_wait_condition.yaml"
         }
      }
   }
}
```

### YAML

```
Resources:
  MyWaitHandle:
    Type: AWS::CloudFormation::WaitConditionHandle
  Fn::Transform:
    Name: AWS::Include
    Parameters:
      Location: "s3://`amzn-s3-demo-bucket`/single_wait_condition.yaml"
```

For more information, see [Create wait conditions in a CloudFormation
template](../UserGuide/using-cfn-waitcondition.md "../UserGuide/using-cfn-waitcondition.md") in the _AWS CloudFormation User Guide_.
