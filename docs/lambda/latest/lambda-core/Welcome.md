# Welcome

**Overview**

AWS Lambda Core is a set of APIs for managing shared infrastructure resources used by Lambda. The
Lambda Core API provides operations for creating and managing network connectors that enable Lambda
MicroVMs to access resources in your Amazon Virtual Private Cloud (Amazon VPC).

Network connectors provision elastic network interfaces (ENIs) in your VPC subnets, providing a managed
network path from Lambda compute environments to private resources such as Amazon RDS databases,
Amazon ElastiCache clusters, and internal APIs. You create a network connector once and attach it to one or more
Lambda MicroVMs at run time.

The _AWS Lambda Core API Reference_ provides information about each of the API
methods, including details about the parameters in each API request and response.

You can use Software Development Kits (SDKs), Integrated Development Environment (IDE) Toolkits, and command
line tools to access the API. For installation instructions, see [Tools for
Amazon Web Services](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/").

For a list of Region-specific endpoints that Lambda supports, see [Lambda endpoints and quotas](../../../general/latest/gr/lambda-service.md "../../../general/latest/gr/lambda-service.md") in the
_AWS General Reference._

When making the API calls, you will need to authenticate your request by providing a signature. Lambda supports signature version 4. For more information, see [Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the
_AWS General Reference._

This document was last published on August 28, 2026.
