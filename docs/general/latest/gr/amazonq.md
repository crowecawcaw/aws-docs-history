# Amazon Q Business endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service regions and endpoints

The following table shows the AWS Regions and endpoints currently supported by
Amazon Q Business.

| Region name           | Region         | Endpoint                                                                       | Protocol |
| --------------------- | -------------- | ------------------------------------------------------------------------------ | -------- |
| US East (N. Virginia) | us-east-1      | qbusiness.us-east-1.api.aws                                                    | HTTPS    |
| US West (Oregon)      | us-west-2      | qbusiness.us-west-2.api.aws                                                    | HTTPS    |
| Europe (Ireland)      | eu-west-1      | qbusiness.eu-west-1.api.aws<br>qbusiness-websocket.eu-west-1.api.aws           | HTTPS    |
| Asia Pacific (Sydney) | ap-southeast-2 | qbusiness.ap-southeast-2.api.aws<br>qbusiness-websocket.ap-southeast-2.api.aws | HTTPS    |

###### Note

The Europe (Ireland) and the Asia Pacific (Sydney) regions don't currently support all
features available in the US regions, such as Q App, Q Actions, and Audio/Video
files. While these features will become available soon, Amazon Q Business customers in this
region can do the following:

- Get answers to questions submitted to the enterprise retrieval augmented generation system.
- Generate content through Amazon Q Business assistant
- Access capabilities such as embedded images in files.
- Perform tabular search on small tables.
- Ingest data from scanned PDFs.
- Answer questions from data in scanned PDFs.
- Respond to queries to LLM knowledge.

## Service quotas

The following table shows the quotas that are related to Amazon Q Business for your
AWS account.

| Name           | Description                                      | Default | Adjustable |
| -------------- | ------------------------------------------------ | ------- | ---------- |
| Applications   | Maximum number of applications per account       | 50      | No         |
| Data sources   | Maximum number of data sources per application   | 50      | No         |
| Data accessors | Maximum number of data accessors per application | 10      | No         |
| Plugins        | Maximum number of plugins per application        | 25      | No         |
| Actions        | Maximum number of actions per plugin             | 20      | No         |
