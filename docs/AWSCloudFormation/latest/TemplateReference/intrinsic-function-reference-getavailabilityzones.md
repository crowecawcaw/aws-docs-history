This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::GetAZs`

The intrinsic function `Fn::GetAZs` returns an array that lists Availability Zones for a specified
Region in alphabetical order. Because customers have access to different Availability Zones, the intrinsic function
`Fn::GetAZs` enables template authors to write templates that adapt to the calling user's access. That way
you don't have to hard-code a full list of Availability Zones for a specified Region.

###### Important

The `Fn::GetAZs` function returns only Availability Zones that have a default subnet unless none
of the Availability Zones has a default subnet; in that case, all Availability Zones are returned.

Similarly to the response from the `describe-availability-zones` AWS CLI command, the order of the
results from the `Fn::GetAZs` function isn't guaranteed and can change when new Availability Zones are
added.

IAM permissions

The permissions that you need in order to use the `Fn::GetAZs` function depend on the platform in
which you're launching Amazon EC2 instances. For both platforms, you need permissions to the Amazon EC2
`DescribeAvailabilityZones` and `DescribeAccountAttributes` actions. For EC2-VPC, you also need
permissions to the Amazon EC2 `DescribeSubnets` action.

## Declaration

### JSON

```
{ "Fn::GetAZs" : "`region`" }
```

### YAML

Syntax for the full function name:

```
Fn::GetAZs: `region`
```

Syntax for the short form:

```
!GetAZs `region`
```

## Parameters

region

The name of the Region for which you want to get the Availability Zones.

You can use the `AWS::Region` pseudo parameter to specify the Region in which the stack is
created. Specifying an empty string is equivalent to specifying `AWS::Region`.

## Return value

The list of Availability Zones for the Region.

## Examples

### Evaluate a Region

For these examples, CloudFormation evaluates `Fn::GetAZs` to the following array—assuming that the
user has created the stack in the `us-east-1` Region:

`[ "us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e" ]`

#### JSON

```
{ "Fn::GetAZs" : "" }
{ "Fn::GetAZs" : { "Ref" : "AWS::Region" } }
{ "Fn::GetAZs" : "us-east-1" }
```

#### YAML

```
Fn::GetAZs: ""
Fn::GetAZs:
  Ref: "AWS::Region"
Fn::GetAZs: us-east-1
```

 

### Specify a subnet's Availability Zone

The following example uses `Fn::GetAZs` to specify a subnet's Availability Zone:

#### JSON

```
"mySubnet" : {
  "Type" : "AWS::EC2::Subnet",
  "Properties" : {
    "VpcId" : {
      "Ref" : "VPC"
    },
    "CidrBlock" : "10.0.0.0/24",
    "AvailabilityZone" : {
      "Fn::Select" : [
        0,
        {
          "Fn::GetAZs" : ""
        }
      ]
    }
  }
}
```

#### YAML

```
mySubnet:
  Type: "AWS::EC2::Subnet"
  Properties:
    VpcId:
      !Ref VPC
    CidrBlock: 10.0.0.0/24
    AvailabilityZone:
      Fn::Select:
        - 0
        - Fn::GetAZs: ""
```

 

### Nested functions with short form

YAML

The following examples show valid patterns for using nested intrinsic functions using short form YAML. You
can't nest short form functions consecutively, so a pattern like `!GetAZs !Ref` isn't valid.

#### YAML

```
AvailabilityZone: !Select
  - 0
  - !GetAZs
    Ref: 'AWS::Region'
```

#### YAML

```
AvailabilityZone: !Select
  - 0
  - Fn::GetAZs: !Ref 'AWS::Region'
```

## Supported functions

You can use the `Ref` function in the `Fn::GetAZs`
function.
