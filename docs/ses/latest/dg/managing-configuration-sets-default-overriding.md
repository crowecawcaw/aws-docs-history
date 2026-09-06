

# Override the current default configuration set used by the identity using the SES API
<a name="managing-configuration-sets-default-overriding"></a>

You can use the [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html) operation to send email with a different configuration set. If you do, the configuration set that you specify overrides the default configuration set for the identity.

**Note**  
Before you complete the procedure in this section, you have to install and configure the AWS CLI. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

**To override a default configuration set using the AWS CLI**
+ At the command line, enter the following command to use the [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html) operation.

```
aws sesv2 send-email --destination file://{{DESTINATION-JSON}} --content file://{{CONTENT-JSON}} --from-email-address {{ADDRESS-OR-DOMAIN}} --configuration-set-name {{CONFIG-SET}}
```

In the preceding commands, replace {{DESTINATION-JSON}} with your destination JSON file, {{CONTENT-JSON}} with your content JSON file, {{ADDRESS-OR-DOMAIN}} with your FROM email address, and {{CONFIG-SET}} with the name of the configuration set you wish to use instead of the default configuration set for the identity.

If the command executes successfully, it outputs a `MessageId`.