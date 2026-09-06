

# Managing instance classes
<a name="db-instance-classes"></a>

The instance class determines the computation and memory capacity of an Amazon DocumentDB (with MongoDB compatibility) instance. The instance class you need depends on your processing power and memory requirements. 

Amazon DocumentDB supports the R4, R5, R6G, R8G, T3, and T4G families of instance classes. These classes are current-generation instance classes that are optimized for memory-intensive applications. For the specifications on these classes, see [Instance class specifications](#db-instance-class-specs). 

**Topics**
+ [Determining an instance class](#db-instance-class-determining)
+ [Changing an instance's class](#db-instance-class-changing)
+ [Supported instance classes by Region](#db-instance-classes-by-region)
+ [Instance class specifications](#db-instance-class-specs)

## Determining an instance class
<a name="db-instance-class-determining"></a>

To determine the class of an instance, you can use the AWS Management Console or the `describe-db-instances` AWS CLI operation.

------
#### [ Using the AWS Management Console ]

To determine the instance class for your cluster's instances, complete the following steps in the console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Clusters **to find the instance that you're interested in. 
**Tip**  
If you don't see the navigation pane on the left side of your screen, choose the menu icon (![Menu button.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/docdb-menu-icon.png)) in the upper-left corner of the page.

1. In the Clusters navigation box, you’ll see the column **Cluster Identifier**. Your instances are listed under clusters, similar to the following screenshot.  
![Clusters table showing how an instance is nested under a cluster.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/choose-clusters.png)

1. In the list of instances, expand the cluster to find the instances you are interested in. Find the instance that you want. Then, look at the **Size** column of the instance's row to see its instance class.

   In the following image, the instance class for instance `robo3t` is `db.r5.4xlarge`.  
![List of instances in the Clusters table with the Size column showing the instance type.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/instance-class.png)

------
#### [ Using the AWS CLI ]

To determine the class of an instance using the AWS CLI, use the `describe-db-instances` operation with the following parameters.
+ **--db-instance-identifier** — Optional. Specifies the instance that you want to find the instance class for. If this parameter is omitted, `describe-db-instances` returns a description for up to 100 of your instances.
+ **--query** — Optional. Specifies the members of the instance to include in the results. If this parameter is omitted, all instance members are returned.

**Example**  
The following example finds the instance name and class for the instance `sample-instance-1`.  
For Linux, macOS, or Unix:  

```
aws docdb describe-db-instances \
    --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass]' \
    --db-instance-identifier sample-instance-1
```
For Windows:  

```
aws docdb describe-db-instances ^
    --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass]' ^
    --db-instance-identifier sample-instance-1
```
Output from this operation looks something like the following.  

```
[
    [
        "sample-instance-1",
        "db.r5.large"
    ]
```

**Example**  
The following example finds the instance name and class for up to 100 Amazon DocumentDB instances.  
For Linux, macOS, or Unix:  

```
aws docdb describe-db-instances \
    --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass]' \
    --filter Name=engine,Values=docdb
```
For Windows:  

```
aws docdb describe-db-instances ^
    --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass]' ^
    --filter Name=engine,Values=docdb
```
Output from this operation looks something like the following.  

```
[
    [
        "sample-instance-1",
        "db.r5.large"
    ],
    [
        "sample-instance-2",
        "db.r5.large"
    ],
    [
        "sample-instance-3",
        "db.r5.4xlarge"
    ],
    [
        "sample-instance-4",
        "db.r5.4xlarge"
    ]
]
```

For more information, see [Describing Amazon DocumentDB instances](db-instance-view-details.md). 

------

## Changing an instance's class
<a name="db-instance-class-changing"></a>

You can change the instance class of your instance using the AWS Management Console or the AWS CLI. For more information, see [Modifying an Amazon DocumentDB instance](db-instance-modify.md). 

## Supported instance classes by Region
<a name="db-instance-classes-by-region"></a>

Amazon DocumentDB supports the following instance classes:
+ `R8G`—Latest generation of memory-optimized instances powered by Arm-based AWS Graviton4 processors that provide up to 30% better performance over R6G instances.
+ `R6G`—Memory-optimized instances powered by Arm-based AWS Graviton2 processors that provide up to 30% better performance over R5 instances at 5% less cost.
+ `R6GD`—Memory-optimized R6G instances with local non-volatile memory express (NVMe)-based Solid-State Drive (SSD) storage for ephemeral data.
+ `R5`—Memory-optimized instances that provide up to 100% better performance over R4 instances for the same instance cost.
+ `R4`—Previous generation of memory-optimized instances.
+ `T4G`—Latest-generation low cost burstable general-purpose instance type powered by Arm-based AWS Graviton2 processors that provides a baseline level of CPU performance, delivering up to 35% better price performance over T3 instances and ideal for running applications with moderate CPU usage that experience temporary spikes in usage.
+ `T3`—Low cost burstable general-purpose instance type that provides a baseline level of CPU performance with the ability to burst CPU usage at any time for as long as required.

For detailed specifications on the instance classes, see [Instance class specifications](#db-instance-class-specs). 

**Note**  
I/O-Optimized storage is only available on engine versions 5.0 and 8.0 (instance-based clusters).

A particular instance class may or may not be supported in a given Region. The following table specifies which instance classes are supported by Amazon DocumentDB in each Region.


**Supported instance classes by Region**  

<table>
<thead>
  <tr><th></th><th colspan="8">Instance Classes</th></tr>
  <tr><th>Region</th><th>R8G</th><th>R6GD</th><th>R6G</th><th>R5</th><th>R4</th><th>T4G</th><th>T3</th><th>Serverless</th></tr>
</thead>
<tbody>
  <tr><td>US East (Ohio)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>US East (N. Virginia)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>US West (Oregon)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Africa (Cape Town)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>South America (São Paulo)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Hong Kong)</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Hyderabad)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Malaysia)</td><td></td><td></td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Mumbai)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Osaka)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Seoul)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Sydney)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Jakarta)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Melbourne)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Singapore)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Thailand)</td><td></td><td></td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Tokyo)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Canada (Central)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Canada West (Calgary)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Frankfurt)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Zurich)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Ireland)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (London)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Milan)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Paris)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Spain)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Stockholm)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Mexico (Central)</td><td></td><td></td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Middle East (UAE)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>China (Beijing)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>China (Ningxia)</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Israel (Tel Aviv)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>AWS GovCloud (US-West)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td></tr>
  <tr><td>AWS GovCloud (US-East)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
