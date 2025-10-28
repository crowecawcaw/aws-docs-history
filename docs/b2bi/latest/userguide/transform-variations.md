# Transforming and generating EDI

There are multiple ways to transform or generate X12 EDI in AWS B2B Data Interchange. This topic describes
the various ways you can create and configure inbound and outbound transformations.

- _Inbound EDI_: you receive an X12 EDI document from your
  trading partner. AWS B2B Data Interchange converts this X12 EDI document into a JSON or XML
  formatted data file with a service-defined structure. You can optionally apply a
  mapping—written in JSONata or XSLT—to produce a custom JSON or XML formatted data
  file.
- _Outbound EDI_: you have a JSON or XML formatted data file
  containing information that you wish to incorporate into an X12 EDI document that
  will be sent to your trading partner. You can align your JSON or XML formatted data
  file to conform with the service-defined structure directly, or you can apply a
  mapping in JSONata or XSLT to convert your custom JSON or XML into the
  service-defined structure necessary to produce an outbound X12 EDI document.
  As a prerequisite, you must set up bucket policies for the Amazon S3 buckets that you use with
  B2B Data Interchange, as described in [Configuring S3 bucket policies](b2bi-prereq.md#bucket-policy-configuration "b2bi-prereq.md#bucket-policy-configuration").

###### Topics

- [Generative AI-assisted EDI mapping](generative-ai-assisted-mapping.md "generative-ai-assisted-mapping.md")
- [Inbound EDI](transform-inbound-variations.md "transform-inbound-variations.md")
- [Outbound EDI](transform-outbound-variations.md "transform-outbound-variations.md")
