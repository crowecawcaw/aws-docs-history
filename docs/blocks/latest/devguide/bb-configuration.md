

# Configuration
<a name="bb-configuration"></a>

This section covers Blocks for application settings and secrets.

## AppSetting
<a name="bb-app-setting"></a>

A single configuration value or secret. Read and update values at runtime. Mark a setting as `secret: true` to store it as a SecureString. Values are typed and can be read in your API handlers without environment variable boilerplate.

Locally, AppSetting stores values in memory. On AWS, it provisions an SSM Parameter Store parameter (or SecureString for secrets). Best for API keys, feature flags, and any configuration that might change without a redeploy.

For more information, see [bb-app-setting on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-app-setting).