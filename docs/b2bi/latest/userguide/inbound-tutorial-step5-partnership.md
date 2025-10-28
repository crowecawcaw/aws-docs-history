# Step 5: Create a

partnership

A partnership represents your trading relationship with a business partner. It
combines your profile with trading capabilities and defines how to handle inbound EDI
documents, including acknowledgment generation settings.

###### To create a partnership

1. In the AWS B2B Data Interchange console, choose **Partnerships**.
2. Choose **Create partnership**.
3. In the **Partnership details** section, enter:
   - **Partnership name**:
     `SupplierABC-Partnership`
   - **Email**:
     `edi@supplierabc.example.com`
   - **Profile**: Select
     **AcmeCorpProfile**
   - **Trading capabilities**: Select
     **Inbound-850-Processing**

4. In the **Inbound EDI configuration** section:
   - **TA1 Technical Acknowledgments**: Select
     **Do not generate**
   - **Functional (997 and 999) Acknowledgments**: Select
     **Generate 997**
   - **Include AK2 loop**: Leave unchecked

5. Optionally, add tags:
   - Key: `Partner`, Value:
     `SupplierABC`
   - Key: `DocumentType`, Value:
     `PurchaseOrder`

6. Choose **Create partnership**.

## Required fields

- Partnership name
- Email address
- Profile selection
- Trading capabilities selection

## Example data used

- Partnership name: SupplierABC-Partnership
- Email: edi@supplierabc.example.com
- Profile: AcmeCorpProfile
- Trading capability: Inbound-850-Processing
