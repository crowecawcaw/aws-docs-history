# MIDAPERF01-BP02 Compress, sample and summarize data at edge, before sending to the cloud

environment

In manufacturing environments, IoT devices and sensors often generate massive volumes of
high-frequency data that can overwhelm networking, processing, and storage resources.

**Desired outcome:** Reduce amount of data flowing from
on-premises to cloud by summarizing time series machine data, for example average temperature
over a time period instead of raw temperature values every second. This allows for quicker
data processing long term for trending insights.

**Common anti-patterns:**

- Sending raw, unprocessed data streams directly to the cloud
- Ignoring data compression opportunities
- Not implementing edge-level data processing
- Overwhelming network bandwidth with high-frequency data

- Creating unnecessary network congestion
- Ignoring data transmission timing optimization
- Bypassing gateway-level processing capabilities
- Not using MQTT topic filtering
- Skipping data summarization strategies

**Benefits of establishing this best practice:**

- Less processing time processing and querying long term data
- Less time transmitting data to cloud
- Reduced storage costs
- Reduced network congestion to cloud

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

To reduce network traffic and overhead to allow faster processing:

1. Configure small data processing applications to summarize data on your gateway
   devices using AWS IoT Greengrass components
   1. **Manufacturing example:** Deploy AWS IoT Greengrass on factory floor gateways to
      run edge analytics components that process real-time data from CNC machines,
      conveyor belt sensors, and quality control cameras, summarizing production metrics
      like throughput rates, defect counts, and equipment utilization before sending to
      the cloud.

2. Subscribe to direct topics through MQTT of machine data, then use components to
   summarize and re-publish data on a new topic that is routed to AWS IoT Core or SiteWise.
   1. **Industrial example:** Use AWS IoT Greengrass components to subscribe to MQTT
      topics from industrial equipment like turbines, pumps, and generators, then
      aggregate temperature, vibration, and pressure readings into health score summaries
      that are republished to AWS IoT SiteWise for asset monitoring dashboards and AWS IoT Core for further processing and alerting.

3. Alternatively, locally compress summarized data into Apache Parquet format and
   transfer directly to Amazon S3.
   1. **Manufacturing example:** Configure edge devices in automotive plants to compress
      daily production data (part counts, cycle times, energy consumption) from assembly
      line robots and quality inspection systems into Parquet files, then batch upload to
      Amazon S3 for long-term storage and analysis with AWS analytics services like Amazon Athena and Quick Suite for operational intelligence reporting.

### Implementation Steps

1. Create data processing component in your language of choice, using the AWS IoT Greengrass Development Kit (GDK).
2. Have component subscribe to raw data topics on-premises.
3. Build components to do tasks such as summarize data and rolling averages for set
   time periods, and re-publish to new topic.
4. Relay only new topic from on premises to AWS IoT Core or SiteWise for storage and
   processing.

## Key AWS services

- AWS IoT Core
- AWS IoT Greengrass
- AWS IoT SiteWise
- AWS IoT SiteWise Edge

## Resources

- [Cost-effectively ingest IoT data directly into Amazon S3 using AWS IoT Greengrass](../../../prescriptive-guidance/latest/patterns/cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass.md "../../../prescriptive-guidance/latest/patterns/cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass.md")
- [Ingest and analyze equipment data in the cloud](https://aws.amazon.com/blogs/industries/ingest-and-analyze-equipment-data-in-the-cloud/ "https://aws.amazon.com/blogs/industries/ingest-and-analyze-equipment-data-in-the-cloud/")
- [Getting Started with AWS IoT Greengrass Solution Accelerators for Edge
  Computing](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0320-IOT_Slide-Deck.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/2020_0320-IOT_Slide-Deck.pdf")
