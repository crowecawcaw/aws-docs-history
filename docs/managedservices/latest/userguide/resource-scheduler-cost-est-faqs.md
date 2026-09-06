

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Cost estimator tips
<a name="resource-scheduler-cost-est-faqs"></a>

Cost Savings Estimator does not accept discounts such as reserved instances, savings plans, and so forth, into consideration in its calculation. The Estimator takes usage costs from Cost Explorer and calculates the average cost per hour for the resources. For more details, see [ Understanding your AWS Cost Datasets: A Cheat Sheet](https://aws.amazon.com/blogs/aws-cost-management/understanding-your-aws-cost-datasets-a-cheat-sheet/)

In order for the cost savings estimator to retrieve cost and usage only for resources managed by Resource Scheduler from Cost Explorer, the tag key that Resource Scheduler uses to target resources needs to be activated as the **Cost Allocation** tag in the Billing Dashboard. If the account belongs to an organization, the tag key needs to be activated in the management account of the organization. For information on doing this, see [User-Defined Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html). If the cost allocation tag is not activated, the estimator is not able to calculate the savings and publish the metric, even if it is enabled.