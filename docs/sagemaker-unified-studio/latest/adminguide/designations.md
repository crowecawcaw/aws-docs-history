

# Designations

Designations are named permission sets that control which actions members can perform at the project level in Amazon SageMaker Unified Studio. The permissions in a designation are specific Amazon DataZone API actions that members can perform. You can use designations to define granular access controls for project members without modifying IAM policies. You can also optionally configure a layout customization for a designation to control which tools and pages appear in the left navigation pane of the Amazon SageMaker Unified Studio portal. Amazon SageMaker Unified Studio provides two types of designations:
+ **Managed designations** – AWS managed designations (Owner and Contributor) that you can't edit or delete. These designations provide baseline permission sets for common project roles.
+ **Custom designations** – Designations that domain administrators create to define specific permission sets for their organization. You can tailor these designations to match your organization's access control requirements.

![Designations overview in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/Designations-Main.png)


Designations use Cedar policy language to define permissions. Each project member has one designation through direct assignment. Members can also inherit additional designations through group membership. When a member has multiple designations, the member receives the union of all permission sets. Designations are available in all AWS Regions where Amazon SageMaker Unified Studio is available.

**Topics**
+ [How designations work](#how-designations-work)
+ [Controlling the user interface layout](#control-ui-layout)
+ [Designations and AWS Identity and Access Management](#designations-and-iam)
+ [Considerations](#designations-considerations)
+ [Create designations](create-designations.md)
+ [Assign designations](assign-designations.md)
+ [Edit designations](edit-designations.md)
+ [Delete designations](delete-designations.md)
+ [Designation permissions](designation-permissions.md)
+ [Example designations](example-designations.md)

## How designations work
<a name="how-designations-work"></a>

The following describes how designations work in Amazon SageMaker Unified Studio:

1. A domain administrator creates a designation by selecting permissions, such as publishing assets, creating data products, or approving subscriptions.

1. Optionally, the domain administrator configures a layout customization for the designation to control which tools and pages appear in the left navigation pane of the Amazon SageMaker Unified Studio portal.

1. Within a project, the project owner assigns one designation to each member (IAM role, IAM user, SSO user, or SSO group).

1. When a member performs an action through the portal or API, Amazon SageMaker Unified Studio evaluates the assigned designation and permits or denies the action based on the permissions it contains.

1. Because designations are defined once at the domain level and assigned per project, organizations get consistent permission enforcement across every project.

## Controlling the user interface layout
<a name="control-ui-layout"></a>

Beyond controlling permissions, each designation can include one layout customization. A layout customization controls which tools and pages appear in the left navigation pane of the Amazon SageMaker Unified Studio portal for members who have that designation, so you can tailor the portal to a persona or role. A layout customization changes only what members see in the portal; it doesn't grant or restrict the permissions and API access that the designation defines. Hiding a tool removes it from the navigation pane, but members can still perform the underlying actions through the API if their designation permits them. A layout customization is optional, and each designation can have at most one. Both managed designations (Owner and Contributor) and custom designations can have a layout customization. You configure layout customizations only in the Amazon SageMaker Unified Studio domain management portal. If a designation has no layout customization, members who have it see the full default left navigation pane, including any new navigation links that are later added to the portal.

**Note**  
The API and AWS CLI don't support layout customizations.

The following image shows an example layout customization for a designation. It shows which navigation items are selected to appear in the left navigation pane of the Amazon SageMaker Unified Studio portal for members who have the designation.

![Layout customization for a designation, showing the navigation items that are selected to appear in the left navigation pane of the Amazon SageMaker Unified Studio portal](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/ui-customization-detail.png)


## Designations and AWS Identity and Access Management
<a name="designations-and-iam"></a>

Designations work alongside IAM to provide layered access control. The following describes how these two authorization layers interact:
+ IAM evaluates whether a principal can invoke a DataZone or SageMaker operation at the AWS API boundary.
+ Designations evaluate whether the user's assigned permission set grants the specific action within the project.
+ Both layers must allow an action for it to succeed. An IAM Deny statement blocks the action regardless of the user's designation permissions.
+ You don't need to modify existing IAM policies to use designations.

## Considerations
<a name="designations-considerations"></a>

The following considerations and limitations apply to custom designations in Amazon SageMaker Unified Studio.
+ **Notifications** – Members with a custom designation receive the same project notifications as the Contributor managed designation. As a result, they might see notifications for events that they can't act on. They might also miss notifications that go only to project owners. Members can still perform any action their designation permits in the portal.
+ **Amazon QuickSight** – In projects that use the Amazon QuickSight blueprint, members with a custom designation receive viewer access to QuickSight folders, regardless of the designation's other permissions. Only the managed Owner and Contributor designations receive QuickSight contributor access, which includes permissions to create subfolders and assign members to folders. A QuickSight administrator can grant additional folder permissions directly in the QuickSight console.
+ **Domain support** – You can use custom designations only for projects in V2 domains. V1 domains don't support custom designations.
+ **Administration project** – You can't create or assign custom designations in a domain's admin project. Admin projects use managed designations, because admin project members are domain administrators.
+ **Permission scope** – Custom designations support a predefined set of permissions. You can't add permissions for API actions that aren't in this set. See [Custom designation permissions](designation-permissions.md#custom-designation-permissions) for the full set of permissions.
+ **Data sources** – Only IAM authorizes DataSource APIs. Designations don't support Cedar authorization for data sources.
+ **Required actions** – When you create a custom designation, you must include the Data Agent actions; you can't exclude them. The user interface adds these actions automatically. When you create a designation with the API, validation confirms these permissions are set. See [Custom designation permissions](designation-permissions.md#custom-designation-permissions) for the full set of permissions.
+ **Notebooks and Querybooks** – The new Query Editor is built on notebooks, and notebook permissions govern both. As a result, applying permissions to notebooks also applies them to querybooks.
+ **Associated accounts** – When you work from an associated domain and perform actions such as enabling the Tooling blueprint and authorizing domain units to use it, or when you authorize use for any non-Tooling blueprint, the AWS Resource Access Manager (AWS RAM) managed permissions must meet the following minimum versions:
  + `AWSRAMPermissionAmazonDataZoneDomainFullAccessWithPortalAccess` – Minimum version v8
  + `AWSRAMPermissionsAmazonDatazoneDomainExtendedServiceAccess` – Minimum version v11
  + `AWSRAMPermissionsAmazonDatazoneDomainExtendedServiceWithPortalAccess` – Minimum version v9
  + `AWSRAMDefaultPermissionAmazonDataZoneDomain` – Minimum version v11