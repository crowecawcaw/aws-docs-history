# Enabling AWS Audit Manager

Now that you have completed the prerequisites for setting up Audit Manager, you can enable the
service in your AWS environment.

On this page you'll learn how to enable Audit Manager using the Audit Manager console, the AWS Command Line Interface
(AWS CLI), or the Audit Manager API. Choose the method that best suits your needs, and follow the
corresponding steps to get Audit Manager up and running.

## Prerequisites

Make sure that you completed all of the tasks that are described in [Prerequisites for setting up AWS Audit Manager](setup-prerequisites.md "setup-prerequisites.md").

## Procedure

You can enable Audit Manager using the AWS Management Console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI).

Audit Manager console

###### To enable Audit Manager using the console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. Use the credentials of your IAM identity to sign in.
3. Choose **Set up AWS Audit Manager**.

![Screenshot of the setup call to action.](images/setup-set-up-audit-manager-console.png) 4. Under **Permissions**, no action is required. This is
because Audit Manager uses a [service-linked role](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy") to connect to data sources on your
behalf. You can review the service-linked role by choosing
**View IAM service-linked role permission**.

![Screenshot of the permissions section of the Audit Manager setup options.](images/setup-permissions-console.png) 5. Under **Data encryption**, the default option is for
Audit Manager to create and manage an AWS KMS key for securely storing your
data.

![Screenshot of the default encryptions setting for Audit Manager setup.](images/setup-encryption-default-console.png)

If you want to use your own customer managed key to encrypt data in Audit Manager, select
the check box next to **Customize encryption settings
(advanced)**. You can then choose an existing KMS key or
[create a new
one](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").

![Screenshot of the custom encryptions setting for Audit Manager setup.](images/setup-encryption-custom-console.png) 6. (Optional) Under **Delegated administrator -
optional**, you can specify a delegated administrator
account if you want Audit Manager to run assessments for multiple accounts.
For more information and recommendations, see [Enable and set up AWS Organizations](setup-recommendations.md#enabling-orgs "setup-recommendations.md#enabling-orgs").

![Screenshot of the delegated administrator section of the Audit Manager setup options.](images/setup-delegated-admin-console.png) 7. (Optional) Under **AWS Config –
optional**, we recommend that you enable AWS Config for an
optimal experience. This enables Audit Manager to generate evidence using
AWS Config rules. For instructions and recommended settings, see [Enable and set up AWS Config](setup-recommendations.md#config-recommendations "setup-recommendations.md#config-recommendations").

![Screenshot of the AWS Config section of the Audit Manager setup options.](images/setup-config-console.png) 8. (Optional) Under **Security Hub CSPM – optional**, we recommend
that you enable Security Hub CSPM for an optimal experience. This enables Audit Manager to
generate evidence using Security Hub CSPM checks. For instructions and recommended
settings, see [Enable and set up AWS Security Hub CSPM](setup-recommendations.md#securityhub-recommendations "setup-recommendations.md#securityhub-recommendations").

![Screenshot of the Security Hub CSPM section of the Audit Manager setup options.](images/setup-securityhub-console.png) 9. Choose **Complete setup** to finish the setup
process.

![Screenshot that shows how to complete Audit Manager setup in the console.](images/setup-complete-console.png)

AWS CLI

###### To enable Audit Manager using the AWS CLI

In the command line, run the [register-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/register-account.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/register-account.html") command using the following setup
parameters:

- `--kms-key` (optional) – Use this parameter
  to encrypt your Audit Manager data using your own customer managed key. If you
  don't specify an option here, Audit Manager creates and manages an
  AWS KMS key on your behalf for the secure storage of your
  data.
- `--delegated-admin-account` (optional) – Use
  this parameter to designate your organization’s delegated
  administrator account for Audit Manager. If you don't specify an option
  here, no delegated administrator is registered.

Input example (replace the `placeholder text`
with your own information):

```
aws auditmanager register-account \
--kms-key `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` \
--delegated-admin-account `111122224444`
```

Output example:

```
{
    "status": "ACTIVE"
}
```

For more information about the AWS CLI and for instructions on installing the
AWS CLI tools, see the following in the _AWS Command Line Interface User
Guide_.

- [AWS
  Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md")
- [Getting Set Up with the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md")

Audit Manager API

###### To enable Audit Manager using the Audit Manager API

Use the [RegisterAccount](../APIReference/API_RegisterAccount.md "../APIReference/API_RegisterAccount.md") operation with the following setup
parameters:

- [kmsKey](../APIReference/API_RegisterAccount.md#auditmanager-RegisterAccount-request-kmsKey "../APIReference/API_RegisterAccount.md#auditmanager-RegisterAccount-request-kmsKey") (optional) – Use this parameter to
  encrypt your Audit Manager data using your own customer managed key. If you don't
  specify an option here, Audit Manager creates and manages an AWS KMS key
  on your behalf for the secure storage of your data.
- [delegatedAdminAccount](../APIReference/API_RegisterAccount.md#auditmanager-RegisterAccount-request-delegatedAdminAccount "../APIReference/API_RegisterAccount.md#auditmanager-RegisterAccount-request-delegatedAdminAccount") (optional) – Use this
  parameter to specify your organization’s delegated administrator
  account for Audit Manager. If you don't specify one, no delegated
  administrator is registered.

Input example (replace the `placeholder text`
with your own information):

```
{
    "kmsKey":"`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`",
    "delegatedAdminAccount":"`111122224444`"
}
```

Output example:

```
{
  "status": "ACTIVE"
}
```

## Next steps

After you enable Audit Manager, we recommend that you set up some recommended features and
integrations for an optimal experience. For more information, see
[Enabling the recommended features and
AWS services for AWS Audit Manager](setup-recommendations.md "setup-recommendations.md").
