# Outbound EDI tutorial

This tutorial guides you through setting up an outbound B2B Data Interchange workflow
using AWS B2B Data Interchange. You'll learn how to transform JSON data into X12 EDI documents (specifically
850 Purchase Orders) for sending to your trading partners.

## Converting JSON to EDI X12 documents

Learn how to automatically convert JSON purchase orders into X12 850 EDI documents
that you can send to your suppliers. This tutorial shows you how to set up an automated
workflow that transforms JSON files in Amazon S3 into properly formatted EDI
documents.

Here's how the workflow operates:

1. Your procurement system creates a purchase order in JSON format and uploads it
   to Amazon S3.
2. AWS B2B Data Interchange detects the new file and converts it to an X12 850 EDI
   document.
3. The converted document is saved to your output directory, ready for
   transmission to your supplier through Transfer Family or another EDI method.

###### Note

This tutorial covers outbound EDI (JSON to X12). For inbound EDI (X12 to JSON),
see [Inbound EDI tutorial](inbound-edi-tutorial.md "inbound-edi-tutorial.md").

By completing this tutorial, you'll:

- Create a business profile for your organization
- Set up an outbound transformer to convert JSON to X12 850 EDI
- Configure a trading capability that automates the transformation
  process
- Establish a partnership with outbound EDI settings
- Test the complete end-to-end workflow

By completing this tutorial, you'll create a business profile representing your
organization, an outbound transformer that converts JSON data to X12 850 EDI documents, a
trading capability that automates the transformation process, a partnership with outbound
EDI configuration, and a complete end-to-end workflow for generating EDI documents.

This setup will automatically monitor your Amazon S3 input directory for JSON files and
transform them into X12 EDI documents, placing the EDI output in your designated output
directory for transmission to trading partners.

###### Tip

Before starting this tutorial, review the [Prerequisites](b2b-tutorials.md#tutorial-prerequisites "b2b-tutorials.md#tutorial-prerequisites") section.

###### Topics

- [Step 1: Setting up Amazon S3
  buckets](outbound-tutorial-step1-s3-setup.md "outbound-tutorial-step1-s3-setup.md")
- [Step 2: Creating your business
  profile](outbound-tutorial-step2-profile.md "outbound-tutorial-step2-profile.md")
- [Step 3: Creating an outbound
  transformer](outbound-tutorial-step3-transformer.md "outbound-tutorial-step3-transformer.md")
- [Step 4: Create a trading
  capability](outbound-tutorial-step4-capability.md "outbound-tutorial-step4-capability.md")
- [Step 5: Create a partnership with
  outbound EDI configuration](outbound-tutorial-step5-partnership.md "outbound-tutorial-step5-partnership.md")
- [Step 6: Test your outbound
  configuration](outbound-tutorial-step6-testing.md "outbound-tutorial-step6-testing.md")
- [Step 7: Monitor your outbound
  workflow](outbound-tutorial-step7-monitoring.md "outbound-tutorial-step7-monitoring.md")
- [Cleanup steps](outbound-tutorial-cleanup.md "outbound-tutorial-cleanup.md")
- [Next steps](outbound-tutorial-conclusion.md "outbound-tutorial-conclusion.md")
