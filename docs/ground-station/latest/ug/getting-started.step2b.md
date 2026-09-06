

# Plan your telemetry
<a name="getting-started.step2b"></a>

 AWS Ground Station telemetry is an optional feature that streams metrics from AWS Ground Station antennas to your AWS account during satellite contacts. This allows you to monitor contact performance in near real-time and build custom monitoring solutions. 

 With AWS Ground Station telemetry, metrics from AWS Ground Station antennas are streamed directly to your account. Telemetry data begins streaming at contact start and continues throughout the contact duration. The telemetry data is delivered to your account in near real-time as it is sampled from the antenna hardware. Once received, you can process the data using your own post-processing software or use other AWS services like Amazon Data Firehose or AWS Lambda. 

![Diagram showing telemetry data flow from AWS Ground Station to Amazon Kinesis Data Streams within AWS Cloud.](http://docs.aws.amazon.com/ground-station/latest/ug/images/telemetry.png)


 In the next step, you'll create the configs needed for your mission profile. If you want to enable telemetry, you'll create a *Telemetry Sink Config* in addition to your tracking config and dataflow configs. For detailed setup instructions, see [Set up telemetry](telemetry.setup.md). 

 For more information about TelemetrySinkConfig, see [Telemetry Sink Config](how-it-works.config.md#how-it-works.config-telemetry-sink). 