</tbody>
</table>


## Instance class specifications
<a name="db-instance-class-specs"></a>

The following table provides details of the Amazon DocumentDB instance classes, including which instance types are supported in each class. You can find explanations for each table column below the table.


<table>
<thead>
  <tr><th>Instance class</th><th>vCPU1</th><th>Memory (GiB)2</th><th>NVMe SSD tiered cache (GiB)3</th><th>Max. temp. storage (GiB)4</th><th>Baseline / burst bandwidth (Gbps)5</th><th>Supporting Engines6</th></tr>
</thead>
<tbody>
  <tr><td colspan="7"><b>R8G – Current Generation Memory-Optimized Instance Class based on Graviton4</b>R8G is the newest instance family (Graviton4), available on engine versions 5.0 and 8.0 only.</td></tr>
  <tr><td><code>db.r8g.large</code></td><td>2</td><td>16</td><td>-</td><td>30</td><td>0.937 / 12.5</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.xlarge</code></td><td>4</td><td>32</td><td>-</td><td>60</td><td>1.875 / 12.5</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.2xlarge</code></td><td>8</td><td>64</td><td>-</td><td>121</td><td>3.75 / 15.0</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.4xlarge</code></td><td>16</td><td>128</td><td>-</td><td>243</td><td>7.5 / 15.0</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.8xlarge</code></td><td>32</td><td>256</td><td>-</td><td>488</td><td>15</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.12xlarge</code></td><td>48</td><td>384</td><td>-</td><td>732</td><td>22</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.16xlarge</code></td><td>64</td><td>512</td><td>-</td><td>987</td><td>30</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.24xlarge</code></td><td>96</td><td>768</td><td>-</td><td>1484</td><td>40</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r8g.48xlarge</code></td><td>192</td><td>1536</td><td>-</td><td>2967</td><td>50</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td colspan="7"><b>R6G – Current Generation Memory-Optimized Instance Class based on Graviton2</b></td></tr>
  <tr><td><code>db.r6g.large</code></td><td>2</td><td>16</td><td>-</td><td>32</td><td>0.75 / 10</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r6g.xlarge</code></td><td>4</td><td>32</td><td>-</td><td>63</td><td>1.25 / 10</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r6g.2xlarge</code></td><td>8</td><td>64</td><td>-</td><td>126</td><td>2.5 / 10</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r6g.4xlarge</code></td><td>16</td><td>128</td><td>-</td><td>252</td><td>5.0 / 10</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r6g.8xlarge</code></td><td>32</td><td>256</td><td>-</td><td>504</td><td>12</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r6g.12xlarge</code></td><td>48</td><td>384</td><td>-</td><td>756</td><td>20</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r6g.16xlarge</code></td><td>64</td><td>512</td><td>-</td><td>1008</td><td>25</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td colspan="7"><b>R6GD – Current Generation NVMe-backed Instance Class based on Graviton2</b></td></tr>
  <tr><td><code>db.r6gd.xlarge</code></td><td>4</td><td>32</td><td>173</td><td>64</td><td>1.25 / 10</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r6gd.2xlarge</code></td><td>8</td><td>64</td><td>346</td><td>128</td><td>2.5 / 10</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r6gd.4xlarge</code></td><td>16</td><td>128</td><td>694</td><td>256</td><td>5.0 / 10</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r6gd.8xlarge</code></td><td>32</td><td>256</td><td>1388</td><td>512</td><td>12</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r6gd.12xlarge</code></td><td>48</td><td>384</td><td>2082</td><td>768</td><td>20</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td><code>db.r6gd.16xlarge</code></td><td>64</td><td>512</td><td>2776</td><td>1024</td><td>25</td><td>5.0.0 and 8.0.0</td></tr>
  <tr><td colspan="7"><b>R5 – Previous Generation Memory-Optimized Instance Class</b></td></tr>
  <tr><td><code>db.r5.large</code></td><td>2</td><td>16</td><td>-</td><td>31</td><td>0.75 / 10</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r5.xlarge</code></td><td>4</td><td>32</td><td>-</td><td>62</td><td>1.25 / 10</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r5.2xlarge</code></td><td>8</td><td>64</td><td>-</td><td>124</td><td>2.5 / 10</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r5.4xlarge</code></td><td>16</td><td>128</td><td>-</td><td>249</td><td>5.0 / 10</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r5.8xlarge</code></td><td>32</td><td>256</td><td>-</td><td>504</td><td>10</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r5.12xlarge</code></td><td>48</td><td>384</td><td>-</td><td>748</td><td>12</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r5.16xlarge</code></td><td>64</td><td>512</td><td>-</td><td>1008</td><td>20</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td><code>db.r5.24xlarge</code></td><td>96</td><td>768</td><td>-</td><td>1500</td><td>25</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td colspan="7"><b>R4 – Previous Generation Memory-Optimized Instance Class</b>R4 instances are only supported on engine version 3.6. Note that Amazon DocumentDB 3.6 reaches end of standard support on March 30, 2026. Extended Support (paid) is available until March 2029.</td></tr>
  <tr><td><code>db.r4.large</code></td><td>2</td><td>15.25</td><td>-</td><td>30</td><td>0.75 / 10</td><td>3.6.0 only</td></tr>
  <tr><td><code>db.r4.xlarge</code></td><td>4</td><td>30.5</td><td>-</td><td>60</td><td>1.25 / 10</td><td>3.6.0 only</td></tr>
  <tr><td><code>db.r4.2xlarge</code></td><td>8</td><td>61</td><td>-</td><td>120</td><td>2.5 / 10</td><td>3.6.0 only</td></tr>
  <tr><td><code>db.r4.4xlarge</code></td><td>16</td><td>122</td><td>-</td><td>240</td><td>5.0 /10</td><td>3.6.0 only</td></tr>
  <tr><td><code>db.r4.8xlarge</code></td><td>32</td><td>244</td><td>-</td><td>480</td><td>10</td><td>3.6.0 only</td></tr>
  <tr><td><code>db.r4.16xlarge</code></td><td>64</td><td>488</td><td>-</td><td>960</td><td>25</td><td>3.6.0 only</td></tr>
  <tr><td colspan="7"><b>T4G – Latest Generation Burstable Performance Instance Classes based on Graviton2</b>T-series instances run in Unlimited CPU burst mode. Burst usage beyond the baseline is billed extra. Not supported for Global Clusters.</td></tr>
  <tr><td><code>db.t4g.medium</code></td><td>2</td><td>4</td><td>-</td><td>8.13</td><td>0.256 / 5</td><td>4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td colspan="7"><b>T3 – Previous Generation Burstable Performance Instance Classes</b></td></tr>
  <tr><td><code>db.t3.medium</code></td><td>2</td><td>4</td><td>-</td><td>7.5</td><td>0.256 / 5</td><td>3.6.0, 4.0.0, 5.0.0, and 8.0.0</td></tr>
  <tr><td colspan="7"> <ol><li> <b>vCPU</b> — The number of virtual central processing units (CPUs). A virtual CPU is a unit of capacity that you can use to compare instance classes. Instead of purchasing or leasing a particular processor to use for several months or years, you are renting capacity by the hour. Our goal is to provide a consistent amount of CPU capacity no matter what the actual underlying hardware.  </li><li> <b>Memory (GiB)</b> — The RAM, in gigabytes, that is allocated to the instance. There is often a consistent ratio between memory and vCPU. </li><li> <b>NVMe SSD tiered cache</b> — The space on the SSD volume, measured in gigabytes, allocated as extended cache for storing ephemeral data. This cache is only available in NVMe-backed instances. </li><li> <b>Max. temp. storage (GiB)</b> — The space, measured in gigabytes, allocated to the instance for non-persistent temporary file storage. For NVMe-backed instances, this storage is hosted on an NVMe-based SSD volume. In all other instances, it is hosted on Amazon Elastic Block Store (EBS). </li><li> <b>Baseline / burst bandwidth (Gbps)</b> — Burst bandwidth represents the maximum bandwidth in gigabits per second. Divide by 8 to get the expected throughput in gigabytes per second. Instances of size 4xlarge and smaller have a baseline bandwidth. To meet additional demand, they can use a network I/O credit mechanism to burst beyond their baseline bandwidth. Instances can use burst bandwidth for a limited time, typically from 5 to 60 minutes, depending on the instance size. </li><li> <b>Supporting Engines</b> — The Amazon DocumentDB engines that support the instance class. </li></ol> </td></tr>
</tbody>
</table>
