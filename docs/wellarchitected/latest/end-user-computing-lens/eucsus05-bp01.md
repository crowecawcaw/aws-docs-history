# EUCSUS05-BP01 Optimize machine image creation, copying, and sharing to each environment (like development, testing, and production)

Using automation with machine images facilitates scalability and
elasticity, minimizing over-provisioning and associated energy
consumption. Centralized management and compliance reporting
further support sustainability initiatives. Overall, automation
pipelines contribute to lower environmental impact and improved
resource optimization.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Use a dedicated and separate account to create your Amazon AppStream images to manage your
changes and your image history. Push the image (copy or share) with other development or
production AWS accounts. For more detail, see [UpdateImagePermissions](../../../appstream2/latest/APIReference/API_UpdateImagePermissions.md "../../../appstream2/latest/APIReference/API_UpdateImagePermissions.md") and [UpdateWorkspaceImagePermission](../../../workspaces/latest/api/API_UpdateWorkspaceImagePermission.md "../../../workspaces/latest/api/API_UpdateWorkspaceImagePermission.md").
