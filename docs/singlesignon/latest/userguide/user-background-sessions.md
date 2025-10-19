# User background sessions

User background sessions allow a user to initiate a long-running job on an AWS managed application such as [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html "https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html"), without that user having to remain signed in while the job runs. The job runs immediately and uses the [trusted identity propagation](trustedidentitypropagation-overview.md "trustedidentitypropagation-overview.md") capability of IAM Identity Center to ensure that the user's permissions are maintained while the job is run in the background. The job can continue to run even if the user turns off their computer, their IAM Identity Center sign-in session expires, or the user signs out of the AWS access portal. This capability enables data scientists, machine learning engineers, and others to start analytics and machine learning workflows that run in the background without active user involvement.

User background sessions are enabled by default for supported AWS managed applications such as Amazon SageMaker Studio. To use this capability, however, you must enable trusted identity propagation in Amazon SageMaker Studio when you create or update a domain. For more information, see [Enable trusted identity propagation in your Amazon SageMaker AI domain](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-setup.html#trustedidentitypropagation-setup-enable "https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-setup.html#trustedidentitypropagation-setup-enable").

The default session duration for user background sessions is 7 days. You can specify a different duration, from a
 minimum of 15 minutes to a maximum of 90 days. Custom duration values must be entered in
 minutes and be between 15 minutes and 129,600 minutes (90 days). 

Keep in mind the following considerations for user background sessions:


* A user background session can be created only when a user manually initiates a job in Amazon SageMaker Studio. This capability is not supported for automated, scheduled workflows.
* For a list of AWS Regions that support user background sessions, see [Supported AWS Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-compatibility.html#trustedidentitypropagation-compatibility-supported-regions "https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-compatibility.html#trustedidentitypropagation-compatibility-supported-regions").
* You can view user background sessions in CloudTrail. For information, see [Identifying user background session details](sso-cloudtrail-use-cases.md#identifying-user-background-session-details "sso-cloudtrail-use-cases.md#identifying-user-background-session-details").
* You can also end active sessions for a user in your organization. For information, see [End active sessions for your workforce users](end-active-sessions.md "end-active-sessions.md").
###### To configure the duration of a user background session

1. Open the IAM Identity Center console.
2. Choose **Settings**.
3. On the **Settings** page, choose the **Authentication** tab.
4. Under **Authentication**, next to **Session duration**, choose **Configure**. The **Configure session duration** dialog box appears.
5. In the **Configure session duration** dialog box, if the **Enable user background sessions** check box is not already selected, select it. Clear the check box to disable user background sessions.


###### Note

Current sessions are not affected if you disable user background sessions.
6. Under **User background sessions**, choose the maximum session duration by selecting the drop-down arrow. Choose the length for the session, and then choose **Save**.


###### Note

Changes to session duration apply only to new sessions. Current sessions keep their original duration.
7. You are returned to the **Authentication** tab. A green notification message appears above the tab indicates that the session settings were updated successfully.
###### Note

A customer managed application can't create a user background session.
