# (Optional) Manage AD users and groups

In this step, you manage users and groups from an Amazon EC2 Amazon Linux 2 instance that's joined to the Active Delivery (AD) domain.

If you followed the _automated_ path, restart and log in to the AD joined instance that was created as part of the
automation.

If you followed the _manual_ path, restart and log in to the instance that you created and joined to the AD in preceding
steps.

In these steps, you use the [adcli](https://www.mankier.com/package/adcli "https://www.mankier.com/package/adcli") and [openldap-clients](https://www.mankier.com/package/openldap-clients "https://www.mankier.com/package/openldap-clients") tools that were installed in the instance as part of a preceding
step.

###### Log in to an Amazon EC2 instance that is joined to the AD domain

1. From the Amazon EC2 console, select the untitled Amazon EC2 instance that was created in previous steps. The instance state might be
   **Stopped**.
2. If the instance state is **Stopped**, choose **Instance state** and then **Start instance**.
3. After the status checks pass, select the instance and choose **Connect** and SSH in to the instance.

###### Manage users and groups when logged into an Amazon EC2 Amazon Linux 2 instance that's joined the AD

When you run the `adcli` commands with the `-U "Admin"` option, you're prompted to enter the AD `Admin`
password. You include the AD `Admin` password as part of the `ldapsearch` commands.

1. ###### Create a user.

```
`$` `adcli create-user `"clusteruser"` --domain `"corp.example.com"` -U "Admin"`
```

2. ###### Set a user password.

```
`$` `aws --region `"region-id"` ds reset-user-password --directory-id `"d-abcdef01234567890"` --user-name `"clusteruser"` --new-password `"new-p@ssw0rd"``
```

3. ###### Create a group.

```
`$` `adcli create-group `"clusterteam"` --domain `"corp.example.com"` -U "Admin"`
```

4. ###### Add a user to a group.

```
`$` `adcli add-member `"clusterteam"` `"clusteruser"` --domain `"corp.example.com"` -U "Admin"`
```

5. ###### Describe users and groups.

Describe all users.

```
`$` `ldapsearch "(&(objectClass=`user`))" -x -h `"192.0.2.254"` -b "DC=`corp`,DC=`example`,DC=`com`" -D "CN=Admin,OU=Users,OU=`CORP`,DC=`corp`,DC=`example`,DC=`com`" -w `"p@ssw0rd"``
```

Describe a specific user.

```
`$` `ldapsearch "(&(objectClass=`user`)(cn=`clusteruser`))" -x -h `"192.0.2.254"` -b "DC=`corp`,DC=`example`,DC=`com`" -D "CN=Admin,OU=Users,OU=`CORP`,DC=`corp`,DC=`example`,DC=`com`" -w `"p@ssw0rd"``
```

Describe all users with a name pattern.

```
`$` `ldapsearch "(&(objectClass=`user`)(cn=`user*`))" -x -h `"192.0.2.254"` -b "DC=`corp`,DC=`example`,DC=`com`" -D "CN=Admin,OU=Users,OU=`CORP`,DC=`corp`,DC=`example`,DC=`com`" -w `"p@ssw0rd"``
```

Describe all users that are part of a specific group.

```
`$` `ldapsearch "(&(objectClass=`user`)(memberOf=CN=`clusterteam`,OU=Users,OU=`CORP`,DC=`corp`,DC=`example`,DC=`com`))" -x -h `"192.0.2.254"` -b "DC=`corp`,DC=`example`,DC=`com`" -D "CN=Admin,OU=Users,OU=`CORP`,DC=`corp`,DC=`example`,DC=`com`" -w `"p@ssw0rd"``
```

Describe all groups

```
`$` `ldapsearch "objectClass=`group`" -x -h `"192.0.2.254"` -b "DC=`corp`,DC=`example`,DC=`com`" -D "CN=Admin,OU=Users,OU=`CORP`,DC=`corp`,DC=`example`,DC=`com`" -w `"p@ssw0rd"``
```

Describe a specific group

```
`$` `ldapsearch "(&(objectClass=`group`)(cn=`clusterteam`))" -x -h `"192.0.2.254"` -b "DC=`corp`,DC=`example`,DC=`com`" -D "CN=Admin,OU=Users,OU=`CORP`,DC=`corp`,DC=`example`,DC=`com`" -w `"p@ssw0rd"``
```

6. ###### Remove a user from a group.

```
`$` `adcli remove-member `"clusterteam"` `"clusteruser"` --domain `"corp.`example`.com"` -U "Admin"`
```

7. ###### Delete a user.

```
`$` `adcli delete-user `"clusteruser"` --domain `"corp.`example`.com"` -U "Admin"`
```

8. ###### Delete a group.

```
`$` `adcli delete-group `"clusterteam"` --domain `"corp.`example`.com"` -U "Admin"`
```
