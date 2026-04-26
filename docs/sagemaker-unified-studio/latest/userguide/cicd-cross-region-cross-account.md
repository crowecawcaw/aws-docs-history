# Cross-region and cross-account deployment

Each deployment target in the manifest maps to an independent Amazon SageMaker Unified Studio project and domain. Targets can be in different AWS Regions and different AWS accounts. Provide AWS credentials for each target through IAM roles, OIDC federation, or environment variables at deploy time.
