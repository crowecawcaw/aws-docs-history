# List account pools for a domain

To use the AWS CLI to view the account pools in a domain, use the
`list-account-pools` command.

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to
  run the `list-account-pools` command with the following format, where
  the domain ID is a required argument.

```
aws datazone list-account-pools --domain-identifier `DOMAIN_ID`
```

Example command:

```
aws datazone list-account-pools --domain-identifier `dzd_dkqsou2EXAMPLE`
```

This command returns output with the account pool details.

```
{
    "items": [
        {
            "domainId": "`dzd_dkqsou2EXAMPLE`",
            "id": "5htvndro7wd89z",
            "name": "my-accountpool",
            "resolutionStrategy": "MANUAL",
            "domainUnitId": "4njnngous3oyw7",
            "createdBy": "",
            "updatedBy": ""
        }
    ]
}
```
