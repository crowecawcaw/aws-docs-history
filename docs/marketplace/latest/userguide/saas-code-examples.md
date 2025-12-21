# Code examples for SaaS product integration

You can use the following code examples to integrate your software as a service (SaaS)
product with the AWS Marketplace APIs that are required for publishing and maintaining your
product. For more information, see the following sections.

###### Topics

- [ResolveCustomer code
  example](#saas-resolvecustomer-example "#saas-resolvecustomer-example")
- [GetEntitlement code
  example](#saas-getentitlement-example "#saas-getentitlement-example")
- [BatchMeterUsage code
  example](#saas-batchmeterusage-example "#saas-batchmeterusage-example")
- [BatchMeterUsage with usage
  allocation tagging code example (Optional)](#saas-batchmeterusage-tagging "#saas-batchmeterusage-tagging")

## `ResolveCustomer` code

example

The following code example is relevant for all pricing models. The Python example
exchanges a `x-amzn-marketplace-token` token for a
`CustomerIdentifier`, `ProductCode`, and
`CustomerAWSAccountId`. The `CustomerAWSAccountId` is the
AWS account ID associated with the subscription. This code runs in an application on
your registration website, when you are redirected there from the AWS Marketplace Management Portal. The
redirect is a POST request that includes the token.

For more information about `ResolveCustomer`, see [ResolveCustomer](../../../marketplacemetering/latest/APIReference/API_ResolveCustomer.md "../../../marketplacemetering/latest/APIReference/API_ResolveCustomer.md") in the _AWS Marketplace Metering Service API Reference_.

###### Note

For new implementation or when updating your integration, use the CustomerAWSAccountId instead of CustomerIdentifier.

```
# Import AWS Python SDK and urllib.parse
import boto3
import urllib.parse as urlparse

# Resolving Customer Registration Token
formFields = urlparse.parse_qs(postBody)
regToken = formFields['x-amzn-marketplace-token'][0]

# If regToken present in POST request, exchange for customerID
if (regToken):
    marketplaceClient = boto3.client('meteringmarketplace')
    customerData = marketplaceClient.resolve_customer(RegistrationToken=regToken)
    productCode = customerData['ProductCode']
    customerID = customerData['CustomerIdentifier']
    customerAWSAccountId = customerData['CustomerAWSAccountId']

    # TODO: Store customer information
    # TODO: Validate no other accounts share the same customerID
```

### Example response

```
{
    'CustomerIdentifier': 'string',
    'CustomerAWSAccountId':'string',
    'ProductCode': 'string'
}
```

## `GetEntitlement` code

example

The following code example is relevant for SaaS products with the contract and SaaS
contract with consumption pricing model. The Python example verifies that a customer has
an active entitlement.

For more information about `GetEntitlement`, see [GetEntitlement](../../../marketplaceentitlement/latest/APIReference/API_GetEntitlements.md "../../../marketplaceentitlement/latest/APIReference/API_GetEntitlements.md") in the _AWS Marketplace Entitlement Service API Reference_.

```
# Import AWS Python SDK
import boto3

marketplaceClient = boto3.client('marketplace-entitlement', region_name='us-east-1')

# Filter entitlements for a specific customerID
#
# productCode is supplied after the AWS Marketplace Ops team has published
# the product to limited
#
# customerID is obtained from the ResolveCustomer response
entitlement = marketplaceClient.get_entitlements({
    'ProductCode': 'productCode',
    'Filter' : {
        # Option 1: Using CustomerIdentifier (for new or updated integrations, use the customer AWS account ID)
        'CUSTOMER_IDENTIFIER': [
            'customerID',
        ]
        # Option 2: Using CustomerAWSAccountID (preferred)
        # 'CUSTOMER_AWS_ACCOUNT_ID': [
        #     'awsAccountID',
        # ]
    },
    'NextToken' : 'string',
    'MaxResults': 123
})

# TODO: Verify the dimension a customer is subscribed to and the quantity,
# if applicable

```

### Example response

The returned value corresponds to the dimensions created when you created the
product in the AWS Marketplace Management Portal.

```
{
   "Entitlements": [
      {
         "CustomerIdentifier": "string",
         "CustomerAWSAccountID": "string",
         "Dimension": "string",
         "ExpirationDate": number,
         "ProductCode": "string",
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

## `BatchMeterUsage` code

example

The following code example is relevant for SaaS subscription and contract with
consumption pricing models, but not for SaaS contract products without consumption. The
Python example sends a metering record to AWS Marketplace to charge your customers for
pay-as-you-go fees.

```
# NOTE: Your application will need to aggregate usage for the
#       customer for the hour and set the quantity as seen below.
#       AWS Marketplace can only accept records for up to an hour in the past.
#
# productCode is supplied after the AWS Marketplace Ops team has
# published the product to limited
#
# You can use either:
# - customerID from the ResolveCustomer response (deprecated after Dec 31, 2025)
# - AWS account ID of the buyer

# Import AWS Python SDK
import boto3
from datetime import datetime

# Option 1: Using CustomerIdentifier (for new or updated integrations, use the customer AWS account ID)
usageRecord = [
    {
        'Timestamp': datetime(2015, 1, 1),
        'CustomerIdentifier': 'customerID',
        'Dimension': 'string',
        'Quantity': 123
    }
]

# Option 2: Using CustomerAWSAccountID (preferred)
# usageRecord = [
#     {
#         'Timestamp': datetime(2015, 1, 1),
#         'CustomerAWSAccountID': 'awsAccountID',
#         'Dimension': 'string',
#         'Quantity': 123
#     }
# ]

marketplaceClient = boto3.client('meteringmarketplace')

response = marketplaceClient.batch_meter_usage(
    UsageRecords=usageRecord,
    ProductCode='productCode'
)

```

For more information about `BatchMeterUsage`, see [BatchMeterUsage](../../../marketplacemetering/latest/APIReference/API_BatchMeterUsage.md "../../../marketplacemetering/latest/APIReference/API_BatchMeterUsage.md") in the _AWS Marketplace Metering Service API Reference_.

### Example response

```
{
    'Results': [
        {
            'UsageRecord': {
                'Timestamp': datetime(2015, 1, 1),
                'CustomerIdentifier': 'string',
                'CustomerAWSAccountID': 'string',
                'Dimension': 'string',
                'Quantity': 123
            },
            'MeteringRecordId': 'string',
            'Status': 'Success' | 'CustomerNotSubscribed' | 'DuplicateRecord'
        },
    ],
    'UnprocessedRecords': [
        {
            'Timestamp': datetime(2015, 1, 1),
            'CustomerIdentifier': 'string',
            'CustomerAWSAccountID': 'string',
            'Dimension': 'string',
            'Quantity': 123
        }
    ]
}

```

## `BatchMeterUsage` with usage

allocation tagging code example (Optional)

The following code example is relevant for SaaS subscriptions and contracts with
usage pricing models, but not for SaaS contract products without usage. The
Python example sends a metering record with appropriate usage allocation tags to AWS Marketplace
to charge your customers for pay-as-you-go fees.

```
# NOTE: Your application will need to aggregate usage for the
#       customer for the hour and set the quantity as seen below.
#       AWS Marketplace can only accept records for up to an hour in the past.
#
# productCode is supplied after the AWS Marketplace Ops team has
# published the product to limited
#
# You can use either:
# - customerID from the ResolveCustomer response (deprecated after Dec 31, 2025)
# - AWS account ID of the buyer

# Import AWS Python SDK
import boto3
import time

# Option 1: Using CustomerIdentifier (for new or updated integrations, use the customer AWS account ID)
usageRecords = [
    {
        "Timestamp": int(time.time()),
        "CustomerIdentifier": "customerID",
        "Dimension": "Dimension1",
        "Quantity": 3,
        "UsageAllocations": [
            {
                "AllocatedUsageQuantity": 2,
                "Tags": [
                    { "Key": "BusinessUnit", "Value": "IT" },
                    { "Key": "AccountId", "Value": "*********" },
                ]
            },
            {
                "AllocatedUsageQuantity": 1,
                "Tags": [
                    { "Key": "BusinessUnit", "Value": "Finance" },
                    { "Key": "AccountId", "Value": "*********" },
                ]
            },
        ]
    }
]

# Option 2: Using CustomerAWSAccountID (preferred)
# usageRecords = [
#     {
#         "Timestamp": int(time.time()),
#         "CustomerAWSAccountID": "awsAccountID",
#         "Dimension": "Dimension1",
#         "Quantity": 3,
#         "UsageAllocations": [
#             {
#                 "AllocatedUsageQuantity": 2,
#                 "Tags": [
#                     { "Key": "BusinessUnit", "Value": "IT" },
#                     { "Key": "AccountId", "Value": "*********" },
#                 ]
#             },
#             {
#                 "AllocatedUsageQuantity": 1,
#                 "Tags": [
#                     { "Key": "BusinessUnit", "Value": "Finance" },
#                     { "Key": "AccountId", "Value": "*********" },
#                 ]
#             },
#         ]
#     }
# ]

marketplaceClient = boto3.client('meteringmarketplace')

response = marketplaceClient.batch_meter_usage(
    UsageRecords=usageRecords,
    ProductCode="testProduct"
)

```

For more information about `BatchMeterUsage`, see [BatchMeterUsage](../../../marketplacemetering/latest/APIReference/API_BatchMeterUsage.md "../../../marketplacemetering/latest/APIReference/API_BatchMeterUsage.md") in the _AWS Marketplace Metering Service API
Reference_.

### Example response

```
{
    "Results": [
        {
            "Timestamp": "1634691015",
            "CustomerIdentifier": "customerID",
            "CustomerAWSAccountID": "awsAccountID",
            "Dimension": "Dimension1",
            "Quantity": 3,
            "UsageAllocations": [
                {
                    "AllocatedUsageQuantity": 2,
                    "Tags": [
                        { "Key": "BusinessUnit", "Value": "IT" },
                        { "Key": "AccountId", "Value": "*********" }
                    ]
                },
                {
                    "AllocatedUsageQuantity": 1,
                    "Tags": [
                        { "Key": "BusinessUnit", "Value": "Finance" },
                        { "Key": "AccountId", "Value": "*********" }
                    ]
                }
            ],
            "MeteringRecordId": "8fjef98ejf",
            "Status": "Success"
        }
    ],
    "UnprocessedRecords": [
        {
            "Timestamp": "1634691015",
            "CustomerIdentifier": "customerID",
            "CustomerAWSAccountID": "awsAccountID",
            "Dimension": "Dimension1",
            "Quantity": 3,
            "UsageAllocations": []
        }
    ]
}
```
