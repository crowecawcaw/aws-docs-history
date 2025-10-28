AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# What are AWS service views

AWS service views are pre-defined views (cannot be modified or deleted) that enable
controlled resource data access by AWS service teams. AWS Resource Explorer is a platform service
that other service teams can take a dependency on to provide value-added services to
customers, while providing access and usage transparency to customers. Service views
represent one of three integration patterns (user views, AWS managed views, and AWS
service views) that other AWS services can use to integrate with Resource Explorer.

There are two types of service views:

- **Resource Explorer-defined service views:** Used by Resource Explorer
  itself to power features like the default search functionality.
- **Service-defined service views:** Created by an
  AWS service during onboarding to access specific resource data. Customers cannot
  use this view directly to view resources.

## Key characteristics of service

views

AWS service views have the following key characteristics:

**Service-defined service view**

Service views are created during AWS service onboarding and cannot be
modified or deleted by customers.

**Pre-defined configuration**

Service views include specific filters and properties defined during
service onboarding to meet the service's integration requirements.

**Global availability**

Service views are automatically available to authorized callers without
setup as a global resource.

## How service views work

Service views support two primary use cases:

- **Search and discovery**:
  - **Resource Explorer-defined service views**:
    Customers can use this view to discover resources in the default search
    functionality.
  - **Service-defined service views**:
    Services can search for customer resources with customer
    credentials.

- **Resource streaming:** Services receive
  real-time resource change notifications through event streams

Customers can manage service views through the following actions:

Customer opt-in is required for streaming access through service views. Customers must
explicitly grant permission through the Resource Explorer
`CreateStreamingAccessForService` API action.
AWS services
must create their own service views and can only use the service views they have
created.

## Customer experience

Customers can manage service views through the following actions:

### Viewing available service views

**How can customers see what service views
exist?**

Customers can view all available service views by using the
`ListServiceViews` API action. This API action returns a list of all
service views that are available in their account, including both Resource Explorer-defined and
service-defined views. The response includes the view name, ARN, and configuration
details.

### Monitoring service access

**How can customers see which services currently have
access?**

Customers can monitor which services have streaming access to their resources by
using the `ListStreamingAccessForServices` API action. This action
provides a complete list of all services that are currently authorized to receive
resource updates, allowing customers to maintain visibility over their resource data
sharing.

## Permissions and security

Service views maintain strong security controls:

- **Customer control:** Customers retain control
  over which services can access their resources (resource streaming only)
  - **Service-linked role-based access
    limitations:** When AWS services use SLRs with Resource Explorer
    permissions, customers must accept the predefined permissions or choose
    not to use the service
  - **Customer options:** To revoke
    Search\*/List\* access granted through SLRs, customers must disable the
    entire service integration

- **IAM integration:** Works with existing IAM
  policies and Resource Explorer permissions
- **Service principal allowlisting:** Only
  pre-approved AWS services can create and use service views

## Related topics

- [Configuring a Resource Explorer view to provide access to
  resource searches](customer-views.md#configure-views "customer-views.md#configure-views")
- [Identity and access management for AWS Resource Explorer](security_iam.md "security_iam.md")
- [Terms and concepts for Resource Explorer](getting-started-terms-and-concepts.md "getting-started-terms-and-concepts.md")
