# Protegrity Data Protection for Amazon S3 and Snowflake

Publication date: **October 12, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture shows how Protegrity on AWS can be used to protect sensitive data in Amazon S3 and then show the same data as clear text based on permissions from Snowflake.

## Protegrity Data Protection for Amazon S3 and Snowflake Diagram

![Reference architecture diagram showing how Protegrity on AWS can be used to protect sensitive data in Amazon S3 and then show the same data as clear text based on permissions from Snowflake.](images/protegrity-data-protection-for-amazon-s3-and-snowflake.png)

1. External Files are sent to an **Amazon S3** (Amazon S3)
   input bucket by **AWS DataSync**.
2. The **Amazon S3** Protegrity accelerator that was
   built using **AWS Lambda** is initiated
   by an **Amazon S3** event. The accelerator
   reads the data from the **Amazon S3** bucket
   and invokes the Protegrity Cloud API protector.
3. Protegrity Cloud API protector, which was built using **Lambda**,
   applies data protection on the data. The Protegrity Cloud API protector
   returns protected (encrypted or tokenized) data if the passed user has
   the right permissions.
4. The **Amazon S3** Protegrity accelerator receives
   the protected data and creates a new object in the output **Amazon S3**
   bucket (data lake). Optionally, data is deleted from the raw data bucket.
5. Data from the **Amazon S3** data lake is loaded
   into a Snowflake table by a Snowflake virtual warehouse. A masking policy
   is applied on that table.
6. When a user queries a dataset containing protected data, Snowflake’s
   masking policy invokes the Protegrity Snowflake protector by using
   an external function. This process is managed by a Snowflake virtual
   warehouse. It’s worth noting the distinct workload isolation and immediate
   scaling capability of Snowflake, as demonstrated in steps 5 and 6, through
   independently scalable virtual warehouses.
7. The Snowflake external function call goes through **Amazon API Gateway**.
   The authorization of this service is achieved using Snowflake’s API integration
   object, which encompasses **API Gateway** and trusted
   roles created for REST API egress from Snowflake's **Amazon Virtual Private Cloud** (Amazon VPC) to the
   customer’s AWS account. The Protegrity protector returns clear text data for
   users with the right permissions.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/protegrity-data-protection-for-amazon-s3-and-snowflake.md "samples/protegrity-data-protection-for-amazon-s3-and-snowflake.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [Protegrity](https://www.protegrity.com/ "https://www.protegrity.com/")
- [Snowflake](https://www.snowflake.com/ "https://www.snowflake.com/")

## Contributors

Contributors to this reference architecture diagram include:

- Venkatesh Aravamudan, Partner Solutions Architect, Amazon Web Services
- Bosco Albuquerque, Senior Partner Solutions Architect, Amazon Web Services
- Tamara Astakhova, Senior Partner Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | October 12, 2023 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
