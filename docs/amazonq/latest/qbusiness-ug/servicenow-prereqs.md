# Prerequisites for connecting Amazon Q Business to ServiceNow Online

Before you begin, make sure that you have completed the following
prerequisites.

**In ServiceNow, make sure you
have:**

- Created a Personal or Enterprise Developer Instance and have a
  ServiceNow instance with an administrative role.
- Copied the host of your ServiceNow instance URL. The format for
  the host URL you enter is
  `your-domain.service-now.com`. You need your
  ServiceNow instance URL to connect to Amazon Q.
- Configured basic authentication credentials containing a username and
  password to allow Amazon Q to connect to your
  ServiceNow instance.
- **Optional:** Configured an OAuth 2.0 credential
  token that can identify Amazon Q using a username, password, and a
  generated client ID, and a client secret. For more information, see [ServiceNow documentation on OAuth 2.0 authentication](https://www.servicenow.com/docs/bundle/utah-platform-security/page/integrate/single-sign-on/concept/c_Authentication.html "https://www.servicenow.com/docs/bundle/utah-platform-security/page/integrate/single-sign-on/concept/c_Authentication.html")
  on the ServiceNow website.
- Depending on what you are searching for, you will need specific roles. Note
  that if you are searching through public articles, you don't require any
  specific role. Apply the following roles depending on your use case:

      + When searching Knowledge article documents in Amazon Q, the
       user should have any of the following roles - Knowledge,
       Knowledge\_Admin, and User\_Admin or Itil.
      + When searching Service Catalog documents in Amazon Q, the
       user should have a catalog role.
      + When searching the Incident document in Amazon Q, the user
       should have the incident\_manager role.

  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your ServiceNow Online authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

###### Note

For more information on connecting ServiceNow Online to Amazon Q Business,
see [Derive generative AI-powered insights from ServiceNow with Amazon Q
Business](https://aws.amazon.com/blogs/machine-learning/derive-generative-ai-powered-insights-from-servicenow-with-amazon-q-business/ "https://aws.amazon.com/blogs/machine-learning/derive-generative-ai-powered-insights-from-servicenow-with-amazon-q-business/") in the _AWS Machine Learning Blog_.
