# Create a ROSA classic cluster using the ROSA CLI

The following sections describe how to get started with ROSA classic using AWS STS and the ROSA CLI.
For steps to create a ROSA classic cluster using Terraform, see [the Red Hat documentation](https://docs.openshift.com/rosa/rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.html "https://docs.openshift.com/rosa/rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.html"). To learn more about the Terraform provider for creating ROSA clusters, see [the Terraform documentation](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs "https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs").

The ROSA CLI uses `auto` mode or `manual` mode to create the IAM resources required to provision a ROSA
cluster.
`auto` mode immediately creates the required IAM roles and policies and an OpenID Connect (OIDC) provider. `manual` mode outputs the AWS CLI commands that are needed to create the IAM resources.
By using `manual` mode, you can review the generated AWS CLI commands before running them manually.
With `manual` mode, you can also pass the commands to another administrator or group in your organization so they can create the resources.

For more options to get started, see [Get started with ROSA](getting-started.md "getting-started.md").

###### Topics

- [Prerequisites](#getting-started-classic-cli-prereqs "#getting-started-classic-cli-prereqs")
- [Create a ROSA classic cluster using the ROSA CLI and AWS STS](#create-rosa-classic-cluster-cli-sts "#create-rosa-classic-cluster-cli-sts")
- [Configure an identity provider and grant cluster access](#getting-started-classic-cli-configure-oidc "#getting-started-classic-cli-configure-oidc")
- [Grant user access to a cluster](#getting-started-classic-cli-grant-user-access "#getting-started-classic-cli-grant-user-access")
- [Configure cluster-admin permissions](#configure-cluster-admin-classic-cli "#configure-cluster-admin-classic-cli")
- [Configure dedicated-admin permissions](#configure-dedicated-admin-classic-cli "#configure-dedicated-admin-classic-cli")
- [Access a cluster through the Red Hat Hybrid Cloud Console](#console-access-classic-cli "#console-access-classic-cli")
- [Deploy an application from the Developer Catalog](#deploy-app-classic-cli "#deploy-app-classic-cli")
- [Revoke cluster-admin permissions from a user](#revoke-cluster-admin-classic-cli "#revoke-cluster-admin-classic-cli")
- [Revoke dedicated-admin permissions from a user](#revoke-dedicated-admin-classic-cli "#revoke-dedicated-admin-classic-cli")
- [Revoke user access to a cluster](#revoke-user-classic-cli "#revoke-user-classic-cli")
- [Delete a cluster and AWS STS resources](#delete-cluster-classic-cli "#delete-cluster-classic-cli")

## Prerequisites

Complete the prerequisite actions listed in [Set up to use ROSA](set-up.md "set-up.md").

## Create a ROSA classic cluster using the ROSA CLI and AWS STS

You can create a ROSA classic cluster using the ROSA CLI and AWS STS.

1. Create the required IAM account roles and policies using `--mode auto` or `--mode manual`.
   - ```
     rosa create account-roles --classic --mode auto
     ```

   ````
   * ```
    rosa create account-roles --classic --mode manual
   ````

   ###### Note

   If your offline access token has expired, the ROSA CLI outputs an error message stating that your authorization token needs updated. For steps to troubleshoot, see [Troubleshoot ROSA CLI expired offline access tokens](troubleshooting-rosa.md#rosa-cli-expired-token "troubleshooting-rosa.md#rosa-cli-expired-token").

2. Create a cluster using `--mode auto` or `--mode manual`. `auto` mode allows you to create a cluster more quickly. `manual` mode prompts you to specify custom settings for your cluster.
   - ```
     rosa create cluster --cluster-name <CLUSTER_NAME> --sts --mode auto
     ```

   ````

   ###### Note

   When you specify `--mode auto`, the `rosa create cluster` command creates the cluster-specific operator IAM roles and the OIDC provider automatically. The operators use the OIDC provider to authenticate.


   ###### Note

   When using the `--mode auto` defaults, the latest stable OpenShift version is installed.
   * ```
    rosa create cluster --cluster-name <CLUSTER_NAME> --sts --mode manual
   ````

   ###### Important

   If you enable etcd encryption in `manual` mode, you incur a performance overhead of approximately 20%.
   The overhead is a result of introducing this second layer of encryption, in addition to the default Amazon EBS encryption that encrypts the etcd volumes.

   ###### Note

   After running `manual` mode to create the cluster, you need to manually create cluster-specific operator IAM roles and the OpenID Connect provider that cluster operators use to authenticate.

3. Check the status of your cluster.

```
 rosa describe cluster -c <CLUSTER_NAME>
```

###### Note

If the provisioning process fails or the `State` field doesn’t change to a ready status after 40 minutes, see [Troubleshooting](troubleshooting-rosa.md "troubleshooting-rosa.md").
To contact Support or Red Hat support for assistance, see [Getting ROSA support](rosa-support.md "rosa-support.md"). 4. Track the progress of the cluster creation by watching the OpenShift installer logs.

```
 rosa logs install -c <CLUSTER_NAME> --watch
```

## Configure an identity provider and grant cluster access

ROSA includes a built-in OAuth server.
After your cluster is created, you must configure OAuth to use an identity provider.
You can then add users to your configured identity provider to grant them access to your cluster.
You can grant these users `cluster-admin` or `dedicated-admin` permissions as required.

You can configure different identity provider types for your ROSA
cluster.
Supported types include GitHub, GitHub Enterprise, GitLab, Google, LDAP, OpenID Connect, and HTPasswd identity providers.

###### Important

The HTPasswd identity provider is included only to enable a single, static administrator user to be created. HTPasswd isn’t supported as a general-use identity provider for ROSA.

The following procedure configures a GitHub identity provider as an example.
For instructions on how to configure each of the supported identity provider types, see [Configuring identity providers for AWS STS](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/install_rosa_classic_clusters/rosa-sts-config-identity-providers "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/install_rosa_classic_clusters/rosa-sts-config-identity-providers").

1. Navigate to [github.com](https://github.com/ "https://github.com/") and log in to your GitHub account.
2. If you don’t have a GitHub organization to use for identity provisioning for your cluster, create one.
   For more information, see [the steps in the GitHub documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch "https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch").
3. Using the ROSA CLI’s interactive mode, configure an identity provider for your cluster.

```
 rosa create idp --cluster=<CLUSTER_NAME> --interactive
```

4. Follow the configuration prompts in the output to restrict cluster access to members of your GitHub organization.

```
 I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Type of identity provider: github
? Identity provider name: github-1
? Restrict to members of: organizations
? GitHub organizations: <GITHUB_ORG_NAME>
? To use GitHub as an identity provider, you must first register the application:
  - Open the following URL:
    https://github.com/organizations/<GITHUB_ORG_NAME>/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.<CLUSTER_NAME>/<RANDOM_STRING>.p1.openshiftapps.com%2Foauth2callback%2Fgithub-1&oauth_application%5Bname%5D=<CLUSTER_NAME>&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.<CLUSTER_NAME>/<RANDOM_STRING>.p1.openshiftapps.com
  - Click on 'Register application'
...
```

5. Open the URL in the output, replacing `<GITHUB_ORG_NAME>` with the name of your GitHub organization.
6. On the GitHub web page, choose **Register application** to register a new OAuth application in your GitHub organization.
7. Use the information from the GitHub OAuth page to populate the remaining `rosa create idp` interactive prompts by running the following command.
   Replace `<GITHUB_CLIENT_ID>` and `<GITHUB_CLIENT_SECRET>` with the credentials from your GitHub OAuth application.

```
 ...
? Client ID: <GITHUB_CLIENT_ID>
? Client Secret: [? for help] <GITHUB_CLIENT_SECRET>
? GitHub Enterprise Hostname (optional):
? Mapping method: claim
I: Configuring IDP for cluster '<CLUSTER_NAME>'
I: Identity Provider 'github-1' has been created.
   It will take up to 1 minute for this configuration to be enabled.
   To add cluster administrators, see 'rosa grant user --help'.
   To login into the console, open https://console-openshift-console.apps.<CLUSTER_NAME>.<RANDOM_STRING>.p1.openshiftapps.com and click on github-1.
```

###### Note

It might take approximately two minutes for the identity provider configuration to become active.
If you configured a `cluster-admin` user, you can run `oc get pods -n openshift-authentication --watch` to watch the OAuth pods redeploy with the updated configuration. 8. Verify that the identity provider is configured correctly.

```
 rosa list idps --cluster=<CLUSTER_NAME>
```

## Grant user access to a cluster

You can grant a user access to your cluster by adding them to the configured identity provider.

The following procedure adds a user to a GitHub organization that’s configured for identity provisioning to the cluster.

1. Navigate to [github.com](https://github.com/ "https://github.com/") and log in to your GitHub account.
2. Invite users that require cluster access to your GitHub organization.
   For more information, see [Inviting users to join your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization "https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization") in the GitHub documentation.

## Configure `cluster-admin` permissions

1. Grant the `cluster-admin` permissions by running the following command.
   Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name.

```
 rosa grant user cluster-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user is listed as a member of the `cluster-admins` group.

```
 rosa list users --cluster=<CLUSTER_NAME>
```

## Configure `dedicated-admin` permissions

1. Grant the `dedicated-admin` permissions by using the following command.
   Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name by running the following command.

```
 rosa grant user dedicated-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user is listed as a member of the `cluster-admins` group.

```
 rosa list users --cluster=<CLUSTER_NAME>
```

## Access a cluster through the Red Hat Hybrid Cloud Console

After you create a cluster administrator user or added a user to your configured identity provider, you can log in to your cluster through the Red Hat Hybrid Cloud Console.

1. Obtain the console URL for your cluster using the following command.
   Replace `<CLUSTER_NAME>` with the name of your cluster.

```
 rosa describe cluster -c <CLUSTER_NAME> | grep Console
```

2. Navigate to the console URL in the output and log in.
   - If you created a `cluster-admin` user, log in using the provided credentials.
   - If you configured an identity provider for your cluster, choose the identity provider name in the **Log in with…​** dialog and complete any authorization requests presented by your provider.

## Deploy an application from the Developer Catalog

From the Red Hat Hybrid Cloud Console, you can deploy a Developer Catalog test application and expose it with a route.

1. Navigate to [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift "https://console.redhat.com/openshift") and choose the cluster you want to deploy the app into.
2. On the cluster’s page, choose **Open console**.
3. In the **Administrator** perspective, choose **Home** > **Projects** > **Create Project**.
4. Enter a name for your project and optionally add a **Display Name** and **Description**.
5. Choose **Create** to create the project.
6. Switch to the **Developer** perspective and choose **+Add**.
   Make sure that the selected project is the one that was just created.
7. In the **Developer Catalog** dialog, choose **All services**.
8. In the **Developer Catalog** page, choose **Languages** > **JavaScript** from the menu.
9. Choose **Node.js**, and then choose **Create Application** to open the **Create Source-to-Image Application** page.

###### Note

You might need to choose **Clear All Filters** to display the **Node.js** option. 10. In the **Git** section, choose **Try Sample**. 11. In the **Name** field, add a unique name. 12. Choose **Create**.

###### Note

The new application takes several minutes to deploy. 13. When the deployment is complete, choose the route URL for the application.

A new tab in the browser opens with a message that’s similar to the following.

```
 Welcome to your Node.js application on OpenShift
```

14. (Optional) Delete the application and clean up resources:
    1.  In the **Administrator** perspective, choose **Home** > **Projects**.
    2.  Open the action menu for your project and choose **Delete Project**.

## Revoke `cluster-admin` permissions from a user

1. Revoke the `cluster-admin` permissions using the following command.
   Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name.

```
 rosa revoke user cluster-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user isn’t listed as a member of the `cluster-admins` group.

```
 rosa list users --cluster=<CLUSTER_NAME>
```

## Revoke `dedicated-admin` permissions from a user

1. Revoke the `dedicated-admin` permissions by using the following command.
   Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name.

```
 rosa revoke user dedicated-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user isn’t listed as a member of the `dedicated-admins` group.

```
 rosa list users --cluster=<CLUSTER_NAME>
```

## Revoke user access to a cluster

You can revoke cluster access for an identity provider user by removing them from the configured identity provider.

You can configure different types of identity providers for your cluster.
The following procedure revokes cluster access for a member of a GitHub organization.

1. Navigate to [github.com](https://github.com/ "https://github.com/") and log in to your GitHub account.
2. Remove the user from your GitHub organization.
   For more information, see [Removing a member from your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization "https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization") in the GitHub documentation.

## Delete a cluster and AWS STS resources

You can use the ROSA CLI to delete a cluster that uses AWS Security Token Service (AWS STS).
You can also use the ROSA CLI to delete the IAM roles and OIDC provider created by ROSA.
To delete the IAM policies created by ROSA, you can use the IAM console.

###### Important

IAM roles and policies created by ROSA might be used by other ROSA clusters in the same account.

1. Delete the cluster and watch the logs.
   Replace `<CLUSTER_NAME>` with the name or ID of your cluster.

```
 rosa delete cluster --cluster=<CLUSTER_NAME> --watch
```

###### Important

You must wait for the cluster to delete completely before you remove the IAM roles, policies, and OIDC provider.
The account IAM roles are required to delete the resources created by the installer.
The operator IAM roles are required to clean up the resources created by the OpenShift operators.
The operators use the OIDC provider to authenticate. 2. Delete the OIDC provider that the cluster operators use to authenticate by running the following command.

```
 rosa delete oidc-provider -c <CLUSTER_ID> --mode auto
```

3. Delete the cluster-specific operator IAM roles.

```
 rosa delete operator-roles -c <CLUSTER_ID> --mode auto
```

4. Delete the account IAM roles using the following command.
   Replace `<PREFIX>` with the prefix of the account IAM roles to delete.
   If you specified a custom prefix when creating the account IAM roles, specify the default `ManagedOpenShift` prefix.

```
 rosa delete account-roles --prefix <PREFIX> --mode auto
```

5. Delete the IAM policies created by ROSA.
   1. Log in to the [IAM console](https://console.aws.amazon.com/iamv2/home#/home "https://console.aws.amazon.com/iamv2/home#/home").
   2. On the left menu under **Access management**, choose **Policies**.
   3. Select the policy that you want to delete and choose **Actions** > **Delete**.
   4. Enter the policy name and choose **Delete**.
   5. Repeat this step to delete each of the IAM policies for the cluster.
