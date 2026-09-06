

# Resource Limit Configuration
<a name="configure-resource-limits"></a>

Amazon MQ for RabbitMQ supports configuring broker resource limits from RabbitMQ 4 onwards. When you create a broker, Amazon MQ automatically applies default values to these resource limits. These defaults act as guardrails to protect your broker availability while accommodating common customer usage patterns. You can customize your broker behavior by changing the limit configuration values to better match your specific workload requirements. For more details about default and maximum allowed values, see [Amazon MQ for RabbitMQ sizing guidelines](rabbitmq-sizing-guidelines.md).

## Resource names and configuration keys
<a name="resource-limit-configuration-keys"></a>


| Resource Name | Configuration Key | 
| --- | --- | 
| Connection | connection\_max | 
| Channel | channel\_max\_per\_node | 
| Queue | cluster\_queue\_limit | 
| Vhost | vhost\_max | 
| Shovel | runtime\_parameters.limits.shovel | 
| Exchange | cluster\_exchange\_limit | 
| Consumer per channel | consumer\_max\_per\_channel | 
| Maximum message size | max\_message\_size | 

## How to override resource limits
<a name="override-resource-limits"></a>

You can override resource limits using the Amazon MQ API and Amazon MQ console.

The following example shows how to override the queue count default limit using the AWS CLI:

```
aws mq update-configuration --configuration-id <config-id> --data "$(echo "cluster_queue_limit=500" | base64 --wrap=0)"
```

A successful invocation creates a configuration revision. You must associate the configuration to your RabbitMQ broker and reboot the broker to apply the override. For more details see [RabbitMQ Broker Configurations](rabbitmq-broker-configuration-parameters.md) 

## Instance specific section support in configuration
<a name="section-support-configuration-data"></a>

With RabbitMQ 4, Amazon MQ supports sections in configuration data. Sections let you define instance-specific resource limits within a single configuration. Each section corresponds to a specific instance type and deployment mode combination. When you associate the configuration with a broker, Amazon MQ automatically applies the matching section for the broker's instance type and deployment mode.

**Important**  
Section support is only available on RabbitMQ 4. If you attempt to apply a configuration that contains sections to a RabbitMQ 3 broker, the API returns a `BadRequestException`.

**Section syntax**

Sections are delimited by double curly braces with the following format:

```
{{<host-instance-family>.<size>.<mode>}}
```

The `mode` value indicates the deployment mode:
+ `1` – Single-instance broker
+ `3` – Cluster broker

Any other mode value is invalid and the API returns an error.

The following example shows configuration data with sections for two different instance types:

```
connection_max = 1000

{{m7g.large.3}}
connection_max = 2000
{{m7g.large.3}}

{{m7g.xlarge.3}}
connection_max = 4000
{{m7g.xlarge.3}}
```

**Allowed configuration keys in sections**

Only the following resource limit configuration keys are supported inside a section. Adding any other configuration key inside a section results in an API error.
+ `max_message_size`
+ `channel_max_per_node`
+ `connection_max`
+ `cluster_queue_limit`
+ `vhost_max`
+ `consumer_max_per_channel`
+ `runtime_parameters.limits.shovel`
+ `cluster_exchange_limit`

**Section precedence rules**

When a configuration key appears in both the generic (top-level) section and an instance-specific section, the value that appears later in the configuration data takes precedence. For example, applying the following configuration to an `m7g.large` cluster broker sets `connection_max` to `2000`:

```
connection_max = 1000

{{m7g.large.3}}
connection_max = 2000
{{m7g.large.3}}
```

Reversing the order sets `connection_max` to `1000`, because the generic value comes last:

```
{{m7g.large.3}}
connection_max = 2000
{{m7g.large.3}}

connection_max = 1000
```

**Note**  
If the configuration data does not define values for a particular instance type, Amazon MQ applies the default values.

**Examples**

The following examples show how to create a configuration with sections and associate it with a broker using the AWS CLI.

*To update a configuration with sections*

Run the following command to update a configuration with instance-specific resource limits for multiple instance types:

```
aws mq update-configuration \
    --configuration-id <config-id> \
    --data "$(echo -e "connection_max = 1000\nchannel_max_per_node = 64\n\n{{m7g.large.3}}\nconnection_max = 2000\nchannel_max_per_node = 128\n{{m7g.large.3}}\n\n{{m7g.xlarge.3}}\nconnection_max = 4000\nchannel_max_per_node = 256\n{{m7g.xlarge.3}}" | base64 --wrap=0)"
```

This configuration defines the following values:
+ Generic defaults: `connection_max = 1000` and `channel_max_per_node = 64`
+ `m7g.large` cluster brokers: `connection_max = 2000` and `channel_max_per_node = 128`
+ `m7g.xlarge` cluster brokers: `connection_max = 4000` and `channel_max_per_node = 256`

*To associate the configuration with a broker*

After you update the configuration, associate it with your broker and reboot the broker to apply the changes. Run the following command:

```
aws mq update-broker \
    --broker-id <broker-id> \
    --configuration id=<config-id>,revision=<revision-number>
```

## Resource limit override errors
<a name="resource-limit-override-errors"></a>

Associating or creating a broker with configuration values outside the supported range results in an error response similar to the following:

```
Configuration Revision N for configuration:cluster_queue_limit has limit: of value: 100000000 larger than maximum allowed limit:5000
```

For default values and maximum supported ranges by instance type and deployment mode, see [Default resource limits](rabbitmq-resource-limits-configuration.md) and [Amazon MQ for RabbitMQ maximum resource limit](rabbitmq-resource-hard-limit.md).