

# Step 3: Create Amazon FSx Volumes
<a name="net-win-step-3-create-amazon-fsx-volumes"></a>

1. The global fileshare and transport directories need to be available across all your SAP system’s EC2 instances. In this guide, we assume that you are using Amazon FSx for this purpose.

1. Be sure that you’ve satisfied the prerequisites in the Technical Requirements section of this document. You will need to have already deployed your EC2 instances in each of the Availability Zones where you will create Amazon FSx filesystems.

1. Follow the step-by-step instructions in the [Getting Started with Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html) documentation

1. For high availability deployments that require Multi-AZ redundancy to tolerate temporary AZ unavailability, follow the instructions to [create multiple ﬁle systems in separate AZs](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/multi-az-deployments.html).