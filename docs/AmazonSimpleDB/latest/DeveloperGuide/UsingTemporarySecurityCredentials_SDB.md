# Using Temporary Security Credentials

In addition to creating users with their own security credentials, IAM also
enables you to grant temporary security credentials to any user to allow the user to
access your AWS services and resources. You can manage users for your system who do not have
AWS accounts; these users are called federated users. Additionally, "users" can also be
applications that you create to access your AWS resources.

You can use these temporary security credentials to make requests to Amazon SimpleDB. Replace
your usual `AWSAccessKeyId` parameter with the one provided by IAM,
add the IAM `SecurityToken` as a new parameter, and sign the
request with the `SecretKeyId` provided by IAM. If you send
requests using expired credentials Amazon SimpleDB denies the request.

For more information about IAM support for temporary security credentials, go to
[Granting Temporary Access to Your AWS Resources](../../../IAM/latest/UserGuide/TokenBasedAuth.md "../../../IAM/latest/UserGuide/TokenBasedAuth.md") in _Using
IAM_.

###### Example Using Temporary Security Credentials to Authenticate an Amazon SimpleDB Request

The following example demonstrates the wire protocol for using temporary security
credentials to authenticate an Amazon SimpleDB request over HTTPS.

```

https://sdb.amazonaws.com/
?Action=GetAttributes
&AWSAccessKeyId=`Access Key ID provided by AWS Security Token Service`
&DomainName=MyDomain
&ItemName=JumboFez
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=`Signature calculated using the SecretKeyId provided by AWS Security Token Service`
&SecurityToken=`Security Token Value`
```

###### Note

provides support for temporary security credentials and session tokens in
the AWS SDKs so you can implement temporary security credentials or session tokens
with a specific programming language. Each SDK has its own instructions for
implementing this feature. For a current list of AWS SDKs that support this feature,
see [Ways to Access the AWS Security Token Service](../../../IAM/latest/UserGuide/AccessingSTS.md "../../../IAM/latest/UserGuide/AccessingSTS.md"). Non-AWS products and
services should have their own documentation about supporting temporary credentials
and session tokens, if available.
