# Listing LF-Tag permissions using the

console

You can use the Lake Formation console to view the permissions granted on LF-Tags. You must be a
LF-Tag creator, a data lake administrator, or have the `Describe` or `Associate` permission
on a LF-Tag to see it.

###### To list LF-Tag permissions (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as the LF-Tag creator, a data lake administrator, or as a user to whom the `Drop`, `Alter`, `Associate`,
or `Describe` permissions on LF-Tags have been granted. 2. In the navigation pane, under **Permissions**, choose **LF-Tags and permissions**, and
choose **LF-Tag permissions** section.

The **LF-Tag permissions** section shows a table that contains principal, tag keys, values, and permissions.

![The page includes a table of permissions with the following columns: Principal, Principal type, Keys, Values, Permissions, and Grantable. There are five rows. To the left of each row is a radio button. Above the table are a search field and these buttons: Refresh, View, Revoke, and Grant. Because no row is initially selected, the View and Revoke buttons are disabled. The values in the first row are: Principal=arn:aws:iam::111122223333:user/datalake_admin, Principal type=IAM user, Keys=environment, Values=All values, Permissions=DESCRIBE, Grantable=DESCRIBE.](images/list-tag-permissions-page.png)
