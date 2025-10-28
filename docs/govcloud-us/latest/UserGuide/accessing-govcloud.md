# Accessing the AWS GovCloud (US) Regions

When you access the AWS GovCloud (US) Regions, use your AWS GovCloud (US) credentials.
Although your AWS GovCloud (US) account is associated with your standard AWS account, each
account has distinct credentials, where users from one account cannot access AWS
resources from the other account.

You can use any of the following methods to access and manage resources in
AWS GovCloud (US) Regions:

- The [AWS Management Console for the AWS GovCloud (US) Region](https://console.amazonaws-us-gov.com "https://console.amazonaws-us-gov.com")
  provides an easy-to-use graphical interface to manage your compute, storage, and
  other cloud resources. Most AWS products can be used with the console, and the
  console supports the majority of functionality for each service. You can sign in
  to the console only as an IAM user. For more information, see [Onboarding to AWS GovCloud (US) as a Solution
  Provider reselling in AWS GovCloud (US)](getting-started-console.md "getting-started-console.md").
- The **AWS command line interface (CLI)** allows
  you to control AWS services from a command line and automate commands through
  scripts. For more information about accessing the CLI for each service, see
  [AWS Command Line Tools](../../../general/latest/gr/GetTheTools.md "../../../general/latest/gr/GetTheTools.md") in
  the _AWS General Reference_.
- The **AWS SDK**s offer SDKs for a variety of
  languages. Some service operations that require computation of an md5 content
  hash, such as S3, may be unavailable or require additional code. The Sample Code
  and Libraries Catalog also provides a listing of code, SDKs, sample
  applications, and other tools available for use. For SDKs that leverage
  cryptography other than OpenSSL, such as Go, make sure you are following best
  practices for meeting compliance. Go leverages a built-in cryptography library
  that is not FIPS 140-3 validated.
- The **Toolkits for developers** provide
  programming libraries that help you quickly deploy your applications to AWS for
  Java or .NET. For more information, see [AWS Toolkit for Eclipse](https://aws.amazon.com/eclipse/ "https://aws.amazon.com/eclipse/") or [AWS Toolkit for Visual
  Studio](https://aws.amazon.com/visualstudio/ "https://aws.amazon.com/visualstudio/").
- You can construct **REST or Query API** calls to
  AWS services. For API syntax and examples, see the API references for each
  service at [https://docs.aws.amazon.com/](../../../index.md "../../../index.md").
