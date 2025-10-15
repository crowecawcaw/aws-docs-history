# Moving resources between stacks

Using the `resource import` feature, you can move resources between, or
 *refactor*, stacks. You need to first add a `Retain`
 deletion policy to the resource you want to move to ensure that the resource is preserved
 when you remove it from the source stack and import it to the target stack.

If you're new to importing, we recommend that you first review the introductory
 information in the [Import AWS resources into a CloudFormation stack](import-resources.md "import-resources.md")
 topic.

###### Important

Not all resources support import operations. See [Resources that support import
 operations](resource-import-supported-resources.md "resource-import-supported-resources.md") before you remove a resource from your stack. If you remove a
 resource that doesn't support import operations from your stack, you can't import the
 resource into another stack or bring it back into the source stack.


## Refactor a stack using the AWS Management Console


1. In the source template, specify a `Retain`
[DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html") for the resource you want to move.


In the following example source template, `Games` is the target of
 this refactor.


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
            "DeletionPolicy": "Retain",
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


	1. On the **Stacks** page, with the stack selected,
	 choose **Update**.
	2. Under **Prepare template**, choose **Replace
	 current template**.
	3. Under **Specify template**, provide the updated
	 source template with the `DeletionPolicy` attribute on
	 `GamesTable`, and then choose
	 **Next**.
	
	
	
	
		* Choose **Amazon S3 URL**, and then specify
		 the URL to the updated source template in the text box.
		* Choose **Upload a template file**, and then
		 browse for the updated source template file.
	4. On the **Specify stack details** page, no changes are
	 required. Choose **Next**.
	5. On the **Configure stack options** page, no changes
	 are required. Choose **Next**.
	6. On the **Review
	 `SourceStackName`** page, review
	 your changes. If your template contains IAM resources, select
	 **I acknowledge that this template may create IAM
	 resources** to specify that you want to use IAM resources
	 in the template. For more information about using IAM resources in
	 templates, see [Control CloudFormation access with AWS Identity and Access Management](control-access-with-iam.md "control-access-with-iam.md"). Then, either update your
	 source stack by creating a change set or update your source stack
	 directly.
3. Remove the resource, related parameters, and outputs from the source template,
 and then add them to the target template.


The source template now looks like the following.


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

The following example target template currently has the
 `PlayersTable` resource, and now also contains
 `GamesTable`.


###### Example JSON


```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Import test",
    "Resources": {
        "PlayersTable": {
            "Type": "AWS::DynamoDB::Table",
            "Properties": {
                "TableName": "Players",
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
        },
        "GamesTable": {
            "Type": "AWS::DynamoDB::Table",
            "DeletionPolicy": "Retain",
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
4. Repeat steps 2 – 3 to update the source stack again, this time to
 delete the target resource from the stack.
5. Perform an import operation to add `GamesTable` to the target
 stack.


	1. On the **Stacks** page, with the parent stack
	 selected, choose **Stack actions**, and then choose
	 **Import resources into stack**.
	
	
	
	![The Import resources into stack option in the console.](/images/AWSCloudFormation/latest/UserGuide/images/stack-actions-import.png)
	2. Read the **Import overview** page for a list of
	 things you're required to provide during this operation. Then, choose
	 **Next**.
	3. On the **Specify template** page, complete one of the
	 following, and then choose **Next**.
	
	
	
	
		* Choose **Amazon S3 URL**, and then specify a
		 URL in the text box.
		* Choose **Upload a template file**, and then
		 browse for a file to upload.
	4. On the **Identify resources** page, identify the
	 resource you're moving (in this example, `GamesTable`). For
	 more information, see [Resource identifiers](import-resources-manually.md#resource-import-identifiers-unique-ids "import-resources-manually.md#resource-import-identifiers-unique-ids").
	
	
	
	
		1. Under **Identifier property**, choose the
		 type of resource identifier. For example, an
		 `AWS::DynamoDB::Table` resource can be identified
		 using the `TableName` property.
		2. Under **Identifier value**, type the actual
		 property value. For example,
		 ``GamesTables``.
		3. Choose **Next**.
	5. On the **Specify stack details** page, modify any
	 parameters, and then choose **Next**. This
	 automatically creates a change set.
	
	
	###### Important
	
	The import operation fails if you modify existing parameters that
	 initiate a create, update, or delete operation.
	6. On the **Review
	 `TargetStackName`** page, confirm
	 that the correct resource is being imported, and then choose
	 **Import resources**. This automatically initiates
	 the change set created in the last step. Any [stack-level tags](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options") are
	 applied to imported resources at this time.
	7. The **Events** pane of the **Stack
	 details** page for your parent stack displays.
	
	
	
	![The Events tab in the console.](../../../images/AWSCloudFormation/latest/UserGuide/images/import-events.png)
	
	###### Note
	
	It's not necessary to run drift detection on the parent stack
	 after this import operation because the
	 `AWS::CloudFormation::Stack` resource is already
	 managed by CloudFormation.

## Refactor a stack using the AWS CLI


1. In the source template, specify a `Retain`
[DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html") for the resource you want to move.


In the following example source template, `GamesTable` is the
 target of this refactor.


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
            "DeletionPolicy": "Retain",
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
2. Update the source stack to apply the deletion policy to the resource.



```
aws cloudformation update-stack --stack-name `SourceStackName`
```
3. Remove the resource, related parameters, and outputs from the source template,
 and then add them to the target template.


The source template now looks like the following.


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

The following example target template currently has the
 `PlayersTable` resource, and now also contains
 `GamesTable`.


###### Example JSON


```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Import test",
    "Resources": {
        "PlayersTable": {
            "Type": "AWS::DynamoDB::Table",
            "Properties": {
                "TableName": "Players",
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
        },
        "GamesTable": {
            "Type": "AWS::DynamoDB::Table",
            "DeletionPolicy": "Retain",
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
4. Update the source stack to delete the `GamesTable` resource and its
 related parameters and outputs from the stack.



```
aws cloudformation update-stack --stack-name `SourceStackName`
```
5. Compose a list of actual resources to import and their unique identifiers in
 the following JSON string format. For more information, see [Resource identifiers](import-resources-manually.md#resource-import-identifiers-unique-ids "import-resources-manually.md#resource-import-identifiers-unique-ids").



```
[{"ResourceType":"AWS::DynamoDB::Table","LogicalResourceId":"GamesTable","ResourceIdentifier":{"TableName":"Games"}}]
```

Alternatively, you can specify the JSON-formatted parameters in a
 configuration file. 


For example, to import `GamesTable`, you might create a
 `ResourcesToImport.txt` file that contains the
 following configuration.



```
[
  {
      "ResourceType":"AWS::DynamoDB::Table",
      "LogicalResourceId":"GamesTable",
      "ResourceIdentifier": {
        "TableName":"Games"
      }
  }
]
```
6. To create a change set, use the following **create-change-set**
 command and replace the placeholder text. For the `--change-set-type`
 option, specify a value of `IMPORT`. For the
 `--resources-to-import` option, replace the sample JSON string
 with the actual JSON string you just created.



```
aws cloudformation create-change-set \
    --stack-name `TargetStackName` --change-set-name `ImportChangeSet` \
    --change-set-type `IMPORT` \
    --template-body `file://TemplateToImport.json` \
    --resources-to-import "`'[{"ResourceType":"AWS::DynamoDB::Table","LogicalResourceId":"GamesTable","ResourceIdentifier":{"TableName":"Games"}}]'`"
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
7. Review the change set to make sure the correct resource is being imported into
 the target stack.



```
aws cloudformation describe-change-set \
    --change-set-name `ImportChangeSet`
```
8. To initiate the change set and import the resource, use the following
 **execute-change-set** command and replace the placeholder
 text. Any stack-level tags are applied to imported resources at this time. On
 successful completion of the operation `(IMPORT_COMPLETE)`, the
 resource is successfully imported.



```
aws cloudformation execute-change-set \
    --change-set-name `ImportChangeSet` --stack-name `TargetStackName`
```

###### Note

It's not necessary to run drift detection on the target stack after this
 import operation because the resource is already managed by
 CloudFormation.
