

# Building Rust Lambda functions with Cargo Lambda in AWS SAM
<a name="building-rust"></a>

Use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) with your Rust AWS Lambda functions.

**Topics**
+ [Prerequisites](#building-rust-prerequisites)
+ [Configuring AWS SAM to use with Rust Lambda functions](#building-rust-configure)
+ [Examples](#building-rust-examples)
+ [Optimizing Rust builds in GitHub Actions](#building-rust-optimize-ci)

## Prerequisites
<a name="building-rust-prerequisites"></a>

**Rust language**  
To install Rust, see [Install Rust](https://www.rust-lang.org/tools/install) in the *Rust language website*.

**Cargo Lambda**  
The AWS SAM CLI requires installation of [Cargo Lambda](https://www.cargo-lambda.info/guide/what-is-cargo-lambda.html), a subcommand for Cargo. For installation instructions, see [Installation](https://www.cargo-lambda.info/guide/installation.html) in the *Cargo Lambda documentation*.

**Docker**  
Building and testing Rust Lambda functions requires Docker. For installation instructions, see [Installing Docker](install-docker.md).

## Configuring AWS SAM to use with Rust Lambda functions
<a name="building-rust-configure"></a>

### Step 1: Configure your AWS SAM template
<a name="building-rust-configure-template"></a>

Configure your AWS SAM template with the following:
+ **Binary** – Optional. Specify when a single Cargo package defines more than one binary, to identify which binary to build for this function. You don't need this property when each function is its own Cargo package, such as in a Cargo workspace.
+ **BuildMethod** – `rust-cargolambda`.
+ **CodeUri** – path to your `Cargo.toml` file.
+ **Handler** – `bootstrap`.
+ **Runtime** – `provided.al2023`.

To learn more about custom runtimes, see [Custom AWS Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html) in the *AWS Lambda Developer Guide*.

Here is an example of a configured AWS SAM template:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Metadata:
      BuildMethod: rust-cargolambda
      BuildProperties: function_a
    Properties:
      CodeUri: ./rust_app
      Handler: bootstrap
      Runtime: provided.al2023
...
```

### Step 2: Use the AWS SAM CLI with your Rust Lambda function
<a name="building-rust-configure-cli"></a>

Use any AWS SAM CLI command with your AWS SAM template. For more information, see [AWS SAM CLI](using-sam-cli.md).

## Examples
<a name="building-rust-examples"></a>

### Hello World example
<a name="building-rust-examples-hello"></a>

**In this example, we build the sample Hello World application using Rust as our runtime.**

First, we initialize a new serverless application using `sam init`. During the interactive flow, we select the **Hello World application** and choose the **Rust** runtime.

```
$ sam init
...
Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: {{1}}

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Multi-step workflow
        3 - Serverless API
        ...
Template: {{1}}

Use the most popular runtime and package type? (Python and zip) [y/N]: {{ENTER}}

Which runtime would you like to use?
        1 - dotnet8
        2 - dotnet6
        3 - go (provided.al2)
        ...
        18 - python3.11
        19 - python3.10
        20 - ruby4.0
        21 - ruby3.3
        22 - ruby3.2
        23 - rust (provided.al2)
        24 - rust (provided.al2023)
Runtime: {{24}}

Based on your selections, the only Package type available is Zip.
We will proceed to selecting the Package type as Zip.

Based on your selections, the only dependency manager available is cargo.
We will proceed copying the template using cargo.

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: {{ENTER}}

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: {{ENTER}}

Project name [sam-app]: {{hello-rust}}

    -----------------------
    Generating application:
    -----------------------
    Name: hello-rust
    Runtime: rust (provided.al2023)
    Architectures: x86_64
    Dependency Manager: cargo
    Application Template: hello-world
    Output Directory: .
    Configuration file: hello-rust/samconfig.toml
    
    Next steps can be found in the README file at hello-rust/README.md
        

Commands you can use next
=========================
[*] Create pipeline: cd hello-rust && sam pipeline init --bootstrap
[*] Validate SAM template: cd hello-rust && sam validate
[*] Test Function in the Cloud: cd hello-rust && sam sync --stack-name {stack-name} --watch
```

The following is the structure of our Hello World application:

```
hello-rust
├── README.md
├── events
│   └── event.json
├── rust_app
│   ├── Cargo.toml
│   └── src
│       └── main.rs
├── samconfig.toml
└── template.yaml
```

In our AWS SAM template, our Rust function is defined as the following:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function 
    Metadata:
      BuildMethod: rust-cargolambda 
    Properties:
      CodeUri: ./rust_app
      Handler: bootstrap
      Runtime: provided.al2023
      Architectures:
        - x86_64
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

Next, we run `sam build` to build our application and prepare for deployment. The AWS SAM CLI creates a `.aws-sam` directory and organizes our build artifacts there. Our function is built using Cargo Lambda and stored as an executable binary at `.aws-sam/build/HelloWorldFunction/bootstrap`.

**Note**  
If you plan on running the **sam local invoke** command in MacOS, you need to build functions different before invoking. To do this, use the following command:  
**SAM\_BUILD\_MODE=debug sam build**
This command is only needed if local testing will be done. This is not recommended when building for deployment.

```
hello-rust$ sam build
Starting Build use cache
Cache is invalid, running build and copying resources for following functions (HelloWorldFunction)
Building codeuri: /Users/.../hello-rust/rust_app runtime: provided.al2023 metadata: {'BuildMethod': 'rust-cargolambda'} architecture: x86_64 functions: HelloWorldFunction
Running RustCargoLambdaBuilder:CargoLambdaBuild
Running RustCargoLambdaBuilder:RustCopyAndRename

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {{stack-name}} --watch
[*] Deploy: sam deploy --guided
```

Next, we deploy our application using `sam deploy --guided`.

```
hello-rust$ sam deploy --guided

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [hello-rust]: {{ENTER}}
        AWS Region [us-west-2]: {{ENTER}}
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: {{ENTER}}
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: {{ENTER}}
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]: {{ENTER}}
        HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: {{y}}
        Save arguments to configuration file [Y/n]: {{ENTER}}
        SAM configuration file [samconfig.toml]: {{ENTER}}
        SAM configuration environment [default]: {{ENTER}}

        Looking for resources needed for deployment:

        ...

        Uploading to hello-rust/56ba6585d80577dd82a7eaaee5945c0b  817973 / 817973  (100.00%)

        Deploying with following values
        ===============================
        Stack name                   : hello-rust
        Region                       : us-west-2
        Confirm changeset            : True
        Disable rollback             : False
        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisam-s3-demo-bucket-1a4x26zbcdkqr
        Capabilities                 : ["CAPABILITY_IAM"]
        Parameter overrides          : {}
        Signing Profiles             : {}

Initiating deployment
=====================

        Uploading to hello-rust/a4fc54cb6ab75dd0129e4cdb564b5e89.template  1239 / 1239  (100.00%)


Waiting for changeset to be created..

CloudFormation stack changeset
---------------------------------------------------------------------------------------------------------
Operation                  LogicalResourceId          ResourceType               Replacement              
---------------------------------------------------------------------------------------------------------
+ Add                      HelloWorldFunctionHelloW   AWS::Lambda::Permission    N/A                      
                           orldPermissionProd                                                             
...                    
---------------------------------------------------------------------------------------------------------

Changeset created successfully. arn:aws:cloudformation:us-west-2:012345678910:changeSet/samcli-deploy1681427201/f0ef1563-5ab6-4b07-9361-864ca3de6ad6


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: {{y}}

2023-04-13 13:07:17 - Waiting for stack create/update to complete

CloudFormation events from stack operations (refresh every 5.0 seconds)
---------------------------------------------------------------------------------------------------------
ResourceStatus             ResourceType               LogicalResourceId          ResourceStatusReason     
---------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS         AWS::IAM::Role             HelloWorldFunctionRole     -                        
CREATE_IN_PROGRESS         AWS::IAM::Role             HelloWorldFunctionRole     Resource creation        
...
---------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
---------------------------------------------------------------------------------------------------------
Outputs                                                                                                 
---------------------------------------------------------------------------------------------------------
Key                 HelloWorldFunctionIamRole                                                           
Description         Implicit IAM Role created for Hello World function                                  
Value               arn:aws:iam::012345678910:role/hello-rust-HelloWorldFunctionRole-10II2P13AUDUY      

Key                 HelloWorldApi                                                                       
Description         API Gateway endpoint URL for Prod stage for Hello World function                    
Value               https://ggdxec9le9.execute-api.us-west-2.amazonaws.com/Prod/hello/                  

Key                 HelloWorldFunction                                                                  
Description         Hello World Lambda Function ARN                                                     
Value               arn:aws:lambda:us-west-2:012345678910:function:hello-rust-HelloWorldFunction-       
yk4HzGzYeZBj                                                                                            
---------------------------------------------------------------------------------------------------------


Successfully created/updated stack - hello-rust in us-west-2
```

To test, we can invoke our Lambda function using the API endpoint.

```
$ curl https://ggdxec9le9.execute-api.us-west-2.amazonaws.com/Prod/hello/
Hello World!%
```

To test our function locally, first we ensure our function’s `Architectures` property matches our local machine.

```
...
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Metadata:
      BuildMethod: rust-cargolambda # More info about Cargo Lambda: https://github.com/cargo-lambda/cargo-lambda
    Properties:
      CodeUri: ./rust_app   # Points to dir of Cargo.toml
      Handler: bootstrap    # Do not change, as this is the default executable name produced by Cargo Lambda
      Runtime: provided.al2023
      Architectures:
        - arm64
...
```

Since we modified our architecture from `x86_64` to `arm64` in this example, we run `sam build` to update our build artifacts. We then run `sam local invoke` to locally invoke our function.

```
hello-rust$ sam local invoke
Invoking bootstrap (provided.al2023)
Local image was not found.
Removing rapid images for repo public.ecr.aws/sam/emulation-provided.al2023
Building image.....................................................................................................................................
Using local image: public.ecr.aws/lambda/provided:al2023-rapid-arm64.

Mounting /Users/.../hello-rust/.aws-sam/build/HelloWorldFunction as /var/task:ro,delegated, inside runtime container
START RequestId: fbc55e6e-0068-45f9-9f01-8e2276597fc6 Version: $LATEST
{"statusCode":200,"body":"Hello World!"}END RequestId: fbc55e6e-0068-45f9-9f01-8e2276597fc6
REPORT RequestId: fbc55e6e-0068-45f9-9f01-8e2276597fc6  Init Duration: 0.68 ms  Duration: 130.63 ms     Billed Duration: 131 ms     Memory Size: 128 MB     Max Memory Used: 128 MB
```

### Single Lambda function project
<a name="building-rust-examples-single"></a>

**Here is an example of a serverless application containing one Rust Lambda function. **

Project directory structure:

```
.
├── Cargo.lock
├── Cargo.toml
├── src
│   └── main.rs
└── template.yaml
```

AWS SAM template:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Metadata:
      BuildMethod: rust-cargolambda
    Properties:
      CodeUri: ./
      Handler: bootstrap
      Runtime: provided.al2023
...
```

### Multiple Lambda function project
<a name="building-rust-examples-multiple"></a>

**Here is an example of a serverless application containing multiple Rust Lambda functions, organized as a Cargo workspace.**

We recommend a Cargo workspace for applications with multiple Rust Lambda functions. Each function is its own package, so functions can declare independent dependencies while sharing common code through a library package. Each package produces a single binary named after the package, so you don't need to set the `Binary` build property.

Project directory structure:

```
.
├── Cargo.lock
├── Cargo.toml
├── function_a
│   ├── Cargo.toml
│   └── src
│       └── main.rs
├── function_b
│   ├── Cargo.toml
│   └── src
│       └── main.rs
└── template.yaml
```

Workspace `Cargo.toml` file, at the root of the project:

```
[workspace]
resolver = "2"
members = [
    "function_a",
    "function_b",
]

[workspace.dependencies]
lambda_runtime = "0.13"
serde = { version = "1", features = ["derive"] }
tokio = { version = "1", features = ["macros", "rt"] }
```

`Cargo.toml` file for each function, such as `function_a/Cargo.toml`:

```
[package]
name = "function_a"
version = "0.1.0"
edition = "2021"

[dependencies]
lambda_runtime = { workspace = true }
serde = { workspace = true }
tokio = { workspace = true }
```

AWS SAM template. The `CodeUri` of each function points to that function's package directory:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  FunctionA:
    Type: AWS::Serverless::Function
    Metadata:
      BuildMethod: rust-cargolambda
    Properties:
      CodeUri: ./function_a
      Handler: bootstrap
      Runtime: provided.al2023
  FunctionB:
    Type: AWS::Serverless::Function
    Metadata:
      BuildMethod: rust-cargolambda
    Properties:
      CodeUri: ./function_b
      Handler: bootstrap
      Runtime: provided.al2023
```

**Note**  
The AWS SAM CLI builds every function in the workspace into the workspace's shared `target` directory, so Cargo compiles shared dependencies once instead of once for each function. This behavior requires AWS SAM CLI version 1.165.0 or later. On earlier versions, each function is built in its own `target` directory and the full dependency tree is recompiled for every function, which makes builds slower as you add functions.

Give each function package a unique binary name. Package names are unique within a workspace, so the default binary name is already unique. If you override the binary name with a `[[bin]]` section, don't give two packages the same binary name. They compile to the same path in the shared `target` directory and overwrite each other. The AWS SAM CLI logs a warning when it detects this.

Alternatively, a single package can define multiple binaries. In that case, use the `Binary` build property to select the binary for each function:

```
Resources:
  FunctionA:
    Type: AWS::Serverless::Function
    Metadata:
      BuildMethod: rust-cargolambda
      BuildProperties:
        Binary: function_a
    Properties:
      CodeUri: ./
      Handler: bootstrap
      Runtime: provided.al2023
```

## Optimizing Rust builds in GitHub Actions
<a name="building-rust-optimize-ci"></a>

Rust builds are compute intensive, and a continuous integration runner starts with no compiled artifacts. Applications with several functions that share large dependencies, such as an AWS SDK, can spend most of their build time compiling the same dependencies. The following practices reduce build time in GitHub Actions.

**Use AWS SAM CLI version 1.165.0 or later for workspaces**  
Version 1.165.0 and later build every member of a Cargo workspace into the workspace's shared `target` directory, so shared dependencies are compiled once per build instead of once for each function. Specify the minimum version when you install the AWS SAM CLI so that a build doesn't silently fall back to the slower behavior.

**Cache the Cargo registry and `target` directory**  
Cache the Cargo registry (`~/.cargo/registry` and `~/.cargo/git/db`) and the workspace `target` directory between runs, so that unchanged dependencies are restored instead of recompiled. Use a separate cache for each compilation target. A job that cross-compiles release artifacts for `arm64` produces different artifacts than a job that compiles natively for `x86_64`, so a shared cache never matches.

**Include build settings in the cache key**  
Cargo includes settings such as `opt-level` and `codegen-units` in the fingerprint that it uses to decide whether a compiled artifact can be reused. If you change the `[profile.release]` section of your workspace `Cargo.toml` file without changing the cache key, the cache is restored but every crate is recompiled anyway. Include a hash of the workspace `Cargo.toml` file in the cache key so that changing a profile setting starts a new cache.

**Commit your `Cargo.lock` file**  
Lambda functions are executables, so commit your `Cargo.lock` file. This gives you reproducible builds and a stable cache key that changes only when your dependencies change.

**Tune the release profile for build time and cold start**  
Your function code is recompiled on every run, because it changes more often than your dependencies. The default release profile optimizes for runtime throughput, which many Lambda functions don't need. Optimizing for size produces smaller binaries, which also helps cold start time, and increasing the number of code generation units increases parallelism during compilation. Leave link time optimization (`lto`) disabled, because it makes compilation slower. Add the following to your workspace `Cargo.toml` file:  

```
[profile.release]
opt-level = "s"
codegen-units = 256
lto = false
strip = true
```
Measure the effect on your own application. These settings trade a small amount of runtime performance for build time and binary size.

**Avoid duplicate workflow runs**  
A workflow that runs on both `push` and `pull_request` events runs twice for the same commit. GitHub Actions caches are scoped by branch and pull request, so the two runs write to different cache scopes and neither reuses the other's cache. Use a concurrency group that is keyed on the head commit, so that only one run builds each commit.

The following workflow builds a Cargo workspace of Rust Lambda functions for `arm64`, and applies the preceding practices:

```
name: Build

on:
  push:
    branches: [main]
  pull_request:

# Collapse the push and pull_request runs for the same commit into a single run.
concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.head.sha || github.sha }}
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5

      - uses: dtolnay/rust-toolchain@stable
        with:
          targets: aarch64-unknown-linux-gnu

      # Cache the Cargo registry and the workspace target directory. The key covers
      # the compilation target, Cargo.lock, and the workspace Cargo.toml, so that
      # changing a dependency or a release profile setting starts a new cache
      # instead of restoring one whose artifacts Cargo discards.
      - uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry/index
            ~/.cargo/registry/cache
            ~/.cargo/git/db
            target
          key: cargo-arm64-${{ hashFiles('Cargo.lock', 'Cargo.toml') }}
          restore-keys: |
            cargo-arm64-

      - name: Install build tools
        run: pip install cargo-lambda 'aws-sam-cli>=1.165.0'

      - name: Build
        run: sam build
```

The `restore-keys` entry lets a run start from the most recent cache when the key doesn't match exactly, so that a dependency change reuses the crates that didn't change instead of compiling everything again.