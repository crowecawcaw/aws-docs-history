# Using the AWS Workload Credentials Provider

## How the AWS Workload Credentials Provider works

The AWS Workload Credentials Provider (formerly the AWS Secrets Manager Agent) provides a client-side HTTP service
that helps you standardize how you consume secrets from Secrets Manager across your compute
environments. You can use it with the following services:

- AWS Lambda
- Amazon Elastic Container Service
- Amazon Elastic Kubernetes Service
- Amazon Elastic Compute Cloud

The AWS Workload Credentials Provider retrieves and caches secrets in memory, allowing your applications to get
secrets from localhost instead of making direct calls to Secrets Manager. The AWS Workload Credentials Provider can only
read secrets—it can't modify them.

The AWS Workload Credentials Provider is open source. The source code, installation instructions, and latest
release information are available on [GitHub](https://github.com/aws/aws-workload-credentials-provider "https://github.com/aws/aws-workload-credentials-provider").

###### Important

The AWS Workload Credentials Provider uses the AWS credentials from your environment to call Secrets Manager. It
includes protection against Server Side Request Forgery (SSRF) to help improve
secret security. The AWS Workload Credentials Provider uses the post-quantum ML-KEM key exchange as the highest-priority key exchange by default.

## Understanding AWS Workload Credentials Provider caching

The AWS Workload Credentials Provider uses an in-memory cache that resets when the AWS Workload Credentials Provider restarts. It
periodically refreshes cached secret values based on the following:

- The default refresh frequency (TTL) is 300 seconds
- You can modify the TTL using a configuration file
- The refresh occurs when you request a secret after the TTL expires

###### Note

The AWS Workload Credentials Provider doesn't include cache invalidation. If a secret rotates before the
cache entry expires, the AWS Workload Credentials Provider might return a stale secret value.

The AWS Workload Credentials Provider returns secret values in the same format as the response of
`GetSecretValue`. Secret values aren't encrypted in the cache.

###### Topics

- [Download the AWS Workload Credentials Provider](#workload-credentials-provider-download "#workload-credentials-provider-download")
- [Build the AWS Workload Credentials Provider from source](#workload-credentials-provider-build "#workload-credentials-provider-build")
- [Install the AWS Workload Credentials Provider](#workload-credentials-provider-install "#workload-credentials-provider-install")
- [Retrieve secrets with the AWS Workload Credentials Provider](#workload-credentials-provider-call "#workload-credentials-provider-call")
- [Understanding the refreshNow parameter](#workload-credentials-provider-refresh "#workload-credentials-provider-refresh")
- [Retrieve secrets across accounts with role chaining](#workload-credentials-provider-role-chaining "#workload-credentials-provider-role-chaining")
- [Pre-fetch secrets at startup](#workload-credentials-provider-prefetch "#workload-credentials-provider-prefetch")
- [Configure the AWS Workload Credentials Provider](#workload-credentials-provider-config "#workload-credentials-provider-config")
- [Optional features](#workload-credentials-provider-features "#workload-credentials-provider-features")
- [Logging](#workload-credentials-provider-log "#workload-credentials-provider-log")
- [Security considerations](#workload-credentials-provider-security "#workload-credentials-provider-security")

## Download the AWS Workload Credentials Provider

To download a pre-built binary of the AWS Workload Credentials Provider, use the following links. Releases for
Windows are signed.

| Platform | Architecture | Download URL                                                                                                                                                                                                                                             | Checksum (SHA-256)                                               |
| -------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Linux    | x86-64       | [Download for Linux x86-64 (3.1.1)](https://artifacts.awcp.global.on.aws/3.1.1/x86_64-unknown-linux-gnu/aws-workload-credentials-provider "https://artifacts.awcp.global.on.aws/3.1.1/x86_64-unknown-linux-gnu/aws-workload-credentials-provider")       | 471c1978f8bf63a0aeefb425e974ac3c816c7e04feb302236512eea375160de4 |
| Linux    | AArch64      | [Download for Linux AArch64 (3.1.1)](https://artifacts.awcp.global.on.aws/3.1.1/aarch64-unknown-linux-gnu/aws-workload-credentials-provider "https://artifacts.awcp.global.on.aws/3.1.1/aarch64-unknown-linux-gnu/aws-workload-credentials-provider")    | 8b09dc4e58b84379f580a9ae179940bcb3de0338421f638a43376bf73380ffb6 |
| Windows  | x86-64       | [Download for Windows x86-64 (3.1.1)](https://artifacts.awcp.global.on.aws/3.1.1/x86_64-pc-windows-msvc/aws-workload-credentials-provider.exe "https://artifacts.awcp.global.on.aws/3.1.1/x86_64-pc-windows-msvc/aws-workload-credentials-provider.exe") | 5fbdac4017e630556b94b90e5ed9ed11be69ac7a47e67655e20181ce990dbe12 |

## Build the AWS Workload Credentials Provider from source

Alternatively, you can build the AWS Workload Credentials Provider from source. Before you begin, make sure you
have the standard development tools and Rust tools installed for your platform.

###### Note

Building the provider with the `fips` feature enabled on macOS currently
requires the following workaround:

- Create an environment variable called `SDKROOT` which is set to
  the result of running `xcrun --show-sdk-path`

RPM-based systems

###### To build on RPM-based systems

1. Use the `install` script provided in the repository.

The script generates a random SSRF token on startup and stores it
in the file `/var/run/awssmatoken`. The token is readable
by the `aws-wcp-token` group
that the install script creates. 2. To allow your application to read the token file, you need to add
the user account that your application runs under to the
`aws-wcp-token` group. For
example, you can grant permissions for your application to read the
token file with the following usermod command, where
`<APP_USER>` is the user ID under
which your application runs.

```
sudo usermod -aG aws-wcp-token `<APP_USER>`
```

###### Install development tools

On RPM-based systems such as AL2023, install the Development
Tools group:

```
sudo yum -y groupinstall "Development Tools"
```

3. ###### Install Rust

Follow the instructions at [Install
Rust](https://www.rust-lang.org/tools/install "https://www.rust-lang.org/tools/install") in the _Rust
documentation_:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh # Follow the on-screen instructions
. "$HOME/.cargo/env"
```

4. ###### Build the provider

Build the AWS Workload Credentials Provider using the cargo build command:

```
cargo build --release
```

You will find the executable under
`target/release/aws-workload-credentials-provider`.

Debian-based systems

###### To build on Debian-based systems

1. ###### Install development tools

On Debian-based systems such as Ubuntu, install the
build-essential package:

```
sudo apt install build-essential
```

2. ###### Install Rust

Follow the instructions at [Install
Rust](https://www.rust-lang.org/tools/install "https://www.rust-lang.org/tools/install") in the _Rust
documentation_:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh # Follow the on-screen instructions
. "$HOME/.cargo/env"
```

3. ###### Build the provider

Build the AWS Workload Credentials Provider using the cargo build command:

```
cargo build --release
```

You will find the executable under
`target/release/aws-workload-credentials-provider`.

Windows

###### To build on Windows

1. ###### Set up development environment

Follow the instructions at [Set up your dev environment on Windows for Rust](https://learn.microsoft.com/en-us/windows/dev-environment/rust/setup "https://learn.microsoft.com/en-us/windows/dev-environment/rust/setup") in the
_Microsoft Windows documentation_. 2. ###### Build the provider

Build the AWS Workload Credentials Provider using the cargo build command:

```
cargo build --release
```

You will find the executable under
`target/release/aws-workload-credentials-provider.exe`.

Cross-compile natively

###### To cross-compile natively

1. ###### Install cross-compile tools

Install `cargo-xwin`:

```
cargo install cargo-xwin
```

2. ###### Add Rust build targets

Install the Windows MSVC build target:

```
rustup target add x86_64-pc-windows-msvc
```

3. ###### Build for Windows

Cross-compile the provider for Windows:

```
cargo xwin build --release --target x86_64-pc-windows-msvc
```

You will find the executable at
`target/x86_64-pc-windows-msvc/release/aws-workload-credentials-provider.exe`.

## Install the AWS Workload Credentials Provider

Choose your compute environment from the following installation options.

Amazon EC2
On Amazon EC2 Linux instances, you can install the AWS Workload Credentials Provider using
either the RPM package (available for AL2023) or the manual install
script.

###### Option A: Install the RPM package (AL2023)

1. ###### Install the package

Install the RPM package. The package manager finds the latest
version for you:

```
sudo dnf install aws-workload-credentials-provider
```

The RPM package automatically sets up the following:

    * The `aws-wcp` service user, along with the
     `awscreds` and `aws-wcp-token`
     groups.
    * The binary and helper scripts in
     `/opt/aws/workload-credentials-provider/`.
    * The AWS Secrets Manager and token systemd services,
     which it starts automatically.
    * A random SSRF token at
     `/var/run/awssmatoken`.

The Secrets Manager capability is available immediately after install. When
you install with the RPM package, the AWS Workload Credentials Provider reads configuration
options from the default path
`/etc/aws-workload-credentials-provider/config.toml`.
To customize the configuration, create or edit that file. 2. ###### (Optional) Enable the Certificate Management capability

To retrieve and refresh certificates from AWS Certificate Manager, see
[Certificate
automation](../../../acm/latest/userguide/acm-certificate-automation.md "../../../acm/latest/userguide/acm-certificate-automation.md") in the _AWS Certificate Manager User
Guide_. 3. ###### Configure application permissions

To allow your application to read the SSRF token file, add the
application's user account to the `aws-wcp-token`
group:

```
sudo usermod -aG aws-wcp-token `APP_USER`
```

Replace `APP_USER` with the user ID under
which your application runs. 4. ###### (Optional) Grant access to provider logs

To read provider logs, add your user to the
`awscreds` group, and then log out and back in (or
run `newgrp awscreds`) for the change to take
effect:

```
sudo usermod -aG awscreds `APP_USER`
```

###### Uninstall the AWS Workload Credentials Provider

To uninstall the AWS Workload Credentials Provider, run `sudo dnf remove
 aws-workload-credentials-provider`. Uninstalling stops all services
and removes the binaries and service units. The uninstall process
preserves the `aws-wcp` user, the groups, and the logs
directory.

###### Option B: Run the install script (any Linux)

1. ###### Navigate to configuration directory

Change to the configuration directory:

```
cd aws_workload_credentials_provider_common/configuration
```

2. ###### Run installation script

Run the `install` script provided in the
repository.

The script generates a random SSRF token on startup and stores it
in the file `/var/run/awssmatoken`. The token is
readable by the `aws-wcp-token`
group that the install script creates. 3. ###### Configure application permissions

Add the user account that your application runs under to the
`aws-wcp-token` group:

```
sudo usermod -aG aws-wcp-token `APP_USER`
```

Replace `APP_USER` with the user ID under
which your application runs.

Container Sidecar
You can run the AWS Workload Credentials Provider as a sidecar container alongside your application
by using Docker. Then your application can retrieve secrets from the local
HTTP server the AWS Workload Credentials Provider provides. For information about Docker, see the
[Docker documentation](https://docs.docker.com "https://docs.docker.com").

###### To create a sidecar container for the AWS Workload Credentials Provider

1. ###### Create provider Dockerfile

Create a Dockerfile for the AWS Workload Credentials Provider sidecar container:

```
# Use the latest Debian image as the base
FROM debian:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the Workload Credentials Provider binary to the container
COPY aws-workload-credentials-provider .

# Install any necessary dependencies
RUN apt-get update && apt-get install -y ca-certificates

# Set the entry point to run the provider
ENTRYPOINT ["./aws-workload-credentials-provider", "sm", "start"]
```

2. ###### Create application Dockerfile

Create a Dockerfile for your client application. 3. ###### Create Docker Compose file

Create a Docker Compose file to run both containers with a
shared network interface:

###### Important

You must load AWS credentials and the SSRF token for the
application to be able to use the AWS Workload Credentials Provider. For Amazon EKS and Amazon ECS,
see the following:

    * [Manage access](../../../eks/latest/userguide/cluster-auth.md "../../../eks/latest/userguide/cluster-auth.md") in the *Amazon EKS User
     Guide*
    * [Amazon ECS task IAM role](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") in the *Amazon ECS
     Developer Guide*

```
version: '3'
services:
    client-application:
    container_name: client-application
    build:
        context: .
        dockerfile: Dockerfile.client
    command: tail -f /dev/null  # Keep the container running


    workload-credentials-provider:
    container_name: workload-credentials-provider
    build:
        context: .
        dockerfile: Dockerfile.provider
    network_mode: "container:client-application"  # Attach to the client-application container's network
    depends_on:
        - client-application
```

4. ###### Copy provider binary

Copy the `aws-workload-credentials-provider`
binary to the same directory that contains your Dockerfiles and
Docker Compose file. 5. ###### Build and run containers

Build and run the containers using Docker Compose:

```
docker-compose up --build
```

6. ###### Next steps

You can now use the AWS Workload Credentials Provider to retrieve secrets from your
client container. For more information, see [Retrieve secrets with the AWS Workload Credentials Provider](#workload-credentials-provider-call "#workload-credentials-provider-call").

Lambda
You can [package the AWS Workload Credentials Provider as a Lambda extension](../../../lambda/latest/dg/packaging-layers.md "../../../lambda/latest/dg/packaging-layers.md"). Then you can [add it
to your Lambda function as a layer](../../../lambda/latest/dg/adding-layers.md "../../../lambda/latest/dg/adding-layers.md") and call the AWS Workload Credentials Provider from your
Lambda function to get secrets.

The following instructions show how to get a secret named
_MyTest_ by using the example script
`secrets-manager-provider-extension.sh` in the [aws-workload-credentials-provider](https://github.com/aws/aws-workload-credentials-provider "https://github.com/aws/aws-workload-credentials-provider") GitHub repository to install the
AWS Workload Credentials Provider as a Lambda extension.

###### To create a Lambda extension for the AWS Workload Credentials Provider

1. ###### Package the provider layer

From the root of the AWS Workload Credentials Provider code package, run the following
commands:

```
AWS_ACCOUNT_ID=`AWS_ACCOUNT_ID`
LAMBDA_ARN=`LAMBDA_ARN`

# Build the release binary
cargo build --release --target=x86_64-unknown-linux-gnu

# Copy the release binary into the `bin` folder
mkdir -p ./bin
cp ./target/x86_64-unknown-linux-gnu/release/aws-workload-credentials-provider ./bin/aws-workload-credentials-provider

# Copy the `secrets-manager-provider-extension.sh` example script into the `extensions` folder.
mkdir -p ./extensions
cp aws_secretsmanager_provider/examples/example-lambda-extension/secrets-manager-provider-extension.sh ./extensions

# Zip the extension shell script and the binary
zip secrets-manager-provider-extension.zip bin/* extensions/*

# Publish the layer version
LAYER_VERSION_ARN=$(aws lambda publish-layer-version \
    --layer-name secrets-manager-provider-extension \
    --zip-file "fileb://secrets-manager-provider-extension.zip" | jq -r '.LayerVersionArn')
```

2. ###### Configure SSRF token

The default configuration of the provider will automatically set
the SSRF token to the value set in the pre-set
`AWS_SESSION_TOKEN` or
`AWS_CONTAINER_AUTHORIZATION_TOKEN` environment
variables (the latter variable for Lambda functions with
SnapStart enabled). Alternatively, you can define the
`AWS_TOKEN` environment variable with an arbitrary
value for your Lambda function instead as this variable takes
precedence over the other two. If you choose to use the
`AWS_TOKEN` environment variable, you must set that
environment variable with a
`lambda:UpdateFunctionConfiguration` call. 3. ###### Attach layer to function

Attach the layer version to your Lambda function:

```
# Attach the layer version to the Lambda function
aws lambda update-function-configuration \
    --function-name $LAMBDA_ARN \
    --layers "$LAYER_VERSION_ARN"
```

4. ###### Update function code

Update your Lambda function to query
`http://localhost:2773/secretsmanager/get?secretId=MyTest`
with the `X-Aws-codes-Secrets-Token` header value set
to the value of the SSRF token sourced from one the environment
variables mentioned above to retrieve the secret. Be sure to
implement retry logic in your application code to accommodate
delays in initialization and registration of the Lambda
extension. 5. ###### Test the function

Invoke the Lambda function to verify that the secret is being
correctly fetched.

## Retrieve secrets with the AWS Workload Credentials Provider

To retrieve a secret, call the local AWS Workload Credentials Provider endpoint with the secret name or ARN as a
query parameter. By default, the AWS Workload Credentials Provider retrieves the `AWSCURRENT` version of the
secret. To retrieve a different version, use either the versionStage or versionId
parameter.

###### Important

To help protect the AWS Workload Credentials Provider, you must include a SSRF token header as part of each
request: `X-Aws-Parameters-Secrets-Token`. The AWS Workload Credentials Provider denies requests
that don't have this header or that have an invalid SSRF token. You can customize
the SSRF header name in the [Configure the AWS Workload Credentials Provider](#workload-credentials-provider-config "#workload-credentials-provider-config").

### Required permissions

The AWS Workload Credentials Provider uses the AWS SDK for Rust, which uses the [AWS
credential provider chain](../../../sdk-for-rust/latest/dg/credentials.md "../../../sdk-for-rust/latest/dg/credentials.md"). The identity of these IAM credentials
determines the permissions the AWS Workload Credentials Provider has to retrieve secrets.

- `secretsmanager:DescribeSecret`
- `secretsmanager:GetSecretValue`

For more information about permissions, see [Permissions reference for AWS Secrets Manager](auth-and-access.md#reference_iam-permissions "auth-and-access.md#reference_iam-permissions").

###### Important

After the secret value is pulled into the AWS Workload Credentials Provider, any user with access to the
compute environment and SSRF token can access the secret from the AWS Workload Credentials Provider cache.
For more information, see [Security considerations](#workload-credentials-provider-security "#workload-credentials-provider-security").

### Example requests

curl

###### Example – Get a secret using curl

The following curl example shows how to get a secret from the
AWS Workload Credentials Provider. The example relies on the SSRF being present in a file,
which is where it is stored by the install script.

```
curl -v -H \
    "X-Aws-Parameters-Secrets-Token: $(</var/run/awssmatoken)" \
    'http://localhost:2773/secretsmanager/get?secretId=`YOUR_SECRET_ID`'
```

Python

###### Example – Get a secret using Python

The following Python example shows how to get a secret from the
AWS Workload Credentials Provider. The example relies on the SSRF being present in a file,
which is where it is stored by the install script.

```
import requests
import json

# Function that fetches the secret from AWS Workload Credentials Provider for the provided secret id.
def get_secret():
    # Construct the URL for the GET request
    url = f"http://localhost:2773/secretsmanager/get?secretId=`YOUR_SECRET_ID`"

    # Get the SSRF token from the token file
    with open('/var/run/awssmatoken') as fp:
        token = fp.read()

    headers = {
        "X-Aws-Parameters-Secrets-Token": token.strip()
    }

    try:
        # Send the GET request with headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the secret value
            return response.text
        else:
            # Handle error cases
            raise Exception(f"Status code {response.status_code} - {response.text}")

    except Exception as e:
        # Handle network errors
        raise Exception(f"Error: {e}")
```

## Understanding the `refreshNow` parameter

The AWS Workload Credentials Provider uses an in-memory cache to store secret values, which it refreshes
periodically. By default, this refresh occurs when you request a secret after the Time
to Live (TTL) has expired, typically every 300 seconds. However, this approach can
sometimes result in stale secret values, especially if a secret rotates before the cache
entry expires.

To address this limitation, the AWS Workload Credentials Provider supports a parameter called
`refreshNow` in the URL. You can use this parameter to force an
immediate refresh of a secret's value, bypassing the cache and ensuring you have the
most up-to-date information.

**Default behavior (without `refreshNow`)**

- Uses cached values until TTL expires
- Refreshes secrets only after TTL (default 300 seconds)
- May return stale values if secrets rotate before the cache
  expires

**Behavior with `refreshNow=true`**

- Bypasses the cache entirely
- Retrieves the latest secret value directly from Secrets Manager
- Updates the cache with the fresh value and resets the TTL
- Ensures you always get the most current secret value

### Force-refresh a secret value

###### Important

The default value of `refreshNow` is `false`.
When set to `true`, it overrides the TTL specified in the AWS Workload Credentials Provider
configuration file and makes an API call to Secrets Manager.

curl

###### Example – Force-refresh a secret using curl

The following curl example shows how to force the AWS Workload Credentials Provider to
refresh the secret. The example relies on the SSRF being present in
a file, which is where it is stored by the install script.

```
curl -v -H \
"X-Aws-Parameters-Secrets-Token: $(</var/run/awssmatoken)" \
'http://localhost:2773/secretsmanager/get?secretId=`YOUR_SECRET_ID`&refreshNow=true'
```

Python

###### Example – Force-refresh a secret using Python

The following Python example shows how to get a secret from the
AWS Workload Credentials Provider. The example relies on the SSRF being present in a file,
which is where it is stored by the install script.

```
import requests
import json

# Function that fetches the secret from AWS Workload Credentials Provider for the provided secret id.
def get_secret():
    # Construct the URL for the GET request
    url = f"http://localhost:2773/secretsmanager/get?secretId=`YOUR_SECRET_ID`&refreshNow=true"

    # Get the SSRF token from the token file
    with open('/var/run/awssmatoken') as fp:
        token = fp.read()

    headers = {
        "X-Aws-Parameters-Secrets-Token": token.strip()
    }

    try:
        # Send the GET request with headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the secret value
            return response.text
        else:
            # Handle error cases
            raise Exception(f"Status code {response.status_code} - {response.text}")

    except Exception as e:
        # Handle network errors
        raise Exception(f"Error: {e}")
```

## Retrieve secrets across accounts with role chaining

Role chaining enables the AWS Workload Credentials Provider to retrieve secrets from other AWS accounts by
assuming IAM roles using AWS STS `AssumeRole`. The AWS Workload Credentials Provider creates and caches
a separate caching client for each unique role ARN. Each role client maintains its own
independent cache, so the same secret fetched with different roles has separate cache
entries.

### Required permissions

To use role chaining, you need the following:

- The AWS Workload Credentials Provider's environment credentials must have
  `sts:AssumeRole` permission on the target role ARN.
- The target role must have `secretsmanager:GetSecretValue` and
  `secretsmanager:DescribeSecret` permissions for the secrets you
  want to access.
- The target role's trust policy must allow the AWS Workload Credentials Provider's identity to
  assume it.

### Retrieve cross-account secrets

Include the `roleArn` query parameter in your request to
the AWS Workload Credentials Provider to specify which role to assume for the secret retrieval.

curl

###### Example – Cross-account secret using curl

```
curl -v -H \
    "X-Aws-Parameters-Secrets-Token: $(</var/run/awssmatoken)" \
    'http://localhost:2773/secretsmanager/get?secretId=`YOUR_SECRET_ID`&roleArn=arn:aws:iam::`ACCOUNT_ID`:role/`ROLE_NAME`'
```

Python

###### Example – Cross-account secret using Python

```
import requests

def get_secret_cross_account():
    secret_id = "`YOUR_SECRET_ID`"
    role_arn = "arn:aws:iam::`ACCOUNT_ID`:role/`ROLE_NAME`"
    url = f"http://localhost:2773/secretsmanager/get?secretId={secret_id}&roleArn={role_arn}"

    with open('/var/run/awssmatoken') as fp:
        token = fp.read()

    headers = {
        "X-Aws-Parameters-Secrets-Token": token.strip()
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Status code {response.status_code} - {response.text}")

    except Exception as e:
        raise Exception(f"Error: {e}")
```

### Role chaining configuration and limits

Configure role chaining with the `max_roles` option in your TOML
configuration file. This sets the maximum number of simultaneous assumed roles, in
the range 1 to 20. The default is 20.

###### Important

Assumed roles are not evicted from the AWS Workload Credentials Provider's role cache. Once the maximum
number of roles has been reached, requests with new role ARNs are rejected with
a `400` error until the AWS Workload Credentials Provider is restarted.

###### Error responses for role chaining

**`400`**

The `roleArn` format is invalid or the maximum
number of assumed roles has been reached.

**`403`**

The AWS STS `AssumeRole` call failed. Verify that the
target role's trust policy allows the AWS Workload Credentials Provider's identity to assume
it.

## Pre-fetch secrets at startup

By default, the AWS Workload Credentials Provider fetches secrets on demand when your application requests them.
With pre-fetching, the AWS Workload Credentials Provider loads specified secrets into the cache when it starts up,
so your application can access them immediately without waiting for the first API
call. Pre-fetching runs as a background task—the AWS Workload Credentials Provider begins accepting
requests immediately and does not block on pre-fetch completion.

You can specify secrets to pre-fetch in two ways:

- **Explicit secrets** – List specific
  secret IDs or ARNs.
- **Tag-based discovery** – Discover
  secrets by tag key. The AWS Workload Credentials Provider fetches all secrets that have the specified
  tag.

### Required permissions

In addition to the standard permissions for retrieving secrets, pre-fetching
requires the following:

- `secretsmanager:BatchGetSecretValue` – Required for all
  pre-fetch operations.
- `secretsmanager:ListSecrets` – Required only when using
  tag-based discovery.

### Configure pre-fetching

Add a `[capabilities.secrets_manager.prefetch]` section to your TOML
configuration file. The
following options are available:

**`cache_buffer_ratio`**

The maximum fraction of the cache to fill per client during
pre-fetch, in the range 0.1 to 1.0. The default is 0.8. When the
buffer limit is reached, the AWS Workload Credentials Provider stops pre-fetching remaining
secrets—it does not evict existing cache entries. Secrets not
loaded during pre-fetch are still available on demand.

**`max_jitter_seconds`**

A random delay in seconds before pre-fetching begins, in the range 0
to 10. The default is 0. Use this to prevent synchronized fleet-wide
API calls when multiple providers start at the same time.

###### Example Pre-fetch configuration with explicit secrets

```
[capabilities.secrets_manager.prefetch]
cache_buffer_ratio = 0.6
max_jitter_seconds = 5
secrets = [
    { secret_id = "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret-AbCdEf" },
    { secret_id = "MyOtherSecret" },
]
```

###### Example Pre-fetch configuration with tag-based discovery

```
[capabilities.secrets_manager.prefetch]
cache_buffer_ratio = 0.8
filter_tags = [
    { key = "Environment" },
    { key = "Team" },
]
```

You can also combine explicit secrets and tag-based discovery in the same
configuration. For cross-account pre-fetching, add the `role_arn`
field. For more information, see [Retrieve secrets across accounts with role chaining](#workload-credentials-provider-role-chaining "#workload-credentials-provider-role-chaining").

###### Example Pre-fetch configuration with cross-account access

```
[capabilities.secrets_manager.prefetch]
cache_buffer_ratio = 0.6
max_jitter_seconds = 5
secrets = [
    { secret_id = "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret-AbCdEf" },
    { secret_id = "cross-account-secret", role_arn = "arn:aws:iam::987654321098:role/SecretAccessRole" },
]
filter_tags = [
    { key = "Environment" },
    { key = "Team", role_arn = "arn:aws:iam::987654321098:role/SecretAccessRole" },
]
```

## Configure the AWS Workload Credentials Provider

To change the configuration of the AWS Workload Credentials Provider, create a [TOML](https://toml.io/en/ "https://toml.io/en/") config file, and then call `./aws-workload-credentials-provider sm
 start --config config.toml`.

The configuration file supports a nested format. The Secrets Manager options are
placed under `[capabilities.secrets_manager]`, with sub-sections for
cache and security settings. Logging options are placed under
`[logging]`.

###### Example nested configuration file

```
[logging]
log_level = "INFO"
log_to_file = true

[capabilities.secrets_manager]
enabled = true
http_port = 2773
region = "us-east-1"
path_prefix = "/v1/"
max_conn = 800
max_roles = 20

[capabilities.secrets_manager.cache]
ttl_seconds = 300
cache_size = 1000

[capabilities.secrets_manager.security]
ssrf_headers = ["X-Aws-Parameters-Secrets-Token", "X-Vault-Token"]
ssrf_env_variables = ["AWS_TOKEN", "AWS_SESSION_TOKEN", "AWS_CONTAINER_AUTHORIZATION_TOKEN"]
```

###### Note

Flat keys at the root level (for example, `http_port = 2773`) are
still supported for backward compatibility with existing configuration
files.

###### Secrets Manager configuration options

**`enabled`**

Whether the Secrets Manager capability is active: `true` or
`false`. The default is `true`.

**`http_port`**

The port for the local HTTP server, in the range 1024 to 65535. The
default is 2773.

**`region`**

The AWS Region to use for requests. If no Region is specified, the
AWS Workload Credentials Provider determines the Region from the SDK. For more information, see [Specify your credentials and default Region](../../../sdk-for-rust/latest/dg/credentials.md "../../../sdk-for-rust/latest/dg/credentials.md") in the _AWS
SDK for Rust Developer Guide_.

**`path_prefix`**

The URI prefix used to determine if the request is a path based request.
The default is "/v1/".

**`max_conn`**

The maximum number of connections from HTTP clients that the AWS Workload Credentials Provider
allows, in the range 1 to 1000. The default is 800.

**`max_roles`**

The maximum number of simultaneous IAM roles for cross-account access,
in the range 1 to 20. The default is 20. For more information, see [Retrieve secrets across accounts with role chaining](#workload-credentials-provider-role-chaining "#workload-credentials-provider-role-chaining").

###### Cache options (`[capabilities.secrets_manager.cache]`)

**`ttl_seconds`**

The TTL in seconds for the cached items, in the range 0 to 3600. The
default is 300. 0 indicates that there is no caching.

**`cache_size`**

The maximum number of secrets that can be stored in the cache, in the
range 1 to 1000. The default is 1000.

###### Security options (`[capabilities.secrets_manager.security]`)

**`ssrf_headers`**

A list of header names the AWS Workload Credentials Provider checks for the SSRF token. The default
is "X-Aws-Parameters-Secrets-Token, X-Vault-Token".

**`ssrf_env_variables`**

A list of environment variable names the AWS Workload Credentials Provider checks in sequential
order for the SSRF token. The environment variable can contain the token or
a reference to the token file as in:
`AWS_TOKEN=file:///var/run/awssmatoken`. The default is
"AWS\_TOKEN, AWS\_SESSION\_TOKEN, AWS\_CONTAINER\_AUTHORIZATION\_TOKEN".

###### Logging options (`[logging]`)

**`log_level`**

The level of detail reported in logs for the AWS Workload Credentials Provider: DEBUG, INFO, WARN,
ERROR, or NONE. The default is INFO.

**`log_to_file`**

Whether to log to a file or stdout/stderr: `true` or
`false`. The default is `true`.

## Optional features

The AWS Workload Credentials Provider can be built with optional features by passing the `--features`
flag to `cargo build`. The available features are:

###### Build features

**`prefer-post-quantum`**

Makes `X25519MLKEM768` the highest-priority key exchange
algorithm. Otherwise, it is available but not highest-priority.
`X25519MLKEM768` is a hybrid, post-quantum-secure key exchange
algorithm.

**`fips`**

Restricts the cipher suites used by the provider to only FIPS-approved
ciphers.

## Logging

**Local logging**

The AWS Workload Credentials Provider logs errors locally to the file
`logs/secrets_manager_provider.log` or to stdout/stderr
depending on the `log_to_file` config variable. When your
application calls the AWS Workload Credentials Provider to get a secret, those calls appear in the
local log. They do not appear in the CloudTrail logs.

**Log rotation**

The AWS Workload Credentials Provider creates a new log file when the file reaches 10 MB, and it
stores up to five log files total.

**AWS service logging**

The log does not go to Secrets Manager, CloudTrail, or CloudWatch. Requests to get secrets from
the AWS Workload Credentials Provider do not appear in those logs. When the AWS Workload Credentials Provider makes a call to
Secrets Manager to get a secret, that call is recorded in CloudTrail with a user agent
string containing `aws-workload-credentials-provider`.

You can configure logging options in the [Configure the AWS Workload Credentials Provider](#workload-credentials-provider-config "#workload-credentials-provider-config").

## Security considerations

**Domain of trust**

For a local provider architecture, the domain of trust is where the
provider endpoint and SSRF token are accessible, which is usually the
entire host. The domain of trust for the AWS Workload Credentials Provider should match the domain
where the Secrets Manager credentials are available in order to maintain the same
security posture. For example, on Amazon EC2 the domain of trust for the
AWS Workload Credentials Provider would be the same as the domain of the credentials when using
roles for Amazon EC2.

###### Important

Security conscious applications that are not already using a provider-based solution with
the Secrets Manager credentials locked down to the application should consider using the
language-specific AWS SDKs or caching solutions. For more information, see [Get secrets](retrieving-secrets.md "retrieving-secrets.md").
