

# Flight Information Management System (FIMS)
<a name="flight-information-management-system"></a>

Publication date: **February 2, 2022 ([Diagram history](diagram-history.md))**

This architecture enables you to manage and operate services required for unmanned aerial systems on AWS.

## Flight Information Management System (FIMS) diagram
<a name="flight-information-management-system-diagram1"></a>

![Reference architecture diagram showing how you can manage and operate services required for unmanned aerial systems on AWS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/aerospace/images/flight-information-management-system.png)


1. Operators access the FIMS services through a web-based portal for flight planning and additional services.

1. Flight plans are sent to appropriate microservices and [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) (Amazon ECS) is leveraged for processing approvals.

1. Persistent relational data such as registration and flight plan are stored in [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/).

1. Real-time data (such as telemetry, position, track, and velocity) is stored in [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) .

1. Cached data is stored through [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/) for quick retrieval.

1. Processed data is encrypted and stored in data lake, and managed by [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/), in accordance with regulatory compliance.

1. Virtualization tools to view real-time positioning, flight paths, potential conflicts, etc. can be deployed using [Quick](https://docs.aws.amazon.com/quick/latest/userguide/) and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/).

1. Flight plan approvals automatically provided to UAS operators by FIMS.

1. UAS operators request/receive manual approval from FIMS Admins for flight plans when conflicts arise.

1. UAS provider data stored in Amazon Aurora and real-time data stored in DynamoDB databases.

1. Data lake built on [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) is used for secure data archival, analytics, and visualization.

1. Supplemental data from weather services is ingested into FIMS for smart decisioning.

## Further reading
<a name="flight-information-management-system-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 