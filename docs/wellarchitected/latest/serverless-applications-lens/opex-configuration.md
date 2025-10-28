# Configuration

For configuration management, use environment variables for infrequent changes,
such as logging level and database connection strings. Use [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") Parameter Store (SSM) or AWS AppConfig for dynamic
configuration, such as feature toggles. Store sensitive data using AWS Secrets Manager. In
Lambda functions, lookup values by reference from these external systems (SSM, AWS AppConfig,
Secrets Manager) in the function’s global scope outside the handler to reduce API calls. You
can achieve the same goal of reducing API calls to configuration and secrets stores using
Lambda extensions which provide more fine-grained controls and the ability to re-fetch
values. Lambda extensions are powerful and flexible yet bring additional considerations and
challenges including integrations with unit tests and consistent delivery across functions
and runtimes. Lambda Powertools offer similar functionality to retrieve values from various
providers including SSM, AWS AppConfig, Secrets Manager, DynamoDB or custom stores.
