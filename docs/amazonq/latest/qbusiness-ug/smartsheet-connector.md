

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Smartsheet to Amazon Q Business
<a name="smartsheet-connector"></a>

Smartsheet is an enterprise work management platform that lets users manage projects, programs and processes at scale using sheets, channels, and workspaces. You can connect your Smartsheet instance to Amazon Q Business—using either the AWS Management Console, CLI, or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API—and create an Amazon Q Business web experience.

Integrating Smartsheet as a data source in Amazon Q Business enables users to quickly get insights from project sheets. For example, users can ask questions like:
+ "Which project manager is responsible for Project Harpo?", where the answer comes from a Smartsheet row
+ "What are the requirements for the Create APIs task?", where the answer is fetched from a PDF attached to the row for Create APIs
+ "Who is the owner of the Individual Task Management workspace?", where the answer comes from workspace metadata

With the Amazon Q Business Smartsheet connector, you can solve the following kinds of use cases.
+ **Project status updates** – Get quick insights into project health without having to open Smartsheet with questions like:
  + "What's the status of the website redesign project?"
  + "Is the mobile app launch on track for the planned date?" 
  + "Which projects are currently behind schedule in the Q3 Roadmap sheet?" 
+ **Task management** – Find information about tasks and action items with questions like:
  + "What tasks are assigned to Mary Major?"
  + "Has the marketing plan document been completed?" 
  + "What's the due date for the customer research presentation?"

The Amazon Q Business Smartsheet connector understands user access permissions and strictly enforces them at the time of the query. This ensures that users aren't able to see content they don't have access to.

**Note**  
We recommend enabling [Cross-region inference for Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html) for your Amazon Q Business application connector to get the best customer experience with improved query response accuracy.

**Topics**
+ [Known limitations for the Smartsheet connector](smartsheet-limitations.md)
+ [Prerequisites for connecting Amazon Q Business to Smartsheet](smartsheet-prereqs.md)
+ [Connecting Amazon Q Business to Smartsheet using the console](smartsheet-console.md)
+ [Connecting Amazon Q Business to Smartsheet using APIs](smartsheet-api.md)
+ [How Amazon Q Business connector crawls Smartsheet ACLs](smartsheet-user-management.md)
+ [IAM role for Smartsheet connector](smartsheet-iam-role.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).