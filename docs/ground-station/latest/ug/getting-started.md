# Understand next steps

Now that you have an onboarded satellite and a valid mission profile, you are ready to
schedule contacts and communicate with your satellite with AWS Ground Station.

You can schedule a contact in one of the following ways:

- The [AWS Ground Station console](https://console.aws.amazon.com/groundstation "https://console.aws.amazon.com/groundstation").
- The AWS CLI
  [reserve-contact](../../../cli/latest/reference/groundstation/reserve-contact.md "../../../cli/latest/reference/groundstation/reserve-contact.md") command.
- The AWS SDK.
  [ReserveContact](../APIReference/API_ReserveContact.md "../APIReference/API_ReserveContact.md") API.

For information about how AWS Ground Station tracks the trajectory of your satellite and how that information
is used, please reference [Understand how AWS Ground Station uses ephemerides](ephemeris.md "ephemeris.md").

AWS Ground Station maintains a number of preconfigured CloudFormation templates to make getting started with the
service easier. See [Example mission profile configurations](examples.md "examples.md") for examples of how
AWS Ground Station can be used.

Processing the digital intermediate frequency data, or the demodulated and decoded data provided
to you from AWS Ground Station will depend on your specific use case. The following blog posts can help you
to understand some of the options available to you:

- [Automated Earth observation using AWS Ground Station Amazon S3 data delivery](https://aws.amazon.com/blogs/publicsector/automated-earth-observation-aws-ground-station-amazon-s3-data-delivery "https://aws.amazon.com/blogs/publicsector/automated-earth-observation-aws-ground-station-amazon-s3-data-delivery") (and it's associated GitHub repository [awslabs/aws-groundstation-eos-pipeline](https://github.com/awslabs/aws-groundstation-eos-pipeline "https://github.com/awslabs/aws-groundstation-eos-pipeline"))
- [Virtualizing the satellite ground segment with AWS](https://aws.amazon.com/blogs/publicsector/virtualizing-satellite-ground-segment-aws/ "https://aws.amazon.com/blogs/publicsector/virtualizing-satellite-ground-segment-aws/")
- [Earth observation using AWS Ground Station: A how to guide](https://aws.amazon.com/blogs/publicsector/earth-observation-using-aws-ground-station/ "https://aws.amazon.com/blogs/publicsector/earth-observation-using-aws-ground-station/")
- [Building high-throughput satellite data downlink architectures with AWS Ground Station WideBand DigIF and Amphinicy Blink SDR](https://aws.amazon.com/blogs/publicsector/building-high-throughput-satellite-data-downlink-architectures-aws-ground-station-wideband-digif-amphinicy-blink-sdr/ "https://aws.amazon.com/blogs/publicsector/building-high-throughput-satellite-data-downlink-architectures-aws-ground-station-wideband-digif-amphinicy-blink-sdr/") (and it's associated GitHub repository [aws-samples/aws-groundstation-wbdigif-snpp](https://github.com/aws-samples/aws-groundstation-wbdigif-snpp "https://github.com/aws-samples/aws-groundstation-wbdigif-snpp"))
