# Configure and use npm with CodeArtifact

After you create a repository in CodeArtifact, you can use the npm client to install
and publish packages. The recommended method for configuring npm with your repository endpoint and authorization token
is by using the `aws codeartifact login` command. You can also configure npm manually.

###### Contents

- [Configuring npm with the login command](npm-auth.md#configure-npm-login-command "npm-auth.md#configure-npm-login-command")
- [Configuring npm without using the
  login command](npm-auth.md#configuring-npm-without-using-the-login-command "npm-auth.md#configuring-npm-without-using-the-login-command")
- [Running npm commands](npm-auth.md#running-npm-commands "npm-auth.md#running-npm-commands")
- [Verifying npm authentication and
  authorization](npm-auth.md#verifying-npm-authentication-and-authorization "npm-auth.md#verifying-npm-authentication-and-authorization")
- [Changing back to the default npm registry](npm-auth.md#revert-default-npm-registry "npm-auth.md#revert-default-npm-registry")
- [Troubleshooting slow installs with npm 8.x or higher](npm-auth.md#troubleshooting-slow-npm-install "npm-auth.md#troubleshooting-slow-npm-install")

## Configuring npm with the login command

Use the `aws codeartifact login` command to fetch credentials for use with npm.

###### Note

If you are accessing a repository in a domain that you own, you don't need to include
`--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").

###### Important

If you are using npm 10.x or newer, you must use AWS CLI version 2.9.5 or newer to successfully run the
`aws codeartifact login` command.

```
aws codeartifact login --tool `npm` --domain `my_domain` --domain-owner `111122223333` --repository `my_repo`
```

This command makes the following changes to your ~/.npmrc file:

- Adds an authorization token after fetching it from CodeArtifact using your AWS
  credentials.
- Sets the npm registry to the repository specified by the
  `--repository` option.
- **For npm 6 and lower:** Adds `"always-auth=true"` so the authorization token is sent for
  every npm command.

The default authorization period after calling `login` is 12 hours, and `login` must
be called to periodically refresh the token. For more information about
the authorization token created with the `login` command, see
[Tokens created with the login command](tokens-authentication.md#auth-token-login "tokens-authentication.md#auth-token-login").

## Configuring npm without using the

login command

You can configure npm with your CodeArtifact repository without the `aws codeartifact login` command by
manually updating the npm configuration.

###### To configure npm without using the login command

1. In a command line, fetch a CodeArtifact authorization token and store it in an environment variable. npm will use this token
   to authenticate with your CodeArtifact repository.

###### Note

The following command is for macOS or Linux machines. For information on configuring
environment variables on a Windows machine, see [Pass an auth token using an environment variable](tokens-authentication.md#env-var "tokens-authentication.md#env-var").

```
CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text`
```

2. Get your CodeArtifact repository's endpoint by running the following command. Your repository endpoint is used to point npm to
   your repository to install or publish packages.
   - Replace `my_domain` with your CodeArtifact domain name.
   - Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
     `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").
   - Replace `my_repo` with your CodeArtifact repository name.

```
aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format npm
```

The following URL is an example repository endpoint.

```
https://`my_domain`-111122223333.d.codeartifact.`us-west-2`.amazonaws.com/npm/`my_repo`/
```

###### Important

The registry URL must end with a forward slash (/). Otherwise, you cannot connect to the repository. 3. Use the `npm config set` command to set the registry to your CodeArtifact repository. Replace the URL with the repository endpoint URL from the previous step.

```
npm config set registry=https://`my_domain`-`111122223333`.d.codeartifact.`region`.amazonaws.com/npm/`my_repo`/
```

###### Note

To use a dualstack endpoint, use the `codeartifact.`region`.on.aws` endpoint. 4. Use the `npm config set` command to add your authorization token to your npm configuration.

```
npm config set //`my_domain`-`111122223333`.d.codeartifact.`region`.amazonaws.com/npm/`my_repo`/:_authToken=$CODEARTIFACT_AUTH_TOKEN
```

**For npm 6 or lower:** To make npm always pass the auth token to CodeArtifact, even for `GET`
requests, set the `always-auth` configuration variable with `npm config set`.

```
npm config set //`my_domain`-`111122223333`.d.codeartifact.`region`.amazonaws.com/npm/`my_repo`/:always-auth=true
```

**Example npm configuration file (`.npmrc`)**

The following is an example `.npmrc` file after following the preceding
instructions to set the CodeArtifact registry endpoint, add an authentication token, and configure
`always-auth`.

```
registry=https://my_domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/npm/my-cli-repo/
//my_domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/npm/my_repo/:_authToken=eyJ2ZX...
//my_domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/npm/my_repo/:always-auth=true
```

## Running npm commands

After you configure the npm client, you can run npm commands. Assuming that
a package is present in your repository or one of its upstream repositories, you can
install it with `npm install`. For example, use the following to install the
`lodash` package.

```
npm install lodash
```

Use the following command to publish a new npm package to a CodeArtifact repository.

```
npm publish
```

For information about how to create npm packages, see [Creating Node.js
Modules](https://docs.npmjs.com/getting-started/creating-node-modules "https://docs.npmjs.com/getting-started/creating-node-modules") on the npm documentation website. For a list of npm commands supported
by CodeArtifact, see [npm Command Support](npm-commands.md "npm-commands.md").

## Verifying npm authentication and

authorization

Invoking the `npm ping` command is a way to verify the following:

- You have correctly configured your credentials so that you can authenticate to an
  CodeArtifact repository.
- The authorization configuration grants you the `ReadFromRepository` permission.

The output from a successful invocation of `npm ping` looks like the
following.

```
$ npm -d ping
npm info it worked if it ends with ok
npm info using npm@6.4.1
npm info using node@v9.5.0
npm info attempt registry request try #1 at 4:30:59 PM
npm http request GET https://<domain>.d.codeartifact.us-west-2.amazonaws.com/npm/shared/-/ping?write=true
npm http 200 https:///npm/shared/-/ping?write=true
Ping success: {}
npm timing npm Completed in 716ms
npm info ok
```

The `-d` option causes npm to print additional debug
information, including the repository URL. This information makes it easy to confirm that
npm is configured to use the repository you expect.

## Changing back to the default npm registry

Configuring npm with CodeArtifact sets the npm registry to the specified CodeArtifact repository. You can run the following command to set the npm registry back to its default
registry when you're done connecting to CodeArtifact.

```
npm config set registry https://registry.npmjs.com/
```

## Troubleshooting slow installs with npm 8.x or higher

There is a known issue in npm versions 8.x and greater where if a request is made to a package repository, and the repository
redirects the client to Amazon S3 instead of streaming the assets directly, the npm client can hang for several minutes per dependency.

Because CodeArtifact repositories are designed to always redirect the request to Amazon S3, sometimes
this issue occurs, which causes long build times due to long npm install times.
Instances of this behavior will present themselves as a progress bar showing for several minutes.

To avoid this issue, use either the `--no-progress` or `progress=false` flags with `npm`
cli commands, as shown in the following example.

```
npm install lodash --no-progress
```
