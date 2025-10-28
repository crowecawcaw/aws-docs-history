# Step 5: Create a partnership with

outbound EDI configuration

A partnership represents your trading relationship with a business partner. For
outbound EDI, the partnership requires extensive configuration of EDI headers, control
numbers, and formatting options that will be used to generate properly formatted EDI
documents for your trading partner.

###### Important

Outbound partnerships require significantly more configuration than inbound
partnerships. You must specify all interchange control header (ISA) and functional
group header (GS) values that your trading partner expects to receive.

###### To create an outbound partnership

1. In the AWS B2B Data Interchange console, choose **Partnerships**.
2. Choose **Create partnership**.
3. In the **Partnership details** section, enter:
   - **Partnership name**:
     `SupplierXYZ-Outbound-Partnership`
   - **Email**:
     `edi@supplierxyz.example.com`
   - **Profile**: Select
     **AcmeCorpOutboundProfile**
   - **Trading capabilities**: Select
     **Outbound-850-Generation**

4. In the **Inbound EDI configuration** section, leave the
   acknowledgment settings as default (this section is not used for outbound
   processing).
5. In the **Outbound EDI configuration** section, configure the
   EDI headers:
   1. **Interchange control header (ISA
      segment):**
      - **Interchange ID qualifier (ISA05)**:
        `ZZ`
      - **Interchange sender ID (ISA06)**:
        `ACMECORP`
      - **Interchange ID qualifier (ISA07)**:
        `ZZ`
      - **Interchange receiver ID (ISA08)**:
        `SUPPLIERXYZ`
      - **Repetition separator (ISA11)**:
        `U`
      - **Acknowledgment requested (ISA14)**:
        `0`
      - **Usage indicator (ISA15)**:
        `P`

   2. **Functional group header (GS
      segment):**
      - **Application sender's code (GS02)**:
        `ACMECORP`
      - **Application receiver's code (GS03)**:
        `SUPPLIERXYZ`
      - **GS-05 time format**: Select your preferred
        time format
      - **Responsible agency code (GS07)**:
        `X`

   3. **Control numbers:** Accept default
      values (starting at 1) for both interchange and group control
      numbers.
   4. **Delimiters (optional):** Leave as
      default unless your trading partner requires specific delimiters.
   5. **New Lines Formatting:** accept the
      default value of **One segment per line - add a new line
      character after each segment**.
   6. **EDI validation:** Leave
      **Enable outbound EDI validation** selected
      (recommended).

6. Optionally, add tags:
   - Key: `Partner`, Value:
     `SupplierXYZ`
   - Key: `DocumentType`, Value:
     `PurchaseOrder`
   - Key: `Direction`, Value:
     `Outbound`

7. Choose **Create partnership**.

## Required fields

- Partnership name
- Email address
- Profile selection
- Trading capabilities selection
- All ISA segment fields (ISA01-ISA15)
- All GS segment fields (GS01-GS08)
- Control number starting values

## Example data used

- Partnership name: SupplierXYZ-Outbound-Partnership
- Email: edi@supplierxyz.example.com
- Profile: AcmeCorpOutboundProfile
- Trading capability: Outbound-850-Generation
- Sender ID: ACMECORP
- Receiver ID: SUPPLIERXYZ
