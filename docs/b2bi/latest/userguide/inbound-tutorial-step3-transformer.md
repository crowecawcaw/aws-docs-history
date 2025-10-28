# Step 3: Create an inbound

transformer

An inbound transformer defines how to convert X12 EDI documents to JSON or XML format.
It contains the mapping logic that extracts data from the structured EDI format and
transforms it into a more accessible JSON structure for your applications.

## Create sample files in Amazon S3

Before creating the transformer, you need to create sample input and output files
in your Amazon S3 buckets that will be used to generate the mapping.

### Create the input sample

file

###### To create the EDI input sample

1. Create a file named `sample-850-input.edi` with the
   following content:

```
ISA*00*          *00*          *ZZ*SENDER         *ZZ*RECEIVER       *230101*1200*U*00401*000000001*0*P*>~
GS*PO*SENDER*RECEIVER*20230101*1200*1*X*004010~
ST*850*0001~
BEG*00*SA*PO123456**20230101~
N1*ST*ACME CORPORATION~
N3*123 MAIN STREET~
N4*ANYTOWN*NY*12345*US~
PO1*1*10*EA*25.00**BP*WIDGET001*VN*WIDGET-A~
PID*F****PREMIUM WIDGET~
SE*8*0001~
GE*1*1~
IEA*1*000000001~
```

2. Upload this file to your input Amazon S3 bucket (for example,
   `s3://my-b2bi-input-bucket-your-account-id/sample-850-input.edi`).

### Create the output sample

file

###### To create the JSON output sample

1. Create a file named
   `sample-purchase-order-output.json` with the
   following content:

```
{
  "purchaseOrder": {
    "poNumber": "PO123456",
    "orderDate": "2023-01-01",
    "shipTo": {
      "name": "ACME CORPORATION",
      "address": "123 MAIN STREET",
      "city": "ANYTOWN",
      "state": "NY",
      "postalCode": "12345",
      "country": "US"
    },
    "lineItems": [
      {
        "lineNumber": "1",
        "quantity": "10",
        "unitOfMeasure": "EA",
        "unitPrice": "25.00",
        "productId": "WIDGET001",
        "description": "PREMIUM WIDGET"
      }
    ]
  }
}
```

2. Upload this file to your output Amazon S3 bucket (for example,
   `s3://my-b2bi-output-bucket-your-account-id/sample-purchase-order-output.json`).

## Create the transformer

An inbound transformer defines how to convert X12 EDI documents to JSON format. It
contains the mapping logic that extracts data from the structured EDI format and
transforms it into a more accessible JSON structure for your applications.

###### To create a transformer

1. In the AWS B2B Data Interchange console, choose **Transformers** from the
   navigation pane.
2. Choose **Create transformer**.
3. In the **Transformer details** section, enter:
   - **Transformer name**:
     `X12-850-to-JSON-Transformer`
   - **EDI direction**: Select
     **Inbound**

4. In the **Input details** section:
   - **X12 version**: Select
     **4010**
   - **X12 transaction set**: Select **850 -
     Purchase Order**

5. In the **Output details** section:
   - **Data format**: Select
     **JSON**

6. In the **Sample documents** section:
   - **Input sample**: Choose **Browse
     S3** and select the
     `sample-850-input.edi` file you created in
     your input bucket.
   - **Output sample**: Choose **Browse
     S3** and select the
     `sample-purchase-order-output.json` file you
     created in your output bucket.

7. Choose **Generate mapping** to create the initial
   transformation template.
8. Review the generated mapping in the **Mapping**
   section.
9. Set **Status** to **Active**.
10. Choose **Create transformer**.

## Required fields

- Transformer name
- EDI direction (must be Inbound)
- X12 version
- X12 transaction set
- Data format
- Status (must be Active to use in capabilities)
