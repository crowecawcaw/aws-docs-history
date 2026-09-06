

# Assign authorization policies to asset types
<a name="assign-authorization-policies-to-asset-types"></a>

In Amazon SageMaker Unified Studio, asset types define how assets are represented in the Amazon SageMaker catalog. An asset type defines the schema for a specific type of asset. You can complete the following procedure to assign authorization policies to asset types. Only domaint unit owners and project owners can edit asset types' usage permissions. Project contributors can view asset type usage permissions but they cannot edit them.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your administrator and log in using your SSO or AWS credentials. 

1. In the left navigation pane, choose **Manage**, then under **Domain management**, choose **Asset types**.

1. Choose an existing asset type and then choose the **Permissions** tab.

1. Choose **Add usage permission**, and in the **Add projects and designations** pop up window, specify the authorized projects (you can choose **Select projects in a domain unit** or **All project in a domain unit**), the specific domain unit, and the allowed designations - which designations a project member must have to use this policy. You can choose **Owner** or **Contributor**.

1. Choose Add policy grant to save the changes and complete modifying the asset type usage permissions.