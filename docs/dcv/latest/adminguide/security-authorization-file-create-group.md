# Creating groups

You can use `[groups]` section of the permissions file to define user groups for users that have similar use cases or permissions
requirements. Groups can be assigned specific permissions. Permissions assigned to a group apply to all of the users that are included in the
group.

To create groups in your permissions file, you must first add the groups section heading to the file.

```
[groups]
```

You can then create your groups under the section heading. To create a group, provide the group name, and then specify the group members in
a comma-separated list. Group members can be individual users, other groups, and operating system user groups.

```
`group_name`=`member_1`, `member_2`, `member_3`
```

###### To add a user to a group

Specify the user name.

###### Note

You can prefix the user name with `user:`. Windows domain user names can include a domain name.

```
`group_name`=`user_1`, user:`user_2`, `domain_name\user_3`
```

###### To add an existing group to a group

Specify the group name prefixed with `group:`

```
`group_name`=group:`group_1`, group:`group_2`
```

###### To add an operating system user group to a group (Linux Amazon DCV servers only)

Specify the group's name prefixed with `osgroup:`

```
`group_name`=osgroup:`os_group_1`, osgroup:`os_group2`
```

###### Example

The following example adds the groups section heading and creates a group that's named `my-group`. This group includes
individual users. They're named `john` and `jane`. One of them is an existing group that's named `observers`.
The other is an operating system user group that's named `guests`:

```
[groups]
my-group=john, user:jane, group:observers, osgroup:guests
```
