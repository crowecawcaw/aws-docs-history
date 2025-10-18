# Amazon SNS-backed custom resources

The following topic shows you how to configure a custom resource with a service token that
 specifies the Amazon SNS topic that CloudFormation sends requests to. You also learn the sequence of
 events and messages sent and received as a result of custom resource stack creation, updates,
 and deletion.

With custom resources and Amazon SNS, you can enable scenarios such as adding new resources to a
 stack and injecting dynamic data into a stack. For example, when you create a stack,
 CloudFormation can send a `Create` request to a topic that's monitored by an
 application that's running on an Amazon EC2 instance. The Amazon SNS notification triggers the
 application to carry out additional provisioning tasks, such as retrieve a pool of
 allow-listed Elastic IP addresses. After it's done, the application sends a response (and any
 output data) that notifies CloudFormation to proceed with the stack operation.

When you specify an Amazon SNS topic as the target of a custom resource, CloudFormation sends
 messages to the specified SNS topic during stack operations involving the custom resource. To
 process these messages and perform the necessary actions, you must have a supported endpoint
 subscribed to the SNS topic.

For an introduction to custom resources and how they work, see [Create custom provisioning logic with custom
 resources](template-custom-resources.md "template-custom-resources.md"). For
 information about Amazon SNS and how it works, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/ "https://docs.aws.amazon.com/sns/latest/dg/").


## Using Amazon SNS to
 create custom resources


###### Topics

