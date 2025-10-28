End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Summary

Migrating your AWS IoT Analytics workload from AWS IoT Analytics to Amazon Kinesis Data Streams, Amazon S3, and enhances your ability to handle large-scale, complex AWS IoT data.
This architecture provides scalable, durable storage and powerful analytics capabilities, enabling you to gain deeper insights from your IoT data in real-time.

Cleaning up resources created using AWS CloudFormation is essential to avoid unexpected costs once the migration has completed.

Refer to the AWS IoT Analytics
[pricing page](https://aws.amazon.com/iot-analytics/pricing/ "https://aws.amazon.com/iot-analytics/pricing/") for costs involved in
data migration. Consider deleting the newly created dataset when finished to avoid any unnecessary expenses.

Full dataset export: To export the complete dataset without any time-based splitting,
you can also use AWS IoT Analytics console and set a content delivery rule accordingly.

By following the migration guide, you can seamlessly transition your data ingestion and processing pipelines,
ensuring continuous and reliable data flow. Leveraging AWS Glue and Amazon Athena further simplifies data
preparation and querying, allowing you to perform sophisticated analyzes without managing any infrastructure.

This approach empowers you to scale your AWS IoT Analytics efforts effectively, making it easier to adapt to the
growing demands of your business and extract maximum value from your AWS IoT data.
