# CloudFormation template Metadata

syntax

`Metadata` stores additional information using JSON or YAML objects. The types
of template-level metadata you can use in your template include:

Custom metadata

Stores user-defined key-value pairs. For example, you can provide additional
information that doesn't impact resource creation but offers additional context
about the infrastructure, team, or deployment specifics.

`AWS::CloudFormation::Interface`

Defines the grouping and ordering of input parameters when they're displayed
in the CloudFormation console. By default, the CloudFormation console alphabetically
sorts parameters by their logical ID.

`AWS::CloudFormation::Designer`

AWS CloudFormation Designer (Designer) reached end of life on
February 5, 2025.

###### Important

During a stack update, you cannot update the `Metadata` section by itself.
You can update it only when you include changes that add, modify, or delete
resources.

CloudFormation does not transform, modify, or redact any information you include in the
`Metadata` section. Because of this, we strongly recommend you do not use
this section to store sensitive information, such as passwords or secrets.

## Syntax

To declare custom metadata in your CloudFormation template, use the following
syntax:

### JSON

```
"Metadata" : {
  "`Instances`" : {"`Description`" : "`Information about the instances`"},
  "`Databases`" : {"`Description`" : "`Information about the databases`"}
}
```

### YAML

```
Metadata:
  `Instances`:
    `Description`: "`Information about the instances`"
  `Databases`:
    `Description`: "`Information about the databases`"
```

For the syntax for the `AWS::CloudFormation::Interface`, see [Organizing CloudFormation parameters with
AWS::CloudFormation::Interface metadata](aws-cloudformation-interface.md "aws-cloudformation-interface.md").