* [Step 1: Stack creation](#crpg-walkthrough-stack-creation "#crpg-walkthrough-stack-creation")
* [Step 2: Stack updates](#crpg-walkthrough-stack-updates "#crpg-walkthrough-stack-updates")
* [Step 3: Stack deletion](#crpg-walkthrough-stack-deletion "#crpg-walkthrough-stack-deletion")

### Step 1: Stack creation



1. The template developer creates a CloudFormation stack that contains a custom resource. 


In the template example below, we use the custom resource type name
 `Custom::`SeleniumTester`` for the
 custom resource with logical ID
 ``MySeleniumTest``. Custom resource type
 names must be alphanumeric and can have a maximum length of 60 characters. 


The custom resource type is declared with a service token, optional
 provider-specific properties, and optional [Fn::GetAtt](resources-section-structure.md#resource-properties-getatt "resources-section-structure.md#resource-properties-getatt") attributes that are
 defined by the custom resource provider. These properties and attributes can be used to pass
 information from the template developer to the custom resource provider and vice-versa. The service
 token specifies an Amazon SNS topic that the resource provider has configured.



```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Resources" : {
      "`MySeleniumTest`" : {
         "Type": "Custom::`SeleniumTester`",
         "Version" : "1.0",
         "Properties" : {
            "ServiceToken": "arn:aws:sns:`us-west-2`:`123456789012`:`CRTest`",
            `"seleniumTester" : "SeleniumTest()",
 "endpoints" : [ "http://mysite.com", "http://myecommercesite.com/", "http://search.mysite.com" ],
 "frequencyOfTestsPerHour" : [ "3", "2", "4" ]`
         }
      }
   },
   "Outputs" : {
      "`topItem`" : {
         "Value" : { "Fn::GetAtt" : ["`MySeleniumTest`", "`resultsPage`"] }
      },
      "`numRespondents`" : {
         "Value" : { "Fn::GetAtt" : ["`MySeleniumTest"`, "`lastUpdate`"] }
      }
   }
}
```

###### Note

The names and values of the data accessed with
 ``Fn::GetAtt`` are returned by the custom resource provider during
 the provider's response to CloudFormation. If the custom resource provider is a third-party, then
 the template developer must obtain the names of these return values from the
 custom resource provider.
2. CloudFormation sends an Amazon SNS notification to the resource provider with a
 `"RequestType" : "Create"` that contains information about the
 stack, the custom resource properties from the stack template, and an S3 URL for
 the response.


The SNS topic that's used to send the notification is embedded in the template
 in the `ServiceToken` property. To avoid using a hardcoded value, a
 template developer can use a template parameter so that the value is entered at the
 time the stack is launched.


The following example shows a custom resource `Create` request which
 includes a custom resource type name, `Custom::SeleniumTester`, created
 with a `LogicalResourceId` of `MySeleniumTester`:



```
{
   "RequestType" : "Create",
   "ResponseURL" : "http://pre-signed-S3-url-for-response",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "unique id for this create request",
   "ResourceType" : "Custom::SeleniumTester",
   "LogicalResourceId" : "MySeleniumTester",
   "ResourceProperties" : {
      "seleniumTester" : "SeleniumTest()",
      "endpoints" : [ "http://mysite.com", "http://myecommercesite.com/", "http://search.mysite.com" ],
      "frequencyOfTestsPerHour" : [ "3", "2", "4" ]
   }
}
```

For detailed information about the request object for `Create`
 requests, see the [Create request for CloudFormation custom
 resources](crpg-ref-requesttypes-create.md "crpg-ref-requesttypes-create.md") topic.
3. The custom resource provider processes the data sent by the template developer and determines
 whether the `Create` request was successful. The resource provider then
 uses the S3 URL sent by CloudFormation to send a response of either
 `SUCCESS` or `FAILED`.


Depending on the response type, different response fields will be expected by
 CloudFormation. For information about the response fields for a particular request
 type, see the documentation for that request type in the [Custom resource request types](crpg-ref-requesttypes.md "crpg-ref-requesttypes.md")
 section.


In response to a create or update request, the custom resource provider can return data
 elements in the [Data](crpg-ref-responses.md#crpg-ref-responses-data "crpg-ref-responses.md#crpg-ref-responses-data") field of the response. These are name
 value pairs, and the *names* correspond to the
 ``Fn::GetAtt`` attributes used with the custom
 resource in the stack template. The *values* are the data
 that's returned when the template developer calls ``Fn::GetAtt``
 on the resource with the attribute name.


The following is an example of a custom resource response:



```
{
   "Status" : "SUCCESS",
   "PhysicalResourceId" : "Tester1",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "unique id for this create request",
   "LogicalResourceId" : "MySeleniumTester",
   "Data" : {
      "resultsPage" : "http://www.myexampledomain/test-results/guid",
      "lastUpdate" : "2012-11-14T03:30Z"
   }
}
```

For detailed information about the response object for `Create`
 requests, see the [Create request for CloudFormation custom
 resources](crpg-ref-requesttypes-create.md "crpg-ref-requesttypes-create.md") topic.


The `StackId`, `RequestId`, and
 `LogicalResourceId` fields must be copied verbatim from the request.
4. CloudFormation declares the stack status as `CREATE_COMPLETE` or
 `CREATE_FAILED`. If the stack was successfully created, the
 template developer can use the output values of the created custom resource by
 accessing them with [Fn::GetAtt](resources-section-structure.md#resource-properties-getatt "resources-section-structure.md#resource-properties-getatt").


For example, the custom resource template used for illustration used
 ``Fn::GetAtt`` to copy resource outputs into the stack
 outputs:



```
"Outputs" : {
   "`topItem`" : {
      "Value" : { "Fn::GetAtt" : ["`MySeleniumTest`", "`resultsPage`"] }
   },
   "`numRespondents`" : {
      "Value" : { "Fn::GetAtt" : ["`MySeleniumTest`", "`lastUpdate`"] }
   }
}
```

### Step 2: Stack updates


To update an existing stack, you must submit a template that specifies updates for
 the properties of resources in the stack, as shown in the example below. CloudFormation
 updates only the resources that have changes specified in the template. For more
 information, see [Understand update behaviors of stack
 resources](using-cfn-updating-stacks-update-behaviors.md "using-cfn-updating-stacks-update-behaviors.md").


You can update custom resources that require a replacement of the underlying physical
 resource. When you update a custom resource in a CloudFormation template, CloudFormation sends
 an update request to that custom resource. If a custom resource requires a replacement,
 the new custom resource must send a response with the new physical ID. When CloudFormation
 receives the response, it compares the `PhysicalResourceId` between the old
 and new custom resources. If they're different, CloudFormation recognizes the update as a
 replacement and sends a delete request to the old resource, as shown in [Step 3: Stack deletion](#crpg-walkthrough-stack-deletion "#crpg-walkthrough-stack-deletion").


###### Note

If you didn't make changes to the custom resource, CloudFormation won't send requests
 to it during a stack update.



1. The template developer initiates an update to the stack that contains a custom
 resource. During an update, the template developer can specify new Properties in the
 stack template.


The following is an example of an `Update` to the stack template
 using a custom resource type:



```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Resources" : {
      "MySeleniumTest" : {
         "Type": "Custom::SeleniumTester",
         "Version" : "1.0",
         "Properties" : {
            "ServiceToken": "arn:aws:sns:us-west-2:123456789012:CRTest",
            "seleniumTester" : "SeleniumTest()",
            "endpoints" : [ "http://mysite.com", "http://myecommercesite.com/", "http://search.mysite.com",
               `"http://mynewsite.com"` ],
            "frequencyOfTestsPerHour" : [ "3", "2", "4", `"3"` ]
         }
      }
   },
   "Outputs" : {
      "topItem" : {
         "Value" : { "Fn::GetAtt" : ["MySeleniumTest", "resultsPage"] }
      },
      "numRespondents" : {
         "Value" : { "Fn::GetAtt" : ["MySeleniumTest", "lastUpdate"] }
      }
   }
}
```
2. CloudFormation sends an Amazon SNS notification to the resource provider with a
 `"RequestType" : "Update"` that contains similar information to the
 `Create` call, except that the `OldResourceProperties`
 field contains the old resource properties, and ResourceProperties contains the
 updated (if any) resource properties.


The following is an example of an `Update` request:



```
{
   "RequestType" : "Update",
   "ResponseURL" : "http://pre-signed-S3-url-for-response",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "uniqueid for this update request",
   "LogicalResourceId" : "MySeleniumTester",
   "ResourceType" : "Custom::SeleniumTester",  
   "PhysicalResourceId" : "Tester1",
   "ResourceProperties" : {
      "seleniumTester" : "SeleniumTest()",
      "endpoints" : [ "http://mysite.com", "http://myecommercesite.com/", "http://search.mysite.com",
         "http://mynewsite.com" ],
      "frequencyOfTestsPerHour" : [ "3", "2", "4", "3" ]
   },
   "OldResourceProperties" : {
      "seleniumTester" : "SeleniumTest()",
      "endpoints" : [ "http://mysite.com", "http://myecommercesite.com/", "http://search.mysite.com" ],
      "frequencyOfTestsPerHour" : [ "3", "2", "4" ]
   }
}
```

For detailed information about the request object for `Update`
 requests, see the [Update request for CloudFormation custom
 resources](crpg-ref-requesttypes-update.md "crpg-ref-requesttypes-update.md") topic.
3. The custom resource provider processes the data sent by CloudFormation. The custom resource
 performs the update and sends a response of either `SUCCESS` or
 `FAILED` to the S3 URL. CloudFormation then compares the
 `PhysicalResourceIDs` of old and new custom resources. If they're
 different, CloudFormation recognizes that the update requires a replacement and sends
 a delete request to the old resource. The following example demonstrates the
 custom resource provider response to an `Update` request.



```
{
   "Status" : "SUCCESS",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "uniqueid for this update request",
   "LogicalResourceId" : "MySeleniumTester",
   "PhysicalResourceId" : "Tester2"
}
```

For detailed information about the response object for `Update`
 requests, see the [Update request for CloudFormation custom
 resources](crpg-ref-requesttypes-update.md "crpg-ref-requesttypes-update.md") topic.


The `StackId`, `RequestId`, and
 `LogicalResourceId` fields must be copied verbatim from the request.
4. CloudFormation declares the stack status as `UPDATE_COMPLETE` or
 `UPDATE_FAILED`. If the update fails, the stack rolls back. If the
 stack was successfully updated, the template developer can access any new output values
 of the created custom resource with ``Fn::GetAtt``.

### Step 3: Stack deletion



1. The template developer deletes a stack that contains a custom resource. CloudFormation
 gets the current properties specified in the stack template along with the SNS
 topic, and prepares to make a request to the custom resource provider.
2. CloudFormation sends an Amazon SNS notification to the resource provider with a
 `"RequestType" : "Delete"` that contains current information about
 the stack, the custom resource properties from the stack template, and an S3 URL
 for the response.


Whenever you delete a stack or make an update that removes or replaces the
 custom resource, CloudFormation compares the `PhysicalResourceId` between
 the old and new custom resources. If they're different, CloudFormation recognizes the
 update as a replacement and sends a delete request for the old resource
 (`OldPhysicalResource`), as shown in the following example of a
 `Delete` request.



```
{
   "RequestType" : "Delete",
   "ResponseURL" : "http://pre-signed-S3-url-for-response",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "unique id for this delete request",
   "ResourceType" : "Custom::SeleniumTester",
   "LogicalResourceId" : "MySeleniumTester",
   "PhysicalResourceId" : "Tester1",
   "ResourceProperties" : {
      "seleniumTester" : "SeleniumTest()",
      "endpoints" : [ "http://mysite.com", "http://myecommercesite.com/", "http://search.mysite.com",
         "http://mynewsite.com" ],
      "frequencyOfTestsPerHour" : [ "3", "2", "4", "3" ]
   }
}
```

For detailed information about the request object for `Delete`
 requests, see the [Delete request for CloudFormation custom
 resources](crpg-ref-requesttypes-delete.md "crpg-ref-requesttypes-delete.md") topic.


`DescribeStackResource`, `DescribeStackResources`, and
 `ListStackResources` display the user-defined name if it has been
 specified.
3. The custom resource provider processes the data sent by CloudFormation and determines whether the
 `Delete` request was successful. The resource provider then uses the
 S3 URL sent by CloudFormation to send a response of either `SUCCESS` or
 `FAILED`. To successfully delete a stack with a custom resource, the
 custom resource provider must respond successfully to a delete request.


The following is an example of a custom resource provider response to a `Delete`
 request:



```
{
   "Status" : "SUCCESS",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "unique id for this delete request",
   "LogicalResourceId" : "MySeleniumTester",
   "PhysicalResourceId" : "Tester1"
}
```

For detailed information about the response object for `Delete`
 requests, see the [Delete request for CloudFormation custom
 resources](crpg-ref-requesttypes-delete.md "crpg-ref-requesttypes-delete.md") topic.


The `StackId`, `RequestId`, and
 `LogicalResourceId` fields must be copied verbatim from the request.
4. CloudFormation declares the stack status as `DELETE_COMPLETE` or
 `DELETE_FAILED`.
