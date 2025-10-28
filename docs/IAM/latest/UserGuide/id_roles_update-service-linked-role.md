# Update a service-linked role

The method that you use to edit a service-linked role depends on the service. Some
services might allow you to edit the permissions for a service-linked role from the service
console, API, or CLI. However, after you create a service-linked role, you cannot change the
name of the role because various entities might reference the role. You can edit the
description of any role from the IAM console, API, or CLI.

For information about which services support using service-linked roles, see [AWS services that work with
IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md") and look for the services that
have **Yes** in the **Service-Linked
Role** column. To learn whether the service supports editing the service-linked
role, choose the **Yes** link to view the service-linked role
documentation for that service.

## Editing a service-linked role

description (console)

You can use the IAM console to edit the description of a service-linked role.

###### To edit the description of a service-linked role (console)

1. In the navigation pane of the IAM console, choose
   **Roles**.
2. Choose the name of the role to modify.
3. To the far right of **Role description**, choose
   **Edit**.
4. Enter a new description in the box and choose **Save**.

## Editing a service-linked role description

(AWS CLI)

You can use IAM commands from the AWS CLI to edit the description of a service-linked
role.

###### To change the description of a service-linked role (AWS CLI)

1. (Optional) To view the current description for a role, run the following
   commands:

```
`aws iam get-role --role-name `ROLE-NAME``
```

Use the role name, not the ARN, to refer to roles with the CLI commands. For
example, if a role has the following ARN:
`arn:aws:iam::123456789012:role/myrole`, you refer to the role as
`myrole`. 2. To update a service-linked role's description, run the following command:

```
`aws iam update-role --role-name `ROLE-NAME` --description `OPTIONAL-DESCRIPTION``
```

## Editing a service-linked role description

(AWS API)

You can use the AWS API to edit the description of a service-linked role.

###### To change the description of a service-linked role (AWS API)

1. (Optional) To view the current description for a role, call the following operation,
   and specify the name of the role:

AWS API: [GetRole](../APIReference/API_GetRole.md "../APIReference/API_GetRole.md") 2. To update a role's description, call the following operation, and specify the name
(and optional description) of the role:

AWS API: [UpdateRole](../APIReference/API_UpdateRole.md "../APIReference/API_UpdateRole.md")
