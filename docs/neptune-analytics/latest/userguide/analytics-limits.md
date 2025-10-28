# Limits for Neptune Analytics

## Regions

Neptune Analytics is available in the following AWS Regions:

- US East (N. Virginia):   `us-east-1`
- US East (Ohio):   `us-east-2`
- US West (Oregon):   `us-west-2`
- Asia Pacific (Singapore):   `ap-southeast-1`
- Asia Pacific (Sydney):   `ap-southeast-2`
- Asia Pacific (Tokyo):   `ap-northeast-1`
- Asia Pacific (Mumbai):   `ap-south-1`
- Europe (Ireland):   `eu-west-1`
- Europe (London):   `eu-west-2`
- Europe (Frankfurt):   `eu-central-1`
- Canada (Central):   `ca-central-1`

## Quotas

Your AWS account has default quotas, formerly referred to as limits, for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request increases for some
quotas, and other quotas cannot be increased.

To view the quotas for Neptune Analytics, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS services** and
select **Neptune Analytics**.

To request a quota increase, see [Requesting a Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

## Vertex enumeration is not memory bounded

The following quotas and limits apply to Neptune Analytics:

The current implementation of vertex enumeration and counting is not memory bounded.
As a consequence, queries such as `MATCH (n) RETURN count(n)` will require a
significant amount of memory and, depending on the chosen capacity and dataset shape,
may run into out-of-memory exceptions.

Where possible, we recommend replacing such queries with queries that operate on
a per-label basis. For instance, a query such as `MATCH (n : Person) RETURN
 count(n)` will be significantly more efficient, both in terms of memory consumption
and memory utilization.

## Parameterized openCypher queries not supported for algorithms

Neptune Analytics supports [parameterized
openCypher queries](../../../neptune/latest/userguide/opencypher-parameterized-queries.md "../../../neptune/latest/userguide/opencypher-parameterized-queries.md") with the limitation that parameters are not allowed inside
algorithms.

For instance, a query such as `CALL neptune.algo.degree($id)` where `$id`
is passed in as a parameter is currently not supported.

## Size limits on properties, labels and strings

The maximum length of the strings supported is 1,048,062 bytes. The limit would be lower for strings with unicode
characters since some unicode characters are represented using multiple bytes.

## Labelless vertices with only embeddings are not supported

Neptune Analytics supports labelless vertices, which are vertices without vertex labels. The labelless vertices may or may not
have vertex properties. However, there is a limitation that labelless vertices with only vector embeddings are not
supported. They must either have a vertex label or a vertex property.
