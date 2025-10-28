# Using the AWS Secrets Manager Agent

## How the Secrets Manager Agent works

The AWS Secrets Manager Agent is a client-side HTTP service that helps you standardize how you
consume secrets from Secrets Manager across your compute environments. You can use it with the
following services:

- AWS Lambda
- Amazon Elastic Container Service
- Amazon Elastic Kubernetes Service
- Amazon Elastic Compute Cloud

The Secrets Manager Agent retrieves and caches secrets in memory, allowing your applications to get
secrets from localhost instead of making direct calls to Secrets Manager. The Secrets Manager Agent can only
read secrets—it can't modify them.

###### Important

The Secrets Manager Agent uses the AWS credentials from your environment to call Secrets Manager. It
includes protection against Server Side Request Forgery (SSRF) to help improve
secret security. The Secrets Manager Agent uses the post-quantum ML-KEM key exchange as the highest-priority key exchange by default.

## Understanding Secrets Manager Agent caching

The Secrets Manager Agent uses an in-memory cache that resets when the Secrets Manager Agent restarts. It
periodically refreshes cached secret values based on the following:

- The default refresh frequency (TTL) is 300 seconds
- You can modify the TTL using a configuration file
- The refresh occurs when you request a secret after the TTL expires

###### Note

The Secrets Manager Agent doesn't include cache invalidation. If a secret rotates before the
cache entry expires, the Secrets Manager Agent might return a stale secret value.

The Secrets Manager Agent returns secret values in the same format as the response of
`GetSecretValue`. Secret values aren't encrypted in the cache.

###### Topics

