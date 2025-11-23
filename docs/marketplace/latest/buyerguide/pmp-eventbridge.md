# AWS Marketplace Private Marketplace EventBridge events

Private marketplace administrators and buyers receive _events_ from
AWS Marketplace every time a buyer creates a request for a product. They also receive events when the
request is approved or declined. The events contain details such as product IDs and seller
names.

The topics in this section provide detailed information about the events listed in the following table.

| Action                                                                        | Event received            | More information                                                                              |
| ----------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------- |
| Buyer requests a product for their private marketplace                        | Product Request Created   | [New product request event](#event-new-product-requests "#event-new-product-requests")        |
| Administrator approves the product                                            | Product Request Approved  | [Product request approved event](#event-when-request-approved "#event-when-request-approved") |
| Administrator declines the product, or the system auto-declines after 30 days | Product Request Declined  | [Product request declined event](#event-request-declined "#event-request-declined")           |
| Buyer cancels a request for product for their Private Marketplace             | Product Request Cancelled | [Product request cancelled event](#event-request-cancelled "#event-request-cancelled")        |
| System auto-declines a product request after 30 days                          | Product Request Expired   | [Product request expired event](#event-request-expired "#event-request-expired")              |

## New product request event

When a buyer requests a product for their Private Marketplace catalog, the buyer and Private Marketplace administrators receive an event with the `Product Request Created` detail type.

The following example shows the event body for a `Product Request Created` event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Product Request Created",
  "source": "aws.private-marketplace",
  "account": "255182084545",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:255182084545:AWSMarketplace/Experience/exp-12345",
    "arn:aws:aws-marketplace:us-east-1:982534358349:AWSMarketplace/ProductProcurementRequest/prodprocreq-67890"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "expirationDate": "2022-11-01T13:12:22Z",
    "schemaVersion": "1.0.0",
    "product": {
        "id": "product-12345",
        "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/product-12345",
        "title": "MSP360 Backup for Google Workspace"
    },
    "manufacturer": {
        "name": "Test Vendor"
    },
    "experienceId": "exp-12345",
    "productProcurementRequestId": "prodprocreq-67890",
    "catalog": "AWSMarketplace",
    "requesterArn": "arn:aws:iam::255182084545:user/pmp-enduser"
  }
}
```

## Product request approved event

When a Private Marketplace administrator approves a product for a buyer's Private Marketplace catalog, the buyer and Private Marketplace administrators receive an event with the `Product Request Approved` detail type.

The following example shows the event body for a `Product Request Approved` event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Product Request Approved",
  "source": "aws.private-marketplace",
  "account": "255182084545",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:255182084545:AWSMarketplace/Experience/exp-12345",
    "arn:aws:aws-marketplace:us-east-1:982534358349:AWSMarketplace/ProductProcurementRequest/prodprocreq-67890"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "approvedDate": "2022-11-05T13:12:22Z",
    "schemaVersion": "1.0.0",
    "product": {
        "id": "product-12345",
        "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/product-12345",
        "title": "MSP360 Backup for Google Workspace"
    },
    "manufacturer": {
        "name": "Test Vendor"
    },
    "experienceId": "exp-12345",
    "productProcurementRequestId": "prodprocreq-67890",
    "catalog": "AWSMarketplace",
    "requesterArn": "arn:aws:iam::255182084545:user/pmp-enduser"
  }
}
```

## Product request declined event

When a Private Marketplace administrator declines a product addition, the buyer and Private Marketplace administrators receive an event with the `Product Request Declined` detail type.

The following example shows the event body for a `Product Request Declined` event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Product Request Declined",
  "source": "aws.private-marketplace",
  "account": "255182084545",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:255182084545:AWSMarketplace/Experience/exp-12345",
    "arn:aws:aws-marketplace:us-east-1:982534358349:AWSMarketplace/ProductProcurementRequest/prodprocreq-67890"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "declinedDate": "2022-11-05T13:12:22Z",
    "declinedCause": "REQUEST_EXPIRED",
    "schemaVersion": "1.0.0",
    "product": {
        "id": "product-12345",
        "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/product-12345",
        "title": "MSP360 Backup for Google Workspace"
    },
    "manufacturer": {
        "name": "Test Vendor"
    },
    "experienceId": "exp-12345",
    "productProcurementRequestId": "prodprocreq-67890",
    "catalog": "AWSMarketplace",
    "requesterArn": "arn:aws:iam::255182084545:user/pmp-enduser"
  }
}
```

## Product request cancelled event

When a Private Marketplace buyer cancels a product request, the buyer and Private Marketplace administrators receive an event with the `Product Request Cancelled` detail type.

The following example shows the event body for a `Product Request Cancelled` event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Product Request Cancelled",
  "source": "aws.private-marketplace", // Event is specific to Private Marketplace
  "account": "982534358349",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:255182084545:AWSMarketplace/Experience/exp-12345",
    "arn:aws:aws-marketplace:us-east-1:982534358349:AWSMarketplace/ProductProcurementRequest/prodprocreq-67890"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "cancelledDate": "2022-11-05T13:12:22Z",
    "schemaVersion": "1.0.0",
    "product": {
        "id": "prod-xpaczqtfx7xqe",
        "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/product-12345",
        "title": "MSP360 Backup for Google Workspace"
    },
    "manufacturer": {
        "name": "Test Vendor"
    },
    "experienceId": "exp-12345",
    "productProcurementRequestId": "prodprocreq-67890",
    "catalog": "AWSMarketplace",
    "requesterArn": "arn:aws:iam::982534358349:enduser1"
  }
}
```

## Product request expired event

When a Private Marketplace product request expires after 30 days, the buyer and Private Marketplace administrators receive an event with the `Product Request Expired` detail type.

The following example shows the event body for a `Product Request Expired` event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Product Request Expired",
  "source": "aws.private-marketplace",
  "account": "255182084545",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:255182084545:AWSMarketplace/Experience/exp-12345",
    "arn:aws:aws-marketplace:us-east-1:982534358349:AWSMarketplace/ProductProcurementRequest/prodprocreq-67890"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "declinedDate": "2022-11-05T13:12:22Z",
    "declinedCause": "REQUEST_EXPIRED",
    "schemaVersion": "1.0.0",
    "product": {
        "id": "product-12345",
        "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/product-12345",
        "title": "MSP360 Backup for Google Workspace"
    },
    "manufacturer": {
        "name": "Test Vendor"
    },
    "experienceId": "exp-12345",
    "productProcurementRequestId": "prodprocreq-67890",
    "catalog": "AWSMarketplace",
    "requesterArn": "arn:aws:iam::255182084545:user/pmp-enduser"
  }
}
```
