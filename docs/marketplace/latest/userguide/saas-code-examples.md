# Code examples for SaaS product integration

You can use the following code examples to integrate your software as a service (SaaS)
product with the AWS Marketplace APIs that are required for publishing and maintaining your
product. For more information, see the following sections.

###### Topics

- [ResolveCustomer code example](#saas-resolvecustomer-example "#saas-resolvecustomer-example")
- [GetEntitlement code example](#saas-getentitlement-example "#saas-getentitlement-example")
- [BatchMeterUsage code example](#saas-batchmeterusage-example "#saas-batchmeterusage-example")
- [BatchMeterUsage code example: With License ARN](#saas-batchmeterusage-licensearn-example "#saas-batchmeterusage-licensearn-example")
- [BatchMeterUsage with usage allocation tagging code example (Optional)](#saas-batchmeterusage-tagging "#saas-batchmeterusage-tagging")

## `ResolveCustomer` code example

The following code example is relevant for all pricing models. The Python example
exchanges a `x-amzn-marketplace-token` token for a
`CustomerIdentifier`, `ProductCode`, `LicenseArn`, and
`CustomerAWSAccountId`. The `CustomerAWSAccountId` is the
AWS account ID associated with the subscription, and `LicenseArn` is a unique identifier for a specific granted license. These are used for software purchased through AWS Marketplace. This code runs in an application on
your registration website, when you are redirected there from the AWS Marketplace Management Portal. The
redirect is a POST request that includes the token.

For more information about `ResolveCustomer`, see [ResolveCustomer](../../../marketplacemetering/latest/APIReference/API_ResolveCustomer.md "../../../marketplacemetering/latest/APIReference/API_ResolveCustomer.md") in the _AWS Marketplace Metering Service API Reference_.

###### Important

For new SaaS product integrations, the `CustomerIdentifier` field is not populated in the `ResolveCustomer` API response. Use `CustomerAWSAccountId` and `LicenseArn` instead for customer identification.

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
    licenseARN = customerData['LicenseArn']

    # TODO: Store customer information
    # TODO: Validate no other accounts share the same customerID
```

### Example response

```
{
    'CustomerIdentifier': 'string',
    'CustomerAWSAccountId':'string',
    'ProductCode': 'string',
    'LicenseArn' : 'string'
}
```

## `GetEntitlement` code example

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
        # Option 1: Using CustomerAWSAccountId (preferred)
        'CUSTOMER_AWS_ACCOUNT_ID': [
            'awsAccountId',
        ]
        # Option 2: Using LICENSE_ARN (to get entitlements for the license)
        # 'LICENSE_ARN': [
        #     'licenseARN',
        # ]
        # Option 3: Using CustomerIdentifier (existing integrations only, not supported for new integrations)
        # 'CUSTOMER_IDENTIFIER': [
        #     'customerID',
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

## `BatchMeterUsage` code example

The following code example is relevant for SaaS subscription and contract with
consumption pricing models, but not for SaaS contract products without consumption. The
Python example sends a metering record to AWS Marketplace to charge your customers for
pay-as-you-go fees.

###### Important

`BatchMeterUsage` does not support `CustomerIdentifier` for new SaaS product integrations. For new integrations, see [BatchMeterUsage code example: With License ARN](#saas-batchmeterusage-licensearn-example "#saas-batchmeterusage-licensearn-example").

```
# NOTE: Your application will need to aggregate usage for the
#       customer for the hour and set the quantity as seen below.
#       AWS Marketplace can only accept records for up to an hour in the past.
#
# productCode is supplied after the AWS Marketplace Ops team has
# published the product to limited
#
# customerID is obtained from the ResolveCustomer response

# Import AWS Python SDK
import boto3
from datetime import datetime

usageRecord = [
    {
        'Timestamp': datetime(2015, 1, 1),
        'CustomerIdentifier': 'customerID',
        'Dimension': 'string',
        'Quantity': 123
    }
]

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
                'CustomerAWSAccountId': 'string',
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
            'CustomerAWSAccountId': 'string',
            'Dimension': 'string',
            'Quantity': 123
        }
    ]
}

```

## `BatchMeterUsage` code example: With License ARN

The following code example is relevant for SaaS products that support Concurrent Agreements.
The `LicenseArn` and `CustomerAWSAccountId` are returned by the
`ResolveCustomer` API when a buyer registers to your product.

```
# NOTE: Your application will need to aggregate usage for the
#       customer for the hour and set the quantity as seen below.
#       AWS Marketplace can only accept records for up to an hour in the past.
#
# LicenseArn and CustomerAWSAccountId are returned by the ResolveCustomer
# API when a buyer registers to your product

# Import AWS Python SDK
import boto3
from datetime import datetime


usageRecord = [{
    'LicenseArn' : 'licenseArn',
    'Timestamp': datetime(2015, 1, 1),
    'CustomerAWSAccountId': 'awsAccountId',
    'Dimension': 'string',
    'Quantity': 123
}]


marketplaceClient = boto3.client('meteringmarketplace')

response = marketplaceClient.batch_meter_usage(
    UsageRecords = usageRecord
)
```

### Example response

```
{
    'Results': [
        {
            'UsageRecord': {
                'Timestamp': datetime(2015, 1, 1),
                'CustomerIdentifier': 'string',
                'CustomerAWSAccountId': 'string',
                'Dimension': 'string',
                'Quantity': 123,
                'LicenseArn': 'string'
            },
            'MeteringRecordId': 'string',
            'Status': 'Success' | 'CustomerNotSubscribed' | 'DuplicateRecord'
        },
    ],
    'UnprocessedRecords': [
        {
            'Timestamp': datetime(2015, 1, 1),
            'CustomerIdentifier': 'string',
            'CustomerAWSAccountId': 'string',
            'Dimension': 'string',
            'Quantity': 123,
            'LicenseArn': 'string'
        }
    ]
}
```

## `BatchMeterUsage` with usage allocation tagging code example (Optional)

The following code example is relevant for SaaS subscriptions and contracts with
usage pricing models, but not for SaaS contract products without usage. The
Python example sends a metering record with appropriate usage allocation tags to AWS Marketplace
to charge your customers for pay-as-you-go fees.

This example uses `LicenseArn` and `CustomerAWSAccountId`, which
are returned by the `ResolveCustomer` API when a buyer registers to your
product. Using `LicenseArn` supports products with Concurrent Agreements,
where a single buyer can have multiple active agreements for the same product.

```
# NOTE: Your application will need to aggregate usage for the
#       customer for the hour and set the quantity as seen below.
#       AWS Marketplace can only accept records for up to an hour in the past.
#
# LicenseArn and CustomerAWSAccountId are returned by the
# ResolveCustomer API when a buyer registers to your product.

# Import AWS Python SDK
import boto3
from datetime import datetime, timezone

usageRecords = [
    {
        "Timestamp": datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0),
        "CustomerAWSAccountId": "111122223333",
        "Dimension": "Dimension1",
        "LicenseArn": "arn:aws:license-manager::123456789012:license:l-exampleLicense12345",
        "Quantity": 10000,
        "UsageAllocations": [
            {
                "AllocatedUsageQuantity": 5000,
                "Tags": [
                    {"Key": "user", "Value": "john"},
                    {"Key": "feature", "Value": "data-processing"},
                    {"Key": "job-name", "Value": "job11111"},
                ]
            },
            {
                "AllocatedUsageQuantity": 2500,
                "Tags": [
                    {"Key": "user", "Value": "john"},
                    {"Key": "feature", "Value": "data-storage"},
                    {"Key": "cluster-name", "Value": "cluster11111"},
                ]
            },
            {
                "AllocatedUsageQuantity": 2500,
                "Tags": [
                    {"Key": "user", "Value": "jane"},
                    {"Key": "feature", "Value": "data-storage"},
                    {"Key": "cluster-name", "Value": "cluster22222"},
                ]
            },
        ]
    },
    {
        "Timestamp": datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0),
        "CustomerAWSAccountId": "111122223333",
        "Dimension": "Dimension2",
        "LicenseArn": "arn:aws:license-manager::123456789012:license:l-exampleLicense12345",
        "Quantity": 2000,
        "UsageAllocations": [
            {
                "AllocatedUsageQuantity": 1000,
                "Tags": [
                    {"Key": "user", "Value": "john"},
                    {"Key": "feature", "Value": "data-processing"},
                    {"Key": "job-name", "Value": "job11111"},
                ]
            },
            {
                "AllocatedUsageQuantity": 1000,
                "Tags": [
                    {"Key": "user", "Value": "jane"},
                    {"Key": "feature", "Value": "data-processing"},
                    {"Key": "job-name", "Value": "job22222"},
                ]
            },
        ]
    }
]

