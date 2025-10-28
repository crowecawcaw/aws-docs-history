Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Setting up your space for

Support for Amazon CodeCatalyst

Support for Amazon CodeCatalyst manages support cases as part of Support API integration with CodeCatalyst.

The `AWSRoleForCodeCatalystSupport` role is a service role that is used for support cases in
your space. The role must be added to the designated billing account for the space.
For more information or to create the role, see [Creating the AWSRoleForCodeCatalystSupport role for your
account and space](ipa-iam-roles.md#ipa-iam-roles-support-create "ipa-iam-roles.md#ipa-iam-roles-support-create").

###### Note

For a space that was created before April 20, 2023, you must create the role in
order for support for CodeCatalyst to work for your space. If creating a space after April
20, 2023, you can create the role during space creation, on the Billing details page
in CodeCatalyst, or by clicking the support banner link in CodeCatalyst.

###### To set up support for your space

1. When you create a CodeCatalyst space, you are instructed to connect a billing
   account. The designated billing account for the space will be billed by
   AWS. For more information about creating a space, see [Creating a new space and
   development role (starting without an invitation)](sign-up-create-resources.md "sign-up-create-resources.md").
2. When you create a CodeCatalyst space, the option is available to create the
   `AWSRoleForCodeCatalystSupport` service role that allows CodeCatalyst users to access
   support. The role uses the managed policy `AmazonCodeCatalystSupportAccess`. The role must
   be added to the AWS account designated as the billing account for the
   space. For more information about creating this role, see [Creating the AWSRoleForCodeCatalystSupport role for your
   account and space](ipa-iam-roles.md#ipa-iam-roles-support-create "ipa-iam-roles.md#ipa-iam-roles-support-create").
3. For the designated billing account for the space, the space
   administrator is recommended to purchase a Business Support or Enterprise
   Support plan for the AWS account. All members in the space will be able
   to manage support cases from Support for Amazon CodeCatalyst, and channels of support will be
   aligned to the Support plan you have purchased where integrations are
   completed.
4. To create and manage support cases in CodeCatalyst, see [Creating a CodeCatalyst support case in
   CodeCatalyst](creating-a-support-case.md "creating-a-support-case.md").
