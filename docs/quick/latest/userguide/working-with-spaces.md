

# Organize, collaborate, and share resources with spaces in AWS Quick

A space in AWS Quick is a collection of data and Quick resources scoped for a particular team or domain. You can use spaces to aggregate and organize files, dashboards, topics, knowledge bases, and application actions into a unified and customizable knowledge center for your team. Spaces integrate seamlessly with Quick agents for contextual conversations and are designed to scale across personal, team, and cross-team use cases.

Spaces allow your team to get the most relevant results from conversational agents and other AI tools inside Quick by grounding the results with only data relevant for your task or domain. Multiple people on the team can contribute to the knowledge inside a space; this reduces data silos and streamline information discovery. Spaces also serve as a data layer for apps in AWS Quick applications. For more information, see [Build web applications with apps in AWS Quick](using-amazon-quick-apps.md).

**Note**  
Quick resources added to a space respect user access permissions. If a user can't access a resource outside a space, they won't be able to access it inside a space. Files uploaded to a space are always available to everyone with access to the space.

Your spaces and the data in them are available wherever you work with Quick, across the web, desktop, and mobile. To focus a conversation on a space, add the space to the conversation so Quick grounds its responses in that space's content.

You can use spaces to accomplish tasks like:
+ Aggregating and sharing customer feedback, allowing any team member to ask questions and get summaries
+ Onboarding new team members with team documents, manuals, and processes
+ Analyzing hundreds of annual reports
+ Summarizing and search for action items from audio meeting recordings

**Topics**
+ [AWS Quick user interactions with spaces](#spaces-user-interactions)
+ [AWS Quick user permission for spaces](#user-space-permissions)
+ [Understanding file upload status](#file-upload-statuses)
+ [Limitations of spaces](#space-quotas)
+ [Creating a space](creating-spaces.md)
+ [Managing a space](managing-spaces.md)

## AWS Quick user interactions with spaces
<a name="spaces-user-interactions"></a>

The following table shows how each user type in AWS Quick interacts with spaces.


| User type | Capabilities | 
| --- | --- | 
| Administrators |  +  Control whether users with space creation capabilities can create spaces   | 
| All other users |  +  Create and maintain spaces <br />+  Add topics, dashboards, datasets, knowledge bases, and application actions to spaces <br />+  Upload files directly into spaces <br />+  Attach an agent to a space <br />+  Interact with space data through chat <br />+  Share spaces   | 

## AWS Quick user permission for spaces
<a name="user-space-permissions"></a>

What you can do with a space also depends on the permissions you're assigned for it. There are two permission types that users can be assigned:
+ **Owner** – Owners can create, edit, share, and delete a space.
+ **Viewer** – Viewers can view ask questions, and download files from spaces.

The following table outlines how user permissions determine what you can do with a AWS Quick space:


| Permissions type | Permissions | 
| --- | --- | 
| Owners | +  Create a space <br />+  Upload files to a space <br />+  Share spaces with others <br />+  Link and unlink AWS Quick resources (topics, dashboards, datasets, knowledge bases, and application actions) to a space <br />+  Delete a space As an owner, you can designate another user co-owner of a space. If you do so, the user can undertake all post-creation management actions an owner can. | 
| Viewers |  +  Download files uploaded into a space <br />+  Ask questions from data inside space <br />+  Use a specific space as context for an agent <br />+  Search for a space by name <br />+  Access a space using a direct URL <br />+  View a preset list sample questions to help get started on using the space   | 

## Understanding file upload status
<a name="file-upload-statuses"></a>

When you upload files, you should see the following status messages:

**Uploading**  
Files are being uploaded into your computer.

**Processing**  
Files are being processed.

**Text ready**  
The text content of the document is ready to be queried. However, the document's images and tables are still processing.

**Ready**  
The text and media of the document has been processed.

**Deleting**  
The document is being deleted.

## Limitations of spaces
<a name="space-quotas"></a>

The following list outlines the limitations of spaces:
+ A space can't contain other spaces.
+ Users must have access to AWS Quick resources outside a space to access them within it. Sharing a space doesn't automatically grant access to the assets in the space.
+ If an AWS Quick resource in a space is deleted outside the space, users aren't notified. A deleted resource displays a message that it's no longer available.
+ Files uploaded to spaces will be rejected if your index data storage capacity is full. Reach out to your system administrator if this happens.
+ Files uploaded to a space must be one of the following formats: `.html`, `.xhtml`, `.txt`, `.pdf`, `.csv`, `.tsv`, `.xml`, `.json`, `.md`, `.rtf`, `.xslt`, `.eml`, `.vtt`, `.docx`, `.dotx`, `.docm`, `.dotm`, `.ppt`, `.pptx`, `.pptm`, `.ppsm`, `.ppsx`, `.xlsx`, `.xls`, `.xlam`, `.xlsm`, `.xltx`, `.xltm`, `.c`, `.h`, `.cpp`, `.hpp`, `.cs`, `.java`, `.py`, `.go`, `.rb`, `.scala`, `.m`, `.sql`, `.clj`, `.mp3`, `.wav`, `.m4a`, `.flac`, `.ogg`, `.mp4`, `.mov`, `.m4v`.
+ File uploads are limited to 500 MB for PDF, Word, and PowerPoint files, and 50 MB for all other supported file types.
+ Spaces support up to 10,000 files (compared to 20 files in regular chat conversations), as long as the total space storage is less than 10 GB.
+ You can add at most 20 resources of a specific resource type (dashboard, topic, knowledge base, or action) to a space.