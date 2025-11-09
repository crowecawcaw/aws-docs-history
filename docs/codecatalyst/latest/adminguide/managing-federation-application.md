Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Administering Identity Center applications

An _Identity Center application_ is an association between your CodeCatalyst
space and IAM Identity Center. The Identity Center application allows users from your company directory to sign in to CodeCatalyst,
so your application name will represent your company and will be visible for selection as an
option where users from a workforce directory will access CodeCatalyst. As part of creating a space
that supports identity federation, you will choose or create the Identity Center application that will be
associated with your space. You can associate multiple spaces with a single
Identity Center application. When setting up the Identity Center application for CodeCatalyst, note that the application name must
be unique across CodeCatalyst and your IAM Identity Center instances. This uniqueness requirement helps prevent
confusion and ensures proper identification of different applications. This unique name is
primarily for administrative purposes within IAM Identity Center and doesn't affect the functionality of
CodeCatalyst.

###### Note

The name for your Identity Center application must be globally unique. In addition, since the name will be viewable for signing in and on certain pages in CodeCatalyst, choose a name that will suitably relate to your company for users signing in.

You can manage this application and its association with your space in the
Amazon CodeCatalyst page in the AWS Management Console. For information about creating your application, see [Creating a space for identity
federation](setting-up-federation-space-create.md "setting-up-federation-space-create.md").

###### Important

Dev Environments aren't available for users in spaces where Active Directory is used as
the identity provider. When planning a space where the identity provider will be Active
Directory, note that users will not be able to use Dev Environments. For more information, see
[I can't create a Dev Environment when I'm signed in to CodeCatalyst using a single sign-on
account](../userguide/devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider "../userguide/devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider").

| Topic                                                                                                                                                              | Description                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Viewing Identity Center application details](managing-federation-application-view.md "managing-federation-application-view.md")                                   | This topic describes how to view the space name, display name, and application<br>name of your Identity Center application. You can also view the users to whom you have assigned the<br>\*_Space administrator_<br>• role, and view the SSO groups that<br>you have added to your space. |
| [Editing Identity Center application details](managing-federation-application-edit.md "managing-federation-application-edit.md")                                   | This topic describes how to edit the SSO groups assigned to your space, how<br>to assign additional administrators to your space, and how to make updates to<br>your connected groups.                                                                                                    |
| [Associating a space to your<br>Identity Center application](managing-federation-application-associate.md "managing-federation-application-associate.md")          | This topic describes how to connect a CodeCatalyst space to an<br>Identity Center application.                                                                                                                                                                                            |
| [Disassociating an Identity Center application<br>from a space](managing-federation-application-disassociate.md "managing-federation-application-disassociate.md") | This topic describes how to disconnect a CodeCatalyst space from an Identity Center application.<br>You can reconnect the application later, or associate it with another<br>space.                                                                                                       |
