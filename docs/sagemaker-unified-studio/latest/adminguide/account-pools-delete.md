# Delete an account pool

To use the AWS CLI to delete an account pool, use the `delete-account-pool`
command.

###### Important

This operation will delete the account pool for the domain. This operation cannot
be undone.

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to
  run the `delete-account-pool` command with the following format,
  where the domain ID and account pool ID are required arguments.

```
aws datazone delete-account-pool --domain-identifier `DOMAIN_ID` --identifier `ACCOUNT_POOL_ID`
```

Example command:

```
aws datazone delete-account-pool --domain-identifier `dzd_dkqsou2EXAMPLE` --identifier 5htvndro7wd89z
```

This command performs the deletion and does not return any output.
