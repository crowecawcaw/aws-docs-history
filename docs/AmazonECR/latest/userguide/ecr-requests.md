# Making requests to Amazon ECR registries

You can push, pull, delete, view, and manage OCI images, Docker images, and OCI-compatible
artifacts in Amazon ECR private registries using either IPv4-only endpoints or dual-stack (IPv4
and IPv6) endpoints. For making requests from IPv4 networks, you can use either dual-stack
or IPv4 endpoints. For making requests from an IPv6 network, use a dual-stack endpoint. For
more information about making requests to Amazon ECR Public registries using IPv4 and dual-stack
endpoints, see [Making requests to Amazon ECR Public
registries](../public/public-ecr-requests.md "../public/public-ecr-requests.md"). There are no additional charges for accessing Amazon ECR over IPv6. For
more information about pricing, see [Amazon Elastic Container Registry
pricing](https://aws.amazon.com/ecr/pricing/ "https://aws.amazon.com/ecr/pricing/").

Amazon ECR endpoints are designated by attributes beyond IPv4-only endpoint or dual-stack
endpoints support. These attributes can include:

- **Region** – Each endpoint is specific to a Region.
- **Type** – Endpoint selection depends on whether you're
  using the AWS SDK or OCI-compatible and Docker command line interfaces.
- **Security** – In select Regions Amazon ECR offers
  FIPS-compliant endpoints. For more information about a list of FIPS-compliant Amazon ECR
  endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  For more information about service endpoints supported by IPv4, dual-stack, Docker, and
  OCI client, which handles Amazon ECR API calls from AWS CLI and AWS SDKs see, [Service
  endpoints](../../../general/latest/gr/ecr.md#ecr_region "../../../general/latest/gr/ecr.md#ecr_region").

## Getting started with making requests over IPv6

To make a request to an Amazon ECR registry over IPv6, you need to use a dual-stack
endpoint. Before accessing an Amazon ECR registry over IPv6, verify the following
requirements:

- Your client and network must support IPv6.
- Amazon ECR supports the following request types over IPv6:
  - OCI and Docker client requests:

  ``<registry-id>`.dkr-ecr.`<aws-region>`.on.aws`
  - AWS API requests:

  `ecr.`<aws-region>`.api.aws`

- You must update any AWS Identity and Access Management (IAM) or registry policies that use source IP
  address filtering to include IPv6 address ranges. For more information, see
  [Using IPv6 addresses in IAM policies](#ecr-request-ipv6-access-iam "#ecr-request-ipv6-access-iam").
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

```
curl --verbose https://ecr.us-west-2.api.aws
```

You get back information similar to the following example. If you are connected over
IPv6 the connected IP address will be an IPv6 address.

```
* About to connect() to ecr.us-west-2.api.aws port 443 (#0)
* Trying IPv6 address... connected
* Connected to ecr.us-west-2.api.aws (IPv6 address) port 443 (#0)
> Host: ecr.us-west-2.api.aws
* Request completely sent off
```

If you are using Microsoft Windows 7 or Windows 10, you can test whether you can
access a dual-stack endpoint over IPv4 or IPv6 by using the `ping` command as
shown in the following example.

```
ping ecr.us-west-2.api.aws
```

## Making requests over IPv6 by using dual-stack

endpoints

You can make Amazon ECR API calls over IPv6 using dual-stack endpoints. The
functionality and performance of Amazon ECR API operations remain consistent whether you
use IPv4 or IPv6.

When you use the AWS Command Line Interface (AWS CLI) and AWS SDKs, you can enable IPv6 either by
using a parameter or flag to switch to a dual-stack endpoint, or by directly specifying
the dual-stack endpoint in your config file to override the default Amazon ECR endpoint. You
can also make configuration changes by using a command, which sets
`use_dualstack_endpoint` to true in the default profile. For more
information about `use_dualstack_endpoint`, see [Dual-stack and FIPS
endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md").

###### Example Making configuration changes by using a command

`aws configure set default.ecr.use_dualstack_endpoint true`

###### Example Making requests over IPv6 using

AWS CLI

`aws ecr describe-repositories --region us-west-2 --endpoint-url
 https://ecr.us-west-2.api.aws`

## Using Amazon ECR endpoints from the docker

CLI

After you sign in to your Amazon ECR repository and tag your image, you can push and pull
OCI images and Docker images to and from Amazon ECR registries. The following examples
demonstrate docker push and docker pull commands with both dual-stack endpoints.

###### Example Pushing docker images using IPv4

endpoint

`docker push
 `<registry-id>`.dkr.ecr.us-west-1.amazonaws.com/my-repository:tag`

###### Example Pushing docker images using dual-stack

endpoint

`docker push
 `<registry-id>`.dkr-ecr.us-west-1.on.aws/my-repository:tag`

###### Example Pulling docker images using IPv4 endpoint

`docker pull
 `<registry-id>`.dkr.ecr.us-west-1.amazonaws.com/my-repository:tag`

###### Example Pulling docker images using dual-stack endpoint

`docker pull
 `<registry-id>`.dkr-ecr.us-west-1.on.aws/my-repository:tag`

## Using IPv6 addresses in IAM policies

Before you access a registry using IPv6, ensure that your IAM user and Amazon ECR
registry policies that use IP address filtering include IPv6 address ranges. If IP
address filtering policies aren't updated to handle IPv6 addresses, clients might
incorrectly lose or gain access to the registry when they start using IPv6. For more
information about managing access permissions with IAM, see [Identity and Access Management for Amazon Elastic Container Registry](security-iam.md "security-iam.md").

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
 "Action": "ecr:*",
 "Resource": "arn:aws:ecr:*:*:repository/`exampleregistry`/*",
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
