# Resource management

The AgentCore Browser provides two types of resources:

System ARNs

System ARNs are default resources pre-created for ease of use. These ARNs have
default configuration with the most restrictive options and are available for all
regions where Amazon Bedrock AgentCore is available.

| Field       | Value                                                          |
| ----------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID          | aws.browser.v1                                                 |
| ARN         | arn:aws:bedrock-agentcore:us-east-1:aws:browser/aws.browser.v1 |
| Name        | Amazon Bedrock AgentCore Browser Tool                          |
| Description | AWS built-in browser for secure web browsing                   |
| Status      | READY                                                          | Custom ARNs Custom ARNs allow you to configure a browser tool with your own settings. You can choose the public network setting, recording configuration, security settings, and permissions through an IAM runtime role that defines what AWS resources the browser tool can access. ## Network settings The AgentCore Browser supports the public network mode. This mode allows the tool to access public internet resources. This option enables integration with external APIs and services. |
