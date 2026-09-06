

# Getting architecture recommendations in ARC
<a name="recovery-readiness.evaluate-arch"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

If you have an existing application, Amazon Application Recovery Controller (ARC) can evaluate the architecture of your application and routing policies to provide recommendations for modifying the design to improve your application's recovery resiliency. After you create a recovery group in ARC that represents your application, follow the steps in this section to get recommendations for your application's architecture.

We recommend that you specify a target resource for the DNS target resource for your recovery group, if you haven't specified one yet, so that we can provide more detailed recommendations. When you provide additional information, ARC can provide better recommendations for you. For example, if you enter an Amazon Route 53 resource record or a Network Load Balancer as a target resource, ARC can provide information about whether you've created the optimal number of cells for your recovery group.

Note the following for DNS target resources:
+ Specify only a Route 53 resource record or Network Load Balancer for a target resource.
+ Create only one DNS target resource for each recovery group.
+ Recommended: Create one DNS target resource for each cell.
+ Group the DNS target resources into one resource set with a readiness check.

The following procedure explains how to create DNS target resources and get architecture recommendations for your application.

# To get recommendations for updating your architecture


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Readiness check**.

1. Under **Recovery group name**, choose the recovery group that represents your application.

1. On the **Recovery group details** page, on the **Action** menu, choose **Get architecture recommendations for this recovery group**.

1. If you haven't created a DNS target resource readiness check yet, create one so that ARC can provide architecture recommendations. Choose **Create a DNS target resource**.

   For more information about DNS target resources, see [Readiness check components](introduction-components-readiness.md).

1. To create a resource set for a DNS target resource, you create a readiness check. Enter a name for the readiness check, and then, for the type of readiness check, choose **DNS target resource**.

1. Enter a name for the resource set.

1. Enter the attributes for your application, including the DNS name, hosted zone ARN, and record set ID.
**Tip**  
To see the format for a hosted zone ARN, see **ARN format for hosted zone** in [Resource types and ARN formats in ARC](recovery-readiness.resource-types-arns.md).

   Optionally, but strongly recommended, choose **Add optional attribute** and provide a Network Load Balancer ARN or your domain's Route 53 resource record.

1. (Optional) In **Recovery group configuration**, choose a cell for your DNS target resource, to set the readiness scope.

1. Choose **Create resource set**.

1. On the **Recovery group** details page, choose **Get architecture recommendations**. ARC displays a set of recommendations on the page.

Review the list of recommendations. Then you can decide whether and how to make changes to improve your app's recovery resilience.