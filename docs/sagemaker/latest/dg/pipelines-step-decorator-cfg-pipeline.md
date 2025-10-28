# Configure your pipeline

You are advised to use the SageMaker AI config file to set the
defaults for the pipeline. For information about the SageMaker AI configuration file, see
[Configuring
and using defaults with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/overview.html#configuring-and-using-defaults-with-the-sagemaker-python-sdk "https://sagemaker.readthedocs.io/en/stable/overview.html#configuring-and-using-defaults-with-the-sagemaker-python-sdk").
Any configuration added to the config file applies to all
steps in the pipeline. If you want to override options for any of the steps, provide
new values in the `@step` decorator arguments. The following topic
describes how to set up a config file.

The `@step` decorator's configuration in the config file is identical to
the `@remote` decorator's configuration.
To set up the pipeline role ARN and pipeline tags in the config file,
use the `Pipeline` section shown in the following snippet:

```
SchemaVersion: '1.0'
SageMaker:
  Pipeline:
    RoleArn: 'arn:aws:iam::555555555555:role/IMRole'
    Tags:
    - Key: 'tag_key'
      Value: 'tag_value'
```

For most of the defaults you can set in the configuration file you can also
override by passing new values to the `@step` decorator. For example,
you can override the instance type set in the config file for your
preprocessing step, as shown in the following example:

```
@step(instance_type="`ml.m5.large`")
def preprocess(raw_data):
    df = pandas.read_csv(raw_data)
    ...
    return procesed_dataframe
```

A few arguments are not part of the `@step` decorator parameters
list—these can be configured for the entire pipeline only
through the SageMaker AI configuration file. They are listed as follows:

- `sagemaker_session` (`sagemaker.session.Session`): The
  underlying SageMaker AI session to which SageMaker AI delegates service calls.
  If unspecified, a session is created using a default configuration as follows:

```
SageMaker:
  PythonSDK:
    Modules:
      Session:
        DefaultS3Bucket: 'default_s3_bucket'
        DefaultS3ObjectKeyPrefix: 'key_prefix'
```

- `custom_file_filter` (`CustomFileFilter)`: A
  `CustomFileFilter`
  object that specifies the local directories and files to include in
  the pipeline step. If unspecified, this value defaults to `None`. For
  `custom_file_filter` to take effect,
  you must set `IncludeLocalWorkdir`
  to `True`. The following example shows a configuration that ignores
  all notebook files, and files and directories named `data`.

```
SchemaVersion: '1.0'
SageMaker:
  PythonSDK:
    Modules:
      RemoteFunction:
        IncludeLocalWorkDir: true
        CustomFileFilter:
          IgnoreNamePatterns: # files or directories to ignore
          - "*.ipynb" # all notebook files
          - "data" # folder or file named "data"
```

For more details about how to use `IncludeLocalWorkdir`
with `CustomFileFilter`, see [Using modular code with the @remote
decorator](train-remote-decorator-modular.md "train-remote-decorator-modular.md").

- `s3_root_uri (str)`: The root Amazon S3 folder to which SageMaker AI uploads
  the code archives and data. If unspecified, the default SageMaker AI bucket is
  used.
- `s3_kms_key (str)`: The key used to encrypt the input and output
  data. You can only configure this argument in the SageMaker AI config file and the argument applies to
  all steps defined in the pipeline. If unspecified, the value defaults to `None`.
  See the following snippet for an example S3 KMS key configuration:

```
SchemaVersion: '1.0'
SageMaker:
  PythonSDK:
    Modules:
      RemoteFunction:
        S3KmsKeyId: 's3kmskeyid'
        S3RootUri: 's3://amzn-s3-demo-bucket/my-project
```
