

# Logz.io
<a name="logz-io"></a>

Logz.io helps cloud native businesses monitor and secure their environments via the [Logz.io](http://logz.io/) Open 360 Platform – transforming observability and security from a high-cost, low-value burden into a high-value, cost-efficient enabler of better business outcomes.

Logz.io Cloud SIEM directly addresses today’s leading security challenges – from data overload to the omnipresent cyber skills gap – via fast querying, multidimensional detection and deep customizable security content to help monitor and investigate across the full-expanse of your cloud environment – with no performance degradation, regardless of data volumes.

The Logz.io solution was purpose-built to deliver advanced threat analysis and investigation with less complexity and cost. Customers are backed by dedicated security analysts, threat content as a service and AI-backed capabilities purpose-built to help reduce noisy data and focus on the information that enables your team to rapidly prioritize real world threats.

## AWS AppFabric audit log ingestion considerations
<a name="logz-io-ingestion-considerations"></a>

The following sections describe the AppFabric output schema, output formats, and output destinations to use with Logz.io.

### Schema and format
<a name="logz-io-schema-format"></a>

Logz.io supports the following AppFabric output schema and formats:
+ Raw - JSON
  + AppFabric outputs data in the original schema used by the source application in the JSON format.
+ OCSF - JSON
  + AppFabric normalizes the data using the Open Cybersecurity Schema Framework (OCSF) and outputs the data in the JSON format.

### Output locations
<a name="logz-io-output-locations"></a>

Logz.io supports the following AppFabric output locations:
+ Amazon Data Firehose
  + To configure your Firehose delivery stream so that it sends data to Logz.io, follow the instructions in [Choose Logz.io for Your Destination](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-logz) in the *Amazon Data Firehose Developer Guide*.
+ Amazon Simple Storage Service (Amazon S3)
  + To configure Logz.io to receive data from the Amazon S3 bucket that contains your audit logs, follow the instructions in [Configure an Amazon S3 bucket](https://docs.logz.io/shipping/log-sources/s3-bucket.html) on the Logz.io website.