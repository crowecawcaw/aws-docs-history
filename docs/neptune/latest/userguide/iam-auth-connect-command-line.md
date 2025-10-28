# Connecting to Amazon Neptune databases using IAM authentication from the command line

Having a command-line tool for submitting queries to your Neptune DB cluster
is very handy, as illustrated in many of the examples in this documentation. The [curl](https://curl.haxx.se/ "https://curl.haxx.se/") tool is an excellent option for communicating
with Neptune endpoints if IAM authentication is not enabled.

**However, to keep your data secure it is best to enable
IAM authentication.**

When IAM authentication is enabled, every request must be [signed using Signature Version 4
(Sig4)](../../../general/latest/gr/signing-aws-api-requests.md "../../../general/latest/gr/signing-aws-api-requests.md"). The third-party [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl")
command-line tool uses the same syntax as `curl`, and can sign queries
using Sig4 signing. The [Using awscurl](#iam-auth-connect-awscurl "#iam-auth-connect-awscurl") section below explains how to use
`awscurl` securely with temporary credentials.

## Setting up a command-line tool to use HTTPS

Neptune requires that all connections use HTTPS. Any command line tool like
`curl` or `awscurl` needs access to appropriate certificates
in order to use HTTPS. As long as `curl` or `awscurl` can
locate the appropriate certificates, they handle HTTPS connections just like HTTP
connections, without needing extra parameters. Examples in this documentation are
based on that scenario.

To learn how to obtain such certificates and how to format them properly into
a certificate authority (CA) certificate store that `curl` can use, see
[SSL Certificate Verification](https://curl.haxx.se/docs/sslcerts.html "https://curl.haxx.se/docs/sslcerts.html")
in the `curl` documentation.

You can then specify the location of this CA certificate store using the
`CURL_CA_BUNDLE` environment variable. On Windows, `curl`
automatically looks for it in a file named `curl-ca-bundle.crt`. It looks first in
the same directory as `curl.exe` and then elsewhere on the path. For more
information, see [SSL Certificate
Verification](https://curl.haxx.se/docs/sslcerts.html "https://curl.haxx.se/docs/sslcerts.html").

## Using `awscurl` with temporary

credentials to securely connect to a DB cluster with IAM authentication enabled

The [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl") tool uses
the same syntax as `curl`, but needs additional information as well:

- **`--access_key`**   –  
  A valid access key. If not supplied using this parameter, it must be supplied
  in the `AWS_ACCESS_KEY_ID` enviroment variable, or in a
  configuration file.
- **`--secret_key`**   –  
  A valid secret key corresponding to the access key. If not supplied using
  this parameter, it must be supplied in the `AWS_SECRET_ACCESS_KEY`
  enviroment variable, or in a configuration file.
- **`--security_token`**   –  
  A valid session token. If not supplied using this parameter, it must be
  supplied in the `AWS_SECURITY_TOKEN` enviroment variable, or in
  a configuration file.

In the past, it was common practice to use persistent credentials with
`awscurl`, such as IAM user credentials or even root credentials,
but this is not recommended. Instead, generate temporary credentials using
one of the [AWS
Security Token Service (STS) APIs](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md"), or one of their [AWS CLI wrappers](../../../cli/latest/reference/sts/index.md "../../../cli/latest/reference/sts/index.md").

It is best to place the `AccessKeyId`, `SecretAccessKey`,
and `SessionToken` values that are returned by the STS call
into appropriate environment variables in your shell session rather than into
a configuration file. Then, when the shell terminates, the credentials are
automatically discarded, which is not the case with a configuration file.
Similarly, don't request a longer duration for the temporary credentials
than you are likely to need.

The following example shows the steps you might take in a Linux shell to
obtain temporary credentials that are good for half an hour using [sts assume-role](../../../cli/latest/reference/sts/assume-role.md "../../../cli/latest/reference/sts/assume-role.md"), and then
place them in environment variables where `awscurl` can find them:

```
aws sts assume-role \
    --duration-seconds 1800 \
    --role-arn "arn:aws:iam::`(account-id)`:role/`(rolename)`" \
    --role-session-name AWSCLI-Session > $output
AccessKeyId=$(cat $output | jq '.Credentials''.AccessKeyId')
SecretAccessKey=$(cat $output | jq '.Credentials''.SecretAccessKey')
SessionToken=$(cat $output | jq '.Credentials''.SessionToken')

export AWS_ACCESS_KEY_ID=$AccessKeyId
export AWS_SECRET_ACCESS_KEY=$SecretAccessKey
export AWS_SESSION_TOKEN=$SessionToken
```

You could then use `awscurl` to make a signed request to your
DB cluster something like this:

```
awscurl `(your cluster endpoint)`:8182/status \
    --region us-east-1 \
    --service neptune-db
```
