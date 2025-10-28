# General template snippets

The following examples show different CloudFormation template features that aren't specific to an
AWS service.

###### Topics

- [Base64 encoded UserData property](#scenario-userdata-base64 "#scenario-userdata-base64")
- [Base64 encoded UserData property with
  AccessKey and SecretKey](#scenario-userdata-base64-with-keys "#scenario-userdata-base64-with-keys")
- [Parameters section with one literal string
  parameter](#scenario-one-string-parameter "#scenario-one-string-parameter")
- [Parameters section with string
  parameter with regular expression constraint](#scenario-constraint-string-parameter "#scenario-constraint-string-parameter")
- [Parameters section with number parameter
  with MinValue and MaxValue constraints](#scenario-one-number-min-parameter "#scenario-one-number-min-parameter")
- [Parameters section with number parameter
  with AllowedValues constraint](#scenario-one-number-parameter "#scenario-one-number-parameter")
- [Parameters section with one literal
  CommaDelimitedList parameter](#scenario-one-list-parameter "#scenario-one-list-parameter")
- [Parameters section with parameter value
  based on pseudo parameter](#scenario-one-pseudo-parameter "#scenario-one-pseudo-parameter")
- [Mapping section with three
  mappings](#scenario-mapping-with-four-maps "#scenario-mapping-with-four-maps")
- [Description based on literal
  string](#scenario-description-from-literal-string "#scenario-description-from-literal-string")
- [Outputs section with one literal
  string output](#scenario-output-with-literal-string "#scenario-output-with-literal-string")
- [Outputs section with one resource
  reference and one pseudo reference output](#scenario-output-with-ref-and-pseudo-ref "#scenario-output-with-ref-and-pseudo-ref")
- [Outputs section with an output based on
  a function, a literal string, a reference, and a pseudo parameter](#scenario-output-with-complex-spec "#scenario-output-with-complex-spec")
- [Template format version](#scenario-format-version "#scenario-format-version")
- [AWSTags property](#scenario-format-aws-tag "#scenario-format-aws-tag")

## Base64 encoded UserData property

This example shows the assembly of a `UserData` property using the `Fn::Base64` and
`Fn::Join` functions. The references `MyValue` and
`MyName` are parameters that must be defined in the `Parameters`
section of the template. The literal string `Hello World` is just
another value this example passes in as part of the
`UserData`.

### JSON

```
"UserData" : {
    "Fn::Base64" : {
        "Fn::Join" : [ ",", [
            { "Ref" : "MyValue" },
            { "Ref" : "MyName" },
            "Hello World" ] ]
    }
}
```

### YAML

```
UserData:
  Fn::Base64: !Sub |
     Ref: MyValue
     Ref: MyName
     Hello World
```

## Base64 encoded UserData property with

AccessKey and SecretKey

This example shows the assembly of a `UserData` property using the `Fn::Base64` and
`Fn::Join` functions. It includes the `AccessKey` and `SecretKey`
information. The references `AccessKey` and
`SecretKey` are parameters that must be defined in the
Parameters section of the template.

### JSON

```
"UserData" : {
    "Fn::Base64" : {
        "Fn::Join" : [ "", [
            "ACCESS_KEY=", { "Ref" : "AccessKey" },
            "SECRET_KEY=", { "Ref" : "SecretKey" } ]
        ]
    }
}
```

### YAML

```
UserData:
  Fn::Base64: !Sub |
     ACCESS_KEY=${AccessKey}
     SECRET_KEY=${SecretKey}
```

## Parameters section with one literal string

parameter

The following example depicts a valid Parameters section declaration in which a single
`String` type parameter is declared.

### JSON

```
"Parameters" : {
    "UserName" : {
        "Type" : "String",
        "Default" : "nonadmin",
        "Description" : "Assume a vanilla user if no command-line spec provided"
    }
}
```

### YAML

```
Parameters:
  UserName:
    Type: String
    Default: nonadmin
    Description: Assume a vanilla user if no command-line spec provided
```

## Parameters section with string

parameter with regular expression constraint

The following example depicts a valid Parameters section declaration in which a single
`String` type parameter is declared. The `AdminUserAccount` parameter has a
default of `admin`. The parameter value must have a minimum length of 1, a maximum length
of 16, and contains alphabetical characters and numbers but must begin with an
alphabetical character.

### JSON

```
"Parameters" : {
    "AdminUserAccount": {
      "Default": "admin",
      "NoEcho": "true",
      "Description" : "The admin account user name",
      "Type": "String",
      "MinLength": "1",
      "MaxLength": "16",
      "AllowedPattern" : "[a-zA-Z][a-zA-Z0-9]*"
    }
}
```

### YAML

```
Parameters:
  AdminUserAccount:
    Default: admin
    NoEcho: true
    Description: The admin account user name
    Type: String
    MinLength: 1
    MaxLength: 16
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
```

## Parameters section with number parameter

with MinValue and MaxValue constraints

The following example depicts a valid Parameters section declaration in which a single
`Number` type parameter is declared. The `WebServerPort` parameter has a
default of 80 and a minimum value 1 and maximum value 65535.

### JSON

```
"Parameters" : {
    "WebServerPort": {
      "Default": "80",
      "Description" : "TCP/IP port for the web server",
      "Type": "Number",
      "MinValue": "1",
      "MaxValue": "65535"
    }
}
```

### YAML

```
Parameters:
  WebServerPort:
    Default: 80
    Description: TCP/IP port for the web server
    Type: Number
    MinValue: 1
    MaxValue: 65535
```

## Parameters section with number parameter

with AllowedValues constraint

The following example depicts a valid Parameters section declaration in which a single
`Number` type parameter is declared. The `WebServerPort` parameter has a
default of 80 and allows only values of 80 and 8888.

### JSON

```
"Parameters" : {
    "WebServerPortLimited": {
      "Default": "80",
      "Description" : "TCP/IP port for the web server",
      "Type": "Number",
      "AllowedValues" : ["80", "8888"]
    }
}
```

### YAML

```
Parameters:
  WebServerPortLimited:
    Default: 80
    Description: TCP/IP port for the web server
    Type: Number
    AllowedValues:
    - 80
    - 8888
```

## Parameters section with one literal

CommaDelimitedList parameter

The following example depicts a valid `Parameters` section declaration in which a single
`CommaDelimitedList` type parameter is declared. The `NoEcho` property is
set to `TRUE`, which will mask its value with asterisks (\*\*\*\*\*) in the
**describe-stacks** output, except for information stored in the locations specified below.

###### Important

Using the `NoEcho` attribute does not mask any information stored in the following:

- The `Metadata` template section. CloudFormation does not transform, modify, or redact any
  information you include in the `Metadata` section. For more information, see
  [Metadata](metadata-section-structure.md "metadata-section-structure.md").
- The `Outputs` template section. For more information, see
  [Outputs](outputs-section-structure.md "outputs-section-structure.md").
- The `Metadata` attribute of a resource definition. For more information, see
  [`Metadata` attribute](../TemplateReference/aws-attribute-metadata.md "../TemplateReference/aws-attribute-metadata.md").
  We strongly recommend you do not use these mechanisms to include sensitive information, such as
  passwords or secrets.

###### Important

Rather than embedding sensitive information directly in your CloudFormation templates, we recommend you use dynamic parameters in the stack template to
reference sensitive information that is stored and managed outside of CloudFormation, such as in the AWS Systems Manager Parameter Store or AWS Secrets Manager.

For more information, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best practice.

### JSON

```
"Parameters" : {
    "UserRoles" : {
        "Type" : "CommaDelimitedList",
        "Default" : "guest,newhire",
        "NoEcho" : "TRUE"
    }
}
```

### YAML

```
Parameters:
  UserRoles:
    Type: CommaDelimitedList
    Default: "guest,newhire"
    NoEcho: true
```

## Parameters section with parameter value

based on pseudo parameter

The following example shows commands in the EC2 user data that use the pseudo
parameters `AWS::StackName` and `AWS::Region`. For more
information about pseudo parameters, see [Get AWS values using pseudo parameters](pseudo-parameter-reference.md "pseudo-parameter-reference.md").

### JSON

```
          "UserData"       : { "Fn::Base64" : { "Fn::Join" : ["", [
             "#!/bin/bash -xe\n",
             "yum install -y aws-cfn-bootstrap\n",

             "/opt/aws/bin/cfn-init -v ",
             "         --stack ", { "Ref" : "AWS::StackName" },
             "         --resource LaunchConfig ",
             "         --region ", { "Ref" : "AWS::Region" }, "\n",

             "/opt/aws/bin/cfn-signal -e $? ",
             "         --stack ", { "Ref" : "AWS::StackName" },
             "         --resource WebServerGroup ",
             "         --region ", { "Ref" : "AWS::Region" }, "\n"
        ]]}}
      }
```

### YAML

```
UserData:
  Fn::Base64: !Sub |
     #!/bin/bash -xe
     yum update -y aws-cfn-bootstrap
     /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchConfig --region ${AWS::Region}
     /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
```

## Mapping section with three

mappings

The following example depicts a valid `Mapping` section declaration that contains three
mappings. The map, when matched with a mapping key of `Stop`,
`SlowDown`, or `Go`, provides the RGB
values assigned to the corresponding `RGBColor` attribute.

### JSON

```
"Mappings" : {
    "LightColor" : {
        "Stop" : {
            "Description" : "red",
            "RGBColor" : "RED 255 GREEN 0 BLUE 0"
        },
        "SlowDown" : {
            "Description" : "yellow",
            "RGBColor" : "RED 255 GREEN 255 BLUE 0"
        },
        "Go" : {
            "Description" : "green",
            "RGBColor" : "RED 0 GREEN 128 BLUE 0"
        }
    }
}
```

### YAML

```
Mappings:
  LightColor:
    Stop:
      Description: red
      RGBColor: "RED 255 GREEN 0 BLUE 0"
    SlowDown:
      Description: yellow
      RGBColor: "RED 255 GREEN 255 BLUE 0"
    Go:
      Description: green
      RGBColor: "RED 0 GREEN 128 BLUE 0"
```

## Description based on literal

string

The following example depicts a valid `Description` section declaration where the value
is based on a literal string. This snippet can be for templates, parameters, resources,
properties, or outputs.

### JSON

```
"Description" : "`Replace this value`"
```

### YAML

```
Description: "`Replace this value`"
```

## Outputs section with one literal

string output

This example shows a output assignment based on a literal string.

### JSON

```
"Outputs" : {
    "MyPhone" : {
        "Value" : "Please call 555-5555",
        "Description" : "A random message for aws cloudformation describe-stacks"
    }
}
```

### YAML

```
Outputs:
  MyPhone:
    Value: Please call 555-5555
    Description: A random message for aws cloudformation describe-stacks
```

## Outputs section with one resource

reference and one pseudo reference output

This example shows an `Outputs` section with two output assignments. One is based on a
resource, and the other is based on a pseudo reference.

### JSON

```

"Outputs" : {
   "SNSTopic" : { "Value" : { "Ref" : "MyNotificationTopic" } },
   "StackName" : { "Value" : { "Ref" : "AWS::StackName" } }
}
```

### YAML

```
Outputs:
  SNSTopic:
    Value: !Ref MyNotificationTopic
  StackName:
    Value: !Ref AWS::StackName
```

## Outputs section with an output based on

a function, a literal string, a reference, and a pseudo parameter

This example shows an Outputs section with one output assignment. The Join function is
used to concatenate the value, using a percent sign as the delimiter.

### JSON

```
"Outputs" : {
    "MyOutput" : {
        "Value" : { "Fn::Join" :
            [ "%", [ "A-string", {"Ref" : "AWS::StackName" } ] ]
        }
    }
}
```

### YAML

```
Outputs:
  MyOutput:
    Value: !Join [ %, [ 'A-string', !Ref 'AWS::StackName' ]]
```

## Template format version

The following snippet depicts a valid `AWSTemplateFormatVersion` section
declaration.

### JSON

```
"AWSTemplateFormatVersion" : "2010-09-09"
```

### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
```

## AWSTags property

This example shows an AWS `Tags` property. You would specify this property within the
Properties section of a resource. When the resource is created, it will be tagged with
the tags you declare.

### JSON

```
"Tags" : [
      {
        "Key" : "keyname1",
        "Value" : "value1"
      },
      {
        "Key" : "keyname2",
        "Value" : "value2"
      }
    ]
```

### YAML

```
Tags:
  -
    Key: "keyname1"
    Value: "value1"
  -
    Key: "keyname2"
    Value: "value2"
```
