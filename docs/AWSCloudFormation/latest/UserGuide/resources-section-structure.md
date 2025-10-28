# CloudFormation template Resources

syntax

The `Resources` section is a required top-level section in a CloudFormation
template. It declares the AWS resources that you want CloudFormation to provision and
configure as part of your stack.

## Syntax

The `Resources` section uses the following syntax:

### JSON

```
"Resources" : {
    "`LogicalResourceName1`" : {
        "Type" : "AWS::`ServiceName::ResourceType`",
        "Properties" : {
            `"PropertyName1" : "PropertyValue1"`,
            `...`
        }
    },

    "`LogicalResourceName2`" : {
        "Type" : "AWS::`ServiceName::ResourceType`",
        "Properties" : {
            `"PropertyName1" : "PropertyValue1"`,
            `...`
        }
    }
}
```

### YAML

```
Resources:
  `LogicalResourceName1`:
    Type: AWS::`ServiceName::ResourceType`
    Properties:
      `PropertyName1: PropertyValue1`
      `...`

  `LogicalResourceName2`:
    Type: AWS::`ServiceName::ResourceType`
    Properties:
      `PropertyName1: PropertyValue1`
      `...`
```

## Logical ID (also called \*logical

name\*)

Within a CloudFormation template, resources are identified by their logical resource
names. These names must be alphanumeric (A-Za-z0-9) and unique within the template.
Logical names are used to reference resources from other sections of the template.

## Resource type

Each resource must have a `Type` attribute, which defines the kind of AWS
resource it is. The `Type` attribute has the format
`AWS::`ServiceName`::`ResourceType``.
 For example, the `Type`attribute for an Amazon S3 bucket is
`AWS::S3::Bucket`.

For the full list of supported resource types, see the [AWS resource and property types reference](../TemplateReference/aws-template-resource-type-ref.md "../TemplateReference/aws-template-resource-type-ref.md").

## Resource properties

Resource properties are additional options that you can specify to define
configuration details for the specific resource type. Some properties are required,
while others are optional. Some properties have default values, so specifying those
properties is optional.

For details on the properties supported for each resource type, see the topics in
[AWS resource and property types reference](../TemplateReference/aws-template-resource-type-ref.md "../TemplateReference/aws-template-resource-type-ref.md").

Property values can be literal strings, lists of strings, Booleans, dynamic
references, parameter references, pseudo references, or the value returned by a
function. The following examples show you how to declare different property value
types:

### JSON

```
"Properties" : {
    "`String`" : "`A string value`",
    "`Number`" : `123`,
    "`LiteralList`" : [ "`first-value`", "`second-value`" ],
    "`Boolean`" : `true`
}
```

### YAML

```
Properties:
  `String`: `A string value`
  `Number`: `123`
  `LiteralList`:
    - `first-value`
    - `second-value`
  `Boolean`: `true`

```

## Physical ID

In addition to the logical ID, certain resources also have a physical ID, which is the
actual assigned name for that resource, such as an EC2 instance ID or an S3 bucket name.
Use the physical IDs to identify resources outside of CloudFormation templates, but only
after the resources have been created. For example, suppose you give an EC2 instance
resource a logical ID of `MyEC2Instance`. When CloudFormation creates the
instance, CloudFormation automatically generates and assigns a physical ID (such as
`i-1234567890abcdef0`) to the instance. You can use this physical ID to
identify the instance and view its properties (such as the DNS name) by using the Amazon
EC2 console.

For Amazon S3 buckets and many other resources, CloudFormation automatically generates a unique
physical name for the resource if you don't explicitly specify one. This physical name
is based on a combination of the name of the CloudFormation stack, the resource's logical
name specified in the CloudFormation template, and a unique ID. For example, if you have an
Amazon S3 bucket with the logical name `MyBucket` in a stack named
`MyStack`, CloudFormation might name the bucket with the following physical
name `MyStack-MyBucket-abcdefghijk1`.

For resources that support custom names, you can assign your own physical names to
help you quickly identify resources. For example, you can name an S3 bucket that stores
logs as `MyPerformanceLogs`. For more information, see [Name type](../TemplateReference/aws-properties-name.md "../TemplateReference/aws-properties-name.md").

## Referencing resources

Often, you need to set properties on one resource based on the name or property of
another resource. For example, you might create an EC2 instance that uses EC2 security
groups, or a CloudFront distribution backed by an S3 bucket. All of these resources can be
created in the same CloudFormation template.

CloudFormation provides intrinsic functions that you can use to refer to other resources
and their properties. These functions allow you to create dependencies between resources
and pass values from one resource to another.

### The `Ref` function

The `Ref` function is commonly used to retrieve an identifying property
of resources defined within the same CloudFormation template. What it returns depends on
the type of resource. For most resources, it returns the physical name of the
resource. However, for some resource types, it might return a different value, such
as an IP address for an `AWS::EC2::EIP` resource or an Amazon Resource
Name (ARN) for an Amazon SNS topic.

The following examples demonstrate how to use the `Ref` function in
properties. In each of these examples, the `Ref` function will return the
actual name of the `LogicalResourceName` resource declared elsewhere in
the template. The `!Ref` syntax example in the YAML example is just a
shorter way of writing the `Ref` function.

#### JSON

```
"Properties" : {
    "`PropertyName`" : { "Ref" : "`LogicalResourceName`" }
}
```

#### YAML

```
Properties:
  `PropertyName1`:
    Ref: `LogicalResourceName`
  `PropertyName2`: !Ref `LogicalResourceName`
```