marketplaceClient = boto3.client('meteringmarketplace', region_name='us-east-1')

response = marketplaceClient.batch_meter_usage(
    UsageRecords=usageRecords
)

```

For more information about `BatchMeterUsage`, see [BatchMeterUsage](../../../marketplacemetering/latest/APIReference/API_BatchMeterUsage.md "../../../marketplacemetering/latest/APIReference/API_BatchMeterUsage.md") in the _AWS Marketplace Metering Service API
Reference_.

### Example response

```
{
    "Results": [
        {
            "UsageRecord": {
                "Timestamp": "2025-06-05T14:00:00Z",
                "CustomerIdentifier": "customerID",
                "CustomerAWSAccountId": "111122223333",
                "Dimension": "Dimension1",
                "Quantity": 10000,
                "LicenseArn": "arn:aws:license-manager::123456789012:license:l-exampleLicense12345",
                "UsageAllocations": [
                    {
                        "AllocatedUsageQuantity": 5000,
                        "Tags": [
                            { "Key": "user", "Value": "john" },
                            { "Key": "feature", "Value": "data-processing" },
                            { "Key": "job-name", "Value": "job11111" }
                        ]
                    },
                    {
                        "AllocatedUsageQuantity": 2500,
                        "Tags": [
                            { "Key": "user", "Value": "john" },
                            { "Key": "feature", "Value": "data-storage" },
                            { "Key": "cluster-name", "Value": "cluster11111" }
                        ]
                    },
                    {
                        "AllocatedUsageQuantity": 2500,
                        "Tags": [
                            { "Key": "user", "Value": "jane" },
                            { "Key": "feature", "Value": "data-storage" },
                            { "Key": "cluster-name", "Value": "cluster22222" }
                        ]
                    }
                ]
            },
            "MeteringRecordId": "8fjef98ejf",
            "Status": "Success"
        }
    ],
    "UnprocessedRecords": []
}
```
