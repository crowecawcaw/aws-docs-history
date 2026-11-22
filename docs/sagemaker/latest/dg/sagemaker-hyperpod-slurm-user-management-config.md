

# User management extension configuration

You configure the user management extension with a JSON object that you pass in the `ConfigurationValues` parameter of `CreateClusterExtension` and `UpdateClusterExtension`. Setting names are case sensitive and use camel case. Unknown settings are rejected at every level. `userSources` is required, and every other setting is optional.

The following example shows where each setting goes. It isn't a valid configuration on its own.

```json
{
  "sharedFilesystemMount": "/fsx",
  "userSources": {
    "localUsers": {
      "sharedFilesystemMount": "/fsx",
      "groups":       [ { "name": "...", "gid": 3001, "ssh": [ ... ], "sudo": [ ... ] } ],
      "users":        [ { "username": "...", "uid": 2001, "groups": [ ... ], "homeDirectory": "...", "shell": "bash" } ],
      "deleteUsers":  [ { "username": "...", "uid": 2004 } ],
      "deleteGroups": [ { "name": "...", "gid": 3005 } ]
    },
    "ldap": {
      "ldapUri": [ "ldaps://..." ],
      "ldapSearchBase": "...",
      "ldapDefaultBindDn": "...",
      "ldapDefaultAuthtokSecretArn": "arn:aws:secretsmanager:...",
      "ldapTlsCacertSecretArn": "arn:aws:secretsmanager:...",
      "ldapSchema": "AD",
      "domain": "...",
      "ldapIdMapping": "ENABLED",
      "useFullyQualifiedNames": "DISABLED",
      "sshAuthMethod": "PUBLIC_KEY",
      "ldapUserSshPublicKey": "altSecurityIdentities",
      "sharedFilesystemMount": "/fsx",
      "ldapGroups": [ { "name": "...", "ssh": [ ... ], "sudo": [ ... ] } ]
    }
  }
}
```

## Top-level settings
<a name="sagemaker-hyperpod-slurm-user-management-config-top-level-settings"></a>


| Setting | Type | Default | Description | 
| --- | --- | --- | --- | 
| sharedFilesystemMount | String, up to 256 characters | "" | An absolute path to a shared file system that's mounted on every node, which holds home directories as {{mount}}/{{username}}, for example /fsx. An empty string means that the extension detects the mount. Each source can override this setting. | 
| userSources | Object | None (required) | The user sources, keyed by type: localUsers, ldap, both, or neither. {} is an empty user list. A configuration without userSources, such as {}, is rejected. | 

## How updates apply to user sources
<a name="sagemaker-hyperpod-slurm-user-management-config-how-updates-apply-to-user-sources"></a>

Updates use JSON merge patch, like every extension. The following list describes what this means for the user management extension:
+ **Objects merge:** A source that you leave out of an update keeps its current configuration, so you can update `ldap` without sending `localUsers` again. Within a source, settings are merged one at a time.
+ **Lists replace:** Every list replaces the current list, including `users`, `groups`, `deleteUsers`, `deleteGroups`, `ldapUri`, `ldapGroups`, `ssh`, `sudo`, and `nodeTypes`. To add one user, send the full `users` list with the new user.
+ **null resets:** A setting set to `null` returns to its default value. A source set to `null` is removed. For `localUsers`, the accounts that it created stay on the nodes. For `ldap`, every node removes the directory configuration.
+ **Removal is explicit:** Leaving a user or group out of a list doesn't delete it. The user keeps their account, home directory, Slurm associations, and SSH access until you list them in `deleteUsers`. A group stays until you list it in `deleteGroups`.

## localUsers
<a name="sagemaker-hyperpod-slurm-user-management-config-localusers"></a>

The `localUsers` source holds the accounts that the extension creates. Every list is optional.


| Setting | Type | Limits | Description | 
| --- | --- | --- | --- | 
| groups | Array of group objects | Up to 50 | The groups that this source owns, with their group IDs (GIDs) and the SSH and sudo access that they grant. | 
| users | Array of user objects | Up to 100 | The accounts to create on every node. | 
| sharedFilesystemMount | String | Up to 256 characters, absolute path | The mount for this source's home directories, for example /home. Overrides the top-level setting. | 
| deleteUsers | Array of { "username", "uid" } objects | Up to 100, unique | The accounts to remove from every node. Each entry must match both the user name and the UID. For what's removed, see [Remove a user](sagemaker-hyperpod-slurm-user-management-manage.md#sagemaker-hyperpod-slurm-user-management-manage-remove-a-user). | 
| deleteGroups | Array of { "name", "gid" } objects | Up to 50, unique | The groups to remove from every node, each matched by name and GID. No user in users can still list a group that you delete. | 

