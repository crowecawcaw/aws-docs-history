# View an account pool

To use the AWS CLI to view the accounts in an account pool, use the
`get-account-pool` command.

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to
  run the `get-account-pool` command with the following format, where
  the domain ID and account pool ID are required arguments.

```
aws datazone get-account-pool --domain-identifier `DOMAIN_ID` --identifier `ACCOUNT_POOL_ID`
```

Example command:

```
aws datazone get-account-pool --domain-identifier `dzd_dkqsou2EXAMPLE` --identifier `cln5qjqEXAMPLE`
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
    "createdBy": "",
    "createdAt": "2025-08-08T00:34:48.946606+00:00",
    "lastUpdatedAt": "2025-08-08T00:34:48.946606+00:00",
    "updatedBy": "",
    "domainUnitId": "4njnngous3oyw7"
}
```
