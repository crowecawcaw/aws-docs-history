AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configuring inputs and outputs for

your actions

Each automation action responds based on input that it receives. In most cases, you then
pass output to the subsequent actions. In the visual design experience, you can configure an action's input
and output data in the **Inputs** and **Outputs** tabs of
the **Form** panel.

For detailed information about how to define and use output for automation
actions, see [Using action outputs as
inputs](automation-action-outputs-inputs.md "automation-action-outputs-inputs.md").

## Provide input data for an action

Each automation action has one or more inputs that you must provide a value for. The
value you provide for an action's input is determined by the data type and format that's
accepted by the action. For example, the `aws:sleep` actions requires an ISO 8601
formatted string value for the `Duration` input.

Generally, you use actions in your runbook's workflow that return output that you want
to use in subsequent actions. It's important to make sure your input values are correct to
avoid errors in your runbook's workflow. Input values are also important because they
determine whether the action returns the expected output. For example, when using the
`aws:executeAwsApi` action, you want to make sure that you're providing the
right value for the API operation.

## Define output data for an action

Some automation actions return output after performing their defined operations. Actions
that return output either have predefined outputs, or allow you to define the outputs
yourself. For example, the `aws:createImage` action has predefined outputs that
return an `ImageId` and `ImageState`. Comparatively, with the
`aws:executeAwsApi` action, you can define the outputs you that want from the
specified API operation. As a result, you can return one or more values from a single API
operation to use in subsequent actions.

Defining your own outputs for an automation action requires that you specify a name of
the output, the data type, and the output value. To continue using the
`aws:executeAwsApi` action as an example, let's say you're calling the
`DescribeInstances` API operation from Amazon EC2. In this example, you want to
return, or output, the `State` of an Amazon EC2 instance and branch your runbook's
workflow based on the output. You choose to name the output
`InstanceState`, and use the `String` data type.

The process to define the actual value of the output differs, depending on the action.
For example, if you're using the `aws:executeScript` action, you must use
`return` statements in your functions to provide data to your outputs. With
other actions like `aws:executeAwsApi`,
`aws:waitForAwsResourceProperty`, and
`aws:assertAwsResourceProperty`, a `Selector` is required. The
`Selector`, or `PropertySelector` as some actions refer to it, is a
JSONPath string that is used to process the JSON response from an API
operation. It's important to understand how the JSON response object from an API operation
is structured so you can select the correct value for your output. Using the
`DescribeInstances` API operation mentioned earlier, see the following example
JSON response:

```
{
  "reservationSet": {
    "item": {
      "reservationId": "r-1234567890abcdef0",
      "ownerId": 123456789012,
      "groupSet": "",
      "instancesSet": {
        "item": {
          "instanceId": "i-1234567890abcdef0",
          "imageId": "ami-bff32ccc",
          "instanceState": {
            "code": 16,
            "name": "running"
          },
          "privateDnsName": "ip-192-168-1-88.eu-west-1.compute.internal",
          "dnsName": "ec2-54-194-252-215.eu-west-1.compute.amazonaws.com",
          "reason": "",
          "keyName": "my_keypair",
          "amiLaunchIndex": 0,
          "productCodes": "",
          "instanceType": "t2.micro",
          "launchTime": "2018-05-08T16:46:19.000Z",
          "placement": {
            "availabilityZone": "eu-west-1c",
            "groupName": "",
            "tenancy": "default"
          },
          "monitoring": {
            "state": "disabled"
          },
          "subnetId": "subnet-56f5f000",
          "vpcId": "vpc-11112222",
          "privateIpAddress": "192.168.1.88",
          "ipAddress": "54.194.252.215",
          "sourceDestCheck": true,
          "groupSet": {
            "item": {
              "groupId": "sg-e4076000",
              "groupName": "SecurityGroup1"
            }
          },
          "architecture": "x86_64",
          "rootDeviceType": "ebs",
          "rootDeviceName": "/dev/xvda",
          "blockDeviceMapping": {
            "item": {
              "deviceName": "/dev/xvda",
              "ebs": {
                "volumeId": "vol-1234567890abcdef0",
                "status": "attached",
                "attachTime": "2015-12-22T10:44:09.000Z",
                "deleteOnTermination": true
              }
            }
          },
          "virtualizationType": "hvm",
          "clientToken": "xMcwG14507example",
          "tagSet": {
            "item": {
              "key": "Name",
              "value": "Server_1"
            }
          },
          "hypervisor": "xen",
          "networkInterfaceSet": {
            "item": {
              "networkInterfaceId": "eni-551ba000",
              "subnetId": "subnet-56f5f000",
              "vpcId": "vpc-11112222",
              "description": "Primary network interface",
              "ownerId": 123456789012,
              "status": "in-use",
              "macAddress": "02:dd:2c:5e:01:69",
              "privateIpAddress": "192.168.1.88",
              "privateDnsName": "ip-192-168-1-88.eu-west-1.compute.internal",
              "sourceDestCheck": true,
              "groupSet": {
                "item": {
                  "groupId": "sg-e4076000",
                  "groupName": "SecurityGroup1"
                }
              },
              "attachment": {
                "attachmentId": "eni-attach-39697adc",
                "deviceIndex": 0,
                "status": "attached",
                "attachTime": "2018-05-08T16:46:19.000Z",
                "deleteOnTermination": true
              },
              "association": {
                "publicIp": "54.194.252.215",
                "publicDnsName": "ec2-54-194-252-215.eu-west-1.compute.amazonaws.com",
                "ipOwnerId": "amazon"
              },
              "privateIpAddressesSet": {
                "item": {
                  "privateIpAddress": "192.168.1.88",
                  "privateDnsName": "ip-192-168-1-88.eu-west-1.compute.internal",
                  "primary": true,
                  "association": {
                    "publicIp": "54.194.252.215",
                    "publicDnsName": "ec2-54-194-252-215.eu-west-1.compute.amazonaws.com",
                    "ipOwnerId": "amazon"
                  }
                }
              },
              "ipv6AddressesSet": {
                "item": {
                  "ipv6Address": "2001:db8:1234:1a2b::123"
                }
              }
            }
          },
          "iamInstanceProfile": {
            "arn": "arn:aws:iam::123456789012:instance-profile/AdminRole",
            "id": "ABCAJEDNCAA64SSD123AB"
          },
          "ebsOptimized": false,
          "cpuOptions": {
            "coreCount": 1,
            "threadsPerCore": 1
          }
        }
      }
    }
  }
}
```

In the JSON response object, the instance `State` is nested in an
`Instances` object, which is nested in the `Reservations` object. To
return the value of the instance `State`, use the following string for the
`Selector` so the value can be used in our output:
`$.Reservations[0].Instances[0].State.Name`.

To reference an output value in subsequent actions of your runbook's workflow, the
following format is used: `{{
`StepName`.`NameOfOutput` }}`.
For example, `{{ GetInstanceState.InstanceState }}`. In the
visual design experience, you can choose output values to use in subsequent actions using the dropdown
for the input. When using outputs in subsequent actions, the data type of the output must
match the data type for the input. In this example, the `InstanceState` output is
a `String`. Therefore, to use the value in a subsequent action's input, the input
must accept a `String`.
