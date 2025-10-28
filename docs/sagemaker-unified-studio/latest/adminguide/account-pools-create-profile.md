# Create a project profile with an account pool

You can create a project profile that has your account pool associated such that you
can choose accounts and regions from it when creating a project with the profile.

Use the console or the CLI to set up your account pool-associated project profile.

## Create a project profile with an account pool (Console)

To configure a custom project profile using the console, see the steps in [Custom project profile](custom.md "custom.md").

## Create a project profile with an account pool (CLI)

Use the `create-project-profile` command to set up your account
pool-associated project profile.

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI
  to run the `create-project-profile` command with the following
  format, where the domain ID and name of the project profile are required
  arguments, along with the environment configuration for blueprints, which is
  provided as JSON with account pool details. The status is disabled by
  default, so the following command also enables the environment
  configuration.

```
aws datazone create-project-profile --domain-identifier `DOMAIN_ID` --name `PROFILE_NAME` --status ENABLED --environment-configuration <environment_configuration>
```

Example command:

```
aws datazone create-project-profile --domain-identifier `dzd_dkqsou2EXAMPLE` --name NAME --status ENABLED --environment-configuration '[{"name": "Tooling", "environmentBlueprintId": "4son14jdv5dq7b", "deploymentOrder": 0, "accountPools": ["`cln5qjqEXAMPLE`"]}, {"name": "DataLake", "environmentBlueprintId": "`BLUEPRINT_ID`", "accountPools": ["`cln5qjqEXAMPLE`"]}]'
```

This command returns output with the project profile details.

```
{
    "domainId": "`dzd_dkqsou2EXAMPLE`",
    "id": "aipopwr7db0rzb",
    "name": "NAME",
    "status": "ENABLED",
    "allowCustomProjectResourceTags": false,
    "environmentConfigurations": [
        {
            "name": "Tooling",
            "id": "948f994d-ed81-496a-8e1f-2f0e1288dcec",
            "environmentBlueprintId": "4son14jdv5dq7b",
            "deploymentMode": "ON_CREATE",
            "accountPools": [
                "`cln5qjqEXAMPLE`"
            ],
            "deploymentOrder": 0
        },
        {
            "name": "DataLake",
            "id": "3210351a-111c-476b-a66d-64d88a99a567",
            "environmentBlueprintId": "`BLUEPRINT_ID`",
            "deploymentMode": "ON_CREATE",
            "accountPools": [
                "`cln5qjqEXAMPLE`"
            ]
        }
    ],
    "createdAt": "2025-08-08T00:57:39.358016+00:00",
    "lastUpdatedAt": "2025-08-08T00:57:39.358016+00:00",
    "domainUnitId": "4njnngous3oyw7"
}
```
