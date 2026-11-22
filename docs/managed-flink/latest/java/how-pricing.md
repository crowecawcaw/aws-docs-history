

# Per second billing in Managed Service for Apache Flink

Managed Service for Apache Flink is now billed in one-second increments. There is a ten-minute minimum charge per application. Per-second billing is applicable to applications that are newly launched or already running. This section describes how Managed Service for Apache Flink meters and bills you for your usage. To learn more about Managed Service for Apache Flink pricing, see [Amazon Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/). 

## How it works
<a name="how-resources-kda"></a>

Managed Service for Apache Flink charges you for the duration and number of **Kinesis Processing Units (KPUs)** that are billed in one-second increments in the supported AWS Regions. A single KPU comprises 1vCPU compute and 4 GB of memory. You are charged an hourly rate based on the number of KPUs used to run your applications. 

For example, an application running for 20 minutes and 10 seconds will be charged for 20 minutes and 10 seconds, multiplied by the resources it used. An application that is running for 5 minutes will be charged the ten-minute minimum, multiplied by the resources it used.

Managed Service for Apache Flink states usage in hours. For example, 15 minutes corresponds to 0.25 hours. 

For Apache Flink applications, you are charged a single additional KPU per application, used for orchestration. Applications are also charged for running storage and durable backups. Running application storage is used for stateful processing capabilities in Managed Service for Apache Flink and is charged per GB/month. Durable backups are optional and provide point-in-time recovery for applications, charged per GB/month. 

In streaming mode, Managed Service for Apache Flink automatically scales the number of KPUs required by your stream processing application as the demands of memory and compute fluctuate. You can choose to provision your application with the required number of KPUs. 

## Billing snapshot storage
<a name="how-pricing-snapshots"></a>

Managed Service for Apache Flink bills snapshot storage as durable application backups, per GB-month. Enhanced snapshots and application snapshots (legacy) have the same rate. For the rate in each AWS Region, see [Amazon Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/) on the AWS website. In enhanced snapshot mode, Managed Service for Apache Flink also bills the storage of system snapshots.

**Note**  
Enhanced snapshots remain after you delete the application. You pay for their storage until you delete them.

