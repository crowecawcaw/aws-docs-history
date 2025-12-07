# CloudFormation template snippets

###### Topics

- [Nested stacks](#w2aac11c41c23b5 "#w2aac11c41c23b5")
- [Wait condition](#w2aac11c41c23b7 "#w2aac11c41c23b7")

## Nested stacks

### Nesting a stack in a template

This example template contains a nested stack resource called `myStack`. When CloudFormation creates a stack from the template, it creates the `myStack`, whose template is specified in the `TemplateURL` property.
The output value `StackRef` returns the stack ID for `myStack` and the value `OutputFromNestedStack` returns the output value `BucketName` from within the `myStack` resource.
The `Outputs.`nestedstackoutputname`` format is reserved for specifying output values from nested stacks and can be used anywhere within the containing template.

For more information, see [AWS::CloudFormation::Stack](../TemplateReference/aws-resource-cloudformation-stack.md "../TemplateReference/aws-resource-cloudformation-stack.md").

#### JSON

```
{
    "AWSTemplateFormatVersion" : "2010-09-09",
    "Resources" : {
        "myStack" : {
	       "Type" : "AWS::CloudFormation::Stack",
	       "Properties" : {
	        "TemplateURL" : "https://s3.amazonaws.com/cloudformation-templates-us-east-1/S3_Bucket.template",
              "TimeoutInMinutes" : "60"
	       }
        }
    },
    "Outputs": {
       "StackRef": {"Value": { "Ref" : "myStack"}},
       "OutputFromNestedStack" : {
             "Value" : { "Fn::GetAtt" : [ "myStack", "Outputs.BucketName" ] }
       }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-templates-us-east-1/S3_Bucket.template
      TimeoutInMinutes: '60'
Outputs:
  StackRef:
    Value: !Ref myStack
  OutputFromNestedStack:
    Value: !GetAtt myStack.Outputs.BucketName
```

### Nesting a stack with input parameters in a

template

This example template contains a stack resource that specifies input parameters. When CloudFormation creates a stack from this template, it uses the value pairs declared within the `Parameters` property as the input parameters for the template used to create the `myStackWithParams` stack. In this example, the `InstanceType` and `KeyName` parameters are specified.

For more information, see [AWS::CloudFormation::Stack](../TemplateReference/aws-resource-cloudformation-stack.md "../TemplateReference/aws-resource-cloudformation-stack.md").

#### JSON

```
{
    "AWSTemplateFormatVersion" : "2010-09-09",
    "Resources" : {
        "myStackWithParams" : {
  	       "Type" : "AWS::CloudFormation::Stack",
	       "Properties" : {
	           "TemplateURL" : "https://s3.amazonaws.com/cloudformation-templates-us-east-1/EC2ChooseAMI.template",
	           "Parameters" : {
	               "InstanceType" : "t2.micro",
	               "KeyName" : "mykey"
	           }
   	       }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myStackWithParams:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-templates-us-east-1/EC2ChooseAMI.template
      Parameters:
        InstanceType: t2.micro
        KeyName: mykey
```

## Wait condition

### Using a wait condition with an Amazon EC2

instance

###### Important

For Amazon EC2 and Amazon EC2 Auto Scaling resources, we recommend that you use a CreationPolicy attribute instead of wait conditions.
Add a CreationPolicy attribute to those resources, and use the cfn-signal helper script to signal when an instance creation process has completed successfully.

If you can't use a creation policy, you view the following example template, which
declares an Amazon EC2 instance with a wait condition. The `myWaitCondition` wait condition
uses `myWaitConditionHandle` for signaling, uses the `DependsOn` attribute to specify that the
wait condition will trigger after the Amazon EC2 instance resource has been created, and
uses the `Timeout` property to specify a duration of 4500 seconds for the wait
condition. In addition, the presigned URL that signals the wait condition is passed
to the Amazon EC2 instance with the `UserData` property of the `Ec2Instance` resource, thus
allowing an application or script running on that Amazon EC2 instance to retrieve the
presigned URL and employ it to signal a success or failure to the wait condition.
You need to use `cfn-signal` or create the application or script that signals the wait
condition. The output value `ApplicationData` contains the data passed back from the
wait condition signal.

For more information, see [Create wait conditions in a CloudFormation
template](using-cfn-waitcondition.md "using-cfn-waitcondition.md").

#### JSON

```
{
    "AWSTemplateFormatVersion" : "2010-09-09",
    "Mappings" : {
        "RegionMap" : {
            "us-east-1" : {
                "AMI" : "ami-0123456789abcdef0"
            },
            "us-west-1" : {
                "AMI" : "ami-0987654321fedcba0"
            },
            "eu-west-1" : {
                "AMI" : "ami-0abcdef123456789a"
            },
            "ap-northeast-1" : {
                "AMI" : "ami-0fedcba987654321b"
            },
            "ap-southeast-1" : {
                "AMI" : "ami-0c1d2e3f4a5b6c7d8"
            }
        }
    },
    "Resources" : {
        "Ec2Instance" : {
            "Type" : "AWS::EC2::Instance",
            "Properties" : {
                "UserData" : { "Fn::Base64" : {"Ref" : "myWaitHandle"}},
                "ImageId" : { "Fn::FindInMap" : [ "RegionMap", { "Ref" : "AWS::Region" }, "AMI" ]}
            }
        },
        "myWaitHandle" : {
            "Type" : "AWS::CloudFormation::WaitConditionHandle",
            "Properties" : {
            }
        },
        "myWaitCondition" : {
            "Type" : "AWS::CloudFormation::WaitCondition",
            "DependsOn" : "Ec2Instance",
            "Properties" : {
                "Handle" : { "Ref" : "myWaitHandle" },
                "Timeout" : "4500"
            }
        }
    },
    "Outputs" : {
        "ApplicationData" : {
            "Value" : { "Fn::GetAtt" : [ "myWaitCondition", "Data" ]},
            "Description" : "The data passed back as part of signalling the WaitCondition."
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-0123456789abcdef0
    us-west-1:
      AMI: ami-0987654321fedcba0
    eu-west-1:
      AMI: ami-0abcdef123456789a
    ap-northeast-1:
      AMI: ami-0fedcba987654321b
    ap-southeast-1:
      AMI: ami-0c1d2e3f4a5b6c7d8
Resources:
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      UserData:
        Fn::Base64: !Ref myWaitHandle
      ImageId:
        Fn::FindInMap:
        - RegionMap
        - Ref: AWS::Region
        - AMI
  myWaitHandle:
    Type: AWS::CloudFormation::WaitConditionHandle
    Properties: {}
  myWaitCondition:
    Type: AWS::CloudFormation::WaitCondition
    DependsOn: Ec2Instance
    Properties:
      Handle: !Ref myWaitHandle
      Timeout: '4500'
Outputs:
  ApplicationData:
    Value: !GetAtt myWaitCondition.Data
    Description: The data passed back as part of signalling the WaitCondition.
```

### Using the cfn-signal helper script to signal a wait

condition

This example shows a `cfn-signal` command line that signals success to a wait
condition. You need to define the command line in the `UserData`
property of the EC2 instance.

#### JSON

```
"UserData": {
  "Fn::Base64": {
    "Fn::Join": [
      "",
      [
         "#!/bin/bash -xe\n",
         "/opt/aws/bin/cfn-signal --exit-code 0 '",
         {
           "Ref": "myWaitHandle"
         },
         "'\n"
      ]
    ]
  }
}
```

#### YAML

```
UserData:
  'Fn::Base64':
    'Fn::Join':
      - ''
      - - |
          #!/bin/bash -xe
        - /opt/aws/bin/cfn-signal --exit-code 0 '
        - Ref: myWaitHandle
        - |
          '
```

### Using Curl to signal a wait

condition

This example shows a Curl command line that signals success to a wait
condition.

```
curl -T /tmp/a "https://cloudformation-waitcondition-test.s3.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-east-1%3A034017226601%3Astack%2Fstack-gosar-20110427004224-test-stack-with-WaitCondition--VEYW%2Fe498ce60-70a1-11e0-81a7-5081d0136786%2FmyWaitConditionHandle?Expires=1303976584&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Signature=ik1twT6hpS4cgNAw7wyOoRejVoo%3D"
```

Where the file /tmp/a contains the following JSON structure:

```
{
  "Status" : "SUCCESS",
  "Reason" : "Configuration Complete",
  "UniqueId" : "ID1234",
  "Data" : "Application has completed configuration."
}
```

This example shows a Curl command line that sends the same success signal except
it sends the JSON as a parameter on the command line.

```
curl -X PUT -H 'Content-Type:' --data-binary '{"Status" : "SUCCESS","Reason" : "Configuration Complete","UniqueId" : "ID1234","Data" : "Application has completed configuration."}' "https://cloudformation-waitcondition-test.s3.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-east-1%3A034017226601%3Astack%2Fstack-gosar-20110427004224-test-stack-with-WaitCondition--VEYW%2Fe498ce60-70a1-11e0-81a7-5081d0136786%2FmyWaitConditionHandle?Expires=1303976584&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Signature=ik1twT6hpS4cgNAw7wyOoRejVoo%3D"
```
