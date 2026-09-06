

# Using shared AWS Cloud Map namespaces with Amazon ECS Service Connect
<a name="service-connect-shared-namespaces-setup"></a>

Setting up shared AWS Cloud Map namespaces for Service Connect involves the following steps: Namespace owner creating the namespace, owner sharing it through AWS Resource Access Manager (AWS RAM), consumer accepting the resource share, and consumer configuring Service Connect to use the shared namespace.

## Step 1: Create the AWS Cloud Map namespace
<a name="service-connect-shared-namespaces-create"></a>

The namespace owner creates a AWS Cloud Map namespace that will be shared with other accounts.

**To create a namespace for sharing using the AWS Management Console**

1. Open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/).

1. Choose **Create namespace**.

1. Enter a **Namespace name**. This name will be used by services across all participating accounts.

1. For **Namespace type**, choose the appropriate type for your use case:
   + **API calls** ‐ HTTP namespaces for service discovery without DNS functionality.
   + **API calls and DNS queries in VPCs** ‐ Private DNS namespaces for service discovery with private DNS queries in a VPC.
   + **API calls and public DNS queries** ‐ Public DNS namespaces for service discovery with public DNS queries.

1.  Choose **Create namespace**.

## Step 2: Share the namespace using AWS RAM
<a name="service-connect-shared-namespaces-share"></a>

The namespace owner uses AWS RAM to share the namespace with other AWS accounts.

**To share a namespace using the AWS RAM console**

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/).

1. Choose **Create resource share**.

1. For **Name**, enter a descriptive name for the resource share.

1. In the **Resources** section:

   1. For **Resource type**, choose **Cloud Map Namespaces**.

   1. Select the namespace you created in the previous step.

1. In the **Managed permissions** section, specify **AWSRAMPermissionCloudMapECSFullPermission**.
**Important**  
You must use the `AWSRAMPermissionCloudMapECSFullPermission` managed permission to share the namespace for Service Connect to work properly with the namespace.

1. In the **Principals** section, specify the AWS accounts you want to share the namespace with. You can enter account IDs or organizational unit IDs.

1. Choose **Create resource share**.

## Step 3: Accept the resource share
<a name="service-connect-shared-namespaces-accept"></a>

Namespace consumer accounts must accept the resource share invitation to use the shared namespace.

**To accept a resource share invitation using the AWS RAM console**

1. In the consumer account, open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/).

1. In the navigation pane, choose **Shared with me**, then choose **Resource shares**.

1. Select the resource share invitation and choose **Accept resource share**.

1. After accepting, note the shared namespace ARN from the resource details. You'll use this ARN when configuring Service Connect services.

## Step 4: Configure an Amazon ECS service with the shared namespace
<a name="service-connect-shared-namespaces-configure"></a>

After accepting the shared namespace, the namespace consumer can configure Amazon ECS services to use the shared namespace. The configuration is similar to using a regular namespace, but you must specify the namespace ARN instead of the name. For a detailed service creation procedure, see [Creating an Amazon ECS rolling update deployment](create-service-console-v2.md).

**To create a service with a shared namespace using the AWS Management Console**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster that you want to create the service in.

1. Under **Services**, choose **Create**.

1. After filling in other details depending on your workload, in the **Service Connect** section, choose **Use Service Connect**.

1. For **Namespace**, enter the full ARN of the shared namespace.

   The ARN format is: `arn:aws:servicediscovery:{{region}}:{{account-id}}:namespace/{{namespace-id}}`

1. Configure the remaining Service Connect settings as needed for your service type (client or client-server).

1. Complete the service creation process.

You can also configure services using the AWS CLI or AWS SDKs by specifying the shared namespace ARN in the `namespace` parameter of the `serviceConnectConfiguration`.

```
aws ecs create-service \
    --cluster my-cluster \
    --service-name my-service \
    --task-definition my-task-def \
    --service-connect-configuration '{
        "enabled": true,
        "namespace": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcdef1234567890",
        "services": [{
            "portName": "web",
            "discoveryName": "my-service",
            "clientAliases": [{
                "port": 80,
                "dnsName": "my-service"
            }]
        }]
    }'
```