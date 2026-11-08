

# Software bill of materials
<a name="securityhub-v2-sbom"></a>

 A software bill of materials (SBOM) is a list of the software packages installed on a compute resource. AWS Security Hub builds an organization-wide SBOM inventory from the SBOMs that Amazon Inspector generates for the compute resources it scans. Security Hub keeps the inventory current as Amazon Inspector scans new and changed resources, so you don't need to export and reconcile SBOM files yourself. 

 The inventory covers the following types of compute resources, in AWS and in other cloud providers that you connect to Security Hub: 
+  **Virtual machines** – For example, Amazon Elastic Compute Cloud (Amazon EC2) instances and Microsoft Azure virtual machines. 
+  **Container images** – For example, Amazon Elastic Container Registry (Amazon ECR) container images and Azure Container Registry container images. 
+  **Serverless functions** – For example, AWS Lambda functions. 

 Use the SBOM inventory to find every resource that contains a specific package when a new vulnerability is disclosed, to understand what a resource does when you triage a finding on it, and to keep a current record of your software supply chain for compliance programs. 

 Administrator accounts can view software from all enabled accounts in their organization. Member accounts can view only the software on resources in their own account. 

## How the SBOM inventory works
<a name="securityhub-v2-sbom-how-it-works"></a>

 When Amazon Inspector scans a supported resource, it generates an SBOM that lists the packages it found on that resource. Amazon Inspector sends each new SBOM to Security Hub, and Security Hub stores the latest SBOM for each resource. When a resource is terminated, deleted, or leaves Amazon Inspector coverage, Security Hub removes its software from the inventory. Security Hub also reconciles the inventory against Amazon Inspector on a schedule so that the two stay in sync. 

 Security Hub organizes the inventory by package. A package is a single software component, such as `openssl` version `3.1.4`. 

 A package appears once in the inventory no matter how many resources it is installed on. The **Resources** count tells you how widely it is deployed. In the summary charts, Security Hub counts one installation for each resource a package is on, so the chart totals can be higher than the number of rows in the table. For example, `openssl 3.1.4` installed on three resources is one row in the table and three installations in the chart. 

 After Amazon Inspector generates a new SBOM, it can take a few hours for the change to appear in the SBOM inventory. 

## Prerequisites
<a name="securityhub-v2-sbom-prerequisites"></a>

 The SBOM inventory requires no setup in Security Hub. It populates automatically when the following conditions are met: 
+  Security Hub is enabled in the AWS account and AWS Region. 
+  Amazon Inspector is enabled for the compute resource types that you want to inventory, such as Amazon EC2 instances, Amazon ECR container images, or Lambda functions. Security Hub shows software only for the resource types that Amazon Inspector scans. For example, if Amazon Inspector scans Amazon EC2 instances but not Lambda functions, the inventory contains software from your Amazon EC2 instances only. For resources in other cloud providers, Amazon Inspector scanning is set up when you connect the provider to Security Hub. For more information, see [Integrating Security Hub with Microsoft Azure](securityhub-v2-azure.md). 

 If Amazon Inspector isn't enabled, the SBOM page shows an **Amazon Inspector is not enabled** message with an **Enable Inspector** button that opens the Security Hub configuration settings. For more information about enabling Amazon Inspector through Security Hub, see [Vulnerability management from Amazon Inspector](securityhub-v2-da-policy.md#securityhub-v2-configuration-catalog-vuln). 

## Viewing the SBOM page
<a name="securityhub-v2-sbom-page"></a>

 The SBOM page lists every package in the inventory for the accounts you can view. 

**To open the SBOM page**

1.  Open the Security Hub console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/). 

1.  In the navigation pane, under **Inventory**, choose **SBOM**. 

 The SBOM page shows the following information: 
+  **Distribution and footprint** – Two charts that summarize the inventory. **Packages by type** shows how installations are distributed across package types, with the total number of installations in the center. **Most common packages** shows the packages that are installed on the largest number of resources. Choose a chart value to filter the package table to that value. 
+  **Package table** – One row for each package and version, with the **Package**, **Version**, **Package type**, and **Resources** columns. The table is sorted by package name by default. Choose a column header to sort by that column. 
+  **Filters and grouping** – Filter the table by package, version, package type, account, Region, resource type, or cloud provider, and group it by package type, account, Region, or resource type. Quick filters show the most common values for each of these properties. You can save a set of filters as a filter set and reuse it later. 

## Pivoting between packages and resources
<a name="securityhub-v2-sbom-pivot"></a>

 The SBOM inventory connects packages to the resources they are installed on, so you can move between the two views in either direction. 

 From the SBOM page, choose a package name or its **Resources** count to list the resources that contain that package. From that list, choose a resource to open its resource detail panel, where you can review the resource's criticality, its findings, and all of its installed software. 

 From the **Resources** page, or from any finding, open a compute resource and choose the **Installed software** tab to see every package installed on that resource, with its version and package type. You can filter the list to find a specific package. 