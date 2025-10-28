# Step 6: Test your outbound

configuration

Testing ensures your complete outbound workflow functions correctly before processing
real business documents. This validates that all components work together and that your
JSON data is properly transformed into valid X12 EDI documents.

###### To test your outbound configuration

1. Create a test JSON file named `test-purchase-order.json`
   with this content:

```
{
  "purchaseOrder": {
    "poNumber": "TEST-PO-001",
    "orderDate": "2023-01-20",
    "buyerInfo": {
      "name": "ACME CORPORATION",
      "address": "123 TEST STREET",
      "city": "TESTTOWN",
      "state": "NY",
      "postalCode": "10001",
      "country": "US"
    },
    "supplierInfo": {
      "name": "SUPPLIER XYZ",
      "address": "789 SUPPLIER AVENUE",
      "city": "SUPPLIERTOWN",
      "state": "CA",
      "postalCode": "90210",
      "country": "US"
    },
    "lineItems": [
      {
        "lineNumber": "1",
        "quantity": "15",
        "unitOfMeasure": "EA",
        "unitPrice": "29.99",
        "productId": "TEST-ITEM-001",
        "description": "TEST PRODUCT ITEM"
      }
    ]
  }
}
```

2. Upload the test file to your input bucket:
   1. Navigate to
      `my-b2bi-outbound-input-bucket-`your-account-id``
      in the Amazon S3 console.
   2. Create the required folder structure for your trading capability and
      partner:
      1. Choose **Create folder**.
      2. Enter the capability ID folder name (for example:
         `ca-a1b2c3d4e5f6g7h8i`).
      3. Choose **Create folder**.
      4. Navigate into the capability folder, then choose
         **Create folder** again.
      5. Enter the trading partner ID folder name (for example:
         `tp-a1b2c3d4e5f6g7h8i`).
      6. Choose **Create folder**.

   3. Navigate into the trading partner folder (the final path should be:
      `ca-[capability-id]/tp-[partner-id]/`).
   4. Choose **Upload**.
   5. Select your `test-purchase-order.json` file.
   6. Choose **Upload**.###### Note

The correct folder structure is
`ca-[capability-id]/tp-[partner-id]/`. You can find
the exact path in the B2BI console under **Partnerships** →
**Assigned trading capabilities** section, which shows
a direct link to the input directory with the correct folder
structure. 3. Monitor the transformation:

    * Wait 2-3 minutes for processing
    * Check your output bucket for the generated X12 EDI file
    * The output will be in a directory structure like:
     ``partnership-id`/`capability-id`/processed/`

4. Verify the X12 EDI output contains properly formatted purchase order data with
   correct ISA and GS headers.

## Expected results

- X12 EDI file appears in output bucket within 2-3 minutes
- File contains properly formatted X12 850 EDI document
- ISA and GS headers match your partnership configuration
- Control numbers are properly incremented
- CloudWatch logs show successful transformation (if logging enabled)
