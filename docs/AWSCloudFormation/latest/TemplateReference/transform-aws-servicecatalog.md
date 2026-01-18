This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `AWS::ServiceCatalog`

transform

This topic describes how to use the `AWS::ServiceCatalog` transform to
reference outputs from an existing AWS Service Catalog provisioned product in your CloudFormation
template.

## Usage

To use the `AWS::ServiceCatalog` transform, you must declare it at the top
level of your CloudFormation template. You can't use `AWS::ServiceCatalog` as a
transform embedded in any other template section.

Where an output value is required, you provide the name of the provisioned product and
the output key name.

You can reference multiple provisioned products and key names in your template, a
maximum of 20 per template. During provisioning, the transform retrieves the value from
each referenced provisioned product and key, substituting the output value in your
CloudFormation template.

The declaration must use the literal string `AWS::ServiceCatalog` as its
value. You can't use a parameter or function to specify a transform value.

### Syntax

To declare this transform in your CloudFormation template, use the following
syntax:

#### JSON

```
{
  "Transform":"AWS::ServiceCatalog",
  "Resources":{
    `...`
  }
}
```

#### YAML

```
Transform: AWS::ServiceCatalog
Resources:
  `...`
```

The `AWS::ServiceCatalog` transform is a standalone declaration with no
additional parameters.

## Examples

The following examples show how you can reference outputs from an existing Service
Catalog provisioned product in a CloudFormation template.

In these examples, `SampleProvisionedProduct` is a previously created
provisioned product. `SampleOutputKey` is an output key of this provisioned
product.

### JSON

This example is a working version.

Template versions that don't wrap the value as a string literal will fail.

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Transform":"AWS::ServiceCatalog",
  "Resources":{
    "ExampleParameter":{
      "Type":"AWS::SSM::Parameter",
      "Properties":{
        "Type":"String",
        "Value":"[[servicecatalog:provisionedproduct:SampleProvisionedProduct:SampleOutputKey]]"
      }
    }
  }
}
```

### YAML

Examples 1–4 are valid templates. In Examples 1 and 2, the transform and
value are string literals.

Example 5 isn't a valid template. The value must be wrapped in a string
`'` or `"` or `>-`. If not, the user receives
an error.

```
// Example 1
AWSTemplateFormatVersion: 2010-09-09
Transform: 'AWS::ServiceCatalog'
Resources:
  ExampleParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Type: String
      Value: '[[servicecatalog:provisionedproduct:SampleProvisionedProduct:SampleOutputKey]]'

// Example 2
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::ServiceCatalog
Resources:
  ExampleParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Type: String
      Value: '[[servicecatalog:provisionedproduct:SampleProvisionedProduct:SampleOutputKey]]'


// Example 3
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::ServiceCatalog
Resources:
  ExampleParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Type: String
      Value: "[[servicecatalog:provisionedproduct:SampleProvisionedProduct:SampleOutputKey]]"


// Example 4
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::ServiceCatalog
Resources:
  ExampleParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Type: String
      Value: >-
        [[servicecatalog:provisionedproduct:SampleProvisionedProduct:SampleOutputKey]]


// Example 5
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::ServiceCatalog
Resources:
  ExampleParameter2:
    Type: AWS::SSM::Parameter
    Properties:
      Type: String
      Value: [[servicecatalog:provisionedproduct:SSMProductProvisionedProduct:SampleOutputKey]]
```
