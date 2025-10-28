# View the list of accounts in an account pool

To use the AWS CLI to view the accounts in an account pool where the source is a list of
static accounts, use the `list-accounts-in-account-pool` command.

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to
  run the `list-accounts-in-account-pool` command with the following
  format, where the domain ID is a required argument.

```
aws datazone list-accounts-in-account-pool --domain-identifier `DOMAIN_ID` --identifier `ACCOUNT_POOL_ID`
```

Example command:

```
aws datazone list-accounts-in-account-pool --domain-identifier `dzd_dkqsou2EXAMPLE` --identifier `cln5qjqEXAMPLE`
```

This command returns output with the account pool account list details.

```
{
    "items": [
        {
            "awsAccountId": "`111122223333`",
            "supportedRegions": [
                "us-east-1"
            ],
            "awsAccountName": "ExampleAccount"
        }
    ]
}
```
