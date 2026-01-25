# Secret management lifecycle

Amazon EVS uses AWS Secrets Manager to create, encrypt, and store secrets in your account on initial environment deployment.
These secrets contain the VCF credentials needed to install and access VCF management appliances such as vCenter Server, NSX, and SDDC Manager, as well as the ESX host root password.
Amazon EVS also deletes managed secrets on your behalf when the EVS environment is deleted.

You are responsible for secret lifecyle management, including secret rotation.
Amazon EVS does not provide managed rotation of your secrets.
We recommend that you rotate secrets regularly on a set rotation window to ensure that secrets are not long-lived.
For more information, see [Rotation schedules](../../../secretsmanager/latest/userguide/rotate-secrets_schedule.md "../../../secretsmanager/latest/userguide/rotate-secrets_schedule.md") in the _AWS Secrets Manager User Guide_.
