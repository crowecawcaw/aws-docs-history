# Offboard a workload from Incident Detection and Response

To offboard a workload from AWS Incident Detection and Response, create a new support case for each workload. When you create the support case, keep the following in mind:

- To offboard a workload that's in a single AWS account, create the support case either from the workload's account or from your payer account.
- To offboard a workload that spans multiple AWS accounts, then create the support case from your **payer account**. In the body of the support case, list all account IDs to offboard.

###### Important

If you create a support case to offboard a workload from the incorrect account, you might experience delays and requests for additional information before your workloads can be offloaded.

###### Request to offboard a workload

1. Go to the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"), and then select **Create case**.
2. Choose **Technical**.
3. For **Service**, choose **Incident Detection and Response**.
4. For **Category**, choose **Workload Offboarding**.
5. For **Severity**, choose **General Guidance**.
6. Enter a **Subject** for this change. For example:

[Offboard] AWS Incident Detection and Response - `workload_name` 7. Enter a **Description** for this change. For example, enter "This request is for offboarding an existing workload onboarded into AWS Incident Detection and Response". Make sure that you include the following information in your request:

    * **Workload name:** Your workload name.
    * **Account ID(s):** ID1, ID2, ID3, and so on.
    * **Reason for offboarding:** Provide a reason for offboarding the workload.

8. In the **Additional contacts - optional** section, enter any email IDs that you want to receive correspondence about this offboarding request.
9. Choose **Submit**.
