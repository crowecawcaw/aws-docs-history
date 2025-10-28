# Configure and use twine with CodeArtifact

[twine](https://pypi.org/project/twine/ "https://pypi.org/project/twine/") is a package publishing utility for Python packages.
To use twine to publish Python packages to your CodeArtifact repository, you must first
configure twine with your CodeArtifact repository information and credentials.

twine can only be used to publish Python packages. To install Python packages, you can use
[pip](https://pypi.org/project/pip/ "https://pypi.org/project/pip/"). For more information, see
[Configure and use pip with CodeArtifact](python-configure-pip.md "python-configure-pip.md").

## Configure twine with the `login` command

First, configure your AWS credentials for use with the AWS CLI, as described in [Getting started with CodeArtifact](getting-started.md "getting-started.md"). Then, use the CodeArtifact
`login` command to fetch credentials and configure twine with them.

###### Note

If you are accessing a repository in a domain that you own, you don't need to include
`--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").

To configure twine, run the following command.

```
aws codeartifact login --tool `twine` --domain `my_domain` --domain-owner `111122223333` --repository `my_repo`
```

`login` fetches an authorization token from CodeArtifact using your AWS credentials.
The `login` command configures twine for use with CodeArtifact by editing
`~/.pypirc` to add the repository specified by the
`--repository` option with credentials.

The default authorization period after calling `login` is 12 hours, and `login` must
be called to periodically refresh the token. For more information about
the authorization token created with the `login` command, see
[Tokens created with the login command](tokens-authentication.md#auth-token-login "tokens-authentication.md#auth-token-login").

## Configure twine without the `login` command

If you cannot use the `login` command to configure twine, you
can use the `~/.pypirc` file or environment variables. To use the
`~/.pypirc` file, add the following entries to it. The password must
be an auth token acquired by the `get-authorization-token` API.

```
[distutils]
index-servers =
 codeartifact
[codeartifact]
repository = https://`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/pypi/`my_repo`/
password = `auth-token`
username = aws
```

###### Note

To use a dualstack endpoint, use the `codeartifact.`region`.on.aws` endpoint.

To use environment variables, do the following.

###### Note

If you are accessing a repository in a domain that you own, you do not need to include the
`--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").

```
export TWINE_USERNAME=aws
export TWINE_PASSWORD=`aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text`
export TWINE_REPOSITORY_URL=`aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format pypi --query repositoryEndpoint --output text`
```

## Run twine

Before using twine to publish Python package assets, you must first configure CodeArtifact
permissions and resources.

1. Follow the steps in the
   [Setting up with AWS CodeArtifact](get-set-up-for-codeartifact.md "get-set-up-for-codeartifact.md")
   section to configure your AWS account, tools, and permissions.
2. Configure twine by following the steps in [Configure twine with the login command](#python-configure-twine-login "#python-configure-twine-login")
   or [Configure twine without the login command](#python-configure-twine-without-login "#python-configure-twine-without-login").

After you configure twine, you can run `twine` commands. Use the
following command to publish Python package assets.

```
twine upload --repository codeartifact mypackage-1.0.tgz
```

For information about how to build and package your Python application, see [Generating Distribution Archives](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives "https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives") on the Python Packaging Authority
website.
