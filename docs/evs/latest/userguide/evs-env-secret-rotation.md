

# Manage secrets

Amazon Elastic VMware Service stores credentials for your environment as secrets in AWS Secrets Manager in your account, and connectors read the secrets that you create. You are responsible for the lifecycle of these secrets, including rotation, because Amazon EVS doesn’t provide managed rotation.

## Secrets in an Amazon EVS environment
<a name="evs-env-secret-types"></a>

The secrets in your account depend on the deployment mode and on the connectors that you create. The following table lists the secrets for each VMware Cloud Foundation (VCF) version and who creates them.


| Secret | VCF 9.x (Self-deployed) | VCF 5.2.x (EVS-deployed) | Who creates it | 
| --- | --- | --- | --- | 
| ESX root password of each host | Yes | Yes | Amazon EVS, when it creates the host. | 
| Credentials of the VCF management appliances, such as vCenter Server, NSX, and SDDC Manager | No | Yes | Amazon EVS, when it deploys the environment and installs VCF. In Self-deployed mode, you set these passwords yourself when you install VCF. | 
| Connector credentials for VCF Operations, SDDC Manager, or vCenter Server | Yes | Yes | You, before you create a connector. For more information, see [Create a connector](evs-env-create-connector.md). | 

In EVS-deployed environments, Amazon EVS encrypts the secrets that it creates with the AWS KMS key that you choose when you create the environment. You can choose the AWS managed key for Secrets Manager or a customer managed key.

When you delete the environment, Amazon EVS also deletes the secrets that it created.

To get a secret value, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*. For EVS-deployed environments, see also [Retrieve VCF credentials and access appliances](access-vcf.md).

## How Amazon EVS accesses connector secrets
<a name="evs-env-secret-access"></a>

Amazon EVS can read a connector secret only when the secret has the tag `EvsAccess=true`. If you encrypt the secret with your own AWS KMS key, the key also needs the `EvsAccess=true` tag. Amazon EVS uses its service-linked role for this access, and the role’s permissions are scoped to resources with this tag. For more information, see [AWS managed policies for Amazon EVS](security-iam-awsmanpol.md).

## Rotate secrets
<a name="evs-env-secret-rotate"></a>

We recommend that you rotate secrets regularly on a set schedule, so that no secret is long-lived. For more information, see [Rotation schedules](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html) in the * AWS Secrets Manager User Guide*.

When you change a password in VCF, also update the matching secret, so that the secret holds the password that works. For connector secrets, this matters most, because a connector with old credentials fails its reachability check.
+ To give a vCenter connector new credentials, see [Rotate vCenter connector credentials](rotate-vcenter-credentials.md).
+ To point any connector to a different secret, see [Update a connector](evs-env-update-connector.md).

In Self-deployed environments, you are also responsible for password rotation on all VCF management appliances. For the full split of responsibilities, see [Shared responsibility and support](plan-shared-responsibility.md).