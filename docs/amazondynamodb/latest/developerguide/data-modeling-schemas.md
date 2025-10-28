# Data modeling schema design packages in DynamoDB

Learn about data modeling schema design packages for DynamoDB,
including use cases, access patterns, and final schema designs for social networks,
gaming profiles, complaint management, recurring payments, device status, and online
shops.

![Image showing the conceptual relationship between the data, the blocks that sit under them, and then the foundation that sits under the blocks. Emphasis on the foundation.](images/DataModeling/SchemaDesignData.png)

## Prerequisites

Before we attempt to design our schema for DynamoDB, we must first gather some
prerequisite data on the use case the schema needs to support. Unlike relational
databases, DynamoDB is sharded by default, meaning that the data will live on multiple
servers behind the scenes so designing for data locality is important. We'll need to put
together the following list for each schema design:

- List of entities (ER Diagram)
- Estimated volumes and throughput for each entity
- Access patterns that need to be supported (queries and writes)
- Data retention requirements

###### Topics

- [Social network schema design in
  DynamoDB](data-modeling-schema-social-network.md "data-modeling-schema-social-network.md")
- [Gaming profile schema design in
  DynamoDB](data-modeling-schema-gaming-profile.md "data-modeling-schema-gaming-profile.md")
- [Complaint management system schema
  design in DynamoDB](data-modeling-complaint-management.md "data-modeling-complaint-management.md")
- [Recurring payments schema design in
  DynamoDB](data-modeling-schema-recurring-payments.md "data-modeling-schema-recurring-payments.md")
- [Monitoring device status updates in
  DynamoDB](data-modeling-device-status.md "data-modeling-device-status.md")
- [Using DynamoDB as a data store for an online
  shop](data-modeling-online-shop.md "data-modeling-online-shop.md")