- [Build the Secrets Manager Agent](#secrets-manager-agent-build "#secrets-manager-agent-build")
- [Install the Secrets Manager Agent](#secrets-manager-agent-install "#secrets-manager-agent-install")
- [Retrieve secrets with the Secrets Manager Agent](#secrets-manager-agent-call "#secrets-manager-agent-call")
- [Understanding the
  refreshNow parameter](#secrets-manager-agent-refresh "#secrets-manager-agent-refresh")
- [Configure the Secrets Manager Agent](#secrets-manager-agent-config "#secrets-manager-agent-config")
- [Optional features](#secrets-manager-agent-features "#secrets-manager-agent-features")
- [Logging](#secrets-manager-agent-log "#secrets-manager-agent-log")
- [Security considerations](#secrets-manager-agent-security "#secrets-manager-agent-security")

## Build the Secrets Manager Agent

Before you begin, ensure you have the standard development tools and Rust tools
installed for your platform.

###### Note

Building the agent with the `fips` feature enabled on macOS currently
requires the following workaround:

- Create an environment variable called `SDKROOT` which is set to
  the result of running `xcrun --show-sdk-path`

RPM-based systems

###### To build on RPM-based systems

1. Use the `install` script provided in the repository.

The script generates a random SSRF token on startup and stores it
in the file `/var/run/awssmatoken`. The token is readable
by the `awssmatokenreader` group that the install script
creates. 2. To allow your application to read the token file, you need to add
the user account that your application runs under to the
`awssmatokenreader` group. For example, you can grant
permissions for your application to read the token file with the
following usermod command, where
`<APP_USER>` is the user ID under
which your application runs.

```
sudo usermod -aG awssmatokenreader `<APP_USER>`
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

4. ###### Build the agent

Build the Secrets Manager Agent using the cargo build command:

```
cargo build --release
```

You will find the executable under
`target/release/aws_secretsmanager_agent`.

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

3. ###### Build the agent

Build the Secrets Manager Agent using the cargo build command:

```
cargo build --release
```

You will find the executable under
`target/release/aws_secretsmanager_agent`.

Windows

###### To build on Windows

1. ###### Set up development environment

Follow the instructions at [Set up your dev environment on Windows for Rust](https://learn.microsoft.com/en-us/windows/dev-environment/rust/setup "https://learn.microsoft.com/en-us/windows/dev-environment/rust/setup") in the
_Microsoft Windows documentation_. 2. ###### Build the agent

Build the Secrets Manager Agent using the cargo build command:

```
cargo build --release
```

You will find the executable under
`target/release/aws_secretsmanager_agent.exe`.

Cross-compile natively

###### To cross-compile natively

1. ###### Install cross-compile tools

On distributions where the mingw-w64 package is available such
as Ubuntu, install the cross-compile toolchain:

```
# Install the cross compile tool chain
sudo add-apt-repository universe
sudo apt install -y mingw-w64
```

2. ###### Add Rust build targets

Install the Windows GNU build target:

```
rustup target add x86_64-pc-windows-gnu
```

3. ###### Build for Windows

Cross-compile the agent for Windows:

```
cargo build --release --target x86_64-pc-windows-gnu
```

You will find the executable at
`target/x86_64-pc-windows-gnu/release/aws_secretsmanager_agent.exe`.

Cross compile with Rust cross

###### To cross-compile using Rust cross

If the cross-compile tools are not available natively on the system,
you can use the Rust cross project. For more information, see [https://github.com/cross-rs/cross](https://github.com/cross-rs/cross "https://github.com/cross-rs/cross").

###### Important

We recommend 32GB disk space for the build environment.

1. ###### Set up Docker

Install and configure Docker:

```
# Install and start docker
sudo yum -y install docker
sudo systemctl start docker
sudo systemctl enable docker # Make docker start after reboot
```

2. ###### Configure Docker permissions

Add your user to the docker group:

```
# Give ourselves permission to run the docker images without sudo
sudo usermod -aG docker $USER
newgrp docker
```

3. ###### Build for Windows

Install cross and build the executable:

```
# Install cross and cross compile the executable
cargo install cross
cross build --release --target x86_64-pc-windows-gnu
```

## Install the Secrets Manager Agent

Choose your compute environment from the following installation options.

Amazon EC2

###### To install the Secrets Manager Agent on Amazon EC2

1. ###### Navigate to configuration directory

Change to the configuration directory:

```
cd aws_secretsmanager_agent/configuration
```

2. ###### Run installation script

Run the `install` script provided in the
repository.

The script generates a random SSRF token on startup and stores it
in the file `/var/run/awssmatoken`. The token is
readable by the `awssmatokenreader` group that the
install script creates. 3. ###### Configure application permissions

Add the user account that your application runs under to the
`awssmatokenreader` group:

```
sudo usermod -aG awssmatokenreader `APP_USER`
```

Replace `APP_USER` with the user ID under
which your application runs.

Container Sidecar
You can run the Secrets Manager Agent as a sidecar container alongside your application
by using Docker. Then your application can retrieve secrets from the local
HTTP server the Secrets Manager Agent provides. For information about Docker, see the
[Docker documentation](https://docs.docker.com "https://docs.docker.com").

###### To create a sidecar container for the Secrets Manager Agent

1. ###### Create agent Dockerfile

Create a Dockerfile for the Secrets Manager Agent sidecar container:

```
# Use the latest Debian image as the base
FROM debian:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the Secrets Manager Agent binary to the container
COPY secrets-manager-agent .

# Install any necessary dependencies
RUN apt-get update && apt-get install -y ca-certificates

# Set the entry point to run the Secrets Manager Agent binary
ENTRYPOINT ["./secrets-manager-agent"]
```

2. ###### Create application Dockerfile

Create a Dockerfile for your client application. 3. ###### Create Docker Compose file

Create a Docker Compose file to run both containers with a
shared network interface:

###### Important

You must load AWS credentials and the SSRF token for the
application to be able to use the Secrets Manager Agent. For Amazon EKS and Amazon ECS,
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


    secrets-manager-agent:
    container_name: secrets-manager-agent
    build:
        context: .
        dockerfile: Dockerfile.agent
    network_mode: "container:client-application"  # Attach to the client-application container's network
    depends_on:
        - client-application
```

4. ###### Copy agent binary

Copy the `secrets-manager-agent` binary to
the same directory that contains your Dockerfiles and Docker
Compose file. 5. ###### Build and run containers

Build and run the containers using Docker Compose:

```
docker-compose up --build
```

6. ###### Next steps

You can now use the Secrets Manager Agent to retrieve secrets from your
client container. For more information, see [Retrieve secrets with the Secrets Manager Agent](#secrets-manager-agent-call "#secrets-manager-agent-call").

Lambda
You can [package the Secrets Manager Agent as a Lambda extension](../../../lambda/latest/dg/packaging-layers.md "../../../lambda/latest/dg/packaging-layers.md"). Then you can [add it
to your Lambda function as a layer](../../../lambda/latest/dg/adding-layers.md "../../../lambda/latest/dg/adding-layers.md") and call the Secrets Manager Agent from your
Lambda function to get secrets.

The following instructions show how to get a secret named
_MyTest_ by using the example script
`secrets-manager-agent-extension.sh` in [https://github.com/aws/aws-secretsmanager-agent](https://github.com/aws/aws-secretsmanager-agent "https://github.com/aws/aws-secretsmanager-agent") to install the
Secrets Manager Agent as a Lambda extension.

###### To create a Lambda extension for the Secrets Manager Agent

1. ###### Package the agent layer

From the root of the Secrets Manager Agent code package, run the following
commands:

```
AWS_ACCOUNT_ID=`AWS_ACCOUNT_ID`
LAMBDA_ARN=`LAMBDA_ARN`

# Build the release binary
cargo build --release --target=x86_64-unknown-linux-gnu

# Copy the release binary into the `bin` folder
mkdir -p ./bin
cp ./target/x86_64-unknown-linux-gnu/release/aws_secretsmanager_agent ./bin/secrets-manager-agent

# Copy the `secrets-manager-agent-extension.sh` example script into the `extensions` folder.
mkdir -p ./extensions
cp aws_secretsmanager_agent/examples/example-lambda-extension/secrets-manager-agent-extension.sh ./extensions

# Zip the extension shell script and the binary
zip secrets-manager-agent-extension.zip bin/* extensions/*

# Publish the layer version
LAYER_VERSION_ARN=$(aws lambda publish-layer-version \
    --layer-name secrets-manager-agent-extension \
    --zip-file "fileb://secrets-manager-agent-extension.zip" | jq -r '.LayerVersionArn')
```

2. ###### Configure SSRF token

The default configuration of the agent will automatically set
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

## Retrieve secrets with the Secrets Manager Agent

To retrieve a secret, call the local Secrets Manager Agent endpoint with the secret name or ARN as a
query parameter. By default, the Secrets Manager Agent retrieves the `AWSCURRENT` version of the
secret. To retrieve a different version, use either the versionStage or versionId
parameter.

###### Important

To help protect the Secrets Manager Agent, you must include a SSRF token header as part of each
request: `X-Aws-Parameters-Secrets-Token`. The Secrets Manager Agent denies requests
that don't have this header or that have an invalid SSRF token. You can customize
the SSRF header name in the [Configure the Secrets Manager Agent](#secrets-manager-agent-config "#secrets-manager-agent-config").

### Required permissions

The Secrets Manager Agent uses the AWS SDK for Rust, which uses the [AWS
credential provider chain](../../../sdk-for-rust/latest/dg/credentials.md "../../../sdk-for-rust/latest/dg/credentials.md"). The identity of these IAM credentials
determines the permissions the Secrets Manager Agent has to retrieve secrets.

- `secretsmanager:DescribeSecret`
- `secretsmanager:GetSecretValue`

For more information about permissions, see [Permissions reference for AWS Secrets Manager](auth-and-access.md#reference_iam-permissions "auth-and-access.md#reference_iam-permissions").

###### Important

After the secret value is pulled into the Secrets Manager Agent, any user with access to the
compute environment and SSRF token can access the secret from the Secrets Manager Agent cache.
For more information, see [Security considerations](#secrets-manager-agent-security "#secrets-manager-agent-security").

### Example requests

curl

###### Example – Get a secret using curl

The following curl example shows how to get a secret from the
Secrets Manager Agent. The example relies on the SSRF being present in a file,
which is where it is stored by the install script.

```
curl -v -H \\
    "X-Aws-Parameters-Secrets-Token: $(/var/run/awssmatoken)" \\
    'http://localhost:2773/secretsmanager/get?secretId=`YOUR_SECRET_ID`' \\
    echo
```

Python

###### Example – Get a secret using Python

The following Python example shows how to get a secret from the
Secrets Manager Agent. The example relies on the SSRF being present in a file,
which is where it is stored by the install script.

```
import requests
import json

# Function that fetches the secret from Secrets Manager Agent for the provided secret id.
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

## Understanding the

`refreshNow` parameter

The Secrets Manager Agent uses an in-memory cache to store secret values, which it refreshes
periodically. By default, this refresh occurs when you request a secret after the Time
to Live (TTL) has expired, typically every 300 seconds. However, this approach can
sometimes result in stale secret values, especially if a secret rotates before the cache
entry expires.

To address this limitation, the Secrets Manager Agent supports a parameter called
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
When set to `true`, it overrides the TTL specified in the Secrets Manager Agent
configuration file and makes an API call to Secrets Manager.

curl

###### Example – Force-refresh a secret using curl

The following curl example shows how to force the Secrets Manager Agent to
refresh the secret. The example relies on the SSRF being present in
a file, which is where it is stored by the install script.

```
curl -v -H \\
"X-Aws-Parameters-Secrets-Token: $(/var/run/awssmatoken)" \\
'http://localhost:2773/secretsmanager/get?secretId=`YOUR_SECRET_ID`&refreshNow=true' \\
echo
```

Python

###### Example – Force-refresh a secret using Python

The following Python example shows how to get a secret from the
Secrets Manager Agent. The example relies on the SSRF being present in a file,
which is where it is stored by the install script.

```
import requests
import json

# Function that fetches the secret from Secrets Manager Agent for the provided secret id.
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

## Configure the Secrets Manager Agent

To change the configuration of the Secrets Manager Agent, create a [TOML](https://toml.io/en/ "https://toml.io/en/") config file, and then call `./aws_secretsmanager_agent --config
 config.toml`.

###### Configuration options

**`log_level`**

The level of detail reported in logs for the Secrets Manager Agent: DEBUG, INFO, WARN,
ERROR, or NONE. The default is INFO.

**`log_to_file`**

Whether to log to a file or stdout/stderr: `true` or
`false`. The default is `true`.

**`http_port`**

The port for the local HTTP server, in the range 1024 to 65535. The
default is 2773.

**`region`**

The AWS Region to use for requests. If no Region is specified, the
Secrets Manager Agent determines the Region from the SDK. For more information, see [Specify your credentials and default Region](../../../sdk-for-rust/latest/dg/credentials.md "../../../sdk-for-rust/latest/dg/credentials.md") in the _AWS
SDK for Rust Developer Guide_.

**`ttl_seconds`**

The TTL in seconds for the cached items, in the range 0 to 3600. The
default is 300. 0 indicates that there is no caching.

**`cache_size`**

The maximum number of secrets that can be stored in the cache, in the
range 1 to 1000. The default is 1000.

**`ssrf_headers`**

A list of header names the Secrets Manager Agent checks for the SSRF token. The default
is "X-Aws-Parameters-Secrets-Token, X-Vault-Token".

**`ssrf_env_variables`**

A list of environment variable names the Secrets Manager Agent checks in sequential
order for the SSRF token. The environment variable can contain the token or
a reference to the token file as in:
`AWS_TOKEN=file:///var/run/awssmatoken`. The default is
"AWS_TOKEN, AWS_SESSION_TOKEN, AWS_CONTAINER_AUTHORIZATION_TOKEN".

**`path_prefix`**

The URI prefix used to determine if the request is a path based request.
The default is "/v1/".

**`max_conn`**

The maximum number of connections from HTTP clients that the Secrets Manager Agent
allows, in the range 1 to 1000. The default is 800.

## Optional features

The Secrets Manager Agent can be built with optional features by passing the `--features`
flag to `cargo build`. The available features are:

###### Build features

**`prefer-post-quantum`**

Makes `X25519MLKEM768` the highest-priority key exchange
algorithm. Otherwise, it is available but not highest-priority.
`X25519MLKEM768` is a hybrid, post-quantum-secure key exchange
algorithm.

**`fips`**

Restricts the cipher suites used by the agent to only FIPS-approved
ciphers.

## Logging

**Local logging**

The Secrets Manager Agent logs errors locally to the file
`logs/secrets_manager_agent.log` or to stdout/stderr
depending on the `log_to_file` config variable. When your
application calls the Secrets Manager Agent to get a secret, those calls appear in the
local log. They do not appear in the CloudTrail logs.

**Log rotation**

The Secrets Manager Agent creates a new log file when the file reaches 10 MB, and it
stores up to five log files total.

**AWS service logging**

The log does not go to Secrets Manager, CloudTrail, or CloudWatch. Requests to get secrets from
the Secrets Manager Agent do not appear in those logs. When the Secrets Manager Agent makes a call to
Secrets Manager to get a secret, that call is recorded in CloudTrail with a user agent
string containing `aws-secrets-manager-agent`.

You can configure logging options in the [Configure the Secrets Manager Agent](#secrets-manager-agent-config "#secrets-manager-agent-config").

## Security considerations

**Domain of trust**

For an agent architecture, the domain of trust is where the agent endpoint
and SSRF token are accessible, which is usually the entire host. The domain
of trust for the Secrets Manager Agent should match the domain where the Secrets Manager credentials
are available in order to maintain the same security posture. For example,
on Amazon EC2 the domain of trust for the Secrets Manager Agent would be the same as the domain
of the credentials when using roles for Amazon EC2.

###### Important

Security conscious applications that are not already using an agent solution with
the Secrets Manager credentials locked down to the application should consider using the
language-specific AWS SDKs or caching solutions. For more information, see [Get secrets](retrieving-secrets.md "retrieving-secrets.md").
