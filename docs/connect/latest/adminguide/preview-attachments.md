

# Preview attachments in the agent workspace
<a name="preview-attachments"></a>

Agents can preview an attachment on an email contact, a chat contact, or a case directly in the agent workspace, without downloading it to their device. Previewing keeps customer files off agent machines, and it is faster than downloading a file and opening it in a separate application.

When an attachment is a supported file type, Amazon Connect Customer renders it inline in the preview gallery. When it isn't, or when it can't be rendered, the gallery shows the file's details and a **Download** button in place of the rendered content. Either way, the agent can still download the file as usual.

## Prerequisites
<a name="preview-attachments-prerequisites"></a>

Before agents can preview attachments, the following must be true:
+ **Attachments are enabled for your instance.** Preview works only on files shared through attachments. See [Enable attachments in your CCP so customers and agents can share and upload files](enable-attachments.md).
+ **Attachments have passed scanning, if scanning is set up.** If attachment scanning is set up for your instance, an agent can preview an attachment only after scanning approves it. Files that scanning rejects are never previewable or downloadable. See [Set up attachment scanning in Connect Customer](setup-attachment-scanning.md).
+ **Agents use the agent workspace.** Preview is not available in custom agent applications built on the Connect Customer Streams API.

## Supported file types for preview
<a name="preview-attachments-supported-types"></a>

Amazon Connect Customer renders the following file types inline in the preview gallery.


| Preview type | File extensions | 
| --- | --- | 
| Document | .pdf | 
| Image | .jpg, .jpeg, .jfif, .png, .gif, .webp, .bmp | 
| Text | .txt, .log, .csv, .json, .xml | 

File types that aren't in this table, such as `.docx`, `.xlsx`, `.zip`, or `.eml`, can't be previewed, but agents can still download them. For the file types that can be attached in the first place, see [Connect Customer feature specifications](feature-limits.md).

Note the following behavior for specific file types and sizes:
+ **`.svg` and `.html` files can't be previewed**, even in browsers capable of rendering them. Because both formats can embed potentially malicious executable scripts, Connect Customer blocks their preview to mitigate security risks.
+ **Large attachments might not render inline.** When an attachment is too large to render, the agent sees the file's details and a **Download** button instead.
+ **Long files preview only partially.** For long files, the preview shows only a portion of the content. Agents can download the file to view its complete contents.

## How agents preview an attachment
<a name="preview-attachments-how-to"></a>

1. Agents open an email contact, a chat contact, or a case in the agent workspace. Attachments, if present, appear as a list of file names.

1. Agents can then choose an attachment to view it in the preview gallery, or choose **View all** to open the gallery at the first attachment.

1. In the gallery, the agent can do the following:
   + Move between the attachments by using **Previous attachment** and **Next attachment**, or the thumbnail strip. The thumbnail strip appears when there is more than one attachment.
   + Scroll through a multi-page PDF.
   + Choose **Open in new window** to view the attachment at a larger size in a separate browser window. This is useful for attachments with fine detail, such as multi-page PDFs or images that contain small text. The agent workspace stays open, and the agent can close the window to return to it.
   + Choose **Download** to download the file.

1. Agents can choose **Close preview** to close the gallery and return to the contact.

![The preview gallery open on a PDF attachment, with the thumbnail strip, Open in new window, and Download.](https://docs.aws.amazon.com/connect/latest/adminguide/images/preview-attachments-gallery-pdf.png)


## When a preview isn't available
<a name="preview-attachments-unavailable"></a>

When a file can't be previewed in the agent workspace, the gallery shows the file's name and size with a **Download** button instead of rendered content. Files can't be previewed for the following reasons:
+ The file type isn't listed in [Supported file types for preview](#preview-attachments-supported-types).
+ The file is too large to render inline.
+ Attachment scanning is enabled and has not yet approved the attachment.

![The preview gallery showing an unsupported file type: the file name, size, and a Download button, with no rendered content.](https://docs.aws.amazon.com/connect/latest/adminguide/images/preview-attachments-gallery-unsupported.png)


## Considerations
<a name="preview-attachments-considerations"></a>
+ Preview is available for attachments on email contacts, chat contacts, and cases in the agent workspace.
+ Previews are for viewing an attachment in place. To work with a file, the agent chooses **Download**, or **Open in new window** for a larger view.
+ The preview gallery is localized to all languages that the agent workspace supports.