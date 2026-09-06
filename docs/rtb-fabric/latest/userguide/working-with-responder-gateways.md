

# Responder gateways
<a name="working-with-responder-gateways"></a>

Responder gateways are RTB Fabric infrastructure components that serve as connection points for customer gateways. Responder gateways receive requests from requester gateways and forward them to responder gateways, then return responses through the same pathway. Gateways operate colocated with your VPC and provide routing, load balancing, and processing capabilities. You maintain complete control over your bidding algorithms, response logic, and data processing, while RTB Fabric provides the secure infrastructure for connectivity.

**Topics**
+ [Creating a responder gateway](#creating-responder-gateway)
+ [Creating an external responder gateway](#creating-external-responder-gateway)
+ [Searching for responder gateways](#searching-responder-gateways)
+ [Updating an existing responder gateway](#updating-responder-gateway)
+ [Getting a responder gateway](#getting-responder-gateway)
+ [Listing responder gateways](#listing-responder-gateways)
+ [Viewing associated links](#viewing-responder-associated-links)
+ [Deleting responder gateways](#deleting-responder-gateways)

## Creating a responder gateway
<a name="creating-responder-gateway"></a>

Create a new responder gateway that can respond to bid opportunities.

**Note**  
You are responsible for the data you process through RTB Fabric, including ensuring that personally identifiable information (PII) is handled according to your privacy requirements and applicable regulations.

**To create a responder gateway**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric).

1. In the navigation pane, choose **Responder gateway**.

1. Choose **Create responder gateway**.

1. In the **Responder gateway information** section, for **Gateway description**, enter a description of the gateway's purpose. The description can have up to 255 characters.

1. In the **VPC configuration** section, configure the network settings:

   1. For **VPC ID**, enter a valid VPC ID. For example: vpc-01f345ad6524a6d7.

   1. For **Subnet ID**, enter the IDs of 1-5 subnets, separated by commas. Subnets must have at least 200 free IP addresses. These subnets should match your core workload deployment subnets or be secondary CIDR subnets within the same Availability Zones.

   1. For **Security group ID**, enter the IDs of 1-5 security groups, separated by commas. We recommend you create new security groups for your gateways for security.

1. In the **Responder endpoint configuration** section, choose an endpoint type from the dropdown and configure the fields for that type:
   + **Domain name** — Configure a direct endpoint using a domain name.

     1. For **Domain name**, enter a fully qualified domain name (FQDN) where you want your gateway to be accessed. Valid characters are a-z, A-Z, 0-9, periods (.), and hyphens (-). Maximum length is 253 characters.

     1. For **Port number**, enter the network port number where your gateway will listen for incoming traffic. Enter an integer from 1 to 65535. Common ports are 80 and 443.

     1. For **Protocol**, select either **HTTP** or **HTTPS**.

     1. (HTTPS only) For **CA certificate chain**, enter the CA certificate chain for your domain. Include the intermediate and root certificates in PEM format. Maximum size: 2048 characters.
   + **EKS** — Configure a managed endpoint that points to a Kubernetes cluster.

     1. For **EKS Endpoints resource name**, enter the name of the Kubernetes Endpoints resource. Must be a DNS label with a maximum of 63 characters.

     1. For **EKS Endpoints resource namespace**, enter the Kubernetes namespace where the Endpoints resource is located.

     1. For **Cluster API server endpoint URI**, enter the EKS cluster API server endpoint URL. Must be a valid URI.

     1. For **Cluster API server CA certificate**, enter the base64-encoded CA certificate chain for the EKS API server.

     1. For **Cluster name**, enter the name of the EKS cluster.

     1. For **IAM role**, select an IAM role with `ec2:DescribeSubnets` permission that is associated with EKS RBAC.

     1. For **Port number**, enter the network port number. Enter an integer from 1 to 65535.

     1. For **Protocol**, select either **HTTP** or **HTTPS**.

     1. (HTTPS only) For **Domain name**, enter the fully qualified domain name for the endpoint.

     1. (HTTPS only, optional) For **CA certificate chain**, enter the CA certificate chain in PEM format.
   + **Auto Scaling group** — Configure a managed endpoint using EC2 Auto Scaling groups.

     1. For **Auto Scaling groups**, select one or more Auto Scaling groups that will receive traffic.

     1. For **IAM role**, select an IAM role that grants RTB Fabric permission to discover instances in the Auto Scaling groups.

     1. For **Port number**, enter the network port number. Enter an integer from 1 to 65535.

     1. For **Protocol**, select either **HTTP** or **HTTPS**.

     1. (HTTPS only) For **Domain name**, enter the fully qualified domain name for the endpoint.

     1. (HTTPS only, optional) For **CA certificate chain**, enter the CA certificate chain in PEM format.

     1. (Optional) To enable health checks, configure the **Health check configuration** section. For details, see [Health checks for Managed Endpoints](health-checks-for-managed-endpoints.md).

1. Choose **Create Gateway**.

1. Your new responder gateway appears in the gateways list with an **Activating** status. The gateway status will remain **Activating** for 20-40 minutes until creation is complete.

After creating your gateway, you can view its details, monitor performance metrics, and make configuration changes as needed.

### AWS CLI
<a name="create-responder-cli"></a>

Use the following command to create a responder gateway using the AWS Command Line Interface (AWS CLI).

**Create a responder gateway with domain name and trust store configuration**

```
$ aws rtbfabric create-responder-gateway \
--description {{"My RTB responder gateway"}} \
--vpc-id {{vpc-01f345ad6524a6d7}} \
--subnet-ids {{subnet-abc12345 subnet-def67890}} \
--security-group-ids {{sg-12345678}} \
--domain-name {{responder.example.com}} \
--port {{443}} \
--protocol {{HTTPS}} \
--trust-store-configuration {{certificateAuthorityCertificates="-----BEGIN CERTIFICATE-----..."}} \
--tags {{Environment=Production Team=RTB}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create with EKS managed endpoint configuration**

```
$ aws rtbfabric create-responder-gateway \
--description {{"My EKS responder gateway"}} \
--vpc-id {{vpc-0abc1234def567890}} \
--subnet-ids {{subnet-0abc1234def567890 subnet-0def5678abc901234}} \
--security-group-ids {{sg-0abc1234def567890}} \
--port {{443}} \
--protocol {{HTTPS}} \
--domain-name {{bidder.example.com}} \
--managed-endpoint-configuration {{'{"eksEndpoints":{"endpointsResourceName":"my-bidder-service","endpointsResourceNamespace":"bidding-ns","clusterApiServerEndpointUri":"https://ABCDEF1234567890.gr7.us-east-1.eks.amazonaws.com","clusterApiServerCaCertificateChain":"LS0tLS1CRUdJTi...base64-encoded-CA-cert...LS0tLS1FTkQ=","clusterName":"my-eks-cluster","roleArn":"arn:aws:iam::123456789012:role/RtbFabricManagedEndpointRole"}}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create with ASG managed endpoint configuration**

```
$ aws rtbfabric create-responder-gateway \
--description {{"My ASG responder gateway"}} \
--vpc-id {{vpc-0abc1234def567890}} \
--subnet-ids {{subnet-0abc1234def567890 subnet-0def5678abc901234}} \
--security-group-ids {{sg-0abc1234def567890}} \
--port {{8080}} \
--protocol {{HTTP}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-asg-name"],"roleArn":"arn:aws:iam::123456789012:role/RtbFabricManagedEndpointRole"}}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

### Logging
<a name="responder-gateway-logging"></a>

When logging is configured, default sampling behavior applies. Service logs capture all error logs (`error_log` sampling rate of 1) and no filter logs (`filter_log` sampling rate of 0). To modify sampling rates after creation, see [UpdateLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/) in the *AWS RTB Fabric API Reference*.

## Creating an external responder gateway
<a name="creating-external-responder-gateway"></a>

Create an external responder gateway in RTB Fabric if you do not already have one. Inbound external links with custom domains require an external gateway — a gateway type designed for receiving traffic from endpoints outside RTB Fabric. Standard (internal) responder gateways do not support inbound external links with custom domains features such as certificate association and routing rules.

**To create an external responder gateway**

1. Follow the same steps as [Creating a responder gateway](#creating-responder-gateway), but on the creation page, select the **External gateway** tile instead of the default gateway type.

1. Complete the remaining configuration fields as described in the standard gateway creation procedure.

### Listener configuration
<a name="responder-gateway-listener-config"></a>

A listener configuration defines which protocols a gateway with external links accepts for incoming traffic. By default, a gateway listens on a single protocol (HTTPS). With multiprotocol support, you can configure a gateway to accept both HTTP and HTTPS traffic simultaneously using the `listenerConfig` parameter.

The `listenerConfig` contains a `protocols` list that specifies one or two protocols:
+ `["HTTPS"]` — The gateway accepts HTTPS traffic only (default).
+ `["HTTP", "HTTPS"]` — The gateway accepts both HTTP and HTTPS traffic.

Multi-protocol support is useful when you need to support partners that send traffic over HTTP while also serving HTTPS traffic with TLS termination. When both protocols are enabled, the gateway provisions listeners for each protocol on the public ingress cluster.

**Note**  
If you enable both HTTP and HTTPS, TLS certificate association and SNI-based certificate resolution apply only to HTTPS connections. HTTP connections bypass TLS termination entirely.

### AWS CLI
<a name="create-external-gateway-cli"></a>

Use the following command to create an external responder gateway using the AWS Command Line Interface (AWS CLI).

**Create an external responder gateway with HTTP and ASG managed endpoint**

```
$ aws rtbfabric create-responder-gateway \
--description {{"External gateway for inbound external links with custom domains"}} \
--vpc-id {{vpc-0abc123def456}} \
--subnet-ids {{subnet-0abc123 subnet-0def456}} \
--security-group-ids {{sg-0abc123}} \
--port {{80}} \
--protocol {{HTTP}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-asg-name"],"roleArn":"arn:aws:iam::123456789012:role/RtbFabricManagedEndpointRole"}}'}} \
--gateway-type {{EXTERNAL}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create an external responder gateway with multi-protocol listener configuration (HTTP and HTTPS)**

```
$ aws rtbfabric create-responder-gateway \
--description {{"External gateway for inbound external links with custom domains"}} \
--vpc-id {{vpc-0abc123def456}} \
--subnet-ids {{subnet-0abc123 subnet-0def456}} \
--security-group-ids {{sg-0abc123}} \
--port {{443}} \
--protocol {{HTTPS}} \
--listener-config {{'{"protocols":["HTTP","HTTPS"]}'}} \
--domain-name {{bidder.example.com}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-asg-name"],"roleArn":"arn:aws:iam::123456789012:role/RtbFabricManagedEndpointRole"}}'}} \
--gateway-type {{EXTERNAL}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create an external responder gateway with HTTPS and EKS managed endpoint**

```
$ aws rtbfabric create-responder-gateway \
--description {{"External gateway with EKS endpoint discovery"}} \
--vpc-id {{vpc-0abc123def456}} \
--subnet-ids {{subnet-0abc123 subnet-0def456}} \
--security-group-ids {{sg-0abc123}} \
--port {{443}} \
--protocol {{HTTPS}} \
--domain-name {{bidder.example.com}} \
--managed-endpoint-configuration {{'{"eksEndpoints":{"endpointsResourceName":"my-bidder-service","endpointsResourceNamespace":"bidding-ns","clusterApiServerEndpointUri":"https://ABCDEF1234567890.gr7.us-east-1.eks.amazonaws.com","clusterApiServerCaCertificateChain":"LS0tLS1CRUdJTi...base64-encoded-CA-cert...LS0tLS1FTkQ=","clusterName":"my-eks-cluster","roleArn":"arn:aws:iam::123456789012:role/RtbFabricManagedEndpointRole"}}'}} \
--gateway-type {{EXTERNAL}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Key parameters:**
+ `--gateway-type EXTERNAL` — Required. Creates an external gateway that supports inbound external links with custom domains, certificate association, and routing rules.
+ `--managed-endpoint-configuration` — Required for external gateways. Specifies the backend that receives traffic. Provide either an `autoScalingGroups` configuration (with ASG names and a role ARN) or an `eksEndpoints` configuration (with EKS cluster details). For more information, see [Managed endpoints](managed-endpoints.md).
**Important**  
When using `--protocol HTTPS` with `--managed-endpoint-configuration`, the `--domain-name` parameter is required. The domain name must be allowlisted by the RTB Fabric team for your account before you can create your gateway. Contact AWS Support to request domain name allowlisting. The role used for managed endpoint must have **RTBFabricManagedEndpoint=true** tag.
+ `--protocol` — `HTTP` or `HTTPS`. Choose based on whether you want TLS termination at the gateway.
+ `--port` — The port the gateway listens on (for example, `80` for HTTP or `443` for HTTPS).

Record the gateway endpoint hostname (for example, `rtb-gw-abc123.123456789012.gateway.rtbfabric.us-east-1.amazonaws.com`). You need this value when updating DNS records to route traffic through your custom domain.

## Searching for responder gateways
<a name="searching-responder-gateways"></a>

Use the search functionality in the console to locate specific gateways in your environment. The gateways table displays key information including gateway ID, status, name, associated links, and creation date.

**To search for responder gateways**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric).

1. In the navigation pane, choose **Responder gateways**.

1. In the **Find responder gateways** search box, enter your search criteria to locate specific gateways.

1. The table automatically filters to show matching gateways as you type.

1. If no gateways exist, the console displays **No responder gateways** with an option to create your first gateway.

## Updating an existing responder gateway
<a name="updating-responder-gateway"></a>

You can update the gateway description and Auto Scaling group managed endpoint configuration. Other fields cannot be updated after gateway creation.

**To update a responder gateway**

1. On the **Responder gateways** page, select the radio button next to the responder gateway you want to update.

1. Choose **View details**.

1. Choose **Edit** to modify the gateway configuration.
**Note**  
The **Edit** button is only available for responder gateways that have Auto Scaling group managed endpoints configured.

1. Update the **Gateway description** or **Auto Scaling group** managed endpoint configuration as needed.

1. Choose **Save changes**.

### AWS CLI
<a name="update-responder-gateway-cli"></a>

Use the following commands to update a responder gateway using the AWS Command Line Interface (AWS CLI).

**Update gateway description**

```
$ aws rtbfabric update-responder-gateway \
--gateway-id {{"rtb-gw-kasoi29asfdhn"}} \
--description {{"Updated responder gateway description"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Update Auto Scaling group managed endpoint configuration**

```
$ aws rtbfabric update-responder-gateway \
--gateway-id {{"rtb-gw-kasoi29asfdhn"}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-new-asg-name","my-second-asg"],"roleArn":"arn:aws:iam::123456789012:role/RtbFabricManagedEndpointRole"}}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Getting a responder gateway
<a name="getting-responder-gateway"></a>

Retrieve detailed information about a specific responder gateway, including its configuration, status, VPC settings, and endpoint configuration.

### AWS CLI
<a name="get-responder-gw-cli"></a>

Use the following command to get details for a specific responder gateway using the AWS Command Line Interface (AWS CLI).

**Get details for a specific responder gateway**

```
$ aws rtbfabric get-responder-gateway \
--gateway-id {{"rtb-gw-kasoi29asfdhn"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Listing responder gateways
<a name="listing-responder-gateways"></a>

List all responder gateways in your account.

### AWS CLI
<a name="list-responder-gateways-cli"></a>

Use the following commands to list responder gateways using the AWS Command Line Interface (AWS CLI).

**List all responder gateways**

```
$ aws rtbfabric list-responder-gateways \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Viewing associated links
<a name="viewing-responder-associated-links"></a>

Each responder gateway can have associated links that connect it to requester gateways. You can view these links and their details through the console.

**To view associated links for a responder gateway**

1. On the **Responder gateways** page, select the radio button next to the responder gateway you want to view.

1. Choose **View details** to see comprehensive information about the gateway, including its configuration, status, and associated resources.

1. Choose the **Associated links** tab to view existing links and their details.

### AWS CLI
<a name="get-associated-links-responder-gw-cli"></a>

Use the following command to list all links associated with a specific responder gateway using the AWS Command Line Interface (AWS CLI).

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

## Deleting responder gateways
<a name="deleting-responder-gateways"></a>

When you no longer need a responder gateway, you can delete it from your environment. This action is irreversible and will terminate all bidding activities associated with the gateway.

We recommend deleting unused responder gateways to optimize resource usage and costs. AWS may delete unused gateways after 30 days of inactivity to manage infrastructure resources.

**Warning**  
Deleting a responder gateway is permanent and cannot be undone. Check your gateway metrics to verify there is no active traffic before proceeding with deletion.

**Important**  
You must delete all associated links before you can delete a responder gateway. If the gateway has any associated links, the deletion will fail.

**To delete a responder gateway**

1. On the **Responder gateways** page, select the radio button next to the responder gateway you want to delete.

1. Choose **Delete** from the action buttons at the top of the page.

1. If the gateway has associated links, a dialog appears with the message "To delete this gateway, you must first delete all of its associated links. You can delete links on the Links table." Follow the provided instructions to delete associated links first, then return to delete the gateway. For more information, see [Deleting links](deleting-rtb-links.md).

1. If the gateway has no associated links, confirm the deletion when prompted.

### AWS CLI
<a name="delete-responder-gw-cli"></a>

Use the following command to delete a responder gateway using the AWS Command Line Interface (AWS CLI).

**Delete a responder gateway**

```
$ aws rtbfabric delete-responder-gateway \
--gateway-id {{"rtb-gw-kasoi29asfdhn"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```