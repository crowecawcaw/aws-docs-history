# Best practices for routing control in ARC

We recommend the following best practices for recovery and failover preparedness for
routing control in ARC.

**Topics**

- [Keep purpose-built, long-lived AWS credentials secure and always accessible](#RCBestPracticeCredentials "#RCBestPracticeCredentials")
- [Choose lower TTL values for DNS records involved in failover](#RCBestPracticeLowerTTL "#RCBestPracticeLowerTTL")
- [Limit the time that clients stay connected to your endpoints](#RCBestPracticeCurrentConnections "#RCBestPracticeCurrentConnections")
- [Bookmark or hard code your five Regional cluster endpoints and routing control ARNs](#RCBestPracticeBookmarkEndpoints "#RCBestPracticeBookmarkEndpoints")
- [Choose one of your endpoints at random to update your routing control states](#RCBestPracticeRandomEndpoint "#RCBestPracticeRandomEndpoint")
- [Use the extremely reliable data plane API to list and update routing control states, not the console](#RCBestPracticeUseDataPlane "#RCBestPracticeUseDataPlane")

**Keep purpose-built, long-lived AWS credentials secure and always accessible**
In a disaster recovery (DR) scenario, keep system dependencies to a minimum by using a simple approach to
accessing AWS and performing recovery tasks. Create [IAM long-lived credentials](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md") specifically for DR tasks, and keep the credentials securely in an on-premises physical
safe or a virtual vault, to access when needed. With IAM, you can centrally manage security credentials, such as access keys,
and permissions for access to AWS resources. For non-DR tasks, we recommend that you continue to use federated access, using AWS
services such as [AWS Single Sign-On](https://aws.amazon.com/single-sign-on/ "https://aws.amazon.com/single-sign-on/").

To perform failover tasks in ARC with the recovery cluster data plane API, you can attach a
ARC IAM policy to your user. To learn more, see [Identity-based policy
examples in Amazon Application Recovery Controller (ARC)](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

**Choose lower TTL values for DNS records involved in failover**
For DNS records that you might need to change as part of your failover mechanism, especially records that
are health checked, using lower TTL values is appropriate. Setting a TTL of 60 or 120 seconds is a common choice for this scenario.

The DNS TTL (time to live) setting tells DNS resolvers how long to cache a record before requesting a new one.
When you choose a TTL, you make a trade-off between latency and reliability,
and responsiveness to change. With a shorter TTL on a record, DNS resolvers notice updates to the record more quickly because
the TTL specifies that they must query more frequently.

For more information, see _Choosing TTL values for DNS records_ in
[Best practices for Amazon Route 53 DNS](../../../Route53/latest/DeveloperGuide/best-practices-dns.md "../../../Route53/latest/DeveloperGuide/best-practices-dns.md").

**Limit the time that clients stay connected to your endpoints**
When you use routing controls to shift from one AWS Region to
another, the mechanism that Amazon Application Recovery Controller (ARC) uses to move your application traffic is a DNS update. This update causes all
new connections to be directed away from the impaired location.

However, clients with pre-existing open connections might continue to make requests against the impaired location until
the clients reconnect. To ensure a quick recovery, we recommend that you limit the amount of time clients
stay connected to your endpoints.

If you use an Application Load Balancer, you can use the `keepalive` option to configure how long connections
continue. For more information, see [HTTP client keepalive duration](../../../elasticloadbalancing/latest/application/application-load-balancers.md#http-client-keep-alive-duration "../../../elasticloadbalancing/latest/application/application-load-balancers.md#http-client-keep-alive-duration") in the Application Load Balancer User Guide.

By default, Application Load Balancers set the HTTP client keepalive duration value to 3600 seconds, or 1 hour. We suggest that
you lower the value to be inline with your recovery time goal for your application,
for example, 300 seconds. When you choose an HTTP client keepalive duration time, consider that this value is a trade off
between reconnecting more frequently in general, which can affect latency, and more quickly moving all clients away
from an impaired AZ or Region.

**Bookmark or hard code your five Regional cluster endpoints and routing control ARNs**
We recommend that you keep a local copy of your ARC Regional cluster endpoints,
in bookmarks or saved in automation code that you use to retry your endpoints.
During a failure event, you might not be able to access some API operations, including ARC API operations that
are not hosted on the extremely reliable data plane cluster. You can list the endpoints for your ARC clusters by using the
[DescribeCluster](../../../recovery-cluster/latest/api/cluster-clusterarn.md "../../../recovery-cluster/latest/api/cluster-clusterarn.md")
API operation.

**Choose one of your endpoints at random to update your routing control states**

Routing controls provide five Regional endpoints to ensure high availability, even when dealing with failures. To achieve their full resilience, it's important to have retry logic that can use all five endpoints as necessary.
For information about using code examples with the AWS SDK, including examples for trying cluster
endpoints, see [Code examples for Application Recovery Controller using AWS SDKs](service_code_examples.md "service_code_examples.md").

**Use the extremely reliable data plane API to list and update routing control states, not the console**
Using the ARC data plane API, view your routing controls and states with the
[ListRoutingControls](../../../routing-control/latest/APIReference/API_ListRoutingControls.md "../../../routing-control/latest/APIReference/API_ListRoutingControls.md")
operation and update routing control states to redirect traffic for failover with
the [UpdateRoutingControlState](../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md "../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md")
operation. You can use the AWS CLI [(as in these examples)](getting-started-cli-routing.md "getting-started-cli-routing.md")
or code that you write using one of the AWS SDKs. ARC offers extreme reliability with the API in the data plane to fail
over traffic. We recommend using the API instead of changing routing control states in the AWS Management Console.

Connect to one of your Regional cluster endpoints for ARC to use the data plane API. If the endpoint is
unavailable, try connecting to another cluster endpoint.

If a safety rule blocks a routing control state update, you can bypass it to make the update
and fail over traffic. For more information, see [Overriding safety rules
to reroute traffic](routing-control.md "routing-control.md").

**Test failover with ARC**
Test failover regularly with ARC routing control, to fail over from your primary application stack to a
secondary application stack. It's important to make sure that the ARC structures that you've added are aligned with
the correct resources in your stack, and that everything works as you expect it to. You should test
this after you set up ARC for your environment, and continue to test periodically, so that your failover environment
is prepared, before you experience a failure situation in which you need your secondary system to be up and running
quickly to avoid downtime for your users.
