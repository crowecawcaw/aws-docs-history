# Requesting a quota increase in DynamoDB

You can request a quota increase for each Region using the Service Quotas console,
AWS CLI or a support case. If an adjustable quota isn't available in the Service Quotas
console, use the AWS Support Center Console to create a [service quota increase case](https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase "https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase").

Support could approve, deny, or partially approve your quota increase requests. Increases
aren't granted immediately, and can take a few days to take effect.

###### To request an increase using the Service Quotas console

1. Open the Service Quotas console at
   https://console.aws.amazon.com/servicequotas/home/services/dynamodb/quotas/
2. From the navigation bar, at the top of the screen, select a Region.
3. Filter the list by resource name. For example, enter **On-Demand** to
   locate the quotas for On-Demand Instances.
4. If the quota is adjustable, choose the quota and then choose
   **Request quota increase**.
5. For **Change quota value**, enter the new quota value.
6. Choose **Request**.
7. To view any pending or recently resolved requests in the console, choose **Dashboard**
   from the navigation pane. For pending requests, choose the status of the request to open the
   request receipt. The initial status of a request is **Pending**. After the status changes to
   **Quota requested**, you'll see the case number with Support. Choose the case number to open the
   ticket for your request.
   For more information, including how to use the AWS CLI or SDKs to request a quota
   increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas
   User Guide_.
