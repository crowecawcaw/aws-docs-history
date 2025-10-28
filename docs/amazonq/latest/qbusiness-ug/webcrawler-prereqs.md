# Prerequisites for connecting Amazon Q Business to Web Crawler

Before you begin, make sure that you have completed the following
prerequisites.

###### Note

For more information on connecting Web Crawler to Amazon Q Business,
see [Index website contents using the Amazon Q Web Crawler connector for
Amazon Q Business](https://aws.amazon.com/blogs/machine-learning/index-website-contents-using-the-amazon-q-web-crawler-connector-for-amazon-q-business/ "https://aws.amazon.com/blogs/machine-learning/index-website-contents-using-the-amazon-q-web-crawler-connector-for-amazon-q-business/") in the _AWS Machine Learning
Blog_.

**For Amazon Q Web Crawler, make sure you
have:**

- Copied the seed or sitemap URLs of the websites that you want to index and
  stored them in a text file or an Amazon S3 bucket. Each URL must be
  included on a separate line.
- **For XML sitemaps:** Copied the sitemap XML and
  saved it in an XML file in an Amazon S3 bucket. You can also combine
  multiple sitemap XML files into a .zip file.
- **For websites that require basic, NTLM, or Kerberos
  authentication:**
  - Noted your website authentication credentials, which include a
    username and password.

  ###### Note

  Amazon Q Web Crawler supports the NTLM authentication
  protocol that includes password hashing, and Kerberos authentication
  protocol that includes password encryption.

- **For websites that require SAML or login form
  authentication:**
  - Noted your website authentication credentials, which include a
    username and password.
  - Copied the XPaths (XML Path Language) of the username field (and the
    username button if using SAML), password field and button, and copied
    the login page URL. You can find the XPaths of elements using your web
    browser’s developer tools. XPaths follow this format:
    `//tagname[@Attribute='Value']`.

  ###### Note

  Amazon Q Web Crawler uses a headless
  Chrome browser and the information from the form
  to authenticate and authorize access with an OAuth 2.0 protected
  URL.

- **Optional:** Copied the host name and the port
  number of the web proxy server if you want to use a web proxy to connect to
  internal websites that you want to crawl. The web proxy must be public facing.
  Amazon Q supports connecting to web proxy servers backed by basic
  authentication, or you can connect with no authentication.
- **Optional:** Copied the virtual private cloud
  (VPC) subnet ID if you want to use a VPC to connect to internal websites you
  want to crawl. For more information, see [Using Amazon VPC](connector-vpc.md "connector-vpc.md").
  **In your AWS account, make sure you have:**

- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the API,
  noted the ARN of the IAM role.
- **For websites that require authentication credentials to
  crawl:** Stored your Web Crawler authentication credentials in an
  AWS Secrets Manager secret and, if using the API, noted the ARN of the secret.

###### Note

If you’re a console user, you can create the IAM role and
Secrets Manager secret as part of configuring your Amazon Q application environment on the console.
