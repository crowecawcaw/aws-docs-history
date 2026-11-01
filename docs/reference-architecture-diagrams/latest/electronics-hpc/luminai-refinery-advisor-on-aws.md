

# LUMINAI Refinery Advisor on AWS
<a name="luminai-refinery-advisor-on-aws"></a>

Publication date: **February 29, 2024 ([Diagram history](diagram-history.md))**

This reference architecture illustrates a highly scalable deployment of Beyond Limits’ [LUMINAI Refinery Advisor](https://www.beyond.ai/products/beyond-limits-luminai-refinery-advisor/) on AWS using Amazon Elastic Container Service (Amazon ECS), Amazon Aurora, Amazon MQ, and other AWS managed services.

 LUMINAI is an AI-driven decision support system that maintains a holistic view of the entire site and makes timely, transparent recommendations that enable operators to close the profitability gap in real time and maximize operational efficiency. 

## LUMINAI Refinery Advisor on AWS diagram
<a name="luminai-refinery-advisor-on-aws-diagram1"></a>

![Reference architecture diagram showing a highly scalable deployment of Beyond Limits’ LUMINAI Refinery Advisor on AWS using Amazon Elastic Container Service (Amazon ECS), Amazon Aurora, Amazon MQ, and other AWS managed services.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/images/luminai-refinery-advisor-on-aws.png)


1.  Operations data from multiple refineries stream into the LUMINAI Refinery Advisor System on AWS. 

1.  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) on a public subnet directs data stream to the sensor processing pipeline on a private subnet. 

1.  Stream data ingestion processes running on [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) direct streams to [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/) (Amazon MSK), which ingests and processes streaming data in real time at scale and directs it to ETL jobs running on [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/). As each job completes its task, results are stored on [Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) and placed on [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/), a highly performant and scalable message queuing service. 

1.  LUMINAI’s Orchestrator and Reasoner business services run on Amazon ECS and process messages on Amazon MQ. Both business services leverage AI-driven algorithms to provide real-time insights into each refinery. 

1.  Processed data from business services are stored on Aurora PostgreSQL and are made available to web UI, API, and BI tools. Long-term data is stored on [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3). 

1.  Users can access the refineries' operational data and have a holistic view of each refinery through a web browser. LUMINAI provides access to refinery data through a web UI or APIs. 

1.  Authorized clients such as plant and operations managers, maintenance teams, and data scientists and engineers can access information by using BI tools. 

## Further reading
<a name="luminai-refinery-advisor-on-aws-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [Beyond Limits – Enterprise AI Software Solutions ](https://www.beyond.ai/) 
+  [LUMINAI Refinery Advisor ](https://www.beyond.ai/products/beyond-limits-luminai-refinery-advisor/) 