# AOSREL03-BP01 Regularly review your OpenSearch Service

quotas

Prevent workload limitations in Amazon OpenSearch Service by regularly
reviewing and updating your domain quotas for smooth operation.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome:** Your OpenSearch Service domain quotas are regularly reviewed to prevent limitations
on your OpenSearch workloads.

**Benefits of establishing this best
practice:** Regularly reviewing OpenSearch Service quotas
helps avoid limitations on your workloads, and you can continue to
operate without restrictions.

## Implementation guidance

Familiarize yourself with the domain and instance quotas for
Amazon OpenSearch Service in your specific Region.

### Implementation steps

- Understand Amazon OpenSearch Service's quota and limit
  policies by visiting
  [Amazon OpenSearch Service quotas](../../../opensearch-service/latest/developerguide/limits.md "../../../opensearch-service/latest/developerguide/limits.md") and
  [Amazon OpenSearch Service endpoints and quotas](../../../general/latest/gr/opensearch-service.md "../../../general/latest/gr/opensearch-service.md"), which
  provide a comprehensive list of all applicable quotas and
  restrictions.

- Monitor your quotas regularly:
  - Set a schedule to review your OpenSearch Service quotas
    regularly (like monthly or quarterly).
  - Make this a part of your operational procedures to
    maintain visibility into your resource limits and usage.

- To increase a soft limit, you can open a
  [support
  ticket](https://support.console.aws.amazon.com/support/home/ "https://support.console.aws.amazon.com/support/home/") and use
  [Service Quotas](https://console.aws.amazon.com/servicequotas/home/ "https://console.aws.amazon.com/servicequotas/home/").
- Log in to AWS Management Console.
- To use Service Quotas:
  - Choose **AWS Services** in the Service Quotas left
    navigation.
  - Locate OpenSearch Service Quotas.
  - Search for Amazon OpenSearch Service.
  - Select the desired quota you want to increase, and
    choose **Request increase at account level**.
