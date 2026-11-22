

# Integrate HyperPod clusters with Active Directory

With the `ldap` source, the user management extension connects every node to an Active Directory directory over LDAP over TLS/SSL (LDAPS) through SSSD. For more information about LDAP, see [Lightweight Directory Access Protocol (LDAP)](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) on Wikipedia. Directory users log in with their directory identity, and you manage them and their group membership in the directory. The extension doesn't create local accounts for directory users.

Use the `ldap` source when you already manage identities centrally, or when you have more users than fit in the configuration. You can use it by itself, or together with `localUsers`.

If you don't have a directory yet, follow the directory steps in the blog post [Integrate HyperPod clusters with Active Directory for seamless multi-user login](https://aws.amazon.com/blogs/machine-learning/integrate-hyperpod-clusters-with-active-directory-for-seamless-multi-user-login/), and then configure the cluster with the extension instead of the blog's lifecycle scripts.

## Prerequisites
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-prerequisites"></a>
+ **An LDAPS endpoint:** An Active Directory directory with LDAPS turned on, such as [AWS Directory Service for Microsoft Active Directory](https://aws.amazon.com/directoryservice/), that every node can reach on port 636 or the port in your URI. Use a DNS name that matches the directory's LDAPS certificate.

  You can reach the directory through its domain controllers' own LDAPS, directly or through a transit gateway, or through a Network Load Balancer with a TLS listener. We recommend the domain controllers' own LDAPS. In `ldapUri`, list the domain name first, then up to three domain controllers by name. Plan for about one domain controller per 1,000 nodes, and make sure that each controller's certificate names both the domain and the controller.
+ **A dedicated bind account:** A read-only service account in the directory that SSSD uses to look up users and groups. Use it only for this cluster. For the requirements, see the Important note after this list.
+ **Two secrets:** Two AWS Secrets Manager secrets in the same Region as the cluster. One holds the bind account's password as plain text, not as key-value pairs. The other holds, as plain text, the PEM certificate of the CA that signed the directory's LDAPS certificate.
+ **Execution role permissions:** The execution role of every instance group needs `secretsmanager:GetSecretValue` on both secrets, as in the following policy. If the secrets use a customer managed AWS Key Management Service (AWS KMS) key, also allow `kms:Decrypt` on that key. In private subnets without internet access, create an interface VPC endpoint for `com.amazonaws.{{region}}.secretsmanager`, or route through a NAT gateway.

  ```json
  {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadDirectorySecrets",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": [
        "arn:aws:secretsmanager:{{us-west-2}}:{{111122223333}}:secret:{{ad-readonly-AbCdEf}}",
        "arn:aws:secretsmanager:{{us-west-2}}:{{111122223333}}:secret:{{ldaps-ca-GhIjKl}}"
      ]
    }
  ]
  }
  ```

  Replace the {{replaceable}} values with your AWS Region, account ID, and secret names.
+ **SSH public keys:** For public key login, which is the default, each user's SSH public key is stored in the directory attribute that `ldapUserSshPublicKey` names. The default attribute is `altSecurityIdentities`. The `sshPublicKey` attribute requires an Active Directory schema extension.

**Note**  
**Important: The bind password is readable on your cluster's nodes**  
Anyone who can log in to the cluster can read the bind password, because the extension reads it with the execution role, and every user on the cluster can use that role's credentials. Use a dedicated bind account: one that only this cluster uses, with read-only access scoped to the organizational units that the cluster needs. Never use an administrator account, or any account that can modify the directory. Rotate the password periodically, and right away if you suspect exposure. Scope `GetSecretValue` to the exact ARNs of the two secrets, without wildcards.

You can create the secrets with the AWS CLI, as in the following example.

```
aws secretsmanager create-secret --name {{ad-readonly}} \
    --secret-string file://{{bind-password.txt}}
aws secretsmanager create-secret --name {{ldaps-ca}} \
    --secret-string file://{{ldaps-ca.pem}}
```

## Example configuration
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-example-configuration"></a>

In the following example, replace the {{replaceable}} values with your directory URI, search base, bind DN, secret ARNs, and group names.

```json
{
  "userSources": {
    "ldap": {
      "ldapUri": ["ldaps://{{ad.example.com}}"],
      "ldapSearchBase": "{{dc=example,dc=com}}",
      "ldapDefaultBindDn": "{{CN=ReadOnly,OU=Users,DC=example,DC=com}}",
      "ldapDefaultAuthtokSecretArn": "arn:aws:secretsmanager:{{us-west-2}}:{{111122223333}}:secret:{{ad-readonly-AbCdEf}}",
      "ldapTlsCacertSecretArn": "arn:aws:secretsmanager:{{us-west-2}}:{{111122223333}}:secret:{{ldaps-ca-GhIjKl}}",
      "domain": "{{example.com}}",
      "useFullyQualifiedNames": "ENABLED",
      "sharedFilesystemMount": "/fsx",
      "ldapGroups": [
        { "name": "{{ClusterAdmin@example.com}}",
          "ssh":  [ { "nodeTypes": ["controller", "login", "compute"] } ],
          "sudo": [ { "nodeTypes": ["controller", "login", "compute"] } ] },
        { "name": "{{hpc-users@example.com}}",
          "ssh":  [ { "nodeTypes": ["login", "compute"] } ] }
      ]
    }
  }
}
```

Any directory user under `dc=example,dc=com` resolves on every node. `ClusterAdmin` members can log in to every node and have sudo everywhere. `hpc-users` members can log in to login and compute nodes, without sudo. Other directory users can't log in over SSH.

## How directory login works
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-how-directory-login-works"></a>
+ **Resolving isn't logging in:** Any directory user in the search base resolves, but can log in over SSH only through an `ldapGroups` entry whose `ssh` targets include the node's type. No group has access by default, including `ClusterAdmin` and `ClusterDev`, which had access with the base lifecycle scripts.
+ **No enumeration:** `getent passwd` without a name doesn't list directory users. Look them up by name.
+ **Slurm associations:** Directory users don't get them. If you set `AccountingStorageEnforce=associations`, add them with `sacctmgr` on the controller node.
+ **Group membership:** When you add a user to a directory group, the user gets the group's access after SSSD refreshes its cache. You don't need to update the extension.

## Choosing settings
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-choosing-settings"></a>
+ **`useFullyQualifiedNames`:** Set `ENABLED` if you also use `localUsers` or have unmanaged local accounts, so that directory names, including `ldapGroups` names, end with `@{{domain}}` and can't take a local account's name.
+ **`ldapIdMapping`:** Keep `ENABLED` unless other systems depend on the directory's `uidNumber` and `gidNumber`. Never change it later; it renumbers every directory user.
+ **`sshAuthMethod`:** Keep `PUBLIC_KEY`. `PASSWORD` turns on SSH password authentication for every user on the node.
+ **`sharedFilesystemMount`:** Set it once. Changing it gives directory users new, empty home directories.

**Note**  
Applying the `ldap` source removes the `ec2-instance-connect` package from every node, so Amazon EC2 Instance Connect stops working, and the package isn't reinstalled later. Use SSM or SSH to connect. It also replaces any SSSD configuration on the nodes, including one from `enable_sssd`, and removing the `ldap` source doesn't restore it.

After you install or update the extension with the `ldap` source, check the connection on a node.

```
$ sudo sssctl domain-status {{example.com}}
$ id {{user-1@example.com}}
```

If the status becomes `CreateFailed` or `UpdateFailed`, Health names the problem. For more information, see [Troubleshooting](sagemaker-hyperpod-slurm-user-management-manage.md#sagemaker-hyperpod-slurm-user-management-manage-troubleshooting).

## Changing the directory configuration
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-changing-the-directory-configuration"></a>

Send only the settings that change. Lists such as `ldapUri` and `ldapGroups` replace the whole list, so to add a group, send the complete `ldapGroups` list, including the groups that you already have. To change who is in a group, change its membership in the directory. You don't need to update the extension.

The extension reads both secrets when it applies the configuration to a node. After you rotate a secret, update the extension to apply the new value to existing nodes.

## Removing the directory
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-removing-the-directory"></a>

To remove the directory integration, set the `ldap` source to `null`.

```json
{ "userSources": { "ldap": null } }
```

Every node removes the SSSD directory configuration, the CA certificate, and the directory groups' SSH and sudo rules, and directory users can no longer log in. Their home directories stay on the shared file system, and `ec2-instance-connect` isn't reinstalled.

## Using local users and Active Directory together
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-using-local-users-and-active-directory-together"></a>

You can combine a few local administrators, who don't depend on the directory, with directory users for everyone else. Add a `localUsers` source next to the `ldap` source, and set `useFullyQualifiedNames` to `ENABLED`.

With `useFullyQualifiedNames` set to `ENABLED`, a directory user named `admin-1` appears as `admin-1@example.com` and doesn't conflict with the local `admin-1`. You can update either source without sending the other.

## Moving a directory setup from the base lifecycle scripts
<a name="sagemaker-hyperpod-slurm-user-management-active-directory-moving-a-directory-setup-from-the-base-lifecycle-scripts"></a>

If your cluster joins the directory through `enable_sssd = True` in the base lifecycle scripts, see [Move a directory setup from the base lifecycle scripts](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-move-a-directory-setup-from-the-base-lifecycle-scripts).