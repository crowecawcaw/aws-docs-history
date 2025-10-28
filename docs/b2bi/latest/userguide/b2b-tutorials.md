# AWS B2B Data Interchange: tutorials

This chapter provides complete tutorials for both inbound and outbound EDI processing
using AWS B2B Data Interchange. Choose the tutorial that matches your use case:

- **Outbound EDI Tutorial:** Generate X12 EDI documents
  from your internal JSON data for sending to trading partners: [Outbound EDI tutorial](outbound-edi-tutorial.md "outbound-edi-tutorial.md").
- **Inbound EDI Tutorial:** Transform incoming X12 EDI
  documents from trading partners into JSON format for your internal systems: [Inbound EDI tutorial](inbound-edi-tutorial.md "inbound-edi-tutorial.md").
  Both tutorials use the same foundational concepts and can share resources like profiles.
  You can implement one or both workflows depending on your business requirements. Many of the
  steps are similar between tutorials, with the key differences being the transformer
  configuration (direction and sample data) and partnership settings (outbound requires
  additional EDI header configuration).

## Prerequisites

Before you begin either tutorial, ensure you have the following:

### AWS account

requirements

- An active AWS account with administrative privileges
- Access to the AWS Management Console
- Billing information configured for your AWS account

### Technical prerequisites

- Basic understanding of Electronic Data Interchange (EDI) concepts
- Familiarity with X12 transaction sets (particularly 850 Purchase Orders
  for these tutorials)
- Knowledge of JSON data formats
- Understanding of Amazon S3 bucket operations
- Understanding of EDI workflow concepts and trading partner requirements
  (specific requirements differ between inbound and outbound
  processing)

###### Note

**Direction-specific knowledge:** For outbound
EDI, you'll need additional understanding of EDI header configuration (ISA and
GS segments) and control number management. For inbound EDI, focus on
understanding how to consume transformed JSON data in your downstream
applications.

### Required AWS services

access

- AWS B2B Data Interchange service access in your chosen region
- Amazon S3 service access for input and output buckets
- CloudWatch for monitoring (optional but recommended)
- Amazon EventBridge for event notifications (optional but recommended)

### Sample data

You'll need sample files for testing your transformers. Each tutorial provides
specific examples:

- **Inbound tutorial:** Sample X12 850 EDI
  input and corresponding JSON output
- **Outbound tutorial:** Sample JSON purchase
  order input and corresponding X12 850 EDI output

## Understanding the use cases

Each tutorial addresses a specific business scenario for EDI processing:

- **Inbound EDI scenario:** Transform incoming X12 EDI documents from trading partners into JSON format for your internal systems. See the [Inbound EDI tutorial](inbound-edi-tutorial.md "inbound-edi-tutorial.md") for detailed workflow and setup instructions.
- **Outbound EDI scenario:** Generate X12 EDI documents from your internal JSON data for sending to trading partners. See the [Outbound EDI tutorial](outbound-edi-tutorial.md "outbound-edi-tutorial.md") for detailed workflow and setup instructions.

## What you'll create

Both tutorials guide you through creating the same core AWS B2B Data Interchange components,
configured for different directions:

- **Business Profile:** Stores your organization's
  contact information and serves as the foundation for trading partnerships
- **Transformer:** Defines the mapping logic for
  converting between X12 EDI and JSON formats
- **Trading Capability:** Connects your transformer
  to Amazon S3 directories and automates the processing workflow
- **Partnership:** Represents your trading
  relationship with business partners and defines processing configurations

The key difference is in the configuration: inbound transformers convert X12 EDI to
JSON, while outbound transformers convert JSON to X12 EDI. Outbound partnerships also
require extensive EDI header configuration for generating properly formatted
documents.
