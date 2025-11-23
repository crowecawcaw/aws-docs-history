This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::GetAtt`

The `Fn::GetAtt` intrinsic function returns the value of an attribute from a
resource in the template.

## Declaration

### JSON

```
{ "Fn::GetAtt" : [ "`logicalNameOfResource`", "`attributeName`" ] }
```

### YAML

Syntax for the full function name:

```
Fn::GetAtt: [ `logicalNameOfResource`, `attributeName` ]
```

Syntax for the short form:

```
!GetAtt `logicalNameOfResource`.`attributeName`
```

## Parameters

`logicalNameOfResource`

The logical name (also called _logical ID_) of the resource that
contains the attribute that you want.

`attributeName`

The name of the resource-specific attribute whose value you want. See the resource's
reference page for details about the attributes available for that resource type.

## Return value

The attribute value. For information about `GetAtt` return values for
resources, see the documentation for the resources in the [Resource and property reference](aws-template-resource-type-ref.md "aws-template-resource-type-ref.md").

## Examples

### Return an attribute

value

The following examples return a string containing the DNS name of the load balancer with
the logical name `myELB`.

#### JSON

```
"Fn::GetAtt" : [ "myELB" , "DNSName" ]
```

#### YAML

```
!GetAtt myELB.DNSName
```

#### Return multiple attribute

values

The following examples return the `SourceSecurityGroup.OwnerAlias` and
`SourceSecurityGroup.GroupName` of the load balancer with the logical name
`myELB`.

##### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "myELB": {
            "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
            "Properties": {
                "AvailabilityZones": [
                    "eu-west-1a"
                ],
                "Listeners": [
                    {
                        "LoadBalancerPort": "80",
                        "InstancePort": "80",
                        "Protocol": "HTTP"
                    }
                ]
            }
        },
        "myELBIngressGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "ELB ingress group",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 80,
                        "ToPort": 80,
                        "SourceSecurityGroupOwnerId": {
                            "Fn::GetAtt": [
                                "myELB",
                                "SourceSecurityGroup.OwnerAlias"
                            ]
                        },
                        "SourceSecurityGroupName": {
                            "Fn::GetAtt": [
                                "myELB",
                                "SourceSecurityGroup.GroupName"
                            ]
                        }
                    }
                ]
            }
        }
    }
}

```

##### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myELB:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
        - eu-west-1a
      Listeners:
        - LoadBalancerPort: '80'
          InstancePort: '80'
          Protocol: HTTP
  myELBIngressGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: ELB ingress group
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          SourceSecurityGroupOwnerId: !GetAtt myELB.SourceSecurityGroup.OwnerAlias
          SourceSecurityGroupName: !GetAtt myELB.SourceSecurityGroup.GroupName

```

#### Use `Fn::Sub`

inside `Fn::GetAtt` function

###### Note

When you use the `AWS::LanguageExtensions` transform, you can use
`Fn::GetAtt` in combination with other intrinsic functions. For supported
functions, see [Supported functions](#getatt-supported-functions "#getatt-supported-functions").

The following examples show how to use `Fn::GetAtt` with [Fn::Sub](intrinsic-function-reference-sub.md "intrinsic-function-reference-sub.md"), in conjuction with [Fn::ForEach](intrinsic-function-reference-foreach.md "intrinsic-function-reference-foreach.md"), in the `Outputs` section of
a template to reduce the template length and verbosity. The use of `Fn::Sub`
within `Fn::GetAtt` allows the template to contain one intrinsic function that
can reference a different bucket at every iteration of the `Fn::ForEach` call.

##### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Transform": "AWS::LanguageExtensions",
    "Mappings": {
        "Buckets": {
            "Properties": {
                "Identifiers": ["A", "B", "C"]
            }
        }
    },
    "Resources": {
        "Fn::ForEach::Buckets": [
            "Identifier",
            {"Fn::FindInMap": ["Buckets", "Properties", "Identifiers"]},
            {
                "S3Bucket${Identifier}": {
                    "Type": "AWS::S3::Bucket",
                    "Properties": {
                        "AccessControl": "PublicRead",
                        "MetricsConfigurations": [
                            {
                                "Id": {"Fn::Sub": "EntireBucket${Identifier}"}
                            }
                        ],
                        "WebsiteConfiguration": {
                            "IndexDocument": "index.html",
                            "ErrorDocument": "error.html",
                            "RoutingRules": [
                                {
                                    "RoutingRuleCondition": {
                                        "HttpErrorCodeReturnedEquals": "404",
                                        "KeyPrefixEquals": "out1/"
                                    },
                                    "RedirectRule": {
                                        "HostName": "ec2-11-22-333-44.compute-1.amazonaws.com",
                                        "ReplaceKeyPrefixWith": "report-404/"
                                    }
                                }
                            ]
                        }
                    },
                    "DeletionPolicy": "Retain",
                    "UpdateReplacePolicy": "Retain"
                }
            }
        ]
    },
    "Outputs": {
        "Fn::ForEach::BucketOutputs": [
            "Identifier",
            {"Fn::FindInMap": ["Buckets", "Properties", "Identifiers"]},
            {
                "Fn::ForEach::GetAttLoop": [
                    "Property",
                    ["Arn", "DomainName", "WebsiteURL"],
                    {
                        "S3Bucket${Identifier}${Property}": {
                            "Value": {
                                "Fn::GetAtt": [{"Fn::Sub": "S3Bucket${Identifier}"}, {"Ref": "Property"}]
                            }
                        }
                    }
                ]
            }
        ]
    }
}
```

##### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Mappings:
  Buckets:
    Properties:
      Identifiers:
        - A
        - B
        - C
Resources:
  'Fn::ForEach::Buckets':
    - Identifier
    - Fn::FindInMap:
      - Buckets
      - Properties
      - Identifiers
    - 'S3Bucket${Identifier}':
        Type: 'AWS::S3::Bucket'
        Properties:
          AccessControl: PublicRead
          MetricsConfigurations:
            - Id:
                Fn::Sub: 'EntireBucket${Identifier}'
          WebsiteConfiguration:
            IndexDocument: index.html
            ErrorDocument: error.html
            RoutingRules:
              - RoutingRuleCondition:
                  HttpErrorCodeReturnedEquals: '404'
                  KeyPrefixEquals: out1/
                RedirectRule:
                  HostName: ec2-11-22-333-44.compute-1.amazonaws.com
                  ReplaceKeyPrefixWith: report-404/
        DeletionPolicy: Retain
        UpdateReplacePolicy: Retain
Outputs:
  'Fn::ForEach::BucketOutputs':
    - Identifier
    - Fn::FindInMap:
      - Buckets
      - Properties
      - Identifiers
    - 'Fn::ForEach::GetAttLoop':
        - Property
        - - Arn
          - DomainName
          - WebsiteURL
        - 'S3Bucket${Identifier}${Property}':
            Value: !GetAtt
              - !Sub 'S3Bucket${Identifier}'
              - !Ref Property
```

## Supported functions

When you use the [AWS::LanguageExtensions transform](transform-aws-languageextensions.md "transform-aws-languageextensions.md"), you can use the following
functions within the `Fn::GetAtt` function. This is true with either the
`Fn::GetAtt` logical resource name or the `Fn::GetAtt` attribute
name.

- [Fn::Base64](intrinsic-function-reference-base64.md "intrinsic-function-reference-base64.md")
- [Fn::FindInMap](intrinsic-function-reference-findinmap.md "intrinsic-function-reference-findinmap.md")
- [Fn::If](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if")
- [Fn::Join](intrinsic-function-reference-join.md "intrinsic-function-reference-join.md")
- [Fn::Sub](intrinsic-function-reference-sub.md "intrinsic-function-reference-sub.md")
- [Fn::ToJsonString](intrinsic-function-reference-ToJsonString.md "intrinsic-function-reference-ToJsonString.md")
- [Ref](intrinsic-function-reference-ref.md "intrinsic-function-reference-ref.md")

When the `AWS::LanguageExtensions` transform is not used:

- The `Fn::GetAtt` attribute name can only use the [Ref](intrinsic-function-reference-ref.md "intrinsic-function-reference-ref.md") function.
- The `Fn::GetAtt` logical resource name can't use functions. You must
  specify a string that's a resource's logical ID.
