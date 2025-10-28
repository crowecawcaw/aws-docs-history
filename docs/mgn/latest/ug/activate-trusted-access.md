NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Activate trusted access for AWS Application Migration Service

To use global view, you must activate trusted access to AWS Application Migration Service (AWS MGN) for your organization.

Attach the [AWSOrganizationsFullAccess](../../../aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.md") managed policy to the user.

To enable service access for your organization, take the following steps:

1.  Activate trusted access for AWS MGN

        1. Log in as management account.
        2. Select **Global view** from the left-hand navigation
         menu.
        3. Activate service access by clicking the 'Enable AWS Organizations service access' button

    [Learn more about activating trusted access.](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md")

2.  Select members and turn them into delegated admins for AWS MGN by calling the [RegisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md") API, including the service name:

```

            {
              "AccountId": "string",
              "ServicePrincipal": "mgn.amazonaws.com"
            }

```

###### Important

You can register up to 5 delegated administrators.
