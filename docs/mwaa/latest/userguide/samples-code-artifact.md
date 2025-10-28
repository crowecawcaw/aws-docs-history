# Refreshing a CodeArtifact token

If you're using CodeArtifact to install Python dependencies, Amazon MWAA requires an active token. To allow Amazon MWAA to access an CodeArtifact repository at runtime,
you can use a [startup script](using-startup-script.md "using-startup-script.md") and set the [`PIP_EXTRA_INDEX_URL`](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-extra-index-url "https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-extra-index-url") with the token.

The following topic describes how you can create a startup script that uses the
[`get_authorization_token`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_authorization_token "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_authorization_token")
CodeArtifact API operation to retrieve a fresh token every time your environment starts up, or updates.

###### Topics

- [Version](#samples-code-artifact-version "#samples-code-artifact-version")
- [Prerequisites](#samples-code-artifact-prereqs "#samples-code-artifact-prereqs")
- [Permissions](#samples-code-artifact-permissions "#samples-code-artifact-permissions")
- [Code sample](#samples-code-artifact-code "#samples-code-artifact-code")
- [What's next?](#samples-code-artifact-next-up "#samples-code-artifact-next-up")

## Version

You can use the code example on this page with **Apache Airflow v2** in [Python 3.10](https://peps.python.org/pep-0619/ "https://peps.python.org/pep-0619/") and **Apache Airflow v3** in [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/").

## Prerequisites

To use the sample code on this page, you'll need the following:

- An [Amazon MWAA environment](get-started.md "get-started.md").
- A [CodeArtifact repository](../../../codeartifact/latest/ug/create-repo.md "../../../codeartifact/latest/ug/create-repo.md") where you store dependencies for your environment.

## Permissions

To refresh the CodeArtifact token and write the result to Amazon S3 Amazon MWAA must have the following permissions in the execution role.

- The `codeartifact:GetAuthorizationToken` action allows Amazon MWAA to retrieve a new token from CodeArtifact. The following policy grants permission for every CodeArtifact domain you create.
  You can further restrict access to your domains by modifying the resource value in the statement, and specifying only the domains that you want your environment to access.

```
{
  "Effect": "Allow",
  "Action": "codeartifact:GetAuthorizationToken",
  "Resource": "arn:aws:codeartifact:us-west-2:*:domain/*"
}
```

- The `sts:GetServiceBearerToken` action is required to call the CodeArtifact
  [`GetAuthorizationToken`](../../../codeartifact/latest/APIReference/API_GetAuthorizationToken.md "../../../codeartifact/latest/APIReference/API_GetAuthorizationToken.md") API operation.
  This operation returns a token that must be used when using a package manager such as `pip` with CodeArtifact. To use a package manager
  with a CodeArtifact repository, your environment's execution role role must allow `sts:GetServiceBearerToken` as listed in the following policy
  statement.

```
{
  "Sid": "AllowServiceBearerToken",
  "Effect": "Allow",
  "Action": "sts:GetServiceBearerToken",
  "Resource": "*"
}
```

## Code sample

The following steps describe how you can create a start up script that updates the CodeArtifact token.

1. Copy the contents of the following code sample and save locally as `code_artifact_startup_script.sh`.

```
#!/bin/sh

# Startup script for MWAA, refer to https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html

set -eu

# setup code artifact endpoint and token
# https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-0
# https://docs.aws.amazon.com/mwaa/latest/userguide/samples-code-artifact.html
DOMAIN="amazon"
DOMAIN_OWNER="112233445566"
REGION="us-west-2"
REPO_NAME="MyRepo"
echo "Getting token for CodeArtifact with args: --domain $DOMAIN --region $REGION --domain-owner $DOMAIN_OWNER"
TOKEN=$(aws codeartifact get-authorization-token --domain $DOMAIN --region $REGION --domain-owner $DOMAIN_OWNER | jq -r '.authorizationToken')
echo "Setting Pip env var for '--index-url' to point to CodeArtifact"
export PIP_EXTRA_INDEX_URL="https://aws:$TOKEN@$DOMAIN-$DOMAIN_OWNER.d.codeartifact.$REGION.amazonaws.com/pypi/$REPO_NAME/simple/"
echo "CodeArtifact startup setup complete"
```

2. Navigate to the folder where you saved the script. Use `cp` in a new prompt window to upload the script to your bucket.
   Replace `amzn-s3-demo-bucket` with your information.

```
`aws s3 cp code_artifact_startup_script.sh s3://`amzn-s3-demo-bucket`/code_artifact_startup_script.sh`
```

If successful, Amazon S3 outputs the URL path to the object:

```
upload: ./code_artifact_startup_script.sh to s3://amzn-s3-demo-bucket/code_artifact_startup_script.sh
```

After you upload the script, your environment updates and runs the script at startup.

## What's next?

- Learn how to use startup scripts to customize your environment in [Using a startup script with Amazon MWAA](using-startup-script.md "using-startup-script.md").
- Learn how to upload the DAG code in this example to the `dags` folder in your Amazon S3 bucket in [Adding or updating DAGs](configuring-dag-folder.md "configuring-dag-folder.md").
- Learn more about how to upload the `plugins.zip` file in this example to your Amazon S3 bucket in [Installing custom plugins](configuring-dag-import-plugins.md "configuring-dag-import-plugins.md").
