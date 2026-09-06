

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Getting started with Timestream for InfluxDB 3
<a name="getting-started-with-timestream-for-influxdb-3"></a>

## Setting up Amazon Timestream for InfluxDB 3
<a name="setting-up-amazon-timestream-for-influxdb-3"></a>

 Before you use Amazon Timestream for InfluxDB for the first time, complete the following tasks: 

 If you already have an AWS account, know your Timestream for InfluxDB requirements, and prefer to use the defaults for IAM and Amazon VPC, skip to [Creating and connecting to a Timestream for InfluxDB instance](#creating-and-connecting-to-a-timestream-for-influxdb-instance). 

### Determine requirements
<a name="determine-requirements"></a>

 Before you create a DB instance and a security group, you must know your DB instance and network needs. Here are some important things to consider: 
+  **Resource requirements** – What are the memory and processor requirements for your application or service? 
+  **VPC and security group** – Your DB instance will most likely be in a virtual private cloud (VPC). To connect to your DB instance, you need to set up security group rules. 
+  **High availability** – Do you need failover support? 
+  **IAM policies** – Does your AWS account have policies that grant the permissions needed to perform Amazon Timestream for InfluxDB operations? 
+  **Open ports** – What TCP/IP port does your database listen on? The default for Timestream for InfluxDB is 8086. 
+  **AWS Region** – What AWS Region do you want your database in? 
+  **DB disk subsystem** – What are your storage requirements? 

### Provide access to your DB instance in your VPC by creating a security group
<a name="provide-access-to-your-db-instance-in-your-vpc-by-creating-a-security-group"></a>

 VPC security groups provide access to DB instances in a VPC. They act as a firewall for the associated DB instance, controlling both inbound and outbound traffic at the DB instance level. DB instances are created by default with a firewall and a default security group that protect the DB instance. 

 To create a VPC security group: 

1.  In the AWS Management Console, choose **VPC**. 

1.  In the navigation pane, choose **Security Groups**. 

1.  Choose **Create security group**. 

1.  Enter a name, description, and select your VPC. 

1.  Add inbound rules for Custom TCP with appropriate source settings. 

1.  Create the security group. 

## Creating and connecting to a Timestream for InfluxDB instance
<a name="creating-and-connecting-to-a-timestream-for-influxdb-instance"></a>

Connecting to a Amazon Timestream for InfluxDB DB instance uses token authentication.

 The connection information includes endpoint, port, username, password, and a valid access token. You can find this information using the AWS Management Console or AWS CLI. 

 You can create access tokens using: 
+  [The InfluxDB CLI](https://docs.influxdata.com/influxdb3/enterprise/reference/cli/influxdb3/) 
+  [The InfluxDB 3 Explorer](https://docs.influxdata.com/influxdb3/explorer/) 
+  [The InfluxDB API](https://docs.influxdata.com/influxdb3/enterprise/api/v3/) 

 The following procedure creates both an Amazon Elastic Compute Cloud instance and a Timestream for InfluxDB DB cluster, and shows you how to write data to the DB instance from the Amazon EC2 instance using the Telegraf client. 

### Step 1: Create an Amazon EC2 instance
<a name="step-1-create-an-amazon-ec2-instance"></a>

1.  Sign in to the AWS Management Console and open the Amazon EC2 console. 

1.  Choose the AWS Region where you want to create the Amazon EC2 instance. 

1.  Choose Amazon EC2 Dashboard, then Launch instance. 

1.  Configure your Amazon EC2 instance with appropriate settings. 

### Step 2: Create an InfluxDB 3 instance
<a name="step-2-create-an-influxdb-3-instance"></a>

1.  Sign in to the AWS Management Console and open the Timestream for InfluxDB console. 

1.  In the navigation pane, choose **InfluxDB Databases**. 

1.  Choose **Create InfluxDB 3 database**. 

1.  After selecting InfluxDB 3, choose between the Core and Enterprise editions. For this tutorial, where you'll be ingesting data from a single Amazon EC2 instance and running test queries, the Core edition is sufficient for your needs. 

1.  Configure your DB instance with appropriate settings. For specific engine configurations, you can select from an existing parameter group or create a new one. If no custom configuration is needed, simply proceed and a default parameter group will be automatically created for your instance. 

   **Important:** If creating a private cluster, make sure you add the [required S3 policies](https://docs.aws.amazon.com/timestream/latest/developerguide/s3-vpc-endpoint-private-clusters.html) to create your Timestream for InfluxDB cluster 

1.  Configure your instance size and network settings. Pay special attention to the network configuration. If you choose a private instance, ensure it's accessible from your Amazon EC2 instance's VPC by selecting the appropriate VPC, subnets, and security groups that allow connectivity between your Amazon EC2 instance and the InfluxDB instance. 

1.  Choose **Create InfluxDB database**. 

1.  Wait for your DB instance to become available. 

### Step 3: Access the InfluxDB Explorer
<a name="step-3-access-the-influxdb-explorer.-to-access-your-influxdb-instance-through-the-influxdb-explorer"></a>

The easiest way to start interacting with your InfluxDB instance through the InfluxDB Explorer:

1.  Download the InfluxDB Explorer from [https://docs.influxdata.com/influxdb3/explorer/](https://docs.influxdata.com/influxdb3/explorer/) 

1.  For private DB instances, run the Explorer from within the same VPC (using an Amazon EC2 instance or bastion host). 

1.  For publicly accessible DB instances, you can run the Explorer from any location with internet access. 

1.  Configure the Explorer with your cluster endpoint and credentials. 

If you prefer using the InfluxDB 3 CLI, or APIs, please refer to [InfluxDB 3 documentation](https://docs.influxdata.com/influxdb3/enterprise/) to find information on [writing data](https://docs.influxdata.com/influxdb3/enterprise/write-data/), [executing queries](https://docs.influxdata.com/influxdb3/enterprise/query-data/), or [Administer](https://docs.influxdata.com/influxdb3/enterprise/admin/) your InfluxDB 3 Database 

### Step 4: Send Telegraf data to your InfluxDB instance
<a name="step-4-send-telegraf-data-to-your-influxdb-instance"></a>

1.  Connect to your InfluxDB instance using the InfluxDB Explorer and generate an API token. 

1.  Connect to your Amazon EC2 instance and install Telegraf. 

1.  Configure Telegraf to send data to your InfluxDB instance. 

1.  Enable and start the Telegraf service. 

### Step 5: Delete the Amazon EC2 instance and the InfluxDB DB instance
<a name="step-5-delete-the-amazon-ec2-instance-and-the-influxdb-db-instance"></a>

 After you explore the Telegraf-generated data, delete both your Amazon EC2 and your InfluxDB DB instances to avoid being charged for them. 