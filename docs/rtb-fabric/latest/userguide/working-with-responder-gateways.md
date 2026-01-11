# Responder gateways

Responder gateways are RTB Fabric infrastructure components that serve as connection points for customer applications. Responder gateways receive requests from requester gateways and forward them to responder applications, then return responses through the same pathway. Gateways operate colocated with your VPC and provide routing, load balancing, and processing capabilities. You maintain complete control over your bidding algorithms, response logic, and data processing, while RTB Fabric provides the secure infrastructure for connectivity.

###### Topics

- [Creating a responder gateway](#creating-responder-gateway "#creating-responder-gateway")
- [Searching for responder gateways](#searching-responder-gateways "#searching-responder-gateways")
- [Viewing associated links](#viewing-responder-associated-links "#viewing-responder-associated-links")
- [Deleting responder gateways](#deleting-responder-applications "#deleting-responder-applications")

## Creating a responder gateway

Create a new responder gateway that can respond to bid opportunities.

###### Note

You are responsible for the data you process through RTB Fabric, including ensuring that personally identifiable information (PII) is handled according to your privacy requirements and applicable regulations.

###### To create a responder gateway

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric "https://console.aws.amazon.com/rtbfabric").
2. In the navigation pane, choose **Responder gateway**.
3. Choose **Create responder gateway**.
4. In the **Responder gateway information** section, for **Gateway description**, enter a description of the gateway's purpose. The description can have up to 255 characters.
5. In the **VPC configuration** section, configure the network settings:
   1. For **VPC ID**, enter a valid VPC ID. For example: vpc-01f345ad6524a6d7.
   2. For **Subnet ID**, enter the IDs of 1-5 subnets, separated by commas. Subnets must have at least 200 free IP addresses. These subnets should match your core workload deployment subnets or be secondary CIDR subnets within the same Availability Zones.
   3. For **Security group ID**, enter the IDs of 1-5 security groups, separated by commas. We recommend you create new security groups for your gateways for security.

6. In the **Responder endpoint configuration** section, configure the endpoint where your gateway receives network traffic:
   1. For **DNS name**, enter a fully qualified domain name (FQDN) where you want your gateway to be accessed. Valid characters are a-z, A-Z, 0-9, periods (.), and hyphens (-). Maximum length is 253 characters.
   2. (Optional) For **CA certificate chain**, enter the CA certificate chain for your domain. Include the intermediate and root certificates in PEM format. Maximum size: 2048 characters.
   3. For **Network port number**, enter the network port number where your gateway will listen for incoming traffic. Enter a number from 1 to 65535. Common ports are 80 and 443.
   4. For **Protocol**, choose the web protocol that your gateway will use for communication. Select either **https://** or **http://**.

7. Choose **Create Gateway**.
8. Your new responder gateway appears in the gateways list with an **Activating** status. The gateway status will remain **Activating** for 2-5 minutes until creation is complete.

After creating your application, you can view its details, monitor performance metrics, and make configuration changes as needed.

### Updating gateway description

You can update the gateway description using the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](../api.md "../api.md").

Use the following command to create a responder gateway using the AWS Command Line Interface (AWS CLI).

**Create a responder gateway with required parameters**

```
`$` `aws rtbfabric create-responder-gateway \
--description `"My RTB responder gateway"` \
--vpc-id `vpc-01f345ad6524a6d7` \
--subnet-ids `subnet-abc12345 subnet-def67890` \
--security-group-ids `sg-12345678` \
--port `443` \
--protocol `HTTPS` \
--client-token `"unique-client-token-123"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

**Create with optional domain name and trust store configuration**

```
`$` `aws rtbfabric create-responder-gateway \
--description `"My RTB responder gateway"` \
--vpc-id `vpc-01f345ad6524a6d7` \
--subnet-ids `subnet-abc12345 subnet-def67890` \
--security-group-ids `sg-12345678` \
--domain-name `responder.example.com` \
--port `443` \
--protocol `HTTPS` \
--client-token `"unique-client-token-123"` \
--trust-store-configuration `certificateAuthorityCertificates="-----BEGIN CERTIFICATE-----..."` \
--tags `Environment=Production Team=RTB` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

### Logging

When logging is configured, default sampling behavior applies. Service logs capture all error logs (`error_log` sampling rate of 1) and no filter logs (`filter_log` sampling rate of 0). To modify sampling rates after creation, see [UpdateLink](../api.md "../api.md") in the _AWS RTB Fabric API Reference_.

## Searching for responder gateways

Use the search functionality in the console to locate specific gateways in your environment. The gateways table displays key information including gateway ID, status, name, associated links, and creation date.

###### To search for responder gateways

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric "https://console.aws.amazon.com/rtbfabric").
2. In the navigation pane, choose **Responder gateways**.
3. In the **Find responder gateways** search box, enter your search criteria to locate specific applications.
4. The table automatically filters to show matching applications as you type.
5. If no applications exist, the console displays **No responder gateways** with an option to create your first application.

Use the following command to get details for a specific responder gateway using the AWS Command Line Interface (AWS CLI).

**Get details for a specific responder gateway**

```
`$` `aws rtbfabric get-responder-gateway \
--gateway-id `"rtb-gw-kasoi29asfdhn"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

## Viewing associated links

Each responder gateway can have associated links that connect it to requester gateways. You can view these links and their details through the console.

###### To view associated links for a responder application

1. On the **Responder gateways** page, select the radio button next to the responder gateway you want to view.
2. Choose **View details** to see comprehensive information about the application, including its configuration, status, and associated resources.
3. Choose the **Associated links** tab to view existing links and their details.

Use the following command to list all links associated with a specific responder gateway using the AWS Command Line Interface (AWS CLI).

**List all links associated with a gateway**

```
`$` `aws rtbfabric list-links \
--gateway-id `"rtb-gw-dsj34i23nsllka"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

**List links with pagination**

```
`$` `aws rtbfabric list-links \
--gateway-id `"rtb-gw-dsj34i23nsllka"` \
--max-results `10` \
--next-token `"token"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

## Deleting responder gateways

When you no longer need a responder gateway, you can delete it from your environment. This action is irreversible and will terminate all bidding activities associated with the application.

We recommend deleting unused responder gateways to optimize resource usage and costs. AWS may delete unused gateways after 30 days of inactivity to manage infrastructure resources.

###### Warning

Deleting a responder gateway is permanent and cannot be undone. Check your gateway metrics to verify there is no active traffic before proceeding with deletion.

###### To delete a responder gateway

1. On the **Responder gateways** page, select the radio button next to the responder gateway you want to delete.
2. Choose **Delete** from the action buttons at the top of the page.
3. If the application has associated links, a dialog appears with the message "To delete this application, you must first delete all of its associated links. You can delete links on the Links table." Follow the provided instructions to delete associated links first, then return to delete the application. For more information, see [Deleting links](links.md#deleting-rtb-links "links.md#deleting-rtb-links").
4. If the application has no associated links, confirm the deletion when prompted.

Use the following command to delete a responder gateway using the AWS Command Line Interface (AWS CLI).

**Delete a responder gateway**

```
`$` `aws rtbfabric delete-responder-gateway \
--gateway-id `"rtb-gw-kasoi29asfdhn"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```
