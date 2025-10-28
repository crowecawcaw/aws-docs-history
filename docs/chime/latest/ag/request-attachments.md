**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Requesting user attachments

If you manage an Enterprise account and have the appropriate permissions, you can
request and receive the attachments that your users upload into Amazon Chime. You
can get attachments that users uploaded into 1:1 and group conversations, or into chat
rooms that they created.

###### Note

If you manage an Amazon Chime Team account, you can upgrade to an Enterprise account by
claiming one or more domains. Alternatively, you can remove users from the Team
account, which enables those unmanaged users to get their attachments using the
Amazon Chime Assistant.

###### To request user attachments

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. On the **Accounts** page, select the name of the Amazon Chime
   account.
3. Under **Settings**, choose **Account**,
   **Account actions**, **Request
   attachments**.
4. Within approximately 24 hours, the **Account summary** page
   provides a link to a file containing a list of presigned URLs that you use to
   access each attachment.
5. Download the file.

###### Note

Be sure to maintain an appropriate level of access control on the file.
Any user that obtains the file can use the provided list of URLs to download
the associated attachments.

Presigned URLs expire after 6 days. You can submit a request one time
every 7 days.
To use AWS Identity and Access Management (IAM) policies to manage access to the Amazon Chime administration console
and the **Request attachments** action, use one of the Amazon Chime managed
policies (FullAccess, UserManagement, or ReadOnly). Alternatively, you can update the
custom policies to include the `StartDataExport` action and
`RetrieveDataExport` action. For more information about these actions,
see [Actions defined by Amazon Chime](../../../IAM/latest/UserGuide/list_amazonchime.md#amazonchime-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonchime.md#amazonchime-actions-as-permissions") in the
_IAM User Guide_.
