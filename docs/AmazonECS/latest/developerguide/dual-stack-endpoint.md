# Using Amazon ECS dual-stack endpoints

Amazon ECS dual-stack endpoints support requests to Amazon ECS over Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). For a list of all Amazon ECS endpoints, see [Amazon ECS endpoints and quotas](../../../general/latest/gr/ecs-service.md "../../../general/latest/gr/ecs-service.md") in the
AWS General Reference.

When using the REST API, you directly access an Amazon ECS endpoint by using the endpoint
name (URI). Amazon ECS supports only regional dual-stack endpoint names, which means that you
must specify the region as part of the name.

Use the following naming convention for the dual-stack endpoint
names: `ecs.`region`.api.aws`.

When using the AWS Command Line Interface (AWS CLI) and AWS SDKs, you can use a parameter or a flag to
change to a dual-stack endpoint. You can also specify the dual-stack endpoint directly
as an override of the Amazon ECS endpoint in the config file.

The following sections describe how to use dual-stack endpoints from the AWS CLI, the
AWS SDKs, and the REST API.

###### Topics

- [Using dual-stack endpoints from the AWS CLI](#dual-stack-endpoints-cli "#dual-stack-endpoints-cli")
- [Using dual-stack endpoints from the AWS SDKs](#dual-stack-endpoints-sdks "#dual-stack-endpoints-sdks")
- [Using dual-stack endpoints from the REST API](#dual-stack-endpoints-examples-rest-api "#dual-stack-endpoints-examples-rest-api")

## Using dual-stack endpoints from the AWS CLI

This section provides examples of AWS CLI commands used to make requests to a dual-stack
endpoint. For more information about installing the AWS CLI or updating to the latest
version, see [Installing or updating to
the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide for Version
2_.

To use a dual-stack endpoint, you can set the configuration value
`use_dualstack_endpoint` to `true` in the `config`
file for the AWS CLI to direct all Amazon ECS requests made by the `ecs` AWS CLI
command to the dual-stack endpoint for the specified region. You can specify the region in the `config` file or in a command by using the `--region` option. For more information about
configuration files for the AWS CLI, see [Configuration and credential
file settings in the AWS CLI](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the _AWS Command Line Interface User Guide for Version
2_.

If you want to use a dual-stack endpoint for specific AWS CLI commands, you can use either of the following methods:

- You can use the dual-stack endpoint per command by setting the `--endpoint-url`
  parameter to
  `https://ecs.`aws-region`.api.aws`
  or
  `http://ecs.`aws-region`.api.aws`
  for any `ecs` command.

The following example command lists all available clusters and uses the dual-stack endpoint for the request.

```
`$` aws ecs list-clusters --endpoint-url https://ecs.`aws-region`.api.aws
```

- You can set up separate profiles in your AWS Config file. For example,
  create one profile that sets `use_dualstack_endpoint` to `true` and a profile that does not set `use_dualstack_endpoint`.
  When you run a command, specify which profile you want to use, depending upon whether or not you want to use the dual-stack endpoint.

## Using dual-stack endpoints from the AWS SDKs

This section provides examples of how to access a dual-stack endpoint by using the AWS SDKs.

AWS SDK for Java 2.x
The following example shows how to specify a dual-stack endpoint for the `us-east-1` Region using the AWS SDK for Java 2.x.

```
Region region = Region.US_EAST_1
EcsClient client = EcsClient.builder().region(region).dualstackEnabled(true).build();
```

AWS SDK for GoThe following example shows how to specify a dual-stack endpoint for the `us-east-1` Region using the AWS SDK for Go.

```
sess := session.Must(session.NewSession())
svc := ecs.New(sess, &aws.Config{
    Region: aws.String(endpoints.UsEast1RegionID),
    Endpoint: aws.String("https://ecs.us-east-1.api.aws")
})
```

For more information, see [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md") in the _AWS SDKs and Tools Reference Guide_.

## Using dual-stack endpoints from the REST API

When using the REST API, you can directly access a dual-stack endpoint by specifying it in your request. The following example uses the dual-stack endpoint to list all Amazon ECS clusters in the `us-east-1` Region.

```
POST / HTTP/1.1
Host: ecs.us-east-1.api.aws
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ListClusters
X-Amz-Date: 20150429T170621Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{}
```
