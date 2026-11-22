

# Update integrations (3p apps) across Linked AWS regions

**Warning**  
Connect Customer Global Resiliency instances created after November 5, 2026, will support replication of native integrations (3p app) and their security profile permissions. To enable this for ACGR instances created before November 5, 2026, contact [AWS Support](https://console.aws.amazon.com/support/home).

Connect Customer Global Resiliency replicates integrations, including Standard applications, services, and Model Context Protocol (MCP) servers, across your linked AWS Regions. To replicate an integration, associate it with your Connect Customer Global Resiliency instance.

This topic explains how changes to integrations replicate. It also explains what you set up in the replica Region for Standard applications, services, and MCP servers.

For information about what else is replicated, see [Create a replica of your existing Connect Customer instance](create-replica-connect-instance.md). For information about integrations, see [Integrate third-party applications in the agent workspace](3p-apps.md).

**Topics**
+ [Understanding how integrations replicate](#update-integrations-how-changes-replicate)
+ [Setting up Standard applications and services in the replica Region](#update-integrations-standard-replica)
+ [Setting up MCP servers in the replica Region](#update-integrations-mcp-replica)

## Understanding how integrations replicate
<a name="update-integrations-how-changes-replicate"></a>

Keep the following in mind when you work with integrations in replicated instances:
+ **Associate an integration to replicate it** – To replicate an integration, associate it with your instance. In the Connect Customer console, choose the instance under **Instance association**. Or use the [CreateIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html) API. In the request, set `IntegrationType` to `APPLICATION`. The replicated integration has the same ID, namespace, and tags.
+ **Deleting an integration isn't replicated** – When you delete an integration in one Region, it isn't deleted in the other Region.
+ **The access URL is copied only once** – Connect Customer Global Resiliency copies the access URL during the initial replication. After that, each Region keeps its own access URL, so the integrations in each Region can point to different URLs.

## Setting up Standard applications and services in the replica Region
<a name="update-integrations-standard-replica"></a>

Standard applications and services don't need any additional setup to replicate. After replication, the integration in the replica instance uses the same access URL as the integration in the source instance.

If agents in the replica Region should load the integration from an endpoint that's hosted in that Region, update the access URL in the replica instance. After the initial replication, each Region keeps its own access URL, so you can configure each one independently.

Use the following procedure when agents in the replica Region need to load the integration from an endpoint that's hosted in that Region. This procedure is part of setting up Standard applications and services in the replica Region after replication completes.

**To update the access URL in the replica Region (console)**

1. Open the Connect Customer [console](https://console.aws.amazon.com/connect/) (https://console.aws.amazon.com/connect/), and switch to the AWS Region of your replica instance.

1. In the navigation pane, choose **Integrations**.

1. In the list of integrations, select the replicated integration, and then edit it.

1. For **Access URL**, enter the endpoint that's hosted in the replica Region.

1. Save your changes.

If you can't save your changes, make sure that you have the required IAM permissions. For more information, see [Required IAM permissions](3p-apps.md#onboard-3p-apps-requirements).

To update the access URL by using the AWS CLI, call [UpdateApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateApplication.html) in the Region of your replica instance.

The following AWS CLI command updates the access URL:

```bash
aws appintegrations update-application \
    --region {{replica-region}} \
    --arn {{application-arn}} \
    --application-source-config '{
        "ExternalUrlConfig": {
            "AccessUrl": "https://{{app.example.org}}"
        }
    }'
```

Replace the following placeholder values:
+ {{replica-region}} – The Region of your replica instance.
+ {{application-arn}} – The ARN of the integration.
+ {{app.example.org}} – The endpoint that's hosted in the replica Region.

## Setting up MCP servers in the replica Region
<a name="update-integrations-mcp-replica"></a>

An MCP server connects to Connect Customer through an Amazon Bedrock AgentCore (AgentCore) gateway. Connect Customer Global Resiliency doesn't replicate AgentCore gateways.

After replication, you must point the MCP server in the replica region to AgentCore gateway in the same region. For instructions on setting up an MCP server, see [Integrate an MCP server with Connect Customer](3p-apps-mcp-server.md).

**Important**  
Until you point the replicated MCP server to a gateway in the replica Region, you can update only its tags in the replica instance.

The following procedure shows you how to create an AgentCore gateway in the replica Region and point the replicated MCP server to it. Use the same target names as the gateway in your source Region. Tool names include the target name, so matching target names keeps tool names the same in both Regions.

**To set up an MCP server in the replica Region (console or AWS CLI)**

1. Open the AgentCore console in the AWS Region of your replica instance, and create a gateway with the following settings.
   + For the discovery URL, use the URL of your replica instance, not your source instance. For example: `https://{{my-replica-instance}}.my.connect.aws/.well-known/openid-configuration`.
   + Configure **Allowed audiences** the same way that you configured the gateway in your source Region.
   + Add the same targets, with the same target names, as the gateway in your source Region.

1. Point the replicated MCP server to the new gateway. Do one of the following:
   + Open the Connect Customer [console](https://console.aws.amazon.com/connect/) (https://console.aws.amazon.com/connect/) in the Region of your replica instance, choose **Integrations**, select the MCP server, and edit it. Under **Integration details**, select the gateway that you created in the replica Region, and save your changes.
   + Call UpdateApplication in the Region of your replica instance. Set the access URL to the URL of the new gateway. The following AWS CLI command points the MCP server to the new gateway. Replace the placeholder values as described after the command.

     ```bash
     aws appintegrations update-application \
         --region {{replica-region}} \
         --arn {{application-arn}} \
         --application-source-config '{
             "ExternalUrlConfig": {
                 "AccessUrl": "https://{{gateway-id}}.gateway.bedrock-agentcore.{{replica-region}}.amazonaws.com/mcp"
             }
         }'
     ```

     Replace the following placeholder values:
     + {{replica-region}} – The Region of your replica instance.
     + {{application-arn}} – The ARN of the integration.
     + {{gateway-id}} – The ID of the gateway that you created.

1. In the Connect Customer console in the replica Region, confirm that the gateway is reachable and that its tools are available.

If the gateway isn't reachable or its tools aren't available, check the discovery URL, the **Allowed audiences** setting, and the targets that you configured in step 1.