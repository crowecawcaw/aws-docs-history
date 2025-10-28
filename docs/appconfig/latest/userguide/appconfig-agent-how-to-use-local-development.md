# Working with AWS AppConfig Agent

local development mode

AWS AppConfig Agent supports a _local development mode_. If you enable local
development mode, the agent reads configuration data from a specified directory on disk. It
doesn't retrieve configuration data from AWS AppConfig. You can simulate configuration deployments
by updating files in the specified directory. We recommend local development mode for the
following use cases:

- Test different configuration versions before deploying them using AWS AppConfig.
- Test different configuration options for a new feature before committing changes to
  your code repository.
- Test different configuration scenarios to verify they work as expected.

###### Warning

Don't use local development mode in production environments. This mode doesn't support
important AWS AppConfig safety features like deployment validation and automated
rollbacks.

Use the following procedure to configure AWS AppConfig Agent for local development mode.

###### To configure AWS AppConfig Agent for local development mode

1. Install the agent using the method described for your compute environment. AWS AppConfig
   Agent works with the following AWS services:
   - [AWS Lambda](appconfig-integration-lambda-extensions.md "appconfig-integration-lambda-extensions.md")
   - [Amazon EC2](appconfig-integration-ec2.md "appconfig-integration-ec2.md")
   - [Amazon ECS
     and Amazon EKS](appconfig-integration-containers-agent.md "appconfig-integration-containers-agent.md")

2. If the agent is running, stop it.
3. Add `LOCAL_DEVELOPMENT_DIRECTORY` to the list of environment variables.
   Specify a directory on the filesystem that provides the agent with read permissions. For
   example, `/tmp/local_configs`.
4. Create a file in the directory. The file name must use the following format:

```
`application_name`:`environment_name`:`configuration_profile_name`
```

Here is an example:

```
Mobile:Development:EnableMobilePaymentsFeatureFlagConfiguration
```

###### Note

    * To view feature flag samples you can add to a file in your
     `LOCAL_DEVELOPMENT_DIRECTORY` directory, see [Feature flag
     samples for AWS AppConfig Agent local development mode](appconfig-agent-how-to-use-local-development-samples.md "appconfig-agent-how-to-use-local-development-samples.md").
    * (Optional) You can control the content type the agent returns for your
     configuration data based on the extension you give the file. For example, if you
     name the file with a .json extension, the agent returns a content type of
     `application/json` when your application requests it. If you omit the
     extension, the agent uses `application/octet-stream` for the content
     type. If you need precise control, you can provide an extension in the format
     `.`type`%`subtype``.
     The agent will return a content type of `.type/subtype`.

5. Run the following command to restart the agent and request the configuration
   data.

```
curl http://localhost:2772/applications/`application_name`/environments/`environment_name`/configurations/`configuration_name`
```

The agent checks for changes to the local file at the poll interval specified for the
agent. If the poll interval isn't specified, the agent uses the default interval of 45
seconds. This check at the poll interval ensures that the agent behaves the same in a local
development environment as it does when configured to interact with the AWS AppConfig service.

###### Note

To deploy a new version of a local development configuration file, update the file
with new data.
