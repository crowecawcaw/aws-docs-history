Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Working with attachments

You can add attachments to issues in CodeCatalyst to make related files easily
accessible. Use the following procedure to manage attachments for an issue.

The size of attachments added to issues counts towards your space's storage
quotas. For information about viewing and managing attachments for your project, see
[Viewing and managing attachments](issues-settings-attachments.md "issues-settings-attachments.md").

###### Important

Attachments to issues are not scanned or analyzed by Amazon CodeCatalyst. Any user
could add an attachment to an issue that might potentially contain malicious
code or content. Make sure that users are aware of best practices when it comes
to managing attachments and guarding against malicious code, content, or
viruses.

###### To add, download, or remove attachments

1. Choose the issue for which you want to manage attachments. For help on
   finding your issue, see [Finding and viewing issues](issues-view.md "issues-view.md").
2. To add an attachment, choose **Upload file**. Navigate to
   the file in your operating system's file explorer and select it. Choose
   **Open** to add it as an attachment. For quota
   information, such as maximum attachment size, see [Quotas for issues in CodeCatalyst](issues-quotas.md "issues-quotas.md").

Note the following restrictions to attachment file names and content
types:

    * The following characters are not permitted in file names:




    	+ Control characters: `0x00–0x1f` and
    	 `0x80–0x9f`
    	+ Reserved characters: `/`, `?`,
    	 `<`, `>`, `\`,
    	 `:`, `*`, `|`, and
    	 `"`
    	+ Unix reserved filenames: `.` and
    	 `..`
    	+ Trailing periods and spaces
    	+ Windows reserved filenames: `CON, PRN, AUX, NUL,
    	 COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9,
    	 LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, and
    	 LPT9`
    * The content type of the attachment must adhere to the following
     media-type pattern:



    ```
    media-type = type "/" [tree "."] subtype ["+" suffix]* [";" parameter];
    ```

    For example, `text/html; charset=UTF-8`.

3. To download an attachment, choose the ellipses menu next to the attachment
   you want to download and choose **Download**.
4. To copy an attachment's URL, choose the ellipses menu next to the
   attachment of which you want to copy the URL and choose **Copy
   URL**.
5. To remove an attachment, choose the ellipses menu next to the attachment
   you want to remove and choose **Delete**.
