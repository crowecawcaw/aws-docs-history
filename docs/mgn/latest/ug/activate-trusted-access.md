

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Activate trusted access for AWS Transform MGN
<a name="activate-trusted-access"></a>

To use global view, you must activate trusted access to AWS Transform MGN for your organization.

Attach the [AWSOrganizationsFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.html) managed policy to the user.

To enable service access for your organization, take the following steps:

1. Activate trusted access for MGN

   1. Log in as management account.

   1. Select **Global view** from the left-hand navigation menu.

   1. Activate service access by choosing the 'Enable AWS Organizations service access' button

   [Learn more about activating trusted access.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html)

1. Select members and turn them into delegated admins for MGN by calling the [RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html) API, including the service name:

   ```
               {
                 "AccountId": "string",
                 "ServicePrincipal": "mgn.amazonaws.com"
               }
   ```
**Important**  
You can register up to 5 delegated administrators.