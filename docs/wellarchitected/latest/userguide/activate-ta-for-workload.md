

# Activating AWS Trusted Advisor for a workload
<a name="activate-ta-for-workload"></a>

You can optionally integrate AWS Trusted Advisor and activate it on a per-workload basis for AWS Business and Enterprise Support customers. There is no cost to integrate Trusted Advisor with AWS WA Tool, but for Trusted Advisor pricing details, see [AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html). Activating Trusted Advisor for workloads can provide you a more comprehensive, automated, and monitored approach to reviewing and optimizing your AWS workloads. This can help you improve the reliability, security, performance, and cost optimization for your workloads.

**To activate Trusted Advisor for a workload**

1. To activate Trusted Advisor, workload owners can use AWS WA Tool to update an existing workload, or create a new workload by choosing **Define workload**. 

1. Enter an account ID used by Trusted Advisor in the **Account IDs** field, select an application ARN in the **Application** field, or both to activate Trusted Advisor. 

1. In the **AWS Trusted Advisor** section, select **Activate Trusted Advisor**.  
![Screenshot of the Activate Trusted Advisor section when defining a workload.](http://docs.aws.amazon.com/wellarchitected/latest/userguide/images/defining-workload-activate-ta-support.png)

1. A notification that the **IAM service role will be created** displays the first time Trusted Advisor is activated for a workload. Choosing **View permissions** displays the IAM role permissions. You can view the **Role name**, as well as the **Permissions** and **Trust relationships** JSON automatically created for you in IAM. After the role is created, for subsequent workloads activating** Trusted Advisor**, only the notification for **Additional setup needed** is shown. 

1. In the **Resource definition** dropdown, you can select **Workload Metadata**, **AppRegistry**, or **All**. The **Resource definition** selection defines what data AWS WA Tool fetches from Trusted Advisor to provide the status checks in the workload review that map to Well-Architected best practices.

   **Workload Metadata** – the workload is defined by account IDs and AWS Regions specified in the workload.

   **AppRegistry** – the workload is defined by resources (such as CloudFormation stacks) that are present in the AppRegistry application associated with the workload.

   **All** – the workload is defined by both the workload metadata and AppRegistry resources.

1. Choose **Next**. 

1. Apply the **AWS Well-Architected Framework** to your workload, and choose **Define workload**. Trusted Advisor checks are only linked to the AWS Well-Architected Framework, and not other lenses.

The AWS WA Tool periodically gets data from Trusted Advisor using the roles created in IAM. The IAM role is automatically created for the workload owner. However, to view Trusted Advisor information, the owners of any associated accounts on the workload must go to IAM and create a role, see [Activating Trusted Advisor for a workload in IAM](activate-ta-in-iam.md) for more details. If this role does not exist, AWS WA Tool cannot obtain Trusted Advisor information for that account and displays an error. 

For more information about creating a role in AWS Identity and Access Management (IAM), see [Creating a role for an AWS service (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console) in the *IAM User Guide*.