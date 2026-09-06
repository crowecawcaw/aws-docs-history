

# Internal firewall or missing CORS policy prevents access to chat, email, task, or case attachments
<a name="ts-agent-attachments"></a>

This topic is for developers who need to investigate issues that might occur when using attachments with the chat, email, or task channels in Connect Customer, or when using attachments to upload files to cases.

The following issues might cause attachments to not display for your agents using Connect Customer chat, email, or tasks, or Connect Customer Cases. 

## Configure a CORS policy on your attachments bucket
<a name="cors-policy-not-configured"></a>

A common reason for attachments not appearing in chats, emails, or tasks is that the CORS policy hasn't been configured on your attachments bucket. For instructions, see [Step 4: Configure a CORS policy on your attachments bucket](enable-attachments.md#step4-update-cors-policy). 

## Internal firewall settings are preventing access
<a name="update-firewall-settings"></a>

 Check that your firewall isn't preventing agents from accessing the files in your Amazon S3 bucket. You might need to add the Amazon S3 bucket where your files are stored to your domain allowlist. For more information, see [Set up your network to use the Connect Customer Contact Control Panel (CCP)](ccp-networking.md). 

## Attachments are too large, too many, or don't meet file type requirements
<a name="check-attachment-size"></a>

Check that the attachments meet the size, number, and file type requirements. For more information, see [Connect Customer feature specifications](feature-limits.md).

The maximum attachment size is configurable up to 100 MB. The default is 20 MB. If attachments are being rejected, verify the configured size limit for your instance through the Connect Customer admin website or the Connect Customer API.

To calculate the size of an attachment (artifactSizeInBytes), use a third-party tool such as [ File.size](https://developer.mozilla.org/en-US/docs/Web/API/File/size).

## File type is rejected even though it is expected to be allowed
<a name="check-custom-file-extensions"></a>

If a file type is rejected when uploading an attachment, verify that the file extension has been added to the allowed file extensions list for your instance. For information about configuring custom file extensions, see [Enable attachments in your CCP so customers and agents can share and upload files](enable-attachments.md).

For a list of default supported file types, see [Connect Customer feature specifications](feature-limits.md).