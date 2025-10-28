# Installing Guard as an AWS Lambda function

You can install AWS CloudFormation Guard through Cargo, the Rust package manager.
_Guard as an AWS Lambda_ function (`cfn-guard-lambda`) is a
lightweight wrapper around Guard (`cfn-guard`) that can be used as a Lambda function.

## Prerequisites

Before you can install Guard as a Lambda function, you must fulfill the following
prerequisites:

- AWS Command Line Interface (AWS CLI) configured with permissions to deploy and invoke Lambda functions. For
  more information, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
- An AWS Lambda execution role in AWS Identity and Access Management (IAM). For more information, see [AWS Lambda
  execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md").
- In CentOS/RHEL environments, add the `musl-libc` package repository to your
  yum config. For more information, see [ngompa/musl-libc](https://copr.fedorainfracloud.org/coprs/ngompa/musl-libc/ "https://copr.fedorainfracloud.org/coprs/ngompa/musl-libc/").

## Install the Rust package manager

Cargo is the Rust package manager. Complete the following steps to install Rust, which
includes Cargo.

1. Run the following command from a terminal, and then follow the onscreen instructions to
   install Rust.

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

    1. (Optional) For Ubuntu environments, run the following command.



    ```
    sudo apt-get update; sudo apt install build-essential
    ```

2. Configure your `PATH` environment variable, and run the following
   command.

```
source $HOME/.cargo/env
```

## Install Guard as a Lambda function (Linux,

macOS, or Unix)

To install Guard as a Lambda function, complete the following steps.

1. From your command terminal, run the following command.

```
cargo install cfn-guard-lambda
```

    1. (Optional) To confirm the installation of Guard as a Lambda function, run the
     following command.



    ```
    cfn-guard-lambda --version
    ```

    The command returns the following output.



    ```
    cfn-guard-lambda 3.1.2
    ```

2. To install `musl` support, run the following command.

```
rustup target add x86_64-unknown-linux-musl
```

3. Build with `musl`, and then run the following command in your terminal.

```
cargo build --release --target x86_64-unknown-linux-musl
```

For a [custom
runtime](../../../lambda/latest/dg/runtimes-custom.md "../../../lambda/latest/dg/runtimes-custom.md"), AWS Lambda requires an executable with the name `bootstrap` in the
deployment package .zip file. Rename the generated `cfn-lambda` executable to
`bootstrap` and then add it to the .zip archive.

    1. For macOS environments, create your cargo configuration file in the root of the Rust
     project or in `~/.cargo/config`.



    ```
    [target.x86_64-unknown-linux-musl]
    linker = "x86_64-linux-musl-gcc"
    ```

4. Change to the `cfn-guard-lambda` root directory.

```
cd ~/.cargo/bin/cfn-guard-lambda
```

5. Run the following command in your terminal.

```
cp ./../target/x86_64-unknown-linux-musl/release/cfn-guard-lambda ./bootstrap && zip lambda.zip bootstrap && rm bootstrap
```

6. Run the following command to submit `cfn-guard`as a Lambda function to your
   account.

```
aws lambda create-function --function-name `cfnGuard` \
 --handler guard.handler \
 --zip-file fileb://./lambda.zip \
 --runtime provided \
 --role arn:aws:iam::`444455556666`:role/your_lambda_execution_role \
 --environment Variables={RUST_BACKTRACE=1} \
 --tracing-config Mode=Active
```

## To build and run Guard as a Lambda function

To invoke the submitted `cfn-guard-lambda` as a Lambda function, run the following command.

```
aws lambda invoke --function-name `cfnGuard` \
  --payload '{"data":"`input data`","rules":["`rule1`","`rule2`"]}' \
  output.json
```

## To call the Lambda function request

structure

Requests to `cfn-guard-lambda` require the following fields:

- `data` – The string version of the YAML or JSON template
- `rules` – The string version of the rule set file
