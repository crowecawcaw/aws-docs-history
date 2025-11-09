# Release notes for AWS Service Management Connector for ServiceNow

The latest version includes support for Zurich, Yokohama, and Xanadu and minor fixes to
existing integrations. The prior version included enhancements to
the existing AWS Health integration.

## Version 5.1.10

**AWS ServiceNow Connector Core Features**

- Supports the latest ServiceNow platform releases of Zurich, Yokohama, and Xanadu.

**Support**

- Fix for region selection for AWS Support integration.

## Version 5.1.6

**AWS ServiceNow Connector Core Features**

- Supports the latest ServiceNow platform releases of Yokohama and Xanadu.

**AWS Config**

- Fix for AWS tags filtering.

## Version 5.1.3

**AWS ServiceNow Connector Core Features**

- Supports the latest ServiceNow platform releases Xanadu (X), Washington DC (W), and Vancouver (V).

**AWS Security Hub**

- Fix an issue with date and timestamp for AWS Security Hub findings to show the correct format.

###### Note

To maintain the integration capabilities of the Xanadu ServiceNow release, upgrade the connector to version 5.1.3.

## Version 5.0.0

**AWS Health**

- Create incidents, including changes, from AWS Health events.
- Supports affected resource tracking for planned lifecycle events.
- Supports pagination by syncing health events with visual information.
- Supports AWS Organizations to view and consolidate multiple AWS accounts via Amazon EventBridge.
- Updated dashboard that allows selecting accounts and events.
- Support for ServiceNow Vancouver release.
- Support for ServiceNow Washington DC release.

## Version 4.8.5

**AWS ServiceNow Connector Core Features**

- Dashboard that displays reports/charts for AWS Service Catalog, AWS Config, and AWS Security Hub
  integrations in the ServiceNow platform.
- Support for China Regions (Beijing and Ningxia) for all AWS services compatible
  with China Regions.
- Support for ServiceNow Utah release.

**AWS Service Catalog**

- Support for the Terraform open source product type, enabling self-service
  provisioning with governance for your Terraform
  configurations within AWS from Service Catalog at scale.
- Fix validation issue with mandatory parameters input on catalog item submission.

**AWS Config**

- Support for the following new resource types: Amazon WorkSpaces, Amazon Elastic Container Service (ECS),
  Amazon Elastic Kubernetes Service (EKS), Amazon Elastic File System (EFS), and Amazon RDS Cluster.
- Ability to change synchronization to use many-to-many (MTM) table in the connector.

**AWS Systems Manager OpsCenter**

- Synchronize **Action Item** type OpsItems from AWS Systems Manager Incident Manager.

## Version 4.7.5

**AWS ServiceNow Connector Core Features**

- Supports latest ServiceNow platform releases for Tokyo (T), San Diego (S), and Rome (R).
- Enables conditional dependency on ServiceNow plugins based on the AWS integrations in use.

**AWS Service Catalog**

- Ability to filter Service Catalog synced portfolios in the ServiceNow Service Portal using AWS
  accounts and regions.

**AWS Systems Manager Incident Manager**

- Displays formatted Timeline Events of an incident in ServiceNow incident comments.
- Provides a new Open Incident module to display in-progress incidents.

**Support**

- Ability to configure Support cases through automatic incident creation or staged
  support cases, allowing you to create custom ServiceNow Business Rules and workflow logic.

## Version 4.5.5

**AWS Systems Manager OpsCenter**

- Prevents duplicate incidents created for OpsItems synched to ServiceNow.

## Version 4.5.0

**AWS Health**

- Syncs AWS Health events and resource information.
- Provides a dashboard to view AWS Health status of AWS accounts.

**AWS Systems Manager Incident Manager**

- Syncs AWS Systems Manager Incident Manager incidents as ServiceNow Incidents.
- Creates relationship between synched incident from Incident Manager and the
  associated Ops Item.
- Provides configuration to allow bidirectional or unidirectional
  synchronization of the ‘resolved’ status between ServiceNow incident and
  corresponding AWS incident.

**AWS ServiceNow Connector Core Features**

