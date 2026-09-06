

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Create an IAM role with access to the AWS website
<a name="create-iam-role"></a>

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources for your users. You use IAM to control who can use your AWS resources (authentication) and what resources they can use and in what ways (authorization).

1. Go to the [IAM Management Console](https://console.aws.amazon.com/iam/home?#home), click **Roles** in the left nav pane.

   The Roles management page opens with information about IAM roles, a **Create role** option, and a list of existing roles. ![IAM Roles console page showing role creation options and a searchable list of roles.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/iamConsoleRoles.PNG) 

1. Click **Create role**.

   The Create role **Select type of trusted entity** page opens. Click **Another AWS account** and a settings area opens up below.

   Enter the AMS trusted **Account ID** provided to you by AMS. Leave the **Require external ID** and **Require MFA** options de-selected. ![Create role wizard showing Another AWS account option selected with account ID field.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/iamConsoleCreateRole.PNG)

1. Click **Next: Permissions**.

   The Create role **Attach permissions policies** page opens with options for creating a new policy, refreshing the page, and searching existing policies. A list of existing policies is provided. ![Policy list showing AdministratorAccess and AmazonAPIGateway policies with attachment counts.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/iamConsoleCreateRolePermissionsDetail.PNG)

    

1. Select the **AdministratorAccess** policy and then click **Next: Review**.

   The Create role **Review** page opens. ![Review page showing role name, description, trusted entities, and policies before creation.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/iamConsoleCreateRoleReview.PNG)

1. Name the new role **aws\_managedservices\_onboarding\_role** and type "AMS Onboarding Role" for the **Role description**. Review the settings for the new role and, if satisfied, click **Create role**. 

   The role management page opens with your new role listed.