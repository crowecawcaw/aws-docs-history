

# Requester gateways
<a name="working-with-requester-gateways"></a>

Requester gateways are RTB Fabric infrastructure components that serve as connection points for customer gateways. Requester gateways receive requests from requester gateways and forward them through links to responder gateways. Gateways operate colocated with your VPC and provide routing, load balancing, and processing capabilities. You maintain full control over your bidding logic, data, and auction decisions, while RTB Fabric provides the secure infrastructure for connectivity. Requester gateways are typically used by supply-side platforms (SSPs).

**Topics**
+ [Creating a requester gateway](#creating-requester-gateway)
+ [Searching for requester gateways](#searching-requester-gateways)
+ [Viewing associated links](#viewing-associated-links)
+ [Deleting requester gateways](#deleting-gateways)

## Creating a requester gateway
<a name="creating-requester-gateway"></a>

Create a new requester gateway that can forward bid requests for ad impressions and receive responses.

**Note**  
You are responsible for the data you send through RTB Fabric, including ensuring that personally identifiable information (PII) is handled according to your privacy requirements and applicable regulations.

**To create a requester gateway**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric).

1. In the navigation pane, choose **Requester gateway**.

1. Choose **Create requester gateway**.

1. In the **Requester gateway information** section, for **Requester gateway description**, enter a description of the gateway's purpose. The description can have up to 255 characters.

1. In the **VPC configuration** section, configure the following settings:

   1. For **VPC ID**, enter the ID of the virtual private cloud (VPC) where you want to connect the requester gateway. The VPC ID must start with "vpc-" followed by either 8 or 17 hexadecimal characters in lowercase. For example: vpc-0123abc4567def890.

   1. For **Subnet ID**, enter the subnet IDs where you want to connect your gateway. Enter up to 5 subnet IDs (format: subnet-0123abc4567def89a), separated by commas. Must be from the specified VPC. These subnets should match your core workload deployment subnets or be secondary CIDR subnets within the same Availability Zones.

   1. For **Security group ID**, enter the IDs of 1-5 security groups, separated by commas. We recommend you create new security groups for your gateway for security.

1. Choose **Create gateway**.

1. Your new requester gateway appears in the gateways list with an **Activating** status. The gateway status will remain **Activating** for 20-40 minutes until creation is complete.

### AWS CLI
<a name="create-requester-app-cli"></a>

Use the following command to create a requester gateway using the AWS Command Line Interface (AWS CLI).

**Create a requester gateway with required parameters**

```
$ aws rtbfabric create-requester-gateway \
--description {{"My RTB requester gateway"}} \
--vpc-id {{vpc-12345678}} \
--subnet-ids {{subnet-abc12345 subnet-def67890}} \
--security-group-ids {{sg-12345678}} \
--client-token {{"unique-client-token-123"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create with optional tags**

```
$ aws rtbfabric create-requester-gateway \
--description {{"My RTB requester gateway"}} \
--vpc-id {{vpc-12345678}} \
--subnet-ids {{subnet-abc12345 subnet-def67890}} \
--security-group-ids {{sg-12345678}} \
--client-token {{"unique-client-token-123"}} \
--tags {{Environment=Production Team=RTB}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

### Updating gateway description
<a name="updating-requester-gateway-description"></a>

You can update the gateway description using the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](https://docs.aws.amazon.com/rtb-fabric/latest/api/).

## Searching for requester gateways
<a name="searching-requester-gateways"></a>

Use the search functionality in the console to locate specific gateways associated with your account. The gateways table displays key information including gateway ID, status, name, creation date, and associated resources.

**To search for requester gateways**

1. In the **Find requester gateways** search box, enter your search criteria.

1. You can search across requester gateway ID, status, name, or creation date.

1. The table automatically filters to show matching gateways as you type.

1. If no gateways exist, the console displays **No requester gateways** with an option to create a gateway.

### AWS CLI
<a name="get-requester-app-cli"></a>

Use the following command to get details for a specific requester gateway using the AWS Command Line Interface (AWS CLI).

**Get details for a specific requester gateway**

```
$ aws rtbfabric get-requester-gateway \
--gateway-id {{"rtb-gw-req-12345"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Viewing associated links
<a name="viewing-associated-links"></a>

Each requester gateway can have associated links that connect it to responder gateways. You can view these links directly from the gateways table and see detailed connection information.

**To view associated links for an gateway**

1. In the **Requester gateways** table, locate the gateway whose links you want to view.

1. Select the radio button for the gateway row.

1. The gateway details expand below the table, showing the gateway ID with a collapsible section.

1. In the expanded section, view the **Links associated with this requester gateway** section, which displays the total number of links in parentheses.

1. Review the links table, which shows detailed information for each associated link including link ID, status, creation date, requester gateway name, and responder gateway ID.

The links table includes the following columns:
+ **Link ID** – Unique identifier for the link.
+ **Link status** – Current operational status of the link.
+ **Link creation date (UTC)** – When the link was created.
+ **Requester gateway name** – Name of the requesting gateway.
+ **Responder Gateway ID** – ID of the responding gateway.

### AWS CLI
<a name="get-associated-links-requester-app-cli"></a>

Use the following command to list all links associated with a specific requester gateway using the AWS Command Line Interface (AWS CLI).

**List all links associated with a gateway**

```
$ aws rtbfabric list-links \
--gateway-id {{"rtb-gw-dsj34i23nsllka"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**List links with pagination**

```
$ aws rtbfabric list-links \
--gateway-id {{"rtb-gw-dsj34i23nsllka"}} \
--max-results {{10}} \
--next-token {{"token"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Deleting requester gateways
<a name="deleting-gateways"></a>

When you no longer need a requester gateway, you can delete it from your environment. This action is irreversible and will terminate all bidding activities associated with the gateway.

We recommend deleting unused requester gateways to optimize resource usage and costs. AWS may delete unused gateways after 30 days of inactivity to manage infrastructure resources.

**Warning**  
Deleting a requester gateway is permanent and cannot be undone. Check your gateway metrics to verify there is no active traffic before proceeding with deletion.

**To delete a requester gateway**

1. On the **Requester gateways** page, select the radio button next to the gateway you want to delete.

1. Choose **Delete** from the action buttons at the top of the page.

1. If the gateway has associated links, a dialog appears with the message "To delete this gateway, you must first delete all of its associated links. You can delete links on the Links table." Follow the provided instructions to delete associated links first, then return to delete the gateway. For more information, see [Deleting links](deleting-rtb-links.md).

1. If the gateway has no associated links, a confirmation dialog appears. Verify that you want to delete the selected gateway.

1. Choose **Delete** to confirm the deletion.

### AWS CLI
<a name="delete-requester-app-cli"></a>

Use the following command to delete a requester gateway using the AWS Command Line Interface (AWS CLI).

**Delete a requester gateway**

```
$ aws rtbfabric delete-requester-gateway \
--gateway-id {{"rtb-gw-dsj34i23nsllka"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```