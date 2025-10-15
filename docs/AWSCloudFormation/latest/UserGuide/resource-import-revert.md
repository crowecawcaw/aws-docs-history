# Reverting an import operation

To revert an import operation, specify a `Retain` deletion policy for the
 resource you want to remove from the template to ensure that it's preserved when you delete it
 from the stack.


## Revert an import operation using the
 AWS Management Console


1. Specify a `Retain`
[DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html") for the resources you want to remove from your stack. In
 the following example template, `GamesTable` is the target of this revert
 operation.


###### Example JSON


```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Import test",
    "Resources": {
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
        "GamesTable": {
            "Type": "AWS::DynamoDB::Table",
            **"DeletionPolicy": "Retain",**
            "Properties": {
                "TableName": "Games",
                "AttributeDefinitions": [
                    {
                        "AttributeName": "key",
                        "AttributeType": "S"
                    }
                ],
                "KeySchema": [
                    {
                        "AttributeName": "key",
                        "KeyType": "HASH"
                    }
                ],
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 1
                }
            }
        }
    }
}
```
2. Open the CloudFormation console to perform a stack update to apply the deletion
 policy.


	1. On the **Stacks** page, with the stack selected, choose
	 **Update**, and then choose **Update stack
	 (standard)**.
	2. Under **Prepare template**, choose **Replace
	 current template**.
	3. Under **Specify template**, provide the updated source
	 template with the `DeletionPolicy` attribute on
	 `GamesTable`, and then choose **Next**.
	
	
	
	
		* Choose **Amazon S3 URL**, and then specify the URL to
		 the updated source template in the text box.
		* Choose **Upload a template file**, and then browse
		 for the updated source template file.
	4. On the **Specify stack details** page, no changes are
	 required. Choose **Next**.
	5. On the **Configure stack options** page, no changes are
	 required. Choose **Next**.
	6. On the **Review `MyStack`** page,
	 review your changes. If your template contains IAM resources, select
	 **I acknowledge that this template may create IAM
	 resources** to specify that you want to use IAM resources in the
	 template. For more information, see
	 [Acknowledging IAM resources in CloudFormation
	 templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities").
	 Then, either update your source stack by creating a change set or update your
	 source stack directly.
3. Remove the resource, related parameters, and outputs from the stack template. In
 this example, the template now looks like the following.


###### Example JSON


```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Import test",
    "Resources": {
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
        }
    }
}
```
4. Repeat step 2 to delete the resource (`GamesTable`) and its related
 parameters and outputs from the stack.

## Revert an import operation using the
 AWS CLI


1. Specify a `Retain`
[DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html") for the resources you want to remove from your stack. In
 the following example template, `GamesTable` is the target of this revert
 operation.


###### Example JSON


```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Import test",
    "Resources": {
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
        "GamesTable": {
            "Type": "AWS::DynamoDB::Table",
            **"DeletionPolicy": "Retain",**
            "Properties": {
                "TableName": "Games",
                "AttributeDefinitions": [
                    {
                        "AttributeName": "key",
                        "AttributeType": "S"
                    }
                ],
                "KeySchema": [
                    {
                        "AttributeName": "key",
                        "KeyType": "HASH"
                    }
                ],
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 1
                }
            }
        }
    }
}
```
2. Update the stack to apply the deletion policy to the resource.



```
aws cloudformation update-stack --stack-name `MyStack`
```
3. Remove the resource, related parameters, and outputs from the stack template. In
 this example, the template now looks like the following.


###### Example JSON


```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Import test",
    "Resources": {
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
        }
    }
}
```
4. Update the stack to delete the resource (`GamesTable`) and its related
 parameters and outputs from the stack.



```
aws cloudformation update-stack --stack-name `MyStack`
```
