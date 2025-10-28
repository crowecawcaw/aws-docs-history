# Troubleshoot common setup issues

Explore common troubleshooting issues.

## Could not find executable named 'groff'

When using the AWS CLI, you might encounter the following error: `Could not find
 executable named 'groff'`.

If using a Mac, you can resolve this issue with the following command:

```
brew install groff
```

On a Linux machine, use the following commands:

```
sudo apt-get update -y
sudo apt-get install groff -y
```

## Command not found: jq

When creating your AuthZ permission policy JSON file, you might encounter the following
error: `jq: command not found`.

If using a Mac, you can resolve this issue with the following command:

```
brew install jq
```

On a Linux machine, use the following commands:

```
sudo apt-get update -y
sudo apt-get install jq -y
```

## AWS MLflow plugin installation speeds

Installing the AWS MLflow plugin can take several minutes when using a Mac Python
environment.

## UnsupportedModelRegistryStoreURIException

If you see the `UnsupportedModelRegistryStoreURIException`, do the
following:

1. Restart your Jupyter notebook Kernel.
2. Reinstall the AWS MLflow plugin:

```
!pip install --force-reinstall sagemaker-mlflow
```
