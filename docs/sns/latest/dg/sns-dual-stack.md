# Connect to Amazon SNS using Dual-stack (IPv4 and IPv6) endpoints

Dual-stack endpoints support both IPv4 and IPv6 traffic.
When you make a request to a dual-stack endpoint, the endpoint URL resolves to an IPv4 or an IPv6 address.
For more information on dual-stack and FIPS endpoints, see the
[SDK Reference guide](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md").

Amazon SNS supports Regional dual-stack endpoints,
which means that you must specify the AWS Region as part of the endpoint name.
Dual-stack endpoint names use the following naming convention:
`sns.`Region`.amazonaws.com`. For example, the dual-stack endpoint name for the
`eu-west-1` Region is `sns.`eu-west-1`.amazonaws.com`.

For the full list of Amazon SNS endpoints, see the
[AWS General Reference](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md").
