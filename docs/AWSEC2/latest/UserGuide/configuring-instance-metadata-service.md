# Use the Instance Metadata Service to access instance metadata

You can access instance metadata from a running instance using one of the following
methods:

- Instance Metadata Service Version 2 (IMDSv2) – a session-oriented method

For examples, see [Examples for IMDSv2](#instance-metadata-retrieval-examples "#instance-metadata-retrieval-examples").

- Instance Metadata Service Version 1 (IMDSv1) – a request/response method

For examples, see [Examples for IMDSv1](#instance-metadata-retrieval-examples-imdsv1 "#instance-metadata-retrieval-examples-imdsv1").
By default, you can use either IMDSv1 or IMDSv2, or both.

You can configure the Instance Metadata Service (IMDS) on each instance so that local code
or users must use IMDSv2. When you specify that IMDSv2 must be used,
IMDSv1 no longer works. For information about how to configure your instance to
use IMDSv2, see [Configure the Instance Metadata Service
options](configuring-instance-metadata-options.md "configuring-instance-metadata-options.md").

The `PUT` or `GET` headers are unique to IMDSv2. If
these headers are present in the request, then the request is intended for
IMDSv2. If no headers are present, it is assumed the request is intended for
IMDSv1.

For an extensive review of IMDSv2, see [Add defense in depth against open firewalls, reverse proxies, and SSRF
vulnerabilities with enhancements to the EC2 Instance Metadata
Service](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/ "https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/").

###### Topics

- [How Instance Metadata Service Version 2 works](#instance-metadata-v2-how-it-works "#instance-metadata-v2-how-it-works")
- [Use a supported AWS
  SDK](#use-a-supported-sdk-version-for-imdsv2 "#use-a-supported-sdk-version-for-imdsv2")
- [Examples for IMDSv2](#instance-metadata-retrieval-examples "#instance-metadata-retrieval-examples")
- [Examples for IMDSv1](#instance-metadata-retrieval-examples-imdsv1 "#instance-metadata-retrieval-examples-imdsv1")

## How Instance Metadata Service Version 2 works

IMDSv2 uses session-oriented requests. With session-oriented requests, you
create a session token that defines the session duration, which can be a minimum of
one second and a maximum of six hours. During the specified duration, you can use
the same session token for subsequent requests. After the specified duration
expires, you must create a new session token to use for future requests.

###### Note

The examples in this section use the IPv4 address of the Instance Metadata Service
(IMDS): `169.254.169.254`. If you are retrieving instance
metadata for EC2 instances over the IPv6 address, ensure that you enable and use
the IPv6 address instead: `[fd00:ec2::254]`. The IPv6 address of the
IMDS is compatible with IMDSv2 commands. The IPv6 address is
only accessible on [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type") in an [IPv6-supported subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-ip-address-range "../../../vpc/latest/userguide/configure-subnets.md#subnet-ip-address-range") (dual stack or IPv6 only).

The following examples use a shell script and IMDSv2 to retrieve the
top-level instance metadata items. Each example:

- Creates a session token lasting six hours (21,600 seconds) using the
  `PUT` request
- Stores the session token header in a variable named `TOKEN`
  (Linux instances) or `token` (Windows instances)
- Requests the top-level metadata items using the token

You can run two separate commands, or combine them.

**Separate commands**

First, generate a token using the following command.

```
`[ec2-user ~]$` TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
```

Then, use the token to generate top-level metadata items using the
following command.

```
`[ec2-user ~]$` curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/
```

**Combined commands**

You can store the token and combine the commands. The following example
combines the above two commands and stores the session token header in a
variable named TOKEN.

###### Note

If there is an error in creating the token, instead of a valid token,
an error message is stored in the variable, and the command will not
work.

```
`[ec2-user ~]$` TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
	&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/
```

After you've created a token, you can reuse it until it expires. In the
following example command, which gets the ID of the AMI used to launch the
instance, the token that is stored in `$TOKEN` in the previous
example is reused.

```
`[ec2-user ~]$` curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ami-id
```

```
`PS C:\>` [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
`PS C:\>` Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/
```

After you've created a token, you can reuse it until it expires. In the
following example command, which gets the ID of the AMI used to launch the
instance, the token that is stored in `$token` in the previous
example is reused.

```
`PS C:\>` Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
	-Method GET -uri http://169.254.169.254/latest/meta-data/ami-id
```

When you use IMDSv2 to request instance metadata, the request must include
the following:

1. Use a `PUT` request to initiate a session to the instance
   metadata service. The `PUT` request returns a token that must be
   included in subsequent `GET` requests to the instance metadata
   service. The token is required to access metadata using
   IMDSv2.
2. Include the token in all `GET` requests to the IMDS.
   When token usage is set to `required`, requests without a valid
   token or with an expired token receive a `401 - Unauthorized`
   HTTP error code.
   - The token is an instance-specific key. The token is not valid on
     other EC2 instances and will be rejected if you attempt to use it
     outside of the instance on which it was generated.
   - The `PUT` request must include a header that specifies
     the time to live (TTL) for the token, in seconds, up to a maximum of
     six hours (21,600 seconds). The token represents a logical session.
     The TTL specifies the length of time that the token is valid and,
     therefore, the duration of the session.
   - After a token expires, to continue accessing instance metadata,
     you must create a new session using another `PUT`.
   - You can choose to reuse a token or create a new token with every
     request. For a small number of requests, it might be easier to
     generate and immediately use a token each time you need to access
     the IMDS. But for efficiency, you can specify a longer
     duration for the token and reuse it rather than having to write a
     `PUT` request every time you need to request instance
     metadata. There is no practical limit on the number of concurrent
     tokens, each representing its own session. IMDSv2 is,
     however, still constrained by normal IMDS connection and
     throttling limits. For more information, see [Query throttling](instancedata-data-retrieval.md#instancedata-throttling "instancedata-data-retrieval.md#instancedata-throttling").

HTTP `GET` and `HEAD` methods are allowed in IMDSv2
instance metadata requests. `PUT` requests are rejected if they contain
an X-Forwarded-For header.

By default, the response to `PUT` requests has a response hop limit
(time to live) of `1` at the IP protocol level. If you need a bigger hop
limit, you can adjust it by using the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") AWS CLI command. For example, you might
need a bigger hop limit for backward compatibility with container services running
on the instance. For more information, see [Modify instance metadata
options for existing instances](configuring-IMDS-existing-instances.md "configuring-IMDS-existing-instances.md").

## Use a supported AWS

SDK

To use IMDSv2, your EC2 instances must use an AWS SDK version that
supports using IMDSv2. The latest versions of all the AWS SDKs support
using IMDSv2.

###### Important

We recommend that you to stay up to date with SDK releases to keep up with the
latest features, security updates, and underlying dependencies. Continued use of
an unsupported SDK version is not recommended and is done at your discretion.
For more information, see the [AWS SDKs and Tools maintenance
policy](../../../sdkref/latest/guide/maint-policy.md "../../../sdkref/latest/guide/maint-policy.md") in the _AWS SDKs and Tools Reference Guide_.

The following are the minimum versions that support using IMDSv2:

- [AWS CLI](https://github.com/aws/aws-cli "https://github.com/aws/aws-cli") –
  1.16.289
- [AWS Tools for Windows PowerShell](https://github.com/aws/aws-tools-for-powershell "https://github.com/aws/aws-tools-for-powershell") – 4.0.1.0
- [AWS SDK for .NET](https://github.com/aws/aws-sdk-net "https://github.com/aws/aws-sdk-net") –
  3.3.634.1
- [AWS SDK for C++](https://github.com/aws/aws-sdk-cpp "https://github.com/aws/aws-sdk-cpp") –
  1.7.229
- [AWS SDK for Go](https://github.com/aws/aws-sdk-go "https://github.com/aws/aws-sdk-go") –
  1.25.38
- [AWS SDK for Go
  v2](https://github.com/aws/aws-sdk-go-v2 "https://github.com/aws/aws-sdk-go-v2") – 0.19.0
- [AWS SDK for Java](https://github.com/aws/aws-sdk-java "https://github.com/aws/aws-sdk-java")
  – 1.11.678
- [AWS SDK for Java 2.x](https://github.com/aws/aws-sdk-java-v2 "https://github.com/aws/aws-sdk-java-v2")
  – 2.10.21
- [AWS SDK for JavaScript in Node.js](https://github.com/aws/aws-sdk-js "https://github.com/aws/aws-sdk-js") –
  2.722.0
- [AWS SDK for Kotlin](https://github.com/awslabs/aws-sdk-kotlin "https://github.com/awslabs/aws-sdk-kotlin") – 1.1.4
- [AWS SDK for PHP](https://github.com/aws/aws-sdk-php "https://github.com/aws/aws-sdk-php") –
  3.147.7
- [AWS SDK for Python
  (Botocore)](https://github.com/boto/botocore "https://github.com/boto/botocore") – 1.13.25
- [AWS SDK for Python (Boto3)](https://github.com/boto/boto3 "https://github.com/boto/boto3") –
  1.12.6
- [AWS SDK for Ruby](https://github.com/aws/aws-sdk-ruby "https://github.com/aws/aws-sdk-ruby")
  – 3.79.0

## Examples for IMDSv2

Run the following examples on your Amazon EC2 instance to retrieve the instance metadata
for IMDSv2.

On Windows instances, you can use Windows PowerShell or you can install cURL or wget.
If you install a third-party tool on a Windows instance, ensure that you read the
accompanying documentation carefully, as the calls and the output might be different
from what is described here.

###### Examples

- [Get the available versions of the instance metadata](#instance-metadata-ex-1 "#instance-metadata-ex-1")
- [Get the top-level metadata items](#instance-metadata-ex-2 "#instance-metadata-ex-2")
- [Get the values for metadata items](#instance-metadata-ex-2a "#instance-metadata-ex-2a")
- [Get the list of available public keys](#instance-metadata-ex-3 "#instance-metadata-ex-3")
- [Show the formats in which public key 0 is available](#instance-metadata-ex-4 "#instance-metadata-ex-4")
- [Get public key 0 (in the OpenSSH key format)](#instance-metadata-ex-5 "#instance-metadata-ex-5")
- [Get the subnet ID for an instance](#instance-metadata-ex-6 "#instance-metadata-ex-6")
- [Get the instance tags for an instance](#instance-metadata-ex-7 "#instance-metadata-ex-7")

### Get the available versions of the instance metadata

This example gets the available versions of the instance metadata. Each
version refers to an instance metadata build when new instance metadata
categories were released. The instance metadata build versions do not correlate
with the Amazon EC2 API versions. The earlier versions are available to you in case
you have scripts that rely on the structure and information present in a
previous version.

cURL

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/`
`1.0
2007-01-19
2007-03-01
2007-08-29
2007-10-10
2007-12-15
2008-02-01
2008-09-01
2009-04-04
2011-01-01
2011-05-01
2012-01-12
2014-02-25
2014-11-05
2015-10-20
2016-04-19
...
latest`
```

PowerShell

```
`PS C:\>` `[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/`
`1.0
2007-01-19
2007-03-01
2007-08-29
2007-10-10
2007-12-15
2008-02-01
2008-09-01
2009-04-04
2011-01-01
2011-05-01
2012-01-12
2014-02-25
2014-11-05
2015-10-20
2016-04-19
...
latest`
```

### Get the top-level metadata items

This example gets the top-level metadata items. For more information about the items in
the response, see [Instance metadata categories](ec2-instance-metadata.md#instancedata-data-categories "ec2-instance-metadata.md#instancedata-data-categories").

Note that tags are included in this output only if you've allowed access. For more
information, see [Enable access to tags in instance metadata](work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS").

cURL

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/`
`ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
tags/`
```

PowerShell

```
`PS C:\>` `[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/`
`ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
iam/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
tags/`
```

### Get the values for metadata items

These examples get the values of some of the top-level metadata items that were obtained
in the preceding example. These requests use the stored token that was created using the
command in the previous example. The token must not be expired.

cURL

```
`[ec2-user ~]$` `curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ami-id`
`ami-0abcdef1234567890`
```

```
`[ec2-user ~]$` `curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/reservation-id`
`r-0efghijk987654321`
```

```
`[ec2-user ~]$` `curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/local-hostname`
`ip-10-251-50-12.ec2.internal`
```

```
`[ec2-user ~]$` `curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-hostname`
`ec2-203-0-113-25.compute-1.amazonaws.com`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/ami-id`
`ami-0abcdef1234567890`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/reservation-id`
`r-0efghijk987654321`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/local-hostname`
`ip-10-251-50-12.ec2.internal`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-hostname`
`ec2-203-0-113-25.compute-1.amazonaws.com`
```

### Get the list of available public keys

This example gets the list of available public keys.

cURL

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-keys/`
`0=my-public-key`
```

PowerShell

```
`PS C:\>` `[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/`
`0=my-public-key`
```

### Show the formats in which public key 0 is available

This example shows the formats in which public key 0 is available.

cURL

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-keys/0/`
`openssh-key`
```

PowerShell

```
`PS C:\>` `[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key`
`openssh-key`
```

### Get public key 0 (in the OpenSSH key format)

This example gets public key 0 (in the OpenSSH key format).

cURL

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key`
`ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key`
```

PowerShell

```
`PS C:\>` `[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key`
`ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key`
```

### Get the subnet ID for an instance

This example gets the subnet ID for an instance.

cURL

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/network/interfaces/macs/02:29:96:8f:6a:2d/subnet-id`
`subnet-be9b61d7`
```

PowerShell

```
`PS C:\>` `[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token`
```

```
`PS C:\>` `Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/network/interfaces/macs/02:29:96:8f:6a:2d/subnet-id`
`subnet-be9b61d7`
```

### Get the instance tags for an instance

If access to instance tags in the instance metadata is turned on, you can get the
tags for a instance from instance metadata. For more information, see
[Retrieve tags from instance metadata](work-with-tags-in-IMDS.md#retrieve-tags-from-IMDS "work-with-tags-in-IMDS.md#retrieve-tags-from-IMDS").

## Examples for IMDSv1

Run the following examples on your Amazon EC2 instance to retrieve the instance metadata
for IMDSv1.

On Windows instances, you can use Windows PowerShell or you can install cURL or wget.
If you install a third-party tool on a Windows instance, ensure that you read the
accompanying documentation carefully, as the calls and the output might be different
from what is described here.

###### Examples

- [Get the available versions of the instance metadata](#instance-metadata-ex-1-imdsv1 "#instance-metadata-ex-1-imdsv1")
- [Get the top-level metadata items](#instance-metadata-ex-2-imdsv1 "#instance-metadata-ex-2-imdsv1")
- [Get the values for metadata items](#instance-metadata-ex-2a-imdsv1 "#instance-metadata-ex-2a-imdsv1")
- [Get the list of available public keys](#instance-metadata-ex-3-imdsv1 "#instance-metadata-ex-3-imdsv1")
- [Show the formats in which public key 0 is available](#instance-metadata-ex-4-imdsv1 "#instance-metadata-ex-4-imdsv1")
- [Get public key 0 (in the OpenSSH key format)](#instance-metadata-ex-5-imdsv1 "#instance-metadata-ex-5-imdsv1")
- [Get the subnet ID for an instance](#instance-metadata-ex-6-imdsv1 "#instance-metadata-ex-6-imdsv1")
- [Get the instance tags for an instance](#instance-metadata-ex-7-imdsv1 "#instance-metadata-ex-7-imdsv1")

### Get the available versions of the instance metadata

This example gets the available versions of the instance metadata. Each
version refers to an instance metadata build when new instance metadata
categories were released. The instance metadata build versions do not correlate
with the Amazon EC2 API versions. The earlier versions are available to you in case
you have scripts that rely on the structure and information present in a
previous version.

cURL

```
`[ec2-user ~]$` `curl http://169.254.169.254/`
`1.0
2007-01-19
2007-03-01
2007-08-29
2007-10-10
2007-12-15
2008-02-01
2008-09-01
2009-04-04
2011-01-01
2011-05-01
2012-01-12
2014-02-25
2014-11-05
2015-10-20
2016-04-19
...
latest`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/`
`1.0
2007-01-19
2007-03-01
2007-08-29
2007-10-10
2007-12-15
2008-02-01
2008-09-01
2009-04-04
2011-01-01
2011-05-01
2012-01-12
2014-02-25
2014-11-05
2015-10-20
2016-04-19
...
latest`
```

### Get the top-level metadata items

This example gets the top-level metadata items. For more information about the items in
the response, see [Instance metadata categories](ec2-instance-metadata.md#instancedata-data-categories "ec2-instance-metadata.md#instancedata-data-categories").

Note that tags are included in this output only if you've allowed access. For more
information, see [Enable access to tags in instance metadata](work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS").

cURL

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/`
`ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
instance-action
instance-id
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
tags/`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/`
`ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
iam/
instance-action
instance-id
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
tags/`
```

### Get the values for metadata items

These examples get the values of some of the top-level metadata items that were obtained
in the previous example.

cURL

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/ami-id`
`ami-0abcdef1234567890`
```

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/reservation-id`
`r-0efghijk987654321`
```

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/local-hostname`
`ip-10-251-50-12.ec2.internal`
```

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/public-hostname`
`ec2-203-0-113-25.compute-1.amazonaws.com`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/ami-id`
`ami-0abcdef1234567890`
```

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/reservation-id`
`r-0efghijk987654321`
```

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/local-hostname`
`ip-10-251-50-12.ec2.internal`
```

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public-hostname`
`ec2-203-0-113-25.compute-1.amazonaws.com`
```

### Get the list of available public keys

This example gets the list of available public keys.

cURL

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/public-keys/`
`0=my-public-key`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public-keys/` `0=my-public-key`
```

### Show the formats in which public key 0 is available

This example shows the formats in which public key 0 is available.

cURL

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/public-keys/0/`
`openssh-key`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key`
`openssh-key`
```

### Get public key 0 (in the OpenSSH key format)

This example gets public key 0 (in the OpenSSH key format).

cURL

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key`
`ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key`
`ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key`
```

### Get the subnet ID for an instance

This example gets the subnet ID for an instance.

cURL

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/02:29:96:8f:6a:2d/subnet-id`
`subnet-be9b61d7`
```

PowerShell

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/network/interfaces/macs/02:29:96:8f:6a:2d/subnet-id`
`subnet-be9b61d7`
```

### Get the instance tags for an instance

If access to instance tags in the instance metadata is turned on, you can get the
tags for a instance from instance metadata. For more information, see
[Retrieve tags from instance metadata](work-with-tags-in-IMDS.md#retrieve-tags-from-IMDS "work-with-tags-in-IMDS.md#retrieve-tags-from-IMDS").
