# Setup IAM roles and permissions

AWS Resilience Hub allows you to configure the IAM roles you would like to use while
running assessments for your application. There are multiple ways to configure
AWS Resilience Hub to gain read-only access to your application resources. However, AWS Resilience Hub
recommends the following ways:

- **Role based access** – This role is
  defined and used in the current account. AWS Resilience Hub will assume this role to
  access the resources of your application.

To provide role-based access, the role must include the following:

    + Read-only permission to read your resources (AWS Resilience Hub recommends you
     to use the `AWSResilienceHubAsssessmentExecutionPolicy`
     managed policy).
    + Trust policy to assume this role, which allows AWS Resilience Hub Service
     Principal to assume this role. If you don’t have such a role
     configured in your account, AWS Resilience Hub will display the instructions
     to create that role. For more information, see [Setup permissions](setup-permissions.md "setup-permissions.md").

###### Note

If you provide only the invoker role name and if your resources are
located in another account, AWS Resilience Hub will use this role name in the
other accounts to access the cross-account resources. Optionally, you
can configure the role ARNs for other accounts, which will be used
instead of the invoker role name.

- **Current IAM user access** –
  AWS Resilience Hub will use the current IAM user to access your application
  resources. When your resources are in a different account, AWS Resilience Hub will
  assume the following IAM roles to access the resources:

      + `AwsResilienceHubAdminAccountRole` in the current
       account
      + `AwsResilienceHubExecutorAccountRole` in other
       accounts

  In addition, when you configure a scheduled assessment, AWS Resilience Hub will assume
  the `AwsResilienceHubPeriodicAssessmentRole` role. However, using
  `AwsResilienceHubPeriodicAssessmentRole` is not advised because
  you must manually configure roles and permissions, and some functionalities
  (such as **Drift notification**) might not work as
  expected.
