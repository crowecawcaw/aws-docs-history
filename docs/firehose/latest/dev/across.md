# Understand delivery across AWS accounts and regions

Amazon Data Firehose supports data delivery to HTTP endpoint destinations across AWS accounts.
The Firehose stream and the HTTP endpoint that you choose as your destination can belong to
different AWS accounts.

Amazon Data Firehose also supports data delivery to HTTP endpoint destinations across AWS regions.
You can deliver data from a Firehose stream in one AWS region to an HTTP endpoint in
another AWS region. You can also delivery data from a Firehose stream to an HTTP
endpoint destination outside of AWS regions, for example to your own on-premises
server by setting the HTTP endpoint URL to your desired destination. For these
scenarios, additional data transfer charges are added to your delivery costs. For more
information, see the [Data
Transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer "https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer") section in the "On-Demand Pricing" page.
