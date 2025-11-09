# Working with user attributes

Attributes are pieces of information that help you identify individual users, such as name,
email address, and phone number. A new user pool has a set of default _standard attributes_. You can also add custom attributes to your user pool
definition in the AWS Management Console. This topic describes those attributes in detail and gives you
tips on how to set up your user pool.

Don't store all information about your users in attributes. For example, keep user data that
changes frequently, such as usage statistics or game scores, in a separate data store, such as
Amazon Cognito Sync or Amazon DynamoDB.

Sanitize the inputs for user-attribute string values before you submit them to your user
pool. One method to analyze proposed user attribute values is with a Lambda trigger like [pre sign-up](user-pool-lambda-pre-sign-up.md "user-pool-lambda-pre-sign-up.md").

###### Note

Some documentation and standards refer to attributes as
_members_.

###### Topics

- [Standard attributes](#cognito-user-pools-standard-attributes "#cognito-user-pools-standard-attributes")
- [Username and preferred username](#user-pool-settings-usernames "#user-pool-settings-usernames")
- [Customizing sign-in attributes](#user-pool-settings-aliases "#user-pool-settings-aliases")
- [Custom attributes](#user-pool-settings-custom-attributes "#user-pool-settings-custom-attributes")
- [Attribute permissions
  and scopes](#user-pool-settings-attribute-permissions-and-scopes "#user-pool-settings-attribute-permissions-and-scopes")

## Standard attributes

Amazon Cognito assigns all users a set of standard attributes based on the [OpenID Connect
specification](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims "http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims"). By default, standard and custom attribute values can be any string
with a length of up to 2048 characters, but some attribute values have format restrictions.

The standard attributes are:

- `name`
- `family_name`
- `given_name`
- `middle_name`
- `nickname`
- `preferred_username`
- `profile`
- `picture`
- `website`
- `gender`
- `birthdate`
- `zoneinfo`
- `locale`
- `updated_at`
- `address`
- `email`
- `phone_number`
- `sub`

Except for `sub`, standard attributes are optional by default for all users. To
make an attribute required, during the user pool creation process, select the
**Required** check box next to the attribute. Amazon Cognito assigns a unique user
identifier value to each user's `sub` attribute. Only the
**email** and **phone_number** attributes can be
verified.

Standard attributes have predefined properties that you can view in the
`SchemaAttributes` parameter of a [DescribeUserPool API response](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md#API_DescribeUserPool_ResponseSyntax "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md#API_DescribeUserPool_ResponseSyntax"). You can set custom values for these attribute
properties, like data type, mutability, and length constraints. To modify standard attribute
properties, set their custom values in the [CreateUserPool Schema parameter](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-Schema "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-Schema"). The schema is also where you set required
attributes. You can't modify the properties of standard attributes when you create user pools
in the Amazon Cognito console.

###### Note

When you mark a standard attribute as **Required**, a user can't
register unless they provide a value for the attribute. To create users and not give values
for required attributes, administrators can use the [AdminCreateUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md") API. After you create a user pool, you can't switch an attribute
between required and not required.

###### Standard attribute

details and format restrictions

**birthdate**

Value must be a valid 10 character date in the format YYYY-MM-DD.

**email**

Users and administrators can verify email address values.

An administrator with proper AWS account permissions can change the user's email
address and also mark it as verified. Mark an email address as verified with the [AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md") API or the [admin-update-user-attributes](../../../cli/latest/reference/cognito-idp/admin-update-user-attributes.md "../../../cli/latest/reference/cognito-idp/admin-update-user-attributes.md") AWS Command Line Interface (AWS CLI) command. With this command,
the administrator can change the `email_verified` attribute to
`true`. You can also edit a user in the **Users** menu of
the Amazon Cognito console to mark an email address as verified.

Value must be a [valid email address string](https://datatracker.ietf.org/doc/html/rfc3696#section-3 "https://datatracker.ietf.org/doc/html/rfc3696#section-3") following the standard email format with @ symbol
and domain, up to 2048 characters in length.

**phone_number**

A user must provide a phone number if SMS multi-factor authentication (MFA) is
active. For more information, see [Adding MFA to a user pool](user-pool-settings-mfa.md "user-pool-settings-mfa.md").

Users and administrators can verify phone number values.

An administrator with proper AWS account permissions can change the user's phone
number and also mark it as verified. Mark a phone number as verified with the [AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md") API or the [admin-update-user-attributes](../../../cli/latest/reference/cognito-idp/admin-update-user-attributes.md "../../../cli/latest/reference/cognito-idp/admin-update-user-attributes.md") AWS CLI command. With this command, the
administrator can change the `phone_number_verified` attribute to
`true`. You can also edit a user in the **Users** menu of
the Amazon Cognito console to mark a phone number as verified.

###### Important

Phone numbers must follow these format rules: A phone number must start with a
plus (`+`) sign, followed immediately by the country code. A
phone number can only contain the `+` sign and digits. Remove any
other characters from a phone number, such as parentheses, spaces, or dashes
(`-`) before you submit the value to the service. For example,
a phone number based in the United States must follow this format:
`+14325551212`.

**preferred_username**

You can select `preferred_username` as required or as an alias, but not
both. If the `preferred_username` is an alias, you can make a request to the
[UpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md") API operation and add the attribute value after you
confirm the user.

**sub**

Index and search your users based on the `sub` attribute. The
`sub` attribute is a unique user identifier within each user pool. Users
can change attributes like `phone_number` and `email`. The
`sub` attribute has a fixed value. For more information about finding
users, see [Managing and searching for user accounts](how-to-manage-user-accounts.md "how-to-manage-user-accounts.md").

### View required attributes

Use the following procedure to view required attributes for a given user pool.

###### Note

You can't change required attributes after you create a user pool.

###### To view required attributes

1. Go to [Amazon Cognito](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") in the AWS Management Console.
   If the console prompts you, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Sign-up** menu.
5. In the **Required attributes** section, view the required
   attributes of your user pool.

## Username and preferred username

The `username` value is a separate attribute and not the same as the
`name` attribute. Each user has a `username` attribute. Amazon Cognito
automatically generates a username for federated users. You must provide a
`username` attribute to create a local user in the Amazon Cognito directory. After you
create a user, you can't change the value of the `username` attribute.

Developers can use the `preferred_username` attribute to give users usernames
that they can change. For more information, see [Customizing sign-in attributes](#user-pool-settings-aliases "#user-pool-settings-aliases").

If your application doesn't require a username, you don't need to ask users to provide
one. Your app can create a unique username for users in the background. This can be useful if
you want users to register and sign in with an email address and password. For more
information, see [Customizing sign-in attributes](#user-pool-settings-aliases "#user-pool-settings-aliases").

The `username` must be unique within a user pool. A `username` can
be reused, but only after you delete it and it is no longer in use. For information about the
string constraints to the `username` attributes, see the _username_ property of a [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-Username "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-Username") API request.

## Customizing sign-in attributes

When you create a user pool, you can set up _username
attributes_ if you want your users to be able to sign up and sign in with an email
address or phone number as their username. Alternatively, you can set up _alias attributes_ to give your users the option: they can include
multiple attributes when they sign up, and then sign in with a username, preferred username,
email address, or phone number.

###### Important

After you create a user pool, you can't change this setting.

### How to choose between alias attributes

and username attributes

| Your requirement                                                                                               | Alias attributes | Username attributes |
| -------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------- |
| Users have multiple sign-in attributes                                                                         | Yes¹             | No²                 |
| Users must verify email address or phone number before they can sign in with it                                | Yes              | No                  |
| Sign up users with duplicate email addresses or phone numbers and prevent<br>`UsernameExistsException` errors³ | Yes              | No                  |
| Can assign the same email address or phone number attribute value to more than one<br>user                     | Yes⁴             | No                  |

¹ Available sign-in attributes are username, email address, phone number, and
preferred username.

² Can sign in with email address or phone number.

³ Your user pool doesn't generate `UsernameExistsException` errors when
users register with potentially-duplicate email addresses or phone numbers, but no username.
This behavior is independent of **Prevent username existence errors**,
which applies to sign-in, but not sign-up, operations.

⁴ Only the last user who has verified the attribute can sign in with it.

An attribute is an _alias_ when users have a
username but can also sign in with that attribute. Set up aliases when you want to allow
your users to choose between their username and other attribute values in the username
field of your sign-in form. The `username` attribute is a fixed value that
users can't change. If you mark an attribute as an alias, users can sign in with that
attribute in place of the username. You can mark the email address, phone number, and
preferred username attributes as aliases. For example, if you select email address and
phone number as aliases for a user pool, users in that user pool can sign in with their
username, email address, or phone number, along with their password.

To choose alias attributes, select **User name** and at least one
additional sign-in option when you create your user pool.

###### Note

When you configure your user pool to be case insensitive, a user can use either
lowercase or uppercase letters to sign up or sign in with their alias. For more
information, see [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") in the _Amazon Cognito user pools API Reference_.

If you select email address as an alias, Amazon Cognito doesn't accept a username that
matches a valid email address format. Similarly, if you select phone number as an alias,
Amazon Cognito doesn't accept a username for that user pool that matches a valid phone number
format.

###### Note

Alias values must be unique in a user pool. If you configure an alias for an email
address or phone number, the value that you provide can be in a verified state in only
one account. During sign-up, if your user provides an email address or phone number as
an alias value and another user has already used that alias value, registration
succeeds. However, when a user tries to confirm the account with this email (or phone
number) and enters the valid code, Amazon Cognito returns an `AliasExistsException`
error. The error indicates to the user that an account with this email address (or
phone number) already exists. At this point, the user can abandon their attempt to
create the new account and instead try to reset the password for the old account. If
the user continues to create the new account, your app must call the
`ConfirmSignUp` API with the `forceAliasCreation` option.
`ConfirmSignUp` with `forceAliasCreation` moves the alias from
the previous account to the newly created account, and marks the attribute unverified
in the previous account.

Phone numbers and email addresses only become active aliases for a user after your
user verifies the phone numbers and email addresses. We recommend that you choose
automatic verification of email addresses and phone numbers if you use them as
aliases.

Choose alias attributes to prevent `UsernameExistsException` errors for
email address and phone number attributes when your users sign up.

Activate the `preferred_username` attribute so that your user can change
the username that they use to sign in while their `username` attribute value
doesn't change. If you want to set up this user experience, submit the new
`username` value as a `preferred_username` and choose
`preferred_username` as an alias. Then users can sign in with the new value
that they entered. If you select `preferred_username` as an alias, your user
can provide the value only when they confirm an account. They can't provide the value
during registration.

When the user signs up with a username, you can choose if they can sign in with one
or more of the following aliases.

- Verified email address
- Verified phone number
- Preferred username
  After the user signs up, they can change these aliases.

###### Important

When your user pool supports sign-in with aliases and you want to authorize or
look up a user, don't identify your user by any of their sign-in attributes. The
fixed-value user identifier `sub` is the only consistent indicator of your
user's identity.

Include the following steps when you create the user pool so that users can sign in
with an alias.

Phone number or email address (console)
You must set email address and phone number as alias attributes when you
create a user pool.

###### To create a user pool with username aliases in the Amazon Cognito console

1. Go to [Amazon Cognito](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") in the
   AWS Management Console. If the console prompts you, enter your AWS credentials.
2. Create a new user pool with the **Get started** or
   **Create user pool** button.
3. Choose application settings in **Define your
   application**.
4. In **Configure options** under **Options for
   sign-in identifiers**, select the checkbox next to
   **Username** and at least one of the other options,
   **Email** and **Phone number**.
5. Choose your alias attributes as **Required attributes for
   sign-up**. In the managed login sign-up form, Amazon Cognito prompts new
   users to provide values for required attributes.
6. Under **Add a return URL**, set up an application
   callback URL for redirect after managed login sign-in.
7. Choose **Create**.

Phone number or email address (API/SDK)
Create a new user pool with the [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") API operation. Configure the
`AliasAttributes` parameter as shown. You can remove the
`email` entry if you only want phone-number aliases, or remove the
`phone_number` entry if you only want email-address aliases.

```
"AliasAttributes": [
   "email",
   "phone_number"
],
```

Preferred username (API/SDK)
The Amazon Cognito console creates user pools without `preferred_username`
as an alias. To create user pools with a `preferred_username` alias,
set up user pools with [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") API requests in an AWS SDK. To support the creation of
preferred username attributes at sign-up, set `preferred_username` as a
required attribute. In the managed login sign-up form, Amazon Cognito prompts new users to
provide values for required attributes. You _can_
set `preferred_username` as a required attribute in the Amazon Cognito console,
but this doesn't make it available as an alias.

###### Configure as an alias

Configure `preferred_username` as an alias in the
`AliasAttributes` parameter of a `CreateUserPool`
request as shown. Remove any values that you don't want as alias attributes from
the list.

```
"AliasAttributes": [
   "email",
   "phone_number",
   "preferred_username"
],
```

###### Configure as required

In the managed login sign-up form, Amazon Cognito prompts new users to provide values
for required attributes. Configure `preferred_username` as required
in the `SchemaAttributes` parameter of a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") request.

To set preferred username as a required attribute, configure it as shown. The
following example modifies the default schema of `preferred_username`
to set it as required. Other schema parameters like `AttributeDataType`
(defaults to `string`) and `StringAttributeConstraints`
(defaults to 1-99 characters in length) assume default values.

```
"Schema": [
   {
      "Name": "preferred_username",
      "Required": true
   }
]
```

When the user signs up with an email address or phone number as their username, you
can choose if they can sign up with only email addresses, only phone numbers, or either
one.

To choose username attributes, don't select **Username** as a
sign-in option when you create your user pool.

The email address or phone number must be unique, and it must not already be in use
by another user. It doesn't have to be verified. After the user has signed up with an
email address or phone number, the user can't create a new account with the same email
address or phone number. The user can only reuse the existing account and reset the
account password, if needed. However, the user can change the email address or phone
number to a new email address or phone number. If the email address or phone number
isn't already in use, it becomes the new username.

When you select both email address and phone number as username attributes, users
can sign in with one or the other, even if they provide values for both attributes. The
sign-in username is based on the value that you pass in the `Username`
parameter of [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-Username "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md#CognitoUserPools-SignUp-request-Username").

###### Note

If a user signs up with an email address as their username, they can change the
username to another email address, but they can't change it to a phone number. If they
sign up with a phone number, they can change the username to another phone number, but
they can't change it to an email address.

Use the following steps during the user pool creation process to set up sign-up and
sign-in with email address or phone number.

Username attributes (console)
The following procedure creates a user pool with email address or phone number
username attributes. The difference in the process for username attributes in the
Amazon Cognito console is that you don't also set **Username** as a
sign-in attribute.

###### To create a user pool with username attributes in the Amazon Cognito console

1. Go to [Amazon Cognito](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") in the
   AWS Management Console. If the console prompts you, enter your AWS credentials.
2. Create a new user pool with the **Get started** or
   **Create user pool** button.
3. Choose application settings in **Define your
   application**.
4. In **Configure options** under **Options for
   sign-in identifiers**, select your username attributes:
   **Email**, **Phone number**, or both.
   Leave **Username** unchecked.
5. As a best practice, select your username attributes as **Required
   attributes for sign-up**. In the managed login sign-up form, Amazon Cognito
   prompts new users to provide values for required attributes. If you don't set
   your username attributes as required, Amazon Cognito doesn't prompt new users to
   provide values for them. In that scenario, you must configure your application
   to collect and submit email addresses or phone numbers for each user before
   they can sign in.
6. Under **Add a return URL**, set up an application
   callback URL for redirect after managed login sign-in.
7. Choose **Create**.

Username attributes (API/SDK)
In a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") request, configure the `UsernameAttributes`
parameter as shown. To allow sign-in only with email-address usernames, specify
`email` alone in this list. To allow sign-in only with phone-number
usernames, specify `phone_number` alone. This parameter overrides
username as a sign-in option.

```
"UsernameAttributes": [
   "email",
   "phone_number"
],
```

When you configure username attributes, your can make [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md")
API requests that pass an email address or phone number in the `username`
parameter. The following is the behavior of the code`SignUp` API operation
with username attributes.

- If the `username` string is in valid email address format, for
  example `user@example.com`, the user pool automatically populates the
  `email` attribute of the user with the `username`
  value.
- If the `username` string is in valid phone number format, for example
  `+12065551212`, the user pool automatically populates the
  `phone_number` attribute of the user with the `username`
  value.
- If the `username` string format isn't in email address or phone
  number format, the `SignUp` API returns an exception.
- If the `username` string contains an email address or phone number
  that is already in use, the `SignUp` API returns an exception.
- The `SignUp` API populates the `username` attribute with a
  [UUID](cognito-terms.md#terms-uuid "cognito-terms.md#terms-uuid") for your user. This UUID has the same value
  as the `sub` claim in the user identity token.
  You can use an email address or phone number in place of the username in all APIs
  except the [ListUsers](../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md") operation. In `ListUsers` API requests, you can specify
  a `Filter` of `email` or `phone_number`. If you filter
  by `username`, you must supply the UUID username, not the email address or
  phone number.

## Custom attributes

You can add up to 50 custom attributes to your user pool. You can specify a minimum and/or
maximum length for custom attributes. However, the maximum length for any custom attribute can
be no more than 2048 characters. The name of a custom attribute must match the regular
expression pattern that's described in the `Name` parameter of [SchemaAttributeType](../../../cognito-user-identity-pools/latest/APIReference/API_SchemaAttributeType.md "../../../cognito-user-identity-pools/latest/APIReference/API_SchemaAttributeType.md").

###### Each custom attribute has the following characteristics:

- You can define it as a string, number, boolean, or `DateTime` object. Amazon Cognito
  writes custom attribute values to the ID token only as strings.

###### Note

In the Amazon Cognito console, you can add custom attributes only of the string and number
data types. Additional options like boolean and `DateTime` attribute data
types are only available in the `SchemaAttributes` property of [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") and [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API requests.

- You can't require that users provide a value for the attribute.
- You can't remove or change it after you add it to the user pool.
- The character length of the attribute name is within the limit that Amazon Cognito accepts. For
  more information, see [Quotas in Amazon Cognito](quotas.md "quotas.md").
- It can be _mutable_ or _immutable_. You can only write a value to an immutable attribute when you
  create a user. You can change the value of a mutable attribute if your app client has
  write permission to the attribute. See [Attribute permissions
  and scopes](#user-pool-settings-attribute-permissions-and-scopes "#user-pool-settings-attribute-permissions-and-scopes") for more
  information.

###### Note

In your code, and in rules settings for [Using role-based access control](role-based-access-control.md "role-based-access-control.md"), custom attributes require the `custom:`
prefix to distinguish them from standard attributes.

You can also add _developer attributes_ when you create
user pools, in the `SchemaAttributes` property of [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md"). Developer attributes have a `dev:` prefix. You can only
modify a user's developer attributes with AWS credentials. Developer attributes are a legacy
feature that Amazon Cognito replaced with app client read-write permissions.

Use the following procedure to create a new custom attribute.

###### To add a custom attribute using the console

1. Go to [Amazon Cognito](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") in the AWS Management Console. If
   the console prompts you, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Sign-up** menu, and in the **Custom
   attributes** section, choose **Add custom attributes**.
5. On the **Add custom attributes** page, provide the following details
   about the new attribute:
   - Enter a **Name**.
   - Select a **Type** of either **String** or
     **Number**.
   - Enter a **Min** string length or number value.
   - Enter a **Max** string length or number value.
   - Select **Mutable** if you want to give users permission to change
     the value of a custom attribute after they set the initial value.

6. Choose **Save changes**.

## Attribute permissions

and scopes

For each app client, you can set read and write permissions for each user attribute. This
way, you can control the access that any app has to read and modify each attribute that you
store for your users. For example, you might have a custom attribute that indicates whether a
user is a paying customer or not. Your apps might be able to see this attribute but not change
it directly. Instead, you would update this attribute using an administrative tool or a
background process. You can set permissions for user attributes from the Amazon Cognito console, the
Amazon Cognito API, or the AWS CLI. By default, any new custom attributes aren't available until you set
read and write permissions for them. By default, when you create a new app client, you grant
your app read and write permissions for all standard and custom attributes. To limit your app
to only the amount of information that it requires, assign specific permissions to attributes
in your app client configuration.

As a best practice, specify attribute read and write permissions when you create an app
client. Grant your app client access to the minimum set of user attributes that you need for
the operation of your application.

###### Note

[DescribeUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md") only returns values for `ReadAttributes` and
`WriteAttributes` when you configure app client permissions other than the
default.

###### To update attribute permissions (AWS Management Console)

1. Go to [Amazon Cognito](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") in the AWS Management Console. If
   the console prompts you, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **App clients** menu and choose an app client from the
   list.
5. In the **Attribute permissions** tab, choose
   **Edit**.
6. On the **Edit attribute read and write permissions** page, configure
   your read and write permissions, and then choose **Save changes**.

Repeat these steps for each app client that uses the custom attribute.

For each app client, you can mark attributes as readable or writeable. This applies to
both standard and custom attributes. Your app can retrieve the value of attributes that you
mark as readable, and can set or modify the value of attributes that you mark as writeable. If
your app tries to set a value for an attribute that it isn't authorized to write, Amazon Cognito
returns `NotAuthorizedException`. [GetUser](../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md") requests include an access token with an app client claim; Amazon Cognito only
returns values for attributes that your app client can read. Your user's ID token from an app
only contains claims that correspond to the readable attributes. All app clients can write
user pool required attributes. You can only set the value of an attribute in an Amazon Cognito user pools API
request when you also provide a value for any required attributes that don't yet have a
value.

Custom attributes have distinct features for read and write permissions. You can create
them as mutable or immutable for the user pool, and you can set them as read or write
attributes for any app client.

An immutable custom attribute can be updated once, during user creation. You can populate
an immutable attribute with the following methods.

- `SignUp`: A user signs up with an app client that has write access to an
  immutable custom attribute. They provide a value for that attribute.
- Sign-in with a third-party IdP: A user signs in to an app client that has write access
  to an immutable custom attribute. Your user pool configuration for their IdP has a rule to
  map a provided claim to an immutable attribute. This is possible but not practical,
  because the user will only be able to sign in one time. On sign-in attempts after their
  first, Amazon Cognito rejects the attempt because of the mapping rule to a now-unwriteable
  attribute.
- `AdminCreateUser`: You provide a value for an immutable attribute.

### Attribute permissions

with scopes

In user pools that you configure with an AWS SDK or CDK, the REST API, or the AWS CLI,
you can configure app client read or write access with the OIDC scope
`oidc:profile`. The `oidc:profile` grants read or write access to
the following standard attributes:

- `name`
- `family_name`
- `given_name`
- `middle_name`
- `nickname`
- `preferred_username`
- `profile`
- `picture`
- `website`
- `gender`
- `birthdate`
- `zoneinfo`
- `locale`

This list is the OIDC standard attributes minus `email`,
`phone_number`, `sub`, and `address`, as defined in
[section 2.4 of
the OIDC specification](https://openid.net/specs/openid-connect-basic-1_0.html#Scopes "https://openid.net/specs/openid-connect-basic-1_0.html#Scopes"). For information about the scopes that you can assign to
your app clients, see [Scopes, M2M, and resource
servers](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md").

To configure your app client to write to the attributes under the
`oidc:profile` scope, set the value of [WriteAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md#CognitoUserPools-CreateUserPoolClient-request-WriteAttributes "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md#CognitoUserPools-CreateUserPoolClient-request-WriteAttributes") to `oidc:profile`, plus any other attributes that you
want to permit your application to modify, in a [CreateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md") or [UpdateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md") API request. Similarly, to grant read access to these
attributes, add `oidc:profile` to the value of [ReadAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md#CognitoUserPools-CreateUserPoolClient-request-ReadAttributes "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.md#CognitoUserPools-CreateUserPoolClient-request-ReadAttributes").

You can change attribute permissions and scopes after you have created your user
pool.
