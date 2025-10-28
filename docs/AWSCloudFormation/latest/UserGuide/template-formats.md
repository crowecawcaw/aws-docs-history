# CloudFormation template format

You can author CloudFormation templates in JSON or YAML formats. Both formats serve the same
purpose but offer distinct advantages in terms of readability and complexity.

- JSON – JSON is a lightweight data interchange
  format that's easy for machines to parse and generate. However, it can become cumbersome for
  humans to read and write, especially for complex configurations. In JSON, the template is
  structured using nested braces `{}` and brackets `[]` to define
  resources, parameters, and other components. Its syntax requires explicit declaration of
  every element, which can make the template verbose but ensures strict adherence to a
  structured format.
- YAML – YAML is designed to be more human-readable
  and less verbose than JSON. It uses indentation rather than braces and brackets to denote
  nesting, which can make it easier to visualize the hierarchy of resources and parameters.
  YAML is often preferred for its clarity and ease of use, especially when dealing with more
  complex templates. However, YAML's reliance on indentation can lead to errors if the spacing
  is not consistent, which requires careful attention to maintain accuracy.

## Template structure

CloudFormation templates are divided into different sections, and each section is designed to
hold a specific type of information. Some sections must be declared in a specific order, and
for others, the order doesn't matter. However, as you build your template, it can be helpful
to use the logical order shown in the following examples because values in one section might
refer to values from a previous section.

When authoring templates, don't use duplicate major sections, such as the
`Resources` section. Although CloudFormation might accept the template, it will have
an undefined behavior when processing the template, and might incorrectly provision resources,
or return inexplicable errors.

### JSON

The following example shows the structure of a JSON-formatted template with all
available sections.

```
{
  "AWSTemplateFormatVersion" : "`version date`",

  "Description" : "`JSON string`",

  "Metadata" : {
    `template metadata`
  },

  "Parameters" : {
    `set of parameters`
  },

  "Rules" : {
    `set of rules`
  },

  "Mappings" : {
    `set of mappings`
  },

  "Conditions" : {
    `set of conditions`
  },

  "Transform" : {
    `set of transforms`
  },

  "Resources" : {
    `set of resources`
  },

  "Outputs" : {
    `set of outputs`
  }
}
```

### YAML

The following example shows the structure of a YAML-formatted template with all
available sections.

```
---
AWSTemplateFormatVersion: `version date`

Description:
  `String`

Metadata:
  `template metadata`

Parameters:
  `set of parameters`

Rules:
  `set of rules`

Mappings:
  `set of mappings`

Conditions:
  `set of conditions`

Transform:
  `set of transforms`

Resources:
  `set of resources`

Outputs:
  `set of outputs`

```

## Comments

In JSON-formatted templates, comments are not supported. JSON, by design, doesn't include
a syntax for comments, which means you can't add comments directly within the JSON structure.
However, if you need to include explanatory notes or documentation, you can consider adding
metadata. For more information, see [Metadata
attribute](../TemplateReference/aws-attribute-metadata.md "../TemplateReference/aws-attribute-metadata.md").

In YAML-formatted templates, you can include inline comments by using the `#`
symbol.

The following example shows a YAML template with inline comments.

```
AWSTemplateFormatVersion: 2010-09-09
Description: A sample CloudFormation template with YAML comments.
# Resources section
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      # Linux AMI
      ImageId: ami-1234567890abcdef0
      InstanceType: t2.micro
      KeyName: MyKey
      BlockDeviceMappings:
        - DeviceName: /dev/sdm
          Ebs:
            VolumeType: io1
            Iops: 200
            DeleteOnTermination: false
            VolumeSize: 20
```

## Specifications

CloudFormation supports the following JSON and YAML specifications:

JSON

CloudFormation follows the ECMA-404 JSON standard. For more information about the JSON
format, see [http://www.json.org](http://www.json.org "http://www.json.org").

YAML

CloudFormation supports the YAML Version 1.1 specification with a few exceptions.
CloudFormation doesn't support the following features:

- The `binary`, `omap`, `pairs`,
  `set`, and `timestamp` tags
- Aliases
- Hash merges

For more information about YAML, see [https://yaml.org/](https://yaml.org/ "https://yaml.org/").

## Learn more

For each resource you specify in your template, you define its properties and values using
the specific syntax rules of either JSON or YAML. For more information about the template
syntax for each format, see [CloudFormation template sections](template-anatomy.md "template-anatomy.md").
