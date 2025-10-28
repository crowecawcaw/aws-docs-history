# Work with dataflows

AWS Ground Station uses a _node_ and _edge_ relationship to
construct _dataflows_ to enable stream processing of your data. Each node is
represented by a _config_ which describes its expected processing. To
illustrate this concept, consider a dataflow of `antenna-downlink` to a
`s3-recording`. The `antenna-downlink` node represents the analog to digital
transformation of the radio frequency spectrum per the defined parameters on the config. The
`s3-recording` represents a compute node which will receive incoming data and store it in your S3
bucket. The resulting dataflow is an asynchronous data delivery of digitized RF data to an S3
bucket based on your specifications.

Within your mission profile, you can create many dataflows to meet your needs. The following
sections describe how to set up your other AWS resources to be used with AWS Ground Station and offers
recommendations for constructing dataflows. For detailed information on how each node behaves,
including if it is considered a source or destination node, please see
[Use AWS Ground Station Configs](how-it-works.md "how-it-works.md").

###### Topics

- [AWS Ground Station data plane interfaces](#dataflows.interfaces "#dataflows.interfaces")
- [Use cross-region data delivery](dataflows.md "dataflows.md")
- [Set up and configure Amazon S3](dataflows.md "dataflows.md")
- [Set up and configure Amazon VPC](dataflows.md "dataflows.md")
- [Set up and configure Amazon EC2](dataflows.md "dataflows.md")

## AWS Ground Station data plane interfaces

The resulting data structure of your chosen dataflow depends on the source of the
dataflow. Details of these formats are provided to you during the onboarding of your
satellites. The following summarizes the formats used for each type of dataflow.

- **antenna-downlink**
  - (Bandwidth less-than-or-equal-to 40MHz) data is delivered as [VITA-49 Signal Data/IP](https://www.vita.com/Standards "https://www.vita.com/Standards") Format packets.
  - (Bandwidth greater-than 40MHz) data is delivered as AWS Ground Station Class 2
    packets.

- **antenna-downlink-demod-decode**
  - Data is delivered as Demodulated/Decoded Data/IP Format packets.

- **antenna-uplink**
  - Data must be delivered as [VITA-49 Signal Data/IP](https://www.vita.com/Standards "https://www.vita.com/Standards") Format packets.

- **antenna-uplink-echo**
  - Data is delivered as [VITA-49 Signal Data/IP](https://www.vita.com/Standards "https://www.vita.com/Standards") Format packets.
