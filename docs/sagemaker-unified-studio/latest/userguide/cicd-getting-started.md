# Getting started

The CLI source code, example manifests, and documentation are available in the [GitHub repository](https://github.com/aws/CICD-for-SageMakerUnifiedStudio "https://github.com/aws/CICD-for-SageMakerUnifiedStudio") on the GitHub website.

## Install the CLI

Install the CLI using pip:

```
pip install aws-smus-cicd-cli
```

Verify the installation:

```
aws-smus-cicd-cli --version
```

## Create a manifest

Clone the repository and start from an example manifest for your application pattern:

```
git clone https://github.com/aws/CICD-for-SageMakerUnifiedStudio.git
cp CICD-for-SageMakerUnifiedStudio/examples/data-notebooks/manifest.yaml manifest.yaml
```

Available example patterns:

- **Analytics** — Glue ETL + QuickSight dashboards
- **Data notebooks** — Jupyter notebook workflows
- **ML training** — SageMaker AI training jobs
- **ML deployment** — Model endpoints and inference
- **GenAI** — Bedrock agent applications

Edit the manifest to specify your resources, source locations, and stage-specific configurations.

Alternatively, generate a manifest from an existing project:

```
aws-smus-cicd-cli create --domain-id <domain-id> --dev-project-id <project-id>
```

## Validate your configuration

Before deploying, you can preview what will happen without making changes:

```
# Validate permissions and connections
aws-smus-cicd-cli describe --manifest manifest.yaml --connect

# Preview deployment without applying changes
aws-smus-cicd-cli deploy --targets test --manifest manifest.yaml --dry-run
```

## Deploy

```
aws-smus-cicd-cli deploy --targets test --manifest manifest.yaml
```

## Run post-deployment validation

```
aws-smus-cicd-cli test --manifest manifest.yaml --targets test
```
