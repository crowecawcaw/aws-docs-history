# Using action outputs as

inputs

Several automation actions return pre-defined outputs. You can pass these outputs
as inputs to later steps in your runbook using the format
`{{`stepName`.`outputName`}}`.
You can also define custom outputs for automation actions in your runbooks. This
allows you to run scripts, or invoke API operations for other AWS services once so
you can reuse the values as inputs in later actions. Parameter types in runbooks are
static. This means the parameter type can't be changed after it's defined. To define
a step output provide the following fields:

- Name: (Required) The output name which is used to reference the output
  value in later steps.
- Selector: (Required) The JSONPath expression that is used to determine the
  output value.
- Type: (Optional) The data type of the value returned by the selector
  field. Valid type values are `String`, `Integer`,
  `Boolean`, `StringList`, `StringMap`,
  `MapList`. The default value is `String`.
  If the value of an output doesn't match the data type you've specified, Automation
  tries to convert the data type. For example, if the value returned is an
  `Integer`, but the `Type` specified is
  `String`, the final output value is a `String` value. The
  following type conversions are supported:

- `String` values can be converted to `StringList`,
  `Integer` and `Boolean`.
- `Integer` values can be converted to `String` and
  `StringList`.
- `Boolean` values can be converted to `String` and
  `StringList`.
- `StringList`, `IntegerList`, or
  `BooleanList` values containing one element can be converted
  to `String`, `Integer`, or
  `Boolean`.
  When using parameters or outputs with automation actions, the data type can't be
  dynamically changed within an action's input.

Here is an example runbook that demonstrates how to define action outputs, and
reference the value as input for a later action. The runbooks does the
following:

- Uses the `aws:executeAwsApi` action to call the Amazon EC2
  DescribeImages API operation to get the name of a specific Windows Server
  2016 AMI. It outputs the image ID as `ImageId`.
- Uses the `aws:executeAwsApi` action to call the Amazon EC2
  RunInstances API operation to launch one instance that uses the
  `ImageId` from the previous step. It outputs the instance ID
  as `InstanceId`.
- Uses the `aws:waitForAwsResourceProperty` action to poll the
  Amazon EC2 DescribeInstanceStatus API operation to wait for the instance to reach
  the `running` state. The action times out in 60 seconds. The step
  times out if the instance state failed to reach `running` after
  60 seconds of polling.
- Uses the `aws:assertAwsResourceProperty` action to call the
  Amazon EC2 `DescribeInstanceStatus` API operation to assert that the
  instance is in the `running` state. The step fails if the
  instance state isn't `running`.

```
---
description: Sample runbook using AWS API operations
schemaVersion: '0.3'
assumeRole: "{{ AutomationAssumeRole }}"
parameters:
  AutomationAssumeRole:
    type: String
    description: "(Optional) The ARN of the role that allows Automation to perform the actions on your behalf."
    default: ''
  ImageName:
    type: String
    description: "(Optional) Image Name to launch EC2 instance with."
    default: "Windows_Server-2022-English-Full-Base*"
mainSteps:
- name: getImageId
  action: aws:executeAwsApi
  inputs:
    Service: ec2
    Api: DescribeImages
    Filters:
    - Name: "name"
      Values:
      - "{{ ImageName }}"
  outputs:
  - Name: ImageId
    Selector: "$.Images[0].ImageId"
    Type: "String"
- name: launchOneInstance
  action: aws:executeAwsApi
  inputs:
    Service: ec2
    Api: RunInstances
    ImageId: "{{ getImageId.ImageId }}"
    MaxCount: 1
    MinCount: 1
  outputs:
  - Name: InstanceId
    Selector: "$.Instances[0].InstanceId"
    Type: "String"
- name: waitUntilInstanceStateRunning
  action: aws:waitForAwsResourceProperty
  timeoutSeconds: 60
  inputs:
    Service: ec2
    Api: DescribeInstanceStatus
    InstanceIds:
    - "{{ launchOneInstance.InstanceId }}"
    PropertySelector: "$.InstanceStatuses[0].InstanceState.Name"
    DesiredValues:
    - running
- name: assertInstanceStateRunning
  action: aws:assertAwsResourceProperty
  inputs:
    Service: ec2
    Api: DescribeInstanceStatus
    InstanceIds:
    - "{{ launchOneInstance.InstanceId }}"
    PropertySelector: "$.InstanceStatuses[0].InstanceState.Name"
    DesiredValues:
    - running
outputs:
- "launchOneInstance.InstanceId"
...
```

