# IAM role for an Amazon Q Business web experience

###### Note

If you are using permissions for Amazon Q Apps created prior to July 10, 2024,
you must update your role with the new [Amazon Q Apps](deploy-q-apps-iam-permissions.md "deploy-q-apps-iam-permissions.md") permissions for your users
to have access to use the [permissions
to view and specify approved data sources](deploy-q-apps-iam-permissions.md#deploy-data-source-iam-permissions "deploy-q-apps-iam-permissions.md#deploy-data-source-iam-permissions") and other future features in Q Apps.

To allow Amazon Q to invoke the API operations required to integrate your application environment,
deploy your chat web experience, use an external IdP, and use Amazon Q Apps you must use the
following IAM policies.

###### Topics

- [IAM role for an Amazon Q Business web experience using IAM Identity Center](web-experience-iam-role-idc.md "web-experience-iam-role-idc.md")
- [IAM role for an Amazon Q Business web experience using IAM Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md")
- [IAM permissions for using Amazon Q Apps](deploy-q-apps-iam-permissions.md "deploy-q-apps-iam-permissions.md")
