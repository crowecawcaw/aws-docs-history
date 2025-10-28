# Configuration file

The Amazon SageMaker Python SDK supports setting of default values for AWS infrastructure
primitive types. After administrators configure these defaults, they are automatically
passed when SageMaker Python SDK calls supported APIs. The arguments for the decorator
function can be put inside of configuration files. This is so that you can separate
settings that are related to the infrastructure from the code base. For more information
about parameters and arguments for the remote function and methods, see [Remote function classes and methods specification](https://sagemaker.readthedocs.io/en/stable/remote_function/sagemaker.remote_function.html "https://sagemaker.readthedocs.io/en/stable/remote_function/sagemaker.remote_function.html").

You can set infrastructure settings for the network configuration, IAM roles, Amazon S3
folder for input, output data, and tags inside the configuration file. The configuration
file can be used when invoking a function using either the @remote decorator or the
`RemoteExecutor` API.

An example configuration file that defines the dependencies, resources, and other
arguments follows. This example configuration file is used to invoke a function that is
initiated either using the @remote decorator or the RemoteExecutor API.

```
SchemaVersion: '1.0'
SageMaker:
  PythonSDK:
    Modules:
      RemoteFunction:
        Dependencies: `'path/to/requirements.txt'`
        EnableInterContainerTrafficEncryption: true
        EnvironmentVariables: {'`EnvVarKey`': '`EnvVarValue`'}
        ImageUri: '`366666666666.dkr.ecr.us-west-2.amazonaws.com/my-image:latest`'
        IncludeLocalWorkDir: true
        CustomFileFilter:
          IgnoreNamePatterns:
          - "*.ipynb"
          - "data"
        InstanceType: '`ml.m5.large`'
        JobCondaEnvironment: '`your_conda_env`'
        PreExecutionCommands:
            - 'command_1'
            - 'command_2'
        PreExecutionScript: '`path/to/script.sh`'
        RoleArn: '`arn:aws:iam::366666666666:role/MyRole`'
        S3KmsKeyId: '`yourkmskeyid`'
        S3RootUri: 's3:`//amzn-s3-demo-bucket/my-project`'
        VpcConfig:
            SecurityGroupIds:
            - '`sg123`'
            Subnets:
            - '`subnet-1234`'
        Tags: [{`'Key': 'yourTagKey', 'Value':'yourTagValue'`}]
        VolumeKmsKeyId: '`yourkmskeyid`'
```

The @remote decorator and `RemoteExecutor` will look for
`Dependencies` in the following configuration files:

- An admin-defined configuration file.
- A user-defined configuration file.
  The default locations for these configuration files depend on, and are relative to,
  your environment. The following code example returns the default location of your admin
  and user configuration files. These commands must be run in the same environment where
  you're using the SageMaker Python SDK.

```
import os
from platformdirs import site_config_dir, user_config_dir

#Prints the location of the admin config file
print(os.path.join(site_config_dir("sagemaker"), "config.yaml"))

#Prints the location of the user config file
print(os.path.join(user_config_dir("sagemaker"), "config.yaml"))
```

You can override the default locations of these files by setting the
`SAGEMAKER_ADMIN_CONFIG_OVERRIDE` and
`SAGEMAKER_USER_CONFIG_OVERRIDE` environment variables for the
admin-defined and user-defined configuration file paths, respectively.

If a key exists in both the admin-defined and user-defined configuration files, the
value in the user-defined file will be used.
