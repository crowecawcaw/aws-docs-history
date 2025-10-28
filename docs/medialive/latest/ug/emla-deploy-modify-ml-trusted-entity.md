# Modifying the MediaLive trusted

entity

You must modify the trusted entity role that you created for MediaLive. You should have
already [set up this trust entity](setting-up-trusted-entity.md "setting-up-trusted-entity.md").

You must modify the role that you set up:

- If you [set up with the simple
  option](setup-trusted-entity-simple.md "setup-trusted-entity-simple.md"), this role has the name `MediaLiveAccessRole`.
- If you [set up with the complex
  option](setup-trusted-entity-complex.md "setup-trusted-entity-complex.md"), this role has a name that describes its purpose. In [Create roles](complex-scenario-create-trusted-entity-role-step3.md "complex-scenario-create-trusted-entity-role-step3.md"), we suggested name such
  as `MedialiveAccessRoleForSports`.

You might have several roles. Identify all the roles that will be used with at least
one channel that runs on on-premises node hardware.
You must modify the role to include the action `sts:TagSession`.

Follow this procedure to modify each role that you identified.

1. On the IAM console, in the navigation pane on the left, choose
   **Roles**, then find a role to modify.
2. On the summary page, selected the **Trust relationships** page. The
   current trust statement appears. Choose **Edit trust policy**.
3. The existing trust policy probably looks like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "medialive.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

4. Change the `Action` line to an array of these two actions:

```
     "Action": ["sts:AssumeRole", "sts:TagSession"]
```

5. Choose **Update policy**.
