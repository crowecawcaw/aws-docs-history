# Create an Amazon SageMaker Unified Studio data source for

Amazon SageMaker AI in the project catalog

In the current release of Amazon SageMaker Unified Studio, creating an Amazon Sagemaker AI data source is
not supported via the UI and can only be done by envoking API or CLI actions.

In order to create a data source for Amazon SageMaker AI in Amazon SageMaker Unified Studio, you must first
to create a RAM share between Amazon SageMaker and Amazon DataZone. This RAM share is
necessary for Amazon SageMaker to successfully make Amazon DataZone API calls which are
needed for various membership and security checks.

If you're using the Amazon DataZone domain, you can complete this step by [adding Amazon SageMaker as a trusted service in your Amazon DataZone
domain](../../../datazone/latest/userguide/add-sagemaker-as-trusted-service-associate.md "../../../datazone/latest/userguide/add-sagemaker-as-trusted-service-associate.md").

If you're using a Amazon SageMaker unified domain, you can do this by completing the
following procedure:

1. Navigate to the RAM console at [https://us-east-1.console.aws.amazon.com/ram/home](https://us-east-1.console.aws.amazon.com/ram/home "https://us-east-1.console.aws.amazon.com/ram/home").
2. Choose **Create resource share**.
3. For resource share name enter a unique name. For example
   `DataZone-<DataZone DomainId>-SageMaker`.
4. Under **Resources** choose **DataZone
   Domains** from the drop down and then select the Amazon DataZone
   domain from the list and then choose **Next**.
5. From the Managed Permissions dropdown, choose
   **AWSRAMSageMakerServicePrincipalPermissionAmazonDataZoneDomain**
   and then choose **Next**.
6. Under **Principals** from the **Select principal
   type** dropdown, choose **Service
   principal**.
7. Enter `sagemaker.amazonaws.com` for the service principal name and
   choose **Add** and then choose
   **Next**.
8. Choose **Create resource share**.
   Once this is completed, you can invoke the `CreateDataSource` API action or
   the `create-data-source` CLI action to create a new data source for Amazon
   SageMaker AI in Amazon SageMaker Unified Studio.

```

aws datazone create-data-source --cli-input-json file://create-sagemaker-datasource-example.json

```

Sample payload (create-sagemaker-datasource-example.json per example above) to create
an Amazon Sagemaker data sources in an Amazon DataZone domain:

```

{
  "name": "my-data-source",
  "projectIdentifier": "project123",
  "type": "SAGEMAKER",
  "description": "Description of the datasource",
  "environmentIdentifier": "environment123",
  "configuration": {
    "sageMakerRunConfiguration": {
        "trackingAssets": {
            "SageMakerModelPackageGroupAssetType": [
                "arn:aws:sagemaker:us-east-1:123456789012:model-package-group/my-model-package-group",
            ],
            "SageMakerFeatureGroupAssetType": [
                "arn:aws:sagemaker:us-east-1:123456789012:feature-group/my-feature-group",
            ]
        }
    }
  },
  "recommendation": {
    "enableBusinessNameGeneration": "True"
  },
  "enableSetting": "ENABLED",
  "schedule": {
    "timezone": "UTC",
    "schedule": "cron(7 22 * * ? *)"
  },
  "publishOnImport": "True",
  "assetFormsInput": [
    {
      "formName": "AssetCommonDetailsForm"
      "typeIdentifier": "amazon.datazone.AssetCommonDetailsFormType",
      "typeRevision": "3",
      "content": "form-content"
    }
  ],
  "clientToken": "123456"
}

```

Sample payload (create-sagemaker-datasource-example.json per example above) to create
an Amazon Sagemaker data sources in an Amazon SageMaker unified domain:

```

{
  "name": "my-data-source",
  "projectIdentifier": "project123",
  "type": "SAGEMAKER",
  "description": "Description of the datasource",
  "connectionIdentifier": "connection123",
  "configuration": {
    "sageMakerRunConfiguration": {
        "trackingAssets": {
            "SageMakerModelPackageGroupAssetType": [
                "arn:aws:sagemaker:us-east-1:123456789012:model-package-group/my-model-package-group",
            ],
        }
    }
  },
  "recommendation": {
    "enableBusinessNameGeneration": "True"
  },
  "enableSetting": "ENABLED",
  "schedule": {
    "timezone": "UTC",
    "schedule": "cron(7 22 * * ? *)"
  },
  "publishOnImport": "True",
  "assetFormsInput": [
    {
      "formName": "AssetCommonDetailsForm"
      "typeIdentifier": "amazon.datazone.AssetCommonDetailsFormType",
      "typeRevision": "3",
      "content": "form-content"
    }
  ],
  "clientToken": "123456"
}

```
