

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Restrict a version
<a name="ml-restrict-version"></a>

 You can use the Catalog API to restrict a version of your machine learning product in AWS Marketplace. When restricted, new buyers cannot access that version. Existing subscribers retain access to restricted versions. AWS Marketplace guidelines require continued support for existing buyers for 90 days after restriction. 

**Important**  
 At least one unrestricted version must remain available. You cannot restrict the last publicly available version of a product. 

**To restrict a version:**
+  To restrict a version, call the `StartChangeSet` operation with the `RestrictDeliveryOptions` change type. 

## Request syntax
<a name="ml-restrict-version-request-syntax"></a>

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json
{
"Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "RestrictDeliveryOptions",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
        "Type": "MachineLearningProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptionIds":
        [
          "{{example1-2222-cccc-2222-cccccccccccc}}"
        ]
      }
    }
  ]
}
```

## Required fields
<a name="ml-restrict-version-required-fields"></a>

**Required fields**
+  `Entity` (object)—required 

  Contains information about your ML product.
  +  `Identifier` (string)—required 

    Your product ID. For more information, see [Identifier](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#identifier).
  +  `Type` (string)—required 

    Specifies the delivery method (product type). It must be `MachineLearningProduct@1.0`.
+  `DetailsDocument` (object)—required 

   Contains the updated version information. 
  + `DeliveryOptionIds` (array of objects)—required

    List of DeliveryOption IDs for the versions you want to restrict. Retrieve the unique identifier for each DeliveryOption by calling the DescribeEntity action on the version you're restricting.

## Response syntax
<a name="ml-restrict-version-response-syntax"></a>

A successful request returns:

```
{
    "ChangeSetId": "example123456789012abcdef",
    "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

1. Validation: The system checks if all information meets AWS Marketplace guidelines.
   +  Processing time: Few minutes to several hours 
   +  For validation errors, see [Change set status and errors](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-seller-products.html#seller-product-change-set-errors). 

1.  Status monitoring: You can check the status of the request two ways. 
   + Via AWS Marketplace Management Portal
   + Using the `DescribeChangeSet` operation

1.  Completion: When approved, the new version is restricted. 

## Errors
<a name="ml-restrict-version-errors"></a>

**Asynchronous errors**  
The following errors may occur during change set processing and can be retrieved using the `DescribeChangeSet` operation:


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT\_STATUS | Use an existing public or limited product | 
| MISSING\_DELIVERY\_OPTION\_IDS | Provide delivery option from existing list of IDs. | 
| INVALID\_DELIVERY\_OPTION\_IDS | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| INVALID\_DELIVERY\_OPTION\_STATUS | The delivery option IDs [invalid\_ids] are invalid. Provide delivery options in the public state. | 
| ALL\_DELIVERY\_OPTIONS\_RESTRICTED | Provide fewer delivery options to restrict as at least one must remain in public state. | 