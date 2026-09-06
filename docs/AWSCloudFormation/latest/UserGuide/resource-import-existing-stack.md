

# Importing existing resources into a stack
<a name="resource-import-existing-stack"></a>

This topic shows you how to import existing AWS resources into an existing stack by describing them in a template. To instead scan for existing resources and automatically generate a template that you can use to import existing resources into CloudFormation or replicate resources in a new account, see [Generate templates from existing resources with IaC generator](generate-IaC.md).

**Prerequisites**

Before you begin, you must have the following:
+ A template that describes the entire stack, including both the resources that are already part of the stack and the resources to import. Save the template locally or in an Amazon S3 bucket. 

  **To get a copy of a running stack's template**

  1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation/](https://console.aws.amazon.com/cloudformation/).

  1. From the list of stacks, choose the stack you want to retrieve the template from.

  1. In the stack details pane, choose the **Template** tab, and then choose **Copy to clipboard**.

  1. Paste the code into a text editor to begin adding other resources to the template.
+ For each resource you want to import, include the following:
  + the properties and property values that define the resource's current configuration.
  + the unique identifier for the resource, such as the resource name. For more information, see [Resource identifiers](import-resources-manually.md#resource-import-identifiers-unique-ids).
  + the [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html).

**Topics**
+ [Example template](#resource-import-existing-stack-example-template)
+ [Import an existing resource into a stack using the AWS Management Console](#resource-import-existing-stack-console)
+ [Import an existing resource into a stack using the AWS CLI](#resource-import-existing-stack-cli)

## Example template
<a name="resource-import-existing-stack-example-template"></a>

In this walkthrough, we assume you're using the following example template, called `TemplateToImport.json`, that specifies two DynamoDB tables. `ServiceTable` is currently part of the stack, and `GamesTable` is the table you want to import.

**Note**  
This template is meant as an example only. To use it for your own testing purposes, replace the sample resources with resources from your account. 

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Import test",
    "Resources": {
        "ServiceTable": {
            "Type": "AWS::DynamoDB::Table",
            "Properties": {
                "TableName": "Service",
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

## Import an existing resource into a stack using the AWS Management Console
<a name="resource-import-existing-stack-console"></a>

**Note**  
The CloudFormation console doesn't support the use of the intrinsic function `Fn::Transform` when importing resources. You can use the AWS CLI to import resources that use the `Fn::Transform` function.

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the **Stacks** page, choose the stack you want to import resources into.

1. Choose **Stack actions**, and then choose **Import resources into stack**.  
![The Import resources into stack option in the console.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/stack-actions-import.png)

1. Review the **Import overview** page, and then choose **Next**.

1. On the **Specify template** page, provide your updated template using one of the following methods, and then choose **Next**.
   + Choose **Amazon S3 URL**, and then specify the URL for your template in the text box.
   + Choose **Upload a template file**, and then browse for your template.

1. On the **Identify resources** page, identify each target resource. For more information, see [Resource identifiers](import-resources-manually.md#resource-import-identifiers-unique-ids).

   1. Under **Identifier property**, choose the type of resource identifier. For example, the `AWS::DynamoDB::Table` resource can be identified using the `TableName` property.

   1. Under **Identifier value**, type the actual property value. For example, the `TableName` for the `GamesTable` resource in the example template is `{{Games}}`.

   1. Choose **Next**.

1. On the **Specify stack details** page, update any parameters, and then choose **Next**. This automatically creates a change set.
**Note**  
The import operation fails if you modify existing parameters that initiate a create, update, or delete operation.

1. On the **Review {{stack-name}}** page, review the resources to import, and then choose **Import resources**. This automatically executes the change set created in the last step. Any stack-level tags are applied to imported resources at this time. For more information, see [Configure stack options](cfn-console-create-stack.md#configure-stack-options).

   The **Events** page for the stack displays.  
![The Events tab in the console.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/import-events.png)

1. (Optional) Run drift detection on the stack to make sure the template and actual configuration of the imported resources match. For more information about detecting drift, see [Detect drift on an entire CloudFormation stack](detect-drift-stack.md).

1. (Optional) If your imported resources don't match their expected template configurations, either correct the template configurations or update the resources directly. For more information about importing drifted resources, see [Resolve drift with an import operation](resource-import-resolve-drift.md).

## Import an existing resource into a stack using the AWS CLI
<a name="resource-import-existing-stack-cli"></a>

1. To learn which properties identify each resource type in the template, run the **get-template-summary** command, specifying the S3 URL of the template. For example, the `AWS::DynamoDB::Table` resource can be identified using the `TableName` property. For the `GamesTable` resource in the example template, the value of `TableName` is `Games`. You'll need this information in the next step.

   ```
   aws cloudformation get-template-summary \
       --template-url {{https://amzn-s3-demo-bucket.s3.us-west-2.amazonaws.com/TemplateToImport.json}}
   ```

   For more information, see [Resource identifiers](import-resources-manually.md#resource-import-identifiers-unique-ids).

1. Compose a list of actual resources to import and their unique identifiers in the following JSON string format.

   ```
   [{"ResourceType":"AWS::DynamoDB::Table","LogicalResourceId":"GamesTable","ResourceIdentifier":{"TableName":"Games"}}]
   ```

   Alternatively, you can specify the JSON-formatted parameters in a configuration file. 

   For example, to import `GamesTable` , you might create a {{ResourcesToImport.txt}} file that contains the following configuration.

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

1. To create a change set, use the following **create-change-set** command and replace the placeholder text. For the `--change-set-type` option, specify a value of **IMPORT**. For the `--resources-to-import` option, replace the sample JSON string with the actual JSON string you just created.

   ```
   aws cloudformation create-change-set \
       --stack-name {{TargetStack}} --change-set-name {{ImportChangeSet}} \
       --change-set-type IMPORT \
       --template-url {{https://amzn-s3-demo-bucket.s3.us-west-2.amazonaws.com/TemplateToImport.json}} \
       --resources-to-import {{'[{"ResourceType":"AWS::DynamoDB::Table","LogicalResourceId":"GamesTable","ResourceIdentifier":{"TableName":"Games"}}]'}}
   ```
**Note**  
`--resources-to-import` doesn't support inline YAML. The requirements for escaping quotes in the JSON string vary depending on your terminal. For more information, see [Using quotation marks inside strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html#cli-usage-parameters-quoting-strings-containing) in the *AWS Command Line Interface User Guide*.

   Alternatively, you can use a file URL as input for the `--resources-to-import` option, as shown in the following example.

   ```
   --resources-to-import {{file://ResourcesToImport.txt}}
   ```

1. Review the change set to make sure the correct resources will be imported.

   ```
   aws cloudformation describe-change-set \
       --change-set-name {{ImportChangeSet}} --stack-name {{TargetStack}}
   ```

1. To initiate the change set and import the resources, use the following **execute-change-set** command and replace the placeholder text. Any stack-level tags are applied to imported resources at this time. For more information, see [Configure stack options](cfn-console-create-stack.md#configure-stack-options). On successful completion of the operation `(IMPORT_COMPLETE)`, the resources are successfully imported.

   ```
   aws cloudformation execute-change-set \
       --change-set-name {{ImportChangeSet}} --stack-name {{TargetStack}}
   ```

1. (Optional) Run drift detection on the `IMPORT_COMPLETE` stack to make sure the template and actual configuration of the imported resources match. For more information about detecting drift, see [Detect drift on an entire CloudFormation stack](detect-drift-stack.md).

   1. Run drift detection on the specified stack.

      ```
      aws cloudformation detect-stack-drift --stack-name {{TargetStack}}
      ```

      If successful, this command returns the following sample output.

      ```
      { "Stack-Drift-Detection-Id" : "624af370-311a-11e8-b6b7-500cexample" }
      ```

   1. View the progress of a drift detection operation for the specified stack drift detection ID.

      ```
      aws cloudformation describe-stack-drift-detection-status \
          --stack-drift-detection-id {{624af370-311a-11e8-b6b7-500cexample}}
      ```

   1. View drift information for the resources that have been checked for drift in the specified stack.

      ```
      aws cloudformation describe-stack-resource-drifts --stack-name {{TargetStack}}
      ```

1. (Optional) If your imported resources don't match their expected template configurations, either correct the template configurations or update the resources directly. For more information about importing drifted resources, see [Resolve drift with an import operation](resource-import-resolve-drift.md).