# Setting up permissions

You must give users, groups, or roles permission to interact with Amazon Personalize resources. And you must give Amazon Personalize permission
to access the resources you create in Amazon Personalize and to perform tasks on your behalf.

###### To set up permissions

1. Give Amazon Personalize permission to access your resources in Amazon Personalize and permission to perform tasks on your behalf. See [Giving Amazon Personalize permission to access your resources](set-up-required-permissions.md "set-up-required-permissions.md").
2. Give your users, groups, or roles permission to interact with Amazon Personalize resources and pass your service role to Amazon Personalize. See [Giving users permission to access Amazon Personalize](grant-user-permissions.md "grant-user-permissions.md").
3. Modify your Amazon Personalize service role's trust policy so it prevents the [confused deputy problem](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").
   For a trust relationship policy example, see [Cross-service confused deputy
   prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md"). For information modifying a role's trust policy, see [Modifying a role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md").
4. If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role
   permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").
5. Complete the steps in [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md") to use IAM and Amazon S3 bucket policies to give Amazon Personalize access to your Amazon S3 resources.

###### Topics

- [Giving Amazon Personalize permission to access your resources](set-up-required-permissions.md "set-up-required-permissions.md")
- [Giving users permission to access Amazon Personalize](grant-user-permissions.md "grant-user-permissions.md")
- [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md")
- [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md")
