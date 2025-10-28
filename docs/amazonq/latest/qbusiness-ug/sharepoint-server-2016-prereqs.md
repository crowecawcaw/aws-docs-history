# Prerequisites for connecting Amazon Q Business to SharePoint Server 2016

The following page outlines the prerequisites you need to complete before connecting
SharePoint Server 2016 to Amazon Q, based on the authentication mode of your choice.

###### Topics

- [Prerequisites for using NTLM
  authentication](#sharepoint-server-2016-prereqs-ntlm "#sharepoint-server-2016-prereqs-ntlm")
- [Prerequisites for using Kerberos
  authentication](#sharepoint-server-2016-prereqs-kerberos "#sharepoint-server-2016-prereqs-kerberos")
- [Prerequisites for using
  SharePoint App-Only authentication](#sharepoint-server-2016-prereqs-app-only "#sharepoint-server-2016-prereqs-app-only")

## Prerequisites for using NTLM

authentication

**If you're using NTLM authentication, make sure you've
completed the following steps in SharePoint:**

- Copied your SharePoint instance URLs. The format for the host URL you
  enter is
  `https://yourdomain.sharepoint.com/sites/mysite`.
  Your URL must start with `https` and contain
  `sharepoint.com`.
- Copied the domain name of your SharePoint instance URL.
- Generated an SSL certificate and uploaded it to an Amazon S3 bucket.
- Noted the username and password that you use to connect to
  SharePoint.

**(Optional) If you're using **Email ID with Domain
from IDP** to control access to your documents, make sure you've
completed the following steps:**

- Copied your LDAP Server Endpoint (endpoint of LDAP server including
  protocol and port number). For example:
  `ldap://example.com:389`.
- Copied your LDAP Search Base (search base of the LDAP user). For example:
  `CN=Users,DC=sharepoint,DC=com`.
- Copied your LDAP username and LDAP password.

**(Optional) If using **Email ID with Custom
Domain** for access control, complete the following
step:**

- Noted your custom email domain value—for example:
  `"amazon.com"`.

**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your SharePoint Server 2016 authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.

For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

## Prerequisites for using Kerberos

authentication

**If you're using Kerberos authentication, make sure you've
completed the following steps in SharePoint:**

- Copied your SharePoint instance URLs. The format for the host URL you
  enter is
  `https://yourdomain.sharepoint.com/sites/mysite`.
  Your URL must start with `https` and contain
  `sharepoint.com`.
- Copied the domain name of your SharePoint instance URL.
- Generated an SSL certificate and uploaded it to an Amazon S3 bucket.
- Noted the username and password that you use to connect to
  SharePoint.

**(Optional) If you're using **Email ID with Domain
from IDP** to control access to your documents, make sure you've
completed the following steps:**

- Copied your LDAP Server Endpoint (endpoint of LDAP server including
  protocol and port number). For example:
  `ldap://example.com:389`.
- Copied your LDAP Search Base (search base of the LDAP user). For example:
  `CN=Users,DC=sharepoint,DC=com`.
- Copied your LDAP username and LDAP password.

**(Optional) If using **Email ID with Custom
Domain** for access control, complete the following
step:**

- Noted your custom email domain value—for example:
  `"amazon.com"`.

**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your SharePoint Server 2016 authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.

For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

## Prerequisites for using

SharePoint App-Only authentication

**If you're using SharePoint App-Only authentication, make
sure you've completed the following steps in SharePoint:**

- Copied the SharePoint client ID generated when you registered App Only at
  Site Level. ClientID format is ClientID@TenantId. For example,
  `ffa956f3-8f89-44e7-b0e4-49670756342c@888d0b57-69f1-4fb8-957f-e1f0bedf82fe`.
- Copied the SharePoint client secret generated when you registered App Only
  at Site Level.

###### Important

**Note:** Because client IDs and client
secrets are generated for single sites only when you register SharePoint
Server for App Only authentication, only one site URL is supported for
SharePoint App Only authentication.

- Noted the Tenant ID of your SharePoint account.
- Noted your **LDAP Server Endpoint**, **LDAP
  Search Base**, **LDAP username**, and
  **LDAP password**.

###### Note

SharePoint App-Only Authentication is _not_ supported for
SharePoint 2013 version.

**(Optional) If you're using **Email ID with Domain
from IDP** to control access to your documents, make sure you've
completed the following steps:**

- Copied your LDAP Server Endpoint (endpoint of LDAP server including
  protocol and port number). For example:
  `ldap://example.com:389`.
- Copied your LDAP Search Base (search base of the LDAP user). For example:
  `CN=Users,DC=sharepoint,DC=com`.
- Copied your LDAP username and LDAP password.

**(Optional) If using **Email ID with Custom
Domain** for access control, complete the following
step:**

- Noted your custom email domain value—for example:
  `"amazon.com"`.

**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your SharePoint Server 2016 authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.

For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
