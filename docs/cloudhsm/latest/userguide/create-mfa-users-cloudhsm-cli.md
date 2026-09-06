

# Create users with MFA enabled for CloudHSM CLI
<a name="create-mfa-users-cloudhsm-cli"></a>

Follow these steps to create AWS CloudHSM users with multi-factor authentication (MFA) enabled. 

1. Use CloudHSM CLI to log in to the HSM as an admin.

1. Use the [**user create**](cloudhsm_cli-user-create.md) command to create a user of your choice. Then follow the steps in [Set up MFA for CloudHSM CLI](set-up-mfa-for-cloudhsm-cli.md) to setup MFA for the user.