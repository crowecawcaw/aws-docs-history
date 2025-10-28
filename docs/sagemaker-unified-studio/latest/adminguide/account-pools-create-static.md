# Create an account pool with a static

list of account and region pairs

You can create an account pool where the accounts are provided as a list of static
accounts. Use these steps when your account pool source is a static list and not
provided by the custom Lambda function.

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI
  to run the `get-account-pool` command with the following format,
  where the domain ID, account pool name, and source of accounts are required
  arguments.

```
aws datazone create-account-pool --domain-identifier `DOMAIN_ID` --name `ACCOUNT_POOL_ID` --resolution-strategy MANUAL --account-source <source>
```

Example command:

```
aws datazone create-account-pool --domain-identifier `dzd_dkqsou2EXAMPLE` --name my-accountpool --resolution-strategy MANUAL --account-source '{"accounts": [{"awsAccountId": "`111122223333`", "supportedRegions": ["us-east-1"], "awsAccountName": "ExampleAccount"}]}'
```

This command returns output with the account pool details.

```
{
    "domainId": "`dzd_dkqsou2EXAMPLE`",
    "name": "my-accountpool",
    "id": "`cln5qjqEXAMPLE`",
    "resolutionStrategy": "MANUAL",
    "accountSource": {
        "accounts": [
            {
                "awsAccountId": "`111122223333`",
                "supportedRegions": [
                    "us-east-1"
                ],
                "awsAccountName": "ExampleAccount"
            }
        ]
    },
    "createdAt": "2025-08-08T00:34:48.946606+00:00",
    "lastUpdatedAt": "2025-08-08T00:34:48.946606+00:00",
    "domainUnitId": "4njnngous3oyw7"
}
```
