# Logging

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

When you create your virtual nodes and virtual gateways, you have the option to
configure Envoy access logs. In the console, this is in the **Logging**
section of the virtual node and virtual gateway create or edit workflows.

![Logging configuration interface showing HTTP access logs path field with example path.](images/logging.png)
The preceding image shows a logging path of `/dev/stdout` for Envoy
access logs.

For `format`, specify **one** of two possible
formats, `json`
_or_
`text`, and the pattern. `json` takes key pairs and transforms
them into JSON struct before passing them to Envoy.

The following code block shows the JSON representation that you can use in the
AWS CLI.

```
      "logging": {
         "accessLog": {
            "file": {
               "path": "`/dev/stdout`",
                "format" : {
                    // Exactly one of json or text should be specified
                    "json": [ // json will be implemented with key pairs
                        {
                            "key": "string",
                            "value": "string"
                        }
                    ]
                    "text": "string" //e.g. "%LOCAL_REPLY_BODY%:%RESPONSE_CODE%:path=%REQ(:path)%\n"
                }
            }
         }
      }
```

###### Important

Make sure to check that your input pattern is valid for Envoy, or Envoy will
reject the update and store the latest changes in the `error
 state`.

When you send Envoy access logs to `/dev/stdout`, they are mixed in
with the Envoy container logs. You can export them to a log storage and processing
service like CloudWatch Logs using standard Docker log drivers such as `awslogs`. For
more information, see [Using the awslogs Log
Driver](../../../AmazonECS/latest/developerguide/using_awslogs.md "../../../AmazonECS/latest/developerguide/using_awslogs.md") in the Amazon ECS Developer Guide. To export only the Envoy access logs
(and ignore the other Envoy container logs), you can set the
`ENVOY_LOG_LEVEL` to `off`. You can log request without query
string by including the format string `%REQ_WITHOUT_QUERY(X?Y):Z%`. For
examples, see [`ReqWithoutQuery` Formatter](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/formatter/req_without_query/v3/req_without_query.proto "https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/formatter/req_without_query/v3/req_without_query.proto"). For more information, see
[Access logging](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/access_log.html "https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/access_log.html") in the Envoy documentation.

###### Enable access logs on Kubernetes

When using the [App Mesh Controller for
Kubernetes](mesh-k8s-integration.md "mesh-k8s-integration.md"), you can configure virtual nodes with access logging by
adding the logging configuration to the virtual node spec, as shown in the following
example.

```
---
apiVersion: appmesh.k8s.aws/v1beta2
kind: VirtualNode
metadata:
  name: `virtual-node-name`
  namespace: `namespace`
spec:
  listeners:
    - portMapping:
        port: 9080
        protocol: http
  serviceDiscovery:
    dns:
      hostName: `hostname`
  logging:
    accessLog:
      file:
        path: "/dev/stdout"
```

Your cluster must have a log forwarder to collect these logs, such as Fluentd. For
more information see, [Set up
Fluentd as a DaemonSet to send logs to CloudWatch Logs](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.md").

Envoy also writes various debugging logs from its filters to `stdout`.
These logs are useful for gaining insights into both Envoy’s communication with App Mesh
and service-to-service traffic. Your specific logging level can be configured using the
`ENVOY_LOG_LEVEL` environment variable. For example, the following text
is from an example debug log showing the cluster that Envoy matched for a particular
HTTP request.

```
[debug][router] [source/common/router/router.cc:434] [C4][S17419808847192030829] cluster 'cds_ingress_howto-http2-mesh_color_client_http_8080' match for URL '/ping'
```

## Firelens and Cloudwatch

[Firelens](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-launches-firelens-log-router-for-amazon-ecs-and-aws-fargate/#:~:text=FireLens%20is%20a%20container%20log,for%20log%20analytics%20and%20storage.&text=This%20means%20you%20can%20use,your%20own%20Fluentd%20output%20plugin. "https://aws.amazon.com/about-aws/whats-new/2019/11/aws-launches-firelens-log-router-for-amazon-ecs-and-aws-fargate/#:~:text=FireLens%20is%20a%20container%20log,for%20log%20analytics%20and%20storage.&text=This%20means%20you%20can%20use,your%20own%20Fluentd%20output%20plugin.") is a container log router you can use to collect logs for
Amazon ECS and AWS Fargate. You can find an example of using Firelens in our [AWS Samples
repository](https://github.com/aws-samples/amazon-ecs-firelens-examples "https://github.com/aws-samples/amazon-ecs-firelens-examples").

You can use CloudWatch to gather logging information as well as metrics. You can find
more information on CloudWatch in our [Exporting
metrics](metrics.md#cloudwatch "metrics.md#cloudwatch") section of the App Mesh docs.
