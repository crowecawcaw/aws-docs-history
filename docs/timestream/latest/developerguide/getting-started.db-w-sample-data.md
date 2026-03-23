For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Tutorial

This tutorial shows you how to create a database populated with sample data sets and
run sample queries. The sample data sets used in this tutorial are frequently seen in
IoT and DevOps scenarios. The IoT data set contains time series data such as the speed,
location, and load of a truck, to streamline fleet management and identify optimization
opportunities. The DevOps data set contains EC2 instance metrics such as CPU, network,
and memory utilization to improve application performance and availability. Here's a
[video tutorial](https://www.youtube.com/watch?v=YBWCGDd4ChQ "https://www.youtube.com/watch?v=YBWCGDd4ChQ") for
the instructions described in this section.

Follow these steps to create a database populated with the sample data sets and run
sample queries using the AWS Console:

## Using the console

Follow these steps to create a database populated with the sample data sets and
run sample queries using the AWS Console:

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Databases**.
3. Click on **Create database**.
4. On the create database page, enter the following:
   - **Choose configuration**—Select
     **Sample database**.
   - **Name**—Enter a database name of your
     choice.

   ###### Note

   After creating a database with sample data sets, to use the
   sample queries which are available in the console, you can
   adjust the database name referenced in the query to match the
   database name you enter here. There are sample queries for each
   combination of sample data set and type of time series records.
   - **Choose sample data sets**—Select
     **IoT** and **DevOps**.
   - **Choose the type of time series
     records**—Select **Multi-measure
     records**.
   - Click on **Create database** to create a
     database containing two tables populated with sample data. The table
     names for sample data sets with multi-measure records are
     `DevOpsMulti` and `IoTMulti`. The table
     names for sample datasets with single-measure records are
     `DevOps` and `IoT`.

5. In the navigation pane, choose **Query editor**.
6. Select **Sample queries** from the top menu.
7. Click on one of the sample queries for a data set you chose when creating
   the sample database. This will take you back to the query editor with the
   editor populated with the sample query.
8. Adjust the database name for the sample query.
9. Click **Run** to run the query and see query
   results.

## Using the SDKs

Timestream Live Analytics provides a fully functional sample application that shows you how
to create a database and table, populate the table with ~126K rows of sample data,
and run sample queries. The sample application is available in [GitHub](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps "https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps") for Java, Python, Node.js, Go, and .NET.

1. Clone the GitHub repository Timestream Live Analytics sample applications following
   the instructions from GitHub.
2. Configure the AWS SDK to connect to Amazon Timestream Live Analytics following the
   instructions described in [Using the AWS SDKs](getting-started-sdks.md "getting-started-sdks.md").
3. Compile and run the sample application using the instructions
   below:
   - Instructions for the [Java sample application](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/java/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/java/README.md").
   - Instructions for the [Java v2 sample application](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/javaV2/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/javaV2/README.md").
   - Instructions for the [Go sample application](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/sample_apps/goV2/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/sample_apps/goV2/README.md").
   - Instructions for the [Python sample application](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/python/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/python/README.md").
   - Instructions for the [Node.js sample application](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/js/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/js/README.md").
   - Instructions for the [.NET sample application](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/dotnet/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps/dotnet/README.md").
