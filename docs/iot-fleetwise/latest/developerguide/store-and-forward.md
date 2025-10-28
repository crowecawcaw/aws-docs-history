# Store and forward campaign data

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

Use data partitions within campaigns to temporarily store signal data on the Edge for
vehicles and fleets. By configuring upload and storage options for data partitions, you
can optimize your ideal conditions for data forwarding to your designated data
destinations (like an Amazon S3 bucket). For example, you can configure the data partition to
store data on a vehicle until it connects to Wi-Fi. Then, once the vehicle connects, the
campaign triggers the data in that particular partition to be sent to the cloud.
Alternatively, you can collect data using AWS IoT Jobs.

###### Topics

- [Create data partitions](create-campaign-data-partitions.md "create-campaign-data-partitions.md")
- [Upload campaign data](update-campaign-cli-data-partitions.md "update-campaign-cli-data-partitions.md")
- [Upload data using AWS IoT
  Jobs](update-campaign-cli-data-partitions-jobs.md "update-campaign-cli-data-partitions-jobs.md")
