# Prerequisites for connecting Amazon Q Business to Smartsheet

Before you begin, make sure that you have completed the following
prerequisites.

- **In Smartsheet, make sure you
  have:**
  - Access to the Smartsheet Event Reporting API. Use the [Events API Access Request](https://app.smartsheet.com/b/form/5db2cf1b981f445cabaa22d9421cc19d "https://app.smartsheet.com/b/form/5db2cf1b981f445cabaa22d9421cc19d") form to request access for your
    organization.
  - An Smartsheet system admin user or a licensed user for
    Smartsheet who can generate an access token. With this access
    token, your connector will have access to crawl all sheets and
    workspaces created by or shared with this user.
  - A Smartsheet access token. You need this to connect
    Smartsheet to Amazon Q Business. For information on how to
    generate this token in Smartsheet, see [Authentication and Access Tokens](https://smartsheet.redoc.ly/#section/API-Basics/Authentication-and-Access-Tokens "https://smartsheet.redoc.ly/#section/API-Basics/Authentication-and-Access-Tokens") in the
    _Smartsheet API Reference_.

- **In your AWS account, make sure you have:**

      + Created a Amazon Q Business application.
      + Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
      + Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
      + Stored your Smartsheet authentication credentials in an AWS Secrets Manager
       secret and, if using the Amazon Q API, noted the ARN of the
       secret.


      ###### Note

      If you’re a console user, you can create the IAM role and Secrets Manager
       secret as part of configuring your Amazon Q application on the
       console.

  For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
