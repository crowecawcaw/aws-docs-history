

# Data
<a name="data"></a>


| CMSUS\_7: Are you optimizing data ingestion? | 
| --- | 
|   | 

 

**CMSUS\_BP7.1: Use technologies that support data access and storage patterns and implement a data classification policy** 

For more details, see [SUS04-BP1](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a2.html) and [SUS04-BP2](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a3.html) in the *Sustainability Pillar whitepaper*. 

**CMSUS\_BP7.2: Collect and store only what is needed** 

Optimize data collection frequency. For example, if battery data is being collected, you do not need to collect the data every millisecond although the data is available on the bus. Instead, collect it based on an event or at a larger time interval, such as every 5 seconds. 

**CMSUS\_BP7.3: Avoid multiple connections from the edge** 

**CMSUS\_BP7.4: ** Maximize data transformation at the edge (make data human readable at the edge)

**Prescriptive guidance:**
+  Collect only what is needed. Ensure that there is a business and engineering justification for all data being collected and revisit based on business and engineering needs (rather keeping it constant). 
+  Use onboard capability to the fullest (monitor edge capability). 
+  Before the data gets uploaded to the cloud, compress and aggregate the data at the edge wherever possible. 
+  Use purpose-built intelligent data collection to make the data collection deliberate and flexible.  
+  Transform and preprocess or polish the data at the edge wherever possible to minimize transactions with the cloud. 


| CMSUS\_8: Are you optimizing data consumption?  | 
| --- | 
|   | 

**CMSUS\_BP8.1: Use policies to manage the lifecycle of your datasets** 

For more details, see [SUS04-BP3](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html) and [SUS04-BP4](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a5.html) in the *Sustainability Pillar whitepaper*. 

**CMSUS\_BP8.2: Batch the ingested data before storing, if possible, to conserve storage** .

**CMSUS\_BP8.3: Select compute instances and storage mechanisms from a sustainable point of view**

For example, use Graviton instances.

**Prescriptive guidance:**
+ Use microservice-based architecture (run what is needed). 
+ Use data lifecycle policy to move data to into effective database (cheap/more sustainable storage)
+ Collect carbon footprint data for the vehicle when it's in motion to help customers with efficient routing and fueling mechanisms. 


| CMSUS\_9: Are you optimizing data analytics? | 
| --- | 
|   | 

**CMSUS\_BP9.1: Use elasticity and automation to expand block storage or file system as data grows to minimize the total provisioned storage** 

For more details, see [SUS04-BP3](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html) and [SUS04-BP4](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a5.html) in the *Sustainability Pillar whitepaper*.

**CMSUS\_BP9.2: Use reduced log level at production** 

**CMSUS\_BP9.3: Adopt campaign-based data collection for monitoring** 

**CMSUS\_BP9.4: Alert only if needed**

Use the appropriate notification mechanism, such as push notifications, SMS, Amazon SNS, and Amazon SES. Adjust the notification threshold and interval as needed.

**Prescriptive guidance:**
+  Use connected vehicle data to encourage the end user to be more sustainable (such as when to charge, and where to charge.) 
+  Create alerts and metrics based on the data collected and notify personas involved for actions.  
+  Move the data (old data, used data, and data not required often) to sustainable storage services in specific Regions.  
+  Delete data or create rules to delete data based on business logic. 