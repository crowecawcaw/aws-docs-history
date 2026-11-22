

# Managing knowledge bases in Quick

This section describes how you can manage access controls, secure your data, and maintain knowledge bases throughout their lifecycle.

## Sharing and access control
<a name="managing-knowledge-bases-sharing-and-access-control"></a>

The following section describes how you can control access to your knowledge bases and share them with other users in your organization.

Quick provides Entity-Level Access Control (ELAC) to help you manage permissions for your knowledge bases.

### Configuring Entity-Level Access Control
<a name="managing-knowledge-bases-configuring-entity-level-access-control"></a>

The following procedure shows you how to configure Entity-Level Access Control for your knowledge bases.

1. Open the AWS Quick console.

1. Choose **Customize**, and then choose **Knowledge**.

1. Choose the knowledge base that you want to update.

1. Choose the **Actions** dropdown menu and choose **Edit**.

1. Choose **Permissions**.

1. Choose **Add users & groups**.

1. For each user or group, add them to the knowledge base.

**Important**  
All users must have valid AWS Quick subscriptions before you can share knowledge bases with them.

## Permission Management
<a name="managing-knowledge-bases-permission-management"></a>

### Owner and Co-owner Capabilities
<a name="managing-knowledge-bases-owner-and-co-owner-capabilities"></a>

Owners and co-owners have full control over knowledge bases and can:
+ Edit knowledge base configuration
  + Modify sync settings
  + Update field mappings
  + Configure filters
+ Manage access controls
  + Add or remove users
  + Change permission levels
  + Configure inheritance settings
+ Delete knowledge bases
  + Remove from Spaces
  + Delete source connections
+ Configure sync settings
  + Set sync frequency
  + Define sync scope
  + Monitor sync status

### Viewer Capabilities
<a name="managing-knowledge-bases-viewer-capabilities"></a>

Viewers have read-only access and can:
+ Query knowledge base content through:
  + Chat interfaces
  + Agents
  + Quick dashboards
+ View knowledge base metadata
+ Access permitted content based on their permission level