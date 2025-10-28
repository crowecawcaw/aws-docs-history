# Step 3: Creating an outbound

transformer

An outbound transformer defines how to convert JSON data to X12 EDI format. It
contains the mapping logic that takes structured JSON purchase order data and transforms
it into properly formatted X12 850 EDI documents for transmission to your trading
partners.

Before creating the transformer, you must create sample documents in the buckets you
created earlier.

###### To create sample documents

1.  Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  Create the input sample file:
    1. Save the following JSON code to a file named
       `sample-purchase-order.json`:

    ```
    {
      "purchaseOrder": {
        "poNumber": "PO789012",
        "orderDate": "2023-01-15",
        "buyerInfo": {
          "name": "ACME CORPORATION",
          "address": "*** CORPORATE BLVD",
          "city": "BUSINESSTOWN",
          "state": "TX",
          "postalCode": "*****",
          "country": "US"
        },
        "supplierInfo": {
          "name": "SUPPLIER XYZ",
          "address": "*** VENDOR STREET",
          "city": "VENDORVILLE",
          "state": "CA",
          "postalCode": "*****",
          "country": "US"
        },
        "lineItems": [
          {
            "lineNumber": "1",
            "quantity": "25",
            "unitOfMeasure": "EA",
            "unitPrice": "45.00",
            "productId": "GADGET001",
            "description": "PREMIUM GADGET"
          },
          {
            "lineNumber": "2",
            "quantity": "10",
            "unitOfMeasure": "EA",
            "unitPrice": "75.50",
            "productId": "TOOL002",
            "description": "PROFESSIONAL TOOL"
          }
        ]
      }
    }
    ```

    2. Upload this file to your input bucket:
       `s3://my-b2bi-outbound-input-`account-id``.

3.  Create the output sample file:

        1. Save the following EDI code to a file named
         `sample-850-output.edi`:



        ```
        ISA*00*          *00*          *ZZ*ACMECORP       *ZZ*SUPPLIERXYZ    *230115*1400*U*00401*000000001*0*P*>~
        GS*PO*ACMECORP*SUPPLIERXYZ*20230115*1400*1*X*004010~
        ST*850*0001~
        BEG*00*SA*PO789012**20230115~
        N1*BY*ACME CORPORATION~
        N3*789 CORPORATE BLVD~
        N4*BUSINESSTOWN*TX*75001*US~
        N1*ST*SUPPLIER XYZ~
        N3**** VENDOR STREET~
        N4*VENDORVILLE*CA*******US~
        PO1*1*25*EA*45.00**BP*GADGET001*VN*GADGET001~
        PID*F****PREMIUM GADGET~
        PO1*2*10*EA*75.50**BP*TOOL002*VN*TOOL002~
        PID*F****PROFESSIONAL TOOL~
        SE*13*0001~
        GE*1*1~
        IEA*1*000000001~

        ```
        2. Upload this file to your input bucket:
         `s3://my-b2bi-outbound-input-`account-id``.

    Now that you have your sample files ready, create your outbound transformer.

###### To create an outbound transformer

1. In the B2B Data Interchange console, choose **Transformers** from the
   navigation pane.
2. Choose **Create transformer**.
3. In **Transformer details**, enter:
   - **Transformer name**:
     `JSON-to-X12-850-Transformer`
   - **EDI direction**: Choose **Outbound
     EDI**

4. In **Input details**, for **Data format**,
   choose **JSON**.
5. In **Output details**, select:
   - **X12 version**: **4010**
   - **X12 transaction set**: **850**
     (Purchase Order)

6. In **Sample documents**:
   - **Input sample**: Choose **Browse
     S3**, navigate to your input bucket
     (`s3://my-b2bi-outbound-input-`account-id``),
and select `sample-purchase-order.json`.
   - **Output sample**: Choose **Browse
     S3**, navigate to your input bucket
     (`s3://my-b2bi-outbound-input-`account-id``),
and select `sample-850-output.edi`.

7. Choose **Next**.
8. On the **Mapping configuration** page, choose
   **Generate mapping** to create the initial transformation
   template.

###### Tip

Before generating a mapping, ensure that you've enabled the Amazon Bedrock models as
described in [Prerequisites for using the AWS B2B Data Interchange generative AI-assisted EDI mapping capability](generative-ai-assisted-mapping.md#ai-assist-prereq "generative-ai-assisted-mapping.md#ai-assist-prereq"). 9. Review the generated mapping in the **Mapping**
section. 10. Choose **Generate EDI output preview**. Examine the preview
and, if necessary, use the **Mapping editor** to adjust your
mappings. 11. Check the **EDI output preview errors** section. If any
errors are listed, update the mapping to correct them. 12. When your mappings are acceptable, choose **Next**. 13. On the **Review and create** page, review your transformer
configuration. If everything looks correct, choose
**Save**. 14. Select your new transformer from the list and choose **Activate
transformer**. In the verification dialog box, enter
`Activate` to set the transformer's status to
**Active**.
Your outbound transformer is now active. Note that you can't edit it anymore. To
change any settings, you must delete this transformer and create a new one.

## Configuration summary

Required fields

- Transformer name
- EDI direction (must be Outbound)
- X12 version
- X12 transaction set
- Input and output sample documents
- Status (must be Active to use in capabilities)

Example values

- Transformer name:
  `JSON-to-X12-850-Transformer`
- EDI direction: Outbound EDI
- X12 version: 4010
- X12 transaction set: 850 (Purchase Order)
