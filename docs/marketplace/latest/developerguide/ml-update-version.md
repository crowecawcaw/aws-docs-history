

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Update version information
<a name="ml-update-version"></a>

 You can use the Catalog API to update details of an existing version of your machine learning product in AWS Marketplace. 

**Important**  
 You cannot update the ARN for a version. If you need to modify the ARN, you must create a new version instead. 

**Using `StartChangeSet` to add a version:**
+  To update version information, call the `StartChangeSet` operation with the `UpdateDeliveryOptions` change type. 

## Request syntax
<a name="ml-update-version-request-syntax"></a>

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateDeliveryOptions",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
        "Type": "MachineLearningProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "ReleaseNotes": "{{Adding support for new parameters}}"
        },
        "DeliveryOptions":
        [
          {
            "Id": "{{example1-2222-cccc-2222-cccccccccccc}}",
            "Details":
            {
              "SagemakerModelPackageDeliveryOptionDetails":
              {
                "SampleNotebookUrl": "{{https://www.amazon.com}}",
                "RepositoryUrl":"{{https://www,amazon.com}}",
                "InputProperties": 
                { 
                    "SampleInput": {
                        "RealtimeInferenceUrl": "{{https://www.sampleData.com}}",
                        "BatchTranformUrl": "{{https://www.sampleData.com}}",
                     },
                 },
                 "RecommendedInstanceTypes": {
                        "BatchTransform": "{{ml.m4.large}}",
                        "RealtimeInference": "{{ml.m4.large}}"
                  }
            }
          }
        ]
      }
    }
  ]
}
```

## Required fields
<a name="ml-update-version-required-fields"></a>
+  `Entity` (object)—required 

  Contains information about your ML product.
  +  `Identifier` (string)—required 

    Your product ID. For more information, see [Identifier](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#identifier).
  +  `Type` (string)—required 

    Specifies the delivery method (product type). It must be `MachineLearningProduct@1.0`.
+  `DetailsDocument` (object)—required 

   Contains the updated version information. 
  + `Version` (object)—required

    Defines version-specific information.
    + `VersionTitle` (string)—required

      The version identifier displayed to buyers, such as "Version 1.1" or "1.1". Buyers use this title to select versions for deployment.
    + `ReleaseNotes` (string)—required 

      Detailed notes about this version, limited to 30,000 characters.
  + `DeliveryOptions` (array)—required 

    Specifies delivery methods for your product version. Limited to one delivery option per version.
    + `Id` (string)—required 

      Unique identifier for the DeliveryOption. Retrieve this using the DescribeEntity action on your product.
    + `Details` (object)—required 

      Contains the delivery option specifications.
      + `SageMakerModelPackageSubscriptionDetails` or `SageMakerAlgorithmSubscriptionDetails` (object)—required 

        Details of the delivery option.
        + `SampleNotebookUrl` (string)—required 

          Sample Jupyter notebook link providing code for buyer usage.
        + `RepositoryUrl` (string)—required 

          Git repository URL for cloning notebook and sample data.
        + `UsageInstructions` (string)—required 

          For algorithms: training information. For models: additional usage information.
        + `InputProperties` (object)—required 

          Details of the model/algorithm's input requirements.
          + `Description` (string)—required 

            Description of required inputs.
          + `Limitations` (string) 

            Any input limitations.
          + `SampleInput` (object)—required 

            Sample input data for different operations.
            + `RealtimeInferenceUrl` (string) 

              Sample input URL for realtime inference.
            + `RealtimeInferenceText` (string) 

              Sample input text for realtime inference.
            + `BatchTransformUrl` (string) 

              Sample input URL for batch transform jobs.
            + `BatchTransformText` (string) 

              Sample input text for batch transform jobs.
          + `Parameters` (Array<Object>) 

            Details for each input parameter.
            + `Name` (string)—required 

              Name of the input parameter.
            + `Description` (string)—required 

              Description of the input parameter.
            + `Constraints` (string) 

              Parameter constraints (MinValue, MaxValue, AllowedValues, MinLength, MaxLength, Pattern, etc.).
            + `Required` (boolean) 

              Indicates if the parameter is required. Default is false.
          + `SageMakerCustomAttributes` (Array<Object>) 

            Details for supported CustomAttributes.
            + `Name` (string)—required 

              Name of the custom attribute.
            + `Description` (string)—required 

              Description of the custom attribute.
            + `Constraints` (string) 

              Attribute constraints (MinValue, MaxValue, AllowedValues, MinLength, MaxLength, Pattern, etc.).
            + `Required` (boolean) 

              Indicates if the attribute is required. Default is false.
        + `OutputProperties` (object)—required 

          Details of the model/algorithm's output.
          + `Description` (string)—required 

            Description of model/algorithm outputs.
          + `SampleOutput` (Array<Object>)—required 

            Sample output data for different operations.
            + `RealtimeInferenceUrl` (string) 

              Sample output URL for realtime inference.
            + `RealtimeInferenceText` (string) 

              Sample output text for realtime inference.
            + `BatchTransformUrl` (string) 

              Sample output URL for batch transform jobs.
            + `BatchTransformText` (string) 

              Sample output text for batch transform jobs.
          + `Parameters` (Array) 

            Details for each output parameter.
            + `Name` (string)—required 

              Name of the output parameter.
            + `Description` (string)—required 

              Description of the output parameter.
            + `AlwaysReturned` (boolean) 

              Indicates if the parameter is always returned. Default is false.
        + `RecommendedInstanceTypes` (object)—required 

          Recommended instance types for optimal performance.
          + `BatchTransform` (string)—required 

            Recommended instance type for batch transform operations.
          + `RealtimeInference` (string)—required 

            Recommended instance type for realtime inference operations.
          + `Training` (string)—required 

            Recommended instance type for algorithm training operations. Required only for SageMaker Algorithms.

## Response syntax
<a name="ml-update-version-response-syntax"></a>

A successful request returns:

```
{
    "ChangeSetId": "example123456789012abcdef",
    "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

**Change set processing**  
The change request enters a processing queue, where it undergoes several steps:

1. Validation: The system checks if all information meets AWS Marketplace guidelines.
   +  Processing time: Few minutes to several hours 
   +  For validation errors, see [Change set status and errors](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-seller-products.html#seller-product-change-set-errors). 

1.  Status monitoring: You can check the status of the request two ways. 
   + Via AWS Marketplace Management Portal
   + Using the `DescribeChangeSet` operation

1.  Completion: When approved, the new version is updated. 

## Errors
<a name="ml-update-version-errors"></a>

**Asynchronous errors**  
Specific errors for `UpdateDeliveryOptions` actions can be retrieved using the `DescribeChangeSet` operation after the change set begins processing. For error details and troubleshooting, see [ Change set status and errors](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets). 


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT\_STATUS | Use an existing limited or public product. | 
| INVALID\_DELIVERY\_OPTION\_ID | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| INCOMPATIBLE\_DELIVERY\_OPTION\_STATUS | The delivery option cannot be updated because it's in restricted status. Try adding a new version instead. | 
| INCOMPATIBLE\_DELIVERY\_OPTIONS | Product previously used [X ] as delivery option, therefore all the upcoming delivery options should be of type [X] | 
| INVALID\_RECOMMENDED\_INSTANCE\_TYPE | Provide an existing, available instance type for [X] (X can be Batch Transform, Realtime Inference or ALgorithm Training) | 
| DUPLICATE\_VERSION\_TITLE | The version title must be different from any other version titles of this product. | 
| FIELD\_NOT\_ALLOWED\_TO\_CHANGE | Field X is not allowed to be changed. | 