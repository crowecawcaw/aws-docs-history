

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Share your enterprise data with data accessors using Amazon Q index
<a name="data-accessors"></a>

The Amazon Q Business data accessors feature allows you to securely share your enterprise data with verified independent software vendors (ISVs) using Amazon Q. This feature allows ISVs to retrieve relevant content from your Amazon Q index, enhancing their applications with your organization's knowledge. By granting controlled access to your data, you can leverage third-party tools while maintaining security and data access compliance.

DataAccessor supports two types of authorization patterns to access ISVs end user data on Amazon Q:
+  [Authorization Code](https://aws.amazon.com/about-aws/whats-new/2024/05/aws-iam-identity-pkce-authorizations-aws-applications/)

   AWS IAM Identity Center supports OAuth 2.0 authorization code flows using the Proof Key for Code Exchange (PKCE) standard. This provides AWS applications, such as Amazon Q Business, a simple and safe way to authenticate users and obtain their consent to access Amazon Q Business resources from desktops and mobile devices with web browsers.
+ [Trusted token issuer/App level authentication](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.html#trusted-token-issuer-overview) 
  + A trusted token issuer is an OAuth 2.0 authorization server that creates signed tokens. These tokens authorize applications that initiate requests (requesting applications) for access to AWS managed applications (receiving applications).
  +  [Consideration for granting an ISV with trusted token issuer based authorization](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.html#trusted-token-issuer-overview) 

This topic discusses how an Amazon Q Business administrator can connect to one of the supported data accessors.

**Topics**
+ [A list of verified software providers who are data accessors](data-accessors-list.md)
+ [Prerequisites](data-accessors-prerequisites.md)
+ [Add a data accessor (ISV) to connect to your Amazon Q index](data-accessors-granting-permissions.md)
+ [Completing the process to add a data accessor](data-accessors-external-setup.md)
+ [Deleting or removing a data accessor's access from your Amazon Q index](data-accessors-removing-access.md)