# Getting architecture recommendations in ARC

If you have an existing application, Amazon Application Recovery Controller (ARC) can evaluate the architecture of
your application and routing policies to provide recommendations
for modifying the design to improve your application's recovery resiliency. After you create
a recovery group in ARC that represents your application, follow the steps
in this section to get recommendations for your application's architecture.

We recommend that you specify a target resource for the DNS target resource for your recovery group, if you haven't specified one yet, so that we can
provide more detailed recommendations. When you provide additional information, ARC can provide better recommendations for you. For example, if you
enter an Amazon Route 53 resource record or a Network Load Balancer as a target resource, ARC can provide information about whether you've created the optimal number of
cells for your recovery group.

Note the following for DNS target resources:

- Specify only a Route 53 resource record or Network Load Balancer for a target resource.
- Create only one DNS target resource for each recovery group.
- Recommended: Create one DNS target resource for each cell.
- Group the DNS target resources into one resource set with a readiness check.
  The following procedure explains how to create DNS target resources and get architecture recommendations for your application.

# To get recommendations for updating your architecture

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Readiness check**.
3. Under **Recovery group name**, choose the recovery group that represents your application.
4. On the **Recovery group details** page, on the **Action** menu, choose **Get architecture recommendations
   for this recovery group**.
5. If you haven't created a DNS target resource readiness check yet, create one so that ARC can provide architecture recommendations.
   Choose **Create a DNS target resource**.

For more information about DNS target resources, see [Readiness check components](introduction-components-readiness.md "introduction-components-readiness.md") . 6. To create a resource set for a DNS target resource, you create a readiness check. Enter a name for the readiness check, and then, for the
type of readiness check, choose **DNS target resource**. 7. Enter a name for the resource set. 8. Enter the attributes for your application, including the DNS name, hosted zone ARN, and
record set ID.

###### Tip

To see the format for a hosted zone ARN, see **ARN format for hosted zone** in
[Resource types and ARN formats
in ARC](recovery-readiness.md "recovery-readiness.md").

Optionally, but strongly recommended, choose **Add optional attribute** and
provide a Network Load Balancer ARN or your domain's Route 53 resource record. 9. (Optional) In **Recovery group configuration**, choose a cell for your DNS target resource,
to set the readiness scope. 10. Choose **Create resource set**. 11. On the **Recovery group** details page, choose **Get architecture recommendations**. ARC
displays a set of recommendations on the page.
Review the list of recommendations. Then you can decide whether and how to make changes to improve your app's recovery resilience.
