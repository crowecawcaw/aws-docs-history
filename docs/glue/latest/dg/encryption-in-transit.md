# Encrypting data in transit

AWS provides Transport Layer Security (TLS) encryption for data in motion. You can
configure encryption settings for crawlers, ETL jobs, and development endpoints using
[security
configurations](console-security-configurations.md "console-security-configurations.md") in AWS Glue. You can turn on AWS Glue Data Catalog encryption via the
settings for the Data Catalog.

As of September 4, 2018, AWS KMS (_bring your own key_ and
_server-side encryption_) for AWS Glue ETL and the AWS Glue Data Catalog is
supported.
