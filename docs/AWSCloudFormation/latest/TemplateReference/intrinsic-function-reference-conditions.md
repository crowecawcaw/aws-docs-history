This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# Condition functions

You can use intrinsic functions, such as `Fn::If` or `Fn::Equals`, to
create and configure stack resources based on conditional logic. These conditions evaluate
during stack creation or updates. After you define all your conditions, you can associate them
with resources or resource properties in the `Resources` and `Outputs`
sections of a template.

For advanced scenarios, you can combine conditions using `Fn::And` or
`Fn::Or` functions, or use `Fn::Not` to negate a condition's value. You
can also nest conditions to create more complex conditional logic.

If you're new to using conditions in your templates, we recommend you first review the
[CloudFormation
template Conditions syntax](../UserGuide/conditions-section-structure.md "../UserGuide/conditions-section-structure.md") topic in the _AWS CloudFormation User Guide_.

###### Note

You must define all conditions in the `Conditions` section of a template,
except for `Fn::If` conditions. You can use the `Fn::If` condition in
the `Metadata` attribute, `UpdatePolicy` attribute, and property values
in the `Resources` and `Outputs` sections.

###### Topics

- [Fn::And](#intrinsic-function-reference-conditions-and "#intrinsic-function-reference-conditions-and")
- [Fn::Equals](#intrinsic-function-reference-conditions-equals "#intrinsic-function-reference-conditions-equals")
- [Fn::If](#intrinsic-function-reference-conditions-if "#intrinsic-function-reference-conditions-if")
- [Fn::Not](#intrinsic-function-reference-conditions-not "#intrinsic-function-reference-conditions-not")
- [Fn::Or](#intrinsic-function-reference-conditions-or "#intrinsic-function-reference-conditions-or")
- [Supported functions](#w2308aac24c20c25 "#w2308aac24c20c25")
- [Sample template](#conditions-sample-templates "#conditions-sample-templates")

## `Fn::And`

Returns `true` if all the specified conditions evaluate to true, or returns
`false` if any one of the conditions evaluates to false. `Fn::And`
acts as an AND operator. The minimum number of conditions that you can include is 2, and the
maximum is 10.

### Declaration

#### JSON

```
"Fn::And": [{`condition`}, {`...`}]
```

#### YAML

Syntax for the full function name:

```
Fn::And: [`condition`]
```

Syntax for the short form:

```
!And [`condition`]
```

### Parameters

condition

A condition that evaluates to `true` or `false`.

### `Fn::And` usage examples

The following `MyAndCondition` evaluates to true if the referenced security
group name is equal to `sg-mysggroup` and if `SomeOtherCondition`
evaluates to true:

#### JSON

```
"MyAndCondition": {
   "Fn::And": [
      {"Fn::Equals": ["sg-mysggroup", {"Ref": "ASecurityGroup"}]},
      {"Condition": "SomeOtherCondition"}
   ]
}
```

#### YAML

```
MyAndCondition: !And
  - !Equals ["sg-mysggroup", !Ref ASecurityGroup]
  - !Condition SomeOtherCondition
```

## `Fn::Equals`

Compares if two values are equal. Returns `true` if the two values are equal or
`false` if they aren't.

### Declaration

#### JSON

```
"Fn::Equals" : ["`value_1`", "`value_2`"]
```

#### YAML

Syntax for the full function name:

```
Fn::Equals: [`value_1`, `value_2`]
```

Syntax for the short form:

```
!Equals [`value_1`, `value_2`]
```

### Parameters

value

A string value that you want to compare.

### `Fn::Equals` usage examples

The following `IsProduction` condition evaluates to true if the value for the
`EnvironmentType` parameter is equal to `prod`:

#### JSON

```
"IsProduction" : {
   "Fn::Equals": [
      {"Ref": "EnvironmentType"},
      "prod"
   ]
}
```

#### YAML

```
IsProduction:
  !Equals [!Ref EnvironmentType, prod]
```

## `Fn::If`

Returns one value if the specified condition evaluates to `true` and another
value if the specified condition evaluates to `false`. Currently, CloudFormation
supports the `Fn::If` intrinsic function in the `Metadata` attribute,
`UpdatePolicy` attribute, and property values in the `Resources`
section and `Outputs` sections of a template. You can use the
`AWS::NoValue` pseudo parameter as a return value to remove the corresponding
property.

### Declaration

#### JSON

```
"Fn::If": [`condition_name`, `value_if_true`, `value_if_false`]
```

#### YAML

Syntax for the full function name:

```
Fn::If: [`condition_name`, `value_if_true`, `value_if_false`]
```

Syntax for the short form:

```
!If [`condition_name`, `value_if_true`, `value_if_false`]
```

### Parameters

condition_name

A reference to a condition in the Conditions section. Use the condition's name to
reference it.

value_if_true

A value to be returned if the specified condition evaluates to
true.

value_if_false

A value to be returned if the specified condition evaluates to
`false`.

### `Fn::If` usage examples

###### Topics

- [Conditionally choosing a resource](#w2308aac24c20c19b9b5 "#w2308aac24c20c19b9b5")
- [Conditional outputs](#w2308aac24c20c19b9b7 "#w2308aac24c20c19b9b7")
- [Conditional array values](#w2308aac24c20c19b9b9 "#w2308aac24c20c19b9b9")
- [Conditional properties and property values](#w2308aac24c20c19b9c11 "#w2308aac24c20c19b9c11")
- [Conditional update policies](#w2308aac24c20c19b9c13 "#w2308aac24c20c19b9c13")

#### Conditionally choosing a resource

The following example uses an `Fn::If` function in an Amazon EC2 resource
definition to determine which security group resource to associate with the instance. If
the `CreateNewSecurityGroup` condition evaluates to true, CloudFormation uses the
referenced value of `NewSecurityGroup` (a security group created elsewhere in
the template) to specify the `SecurityGroupIds` property. If
`CreateNewSecurityGroup` is false, CloudFormation uses the referenced value of
`ExistingSecurityGroupId` (a parameter that references an existing security
group).

##### JSON

```
"Resources": {
  "EC2Instance": {
    "Type": "AWS::EC2::Instance",
    "Properties": {
      "ImageId": "ami-0abcdef1234567890",
      "InstanceType": "t3.micro",
      "SecurityGroupIds": {
        "Fn::If": [
          "CreateNewSecurityGroup",
          [{"Ref": "NewSecurityGroup"}],
          [{"Ref": "ExistingSecurityGroupId"}]
        ]
      }]
    }
  }
}
```

##### YAML

```
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0abcdef1234567890
      InstanceType: t3.micro
      SecurityGroupIds: !If
        - CreateNewSecurityGroup
        - [!Ref NewSecurityGroup]
        - [!Ref ExistingSecurityGroupId]
```

#### Conditional outputs

In the `Output` section of a template, you can use the `Fn::If`
function to conditionally output information. In the following snippet, if the
`CreateNewSecurityGroup` condition evaluates to true, CloudFormation outputs the
security group ID of the `NewSecurityGroup` resource. If the condition is
false, CloudFormation outputs the security group ID of the `ExistingSecurityGroup`
resource.

##### JSON

```
"Outputs" : {
  "SecurityGroupId" : {
    "Description" : "Group ID of the security group used.",
    "Value" : {
      "Fn::If" : [
        "CreateNewSecurityGroup",
        {"Ref" : "NewSecurityGroup"},
        {"Ref" : "ExistingSecurityGroupId"}
      ]
    }
  }
}
```

##### YAML

```
Outputs:
  SecurityGroupId:
    Description: Group ID of the security group used.
    Value: !If [CreateNewSecurityGroup, !Ref NewSecurityGroup, !Ref ExistingSecurityGroupId]
```

#### Conditional array values

The following example uses `Fn::If` to conditionally provide different
array values based on a condition. If the `MoreThan2AZs` condition evaluates to
true, it uses three public subnets. Otherwise, it uses only two public subnets.

##### JSON

```
"Subnets": {
  "Fn::If": [
    "MoreThan2AZs",
    [
      {"Fn::ImportValue": "PublicSubnet01"},
      {"Fn::ImportValue": "PublicSubnet02"},
      {"Fn::ImportValue": "PublicSubnet03"}
    ],
    [
      {"Fn::ImportValue": "PublicSubnet01"},
      {"Fn::ImportValue": "PublicSubnet02"}
    ]
  ]
}
```

##### YAML

```
Subnets:
  Fn::If:
    - MoreThan2AZs
    - - Fn::ImportValue: PublicSubnet01
      - Fn::ImportValue: PublicSubnet02
      - Fn::ImportValue: PublicSubnet03
    - - Fn::ImportValue: PublicSubnet01
      - Fn::ImportValue: PublicSubnet02
```

#### Conditional properties and property values

The following example uses the `AWS::NoValue` pseudo parameter in an
`Fn::If` function. The condition uses a snapshot for an Amazon RDS DB instance
only if a snapshot ID is provided. If the `UseDBSnapshot` condition evaluates
to true, CloudFormation uses the `DBSnapshotName` parameter value for the
`DBSnapshotIdentifier` property. If the condition evaluates to false,
CloudFormation removes the `DBSnapshotIdentifier` property.

It also uses an `Fn::If` function in the `AllocatedStorage`
property of the Amazon RDS DB instance. If the `IsProduction` condition evaluates to
true, the storage size is set to `100`. Otherwise, it's set to
`20`.

##### JSON

```
"MyDatabase" : {
  "Type" : "AWS::RDS::DBInstance",
  "Properties": {
    "DBInstanceClass": "db.t3.micro",
    "AllocatedStorage": {
      "Fn::If": [
        "IsProduction",
        100,
        20
      ]
    },
    "Engine" : "MySQL",
    "EngineVersion" : "5.5",
    "MasterUsername" : { "Ref" : "DBUser" },
    "MasterUserPassword" : { "Ref" : "DBPassword" },
    "DBParameterGroupName" : { "Ref" : "MyRDSParamGroup" },
    "DBSnapshotIdentifier" : {
      "Fn::If" : [
        "UseDBSnapshot",
        {"Ref" : "DBSnapshotName"},
        {"Ref" : "AWS::NoValue"}
      ]
    }
  }
}
```

##### YAML

```
MyDatabase:
  Type: AWS::RDS::DBInstance
  Properties:
    DBInstanceClass: db.t3.micro
    AllocatedStorage: !If [IsProduction, 100, 20]
    Engine: MySQL
    EngineVersion: 5.5
    MasterUsername: !Ref DBUser
    MasterUserPassword: !Ref DBPassword
    DBParameterGroupName: !Ref MyRDSParamGroup
    DBSnapshotIdentifier: !If [UseDBSnapshot, !Ref DBSnapshotName, !Ref "AWS::NoValue"]
```

#### Conditional update policies

The following snippet provides an Auto Scaling update policy only if the
`RollingUpdates` condition evaluates to true. If the condition evaluates to
false, CloudFormation removes the `AutoScalingRollingUpdate` update policy.

##### JSON

```
"UpdatePolicy": {
  "Fn::If": [
    "RollingUpdates",
    {
      "AutoScalingRollingUpdate": {
        "MaxBatchSize": 2,
        "MinInstancesInService": 2,
        "PauseTime": "PT0M30S"
      }
    },
    {
      "Ref": "AWS::NoValue"
    }
  ]
}
```

##### YAML

```
UpdatePolicy: !If
  - RollingUpdates
  - AutoScalingRollingUpdate:
      MaxBatchSize: 2
      MinInstancesInService: 2
      PauseTime: PT0M30S
  - !Ref "AWS::NoValue"
```

## `Fn::Not`

Returns `true` for a condition that evaluates to `false` or returns
`false` for a condition that evaluates to `true`. `Fn::Not`
acts as a NOT operator.

### Declaration

#### JSON

```
"Fn::Not": [{`condition`}]
```

#### YAML

Syntax for the full function name:

```
Fn::Not: [`condition`]
```

Syntax for the short form:

```
!Not [`condition`]
```

### Parameters

condition

A condition such as `Fn::Equals` that evaluates to `true` or
`false`.

### `Fn::Not` usage examples

The following `EnvCondition` condition evaluates to true if the value for the
`EnvironmentType` parameter isn't equal to `prod`:

#### JSON

```
"MyNotCondition" : {
   "Fn::Not" : [{
      "Fn::Equals" : [
         {"Ref" : "EnvironmentType"},
         "prod"
      ]
   }]
}
```

#### YAML

```
MyNotCondition:
  !Not [!Equals [!Ref EnvironmentType, prod]]
```

## `Fn::Or`

Returns `true` if any one of the specified conditions evaluate to true, or
returns `false` if all the conditions evaluates to false. `Fn::Or` acts
as an OR operator. The minimum number of conditions that you can include is 2, and the maximum
is 10.

### Declaration

#### JSON

```
"Fn::Or": [{`condition`}, {`...`}]
```

#### YAML

Syntax for the full function name:

```
Fn::Or: [`condition, ...`]
```

Syntax for the short form:

```
!Or [`condition, ...`]
```

### Parameters

condition

A condition that evaluates to `true` or `false`.

### `Fn::Or` usage examples

The following `MyOrCondition` evaluates to true if the referenced security
group name is equal to `sg-mysggroup` or if `SomeOtherCondition`
evaluates to true:

#### JSON

```
"MyOrCondition" : {
   "Fn::Or" : [
      {"Fn::Equals" : ["sg-mysggroup", {"Ref" : "ASecurityGroup"}]},
      {"Condition" : "SomeOtherCondition"}
   ]
}
```

#### YAML

```
MyOrCondition:
  !Or [!Equals [sg-mysggroup, !Ref ASecurityGroup], Condition: SomeOtherCondition]
```

## Supported functions

You can use the following functions in the `Fn::If` condition:

- `Fn::Base64`
- `Fn::FindInMap`
- `Fn::GetAtt`
- `Fn::GetAZs`
- `Fn::If`
- `Fn::Join`
- `Fn::Select`
- `Fn::Sub`
- `Ref`

You can use the following functions in all other condition functions, such as
`Fn::Equals` and `Fn::Or`:

- `Fn::FindInMap`
- `Ref`
- Other condition functions

## Sample template

### Conditionally create resources for a production, development, or test stack

In some cases, you might want to create stacks that are similar but with minor tweaks.
For example, you might have a template that you use for production applications. You want to
create the same production stack so that you can use it for development or testing. However,
for development and testing, you might not require all the extra capacity that's included in
a production-level stack. Instead, you can use an environment type input parameter to
conditionally create stack resources that are specific to production, development, or
testing, as shown in the following sample:

You can specify `prod`, `dev`, or `test` for the
`EnvType` parameter. For each environment type, the template specifies a
different instance type. The instance types can range from a large, compute-optimized
instance type to a small general purpose instance type. In order to conditionally specify
the instance type, the template defines two conditions in the `Conditions`
section of the template: `CreateProdResources`, which evaluates to true if the
`EnvType` parameter value is equal to `prod` and
`CreateDevResources`, which evaluates to true if the parameter value is equal
to `dev`.

In the `InstanceType` property, the template nests two `Fn::If`
intrinsic functions to determine which instance type to use. If the
`CreateProdResources` condition is true, the instance type is
`c5.xlarge`. If the condition is false, the `CreateDevResources`
condition is evaluated. If the `CreateDevResources` condition is true, the
instance type is `t3.medium` or else the instance type is
`t3.small`.

In addition to the instance type, the production environment creates and attaches an
Amazon EC2 volume to the instance. The `MountPoint` and `NewVolume`
resources are associated with the `CreateProdResources` condition so that the
resources are created only if the condition evaluates to true.

###### Example JSON

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Parameters" : {
    "EnvType" : {
      "Description" : "Environment type.",
      "Default" : "test",
      "Type" : "String",
      "AllowedValues" : ["prod", "dev", "test"],
      "ConstraintDescription" : "must specify prod, dev, or test."
    }
  },
  "Conditions" : {
    "CreateProdResources" : {"Fn::Equals" : [{"Ref" : "EnvType"}, "prod"]},
    "CreateDevResources" : {"Fn::Equals" : [{"Ref" : "EnvType"}, "dev"]}
  },
  "Resources" : {
    "EC2Instance" : {
      "Type" : "AWS::EC2::Instance",
      "Properties" : {
        "ImageId" : "ami-1234567890abcdef0",
        "InstanceType" : { "Fn::If" : [
          "CreateProdResources",
          "c5.xlarge",
          {"Fn::If" : [
            "CreateDevResources",
            "t3.medium",
            "t3.small"
          ]}
        ]}
      }
    },
    "MountPoint" : {
      "Type" : "AWS::EC2::VolumeAttachment",
      "Condition" : "CreateProdResources",
      "Properties" : {
        "InstanceId" : { "Ref" : "EC2Instance" },
        "VolumeId"  : { "Ref" : "NewVolume" },
        "Device" : "/dev/sdh"
      }
    },
    "NewVolume" : {
      "Type" : "AWS::EC2::Volume",
      "Condition" : "CreateProdResources",
      "Properties" : {
        "Size" : "100",
        "AvailabilityZone" : { "Fn::GetAtt" : [ "EC2Instance", "AvailabilityZone" ]}
      }
    }
  }
}
```

###### Example YAML

```
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  EnvType:
    Description: Environment type.
    Default: test
    Type: String
    AllowedValues: [prod, dev, test]
    ConstraintDescription: must specify prod, dev, or test.
Conditions:
  CreateProdResources: !Equals [!Ref EnvType, prod]
  CreateDevResources: !Equals [!Ref EnvType, "dev"]
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-1234567890abcdef0
      InstanceType: !If [CreateProdResources, c5.xlarge, !If [CreateDevResources, t3.medium, t3.small]]
  MountPoint:
    Type: AWS::EC2::VolumeAttachment
    Condition: CreateProdResources
    Properties:
      InstanceId: !Ref EC2Instance
      VolumeId: !Ref NewVolume
      Device: /dev/sdh
  NewVolume:
    Type: AWS::EC2::Volume
    Condition: CreateProdResources
    Properties:
      Size: 100
      AvailabilityZone: !GetAtt EC2Instance.AvailabilityZone
```

###### Note

For more complext examples of using conditions to create resources, see the [Condition attribute](aws-attribute-condition.md "aws-attribute-condition.md") topic.
