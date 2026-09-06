

# Troubleshoot common setup issues
<a name="mlflow-troubleshooting"></a>

Explore common troubleshooting issues.

## Could not find executable named 'groff'
<a name="mlflow-troubleshooting-groff"></a>

When using the AWS CLI, you might encounter the following error: `Could not find executable named 'groff'`.

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
<a name="mlflow-troubleshooting-jq"></a>

When creating your AuthZ permission policy JSON file, you might encounter the following error: `jq: command not found`.

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
<a name="mlflow-troubleshooting-speeds"></a>

Installing the AWS MLflow plugin can take several minutes when using a Mac Python environment.

## UnsupportedModelRegistryStoreURIException
<a name="mlflow-troubleshooting-uri-exception"></a>

If you see the `UnsupportedModelRegistryStoreURIException`, do the following:

1. Restart your Jupyter notebook Kernel.

1. Reinstall the AWS MLflow plugin:

   ```
   !pip install --force-reinstall sagemaker-mlflow
   ```

## Unsupported MLflow features
<a name="mlflow-troubleshooting-unsupported-features"></a>

Some features available in open source MLflow are not supported in Amazon SageMaker AI managed MLflow.

The following features are currently not supported:
+ **[MLflow AI Gateway](https://mlflow.org/docs/latest/genai/governance/ai-gateway/)** – The MLflow AI Gateway for managing connections to LLM providers is not available.
+ **[LLM Judges and Scorers](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/)** – Built-in judges and custom judges are not supported. Code-based scorers continue to work as expected.
+ **[Prompt Optimization](https://mlflow.org/docs/latest/genai/prompt-registry/optimize-prompts/)** – Automatic prompt optimization is not available.
+ **[OpenTelemetry Integration](https://mlflow.org/docs/latest/genai/tracing/opentelemetry/)** – The OTEL-compatible traces ingestion endpoint is not available.

If you attempt to use these features, you may encounter missing UI elements or unexpected errors. This is expected behavior in the Amazon SageMaker AI managed environment.