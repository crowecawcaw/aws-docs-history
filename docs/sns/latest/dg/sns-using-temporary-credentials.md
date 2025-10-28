# Using temporary security credentials with

Amazon SNS

AWS Identity and Access Management (IAM) allows you to grant temporary security credentials to users and
applications that need access to your AWS resources. These temporary security
credentials are primarily used for IAM roles and federated access via industry-standard
protocols such as SAML and OpenID Connect (OIDC).

To effectively manage access to AWS resources, it's essential to understand
the following key concepts:

- **IAM Roles** – Roles are used to delegate access
  to AWS resources. Roles can be assumed by entities such as Amazon EC2 instances,
  Lambda functions, or users from other AWS accounts.
- **Federated Users** – These are users
  authenticated via external identity providers (IdPs) using SAML or OIDC. Federated access
  is recommended for human users, while IAM roles should be used for software
  applications.
- **Roles Anywhere** – For external applications
  requiring AWS access, you can use IAM Roles Anywhere to securely manage
  access without creating long-term credentials.
  You can use temporary security credentials to make requests to Amazon SNS. The SDKs and API
  libraries compute the necessary signature using these credentials to authenticate your
  requests. Requests with expired credentials will be denied by Amazon SNS.

For more information on temporary security credentials, refer to [Using IAM roles](../../../IAM/latest/UserGuide/id_roles_use.md "../../../IAM/latest/UserGuide/id_roles_use.md")
and [Providing access
to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the
_IAM User Guide_.

###### Example HTTPS request example

The following example demonstrates how to authenticate an Amazon SNS request using temporary
security credentials obtained from AWS Security Token Service (STS).

```
https://sns.us-east-2.amazonaws.com/
?Action=CreateTopic
&Name=My-Topic
&SignatureVersion=4
&SignatureMethod=AWS4-HMAC-SHA256
&Timestamp=2023-07-05T12:00:00Z
&X-Amz-Security-Token=SecurityTokenValue
&X-Amz-Date=20230705T120000Z
&X-Amz-Credential=`<your-access-key-id>`/20230705/us-east-2/sns/aws4_request
&X-Amz-SignedHeaders=host
&X-Amz-Signature=`<signature-value>`
```

###### Steps to authenticate the request

1. **Obtain Temporary Security Credentials** – Use
   AWS STS to assume a role or get federated user credentials. This will provide you with
   an access key ID, secret access key, and security token.
2. **Construct the Request** – Include the required
   parameters for your Amazon SNS action (for example, CreateTopic), and ensure you use HTTPS for
   secure communication.
3. **Sign the Request** – Use the AWS
   Signature Version 4 process to sign your request. This involves creating a canonical
   request, string-to-sign, and then calculating the signature. For more on AWS Signature Version 4, see [Use Signature Version 4
   signing](../../../ebs/latest/userguide/ebsapis-using-sigv4.md "../../../ebs/latest/userguide/ebsapis-using-sigv4.md") in the _Amazon EBS User Guide_.
4. **Send the Request** – Include the
   X-Amz-Security-Token in your request header to pass the temporary
   security credentials to Amazon SNS.
