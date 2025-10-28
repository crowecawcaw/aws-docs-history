# Barracuda XDR

Barracuda Networks is a trusted partner and leading provider of
cloud-first security solutions, protecting email, networks, data, and applications with
innovative solutions that grow and adapt with businesses’ journey.
Barracuda XDR is an open extended detection and response solution
that combines sophisticated technologies with a team of security analysts in our
security operations center (SOC). The Barracuda XDR platform analyzes
billions of raw events daily from 40+ integrated data sources, and together with extensive
threat detection rules that map to the MITRE ATT&CK® framework, it can detect
threats faster and reduce response time.

## AWS AppFabric audit log ingestion

considerations

The following sections describe the AppFabric output schema, output formats, and output
destinations to use with Barracuda XDR.

### Schema and format

Barracuda XDR supports the following AppFabric output schema
and formats:

- OCSF - JSON: AppFabric normalizes the data using the Open Cybersecurity
  Schema Framework (OCSF) and outputs the data in the JSON format.

### Output locations

Barracuda XDR supports receiving Audit Logs from Amazon
Security Lake. To send data from AppFabric to Barracuda XDR,
following the instructions below:

1. Send data to Amazon Security Lake: Configure AppFabric to send data to Amazon Security Lake
   through a Amazon Data Firehose. For more information, see [Amazon Security Lake](security-lake.md "security-lake.md").
2. Send data to Barracuda XDR: Configure
   Barracuda XDR to receive audit logs from
   Amazon Security Lake. For more information, see [Setting Up and Using Amazon Security Lake](https://campus.barracuda.com/product/xdr/doc/104366130/setting-up-and-using-amazon-web-services-security-lake/ "https://campus.barracuda.com/product/xdr/doc/104366130/setting-up-and-using-amazon-web-services-security-lake/").
