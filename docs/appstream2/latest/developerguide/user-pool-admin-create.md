# Creating a User in Amazon WorkSpaces Applications

You must enter a valid and unique email address for each new user within a Region.
However, you can reuse an email address for a new user in another Region.

When you create a new user, be aware of the following:

- You cannot change the email address, first name, or last name for a user
  that you have already created. To change this information for a user,
  disable the user. Then, recreate the user (as a new user) and specify the
  updated information as needed.
- Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same
  capitalization as the email address specified when their user pool account was created, a "user does not exist" error message
  displays.
- You can assign one or more stacks to the user after the user is
  created.

###### To create a new user

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **User Pool**,
   **Create User**.
3. For **Email**, type the unique email address for the
   user.
4. Type the user's first name and last name in the corresponding fields.
   These fields need not be unique.
5. Choose **Create User**.
   After users are created, WorkSpaces Applications sends them a welcome email. This email includes
   the login portal link, the login email address to be used, and a temporary password.
   By browsing to the login portal and typing their temporary password, users can set a
   permanent password to access their applications.

By default, the new user's status is **Enabled**, meaning you can
assign one or more stacks to the user or perform other administrative
actions.
