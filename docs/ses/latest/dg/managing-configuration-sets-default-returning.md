

# Retrieve the default configuration set used by the identity using the SES API
<a name="managing-configuration-sets-default-returning"></a>

You can use the [GetEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailIdentity.html) operation to return the default configuration set for an email identity, if applicable.

**Note**  
Before you complete the procedure in this section, you have to install and configure the AWS CLI. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

**To return a default configuration set using the AWS CLI**
+ At the command line, enter the following command to use the [GetEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailIdentity.html) operation.

```
aws sesv2 get-email-identity --email-identity {{ADDRESS-OR-DOMAIN}}
```

In the preceding commands, replace {{ADDRESS-OR-DOMAIN}} with with email identity for which you wish to know the default configuration set, if any.

If the command executes successfully, it provides a JSON object with the email identity details.