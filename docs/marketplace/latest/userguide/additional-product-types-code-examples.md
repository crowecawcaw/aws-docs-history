

# Code examples

RTB Fabric module products use contract pricing only and aren't metered. AWS RTB Fabric checks the buyer's entitlement, so you don't report usage. If your systems enforce the purchased quantity, you can use the following Python code example to check entitlements with `GetEntitlements`.

For information about setting up the AWS CLI, along with credentials, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS Command Line Interface User Guide*. If you're new to the AWS Python SDK, see the Boto 3 [Quickstart](https://boto3.readthedocs.io/en/latest/guide/quickstart.html).

**Topics**
+ [`GetEntitlements` code example](#additional-product-types-getentitlements-example)

## `GetEntitlements` code example
<a name="additional-product-types-getentitlements-example"></a>

The following code example is relevant for contract agreements. The Python example verifies that a customer has an active entitlement and returns the purchased quantity.

```python
# Import AWS Python SDK
import boto3

marketplaceClient = boto3.client('marketplace-entitlement', region_name='us-east-1')

# Filter entitlements for a specific buyer
#
# productCode is available from describe-entity after you release
# the product to the Limited state
entitlement = marketplaceClient.get_entitlements({
    'ProductCode': 'productCode',
    'Filter' : {
        # Option 1: Using CustomerAWSAccountId (preferred)
        'CUSTOMER_AWS_ACCOUNT_ID': [
            'awsAccountId',
        ]
        # Option 2: Using LICENSE_ARN (to get entitlements for the license)
        # 'LICENSE_ARN': [
        #     'licenseARN',
        # ]
    },
    'NextToken' : 'string',
    'MaxResults': 123
})

# TODO: Verify the dimension a customer is subscribed to and the quantity,
# if applicable
```

For more information about `GetEntitlements`, see [GetEntitlements](https://docs.aws.amazon.com/marketplaceentitlement/latest/APIReference/API_GetEntitlements.html) in the *AWS Marketplace Entitlement Service API Reference*.

### Example response
<a name="additional-product-types-getentitlements-example-response"></a>

The returned value corresponds to the dimensions created when you created the product in AWS Partner Central or with the Catalog APIs.

```json
{
   "Entitlements": [
      {
         "CustomerIdentifier": "string",
         "CustomerAWSAccountId": "string",
         "Dimension": "string",
         "ExpirationDate": number,
         "ProductCode": "string",
         "LicenseArn": "string",
         "Value": {
            "BooleanValue": boolean,
            "DoubleValue": number,
            "IntegerValue": number,
            "StringValue": "string"
         }
      }
   ],
   "NextToken": "string"
}
```