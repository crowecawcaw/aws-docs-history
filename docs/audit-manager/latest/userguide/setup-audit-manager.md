

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Enabling AWS Audit Manager
<a name="setup-audit-manager"></a>





Now that you have completed the prerequisites for setting up Audit Manager, you can enable the service in your AWS environment. 

On this page you'll learn how to enable Audit Manager using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager API. Choose the method that best suits your needs, and follow the corresponding steps to get Audit Manager up and running.

## Prerequisites
<a name="setup-audit-manager-prerequisites"></a>

Make sure that you completed all of the tasks that are described in [Prerequisites for setting up AWS Audit Manager](setup-prerequisites.md). 

## Procedure
<a name="setup-audit-manager-procedure"></a>

You can enable Audit Manager using the AWS Management Console, the Audit Manager API, or the AWS Command Line Interface (AWS CLI). 

------
#### [ Audit Manager console ]

**To enable Audit Manager using the console**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. Use the credentials of your IAM identity to sign in.

1. Choose **Set up AWS Audit Manager**.   
![Screenshot of the setup call to action.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-set-up-audit-manager-console.png)

1. Under **Permissions**, no action is required. This is because Audit Manager uses a [service-linked role](https://docs.aws.amazon.com/audit-manager/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy) to connect to data sources on your behalf. You can review the service-linked role by choosing **View IAM service-linked role permission**.   
![Screenshot of the permissions section of the Audit Manager setup options.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-permissions-console.png)

1. Under **Data encryption**, the default option is for Audit Manager to create and manage an AWS KMS key for securely storing your data.   
![Screenshot of the default encryptions setting for Audit Manager setup.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-encryption-default-console.png)

   If you want to use your own customer managed key to encrypt data in Audit Manager, select the check box next to **Customize encryption settings (advanced)**. You can then choose an existing KMS key or [create a new one](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).  
![Screenshot of the custom encryptions setting for Audit Manager setup.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-encryption-custom-console.png)

1. (Optional) Under **Delegated administrator - optional**, you can specify a delegated administrator account if you want Audit Manager to run assessments for multiple accounts. For more information and recommendations, see [Enable and set up AWS Organizations](setup-recommendations.md#enabling-orgs).   
![Screenshot of the delegated administrator section of the Audit Manager setup options.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-delegated-admin-console.png)

1. (Optional) Under **AWS Config – optional**, we recommend that you enable AWS Config for an optimal experience. This enables Audit Manager to generate evidence using AWS Config rules. For instructions and recommended settings, see [Enable and set up AWS Config](setup-recommendations.md#config-recommendations).  
![Screenshot of the AWS Config section of the Audit Manager setup options.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-config-console.png)

1. (Optional) Under **Security Hub CSPM – optional**, we recommend that you enable Security Hub CSPM for an optimal experience. This enables Audit Manager to generate evidence using Security Hub CSPM checks. For instructions and recommended settings, see [Enable and set up AWS Security Hub CSPM](setup-recommendations.md#securityhub-recommendations).  
![Screenshot of the Security Hub CSPM section of the Audit Manager setup options.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-securityhub-console.png)

1. Choose **Complete setup** to finish the setup process.  
![Screenshot that shows how to complete Audit Manager setup in the console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/setup-complete-console.png)

------
#### [ AWS CLI ]

**To enable Audit Manager using the AWS CLI**  
In the command line, run the [register-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/register-account.html) command using the following setup parameters:
+ `--kms-key` (optional) – Use this parameter to encrypt your Audit Manager data using your own customer managed key. If you don't specify an option here, Audit Manager creates and manages an AWS KMS key on your behalf for the secure storage of your data. 
+ `--delegated-admin-account` (optional) – Use this parameter to designate your organization’s delegated administrator account for Audit Manager. If you don't specify an option here, no delegated administrator is registered.

Input example (replace the {{placeholder text}} with your own information):

```
aws auditmanager register-account \ 
--kms-key {{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}} \
--delegated-admin-account {{111122224444}}
```

Output example:

```
{
    "status": "ACTIVE"
}
```

For more information about the AWS CLI and for instructions on installing the AWS CLI tools, see the following in the *AWS Command Line Interface User Guide*.
+ [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
+ [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)

------
#### [ Audit Manager API ]

**To enable Audit Manager using the Audit Manager API**  
Use the [RegisterAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html) operation with the following setup parameters:
+ [kmsKey](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html#auditmanager-RegisterAccount-request-kmsKey) (optional) – Use this parameter to encrypt your Audit Manager data using your own customer managed key. If you don't specify an option here, Audit Manager creates and manages an AWS KMS key on your behalf for the secure storage of your data. 
+ [delegatedAdminAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html#auditmanager-RegisterAccount-request-delegatedAdminAccount) (optional) – Use this parameter to specify your organization’s delegated administrator account for Audit Manager. If you don't specify one, no delegated administrator is registered.

Input example (replace the {{placeholder text}} with your own information):

```
{
    "kmsKey":"{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}",
    "delegatedAdminAccount":"{{111122224444}}"
}
```

Output example:

```
{
  "status": "ACTIVE"
}
```

------

## Next steps
<a name="setup-audit-manager-next-steps"></a>

After you enable Audit Manager, we recommend that you set up some recommended features and integrations for an optimal experience. For more information, see [Enabling the recommended features and AWS services for AWS Audit Manager](setup-recommendations.md).