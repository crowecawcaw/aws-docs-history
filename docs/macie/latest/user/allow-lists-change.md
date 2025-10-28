# Changing an allow list

After you create an allow list, you can change most of the list's settings in Amazon Macie. For
example, you can change the list's name and description. You can also add and edit tags for the
list. The only setting that you can't change is a list's type. For example, if an existing list
specifies a regular expression (_regex_), you can't change its
type to predefined text.

If an allow list specifies predefined text, you can also change the entries in the list. To
do this, update the file that contains the entries. Then upload the new version of the file to
Amazon Simple Storage Service (Amazon S3). The next time Macie prepares to use the list, Macie retrieves the latest version
of the file from Amazon S3. When you upload the new file, ensure that you store it in the same S3
bucket and object. Or, if you change the name of the bucket or object, ensure that you update the
list's settings in Macie.

###### To change the settings for an allow list

You can change the settings for an allow list by using the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to change an allow list's settings by using the Amazon Macie
console.

###### To change an allow list's settings by using the console

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**, choose
   **Allow lists**.
3. On the **Allow lists** page, choose the name of the allow list
   that you want to change. The allow list page opens and displays the current settings
   for the list.
4. To add or edit tags for the allow list, choose **Manage tags** in the
   **Tags** section. Then change the tags as necessary. When you finish,
   choose **Save**.
5. To change other settings for the allow list, choose **Edit** in
   the **List settings** section. Then change the settings that you
   want:
   - **Name** – Enter a new name for the list. The name
     can contain as many as 128 characters.
   - **Description** – Enter a new description of the
     list. The description can contain as many as 512 characters.
   - If the allow list specifies predefined text:
     - **S3 bucket name** – Enter the name of the bucket that
       stores the list.

     In Amazon S3, you can find this value in the **Name** field
     of the bucket's properties. This value is case sensitive. In addition, don't
     use wildcard characters or partial values when you enter the name.
     - **S3 object name** – Enter the name of the S3 object that
       stores the list.

     In Amazon S3, you can find this value in the **Key** field
     of the object's properties. If the name includes a path, be sure to include
     the complete path when you enter the name, for example
     `allowlists/macie/mylist.txt`. This value is case
     sensitive. In addition, don't use wildcard characters or partial values when
     you enter the name.

   - If the allow list specifies a regular expression (_regex_), enter a new regex in the **Regular
     expression** box. The regex can contain as many as 512
     characters.

   After you enter the new regex, optionally test it. To do this, enter up to
   1,000 characters in the **Sample data** box, and then choose
   **Test**. Macie evaluates the sample data and reports the
   number of occurrences of text that match the regex. You can repeat this step as
   many times as you like to refine and optimize the regex before you save your
   changes.

6. When you finish, choose **Save**.

Macie tests the list's settings. For a list of predefined text, Macie also verifies
that it can retrieve the list from Amazon S3 and parse the list's content. For a regex, Macie
also verifies that it can compile the expression. If an error occurs, Macie displays a
message that describes the error. For detailed information that can help you
troubleshoot the error, see [Configuration options and requirements for allow
lists](allow-lists-options.md "allow-lists-options.md"). After you address any errors, you can
save your changes.

API
To change an allow list's settings programmatically, use the [UpdateAllowList](../APIReference/allow-lists-id.md "../APIReference/allow-lists-id.md") operation of the
Amazon Macie API. Or, if you're using the AWS CLI, run the [update-allow-list](../../../cli/latest/reference/macie2/update-allow-list.md "../../../cli/latest/reference/macie2/update-allow-list.md") command.
In your request, use the supported parameters to specify a new value for each setting that you
want to change. Note that the `criteria`, `id`, and `name`
parameters are required. If you don't want to change the value for a required parameter,
specify the current value for the parameter.

For example, the following command changes the name and description of an existing
allow list. The example is formatted for Microsoft Windows and it uses the caret (^)
line-continuation character to improve readability.

```
`C:\>` `aws macie2 update-allow-list ^
--id `km2d4y22hp6rv05example` ^
--name `my_allow_list-email` ^
--criteria={\"regex\":\"`[a-z]@example.com`\"} ^
--description "`Ignores all email addresses for the example.com domain`"`
```

Where:

- `km2d4y22hp6rv05example` is the unique identifier for
  the list.
- `my_allow_list-email` is the new name for the
  list.
- `[a-z]@example.com` is the list's criteria, a regular
  expression.
- `Ignores all email addresses for the example.com
domain` is the new description for the list.

When you submit your request, Macie tests the list's settings. If the list specifies
predefined text (`s3WordsList`), this includes verifying that Macie can retrieve
the list from Amazon S3 and parse the list's content. If the list specifies a regex
(`regex`), this includes verifying that Macie can compile the expression.

If an error occurs when Macie tests the settings, your request fails and Macie
returns a message that describes the error. For detailed information that can help you
troubleshoot the error, see [Configuration options and requirements for allow
lists](allow-lists-options.md "allow-lists-options.md"). If the request fails for another reason,
Macie returns an HTTP 4*xx* or 500 response that
indicates why the operation failed.

If your request succeeds, Macie updates the list's settings and you receive output
similar to the following.

```
`{
 "arn": "arn:aws:macie2:us-west-2:123456789012:allow-list/km2d4y22hp6rv05example",
 "id": "km2d4y22hp6rv05example"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the allow list that was
updated, and `id` is the unique identifier for the list.
