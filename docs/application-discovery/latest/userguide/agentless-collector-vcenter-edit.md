AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Editing VMware vCenter

credentials

To collect server inventory, profile, and utilization data from your VMware VMs, set
up connections to your vCenter servers. For information about setting up VMware vCenter
connections, see [Using the VMware vCenter
Agentless Collector data collection module](agentless-collector-gs-data-collection-vcenter.md "agentless-collector-gs-data-collection-vcenter.md").

This section describes how to edit the vCenter credentials.

###### Note

Before editing vCenter credentials, make sure you can provide vCenter credentials
with Read and View permissions set for the System group.

###### To edit the VMware vCenter credentials

On the [Viewing VMware data collection
details](agentless-collector-gs-vcenter-details.md "agentless-collector-gs-vcenter-details.md") page, choose
**Edit vCenter servers**.

- On the **Edit vCenter** page, perform the following:
  1.  Under **vCenter credentials**:
      1. For **vCenter URL/IP**, enter the IP address
         of your VMware vCenter Server host.
      2. For **vCenter Username**, enter the name of a
         local or domain user that the connector uses to communicate with
         vCenter. For domain users, use the form
         _domain_\*username* or
         *username*@*domain\*.
      3. For **vCenter Password**, enter the local or
         domain user password.

  2.  Choose **Save**.