**Group (`localUsers.groups[]`)**


| Setting | Type | Required | Limits | Description | 
| --- | --- | --- | --- | --- | 
| name | String | Yes | 1–32 characters that match ^[a-z\_][a-z0-9\_-]{0,31}$, and not a reserved name | The POSIX group name, for example hpc-users. | 
| gid | Integer | Yes | 2000–60000 | The group ID on every node, for example 3001. | 
| ssh | Array of target objects | No | Up to 20 | The node types where the group's members can log in over SSH. If omitted or empty, the group grants no SSH access. | 
| sudo | Array of target objects | No | Up to 20 | The node types where the group's members get passwordless sudo. If omitted or empty, the group grants no sudo access. | 

**User (`localUsers.users[]`)**


| Setting | Type | Required | Limits | Description | 
| --- | --- | --- | --- | --- | 
| username | String | Yes | 1–32 characters that match ^[a-z\_][a-z0-9\_-]{0,31}$, and not a reserved name | The Linux user name, for example user-1. It can't be the name of a group in groups, because the user's private group takes the same name. | 
| uid | Integer | Yes | 2000–60000 | The user ID on every node, for example 2001. It's also the GID of the user's private group, so don't use the same number as a group's gid. | 
| groups | Array of strings | No | Up to 32, unique | The groups that the user joins. Each group must be declared in localUsers.groups. The user's SSH and sudo access comes only from these groups. | 
| homeDirectory | String | No | Up to 256 characters, an absolute path at least two levels deep, not inside a system directory such as /etc or /usr | The home directory, for example /fsx/projects/user-1. The default is {{mount}}/{{username}}. You can't change it after the extension creates the user. | 
| shell | String | No | bash, sh, or nologin | The login shell. Use nologin for an account that owns files or runs services but doesn't log in. A new account gets bash if you omit this setting. An existing account keeps its shell unless you set it. | 

## ldap
<a name="sagemaker-hyperpod-slurm-user-management-config-ldap"></a>

The `ldap` source resolves users and groups from Active Directory through SSSD. It creates no local accounts. For prerequisites and guidance, see [Integrate HyperPod clusters with Active Directory](sagemaker-hyperpod-slurm-user-management-active-directory.md).


| Setting | Type | Required | Default | Description | 
| --- | --- | --- | --- | --- | 
| ldapUri | Array of strings | Yes | None | One to four unique LDAPS URIs of up to 256 characters each, which SSSD tries in order, for example ldaps://ad.example.com or ldaps://ad.example.com:636. Each URI must start with ldaps://, and a port must be from 1 to 65535. | 
| ldapSearchBase | String, up to 512 characters | Yes | None | The base distinguished name (DN) that holds the directory's users and groups, for example dc=example,dc=com. Users and groups outside it don't resolve. | 
| ldapDefaultBindDn | String, up to 512 characters | Yes | None | The DN of a dedicated, read-only account that SSSD binds as, for example CN=ReadOnly,OU=Users,DC=example,DC=com. Any user who can log in to the cluster can read this account's password. For more information, see [Prerequisites](sagemaker-hyperpod-slurm-user-management-active-directory.md#sagemaker-hyperpod-slurm-user-management-active-directory-prerequisites). | 
| ldapDefaultAuthtokSecretArn | String | Yes | None | The ARN of an AWS Secrets Manager secret in the cluster's Region that holds the bind account's password as plain text. | 
| ldapTlsCacertSecretArn | String | Yes | None | The ARN of a Secrets Manager secret in the cluster's Region that holds, as plain text, the PEM certificate of the certificate authority (CA) that signed the directory's LDAPS certificate. | 
| ldapSchema | String | No | AD | The directory schema. Only AD is supported. | 
| domain | String, up to 255 characters | No | default | The SSSD domain name, which fully qualified names end with, for example example.com. | 
| ldapIdMapping | String | No | ENABLED | ENABLED maps directory users' UIDs and GIDs from their Active Directory security identifiers (SIDs). DISABLED reads the uidNumber and gidNumber attributes. Keep the value that you created the source with, because changing it renumbers every directory user. | 
| useFullyQualifiedNames | String | No | DISABLED | ENABLED names directory users and groups {{name}}@{{domain}}, so that they can't take a local user's name or home directory. We recommend ENABLED when you use both sources. | 
| sshAuthMethod | String | No | PUBLIC\_KEY | How directory users log in over SSH. PUBLIC\_KEY uses a public key stored in the directory. PASSWORD uses their directory password, and turns on SSH password authentication for every user on the node. | 
| ldapUserSshPublicKey | String | No | altSecurityIdentities | The directory attribute that holds users' SSH public keys: altSecurityIdentities or sshPublicKey. | 
| ldapGroups | Array of directory group objects | No | [] | Up to 50 existing directory groups, and the node types where their members can log in over SSH and get sudo. No group has access by default. If you omit this setting, no directory user can log in over SSH. | 
| sharedFilesystemMount | String, up to 256 characters | No | The top-level sharedFilesystemMount | The mount for directory users' home directories, for example /fsx. localUsers.sharedFilesystemMount doesn't apply to directory users. Home directories are created as root at first login, so the mount must not squash root on the nodes that users log in to. Keep the value that you created the source with, because changing it gives directory users new, empty home directories. | 

