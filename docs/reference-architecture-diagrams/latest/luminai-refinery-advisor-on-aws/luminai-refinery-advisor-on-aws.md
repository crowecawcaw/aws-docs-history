

# LUMINAI Refinery Advisor on AWS
<a name="luminai-refinery-advisor-on-aws"></a>

Publication date: **February 29, 2024 ([Diagram history](#diagram-history))**

This reference architecture illustrates a highly scalable deployment of Beyond Limits’ [LUMINAI Refinery Advisor](https://www.beyond.ai/products/beyond-limits-luminai-refinery-advisor/) on AWS using Amazon Elastic Container Service (Amazon ECS), Amazon Aurora, Amazon MQ, and other AWS managed services.

 LUMINAI is an AI-driven decision support system that maintains a holistic view of the entire site and makes timely, transparent recommendations that enable operators to close the profitability gap in real time and maximize operational efficiency. 

## LUMINAI Refinery Advisor on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing a highly scalable deployment of Beyond Limits’ LUMINAI Refinery Advisor on AWS using Amazon Elastic Container Service (Amazon ECS), Amazon Aurora, Amazon MQ, and other AWS managed services.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/luminai-refinery-advisor-on-aws/images/luminai-refinery-advisor-on-aws.png)


1.  Operations data from multiple refineries stream into the LUMINAI Refinery Advisor System on AWS. 

1.  **Application Load Balancer** on a public subnet directs data stream to the sensor processing pipeline on a private subnet. 

1.  Stream data ingestion processes running on **Amazon ECS** direct streams to **Amazon Managed Streaming for Apache Kafka** (Amazon MSK), which ingests and processes streaming data in real time at scale and directs it to ETL jobs running on **Amazon EMR**. As each job completes its task, results are stored on **Amazon Aurora PostgreSQL** and placed on **Amazon MQ**, a highly performant and scalable message queuing service. 

1.  LUMINAI’s Orchestrator and Reasoner business services run on **Amazon ECS** and process messages on **Amazon MQ**. Both business services leverage AI-driven algorithms to provide real-time insights into each refinery. 

1.  Processed data from business services are stored on **Aurora PostgreSQL** and are made available to web UI, API, and BI tools. Long-term data is stored on **Amazon Simple Storage Service** (Amazon S3). 

1.  Users can access the refineries' operational data and have a holistic view of each refinery through a web browser. LUMINAI provides access to refinery data through a web UI or APIs. 

1.  Authorized clients such as plant and operations managers, maintenance teams, and data scientists and engineers can access information by using BI tools. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [Beyond Limits – Enterprise AI Software Solutions ](https://www.beyond.ai/) 
+  [LUMINAI Refinery Advisor ](https://www.beyond.ai/products/beyond-limits-luminai-refinery-advisor/) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 29, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.