# Registering a Delegated

Administrator for AWS Config

Delegated administrators are accounts within a given AWS Organization that are granted
additional administrative privileges for a specified AWS service. For more information,
see [Delegated
administrator](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the _AWS Organizations User Guide_. You must use the
AWS CLI to register a delegated administrator.

###### Registering a Delegated Administrator

1. Log in with management account credentials.
2. Open a command prompt or a terminal window.
3. Enter the following command to enable service access as a delegated administrator
   for your organization to deploy and manage AWS Config rules and conformance packs across
   your organization:

```
aws organizations enable-aws-service-access --service-principal=config-multiaccountsetup.amazonaws.com
```

4. Enter the following command to enable service access as a delegated administrator
   for your organization to aggregate AWS Config data across your organization:

```
aws organizations enable-aws-service-access --service-principal=config.amazonaws.com
```

5. To check if the enable service access is complete, enter the following command and
   press Enter to execute the command.

```
aws organizations list-aws-service-access-for-organization
```

You should see output similar to the following:

```
{
    "EnabledServicePrincipals": [
        {
            "ServicePrincipal": [
                "config.amazonaws.com",
                "config-multiaccountsetup.amazonaws.com"
        ],
            "DateEnabled": 1607020860.881
        }
    ]
}
```

6. Next, enter the following command to register a member account as a delegated
   administrator for AWS Config.

```
aws organizations register-delegated-administrator --service-principal=config-multiaccountsetup.amazonaws.com --account-id `MemberAccountID`
```

and

```
aws organizations register-delegated-administrator --service-principal=config.amazonaws.com --account-id `MemberAccountID`
```

7. To check if the registration of delegated administrator is complete, enter the
   following command from the management account and press Enter to execute the
   command.

```
aws organizations list-delegated-administrators --service-principal=config-multiaccountsetup.amazonaws.com
```

and

```
aws organizations list-delegated-administrators --service-principal=config.amazonaws.com
```

You should see output similar to the following:

```
{
    "DelegatedAdministrators": [
        {
            "Id": "`MemberAccountID`",
            "Arn": "arn:aws:organizations::`ManagementAccountID`:account/`o-c7esubdi38`/`MemberAccountID`",
            "Email": "`name`@amazon.com",
            "Name": "`name`",
            "Status": "`ACTIVE`",
            "JoinedMethod": "`INVITED`",
            "JoinedTimestamp": `1604867734.48`,
            "DelegationEnabledDate": `1607020986.801`
        }
    ]
}
```
