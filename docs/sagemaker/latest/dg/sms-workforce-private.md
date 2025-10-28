# Private workforce

A **private workforce** is a group of
workers that *you* choose. These can be employees
of your company or a group of subject matter experts from your
industry. For example, if the task is to label medical images, you
could create a private workforce of people knowledgeable about the
images in question.

Each AWS account has access to a single private workforce per region, and the owner has the
ability to create multiple **private** **work teams** within that workforce. A single private work team is
used to complete a labeling job or human review task, or a _job_. You can assign each work team to a separate job or use a single team
for multiple jobs. A single worker can be in more than one work team.

Your private workforce can either be created and managed using [Amazon Cognito](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md") or your own private OpenID Connect (OIDC) Identity Provider (IdP).

If you are a new user of [Amazon SageMaker Ground Truth](sms.md "sms.md") or [Amazon Augmented AI](a2i-use-augmented-ai-a2i-human-review-loops.md "a2i-use-augmented-ai-a2i-human-review-loops.md") and do
not require your workers to be managed with your own IdP, it is recommended that you use
Amazon Cognito to create and manage your private workforce.

After you create a workforce, in addition to creating and managing work teams, you can do
the following:

- [Track worker performance](workteam-private-tracking.md "workteam-private-tracking.md")
- [Create and
  manage Amazon SNS topics](sms-workforce-management-private-sns.md "sms-workforce-management-private-sns.md") to notify workers when labeling tasks are
  available
- [Manage
  Private Workforce Access to Tasks Using IP Addresses](sms-workforce-management-private-api.md "sms-workforce-management-private-api.md")

###### Note

Your private workforce is shared between Ground Truth and Amazon A2I. To create and manage
private work teams used by Augmented AI, use the Ground Truth section of the SageMaker AI console.

###### Topics

- [Amazon Cognito Workforces](sms-workforce-private-use-cognito.md "sms-workforce-private-use-cognito.md")
- [OIDC IdP Workforces](sms-workforce-private-use-oidc.md "sms-workforce-private-use-oidc.md")
- [Private workforce management using the
  Amazon SageMaker API](sms-workforce-management-private-api.md "sms-workforce-management-private-api.md")
- [Track Worker Performance Metrics](workteam-private-tracking.md "workteam-private-tracking.md")
- [Create the Amazon SNS topic](sms-workforce-management-private-sns.md "sms-workforce-management-private-sns.md")
