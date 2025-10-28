# Edit an identity to use a

default configuration set using the SES API

You can use the [PutEmailIdentityConfigurationSetAttributes](../APIReference-V2/API_PutEmailIdentityConfigurationSetAttributes.md "../APIReference-V2/API_PutEmailIdentityConfigurationSetAttributes.md") operation to add or remove a default
configuration set from an existing email identity.

###### Note

Before you complete the procedure in this section, you have to install and configure
the AWS CLI. For more information, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

**To add a default configuration set using the AWS CLI**

- At the command line, enter the following command to use the [PutEmailIdentityConfigurationSetAttributes](../APIReference-V2/API_PutEmailIdentityConfigurationSetAttributes.md "../APIReference-V2/API_PutEmailIdentityConfigurationSetAttributes.md") operation.

```
aws sesv2 put-email-identity-configuration-set-attributes --email-identity `ADDRESS-OR-DOMAIN` --configuration-set-name `CONFIG-SET`
```

In the preceding commands, replace `ADDRESS-OR-DOMAIN` with the
email identity that you want to verify. Replace `CONFIG-SET` with
the name of the configuration set you wish to set as the identity's default configuration
set.

If the command executes successfully, it exits without providing any output.

**To remove a default configuration set using the AWS CLI**

- At the command line, enter the following command to use the [PutEmailIdentityConfigurationSetAttributes](../APIReference-V2/API_PutEmailIdentityConfigurationSetAttributes.md "../APIReference-V2/API_PutEmailIdentityConfigurationSetAttributes.md") operation.

```
aws sesv2 put-email-identity-configuration-set-attributes --email-identity `ADDRESS-OR-DOMAIN`
```

In the preceding commands, replace `ADDRESS-OR-DOMAIN` with the
email identity that you want to verify.

If the command executes successfully, it exits without providing any output.
