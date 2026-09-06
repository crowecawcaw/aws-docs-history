

# Flight Information Management System (FIMS)
<a name="flight-information-management-system"></a>

Publication date: **February 2, 2022 ([Diagram history](#diagram-history))**

This architecture enables you to manage and operate services required for unmanned aerial systems on AWS.

## Flight Information Management System (FIMS) Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how you can manage and operate services required for unmanned aerial systems on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/flight-information-management-system/images/flight-information-management-system.png)


1. Operators access the FIMS services through a web-based portal for flight planning and additional services.

1. Flight plans are sent to appropriate microservices and **Amazon Elastic Container Service** (Amazon ECS) is leveraged for processing approvals.

1. Persistent relational data such as registration and flight plan are stored in **Amazon Aurora**.

1. Real-time data (such as telemetry, position, track, and velocity) is stored in **DynamoDB** .

1. Cached data is stored through **Amazon ElastiCache** for quick retrieval.

1. Processed data is encrypted and stored in data lake, and managed by **AWS Lake Formation**, in accordance with regulatory compliance.

1. Virtualization tools to view real-time positioning, flight paths, potential conflicts, etc. can be deployed using **Quick** and **Amazon Managed Grafana**.

1. Flight plan approvals automatically provided to UAS operators by FIMS.

1. UAS operators request/receive manual approval from FIMS Admins for flight plans when conflicts arise.

1. UAS provider data stored in **Amazon Aurora** and real-time data stored in **DynamoDB** databases.

1. Data lake built on **Amazon S3** is used for secure data archival, analytics, and visualization.

1. Supplemental data from weather services is ingested into FIMS for smart decisioning.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 2, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.