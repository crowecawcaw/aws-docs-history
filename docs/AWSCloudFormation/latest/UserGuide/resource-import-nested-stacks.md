# Nesting an existing stack

Use the `resource import` feature to nest an existing stack within another
 existing stack. Nested stacks are common components that you declare and reference from within
 other templates. That way, you can avoid copying and pasting the same configurations into your
 templates and simplify stack updates. If you have a template for a common component, you can
 use the `AWS::CloudFormation::Stack` resource to reference this template from
 within another template. For more information on nested stacks, see [Split a template into reusable pieces using nested
 stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md").

AWS CloudFormation only supports one level of nesting using `resource import`. This means
 that you can't import a stack into a child stack or import a stack that has children.

If you're new to importing, we recommend that you first review the introductory information
 in the [Import AWS resources into a CloudFormation stack
 manually](import-resources-manually.md "import-resources-manually.md") topic.


## Nested stack import
 validation


During a nested stack import operation, AWS CloudFormation performs the following validations.



* The nested `AWS::CloudFormation::Stack` definition in the parent stack
 template matches the actual nested stack's template.
* The tags for the nested `AWS::CloudFormation::Stack` definition in the
 parent stack template match the tags for the actual nested stack resource.

## Nest an existing stack using the
 AWS Management Console


1. Add the `AWS::CloudFormation::Stack` resource to the parent stack
 template with a `Retain`
[DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html"). In the following example parent stack template,
 `MyNestedStack` is the target of the import.


**JSON**



```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Resources" : {
    "ServiceTable":{
           "Type":"AWS::DynamoDB::Table",
           "Properties":{
              "TableName":"Service",
              "AttributeDefinitions":[
                 {
                    "AttributeName":"key",
                    "AttributeType":"S"
                 }
              ],
              "KeySchema":[
                 {
                    "AttributeName":"key",
                    "KeyType":"HASH"
                 }
              ],
              "ProvisionedThroughput":{
                 "ReadCapacityUnits":5,
                 "WriteCapacityUnits":1
              }
           }
        },
    "MyNestedStack" : {
      "Type" : "AWS::CloudFormation::Stack",
      "DeletionPolicy": "Retain",
      "Properties" : {
      "TemplateURL" : "`https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template`",
        `"Parameters" : {
 "InstanceType" : "t1.micro",
 "KeyName" : "mykey"`
        }
      }
    }
  }
}
```

**YAML**



```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ServiceTable:
    Type: 'AWS::DynamoDB::Table'
    Properties:
      TableName: Service
      AttributeDefinitions:
        - AttributeName: key
          AttributeType: S
      KeySchema:
        - AttributeName: key
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 1
  MyNestedStack:
    Type: 'AWS::CloudFormation::Stack'
    DeletionPolicy: Retain
    Properties:
      TemplateURL: >-
        `https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template`
      `Parameters:
 InstanceType: t1.micro
 KeyName: mykey`
```
2. Open the AWS CloudFormation console.
3. On the **Stacks** page, with the parent stack selected, choose
 **Stack actions**, and then choose **Import resources
 into stack**.



![The Import resources into stack option in the console.](images/stack-actions-import.png)
4. Read the **Import overview** page for a list of things you're
 required to provide during this operation. Then, choose
 **Next**.
5. On the **Specify template** page, provide the updated parent
 template using one of the following methods, and then choose
 **Next**.




	* Choose **Amazon S3 URL**, and then specify the URL for your
	 template in the text box.
	* Choose **Upload a template file**, and then browse for your
	 template.
6. On the **Identify resources** page, identify the
 `AWS::CloudFormation::Stack` resource.


	1. Under **Identifier property**, choose the type of resource
	 identifier. For example, an `AWS::CloudFormation::Stack` resource
	 can be identified using the `StackId` property.
	2. Under **Identifier value**, type the ARN of the stack
	 you're importing. For example,
	 ``arn:aws:cloudformation:us-west-2:12345678910:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10``.
	
	
	
	![The Identify resources page in the console.](images/resource-import-stackid.png)
	3. Choose **Next**.
7. On the **Specify stack details** page, modify any parameters, and
 then choose **Next**. This automatically creates a change
 set.


###### Important

The import operation fails if you modify existing parameters that initiate a
 create, update, or delete operation.
8. On the **Review `MyParentStack`** page,
 confirm that the correct resource is being imported, and then choose **Import
 resources**. This automatically executes the change set created in the
 last step. Any stack-level tags are applied to imported resources at this
 time.
9. The **Events** pane of the **Stack details**
 page for your parent stack displays.



![The Events tab in the console.](images/import-events.png)

###### Note

It's not necessary to run drift detection on the parent stack after this import
 operation because the `AWS::CloudFormation::Stack` resource was already
 managed by AWS CloudFormation.

## Nest an existing stack using the
 AWS CLI


1. Add the `AWS::CloudFormation::Stack` resource to the parent stack
 template with a `Retain`
[DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html"). In the following example parent template,
 `MyNestedStack` is the target of the import.


**JSON**



```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Resources" : {
    "ServiceTable":{
           "Type":"AWS::DynamoDB::Table",
           "Properties":{
              "TableName":"Service",
              "AttributeDefinitions":[
                 {
                    "AttributeName":"key",
                    "AttributeType":"S"
                 }
              ],
              "KeySchema":[
                 {
                    "AttributeName":"key",
                    "KeyType":"HASH"
                 }
              ],
              "ProvisionedThroughput":{
                 "ReadCapacityUnits":5,
                 "WriteCapacityUnits":1
              }
           }
        },
    "`MyNestedStack`" : {
      "Type" : "AWS::CloudFormation::Stack",
      "DeletionPolicy": "Retain",
      "Properties" : {
      "TemplateURL" : "`https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template`",
        `"Parameters" : {
 "InstanceType" : "t1.micro",
 "KeyName" : "mykey"`
        }
      }
    }
  }
}
```

**YAML**



```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ServiceTable:
    Type: 'AWS::DynamoDB::Table'
    Properties:
      TableName: Service
      AttributeDefinitions:
        - AttributeName: key
          AttributeType: S
      KeySchema:
        - AttributeName: key
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 1
  `MyNestedStack`:
    Type: 'AWS::CloudFormation::Stack'
    DeletionPolicy: Retain
    Properties:
      TemplateURL: >-
        `https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template`
      `Parameters:
 InstanceType: t1.micro
 KeyName: mykey`
```
2. Compose a JSON string as shown in the following example, with these modifications: 




	* Replace `MyNestedStack` with the logical ID of the
	 target resource as specified in the template.
	* Replace
	 `arn:aws:cloudformation:us-west-2:12345678910:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10`
	 with the ARN of the stack you want to import.

```
[{"ResourceType":"AWS::CloudFormation::Stack","LogicalResourceId":"`MyNestedStack`","ResourceIdentifier":{"StackId":"`arn:aws:cloudformation:us-east-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10`"}}]
```

Alternatively, you can specify the parameters in a configuration file. 


For example, to import `MyNestedStack`, you might create a
 `ResourcesToImport.txt` file that contains the following
 configuration.


**JSON**



```
[
  {
      "ResourceType":"AWS::CloudFormation::Stack",
      "LogicalResourceId":"`MyNestedStack`",
      "ResourceIdentifier": {
        "StackId":"`arn:aws:cloudformation:us-west-2:12345678910:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10`"
      }
  }
]
```

**YAML**



```
ResourceType: 'AWS::CloudFormation::Stack'
  LogicalResourceId: `MyNestedStack`
  ResourceIdentifier:
    StackId: >-
      `arn:aws:cloudformation:us-west-2:12345678910:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10`
```
3. To create a change set, use the following **create-change-set**
 command and replace the placeholder text. For the `--change-set-type`
 option, specify a value of `IMPORT`. For the
 `--resources-to-import` option, replace the sample JSON string with the
 actual JSON string you just created.



```
aws cloudformation create-change-set \
    --stack-name `MyParentStack` --change-set-name `ImportChangeSet` \
    --change-set-type `IMPORT` \
    --template-body `file://TemplateToImport.json` \
    --resources-to-import `'[{"ResourceType":"AWS::CloudFormation::Stack","LogicalResourceId":"MyNestedStack","ResourceIdentifier":{"StackId":"arn:aws:cloudformation:us-west-2:12345678910:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10"}}]'`
```

###### Note

`--resources-to-import` doesn't support inline YAML. The
 requirements for escaping quotes in the JSON string vary depending on your
 terminal. For more information, see [Using quotation marks inside strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html#cli-usage-parameters-quoting-strings-containing "https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html#cli-usage-parameters-quoting-strings-containing") in the
 *AWS Command Line Interface User Guide*.


Alternatively, you can use a file URL as input for the
 `--resources-to-import` option, as shown in the following
 example.



```
--resources-to-import `file://ResourcesToImport.txt`
```

If successful, this command returns the following sample output.



```
{
    "Id": "arn:aws:cloudformation:us-west-2:12345678910:changeSet/ImportChangeSet/8ad75b3f-665f-46f6-a200-0b4727a9442e",
    "StackId": "arn:aws:cloudformation:us-west-2:12345678910:stack/MyParentStack/4e345b70-1281-11ef-b027-027366d8e82b"
}
```
4. Review the change set to make sure the correct stack is being imported.



```
aws cloudformation describe-change-set --change-set-name `ImportChangeSet`
```
5. To initiate the change set and import the stack into the source parent stack, use
 the following **execute-change-set** command and replace the
 placeholder text. Any [stack-level tags](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options")
 are applied to imported resources at this time. On successful completion of the
 import operation `(IMPORT_COMPLETE)`, the stack is successfully
 nested.



```
aws cloudformation execute-change-set --change-set-name `ImportChangeSet`
```

###### Note

It's not necessary to run drift detection on the parent stack after this import
 operation because the `AWS::CloudFormation::Stack` resource is already
 managed by AWS CloudFormation.
