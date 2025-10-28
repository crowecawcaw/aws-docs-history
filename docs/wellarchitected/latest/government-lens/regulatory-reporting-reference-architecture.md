# Regulatory reporting reference architecture

Every government institution deals with volumes of information
for legislative or regulatory reporting. Static legacy
infrastructure and inefficient reporting processes can make
reporting costly and prevent customers from responding quickly
to regulatory changes. Building a reporting data lake on AWS and
using the rich set of services available can address many of the
issues that complicate regulatory reporting, such as data
residing in disconnected silos and distributed ETL processes.
After customers integrate reporting data into a consistent
dataset or data pipeline, they can use that data to gain
additional insights through advanced analytics and machine
learning. 

Data lake architectures supporting these government services use
cases share the following characteristics: 

- They implement data quality, integrity, and lineage into the
  ingest and processing pipelines.
- They require that data is encrypted at rest and in transit.
- They mask or tokenize personally identifiable information (PII) data to help align
  with regulatory requirements (for example, [EU General
  Data Protection Regulation](https://gdpr-info.eu/ "https://gdpr-info.eu/")).
- They use data catalogs with fine-grained access control and
  entitlements.

![Reference architecture diagram showing a regulatory reporting solution regulatory reporting solution to provide structured output data from a variety of disparate sources. The architecture describes ingesting files and data from on-premises and external sources.](images/reg-reporting.png)

_Figure 3: Reference architecture for a regulatory reporting
solution_
