

# AWS CodeConnections supported providers and versions
<a name="supported-versions-connections"></a>

This chapter provides information about the providers and versions that AWS CodeConnections supports.

**Topics**
+ [Supported provider type for Azure DevOps](#w2aab5c25c22b9)
+ [Supported provider type for Bitbucket](#supported-versions-connections-bitbucket)
+ [Supported provider type for GitHub and GitHub Enterprise Cloud](#supported-versions-connections-github)
+ [Supported provider type and versions for GitHub Enterprise Server](#supported-versions-connections-ghes)
+ [Supported provider type for GitLab.com](#supported-versions-connections-gitlab)
+ [Supported provider type for GitLab self-managed](#supported-versions-connections-gitlab-managed)

## Supported provider type for Azure DevOps
<a name="w2aab5c25c22b9"></a>

You can use the connections app with Azure DevOps. 

Installed (hosted) provider types, such as Azure Cloud Hosting, are not supported. 

## Supported provider type for Bitbucket
<a name="supported-versions-connections-bitbucket"></a>

You can use the connections app with Atlassian Bitbucket Cloud. 

Installed Bitbucket provider types, such as Bitbucket Server, are not supported. 

## Supported provider type for GitHub and GitHub Enterprise Cloud
<a name="supported-versions-connections-github"></a>

You can use the connections app with GitHub and GitHub Enterprise Cloud.

**Important**  
AWS CodeConnections does not yet support GitHub Enterprise Cloud with data residency (custom \*.ghe.com domains).

## Supported provider type and versions for GitHub Enterprise Server
<a name="supported-versions-connections-ghes"></a>

You can use the connections app with supported versions of GitHub Enterprise Server. For a list of supported versions, see [https://enterprise.github.com/releases/](https://enterprise.github.com/releases/).

**Important**  
AWS CodeConnections does not support deprecated GitHub Enterprise Server versions. For example, AWS CodeConnections does not support GitHub Enterprise Server version 2.22.0 due to a known issue in the release. To connect, upgrade to version 2.22.1 or the latest available version.

## Supported provider type for GitLab.com
<a name="supported-versions-connections-gitlab"></a>

You can use connections with GitLab.com. For more information, see [Create a connection to GitLab](connections-create-gitlab.md).

**Important**  
Connections support for GitLab includes version 15.x and later.

## Supported provider type for GitLab self-managed
<a name="supported-versions-connections-gitlab-managed"></a>

You can use connections with GitLab self-managed installation (for Enterprise Edition or Community Edition). For more information, see [Create a connection to GitLab self-managed](connections-create-gitlab-managed.md).