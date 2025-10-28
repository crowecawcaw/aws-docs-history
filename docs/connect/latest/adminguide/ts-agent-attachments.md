# Internal firewall or missing CORS policy prevents

access to chat, email, or case attachments

This topic is for developers who need to investigate issues that may occur when using
attachments with the chat or email channels in Amazon Connect, or when using attachments to
upload files to cases.

The following issues may cause attachments to not display for your agents using Amazon Connect
chat or email, or Amazon Connect Cases.

## Configure a CORS policy on your

attachments bucket

A common reason for attachments not appearing in chats or emails is that the CORS
policy hasn't been configured on your attachments bucket. For instructions, see
[Step 2: Configure a CORS policy on your
attachments bucket](enable-attachments.md#step2-update-cors-policy "enable-attachments.md#step2-update-cors-policy").

## Internal firewall settings are preventing

access

Check that your firewall isn't preventing agents from accessing the files in your
Amazon S3 bucket. You may need to add the Amazon S3 bucket where your files are stored to your
domain allowlist. For more information, see [Set up your network to use the Amazon Connect Contact Control Panel
(CCP)](ccp-networking.md "ccp-networking.md").

## Attachments are too large, too many, or

don't meet file type requirements

Check that the attachments meet the size, number, and file type requirements. For
more information, see [Amazon Connect feature specifications](feature-limits.md "feature-limits.md").

To calculate the size of an attachment (artifactSizeInBytes), use a third-party
tool such as [File.size](https://developer.mozilla.org/en-US/docs/Web/API/File/size "https://developer.mozilla.org/en-US/docs/Web/API/File/size").
