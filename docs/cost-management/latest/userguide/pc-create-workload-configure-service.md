

# Configure new services in my workload estimate
<a name="pc-create-workload-configure-service"></a>

This section outlines how to configure new services in a workload estimate.

## Prerequisites
<a name="pc-create-workload-configure-service-prerequisites"></a>

The following procedure assumes that you have already completed the [Adding new services to my workload estimate](pc-create-workload-new-service.md) process.

## Procedure
<a name="pc-create-workload-configure-service-procedure"></a>

**To configure new services in a workload estimate**

1. Open the Pricing Calculator console at [ https://console.aws.amazon.com/costmanagement/ ](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Pricing Calculator**.

1. Navigate to the workload estimate where you added new services.

1. Select the dropdown arrow beside the name of the new service you added.

1. Choose **Configure**.

1. On the **Configure service** page, you can select **Guided configuration** or **Condensed configuration**. 
   + In the **Guided configuration**, you can select a template for that specific service. For more information, see [Guided configuration](#pc-create-workload-guided).
   + In the **Condensed configuration**, you can select the usage type and operation for that specific service. For more information, see [Condensed configuration](#pc-create-workload-condensed).

1. To complete the configuration process for the new services, choose **Save changes**.

### Guided configuration
<a name="pc-create-workload-guided"></a>

After you choose a Location type, Location, and Account, you will need to choose a Template. The templates provide products that typically go together so that you can build a realistic estimate. For example, if you choose the Amazon EC2 template, you are provided with EC2 Instance, EBS storage, EBS snapshots, CloudWatch monitoring, and several data transfer options. If you don’t want to add a specific product to your estimate, you can remove that product by unselecting the checkbox on the product’s container. All products are selected by default.

**Note**  
The values in fields outside of Usage amount will not be saved and you will not be able to view those fields if you reopen a saved usage line.

### Condensed configuration
<a name="pc-create-workload-condensed"></a>

You can use the condensed configuration if you are familiar with usage types and operations of products that you want to model usage for. Usage types are the units that each service uses to measure the usage of a specific type of resource. For example, the BoxUsage:t2.micro(Hrs) usage type filters by the running hours of Amazon EC2 t2.micro instances. Operation are requests made to a service and tasks performed by a service, such as write and get requests to Amazon S3. 

Usage types and operation are available through the Price List API `GetProducts`. On Pricing Calculator console’s Condensed configuration, you will be able to find the usage types and operations in their respective dropdown without needing to query Price List API.