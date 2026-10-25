

# Assign authorization policies to asset types
<a name="assign-authorization-policies-to-asset-types"></a>

Asset types define how the SageMaker catalog represents assets — an asset type defines the schema for a specific type of asset. Only domain unit owners and project members with adequate permissions can edit asset types. All other project members can view them but cannot edit them.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your administrator and log in using your SSO or AWS credentials. 

1. In the left navigation pane, choose **Manage**, then under **Catalog management**, choose **Custom asset types**.

1. Choose an existing asset type, then choose the **Permissions** tab.

1. Choose **Add usage permission**. In the **Add projects and designations** window, specify the authorized projects (**Select projects in a domain unit** or **All projects in a domain unit**), the specific domain unit, and the allowed designations — which designations a project member must have to use this policy.
**Note**  
The **Domain unit** dropdown appears only when the domain contains more than one domain unit.

1. Choose **Add policy grant** to save the changes.