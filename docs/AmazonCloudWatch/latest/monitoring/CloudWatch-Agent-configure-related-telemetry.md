# Configure CloudWatch agent
 service and environment names for related entities

The CloudWatch agent can send metrics and logs with entity data to support the [Explore related pane](ExploreRelated.md "ExploreRelated.md") in the CloudWatch console. The service
 name or environment name can be configured by the [CloudWatch Agent JSON
 configuration](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md").

###### Note

The agent configuration may be overridden. For details about how the agent decides
 what data to send for related entities, see [Using the CloudWatch agent with related
 telemetry](CloudWatch-Agent-RelatedEntities.md "CloudWatch-Agent-RelatedEntities.md").

For metrics, it can be configured at the agent, metrics, or plugin level. For logs it
 can be configured at the agent, logs, or file level. The most specific configuration is
 always used. For example if the configuration exists at the agent level and metrics level,
 then metrics will use the metric configuration, and anything else (logs) will use the
 agent configuration. The following example shows different ways to configure the service
 name and environment name.


```
{
  "agent": {
    "service.name": "agent-level-service",
    "deployment.environment": "agent-level-environment"
  },
  
  "metrics": {
    "service.name": "metric-level-service",
     "deployment.environment": "metric-level-environment",
     
    "metrics_collected": {
      "statsd": {
        "service.name": "statsd-level-service",
        "deployment.environment": "statsd-level-environment",
      },
      "collectd": {
        "service.name": "collectdd-level-service",
        "deployment.environment": "collectd-level-environment",
      }
    }
    
  },
  
  "logs": {
    "service.name": "log-level-service",
    "deployment.environment": "log-level-environment",
    
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log",
            "log_group_name": "amazon-cloudwatch-agent.log",
            "log_stream_name": "amazon-cloudwatch-agent.log",
            
            "service.name": "file-level-service",
            "deployment.environment": "file-level-environment"
          }
        ]
      }
    }
    
  }
}
```
