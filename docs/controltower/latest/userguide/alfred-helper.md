# The ‘alfred’ helper and the AWS CloudFormation parameter files

CfCT provides you with a mechanism known as the _alfred_ helper to get the value for an [SSM
Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") key that's defined in the AWS CloudFormation template.

Using the _alfred_ helper, you can use values that are
stored in the SSM Parameter Store and without updating the AWS CloudFormation template. For more
information, see [What is an AWS CloudFormation template?](../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md#gettingstarted.templatebasics.what "../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md#gettingstarted.templatebasics.what") in the _AWS CloudFormation User Guide_.

###### Important

The _alfred_ helper has two limitations. Parameters
are available only in the home region of the AWS Control Tower management account. As a best
practice, consider working with values that don't change from stack instance to stack
instance. When the 'alfred' helper retreives parameters, it chooses a random stack
instance from the stack set that exports the variable.

## Example

Suppose that you have two AWS CloudFormation stack sets. _Stack set 1_ has one
stack instance and deploys to one account in one Region. It creates an Amazon VPC and subnets
in an availability zone, and the `VPC ID` and `subnet ID` must be
passed into _stack set 2_ as parameter values. Before the `VPC
 ID` and `subnet ID` can be passed to _stack set 2_,
the `VPC ID` and `subnet ID` must be stored in _stack set
1_ using `AWS:::SSM::Parameter`. For more information, see [`AWS:::SSM::Parameter`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.md") in the _AWS CloudFormation User
Guide_.

**AWS CloudFormation stack set 1:**

In the following snippet, the _alfred_ helper can gets value for
the `VPC ID` and `subnet ID` from the parameter store and pass them
as input to the StackSet state machine.

```
VpcIdParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Name: '/stack_1/vpc/id'
      Description: Contains the VPC id
      Type: String
      Value: !Ref MyVpc

SubnetIdParameter:
    Type: AWS::SSM::Parameter
    Properties:
      Name: '/stack_1/subnet/id'
      Description: Contains the subnet id
      Type: String
      Value: !Ref MySubnet
```

**AWS CloudFormation stack set 2:**

The snippet shows the parameters that are specified in the AWS CloudFormation stack 2
`manifest.yaml` file.

```
parameters:
      - parameter_key: VpcId
        parameter_value: $[alfred_ssm_/stack_1/vpc/id]
      - parameter_key: SubnetId
        parameter_value: $[alfred_ssm_/stack_1/subnet/id]
```

**AWS CloudFormation stack set 2.1:**

The snippet shows that you can list `alfred_ssm` properties to support
parameters of type _CommaDelimitedList_. For more
information, see [`Parameters`](../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md#parameters-section-structure-properties-type "../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md#parameters-section-structure-properties-type") in the _AWS CloudFormation User Guide_.

```
parameters:
      - parameter_key: VpcId # Type: String
        parameter_value: $[alfred_ssm_/stack_1/vpc/id']
      - parameter_key: SubnetId # Type: String
        parameter_value: $[ alfred_ssm_/stack_1/subnet/id']
      - parameter_key: AvailablityZones # Type: CommaDelimitedList
        parameter_value:   - "$[alfred_ssm_/availability_zone_1]"  - "$[alfred_ssm_/availability_zone_2]"

```