**Directory group (`ldap.ldapGroups[]`)**


| Setting | Type | Required | Limits | Description | 
| --- | --- | --- | --- | --- | 
| name | String | Yes | 1–64 characters that match ^[A-Za-z0-9\_][A-Za-z0-9.\_@-]{0,63}$ | An existing directory group, for example hpc-users, or hpc-users@example.com when useFullyQualifiedNames is ENABLED. The extension doesn't create the group or change its members. Names match without regard to case. | 
| ssh | Array of target objects | No | Up to 20 | The node types where the group's members can log in over SSH. | 
| sudo | Array of target objects | No | Up to 20 | The node types where the group's members get passwordless sudo. | 

**Target (`ssh[]` and `sudo[]` items)**


| Setting | Type | Required | Valid values | Description | 
| --- | --- | --- | --- | --- | 
| nodeTypes | Array of strings | Yes | One to three unique values from controller, login, and compute | The Slurm node types where the access applies. To target every node, list all three. | 

## Validation rules
<a name="sagemaker-hyperpod-slurm-user-management-config-validation-rules"></a>

When you call the API, HyperPod checks the configuration against the schema on this page, and checks that each secret ARN is in the cluster's Region. A configuration that fails is rejected, and nothing changes. Each message names the setting with a JSON pointer, and never repeats the value.


| Example message | Cause | 
| --- | --- | 
| /userSources/localUsers/users/0/uid: must be at least 2000 | A UID or GID outside 2000–60000. | 
| /userSources/localUsers/users/{{index}}/username: is not in the expected format | A name with capital letters, spaces, or other characters that aren't allowed. | 
| /userSources/localUsers/users: must have at most 100 items | Too many users. | 
| /userSources: has properties the schema does not permit | A misspelled or unknown setting, for example localUser. | 
| /userSources/ldap/ldapUri/0: is not in the expected format | An ldap:// URI. Use ldaps://. | 
| /userSources/ldap/ldapDefaultAuthtokSecretArn: is in region 'us-east-1' but the cluster's region is 'us-west-2' | A secret in another Region. | 
| /: is missing required property "userSources" | A configuration without userSources, such as {}. | 

The nodes check the following rules. A configuration that breaks one is accepted by the API, but every node refuses it before it changes anything, and the status becomes `CreateFailed` or `UpdateFailed`. Health shows the message, which names the setting. Correct the configuration and update the extension.


| Rule | Example message | 
| --- | --- | 
| User names, UIDs, group names, and GIDs are unique within each list. | userSources.localUsers.users[1].uid repeats an earlier entry | 
| Every group in a user's groups is declared in localUsers.groups. | userSources.localUsers.users[0].groups[0] isn't in userSources.localUsers.groups | 
| A user name isn't also a group name, and a UID isn't also a group's GID. | userSources.localUsers.users[0].uid is also userSources.localUsers.groups[0].gid; a user's private group takes its uid | 
| No user in users lists a group in deleteGroups. | ... is in userSources.localUsers.deleteGroups; remove it from this user's groups | 
| An entry can't be both kept and removed, and a removed ID isn't reused in the same configuration. | userSources.localUsers.deleteGroups[0].name is also in userSources.localUsers.groups; it can't be both kept and removed | 
| A directory group name isn't all digits, isn't a system group's name in any case, and doesn't repeat another entry in a different case. | userSources.ldap.ldapGroups[0].name is a system group's name; a directory group can't share it | 
| A directory group name ends with @{{domain}} only when useFullyQualifiedNames is ENABLED, and then with the domain setting. | userSources.ldap.ldapGroups[0].name names a domain; SSSD reports short names unless useFullyQualifiedNames is ENABLED | 

## Reserved names
<a name="sagemaker-hyperpod-slurm-user-management-config-reserved-names"></a>

