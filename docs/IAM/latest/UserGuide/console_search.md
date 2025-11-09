# Using search to find IAM resources

As you work through your access findings, you can use the IAM console search page as a faster option for finding IAM resources. You can
search for resources using partial resource names or ARNs.

Console
The IAM console search feature can locate any of the following:

- IAM entity names that match your search keywords (for users, groups, roles, identity
  providers, and policies)
- Tasks that match your search keywords

The IAM console search feature does not return information about IAM Access Analyzer.

Every line in the search result is an active link. For example, you can choose the user name
in the search result, which takes you to that user's detail page. Or you can choose an action
link, for example **Create user**, to go to the **Create
User** page.

###### Note

Access key search requires you to type the full access key ID in the search box. The
search result shows the user associated with that key. From there you can navigate directly to
that user's page, where you can manage the access key.

Use the **Search** page in the IAM console to find items related to
that account.

###### To search for items in the IAM console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Search**.
4. In the **Search** box, type your search keywords.
5. Choose a link in the search results list to navigate to the corresponding part of the
   console.

The following icons identify the types of items that are found by a search:

| Icon                                            | Description                                    |
| ----------------------------------------------- | ---------------------------------------------- |
| a portrait outline on gray background           | IAM users                                      |
| multiple portrait outlines on a blue background | IAM groups                                     |
| a magic wand icon on a navy background          | IAM roles                                      |
| a document icon on an organe background         | IAM policies                                   |
| a white start on an organe background           | Tasks such as "create user" or "attach policy" |
| a white X on a red background                   | Results from the keyword `delete`              |

**Sample search phrases**

You can use the following phrases in the IAM search. Replace terms in italics with the
names of the actual IAM users, groups, roles, access keys, policies, or identity providers
that you want to locate.

- `user_name` or
  `group_name` or `role_name` or
  `policy_name` or
  `identity_provider_name`
- `access_key`
- `add user `user_name` to groups` or
  `add users to group `group_name``
- `remove user `user_name` from
groups`
- `delete `user_name`` or
`delete `group_name`` or `delete
`role_name``, or `delete
`policy_name``, or `delete
`identity_provider_name``
- `manage access keys `user_name``
- `manage signing certificates
`user_name``
- `users`
- `manage MFA for `user_name``
- `manage password for `user_name``
- `create role`
- `password policy`
- `edit trust policy for role
`role_name``
- `show policy document for role
`role_name``
- `attach policy to `role_name``
- `create managed policy`
- `create user`
- `create group`
- `attach policy to `group_name``
- `attach entities to
`policy_name``
- `detach entities from
`policy_name``
