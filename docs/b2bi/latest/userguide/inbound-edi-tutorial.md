# Inbound EDI tutorial

This tutorial guides you through setting up an inbound B2B Data Interchange workflow using
AWS B2B Data Interchange. You'll learn how to transform incoming X12 EDI documents (specifically 850
Purchase Orders) into JSON format, making them easier to process in your downstream
applications.

By the end of this tutorial, you'll have created a business profile representing your
organization, a transformer that converts X12 850 EDI documents to JSON, a trading
capability that automates the transformation process, a partnership representing your
trading relationship, and a complete end-to-end workflow for processing EDI
documents.

This setup will automatically monitor your Amazon S3 input directory and transform any incoming
EDI documents, placing the JSON output in your designated output directory.

###### Tip

Before starting this tutorial, review the [Prerequisites](b2b-tutorials.md#tutorial-prerequisites "b2b-tutorials.md#tutorial-prerequisites") section.

###### Topics

- [Inbound EDI use case](#inbound-use-case "#inbound-use-case")
- [Step 1: Set up your Amazon S3
  infrastructure](inbound-tutorial-step1-s3-setup.md "inbound-tutorial-step1-s3-setup.md")
- [Step 2: Create your business
  profile](inbound-tutorial-step2-profile.md "inbound-tutorial-step2-profile.md")
- [Step 3: Create an inbound
  transformer](inbound-tutorial-step3-transformer.md "inbound-tutorial-step3-transformer.md")
- [Step 4: Create a trading
  capability](inbound-tutorial-step4-capability.md "inbound-tutorial-step4-capability.md")
- [Step 5: Create a
  partnership](inbound-tutorial-step5-partnership.md "inbound-tutorial-step5-partnership.md")
- [Step 6: Test your inbound
  configuration](inbound-tutorial-step6-testing.md "inbound-tutorial-step6-testing.md")
- [Step 7: Monitor your inbound
  workflow](inbound-tutorial-step7-monitoring.md "inbound-tutorial-step7-monitoring.md")
- [Testing notes - Documentation team
  validation](inbound-tutorial-testing-notes.md "inbound-tutorial-testing-notes.md")
- [Cleanup steps](inbound-tutorial-cleanup.md "inbound-tutorial-cleanup.md")
- [Next steps](#inbound-tutorial-conclusion "#inbound-tutorial-conclusion")

## Inbound EDI use case

**Inbound EDI scenario:** Your trading partners send you
purchase orders in standard X12 850 EDI format. Your internal systems need this data in
JSON format for processing. This tutorial shows you how to automatically transform
incoming X12 EDI documents into structured JSON data that your applications can easily
consume.

**Business workflow:** When a trading partner sends you
an X12 850 purchase order (stored in Amazon S3), AWS B2B Data Interchange automatically transforms it into
JSON format and places it in your output directory, ready for processing by your
internal systems such as order management, inventory, or ERP applications.

###### Note

This tutorial focuses on _inbound_ EDI (X12 EDI → JSON). If you
need to generate _outbound_ EDI documents (JSON → X12 EDI), see
[Outbound EDI tutorial](outbound-edi-tutorial.md "outbound-edi-tutorial.md").

## Next steps

This tutorial provides a complete foundation for using AWS B2B Data Interchange. You can extend this
setup by adding more transaction sets, creating outbound transformations, or integrating
with other AWS services for advanced workflows.

For additional learning resources, see:

- [AWS B2B Data Interchange concepts](b2bi-concepts.md "b2bi-concepts.md") for detailed
  information about AWS B2B Data Interchange components
- [Supported X12 transaction sets](x12-transaction-sets.md "x12-transaction-sets.md")
  for supported transaction sets
- For a self-paced learning experience, go through the [EDI document exchange
  with AWS B2B Data Interchange Workshop](https://catalog.workshops.aws/getting-started-b2b-data-interchange/ "https://catalog.workshops.aws/getting-started-b2b-data-interchange/"), created by the B2B Data Interchange service team. In this workshop, you learn
  how to receive and transform EDI documents from your business partners using AWS B2B Data Interchange and
  AWS Transfer Family.
