# Managing email templates

In addition to [creating email
templates](send-personalized-email-api.md "send-personalized-email-api.md"), you can also use the Amazon SES v2 API to update or delete existing templates,
to list all of your existing templates, or to view the contents of a template.

This section contains procedures for using the AWS CLI to perform tasks related to
SES templates.

###### Note

The procedures in this section assume that you've already installed and configured the
AWS CLI. For more information about installing and configuring the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

## Viewing a list of email

templates

You can use the [`ListEmailTemplate`](../APIReference-V2/API_ListEmailTemplate.md "../APIReference-V2/API_ListEmailTemplate.md") SES v2 API operation to view a
list of all of your existing email templates.

###### To view a list of email templates

- At the command line, enter the following command:

```
aws sesv2 list-email-templates
```

If there are existing email templates in your SES account in the
current Region, this command returns a response that resembles the following
example:

```
{
    "TemplatesMetadata": [
        {
            "Name": "SpecialOffers",
            "CreatedTimestamp": "2020-08-05T16:04:12.640Z"
        },
        {
            "Name": "NewsAndUpdates",
            "CreatedTimestamp": "2019-10-03T20:03:34.574Z"
        }
    ]
}
```

If you haven't created any templates, the command returns a
`TemplatesMetadata` object with no members.

## Viewing the contents of a

specific email template

You can use the [`GetEmailTemplate`](../APIReference-V2/API_GetEmailTemplate.md "../APIReference-V2/API_GetEmailTemplate.md") SES v2 API operation to view the
contents of a specific email template.

###### To view the contents of an email template

- At the command line, enter the following command:

```
aws sesv2 get-email-template --template-name `MyTemplate`
```

In the preceding command, replace `MyTemplate` with
the name of the template that you want to view.

If the template name that you provided matches a template that exists in your
SES account, this command returns a response that resembles the following
example:

```
{
    "Template": {
        "TemplateName": "TestMessage",
        "SubjectPart": "Amazon SES Test Message",
        "TextPart": "Hello! This is the text part of the message.",
        "HtmlPart": "<html>\n<body>\n<h2>Hello!</h2>\n<p>This is the HTML part of the message.</p></body>\n</html>"
    }
}
```

If the template name that you provided doesn't match a template that exists in
your SES account, the command returns a `NotFoundException`
error.

## Deleting an email

template

You can use the [`DeleteEmailTemplate`](../APIReference-V2/API_DeleteEmailTemplate.md "../APIReference-V2/API_DeleteEmailTemplate.md") SES v2 API operation to delete
a specific email template.

###### To delete an email template

- At the command line, enter the following command:

```
aws sesv2 delete-email-template --template-name `MyTemplate`
```

In the preceding command, replace `MyTemplate` with
the name of the template that you want to delete.

This command doesn't provide any output. You can verify that the template was
deleted by using the [GetTemplate](#send-personalized-email-manage-templates-get "#send-personalized-email-manage-templates-get")
operation.

## Updating an email

template

You can use the [`UpdateEmailTemplate`](../APIReference-V2/API_UpdateEmailTemplate.md "../APIReference-V2/API_UpdateEmailTemplate.md") SES v2 API operation to update
an existing email template. For example, this operation is helpful if you want to change
the subject line of the email template, or if you need to modify the body of the message
itself.

###### To update an email template

1. Use the `GetEmailTemplate` command to retrieve the existing
   template by entering the following command on the command line:

```
aws sesv2 get-email-template --template-name `MyTemplate`
```

In the preceding command, replace `MyTemplate` with
the name of the template that you want to update.

If the template name that you provided matches a template that exists in your
SES account, this command returns a response that resembles the following
example:

```
{
    "Template": {
        "TemplateName": "TestMessage",
        "SubjectPart": "Amazon SES Test Message",
        "TextPart": "Hello! This is the text part of the message.",
        "HtmlPart": "<html>\n<body>\n<h2>Hello!</h2>\n<p>This is the HTML part of the message.</p></body>\n</html>"
    }
}
```

2. In a text editor, create a new file. Paste the output of the previous command
   into the file.
3. Modify the template as needed. Any lines that you omit are removed from the
   template. For example, if you only want to change the `SubjectPart`
   of the template, you still need to include the `TextPart` and
   `HtmlPart` properties.

When you finish, save the file as
`update_template.json`. 4. At the command line, enter the following command:

```
aws sesv2 update-email-template --cli-input-json file://`path/to/update_template.json`
```

In the preceding command, replace
`path/to/update_template.json` with the path to the
`update_template.json` file that you created in the
previous step.

If the template is updated successfully, this command doesn't provide any
output. You can verify that the template was updated by using the [`GetEmailTemplate`](../APIReference-V2/API_GetEmailTemplate.md "../APIReference-V2/API_GetEmailTemplate.md") operation.

If the template that you specified doesn't exist, this command returns a
`TemplateDoesNotExist` error. If the template doesn't contain
either the `TextPart` or `HtmlPart` property (or both),
this command returns an `InvalidParameterValue` error.
