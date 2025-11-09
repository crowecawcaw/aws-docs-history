AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Setting up the

Agentless Collector data collection module for VMware vCenter

This section describes how to set up the Agentless Collector VMware vCenter
data collection module to collect server inventory, profile, and utilization data from
your VMware VMs.

###### Note

Before starting vCenter setup, make sure you can provide vCenter credentials with
Read and View permissions set for the System group.

###### To set up the VMware vCenter data collection module

1.  On the **Agentless Collector** dashboard page, under
    **Data collection**, choose **Set up** in
    the **VMware vCenter** section.
2.  On the **Set up VMware vCenter data collection** page,
    perform the following:

        1. Under **vCenter credentials**:


        	1. For **vCenter URL/IP**, enter the IP address
        	 of your VMware vCenter Server host.
        	2. For **vCenter Username**, enter the name of a
        	 local or domain user that the collector uses to communicate with
        	 vCenter. For domain users, use the form
        	 *domain*\*username* or
        	 *username*@*domain*.
        	3. For **vCenter Password**, enter the local or
        	 domain user password.
        2. Under **Data collection preferences**:


        	1. To automatically start collecting data immediately following a
        	 successful setup, select **Start data collection
        	 automatically**.
        3. Choose **Set up**.

    Next, you'll see the **VMware data collection details** page, which
    is described in the next topic.
