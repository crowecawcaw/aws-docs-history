# Making requests to Amazon ECR Public registries

You can push, pull, delete, view, and manage OCI images, Docker images, and OCI-compatible
artifacts in Amazon ECR Public registries using either IPv4-only endpoints or dual-stack (IPv4 and
IPv6) endpoints. For making requests from IPv4 networks, you can use either dual-stack or
IPv4 endpoints. For making requests from an IPv6 network, use a dual-stack endpoint. For
more information about making requests to Amazon ECR private registries using IPv4 and dual-stack
endpoints, see [Making requests to Amazon ECR
registries](../userguide/ecr-requests.md "../userguide/ecr-requests.md"). There are no additional charges for accessing Amazon ECR Public over IPv6.
For more information about pricing, see [Amazon Elastic Container Registry
pricing](https://aws.amazon.com/ecr/pricing/ "https://aws.amazon.com/ecr/pricing/").

Amazon ECR Public endpoints are designated by attributes beyond IPv4-only endpoint or dual-stack
endpoints support. These attributes can include:

- **Region** – Each endpoint is specific to a Region.
- **Type** – Endpoint selection depends on whether you're
  using the AWS SDK or OCI-compatible and Docker command line interfaces.
  For more information about service endpoints supported by IPv4, dual-stack, Docker, and
  OCI client, which handles Amazon ECR Public API calls from AWS CLI and AWS SDKs see, [Service
  endpoints](../../../general/latest/gr/ecr-public.md#ecr-public-region "../../../general/latest/gr/ecr-public.md#ecr-public-region").

## Getting started with making requests over IPv6

To make a request to an Amazon ECR Public registry over IPv6, you need to use a dual-stack
endpoint. Before accessing an Amazon ECR Public registry over IPv6, verify the following
requirements:

- Your client and network must support IPv6.
- Amazon ECR Public supports the following request types over IPv6:
  - OCI and Docker client requests:

  `ecr-public.aws.com`
  - AWS API requests

  `ecr-public.us-east-1.api.aws`

- You must update any AWS Identity and Access Management (IAM) or registry policies that use source IP
  address filtering to include IPv6 address ranges. For more information, see
  [Using IPv6 addresses in IAM policies](#public-ecr-request-ipv6-access-iam "#public-ecr-request-ipv6-access-iam").
- When you use IPv6, server access logs display `Remote IP` addresses
  in IPv6 format. Update your existing tools, scripts, and software to parse these
  IPv6-formatted IP addresses.

###### Note

If you experience issues related to the presence of IPv6 addresses in log
files, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Testing IP address compatibility

If you are using use Linux/Unix or Mac OS X, you can test whether you can access a dual-stack
endpoint over IPv6 by using the `curl` command as shown in the following
example:

###### Example

```
curl -v https://ecr-public.us-east-1.api.aws
```

You get back information similar to the following example. If you are connected over
IPv6 the connected IP address will be an IPv6 address.

```
* About to connect() to ecr-public.us-east-1.api.aws port 80 (#0)
* Trying `IPv6 address`... connected
* Connected to ecr-public.us-east-1.api.aws (`IPv6 address`) port 80 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.18.1 (x86_64-unknown-linux-gnu) libcurl/7.18.1 OpenSSL/1.0.1t zlib/1.2.3
> Host:ecr-public.us-east-1.api.aws
```

If you are using Microsoft Windows 7 or Windows 10, you can test whether you can access a dual-stack endpoint over IPv6 or IPv4
by using the `ping` command as shown in the following example.

```
ping ipv6.ecr-public.us-east-1.api.aws
```

## Making requests over IPv6 by using dual-stack

endpoints

You can make Amazon ECR Public API calls over IPv6 using dual-stack endpoints. The
functionality and performance of Amazon ECR Public API operations remain consistent whether you
use IPv4 or IPv6.

When you use the AWS Command Line Interface (AWS CLI) and AWS SDKs, you can enable IPv6 either by
using a parameter or flag to switch to a dual-stack endpoint, or by directly specifying
the dual-stack endpoint in your config file to override the default Amazon ECR endpoint. The
following example shows how to make requests over IPv6 by using the AWS CLI.

###### Example Making requests over IPv6 using the AWS CLI

`aws ecr-public describe-repositories --region
 `us-east-1`--endpoint-url
`https://ecr-public.us-east-1.api.aws``

## Using Amazon ECR Public endpoints from the docker

CLI

After you sign in to your Amazon ECR Public repository and tag your image, you can push and pull OCI
containers and Docker images to and from Amazon ECR Public registries. The following examples
demonstrate docker push and docker pull commands with both dual-stack endpoints.

###### Example Pushing docker images using IPv4

endpoint

`docker push
 public.ecr.aws/<public-registry-alias>/my-repository:tag`

###### Example Pushing docker images using dual-stack

endpoint

`docker push
 ecr-public.aws.com/<public-registry-alias>/my-repository:tag`

###### Example Pulling docker images using IPv4 endpoint

`docker pull
 public.ecr.aws/<public-registry-alias>/my-repository:tag`

###### Example Pulling docker images using dual-stack endpoint

`docker pull
 ecr-public.aws.com/<public-registry-alias>/my-repository:tag`

## Using IPv6 addresses in IAM policies

Before you access a registry using IPv6, ensure that your IAM user and Amazon ECR
registry policies that use IP address filtering include IPv6 address ranges. If IP
address filtering policies aren't updated to handle IPv6 addresses, clients might
incorrectly lose or gain access to the registry when they start using IPv6. For more
information about managing access permissions with IAM, see [Identity and Access Management for Amazon ECR Public](security-iam.md "security-iam.md").

IAM policies that filter IP addresses use [IP
Address Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress"). The following registry policy example shows
how to identify the `54.240.143.*` range of allowed IPv4 addresses by
using IP address condition operators. Any IP addresses outside of this range are
denied access to the registry (`exampleregistry`). Because all IPv6
addresses are outside of the allowed range, this policy prevents IPv6 addresses from
accessing `exampleregistry`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IPAllow",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "ecr-public:*",
 "Resource": "arn:aws:ecr-public:::`exampleregistry`/*",
 "Condition": {
 "IpAddress": {"aws:SourceIp": "54.240.143.0/24"}
 }
 }
 ]
}`

```

To allow both IPv4 (`54.240.143.0/24`) and IPv6
(`2001:DB8:1234:5678::/64`) address ranges, modify the registry
policy's Condition element as shown in the following example. You can use this
`Condition` block format to update both your IAM user and registry
policies.

```
       "Condition": {
         "IpAddress": {
            "aws:SourceIp": [
              "54.240.143.0/24",
               "2001:DB8:1234:5678::/64"
             ]
          }
        }
```

###### Important

Before using IPv6 you must update all relevant IAM user and registry policies
that use IP address filtering. We don't recommend using IP address filtering in
registry policies.

You can review your IAM user policies using the IAM console at
[https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
