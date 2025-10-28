# Importing users and groups

Users will only appear in the Amazon DCV Access Console if they have been directly imported from the
Access Console, or have already logged in. Users are imported into the Access Console by uploading
a CSV file. Once imported, user names populate on the **Users** page of the Access Console.

User groups can also be imported with a CSV file to the Access Console. If you choose
not to import user groups, you can create from the Access Console directly.

###### To import users and groups with a CSV file

1. Go to the **Users** page.
2. Select the **Import users** button.
3. Upload a CSV file where each row has the following format:

UserID,DisplayName,Role,GroupIDs

With the following parameters:

    * **UserID**– This field is required.
    * **DisplayName**– This field is optional. It
     will be set to the same as UserID, if left empty.
    * **Role**– This field is optional, and can be
     set to either Admin or User. It will be set to User, if left
     empty.
    * **GroupIDs**– This field is optional. You can
     include multiple GroupIDs, separated by “|”.

###### Note

You can import users and groups from the same CSV file.
