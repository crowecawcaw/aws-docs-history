# Create wait conditions in a CloudFormation
 template

This topic explains how to create a wait condition in a template to coordinate the
 creation of stack resources or track the progress of a configuration process. For example,
 you can start the creation of another resource after an application configuration is
 partially complete, or you can send signals during an installation and configuration process
 to track its progress. 

When CloudFormation creates a stack that includes a wait condition:


* It creates a wait condition just like any other resource and sets the wait
 condition’s status to `CREATE_IN_PROGRESS`.
* CloudFormation waits until it receives the requisite number of success signals or the
 wait condition’s timeout period has expired.
* If it receives the requisite number of success signals before the timeout period
 expires:




	+ Wait condition status changes to `CREATE_COMPLETE`
	+ Stack creation continues
* If timeout expires or a failure signal is received:




	+ Wait condition status changes to `CREATE_FAILED`
	+ Stack rolls back
###### Important

For Amazon EC2 and Auto Scaling resources, we recommend that you use a CreationPolicy attribute instead of wait conditions.
Add a CreationPolicy attribute to those resources, and use the cfn-signal helper script to signal when an instance creation process has completed successfully.

For more information, see [CreationPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-creationpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-creationpolicy.html").

###### Note

If you use AWS PrivateLink, resources in the VPC that respond to wait conditions must
 have access to CloudFormation-specific Amazon Simple Storage Service (Amazon S3) buckets. Resources must send wait
 condition responses to a presigned Amazon S3 URL. If they can't send responses to Amazon S3,
 CloudFormation won't receive a response and the stack operation fails. For more information,
 see [Access CloudFormation using an interface endpoint
 (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md")
 and [Controlling access from VPC endpoints with bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html").

###### Topics

* [Creating a wait condition in your
 template](#creating-wait-condition "#creating-wait-condition")
* [Wait condition signal syntax](#wait-condition-signal-syntax "#wait-condition-signal-syntax")
* [Accessing signal data](#wait-condition-access-signal-data "#wait-condition-access-signal-data")

## Creating a wait condition in your
 template


###### 1. Wait condition handle


You start by defining a [AWS::CloudFormation::WaitConditionHandle](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitconditionhandle.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitconditionhandle.html") resource in
 the stack's template. This resource generates the presigned URL needed for sending
 signals. This allows you to send a signal without having to supply your AWS
 credentials. For example: 



```
Resources:
  `MyWaitHandle`:
    Type: AWS::CloudFormation::WaitConditionHandle
```

###### 2. Wait condition


Next, you define an [AWS::CloudFormation::WaitCondition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitcondition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitcondition.html") resource in the
 stack's template. The basic structure of a
 `AWS::CloudFormation::WaitCondition` looks like this: 



```
  `MyWaitCondition`:
    Type: AWS::CloudFormation::WaitCondition
    Properties:
      Handle: `String`
      Timeout: `String`
      Count: `Integer`
```

The `AWS::CloudFormation::WaitCondition` resource has two required
 properties and one optional property.



* `Handle` (required) – A reference to a
 `WaitConditionHandle` declared in the template.
* `Timeout` (required) – The number of seconds for CloudFormation
 to wait for the requisite number of signals to be received. `Timeout`
 is a minimum-bound property, meaning the timeout occurs no sooner than the time
 you specify, but can occur shortly thereafter. The maximum time that you can
 specify is 43200 seconds (12 hours ).
* `Count` (optional) – The number of success signals that
 CloudFormation must receive before it sets that wait condition’s status to
 `CREATE_COMPLETE` and resumes creating the stack. If not
 specified, the default value is 1.

Typically, you want a wait condition to begin immediately after the creation of a
 specific resource. You do this by adding the `DependsOn` attribute to a wait condition. When you add a
 `DependsOn` attribute to a wait condition, CloudFormation creates the
 resource in the `DependsOn` attribute first, and then creates the wait
 condition. For more information, see [DependsOn attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-dependson.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-dependson.html").


The following example demonstrates a wait condition that: 



* Begins after the successful creation of the `MyEC2Instance`
 resource
* Uses the `MyWaitHandle` resource as the
 `WaitConditionHandle`
* Has a timeout of 4500 seconds
* Has the default `Count` of 1 (since no `Count` property
 is specified)


```
  `MyWaitCondition`:
    Type: AWS::CloudFormation::WaitCondition
    DependsOn: `MyEC2Instance`
    Properties:
      Handle: `!Ref MyWaitHandle`
      Timeout: `'4500'`
```

###### 3. Sending a signal


To signal success or failure to CloudFormation, you typically run some code or script.
 For example, an application running on an EC2 instance might perform some additional
 configuration tasks and then send a signal to CloudFormation to indicate
 completion.


The signal must be sent to the presigned URL generated by the wait condition handle.
 You use that presigned URL to signal success or failure.


###### To send a signal

1. To retrieve the presigned URL within the template, use the `Ref`
 intrinsic function with the logical name of the wait condition handle. 


As shown in the following example, your template can declare an Amazon EC2 instance
 and pass the presigned URL to EC2 instances using the Amazon EC2
 `UserData` property. This allows scripts or applications running
 on those instances to signal success or failure to CloudFormation.



```
  `MyEC2Instance`:
    Type: AWS::EC2::Instance
    Properties:
    InstanceType: `t2.micro`  # Example instance type
    ImageId: `ami-055e3d4f0bbeb5878`  # Change this as needed (Amazon Linux 2023 in us-west-2)
    UserData:
      Fn::Base64: 
        Fn::Join: 
          - ""
          - - `"SignalURL="`
            - { "Ref": `"MyWaitHandle"` }
```

This results in `UserData` output similar to:



```
`SignalURL=https://amzn-s3-demo-bucket.s3.amazonaws.com/....`
```

Note: In the AWS Management Console and the command line tools, the presigned URL is
 displayed as the physical ID of the wait condition handle resource.
2. (Optional) To detect when the stack enters the wait condition, you can use one
 of the following methods:




	* If you create the stack with notifications enabled, CloudFormation
	 publishes a notification for every stack event to the specified topic.
	 If you or your application subscribe to that topic, you can monitor the
	 notifications for the wait condition handle creation event and retrieve
	 the presigned URL from the notification message.
	* You can also monitor the stack's events using the AWS Management Console, the
	 AWS CLI, or an SDK.
3. To send a signal, you send an HTTP request message using the presigned URL.
 The request method must be `PUT` and the `Content-Type`
 header must be an empty string or omitted. The request message must be a JSON
 structure of the form specified in [Wait condition signal syntax](#wait-condition-signal-syntax "#wait-condition-signal-syntax").


You must send the number of success signals specified by the
 `Count` property in order for CloudFormation to continue stack
 creation. If you have a `Count` that is greater than 1, the
 `UniqueId` value for each signal must be unique across all
 signals sent to a particular wait condition. The `UniqueId` is an
 arbitrary alphanumerical string.


A `curl` command is one way to send a signal. The following example
 shows a `curl` command line that signals success to a wait
 condition.



```
`$` curl -T `/tmp/a` \
  `"https://amzn-s3-demo-bucket.s3.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-west-2%3A034017226601%3Astack%2Fstack-gosar-20110427004224-test-stack-with-WaitCondition--VEYW%2Fe498ce60-70a1-11e0-81a7-5081d0136786%2FmyWaitConditionHandle?Expires=1303976584&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Signature=ik1twT6hpS4cgNAw7wyOoRejVoo%3D"`
```

where the file ``/tmp/a`` contains
 the following JSON structure:



```
{
   "Status" : `"SUCCESS"`,
   "Reason" : `"Configuration Complete"`,
   "UniqueId" : `"ID1234"`,
   "Data" : `"Application has completed configuration."`
}
```

This example shows a `curl` command line that sends the same
 success signal except it sends the JSON structure as a parameter on the command
 line.



```
`$` curl -X PUT \
  -H 'Content-Type:' --data-binary `'{"Status" : "SUCCESS","Reason" : "Configuration Complete","UniqueId" : "ID1234","Data" : "Application has completed configuration."}'` \
  `"https://amzn-s3-demo-bucket.s3.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-west-2%3A034017226601%3Astack%2Fstack-gosar-20110427004224-test-stack-with-WaitCondition--VEYW%2Fe498ce60-70a1-11e0-81a7-5081d0136786%2FmyWaitConditionHandle?Expires=1303976584&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Signature=ik1twT6hpS4cgNAw7wyOoRejVoo%3D"`
```

## Wait condition signal syntax


When you send signals to the URL generated by the wait condition handle, you must use
 the following JSON format:



```
{
  "Status" : `"StatusValue"`,
  "UniqueId" : `"Some UniqueId"`,
  "Data" : `"Some Data"`,
  "Reason" : `"Some Reason"`
}
```

### Properties


The `Status` field must be one of the following values:



* `SUCCESS`
* `FAILURE`

The `UniqueId` field identifies the signal to CloudFormation. If the
 `Count` property of the wait condition is greater than 1, the
 `UniqueId` value must be unique across all signals sent for a
 particular wait condition; otherwise, CloudFormation will consider the signal a
 retransmission of the previously sent signal with the same `UniqueId` and
 ignore it.


The `Data` field can contain any information you want to send back with
 the signal. You can access the `Data` value by using the [Fn::GetAtt](resources-section-structure.md#resource-properties-getatt "resources-section-structure.md#resource-properties-getatt") function within
 the template.


The `Reason` field is a string with no other restrictions on its
 content besides JSON compliance.


## Accessing signal data


To access the data sent by valid signals, you can create an output value for the wait
 condition in your CloudFormation template. For example:



```
Outputs:
  `WaitConditionData`:
    Description: `The data passed back as part of signalling the WaitCondition`
    Value: !GetAtt `MyWaitCondition`.Data
```

You can then view this data using the [describe-stacks](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html") command, or the
 **Outputs** tab of the CloudFormation console.


The `Fn::GetAtt` function returns the `UniqueId` and
 `Data` as a name/value pair within a JSON structure. For example:



```
`{"Signal1":"Application has completed configuration."}`
```