For more detailed information about the `Ref` function, see [Ref](../TemplateReference/intrinsic-function-reference-ref.md "../TemplateReference/intrinsic-function-reference-ref.md").

### The `Fn::GetAtt`

function

The `Ref` function is helpful if the parameter or the value returned
for a resource is exactly what you want. However, you may need other attributes of a
resource. For example, if you want to create a CloudFront distribution with an S3 origin,
you need to specify the bucket location by using a DNS-style address. A number of
resources have additional attributes whose values you can use in your template. To
get these attributes, you use the `Fn::GetAtt` function.

The following examples demonstrate how to use the `GetAtt` function in
properties. The `Fn::GetAtt` function takes two parameters, the logical
name of the resource and the name of the attribute to be retrieved. The
`!GetAtt` syntax example in the YAML example is just a shorter way of
writing the `GetAtt` function.

#### JSON

```
"Properties" : {
    "`PropertyName`" : {
        "Fn::GetAtt" : [ "`LogicalResourceName`", "`AttributeName`" ]
    }
}
```

#### YAML

```
Properties:
  `PropertyName1`:
    Fn::GetAtt:
      - `LogicalResourceName`
      - `AttributeName`
  `PropertyName2`: !GetAtt `LogicalResourceName`.`AttributeName`
```

For more detailed information about the `GetAtt` function, see [Fn::GetAtt](../TemplateReference/intrinsic-function-reference-getatt.md "../TemplateReference/intrinsic-function-reference-getatt.md").

## Examples

The following examples illustrate how to declare resources and how CloudFormation
templates can reference other resources defined within the same template and existing
AWS resources.

###### Topics

- [Declaring a
  single resource with a custom name](#resources-section-structure-examples-single-resource "#resources-section-structure-examples-single-resource")
- [Referencing other
  resources with the Ref function](#resources-section-structure-examples-ref "#resources-section-structure-examples-ref")
- [Referencing resource
  attributes using the Fn::GetAtt function](#resources-section-structure-examples-getatt "#resources-section-structure-examples-getatt")

### Declaring a

single resource with a custom name

The following examples declare a single resource of type
`AWS::S3::Bucket` with the logical name `MyBucket`. The
`BucketName` property is set to `amzn-s3-demo-bucket`,
which should be replaced with the desired name for your S3 bucket.

If you use this resource declaration to create a stack, CloudFormation will create an
Amazon S3 bucket with default settings. For other resources, such as an Amazon EC2 instance or
Auto Scaling group, CloudFormation requires more information.

#### JSON

```
{
    "Resources": {
        "MyBucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": "`amzn-s3-demo-bucket`"
            }
        }
    }
}
```

#### YAML

```
Resources:
  MyBucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: `amzn-s3-demo-bucket`
```

### Referencing other

resources with the `Ref` function

The following examples show a resource declaration that defines an EC2 instance
and a security group. The `Ec2Instance` resource references the
`InstanceSecurityGroup` resource as part of its
`SecurityGroupIds` property using the `Ref` function. It
also includes an existing security group (`sg-12a4c434`) that's not
declared in the template. You use literal strings to refer to existing AWS
resources.

#### JSON

```
{
    "Resources": {
        "Ec2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "SecurityGroupIds": [
                    {
                        "Ref": "InstanceSecurityGroup"
                    },
                    "sg-12a4c434"
                ],
                "KeyName": "MyKey",
                "ImageId": "ami-1234567890abcdef0"
            }
        },
        "InstanceSecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Enable SSH access via port 22",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 22,
                        "ToPort": 22,
                        "CidrIp": "0.0.0.0/0"
                    }
                ]
            }
        }
    }
}
```

#### YAML

```
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
        - sg-12a4c434
      KeyName: MyKey
      ImageId: ami-1234567890abcdef0
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
```

### Referencing resource

attributes using the `Fn::GetAtt` function

The following examples show a resource declaration that defines a CloudFront
distribution resource and an S3 bucket. The `MyDistribution` resource
specifies the DNS name of the `MyBucket` resource using
`Fn::GetAtt` function to get the bucket's `DomainName`
attribute. You'll notice that the `Fn::GetAtt` function lists its two
parameters in an array. For functions that take multiple parameters, you use an
array to specify their parameters.

#### JSON

```
{
  "Resources": {
    "MyBucket": {
      "Type": "AWS::S3::Bucket"
    },
    "MyDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Origins": [
            {
              "DomainName": {
                "Fn::GetAtt": [
                  "MyBucket",
                  "DomainName"
                ]
              },
              "Id": "MyS3Origin",
              "S3OriginConfig": {}
            }
          ],
          "Enabled": "true",
          "DefaultCacheBehavior": {
            "TargetOriginId": "MyS3Origin",
            "ForwardedValues": {
              "QueryString": "false"
            },
            "ViewerProtocolPolicy": "allow-all"
          }
        }
      }
    }
  }
}
```

#### YAML

```
Resources:
  MyBucket:
    Type: 'AWS::S3::Bucket'
  MyDistribution:
    Type: 'AWS::CloudFront::Distribution'
    Properties:
      DistributionConfig:
        Origins:
          - DomainName: !GetAtt
              - MyBucket
              - DomainName
            Id: MyS3Origin
            S3OriginConfig: {}
        Enabled: 'true'
        DefaultCacheBehavior:
          TargetOriginId: MyS3Origin
          ForwardedValues:
            QueryString: 'false'
          ViewerProtocolPolicy: allow-all
```
