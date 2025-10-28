# Managing users in your user pool

After you create a user pool, you can create, confirm, and manage user accounts. With
Amazon Cognito user pools groups you can manage your users and their access to resources by mapping IAM roles
to groups.

Managing users in your Amazon Cognito user pool involves a variety of configuration options and
administrative tasks. User pools can scale to millions of users. A user directory of this
scale requires equally scalable and repeatable administrative tools. You might want to
create many user profiles, manage inactive users, produce governance and compliance reports,
or set up self-service tools where users do most of the work. After you create a user pool,
you can control how users sign up and confirm their accounts, including requiring email or
phone number verification. Administrators can also create user accounts directly and
customize the welcome messages and password requirements.

User pools have user groups, where you can manage access to resources based on a user's
group membership. You can assign IAM roles to these groups to manage access to
AWS services with identity pools. Users' group membership is present in both ID and access
tokens. With this information, you can make access-control decisions at runtime in your
application or with a policy engine like Amazon Verified Permissions.

User pools often have many users. You will frequently find yourself searching for and
updating user accounts. The Amazon Cognito console and API support querying users based on standard
attributes like username, email, and phone number. Administrators can also reset passwords,
disable accounts, and view user event history.

For migrating existing user data, Amazon Cognito has options to import users from a CSV file and to
use a [Lambda trigger](user-pool-lambda-migrate-user.md "user-pool-lambda-migrate-user.md") to automatically
migrate users when they first sign in. These options support user transitions from other
user directories to your user pool.

You can use the user-management features in user pools to have fine-grained control over
the user lifecycle and authentication experience. The combination of self-service sign-up,
admin-created accounts, groups, and migration tools makes Amazon Cognito user pools a flexible user
directory.

###### Topics

- [Configuring policies for user
  creation](user-pool-settings-admin-create-user-policy.md "user-pool-settings-admin-create-user-policy.md")
- [Signing up and confirming user accounts](signing-up-users-in-your-app.md "signing-up-users-in-your-app.md")
- [Creating user accounts as administrator](how-to-create-user-accounts.md "how-to-create-user-accounts.md")
- [Adding groups to a user pool](cognito-user-pools-user-groups.md "cognito-user-pools-user-groups.md")
- [Managing and searching for user accounts](how-to-manage-user-accounts.md "how-to-manage-user-accounts.md")
- [Passwords, account recovery, and password
  policies](managing-users-passwords.md "managing-users-passwords.md")
- [Importing users into a user pool](cognito-user-pools-import-users.md "cognito-user-pools-import-users.md")
- [Working with user attributes](user-pool-settings-attributes.md "user-pool-settings-attributes.md")
