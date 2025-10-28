# Datavant Switchboard with AWS Clean Rooms

Publication date: **January 24, 2024 ([Diagram history](#diagram-history "#diagram-history"))**

Datavant’s data de-identification and tokenization tools enable healthcare and life sciences companies to replace their private patient information with an encrypted “token” that can’t be reverse-engineered to reveal sensitive information. These companies can leverage AWS Clean Rooms with collaborators to securely analyze and gain new insights from their collective datasets without sharing, copying, or moving one another’s underlying data outside of AWS.

## Datavant Switchboard with AWS Clean Rooms Diagram

![Reference architecture diagram showing how Datavant’s data de-identification and tokenization tools enable healthcare and life sciences companies to replace their private patient information with an encrypted “token” that can’t be reverse-engineered to reveal sensitive information. These companies can leverage AWS Clean Rooms with collaborators to securely analyze and gain new insights from their collective datasets without sharing, copying, or moving one another’s underlying data outside of AWS.](images/datavant-switchboard-with-aws-clean-rooms.png)

1. De-identify and tokenize data in an **Amazon Simple Storage Service** (Amazon S3) bucket by using Datavant Switchboard.
   Deploy the container through supported methods, including **AWS Fargate**,
   **Amazon Elastic Kubernetes Service** (Amazon EKS) and **Amazon Elastic Container Service** (Amazon ECS).
2. Link tokenized data with fellow collaborators through Datavant Switchboard and store the output
   in an **Amazon S3** bucket.
3. Leverage **AWS Glue crawler** to crawl linked, tokenized data.
   Prepare the data source for collaboration with **AWS Glue Data Catalog**.
4. The collaboration creator initiates **AWS Clean Rooms** and invites the
   member to the collaboration. Analysis rules are agreed upon and implemented. Members associate
   configured tables from **Data Catalog** and give
   **AWS Clean Rooms** service role to access their **AWS Glue** tables.
5. The member who can query leverages AGGREGATE and LIST functions across tables in the collaboration.
   Results can be exported to **Amazon S3** for the member who can receive query
   results
6. The member who can receive query results can leverage analytics services, including **Amazon Redshift**,
   **Amazon Athena**, **Amazon EMR**, **Amazon SageMaker AI**,
   and more to derive insights from newly enriched data sets.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/datavant-switchboard-with-aws-clean-rooms.md "samples/datavant-switchboard-with-aws-clean-rooms.md") which contains an editable PowerPoint.

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

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | January 24, 2024 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
