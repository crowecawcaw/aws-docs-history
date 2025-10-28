# Setting up a Buildkite runner

programmatically

In order to configure a Buildkite runner project programatically, you will need to
configure the following resources:

###### To create a Buildkite runner programmatically

1.  Create a Buildkite agent token and save the token in plaintext within
    AWS Secrets Manager.
2.  Set up a CodeBuild project with your preferred configuration. You will need to
    configure the following additional attributes:

        1. An environment value with name
         `CODEBUILD_CONFIG_BUILDKITE_AGENT_TOKEN`, type
         `SECRETS_MANAGER`, and a value equal to the Buildkite
         agent token associated with your Buildkite cluster.
        2. Source type equal to `NO_SOURCE`
        3. Permissions to access the secret created in step 1 in your project’s
         service role

    For example, you can use the following command to create a valid Buildkite
    runner project through the CLI:

```
aws codebuild create-project \
--name buildkite-runner-project \
--source "{\"type\": \"NO_SOURCE\",\"buildspec\":\"\"}" \
--environment "{\"image\":\"aws/codebuild/amazonlinux-x86_64-standard:5.0\",\"type\":\"LINUX_CONTAINER\",\"computeType\":\"BUILD_GENERAL1_MEDIUM\",\"environmentVariables\":[{\"name\":\"CODEBUILD_CONFIG_BUILDKITE_AGENT_TOKEN\",\"type\":\"SECRETS_MANAGER\",\"value\":\"<buildkite-secret-name>\"}]}" \
--artifacts "{\"type\": \"NO_ARTIFACTS\"}" \
--service-role `<service-role>`
```

3.  Create a Buildkite runner webhook on the project created in step 2. You will
    need to use the following configuration options when creating the
    webhook:

        1. **build-type** should be equal to
         `RUNNER_BUILDKITE_BUILD`
        2. A filter with type `EVENT` and a pattern equal to
         `WORKFLOW_JOB_QUEUED`

    For example, you can use the following command to create a valid Buildkite
    runner webhook through the CLI:

```
aws codebuild create-webhook \
--project-name buildkite-runner-project \
--filter-groups "[[{\"type\":\"EVENT\",\"pattern\":\"WORKFLOW_JOB_QUEUED\"}]]" \
--build-type RUNNER_BUILDKITE_BUILD
```

4. Save the **Payload URL** and **Secret**
   values returned by the `create-webhook` call and use the credentials
   to create a webhook within the Buildkite console. You can reference Step 3:
   Create a CodeBuild webhook within Buildkite in [Tutorial: Configure a CodeBuild-hosted Buildkite
   runner](sample-runner-buildkite.md "sample-runner-buildkite.md")
   for a guide on how to set up this resource.
