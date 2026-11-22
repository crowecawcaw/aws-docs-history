

# Building Python Lambda Event Functions with uv in AWS SAM

Use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) with uv, a fast Python package installer and resolver, to build your Python AWS Lambda Event Functions.

**Topics**
+ [Prerequisites](#building-python-uv-prerequisites)
+ [Configuring AWS SAM to use with Python Lambda Event Functions and uv](#building-python-uv-configure)
+ [Examples](#building-python-uv-examples)

## Prerequisites
<a name="building-python-uv-prerequisites"></a>

**Python**  
To install Python, see [Download Python](https://www.python.org/downloads/) in the *Python website*.

**uv**  
The AWS SAM CLI requires installation of [uv](https://docs.astral.sh/uv/), an extremely fast Python package installer and resolver. For installation instructions, see [Installation](https://docs.astral.sh/uv/getting-started/installation/) in the *uv documentation*.

## Configuring AWS SAM to use with Python Lambda Event Functions and uv
<a name="building-python-uv-configure"></a>

### Step 1: Configure your AWS SAM template
<a name="building-python-uv-configure-template"></a>

Configure your AWS SAM template with the following:
+ **BuildMethod** – `python-uv`.
+ **CodeUri** – path to your function code directory containing `pyproject.toml` or `requirements.txt`.
+ **Handler** – your function handler (e.g., `app.lambda_handler`).
+ **Runtime** – Python runtime version (e.g., `python3.12`).

Here is an example of a configured AWS SAM template:

```yaml
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

### Step 2: Configure build properties (optional)
<a name="building-python-uv-configure-buildproperties"></a>

For a project that uses `pyproject.toml`, the AWS SAM CLI installs your dependencies by running `uv export --locked` and then `uv pip install`. If a `uv.lock` file exists, the build uses the versions that it locks. If there's no `uv.lock` file, the build runs **uv lock** first, and the new `uv.lock` file stays in your project.

If the `uv.lock` file no longer matches `pyproject.toml`, the build fails instead of updating the lock file. Run **uv lock** to update it. Dependency groups, including the `dev` group, aren't installed by default.

To change what is installed, add the following properties under `Metadata.BuildProperties`. If you set any of these properties on a function that doesn't use `BuildMethod: python-uv`, the build fails.

**`UvGroups`**  
A list of dependency groups to include.  
*Type*: List of strings

**`UvExtras`**  
A list of optional dependencies (extras) to include. You can't use `UvExtras` together with `UvAllExtras`.  
*Type*: List of strings

**`UvAllExtras`**  
A Boolean that includes all optional dependencies (extras) when set to `true`.  
*Type*: Boolean

**`UvPrune`**  
A list of packages to leave out of the deployment package, along with any dependencies that only those packages need. Use this for packages that the Lambda runtime already includes, such as `boto3`. Your function then uses the version in the runtime instead of the version in `uv.lock`. Each name must be a package in `uv.lock`, and it can't be the project that you're building.  
*Type*: List of strings

**`UvCompileBytecode`**  
A Boolean that compiles the installed dependencies to Python bytecode (`.pyc` files) with the function's Python version when set to `true`. The AWS SAM CLI writes unchecked hash-based `.pyc` files. These files stay valid in the deployment package. The function's Python version must be available to uv on the build machine. If it isn't, the build logs a warning and skips bytecode compilation.  
If you don't set this property, a true value of the `UV_COMPILE_BYTECODE` environment variable, such as `1`, also turns it on. An explicit `false` takes precedence over the environment variable. This property also works when your dependencies are in `requirements.txt`.  
*Type*: Boolean  
*Default*: `false`

`UvGroups`, `UvExtras`, `UvAllExtras`, and `UvPrune` apply only to projects that use `pyproject.toml`. If your dependencies are in `requirements.txt`, the build fails when you set them. These four properties require AWS SAM CLI version 1.173.0 or later. `UvCompileBytecode` requires AWS SAM CLI version 1.174.0 or later.

The following example AWS SAM template configures build properties for a function:

```yaml
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./my_function
      Handler: app.lambda_handler
      Runtime: python3.12
    Metadata:
      BuildMethod: python-uv
      BuildProperties:
        UvGroups:
          - lambda
        UvPrune:
          - boto3
        UvCompileBytecode: true
```

The following settings are configured in this example:
+ `UvGroups` installs the dependencies in the `lambda` dependency group.
+ `UvPrune` removes `boto3` from the deployment package.
+ `UvCompileBytecode` compiles the installed dependencies to Python bytecode.

## Examples
<a name="building-python-uv-examples"></a>

### Hello World example
<a name="building-python-uv-examples-hello"></a>

**In this example, we build a sample Hello World application using Python with uv as the package manager.**

uv can use either `pyproject.toml` or `requirements.txt` to read dependencies. If both are present, **sam build** uses `pyproject.toml` when a `uv.lock` file is next to it or when it lists dependencies in its `[project]` table. Otherwise, **sam build** uses `requirements.txt`.

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

```yaml
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