- Displays AWS account number for validated accounts.
- Supports latest ServiceNow platform releases for Quebec (Q - Patch 5 going
  forward), Rome (R), and San Diego (S).

**AWS Service Catalog**

- Provides Service Portal widget to search AWS Service Catalog products from ServiceNow
  Service Portal.
- Configures independent workflows for different portfolios.
- Provides feature to set a table filter for user selectable Automated
  Tags.

**Support**

- Offers near real-time sync of Support cases to ServiceNow using Amazon
  EventBridge and Amazon SQS queue.
- Syncs Support case severity back into ServiceNow incident.
- Supports AWS accounts with different service accesses.

**AWS Security Hub**

- Provides revised AWS Security Hub Findings form to show remediation
  information.

**AWS Systems Manager Change Manager**

- Syncs AWS CloudTrail events and resource information related to the AWS Change
  Request.

**AWS Config**

- Supports Amazon API Gateway resource type.
- Creates relationship between RDS Instances and RDS Cluster, if present.
- Introduces new attribute mappings and relationships on existing resource
  types.

## Version 4.0.1

**AWS ServiceNow Connector Core Features**

- Supports the latest ServiceNow platform releases for Quebec (Q - Patch 5 going
  forward), Rome (R), and San Diego (S).

**AWS Service Catalog**

- Accurately retrieves launch paths/parameters for catalog items in order
  guides.

**Support**

- Uses GovCloud accounts with Support integration.

**AWS Security Hub**

- Syncs ServiceNow Incident state updates to AWS Security Hub Findings.

## Version 4.0.0

**AWS ServiceNow Connector Core Features**

- Uses Guided Setup to enable you to configure and mark complete ServiceNow install
  components for the AWS Service Management Connector.
- Supports the latest ServiceNow platform releases for Rome (R), Quebec (Q - Patch 5
  going forward).

**Support**

- Views, creates, updates, adds correspondence, and resolves Support cases from
  ServiceNow as incidents.
- Tracks and manages AWS cases (incidents) within ServiceNow as incidents to
  ascertain the health of their AWS services and resources as opposed to swiveling
  between multiple platforms.

**AWS Systems Manager Change Manager**

- Creates Change Requests from a curated list of AWS Change Templates that are
  vetted in AWS Systems Manager Change Manager.
- Enables you to customize the change workflow in ServiceNow and streamline and
  align the maintenance and Service Management governance of AWS resources with your
  existing Change Management process.

**AWS Systems Manager Automation**

- Updates mappings to accurately display Status values of Automation document
  execution in ServiceNow.

## Version 3.8.5

**AWS ServiceNow Connector Core Features**

- Enhances AWS services (AWS Service Catalog, AWS Config, AWS Systems Manager, AWS Security Hub) synchronization to ServiceNow into separate, distinct scheduled
  jobs.
- Renames 'Sync all Accounts' scheduled job to 'Synchronize changes to all AWS
  accounts' based on synchronization enhancements.
- Supports the latest ServiceNow platform releases for Rome (R), Quebec (Q -
  Patch 5 going forward), Paris (P) and Orlando (O).

**AWS Service Catalog**

- Views AppRegistry applications, attribute groups and linked resources in the
  ServiceNow CMDB.
- Enables support for ServiceNow order guides for AWS Service Catalog products and
  AWS Systems Manager automation documents.
- Supports NoEcho parameters when viewing AWS Service Catalog Provisioned Products
  parameters through ServiceNow Requested Item.

**AWS Config**

- Adds a configurable ServiceNow system property for AWS Config integration to
  automatically copy the AWS Resource Id (Object ID in ServiceNow) into ServiceNow's
  Name field to make AWS resources visible as configuration items.
- Updates ELB resource mapping from cmdb_ci_lb_service table to
  cmdb_ci_cloud_load_balancer table.
- Updates relationships visible in the ServiceNow CMDB for AWS resources such as
  Cloud Subnet, DynamoDB, EC2, ELB, RDS, Storage volume, Security groups, and
  VPC.

**AWS Security Hub**

- Synchronizes UserDefinedFields JSON blob for Security Hub Findings.
