# CI/CD for Amazon SageMaker Unified Studio

The Amazon SageMaker Unified Studio CI/CD CLI (`aws-smus-cicd-cli`) is an open-source command line tool that deploys multi-service data and AI applications across development, test, and production environments from a single manifest file. The CLI is available at no additional cost — you pay only for the underlying AWS resources provisioned during deployment.

**GitHub repository:** [github.com/aws/CICD-for-SageMakerUnifiedStudio](https://github.com/aws/CICD-for-SageMakerUnifiedStudio "https://github.com/aws/CICD-for-SageMakerUnifiedStudio") on the GitHub website

When you build data and AI applications in Amazon SageMaker Unified Studio, your applications often combine multiple AWS services into a single workflow. Promoting these applications from development to test and production requires substituting service-specific configurations for each stage and provisioning resources in the correct order. The CI/CD CLI automates this process.

The CLI uses a declarative YAML manifest (`manifest.yaml`) that defines:

- **Application resources** — Glue ETL jobs, Athena queries, MWAA workflows, Bedrock agents, QuickSight dashboards, and catalog assets
- **Pipeline stages** — Each stage maps to an independent Amazon SageMaker Unified Studio project, providing full isolation between environments
- **Stage-specific configurations** — S3 bucket paths, IAM role ARNs, account IDs, and connection strings that are substituted automatically at deploy time
