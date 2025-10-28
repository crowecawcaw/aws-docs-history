# Connecting Smartsheet to Amazon Q Business

Smartsheet is an enterprise work management platform that lets users manage
projects, programs and processes at scale using sheets, channels, and workspaces. You can
connect your Smartsheet instance to Amazon Q Business—using either the
AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q Business web experience.

Integrating Smartsheet as a data source in Amazon Q Business enables users
to quickly get insights from project sheets. For example, users can ask questions
like:

- "Which project manager is responsible for Project Harpo?", where the answer comes
  from a Smartsheet row
- "What are the requirements for the Create APIs task?", where the answer is fetched
  from a PDF attached to the row for Create APIs
- "Who is the owner of the Individual Task Management workspace?", where the answer
  comes from workspace metadata
  With the Amazon Q Business Smartsheet connector, you can solve the following
  kinds of use cases.

- **Project status updates** – Get quick
  insights into project health without having to open Smartsheet with
  questions like:
  - "What's the status of the website redesign project?"
  - "Is the mobile app launch on track for the planned date?"
  - "Which projects are currently behind schedule in the Q3 Roadmap sheet?"

- **Task management** – Find information about
  tasks and action items with questions like:

      + "What tasks are assigned to Mary Major?"
      + "Has the marketing plan document been completed?"
      + "What's the due date for the customer research presentation?"

  The Amazon Q Business Smartsheet connector understands user access
  permissions and strictly enforces them at the time of the query. This ensures that users
  aren't able to see content they don't have access to.

###### Note

We recommend enabling [Cross-region inference for Amazon Q Business](cross-region-inference.md "cross-region-inference.md") for your Amazon Q Business application connector to get the best customer experience with
improved query response accuracy.

###### Topics

- [Known limitations for the
  Smartsheet connector](smartsheet-limitations.md "smartsheet-limitations.md")
- [Prerequisites for connecting Amazon Q Business to Smartsheet](smartsheet-prereqs.md "smartsheet-prereqs.md")
- [Connecting Amazon Q Business to
  Smartsheet using the console](smartsheet-console.md "smartsheet-console.md")
- [Connecting Amazon Q Business to Smartsheet
  using APIs](smartsheet-api.md "smartsheet-api.md")
- [How Amazon Q Business connector
  crawls Smartsheet ACLs](smartsheet-user-management.md "smartsheet-user-management.md")
- [IAM role for
  Smartsheet connector](smartsheet-iam-role.md "smartsheet-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
