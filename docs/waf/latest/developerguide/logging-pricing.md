**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Pricing for logging protection pack (web ACL) traffic information

This section explains the pricing considerations for using protection pack (web ACL) traffic logs.

You are charged for logging protection pack (web ACL) traffic information according to the costs associated
with each log destination type. These charges are in addition to the charges for using
AWS WAF. Your costs can vary depending on factors such as the destination type
that you choose and the amount of data that you log.

The following provides links to the pricing information for each logging destination
type:

- **CloudWatch Logs** – The charges are for vended
  log delivery. See [Amazon CloudWatch Logs Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). Under **Paid
  Tier**, choose the **Logs** tab, and then under
  **Vended Logs**, see the information for **Delivery
  to CloudWatch Logs**.
- **Amazon S3 buckets** – The Amazon S3 charges are
  the combined charges for CloudWatch Logs vended log delivery to the Amazon S3 buckets and for
  using Amazon S3.
  - For Amazon S3, see [Amazon S3
    Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").
  - For CloudWatch Logs vended log delivery to the Amazon S3, see [Amazon CloudWatch Logs Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). Under
    **Paid Tier**, choose the
    **Logs** tab, and then under **Vended
    Logs**, see the information for **Delivery to
    S3**

- **Firehose** – See [Amazon Data Firehose Pricing](https://aws.amazon.com/kinesis/data-firehose/pricing/ "https://aws.amazon.com/kinesis/data-firehose/pricing/").
  For information about AWS WAF pricing, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").
