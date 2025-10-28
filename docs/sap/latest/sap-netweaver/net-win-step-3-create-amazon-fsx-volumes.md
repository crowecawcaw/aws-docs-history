# Step 3: Create Amazon FSx Volumes

1. The global fileshare and transport directories need to be available across all your SAP system’s EC2 instances. In this guide, we assume that you are using Amazon FSx for this purpose.
2. Be sure that you’ve satisfied the prerequisites in the Technical Requirements section of this document. You will need to have already deployed your EC2 instances in each of the Availability Zones where you will create Amazon FSx filesystems.
3. Follow the step-by-step instructions in the [Getting Started with Amazon FSx](../../../fsx/latest/WindowsGuide/getting-started.md "../../../fsx/latest/WindowsGuide/getting-started.md") documentation
4. For high availability deployments that require Multi-AZ redundancy to tolerate temporary AZ unavailability, follow the instructions to [create multiple ﬁle systems in separate AZs](../../../fsx/latest/WindowsGuide/multi-az-deployments.md "../../../fsx/latest/WindowsGuide/multi-az-deployments.md").
