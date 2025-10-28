# Find IAM entities in AMS

Your account has default IAM Roles and Policies; see [IAM user role in AMS](defaults-user-role.md "defaults-user-role.md") and
default IAM instance profiles; see [EC2 IAM instance profile](defaults-instance-profile.md "defaults-instance-profile.md") with default policies.
To discover your IAM roles and policies:

- Console: Use the IAM console to view all IAM policies and roles for your account.
- API/CLI (when logged into your AMS account):

###### Note

The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources**
page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for
authentication; for example, `aws amsskms `ams-cli-command` --profile SAML`. You may also need to add the `--region` option as all AMS
commands run out of us-east-1; for example `aws amscm `ams-cli-command` --region=us-east-1`.

List your roles:

```
aws --profile saml iam list-roles
```

List your policies:

```
aws --profile saml iam list-role-policies --role-name `ROLE_NAME`
```
