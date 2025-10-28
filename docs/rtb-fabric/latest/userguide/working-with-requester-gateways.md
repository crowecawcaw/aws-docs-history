# Requester gateways

Requester gateways are RTB Fabric infrastructure components that serve as connection points for customer applications. Requester gateways receive requests from requester applications and forward them through links to responder gateways. Gateways operate colocated with your VPC and provide routing, load balancing, and processing capabilities. You maintain full control over your bidding logic, data, and auction decisions, while RTB Fabric provides the secure infrastructure for connectivity. Requester gateways are typically used by supply-side platforms (SSPs).

###### Topics

- [Creating a requester gateway](#creating-requester-gateway "#creating-requester-gateway")
- [Searching for requester gateways](#searching-requester-gateways "#searching-requester-gateways")
- [Viewing associated links](#viewing-associated-links "#viewing-associated-links")
- [Deleting requester gateways](#deleting-applications "#deleting-applications")

## Creating a requester gateway

Create a new requester gateway that can forward bid requests for ad impressions and receive responses.

###### Note

You are responsible for the data you send through RTB Fabric, including ensuring that personally identifiable information (PII) is handled according to your privacy requirements and applicable regulations.

###### To create a requester gateway

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric "https://console.aws.amazon.com/rtbfabric").
2. In the navigation pane, choose **Requester gateway**.
3. Choose **Create requester gateway**.
4. In the **Requester gateway information** section, for **Requester gateway description**, enter a description of the gateway's purpose. The description can have up to 255 characters.
5. In the **VPC configuration** section, configure the following settings:
   1. For **VPC ID**, enter the ID of the virtual private cloud (VPC) where you want to connect the requester gateway. The VPC ID must start with "vpc-" followed by either 8 or 17 hexadecimal characters in lowercase. For example: vpc-0123abc4567def890.
   2. For **Subnet ID**, enter the subnet IDs where you want to connect your gateway. Enter up to 5 subnet IDs (format: subnet-0123abc4567def89a), separated by commas. Must be from the specified VPC. These subnets should match your core workload deployment subnets or be secondary CIDR subnets within the same Availability Zones.
   3. For **Security group ID**, enter the IDs of 1-5 security groups, separated by commas. We recommend you create new security groups for your gateway for security.

6. Choose **Create gateway**.
7. Your new requester gateway appears in the gateways list with an **Activating** status. The gateway status will remain **Activating** for 2-5 minutes until creation is complete.

Use the following command to create a requester gateway using the AWS Command Line Interface (AWS CLI).

```
# Create a requester gateway with required parameters
aws rtbfabric create-requester-gateway \
    --description "My RTB requester gateway" \
    --vpc-id vpc-12345678 \
    --subnet-ids subnet-abc12345 subnet-def67890 \
    --security-group-ids sg-12345678 \
    --client-token "unique-client-token-123"

# Create with optional tags
aws rtbfabric create-requester-gateway \
    --description "My RTB requester gateway" \
    --vpc-id vpc-12345678 \
    --subnet-ids subnet-abc12345 subnet-def67890 \
    --security-group-ids sg-12345678 \
    --client-token "unique-client-token-123" \
    --tags Environment=Production Team=RTB
```

### Updating gateway description

You can update the gateway description using the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](../api.md "../api.md").

## Searching for requester gateways

Use the search functionality in the console to locate specific gateways associated with your account. The applications table displays key information including application ID, status, name, creation date, and associated resources.

###### To search for requester gateways

1. In the **Find requester gateways** search box, enter your search criteria.
2. You can search across requester gateway ID, status, name, or creation date.
3. The table automatically filters to show matching applications as you type.
4. If no gateways exist, the console displays **No requester gateways** with an option to create a gateway.

Use the following command to get details for a specific requester gateway using the AWS Command Line Interface (AWS CLI).

```
# Get details for a specific requester gateway
aws rtbfabric get-requester-gateway --gateway-id "rtb-gw-req-12345"
```

## Viewing associated links

Each requester gateway can have associated links that connect it to responder applications. You can view these links directly from the applications table and see detailed connection information.

###### To view associated links for an application

1. In the **Requester gateways** table, locate the application whose links you want to view.
2. Select the radio button for the application row.
3. The application details expand below the table, showing the application ID with a collapsible section.
4. In the expanded section, view the **Links associated with this requester gateway** section, which displays the total number of links in parentheses.
5. Review the links table, which shows detailed information for each associated link including link ID, status, creation date, requester application name, and responder application ID.

The links table includes the following columns:

- **Link ID** – Unique identifier for the link.
- **Link status** – Current operational status of the link.
- **Link creation date (UTC)** – When the link was created.
- **Requester gateway name** – Name of the requesting application.
- **Responder Gateway ID** – ID of the responding application.

Use the following command to list all links associated with a specific requester gateway using the AWS Command Line Interface (AWS CLI).

```
# List all links associated with a gateway
aws rtbfabric list-links --gateway-id "rtb-gw-dsj34i23nsllka"

# List links with pagination
aws rtbfabric list-links --gateway-id "rtb-gw-dsj34i23nsllka" --max-results 10 --next-token "token"
```

## Deleting requester gateways

When you no longer need a requester gateway, you can delete it from your environment. This action is irreversible and will terminate all bidding activities associated with the application.

We recommend deleting unused requester gateways to optimize resource usage and costs. AWS may delete unused gateways after 30 days of inactivity to manage infrastructure resources.

###### Warning

Deleting a requester gateway is permanent and cannot be undone. Check your gateway metrics to verify there is no active traffic before proceeding with deletion.

###### To delete a requester gateway

1. On the **Requester gateways** page, select the radio button next to the application you want to delete.
2. Choose **Delete** from the action buttons at the top of the page.
3. If the gateway has associated links, a dialog appears with the message "To delete this application, you must first delete all of its associated links. You can delete links on the Links table." Follow the provided instructions to delete associated links first, then return to delete the application. For more information, see [Deleting gateway links](links.md#deleting-rtb-links "links.md#deleting-rtb-links").
4. If the application has no associated links, a confirmation dialog appears. Verify that you want to delete the selected application.
5. Choose **Delete** to confirm the deletion.

Use the following command to delete a requester gateway using the AWS Command Line Interface (AWS CLI).

```
# Delete a requester gateway
aws rtbfabric delete-requester-gateway --gateway-id "rtb-gw-dsj34i23nsllka"
```