Each of the previously described automation actions allows you to call a specific
API operation by specifying the service namespace, the API operation name, the input
parameters, and the output parameters. Inputs are defined by the API operation that
you choose. You can view the API operations (also called methods) by choosing a
service in the left navigation on the following [Services Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html") page. Choose a method in the
**Client** section for the service that you want to invoke. For
example, all API operations (methods) for Amazon Relational Database Service (Amazon RDS) are listed on the
following page: [Amazon RDS methods](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html").

You can view the schema for each automation action in the following
locations:

- [aws:assertAwsResourceProperty – Assert an AWS resource
  state or event state](automation-action-assertAwsResourceProperty.md "automation-action-assertAwsResourceProperty.md")
- [aws:executeAwsApi
  – Call and run AWS API operations](automation-action-executeAwsApi.md "automation-action-executeAwsApi.md")
- [aws:waitForAwsResourceProperty – Wait on an AWS resource
  property](automation-action-waitForAwsResourceProperty.md "automation-action-waitForAwsResourceProperty.md")
  The schemas include descriptions of the required fields for using each
  action.

###### Using the Selector/PropertySelector fields

Each Automation action requires that you specify either an output
`Selector` (for `aws:executeAwsApi`) or a
`PropertySelector` (for
`aws:assertAwsResourceProperty` and
`aws:waitForAwsResourceProperty`). These fields are used to
process the JSON response from an AWS API operation. These fields use the
JSONPath syntax.

Here is an example to help illustrate this concept for the
`aws:executeAwsAPi` action.

```
---
mainSteps:
- name: getImageId
  action: aws:executeAwsApi
  inputs:
    Service: ec2
    Api: DescribeImages
    Filters:
      - Name: "name"
        Values:
          - "{{ ImageName }}"
  outputs:
    - Name: ImageId
      Selector: "$.Images[0].ImageId"
      Type: "String"
...
```

In the `aws:executeAwsApi` step `getImageId`, the automation
invokes the `DescribeImages` API operation and receives a response from
`ec2`. The automation then applies `Selector -
 "$.Images[0].ImageId"` to the API response and assigns the selected value
to the output `ImageId` variable. Other steps in the same automation can
use the value of `ImageId` by specifying `"{{ getImageId.ImageId
 }}"`.

Here is an example to help illustrate this concept for the
`aws:waitForAwsResourceProperty` action.

```
---
- name: waitUntilInstanceStateRunning
  action: aws:waitForAwsResourceProperty
  # timeout is strongly encouraged for action - aws:waitForAwsResourceProperty
  timeoutSeconds: 60
  inputs:
    Service: ec2
    Api: DescribeInstanceStatus
    InstanceIds:
    - "{{ launchOneInstance.InstanceId }}"
    PropertySelector: "$.InstanceStatuses[0].InstanceState.Name"
    DesiredValues:
    - running
...
```

In the `aws:waitForAwsResourceProperty` step
`waitUntilInstanceStateRunning`, the automation invokes the
`DescribeInstanceStatus` API operation and receives a response from
`ec2`. The automation then applies `PropertySelector -
 "$.InstanceStatuses[0].InstanceState.Name"` to the response and checks if
the specified returned value matches a value in the `DesiredValues` list
(in this case `running`). The step repeats the process until the response
returns an instance state of `running`.

## Using JSONPath in runbooks

A JSONPath expression is a string beginning with "$." that is used to select
one of more components within a JSON element. The following list includes
information about JSONPath operators that are supported by Systems Manager
Automation:

- **Dot-notated child (.)**: Use with a
  JSON object. This operator selects the value of a specific key.
- **Deep-scan (..)**: Use with a JSON
  element. This operator scans the JSON element level by level and selects
  a list of values with the specific key. The return type of this operator
  is always a JSON array. In the context of an automation action output
  type, the operator can be either StringList or MapList.
- **Array-Index ([ ])**: Use with a JSON
  array. This operator gets the value of a specific index.
- **Filter
  ([?(`expression`)])**: Use with a
  JSON array. This operator filters JSON array values that match the
  criteria defined in the filter expression. Filter expressions can only
  use the following operators: ==, !=, >, <, >=, or <=.
  Combining multiple filter expressions with AND (&&) or OR (||)
  is not supported. The return type of this operator is always a JSON
  array.

To better understand JSONPath operators, review the following JSON response
from the ec2 `DescribeInstances` API operation. Following this
response are several examples that show different results by applying different
JSONPath expressions to the response from the `DescribeInstances` API
operation.

```
{
    "NextToken": "abcdefg",
    "Reservations": [
        {
            "OwnerId": "123456789012",
            "ReservationId": "r-abcd12345678910",
            "Instances": [
                {
                    "ImageId": "ami-12345678",
                    "BlockDeviceMappings": [
                        {
                            "Ebs": {
                                "DeleteOnTermination": true,
                                "Status": "attached",
                                "VolumeId": "vol-000000000000"
                            },
                            "DeviceName": "/dev/xvda"
                        }
                    ],
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    }
                }
            ],
            "Groups": []
        },
        {
            "OwnerId": "123456789012",
            "ReservationId": "r-12345678910abcd",
            "Instances": [
                {
                    "ImageId": "ami-12345678",
                    "BlockDeviceMappings": [
                        {
                            "Ebs": {
                                "DeleteOnTermination": true,
                                "Status": "attached",
                                "VolumeId": "vol-111111111111"
                            },
                            "DeviceName": "/dev/xvda"
                        }
                    ],
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    }
                }
            ],
            "Groups": []
        }
    ]
}
```

**JSONPath Example 1: Get a specific String from a JSON
response**

```
JSONPath:
$.Reservations[0].Instances[0].ImageId

Returns:
"ami-12345678"

Type: String
```

**JSONPath Example 2: Get a specific Boolean from a JSON
response**

```
JSONPath:
$.Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.DeleteOnTermination

Returns:
true

Type: Boolean
```

**JSONPath Example 3: Get a specific Integer from a JSON
response**

```
JSONPath:
$.Reservations[0].Instances[0].State.Code

Returns:
16

Type: Integer
```

**JSONPath Example 4: Deep scan a JSON response, then get
all of the values for VolumeId as a StringList**

```
JSONPath:
$.Reservations..BlockDeviceMappings..VolumeId

Returns:
[
   "vol-000000000000",
   "vol-111111111111"
]

Type: StringList
```

**JSONPath Example 5: Get a specific BlockDeviceMappings
object as a StringMap**

```
JSONPath:
$.Reservations[0].Instances[0].BlockDeviceMappings[0]

Returns:
{
   "Ebs" : {
      "DeleteOnTermination" : true,
      "Status" : "attached",
      "VolumeId" : "vol-000000000000"
   },
   "DeviceName" : "/dev/xvda"
}

Type: StringMap
```

**JSONPath Example 6: Deep scan a JSON response, then get
all of the State objects as a MapList**

```
JSONPath:
$.Reservations..Instances..State

Returns:
[
   {
      "Code" : 16,
      "Name" : "running"
   },
   {
      "Code" : 80,
      "Name" : "stopped"
   }
]

Type: MapList

```

**JSONPath Example 7: Filter for instances in the
`running` state**

```
JSONPath:
$.Reservations..Instances[?(@.State.Name == 'running')]

Returns:
[
  {
    "ImageId": "ami-12345678",
    "BlockDeviceMappings": [
      {
        "Ebs": {
          "DeleteOnTermination": true,
          "Status": "attached",
          "VolumeId": "vol-000000000000"
        },
        "DeviceName": "/dev/xvda"
      }
    ],
    "State": {
      "Code": 16,
      "Name": "running"
    }
  }
]

Type: MapList

```

**JSONPath Example 8: Return the `ImageId` of
instances which aren't in the `running` state**

```
JSONPath:
$.Reservations..Instances[?(@.State.Name != 'running')].ImageId

Returns:
[
  "ami-12345678"
]

Type: StringList | String

```
