# Connecting Amazon Q Business to Google Drive

using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _CloudFormation User Guide_.

###### Topics

- [Google Drive New CloudFormation template](#googledrive-v2-cfn-template "#googledrive-v2-cfn-template")

## Google Drive New CloudFormation template

The following is the Google Drive New CloudFormation template. Copy and save this template to a file on your local drive.

For more information about CloudFormation templates, see [Working with CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") in the _CloudFormation User Guide_.

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Template to connect Google Drive New to Amazon Q Business",
  "Parameters": {
    "ApplicationId": {
      "Type": "String",
      "Description": "Amazon Q Business Application ID"
    },
    "IndexId": {
      "Type": "String",
      "Description": "Amazon Q Business Index ID"
    },
    "DataSourceName": {
      "Type": "String",
      "Description": "Name for the Google Drive data source"
    },
    "RoleArn": {
      "Type": "String",
      "Description": "IAM Role ARN for the data source"
    },
    "SecretArn": {
      "Type": "String",
      "Description": "AWS Secrets Manager ARN containing Google Drive credentials"
    }
  },
  "Resources": {
    "GoogleDriveV3DataSource": {
      "Type": "AWS::QBusiness::DataSource",
      "Properties": {
        "ApplicationId": {"Ref": "ApplicationId"},
        "IndexId": {"Ref": "IndexId"},
        "DisplayName": {"Ref": "DataSourceName"},
        "RoleArn": {"Ref": "RoleArn"},
        "Configuration": {
          "type": "GOOGLEDRIVEV3",
          "connectionConfiguration": {
            "secretArn": {"Ref": "SecretArn"},
            "authType": "SERVICE_ACCOUNT"
          },
          "dataEntityConfiguration": {
            "crawlMyDrive": true,
            "crawlSharedWithMe": true,
            "crawlSharedDrives": false
          },
          "accessControlConfiguration": {
            "crawlAcl": true
          },
          "filterConfiguration": {
            "maxFileSizeInMegaBytes": "50"
          },
          "crawlIdentities": false,
          "deletionProtectionConfiguration": {
            "enableDeletionProtection": true,
            "deletionProtectionThreshold": "15"
          }
        }
      }
    }
  }
}
```

[Show moreShow less](# "#")
