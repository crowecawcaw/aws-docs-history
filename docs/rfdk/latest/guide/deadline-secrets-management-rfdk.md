# Deadline Secrets Management in the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

We highly recommend enabling [Deadline Secrets Management](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html") on your RFDK farm. This will provide an additional layer of security to sensitive information that is stored in Deadline.

###### Note

Deadline Secrets Management is supported in RFDK version 0.38.0 and above and Deadline version 10.1.19 and above.

## Setting up Deadline Secrets Management in RFDK

###### Important

Along with setting up Deadline Secrets Management in RFDK, we highly recommend creating dedicated subnets for each component (e.g. `RenderQueue`, `WorkerInstanceFleet`, `SpotEventPluginFleet`, etc.) of your farm to ensure compatibility with Deadline Secrets Management [identity registration settings](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#identity-management-registration-settings-ref-label "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#identity-management-registration-settings-ref-label"). Please see [Deploying Components into Dedicated Subnets](security-best-practice.md#deploying-components-into-dedicated-subnets "security-best-practice.md#deploying-components-into-dedicated-subnets") for more information.

_New in version 0.38.0_

When using Deadline 10.1.19 or later, the `Repository` construct enables Deadline Secrets Management by default. If no administrator credentials are supplied, RFDK will create a Secret in AWS Secrets Manager with automatically generated credentials for the administrator.

If you would like to create your own credentials for Deadline Secrets Management, you can store them as a Secret in AWS Secrets Manager and provide the Secret to the `Repository` construct. This secret must be a JSON document with the following fields:

```
{
  "username": "your_secrets_management_username",
  "password": "your_secrets_management_password"
}
```

###### Note

The `password` must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, one symbol and one number.

In your RFDK app, you can provide this Secret to the `Repository` construct like this:

Python

```
vpc = ec2.Vpc(self, 'Vpc')
version = deadline.VersionQuery(self, 'Version',
  version=`'10.2.0'`,
)

secrets_management_credentials = secretsmanager.Secret.from_secret_complete_arn(
  self,
  'DeadlineSecretsManagementCredentials',
  `'your_secret_arn'`,
)

repository = deadline.Repository(self, 'Repository',
  vpc=vpc,
  version=version,
  secrets_management_settings=deadline.SecretsManagementProps(
    enabled=True,
    credentials=secrets_management_credentials,
  ),
)
```

TypeScript

```
const vpc = new ec2.Vpc(this, 'Vpc');
const version = new deadline.VersionQuery(this, 'Version', {
  version: `'10.2.0'`,
});

const secretsManagementCredentials = secretsmanager.Secret.fromSecretCompleteArn(
  this,
  'DeadlineSecretsManagementCredentials',
  `'yourSecretArn'`,
);

const repository = new deadline.Repository(this, 'Repository', {
  vpc,
  version,
  secretsManagementSettings: {
    enabled: true,
    credentials: secretsManagementCredentials,
  },
});
```

###### Note

Enabling Deadline Secrets Management on the `Repository` will implicitly make the `RenderQueue` construct configure the Deadline RCS as a [Server role](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#assigned-roles "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#assigned-roles"). Additionally, [identity registration settings](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#identity-management-registration-settings-ref-label "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#identity-management-registration-settings-ref-label") will be automatically created that will assign the [Client role](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#assigned-roles "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#assigned-roles") to instances in subnets used by the [`WorkerInstanceFleet`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md"), [`SpotEventPluginFleet`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md"), and [`UsageBasedLicensing`](../../api/latest/docs/aws-rfdk.deadline.md "../../api/latest/docs/aws-rfdk.deadline.md") constructs.

## Using Deadline Secrets Management in RFDK

This section describes how to access and use the resources configured for Deadline Secrets Management by RFDK. For general Deadline Secrets Management usage instructions and information, please refer to the [Deadline Secrets Management documentation](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html").

### Accessing Administrator Credentials

To perform administrative actions with Deadline Secrets Management, such as registering identities, assigning roles, and running Secrets Management administrator commands via DeadlineCommand, you will need to access the Deadline Secrets Management administrator credentials that were provided to the `Repository` construct. If you let RFDK generate these credentials, you can find them in AWS Secrets Manager:

1. Navigate to AWS Secrets Manager in the region your RFDK farm is deployed in.
2. Click on the Secret with a name that contains `SMAdminUser` and a description that says `Admin credentials for Deadline Secrets Management`.
3. Under "Secret value", click the "Retrieve secret value" button and you should see your Deadline Secrets Management administrator `username` and `password`.

### Rotating Deadline Secrets Management Administrator Credentials

Rotating the administrator credentials is a two step process:

1. First we change the administrator password in the Deadline Repository. For this you’ll need to get set up for [Running Administrator Commands via DeadlineCommand](#running-administrator-commands-via-deadlinecommand "#running-administrator-commands-via-deadlinecommand") and then follow the [changing administrator password instructions](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#changing-admin-password "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#changing-admin-password").
2. Next we need to make sure the password used by our RFDK app is updated, in case we redeploy anything in the future that needs to use it. To do this, you need to modify the administrator credentials Secret to the new password. To access the administrator credentials, follow the [Accessing Administrator Credentials](#accessing-administrator-credentials "#accessing-administrator-credentials") steps and then instructions on how to update the contents of that Secrets can be found in these [instructions for modifying a Secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md").

###### Warning

RFDK does not have the ability to rotate the credentials for you. You must change the administrator credentials in Deadline BEFORE changing the values in the AWS Secrets Management Secret that contains the administrator credentials.

### Forgotten Deadline Secrets Management Administrator Credentials

By default, the RFDK `Repository` construct creates an AWS Secret Manager Secret containing the Deadline Secrets Management administrator credentials with a
[removal policy](../../../cdk/latest/guide/resources.md#resources_removal "../../../cdk/latest/guide/resources.md#resources_removal") of `RETAIN` and destroying the CloudFormation stack that contains the
Secret will not delete it. If you’ve overridden the default removal policy and destroyed the CloudFormation stack, or accidentally deleted the administrator credentials
Secret outside of CDK/CloudFormation, you can attempt to recover it by following the
[restore a secret instructions](../../../secretsmanager/latest/userguide/manage_restore-secret.md "../../../secretsmanager/latest/userguide/manage_restore-secret.md") before attempting to reset the password.

If your password isn’t recoverable, you must follow the
[administrator password reset instructions](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#forgetting-a-password-with-other-existing-admin "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#forgetting-a-password-with-other-existing-admin").
These instructions list two options:

1. Use another adminstrator account to help with the password reset.
2. Uninstall and re-install the Deadline Repository. In RFDK this can be done either by destroying your app and starting over with a fresh deployment, or if you decide you do not want to delete your file system and database, you can follow the "Forgetting a password with no other admin" instructions for re-installing the Deadline Repository.

If you choose to attempt to re-install the Deadline Repository, here are some more detailed instructions for how to perform them in an RFDK deployment that uses the
tiered architecture we recommend in our [example app](https://github.com/aws/aws-rfdk/tree/release/examples/deadline/All-In-AWS-Infrastructure-Basic "https://github.com/aws/aws-rfdk/tree/release/examples/deadline/All-In-AWS-Infrastructure-Basic"):

1. Even though the Deadline Repository gets installed by the `Service Tier`, the file system and database that it gets installed onto are in the `Storage Tier`, so we need to make sure we actually run the uninstaller. If your `RenderQueue` has the `SessionManagerHelper` applied to it [like in our example](https://github.com/aws/aws-rfdk/blob/8845f4787cd7761f4b94213a7577ad6745d4246e/examples/deadline/All-In-AWS-Infrastructure-Basic/ts/lib/service-tier.ts#L209 "https://github.com/aws/aws-rfdk/blob/8845f4787cd7761f4b94213a7577ad6745d4246e/examples/deadline/All-In-AWS-Infrastructure-Basic/ts/lib/service-tier.ts#L209") you can connect to it through the AWS Console using Session Manager, and then run these commands:

```
$ cd /mnt/repo
$ sudo ./uninstall
Do you want to uninstall Deadline Repository and all of its modules? [Y/n]: y

----------------------------------------------------------------------------
Uninstall Status

 Uninstalling Deadline Repository
 0% ______________ 50% ______________ 100%
 #########################################

Info: Uninstallation completed
Press [Enter] to continue:
```

1. Once the Repository is uninstalled you can destroy the `ServiceTier` stack by running `npx cdk destroy -f "ServiceTier"` from the directory that contains your RFDK app.
2. After the `ServiceTier` has been destroyed, it can be redeployed to reinstall the repository and create a new AWS Secrets Manager Secret that contains the administrator credentials.

### Running Administrator Commands via DeadlineCommand

###### Note

If you only need to manage identities in Deadline Secrets Management, you can do so entirely in the Deadline Monitor as long as you have your administrator credentials. This is explained in further detail in [Deadline documentation on assigning identity status and roles](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#assigning-identity-status-and-roles "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#assigning-identity-status-and-roles").

Running [administrator commands for Deadline Secrets Management](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#administrator-commands "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#administrator-commands") requires a direct connection to the Deadline Repository. The Deadline Remote Connection Server (RCS), a component deployed by the `RenderQueue`, has a direct connection to the Deadline Repository and can be used to run Deadline Secrets Management commands. You can connect to the Deadline RCS by [Creating a Remote Terminal Session into the Render Queue](connecting-to-deadline-rcs.md "connecting-to-deadline-rcs.md").

Once you have connected to the Deadline RCS, you can perform administrative actions with Deadline Secrets Management via DeadlineCommand. The executable for DeadlineCommand is typically located at `/opt/Thinkbox/Deadline10/bin/deadlinecommand`. For a list of all Deadline Secrets Management administrator commands, please see the [Deadline documentation](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#administrator-commands "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/secrets-management/deadline-secrets-management.html#administrator-commands").

###### Tip

You can store your administrator password in an environment variable and provide the `--password env:<YOUR_ENV_VAR>` option to Deadline Secrets Management commands instead of letting the command prompt you for it and entering it in manually.
