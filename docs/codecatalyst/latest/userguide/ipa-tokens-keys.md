Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Grant users repository access with personal access tokens

To access some CodeCatalyst
resources,
such as source repositories, on a local computer with a Git client or integrated development
environment (IDE), you must enter an application-specific password. You can create a
personal access token (PAT) to use for this purpose. PATs you create are associated with
your user identity across all spaces and projects in CodeCatalyst. You can create more than one
PAT for your
CodeCatalyst
identity.

You can view the names and expiration dates of the PATs you have created, and you can
delete those you no longer need. You can only copy the PAT secret at the time you create
it.

###### Note

By default, PATs expire in 1 year.

## Creating PATs

PATs are associated with your user identity in CodeCatalyst. You can only copy
a
PAT secret at the time you create
it.

### Creating PATs (console)

You can use the console to create PATs in CodeCatalyst.

###### To

create a personal access token (console)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In
   the top menu bar, choose your
   profile badge, and then choose **My settings**. The CodeCatalyst
   **My settings** page opens.

###### Tip

You can also find your user profile by going to the members page for a
project or space and choosing your name from the members
list. 3. Under **Personal access tokens**, choose
**Create**.

The **Create PAT** page displays. 4. In **PAT name**, enter a descriptive name for your
PAT. 5. In **Expiration date**, keep the default date or choose
the calendar icon to select a custom date. The expiration date defaults to 1
year from the current date. 6. Choose **Create**.

###### Tip

You can also create this token when you choose **Clone
repository** for a source repository. 7. To copy the PAT secret, choose **Copy**. Store the PAT
secret where you will be able to retrieve it.

###### Important

The PAT secret only
displays once. You cannot retrieve it after you close the window.
If
you did not save the PAT secret in a secure location, you can create
another one.

.

### Creating PATs (CLI)

You can use the CLI to create PATs in CodeCatalyst.

###### To create a personal access token (AWS CLI)

1. At the terminal or command line, run the
   **create-access-token** command
   as
   follows.

```
aws codecatalyst create-access-token
```

If
successful, the command returns information about the created PAT like the
following example.

```
{
    "secret": "`value`",
    "name": "`marymajor-22222EXAMPLE`",
    "expiresTime": "2024-02-04T01:56:04.402000+00:00"
}
```

2.

You can only view the PAT secret once—when you create the PAT. If you've
misplaced a PAT secret or you're concerned that it's not stored securely, you can
create another one.

You can view the PATs associated with your user account by using the AWS CLI. You
can only view information about the PAT, and not
the
value of the PAT secret itself.

###### Note

Make
sure that you're using a recent version of the AWS CLI to work with CodeCatalyst.
Earlier versions might not contain the CodeCatalyst commands. You must configure your
AWS CLI profile before you can use it with CodeCatalyst. For more information, see [Setting up to use the AWS CLI with CodeCatalyst](set-up-cli.md "set-up-cli.md").

## Viewing PATs

You can view PATs in CodeCatalyst.
The
list shows all of the PATs that you have associated with your user identity. Your PAT is
associated with your user profile across all spaces and projects in
CodeCatalyst. Expired PATs do not display
because they're deleted after they expire.

### Viewing PATs (console)

You can use the console to view PATs associated with your user identity in
CodeCatalyst.

###### To view your personal access tokens (console)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the top menu bar, choose your profile badge, and then choose
   **My settings**. The CodeCatalyst **My
   settings** page opens.

###### Tip

You can also find your user profile by going to the members page for a
project or space and choosing your name from the members
list. 3. Under **Personal access tokens**, view the names and
expiration dates of your current PATs.

### Viewing PATs (CLI)

You can use the CLI to view PATs associated with your user identity in
CodeCatalyst.

###### To view your personal access tokens

(AWS CLI)

- At the terminal or command line, run the
  **list-access-tokens** command as follows.

```
aws codecatalyst list-access-tokens
```

If
successful, the command returns information about the PATs associated with
your user account like the following
example.

```
{
    "items": [
        {
            "id": "`a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa`",
            "name": "`marymajor-22222EXAMPLE`",
            "expiresTime": "2024-02-04T01:56:04.402000+00:00"
        },
        {
            "id": "`a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb`",
            "name": "`marymajor-11111EXAMPLE`",
            "expiresTime": "2023-03-12T01:58:40.694000+00:00"
        }
    ]
}
```

## Deleting PATs

You can delete PATs associated with your user identity in CodeCatalyst.

### Deleting PATs (console)

You can use the console to delete PATs in CodeCatalyst.

###### To delete a personal access token (console)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the top menu bar, choose your profile badge, and then choose
   **My settings**. The CodeCatalyst **My
   settings** page opens.

###### Tip

You can also find your user profile by going to the members page for a
project or space and choosing your name from the members
list. 3. Under **Personal access tokens**, choose the selector
next to the PAT you want to delete, and then choose
**Delete**.

On the **Delete PAT: <name>?** page, to confirm
deletion, type _delete_ in the text field.
Choose **Delete**.

### Deleting PATs (CLI)

You can delete a PAT associated with your user identity by using the AWS CLI. To do
this, you must supply the ID for the PAT, which you can view by using the
**delete-access-token** command.

###### Note

Make sure that you're using a recent version of the AWS CLI to work with CodeCatalyst.
Earlier versions might not contain the CodeCatalyst commands. For more information
about using the AWS CLI with CodeCatalyst, see [Setting up to use the AWS CLI with CodeCatalyst](set-up-cli.md "set-up-cli.md").

###### To delete a personal access token (AWS CLI)

- At the terminal or command line, run the
  **delete-access-token** command, providing the ID for the
  PAT you want to delete. For example, run the following command to delete a
  PAT with an ID of `123EXAMPLE`.

```
aws codecatalyst delete-access-token --id `a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb`
```

If
successful, this command returns no
response.
