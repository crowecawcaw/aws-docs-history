# View SageMaker training plans quotas using the AWS management

console

###### Important

- For pricing information about SageMaker training plans, see the [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") page. Navigate to the
  **Amazon SageMaker HyperPod flexible training plans** section under
  **On-Demand Pricing**. Choose your desired Region to view available
  instance types and their corresponding prices.
- Make sure that your Training Jobs or HyperPod service quotas allow a maximum
  number of instances per instance type that exceeds the number of instances specified in
  your plan.
  You can view the current quotas and limits for SageMaker training plans using the AWS Management
  Console.

To search for a specific quota value:

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas "https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas").
2. In the left navigation pane, choose **AWS services**.
3. From the AWS services list, search for and select
   **Amazon SageMaker AI**.
4. In the **Service quotas** list, you can see the service quota name,
   applied value (if it's available), AWS default quota, and whether the quota value is
   adjustable.
   To find specific quotas, you can use the search bar at the top of the **Service
   quotas** list. Type the `Limit Name` of the quota you are searching for.
   For example, to find the quota for the number of training plans per region, you would type
   `training-plan-total_count` in the search bar.

The following table outlines the quota limit names for SageMaker training plans.

| SageMaker training plans quota limits | Limit Name                                                                                    | Display Name |
| ------------------------------------- | --------------------------------------------------------------------------------------------- | ------------ |
| training-plan-total_count             | Number of training plans per Region                                                           |
| reserved-capacity-ml-p4d-24xlarge     | Number of ml.p4d.24xlarge instances in reserved capacity across training plans per<br>Region  |
| reserved-capacity-ml-p5-48xlarge      | Number of ml.p5.48xlarge instances in reserved capacity across training plans per<br>Region   |
| reserved-capacity-ml-p5e-48xlarge     | Number of ml.p5e.48xlarge instances in reserved capacity across training plans per<br>Region  |
| reserved-capacity-ml-p5en-48xlarge    | Number of ml.p5en.48xlarge instances in reserved capacity across training plans per<br>Region |
| reserved-capacity-ml-trn1-32xlarge    | Number of ml-trn1-32xlarge instances in reserved capacity across training plans per<br>Region |
| reserved-capacity-ml-trn2-48xlarge    | Number of ml.trn2.48xlarge instances in reserved capacity across training plans per<br>Region |

If you need higher limits for your SageMaker training plans, you may be able to request a quota
increase. The ability to increase a quota depends on whether it's adjustable, which you can see
in the **Service quotas** console.

To request a quota increase:

1. Navigate to the specific quota in the **Service quotas**
   console.
2. If the quota is adjustable, you can request a quota increase at either the account level
   or resource level based on the value listed in the **Adjustability**
   column.
3. For **Increase quota value**, enter the new value. The new value must
   be greater than the current value.
4. Choose **Request**.
5. Quota increase requests are subject to review and approval by AWS. To view any pending
   or recently resolved requests in the console, navigate to the **Request
   history** tab from the service's details page, or choose
   **Dashboard** from the navigation pane. For pending requests, choose the
   status of the request to open the request receipt. The initial status of a request is
   `Pending`. After the status changes to `Quota requested`, you see
   the case number with AWS Support. Choose the case number to open the ticket for your
   request.
   To learn more about requesting a quota increase in general, see [Requesting a quota
   increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _AWS Service Quotas User
   Guide_.
