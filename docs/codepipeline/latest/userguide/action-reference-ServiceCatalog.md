

# AWS Service Catalog deploy action reference
<a name="action-reference-ServiceCatalog"></a>

You use an AWS Service Catalog action to deploy templates using your pipeline. These are resource templates that you have created in Service Catalog.

## Action type
<a name="action-reference-ServiceCatalog-type"></a>
+ Category: `Deploy`
+ Owner: `AWS`
+ Provider: `ServiceCatalog`
+ Version: `1`

## Configuration parameters
<a name="action-reference-ServiceCatalog-config"></a>

**TemplateFilePath**  
Required: Yes  
The file path for your resource template in your source location.

**ProductVersionName**  
Required: Yes  
The product version in Service Catalog.

**ProductType**  
Required: Yes  
The product type in Service Catalog.

**ProductId**  
Required: Yes  
The product ID in Service Catalog.

**ProductVersionDescription**  
Required: No  
The product version description in Service Catalog.

## Input artifacts
<a name="action-reference-ServiceCatalog-input"></a>
+ **Number of artifacts:** `1`
+ **Description:** This is the input artifact for your action.

## Output artifacts
<a name="action-reference-ServiceCatalog-output"></a>
+ **Number of artifacts:** `0` 
+ **Description:** Output artifacts do not apply for this action type.

## Service role permissions: Service Catalog action
<a name="edit-role-servicecatalog"></a>

For Service Catalog support, add the following to your policy statement:

```
{
    "Effect": "Allow",
    "Action": [
        "servicecatalog:ListProvisioningArtifacts",
        "servicecatalog:CreateProvisioningArtifact",
        "servicecatalog:DescribeProvisioningArtifact",
        "servicecatalog:DeleteProvisioningArtifact",
        "servicecatalog:UpdateProduct"
    ],
    "Resource": "{{resource_ARN}}"
},
{
    "Effect": "Allow",
    "Action": [
        "cloudformation:ValidateTemplate"
    ],
    "Resource": "{{resource_ARN}}"
}
```

## Example action configurations by type of configuration file
<a name="action-reference-ServiceCatalog-example"></a>

The following example shows a valid configuration for a deploy action that uses Service Catalog, for a pipeline that was created in the console without a separate configuration file:

```
"configuration": {
  "TemplateFilePath": "S3_template.json",
  "ProductVersionName": "devops S3 v2",
  "ProductType": "CLOUD_FORMATION_TEMPLATE",
  "ProductVersionDescription": "{{Product version description}}",
  "ProductId": "prod-example123456"
}
```

The following example shows a valid configuration for a deploy action that uses Service Catalog, for a pipeline that was created in the console with a separate `sample_config.json` configuration file:

```
"configuration": {
  "ConfigurationFilePath": "sample_config.json",
  "ProductId": "prod-example123456"
}
```

### Example action configuration
<a name="action-reference-ServiceCatalog-example-default"></a>

------
#### [ YAML ]

```
Name: ActionName
ActionTypeId:
  Category: Deploy
  Owner: AWS
  Version: 1
  Provider: ServiceCatalog
OutputArtifacts:
- Name: myOutputArtifact
Configuration:
  TemplateFilePath: S3_template.json
  ProductVersionName: devops S3 v2
  ProductType: CLOUD_FORMATION_TEMPLATE
  ProductVersionDescription: {{Product version description}}
  ProductId: prod-example123456
```

------
#### [ JSON ]

```
{
    "Name": "ActionName",
    "ActionTypeId": {
        "Category": "Deploy",
        "Owner": "AWS",
        "Version": 1,
        "Provider": "ServiceCatalog"
    },
    "OutputArtifacts": [
        {
            "Name": "myOutputArtifact"
        }
    ],
    "Configuration": {
        "TemplateFilePath": "S3_template.json",
        "ProductVersionName": "devops S3 v2",
        "ProductType": "CLOUD_FORMATION_TEMPLATE",
        "ProductVersionDescription": "{{Product version description}}",
        "ProductId": "prod-example123456"
    }
}
```

------

## See also
<a name="action-reference-ServiceCatalog-links"></a>

The following related resources can help you as you work with this action.
+ [Service Catalog User Guide](https://docs.aws.amazon.com/servicecatalog/latest/userguide/) – For information about resources and templates in Service Catalog, see the *Service Catalog User Guide*.
+ [Tutorial: Create a pipeline that deploys to Service Catalog](tutorials-S3-servicecatalog.md) – This tutorial shows you how to create and configure a pipeline to deploy your product template to Service Catalog and deliver changes you have made in your source repository.