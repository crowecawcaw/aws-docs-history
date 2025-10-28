# Edit configuration data for extensions in

your account

This topic provides guidance on editing configuration data for extensions in your
account within a specific Region. Extensions can include configuration properties that
apply to all instances of the extension for a given account and Region. These are
defined by the extension author in the extension's configuration definition. If there
are any required properties in the extension's configuration definition, you must
specify those properties before you can use the extension in your account and
Region.

For more information about how configuration definitions are defined when developing
an extension, see the following documentation.

- [Hook configuration schema syntax reference](../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md "../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md")
- [Defining the account-level configuration of an extension](../../../cloudformation-cli/latest/userguide/resource-type-model.md#resource-type-howto-configuration "../../../cloudformation-cli/latest/userguide/resource-type-model.md#resource-type-howto-configuration")

###### Topics

- [Permissions required to
  use dynamic references](#registry-set-configuration-considerations "#registry-set-configuration-considerations")
- [Edit configuration
  data for an extension (console)](#registry-set-configuration-procedure-console "#registry-set-configuration-procedure-console")
- [Edit configuration data
  for an extension (AWS CLI)](#registry-set-configuration-procedure-cli "#registry-set-configuration-procedure-cli")

## Permissions required to

use dynamic references

If your configuration data includes dynamic references to values stored in
AWS Systems Manager or AWS Secrets Manager, any role used to provision the type (for example, when
creating or updating a stack) must have the proper permissions to retrieve that
value. Specifically:

- If the configuration data contains a parameter stored in AWS Systems Manager
  Parameter Store, the user or role used to provision the type must have
  permissions to call [GetParameter](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md").
- If the configuration data contains a secret stored in AWS Secrets Manager, the user
  or role used to provision the type must have permissions to call [GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md").

For more information, see [Get values stored in other services using dynamic
references](dynamic-references.md "dynamic-references.md").

## Edit configuration

data for an extension (console)

Follow the steps in this section to use the console to:

- View the current configuration data for an extension
- Update extension configuration data for your account

###### To view the current configuration data for an extension

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your
   AWS Region.
3. From the navigation pane, under **Registry**, choose
   **Activated extensions**.
4. Find the extension you want to view. For more information, see [View the available and activated extensions in the
   CloudFormation registry](registry-view.md "registry-view.md").
5. Choose the extension to view the extension details.
6. On the extension details page, choose the
   **Configuration** tab.
7. Expand the **Configuration schema** tab to see the
   configuration schema defined for the extension.
8. Expand the **Configuration** tab to see the current
   configuration that you have set for this extension.

###### To update configuration data for an extension

1. On the extension details page, from the **Configuration**
   tab, choose **Edit configuration**.

Alternatively, from **Actions**, choose
**Edit**, and then choose **Edit
configuration**.

CloudFormation displays the **Configure extension** page.
Make sure that **View configuration schema** is toggled on
to see the extension's current configuration definition schema. 2. In the **Configuration JSON** text box, enter a JSON
string that represents the configuration schema you want to set for this
extension. It must validate against the schema defined in
**Configuration schema**. 3. Choose **Configure extension**.

## Edit configuration data

for an extension (AWS CLI)

Follow the steps in this section to use the AWS CLI to:

- View the current configuration data for an extension
- Update extension configuration data for your account

###### To view the current configuration data for an extension

- Use the [describe-type](../../../cli/latest/reference/cloudformation/describe-type.md "../../../cli/latest/reference/cloudformation/describe-type.md") command to return detailed
  information about the extension. The `ConfigurationSchema`
  element of the output contains the current configuration definition of the
  extension in a given Region.

Alternatively, use the [batch-describe-type-configurations](../../../cli/latest/reference/cloudformation/batch-describe-type-configurations.md "../../../cli/latest/reference/cloudformation/batch-describe-type-configurations.md") command
to return configuration data about multiple extensions.

###### To update configuration data for an extension

- Use the [set-type-configuration](../../../cli/latest/reference/cloudformation/set-type-configuration.md "../../../cli/latest/reference/cloudformation/set-type-configuration.md") command to specify
  the configuration data. The JSON you pass for `--configuration`
  must validate against the extension's configuration schema.

In the following example, the **set-type-configuration**
command specifies the configuration data
`"{"CredentialKey":
 "testUserCredential"}"` for the
`--configuration` option.

```
aws cloudformation set-type-configuration --type `RESOURCE` \
  --type-name `My::Resource::Example` \
  --configuration-alias `default` \
  --configuration `"{"CredentialKey": "testUserCredential"}"` \
  --region `us-west-2`
```