For more information about the enhanced snapshots that Managed Service for Apache Flink bills, and about when billing starts and stops, see [Billing for enhanced snapshots](snapshots-how-it-works.md#snapshots-how-it-works-billing-for-snapshots).

Managed Service for Apache Flink does not charge to import or export an enhanced snapshot. Amazon S3 charges apply to the bucket that an import reads or an export writes. You pay for the storage of each enhanced snapshot that you import. For more information about import and export, see [Import and export enhanced snapshots](snapshots-import-export.md).

For current prices, see [Amazon Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/) on the AWS website.

## AWS Region availability
<a name="how-pricing-regions"></a>

**Note**  
At this time, per second billing is not available in the following Regions: AWS GovCloud (US-East), AWS GovCloud (US-West), China (Beijing), and China (Ningxia).

Per second billing is available in the following AWS Regions: 
+ US East (N. Virginia) - us-east-1
+ US East (Ohio) - us-east-2
+ US West (N. California) - us-west-1
+ US West (Oregon) - us-west-2
+ Africa (Cape Town) - af-south-1
+ Asia Pacific (Hong Kong) - ap-east-1
+ Asia Pacific (Hyderabad) - ap-south-1
+ Asia Pacific (Jakarta) - ap-southeast-3
+ Asia Pacific (Melbourne) - ap-southeast-4
+ Asia Pacific (Mumbai) - ap-south-1
+ Asia Pacific (Osaka) - ap-northeast-3
+ Asia Pacific (Seoul) - ap-northeast-2
+ Asia Pacific (Singapore) - ap-southeast-1
+ Asia Pacific (Sydney) - ap-southeast-2
+ Asia Pacific (Tokyo) - ap-northeast-1
+ Canada (Central) - ca-central-1
+ Canada West (Calgary) - ca-west-1
+ Europe (Frankfurt) - eu-central-1
+ Europe (Ireland) - eu-west-1
+ Europe (London) - eu-west-2
+ Europe (Milan) - eu-south-1
+ Europe (Paris) - eu-west-3
+ Europe (Spain) - eu-south-2
+ Europe (Stockholm) - eu-north-1
+ Europe (Zurich) - eu-central-2
+ Israel (Tel Aviv) - il-central-1
+ Middle East (Bahrain) - me-south-1
+ Middle East (UAE) - me-central-1
+ South America (São Paulo) - sa-east-1

## Pricing examples
<a name="how-pricing-examples"></a>

You can find pricing examples on the Managed Service for Apache Flink pricing page. For more information, see [Amazon Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/). Following are further examples with Cost Usage Report illustrations for each.

### A long running, heavy workload
<a name="pricing-example-1"></a>

You are a large Video streaming service and you would like to build a real-time video recommendation based on your users’ interactions. You use an Apache Flink application in Managed Service for Apache Flink to continuously ingest user interaction events from multiple Kinesis data streams and to process events in real time before outputting to a downstream system. User interaction events are transformed using several operators. This includes partitioning data by event type, enriching data with additional metadata, sorting data by timestamp, and buffering data for 5 minutes before delivery. The application has many transformation steps that are compute-intensive and parallelizable. Your Flink application is configured to run with 20 KPUs to accommodate the workload. Your application uses 1 GB of durable application backup every day. The monthly Managed Service for Apache Flink charges will be computed as follows:

**Monthly charges**

The price in the US East (N. Virginia) Region is $0.11 per KPU-hour. Managed Service for Apache Flink allocates 50 GB of running application storage per KPU and charges $0.10 per GB/month.
+ Monthly KPU charges: 24 hours \* 30 days \* (20 KPUs \+ 1 additional KPU for streaming application) \* $0.11/hour = $1,584.00
+ Monthly running application storage charges: 30 days \* 20 KPUs \* 50 GB/KPUs \* $0.10/GB-month = $100.00
+ Monthly durable application storage charges: 30 days \* 1 GB \* 0.023/GB-month = $0.03
+ Total charges: $1,584.00 \+ $100 \+ $0.03 = **$1,684.03**

**Cost usage report for Managed Service for Apache Flink on the Billing and Cost Management console for the month**

Kinesis Analytics
+ USD 1,684.03 - US East (N. Virginia)
+ Amazon Kinesis Analytics CreateSnapshot
  + $0.023 per GB-month of durable application backups
    + 1 GB-month - USD 0.03
+ Amazon Kinesis Analytics StartApplication
  + $0.10 per GB-month of running application storage
    + 1,000 GB-month - USD 100
  + $0.11 per Kinesis Processing Unit-hour for Apache Flink applications
    + 15,120 KPU-hour - USD 1,584

### A batch workload that runs for \~15 minutes every day
<a name="pricing-example-2"></a>

You use an Apache Flink application in Managed Service for Apache Flink to transform log data in Amazon Simple Storage Service (Amazon S3) in batch mode. The log data is transformed using several operators. This includes applying a schema to the different log events, partitioning data by event type, and sorting data by timestamp. The application has many transformation steps, but none are computationally intensive. This application ingests data at 2,000 records/second for 15 minutes every day in a 30-day month. You do not create any durable application backups. The monthly Managed Service for Apache Flink charges will be computed as follows:

**Monthly charges**

The price in the US East (N. Virginia) Region is $0.11 per KPU-hour. Managed Service for Apache Flink allocates 50 GB of running application storage per KPU and charges $0.10 per GB/month.
+ Batch Workload: During the 15 minutes per day, the Managed Service for Apache Flink application is processing 2,000 records/second, which takes 2KPUs. 30 days/month \* 15 minutes/day = 450 minutes/month
+ Monthly KPU charges: 450 minutes/month \* (2KPUs \+ 1 additional KPU for streaming application) \* $0.11/hour = $2.48
+ Monthly running application storage charges: 450 minutes/month \* 2 KPUs \* 50 GB/KPUs \* $0.10/GB-month = $0.11
+ Total charges: $2.48 \+ 0.11 = **$2.59**

**Cost usage report for Managed Service for Apache Flink on the Billing and Cost Management console for the month**

Kinesis Analytics
+ USD 2.59 - US East (N. Virginia)
+ Amazon Kinesis Analytics StartApplication
  + $0.10 per GB-month of running application backups
    + 1.042 GB-month - USD 0.11
  + $0.11 per Kinesis Processing Unit-hour for Apache Flink applications
    + 22.5 KPU-Hour - USD 2.48

### A test application that stops and starts continuously in the same hour, attracting multiple minimum charges
<a name="pricing-example-3"></a>

You’re a large ecommerce platform that processes millions of transactions every day. You want to develop real-time fraud detection. You use an Apache Flink application in Managed Service for Apache Flink to ingest transaction events from Kinesis Data Streams and process events in real-time with different transformation steps. This includes using a sliding window to aggregate events, partitioning events by event types, and applying specific detection rules for different event types. During development, you start and stop your application multiple times to test and debug behavior. There are occasions when your application only runs for a few minutes. There is an hour when you’re testing your application with 4 KPUs and your application does not use any durable application backups:
+ At 10:05 AM, you start your application, which runs for 30 minutes before it’s stopped at 10:35 AM.
+ At 10:40 AM, you start your application again, which runs for 5 minutes before it’s stopped at 10:45 AM.
+ At 10:50 AM, you start the application again, which runs for 2 minutes before it’s stopped at 10:52 AM.

Managed Service for Apache Flink charges a minimum of 10 minutes of usage each time an application starts running. The monthly Managed Service for Apache Flink usage for your application will be computed as follows:
+ First time your application starts and stops: 30 minutes of usage
+ Second time your application starts and stops: 10 minutes of usage (your application runs for 5 minutes rounded up to the 10 minutes minimum charge)
+ Third time your application starts and stops: 10 minutes of usage (your application runs for 2 minutes, rounded up to the 10 minutes minimum charge)

In total, your application would be charged for 50 minutes of usage. If there are no other times in the month your application is running, the monthly Managed Service for Apache Flink charges will be computed as follows:

**Monthly charges**

The price in the US East (N. Virginia) Region is $0.11 per KPU-hour. Managed Service for Apache Flink allocates 50 GB of running application storage per KPU and charges $0.10 per GB/month.
+ Monthly KPU charges: 50 minutes \* (4KPUs \+ 1 additional KPU for streaming application) \* $0.11/hour = $0.46 (rounded to the nearest penny)
+ Monthly running application storage charges: 50 minutes \* 4 KPUs \* 50 GB/KPUs \* $0.10/GB-month = $0.03 (rounded to the nearest penny)
+ Total charges: $0.46 \+ 0.03 = **$0.49**

**Cost usage report for Managed Service for Apache Flink on the Billing and Cost Management console for the month**

Kinesis Analytics
+ USD 0.49 - US East (N. Virginia)
+ Amazon Kinesis Analytics StartApplication
  + $0.10 per GB-month of running application storage
    + 0.232 GB-month - USD 0.03
  + $0.11 per Kinesis Processing Unit-hour for Apache Flink applications
    + 4.167 KPU-Hour - USD 0.46

### Pricing imported snapshots
<a name="pricing-example-4"></a>

This example is hypothetical. Suppose that your Apache Flink application on Managed Service for Apache Flink uses enhanced snapshot mode. The application runs all month with 2 KPUs. You would store 4 enhanced snapshots of 5 GB each for the whole month. You created them before earlier code releases. You would also import a 10 GB Apache Flink savepoint (a state backup that Apache Flink writes) from Amazon S3 as an enhanced snapshot. You would keep the imported enhanced snapshot for the whole month. With the assumed prices that follow, the example monthly Managed Service for Apache Flink charges would be as follows:

**Monthly charges**

For this example, assume that the price in the US East (N. Virginia) Region is USD $0.11 per KPU-hour. Managed Service for Apache Flink allocates 50 GB of running application storage per KPU. Assume that running application storage in the US East (N. Virginia) Region costs USD $0.10 per GB-month. Also assume that Managed Service for Apache Flink bills enhanced snapshot storage in the US East (N. Virginia) Region as durable application backups at USD $0.023 per GB-month. For current prices, see [Amazon Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/) on the AWS website.
+ Estimated monthly KPU charges: In this example, assume the price is USD $0.11 per KPU-hour; the charges would be 24 hours \* 30 days \* (2 KPUs \+ 1 additional KPU for streaming application) \* USD $0.11/hour = USD $237.60
+ Estimated monthly running application storage charges: In this example, assume the price is USD $0.10 per GB-month; the charges would be 2 KPUs \* 50 GB/KPUs \* USD $0.10/GB-month = USD $10.00
+ Estimated monthly enhanced snapshot storage charges: In this example, assume the price is USD $0.023 per GB-month; the charges would be (4 \* 5 GB \+ 10 GB) \* USD $0.023/GB-month = USD $0.69
+ Import charges: In this example, the charges would be USD $0.00 (no charge to import or export an enhanced snapshot)
+ Estimated total charges: In this example, the total would be USD $237.60 \+ USD $10.00 \+ USD $0.69 = **USD $248.29**

The enhanced snapshots remain after you delete the application. In this example, you would pay USD $0.69 each month for their storage until you delete them.