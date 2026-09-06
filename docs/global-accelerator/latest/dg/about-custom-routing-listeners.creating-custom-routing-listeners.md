

# Add a listener for a custom routing accelerator in Global Accelerator
<a name="about-custom-routing-listeners.creating-custom-routing-listeners"></a>

This section explains how to add a listener for a custom routing accelerator on the AWS Global Accelerator console. To learn about using API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To add a listener for a custom routing accelerator


The range that you specify when you create a listener defines how many listener port and destination IP address combinations that you can use with your custom routing accelerator. For maximum flexibility, we recommend that you specify a large port range. Each listener port range that you specify must include a minimum of 16 ports.
**Note**  
After you create a listener, you can edit it to add additional port ranges and associated protocols, but you can't decrease existing port ranges.

1. Open the Global Accelerator console at [ https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home). 

1. On the **Accelerators** page, choose a custom routing accelerator.

1. Choose **Add listener**.

1. On the **Add listener** page, enter the listener port range that you want to associate with the accelerator. 

   Listeners support ports 1-65535. For maximum flexibility with a custom routing accelerator, we recommend that you specify a large port range.

1. Choose **Add listener**.