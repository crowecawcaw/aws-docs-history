AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Using Task Runner with a Proxy

If you are using a proxy host, you can either specify its [configuration](dp-taskrunner-config-options.md "dp-taskrunner-config-options.md") when
invoking Task Runner or set the environment variable, HTTPS_PROXY. The environment
variable used with Task Runner accepts the same configuration used for the [AWS Command Line Interface](../../../cli/latest/userguide/cli-http-proxy.md "../../../cli/latest/userguide/cli-http-proxy.md").
