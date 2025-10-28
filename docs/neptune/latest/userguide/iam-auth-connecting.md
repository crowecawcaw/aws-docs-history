# Connecting to your Amazon Neptune database using AWS Identity and Access Management authentication

Amazon Neptune resources that have IAM DB authentication enabled require all HTTP
requests to be signed using AWS Signature Version 4. For general information about signing
requests with AWS Signature Version 4, see [Signing AWS API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md").

AWS Signature Version 4 is the process to add authentication information to AWS
requests. For security, most requests to AWS must be signed with an access key, which
consists of an access key ID and secret access key.

###### Note

If you are using temporary credentials, they expire after a specified interval,
_including the session token_.

You must update your session token when you request new credentials. For more
information, see [Using Temporary Security Credentials to Request Access to AWS Resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md").

###### Important

Accessing Neptune with IAM-based authentication requires that you create HTTP requests
and sign the requests yourself.

###### How Signature Version 4 Works

1. You create a canonical request.
2. You use the canonical request and some other information to create a
   string-to-sign.
3. You use your AWS secret access key to derive a signing key, and then use that
   signing key and the string-to-sign to create a signature.
4. You add the resulting signature to the HTTP request in a header or as a query string
   parameter.
   When Neptune receives the request, it performs the same steps that you did to calculate
   the signature. Neptune then compares the calculated signature to the one you sent with the
   request. If the signatures match, the request is processed. If the signatures don't match, the
   request is denied.

For general information about signing requests with AWS Signature Version 4, see [Signature
Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _AWS General Reference_.

The following sections contain examples that show how to send signed requests to the
Gremlin and SPARQL endpoints of a Neptune DB instance with IAM authentication enabled.

###### Topics

- [Prerequisites for connecting Amazon Neptune databases using IAM authentication](iam-auth-connect-prerq.md "iam-auth-connect-prerq.md")
- [Connecting to Amazon Neptune databases using IAM authentication from the command line](iam-auth-connect-command-line.md "iam-auth-connect-command-line.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Gremlin console](iam-auth-connecting-gremlin-console.md "iam-auth-connecting-gremlin-console.md")
- [Connecting to Amazon Neptune databases using IAM with
  Gremlin Java](iam-auth-connecting-gremlin-java.md "iam-auth-connecting-gremlin-java.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Java and
  SPARQL](iam-auth-connecting-sparql-java.md "iam-auth-connecting-sparql-java.md")
- [Connecting to Amazon Neptune databases using IAM authentication with SPARQL
  and Node.js](iam-auth-connecting-sparql-node.md "iam-auth-connecting-sparql-node.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Gremlin Python](gremlin-python-iam-auth.md "gremlin-python-iam-auth.md")
- [Connecting to Amazon Neptune databases using IAM
  authentication with Gremlin JavaScript](gremlin-javascript-iam-auth.md "gremlin-javascript-iam-auth.md")
- [Connecting to Amazon Neptune databases using IAM
  authentication with Gremlin Go](gremlin-go-iam-auth.md "gremlin-go-iam-auth.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Gremlin .NET](gremlin-dotnet-iam-auth.md "gremlin-dotnet-iam-auth.md")
