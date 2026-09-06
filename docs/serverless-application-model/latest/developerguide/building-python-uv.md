

# Building Python Lambda functions with uv in AWS SAM
<a name="building-python-uv"></a>


|  | 
| --- |
| This feature is in preview release for AWS SAM and is subject to change. | 

Use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) with uv, a fast Python package installer and resolver, to build your Python AWS Lambda functions.

**Topics**
+ [Prerequisites](#building-python-uv-prerequisites)
+ [Configuring AWS SAM to use with Python Lambda functions and uv](#building-python-uv-configure)
+ [Examples](#building-python-uv-examples)

## Prerequisites
<a name="building-python-uv-prerequisites"></a>

**Python**  
To install Python, see [Download Python](https://www.python.org/downloads/) in the *Python website*.

**uv**  
The AWS SAM CLI requires installation of [uv](https://docs.astral.sh/uv/), an extremely fast Python package installer and resolver. For installation instructions, see [Installation](https://docs.astral.sh/uv/getting-started/installation/) in the *uv documentation*.

**Opt in to AWS SAM CLI beta feature**  
Since this feature is in preview, you must opt in using one of the following methods:  

1. Use the environment variable: `SAM_CLI_BETA_PYTHON_UV=1`.

1. Add the following to your `samconfig.toml` file:

   ```
   [default.build.parameters]
   beta_features = true
   [default.sync.parameters]
   beta_features = true
   ```

1. Use the `--beta-features` option when using a supported AWS SAM CLI command. For example:

   ```
   $ sam build --beta-features
   ```

1. Choose option `y` when the AWS SAM CLI prompts you to opt in. The following is an example:

   ```
   $ sam build
   Starting Build use cache
   Build method "python-uv" is a beta feature.
   Please confirm if you would like to proceed
   You can also enable this beta feature with "sam build --beta-features". [y/N]: {{y}}
   ```

## Configuring AWS SAM to use with Python Lambda functions and uv
<a name="building-python-uv-configure"></a>

### Step 1: Configure your AWS SAM template
<a name="building-python-uv-configure-template"></a>

Configure your AWS SAM template with the following:
+ **BuildMethod** – `python-uv`.
+ **CodeUri** – path to your function code directory containing `pyproject.toml` or `requirements.txt`.
+ **Handler** – your function handler (e.g., `app.lambda_handler`).
+ **Runtime** – Python runtime version (e.g., `python3.12`).

Here is an example of a configured AWS SAM template:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./my_function
      Handler: app.lambda_handler
      Runtime: python3.12
    Metadata:
      BuildMethod: python-uv
...
```

## Examples
<a name="building-python-uv-examples"></a>

### Hello World example
<a name="building-python-uv-examples-hello"></a>

**In this example, we build a sample Hello World application using Python with uv as the package manager.**

uv can use either `pyproject.toml` or `requirements.txt` to read dependencies. If both are given, `sam build` will read from `requirements.txt` for dependencies.

The following is the structure of our Hello World application:

```
hello-python-uv
├── README.md
├── events
│   └── event.json
├── hello_world
│   ├── __init__.py
│   ├── app.py
│   └── pyproject.toml
├── samconfig.toml
└── template.yaml
```

`pyproject.toml` file:

```
[project]
name = "my-function"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31.0",
    "boto3>=1.28.0",
]
```

In our AWS SAM template, our Python function is defined as the following:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.12
      Architectures:
        - x86_64
    Metadata:
      BuildMethod: python-uv
```

Next, we run `sam build` to build our application and prepare for deployment. The AWS SAM CLI creates a `.aws-sam` directory and organizes our build artifacts there. Our function dependencies are installed using uv and stored at `.aws-sam/build/HelloWorldFunction/`.

```
hello-python-uv$ sam build
Starting Build use cache
Build method "python-uv" is a beta feature.
Please confirm if you would like to proceed
You can also enable this beta feature with "sam build --beta-features". [y/N]: {{y}}

Experimental features are enabled for this session.
Visit the docs page to learn more about the AWS Beta terms https://aws.amazon.com/service-terms/.

Cache is invalid, running build and copying resources for following functions (HelloWorldFunction)
Building codeuri: /Users/.../hello-python-uv/hello_world runtime: python3.12 metadata: {'BuildMethod': 'python-uv'} architecture: x86_64 functions: HelloWorldFunction
Running PythonUvBuilder:UvBuild
Running PythonUvBuilder:CopySource

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

**Note**  
The `python-uv` build method is configured per function in the `Metadata` section. Each function in your template can use a different build method, allowing you to mix uv-based functions with `pip`-based functions in the same AWS SAM template. If no build method is specified, `pip` is used by default.