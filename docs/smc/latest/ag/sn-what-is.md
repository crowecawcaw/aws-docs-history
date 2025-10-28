# AWS Service Management Connector for ServiceNow

The AWS Service Management Connector for ServiceNow (formerly the AWS Service Catalog
Connector) enables ServiceNow end users to provision, manage, and operate AWS
resources natively through ServiceNow.

ServiceNow administrators can:

- Provide pre-approved, secured, and governed AWS resources to end
  users through Service Catalog.
- Execute automation playbooks through AWS Systems Manager.
- View and manage operational items as incidents through AWS Systems Manager
  OpsCenter.
- Use AWS Config to track resources in the CMDB seamlessly on ServiceNow with the AWS
  Service Management Connector.
- Define new resource types based on ServiceNow CMDB tables and synchronize these
  with AWS Config custom resources.
- Sync AWS Security Hub findings to ServiceNow incidents or problems.
  ServiceNow end users can:

- Browse, request, and provision pre-secured AWS solutions.
- View AppRegistry applications, attribute groups, and related resource details with
  AppRegistry.
- View, update, and resolve Incidents from AWS Systems Manager OpsItems.
- View configuration item details.
- Execute workflows in ServiceNow on AWS resources.
- View, update, and resolve ServiceNow incidents or problems through AWS Security Hub findings.
- View, create, add correspondence and resolve Support cases from ServiceNow
  (including AMS Accelerate support cases).
- View and execute AWS Systems Manager Change Requests from a curated list of
  pre-approved AWS Change templates.
- View resource performance and the availability of AWS services and account through
  AWS Health dashboard.
- Manage and resolve incidents affecting AWS-hosted applications through the
  integration with AWS Systems Manager Incident Manager.
  These features minimize direct AWS platform access, simplify AWS product request and
  operational actions for ServiceNow users. They also provide streamlined Service Management
  governance and oversight over AWS resources and services.

The AWS-supplied connector is available at no charge in the ServiceNow
store. It supports ServiceNow platform releases San Diego(S), Rome (R), and Quebec (Q -
Patch 5 going forward). These new features are generally available in all AWS Regions where
AWS Service Catalog, AWS Config, and AWS Systems Manager services are available. For list of
regions and service quotas of AWS services, see [Service
endpoints and quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md").

###### Note

For the ServiceNow Quebec release, we only support Quebec Patch 5 going forward due to
a deprecated ServiceNow REST API call, `getDeprecatedValue(),` which
inhibited end users’ ability to request AWS Service Catalog products and AWS Systems Manager automation documents in the Connector. ServiceNow resolved the issue in Quebec
Patch 5, so we now support only Patch 5 going forward.

The following AWS services integrate
into this Connector:

- [Service Catalog](https://aws.amazon.com/servicecatalog "https://aws.amazon.com/servicecatalog") allows you to centrally
  manage commonly deployed AWS services and provisioned software products.
  It helps your organization achieve consistent governance and compliance requirements,
  while enabling users to quickly deploy only the approved AWS services
  they need. It also offers [AppRegistry](https://aws.amazon.com/servicecatalog/features/#AWS_Service_Catalog_AppRegistry_features "https://aws.amazon.com/servicecatalog/features/#AWS_Service_Catalog_AppRegistry_features"), which creates a repository of your
  applications and associated resources.
- [AWS Config](https://aws.amazon.com/config "https://aws.amazon.com/config") enables you to assess, audit, and
  evaluate the configurations of your AWS resources. AWS Config continuously
  monitors and records your AWS resource configurations. It also lets you
  automate the evaluation of recorded conﬁgurations against desired conﬁgurations.
- [AWS Systems Manager](https://aws.amazon.com/systems-manager "https://aws.amazon.com/systems-manager") gives you visibility
  and control of your infrastructure on AWS. Systems Manager provides a unified user
  interface so you can view operational data from multiple AWS services,
  investigate and resolve operational issues through OpsCenter and Incident Manager, and
  automate operational tasks across your AWS resources.
- [AWS Security Hub](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc "https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc") gives you a comprehensive view of your security alerts and
  security posture across your AWS accounts. With AWS Security Hub, there is a
  single place that aggregates, organizes, and prioritizes your security alerts, or
  findings.
- [AWS Health](../../../health.md "../../../health.md")
  provides personalized information about events that can affect your AWS infrastructure,
  guides you through scheduled changes, and accelerates the troubleshooting of issues that
  affect your AWS resources and accounts.
- [Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") provides multiple
  tooling mechanisms, people, and programs designed to proactively help you optimize
  performance, lower costs, and innovate faster. Support enables you to be successful on
  your cloud journey. It addresses requests that range from answering best practices
  questions to providing guidance on configuration and break-fix and problem
  resolution.
- [ServiceNow](https://www.servicenow.com/ "https://www.servicenow.com/") is an enterprise service
  management platform that places a service-oriented lens on the activities, tasks, and
  processes that enable day-to-day work life and a modern work environment. [ServiceNow Service Catalog](https://www.servicenow.com/products/it-service-automation-applications/service-catalog.html "https://www.servicenow.com/products/it-service-automation-applications/service-catalog.html") is a self-service application that end users can
  use to order IT services based on request fulfillment approvals and workflows. The
  [ServiceNow CMDB](https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/product/configuration-management/concept/c_ITILConfigurationManagement.html "https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/product/configuration-management/concept/c_ITILConfigurationManagement.html") provides resource transparency and relationships for the
  logical components of a service.