Users and groups can't use names that the operating system, HyperPod, or installed software already uses. The following names are rejected as group names, in a user's `groups` list, and in `deleteGroups`.

`_chrony`, `_ssh`, `adm`, `admin`, `apache`, `audio`, `avahi`, `avahi-autoipd`, `aws-kinesis-agent-user`, `backup`, `bin`, `cdrom`, `chrony`, `clamilt`, `clamscan`, `clamupdate`, `colord`, `crontab`, `cwagent`, `daemon`, `dbus`, `debuginfod`, `dialout`, `dip`, `disk`, `dnsmasq`, `docker`, `dovecot`, `dovenull`, `ec2-instance-connect`, `ec2-user`, `fax`, `flatpak`, `floppy`, `ftp`, `fwupd-refresh`, `games`, `gnats`, `haproxy`, `input`, `irc`, `kmem`, `kvm`, `landscape`, `ldap`, `libstoragemgmt`, `list`, `lock`, `lp`, `lxd`, `mail`, `mailnull`, `man`, `mem`, `memcached`, `messagebus`, `mock`, `munge`, `mysql`, `named`, `netdev`, `news`, `nginx`, `nobody`, `nogroup`, `nscd`, `nvidia-dcgm`, `ods`, `operator`, `pesign`, `plugdev`, `polkitd`, `postdrop`, `postfix`, `postgres`, `printadmin`, `proxy`, `pulse`, `pulse-access`, `pulse-rt`, `radvd`, `rdma`, `redis6`, `render`, `root`, `rpc`, `rpcuser`, `rtkit`, `sanlock`, `sasl`, `saslauth`, `screen`, `sgx`, `shadow`, `slocate`, `slurm`, `smmsp`, `smtpd`, `smtpq`, `sphinx`, `squid`, `src`, `ssh`, `ssh_keys`, `sshd`, `ssm-user`, `sssd`, `staff`, `stap-server`, `stapdev`, `stapsys`, `stapusr`, `stunnel4`, `sudo`, `sys`, `syslog`, `systemd-coredump`, `systemd-journal`, `systemd-journal-remote`, `systemd-network`, `systemd-oom`, `systemd-resolve`, `systemd-timesync`, `tape`, `tcpdump`, `tomcat`, `tracing`, `tss`, `tty`, `ubuntu`, `unbound`, `usbmon`, `users`, `usershares`, `utempter`, `utmp`, `uucp`, `uuidd`, `video`, `virusgroup`, `voice`, `wbpriv`, `wheel`, `wireshark`, `www-data`.

User names in `users` and `deleteUsers` can't be any of these names, and also can't be `_apt`, `_rpc`, `halt`, `nslcd`, `pollinate`, `shutdown`, `statd`, or `sync`.

## Example configurations
<a name="sagemaker-hyperpod-slurm-user-management-config-example-configurations"></a>

A single administrator:

```json
{
  "userSources": {
    "localUsers": {
      "groups": [
        { "name": "cluster-admins", "gid": 3002,
          "ssh":  [ { "nodeTypes": ["controller", "login", "compute"] } ],
          "sudo": [ { "nodeTypes": ["controller", "login", "compute"] } ] }
      ],
      "users": [ { "username": "admin-1", "uid": 2001, "groups": ["cluster-admins"] } ]
    }
  }
}
```

A custom home directory and a service account. `svc-data` is a non-interactive account that can own files on the shared file system. It has no SSH access and no sudo access.

```json
{
  "sharedFilesystemMount": "/fsx",
  "userSources": {
    "localUsers": {
      "groups": [
        { "name": "hpc-users", "gid": 3001, "ssh": [ { "nodeTypes": ["login"] } ] }
      ],
      "users": [
        { "username": "user-1", "uid": 2002, "groups": ["hpc-users"] },
        { "username": "user-2", "uid": 2003, "groups": ["hpc-users"],
          "homeDirectory": "/fsx/projects/user-2" },
        { "username": "svc-data", "uid": 2900, "shell": "nologin" }
      ]
    }
  }
}
```

An empty user list. This configuration is valid, but it restricts SSH to the `ubuntu` user. Other users can log in over SSH only if another `AllowGroups` rule on the node allows them, for example from the `ldap` source or from your lifecycle scripts:

```json
{ "userSources": {} }
```

**Note**  
The restriction lasts until you add users with SSH access or delete the extension. Deleting the extension removes its SSH and sudo rules but keeps local users and groups.

For Active Directory examples, see [Integrate HyperPod clusters with Active Directory](sagemaker-hyperpod-slurm-user-management-active-directory.md). For the health check codes, see [Logs and health checks](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-logs-and-health-checks).