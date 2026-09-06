

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Add a new version
<a name="ml-add-version"></a>

You can use the Catalog API or the AWS Marketplace Management Portal to add a new version to a machine learning product. For more information about using the portal, refer to [Adding a new version](https://docs.aws.amazon.com/marketplace/latest/userguide/machine-learning-products.html) in the *AWS Marketplace Seller Guide*. 

**Note**  
For ML products, a version consists of a single delivery option, which represents the product you're making available. In the Catalog API, working with delivery options for ML products effectively modifies versions of your product.   
When adding new instance types, include an `UpdatePricingTerms` change type in your change set to specify pricing for new instance types. For new products, `UpdatePricingTerms` must cover all supported instance types. `UpdatePricingDimensions` is not required or supported for ML products, because dimensions are automatically generated for all supported instance types. For more information, refer to [Update pricing dimensions](work-with-seller-products.md#update-dimensions).

**Using `StartChangeSet` to add a version**

 To add a new version, call the `StartChangeSet` operation with the `AddDeliveryOptions` change type: 

1.  To validate your API call without creating a version, set `Intent` to `VALIDATE`. 

1.  For actual version creation, set `Intent` to `APPLY`. 

## Request syntax
<a name="request-syntax"></a>

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json
{
    "Catalog": "AWSMarketplace",
    "ChangeSet": [{
        "ChangeType": "AddDeliveryOptions",
        "Entity": {
            "Identifier": "example1-abcd-1234-5ef6-7890abcdef12@1",
            "Type": "MachineLearningProduct@1.0"
        },
        "DetailsDocument": {
            "Version": {
                "VersionTitle": "version 1.1",
                "ReleaseNotes": "Patch update for small bugfix in version 1.0"
            },
            "DeliveryOptions": [{
                "Details": {
                    "SageMakerAlgorithmDeliveryOptionDetails": {
                       "SageMakerAlgorithmArn": "arn:aws:sagemaker:us-east-2:605142612156:algorithm/scikit-decision-trees-1552343220",
                       "AccessRoleArn": "arn:aws:iam::12345678901:role/AwsMarketplaceSageMakerIngestion",
                        "UsageInstructions":"This is how you use your algorithm", 
                       "SampleNotebookUrl": "https://www.amazon.com",
                        "RepositoryUrl": "https://www,amazon.com",
                        "InputProperties": {
                            "Description": "Input should have all columns in the train/test file except for 'is_fraud' column.",
                            "Limitations": "Can predict on 1 input in the CSV only at a time",
                           "SampleInput": {
                                "RealtimeInferenceText": "{\"prompt\":\"Write summary\",
                                                            \"maxTokens\": 1 }",
                                "BatchTransformUrl": "https://www.sampleData.com",
                            },
                           "Parameters": [{
                                    "Name": "prompt",
                                    "Description": "Represents the instruct-style prompt for the model. DataType is String",
                                    "Constraints": "Minimum length should be 1",
                                    "Required": true
                                },
                                {
                                    "Name": "maxTokens",
                                    "Description": "Denotes the number of tokens to predict per generation. See BPE Tokens for more details.",
                                    "Constraints": "Minvalue: 1, MaxValue: 30"
                                }
                            ],
                            "SageMakerCustomAttributes": [{
                                    "Name": "threshold",
                                    "Description": "Threshold of the confidence score of the detected object",
                                    "Constraints": "Should be an Integer"
                            }]
                    },
                    "OutputProperties": {
                        "Description": "The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                       "SampleOutput": {
                            "RealtimeInferenceUrl": "https://www.sampledata.com",
                            "BatchTransformUrl": "https://www.sampleData.com",
                        },
                       "Parameters": [{
                                "Name": "id",
                                "Description": "An identifier for response"
                                "AlwaysReturned": true
                            },
                            {
                                "Name": "generations",
                                "Description": "The generated text along with the likelihoods for tokens requested.",
                            }
                        ],
                    },
                   "RecommendedInstanceTypes": {
                        "BatchTransform": "ml.m4.large",
                        "RealtimeInference": "ml.m4.large",
                        "Training": "ml.m4.large"
                   }
                }
            }]
        }
    }],
    "Intent": "APPLY"
}
```

## Required fields
<a name="add-version-required-fields"></a>
+  `Entity` (object)—required 

  Contains information about your ML product.
  +  `Identifier` (string)—required 

    Your product ID. For more information, see [Identifier](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#identifier).
  +  `Type` (string)—required 

    Specifies the delivery method (product type). It must be `MachineLearningProduct@1.0`.
+ `DetailsDocument` (object)—required

  Contains all details about the new version of your product.
  + `Version` (object)—required

    Details about the version being added.
    + `VersionTitle` (string)—required

      The title of the version, such as "Version 1.1" or "1.1". Buyers select versions from these titles.
    + `ReleaseNotes` (string)—required

      Detailed notes about this version. Must be under 30,000 characters.
  + `DeliveryOptions` (array)—required

    Array of delivery methods for your product version. Limited to one delivery option per version.
    + `Details` (object)—required
      + `SagemakerModelPackageDeliveryOptionDetails` or `SageMakerAlgorithmDeliveryOptionDetails` (object)
        + `SageMakerModelPackageArn` or `SageMakerAlgorithmArn` (string)—required

          Amazon Resource Name (ARN) of your model package or algorithm.
        + `AccessRoleArn` (string)—required 

          IAM role ARN for AWS Marketplace to access the SageMaker resource.
        + `SampleNotebookUrl` (string)—required 

          Link to sample Jupyter notebook with usage code. For more information, refer to a [sample notebook template](https://github.com/aws/amazon-sagemaker-examples/blob/master/aws_marketplace/curating_aws_marketplace_listing_and_sample_notebook/ModelPackage/Sample_Notebook_Template/title_of_your_product-Model.ipynb) on GitHub.
        + `RepositoryUrl` (string)—required 

          Git repository URL for notebook and sample data access. For more information, see a [sample Git repository](https://github.com/aws/amazon-sagemaker-examples/tree/master/aws_marketplace/curating_aws_marketplace_listing_and_sample_notebook/ModelPackage/Sample_Notebook_Template) on GitHub. 
        + `UsageInstructions` (string)—required 

          Training information for algorithms or usage details for models.
        + `InputProperties` (object)—required
          + `Description` (string)—required 

            Description of model/algorithm inputs
          + `Limitations` (string) 

            Input limitations
          + `SampleInput` (object)—required

            RealtimeInferenceUrl (string) \| RealtimeInferenceText (string) \| BatchTransformUrl (string) \| BatchTransformText (string)
          + `Parameters` (Array<Object>)

            Name (string)—required \| Description (string)—Required \| Constraints (string) \| Required (boolean)
          + `SageMakerCustomAttributes` (Array<Object>)

            Describes any [CustomAttributes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html#API_runtime_InvokeEndpoint_RequestParameters) supported by your model.

            `Name` (string)—required \| `Description` (string)—Required \| `Constraints` (string) \| `Required` (boolean)
        + `OutputProperties` (object)—required
          + `Description` (string)—required
          + `SampleOutput` (Array<Object>)—required

            RealtimeInferenceUrl (string) \| RealtimeInferenceText (string) \| BatchTransformUrl (string) \| BatchTransformText (string)
          + `Parameters` (Array)

            Name (string)—required \| Description (string)—required \| AlwaysReturned (boolean)
        + `RecommendedInstanceTypes` (object)—required
          + `BatchTransform` (string)—Required
          + `RealtimeInference` (string)—Required
          + `Training` (string)—Required for SageMaker Algorithms only

## Response syntax
<a name="response-syntax"></a>

When you submit the request, a change set is created and the API returns:

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

**Change set processing**  
The change request enters a processing queue, where it undergoes several steps:

1. Validation: The system checks to ensure all information meets AWS Marketplace guidelines.
   +  Processing time: Few minutes to several hours 
   +  For validation errors, see [Change set status and errors](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-seller-products.html#seller-product-change-set-errors). 

1.  Status monitoring: You can check the status of the request two ways. 
   + Via AWS Marketplace Management Portal
   + Using the `DescribeChangeSet` operation

1.  Completion: When approved, the new version is added. 

## Errors
<a name="errors"></a>

**Asynchronous errors**  
 The following errors are specific to `AddDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors appear when you call `DescribeChangeSet` while a change set is being processed. For more information about using `DescribeChangeSet` to check the status of a change request, see [Working with change sets](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets). 




| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT\_STATUS | We couldn't locate the provided product. Provide a valid product. | 
| DUPLICATE\_VERSION\_TITLE | The provided version title is already in use. Create a unique version title. | 
| INVALID\_RECOMMENDED\_INSTANCE\_TYPE | You didn't provide a valid instance type for [x]. Enter a valid instance type and try again. Valid types are: [valids] | 
| INCOMPATIBLE\_DELIVERY\_OPTIONS | The delivery option you provided doesn't match your previous selection: [previous selection]. Update your delivery option and try again. | 
| INVALID\_ASSET\_ARN | You didn't provide a valid ARN for SageMakerAlgorithmDeliveryOption. Enter a valid ARN and try again. | 
| DUPLICATE\_ASSET | You didn't provide a unique ARN for this product. Enter a unique ARN and try again. | 
| ASSET\_NOT\_FOUND | We couldn't locate the ARN you provided. Verify that the ARN is correct and has the required permissions. | 
| ASSET\_VALIDATION\_EXCEPTION | Unable to ingest SagemakerModelArn/SagemakerAlgorithmArn [x] into AWS Sagemaker account | 
| INVALID\_ACCESS\_ROLE | We couldn't locate the IAM role ARN you provided. Verify that the ARN is correct and try again. | 
| UPDATE\_PRICING\_REQUIRED | UpdatePricingTerms is required. | 