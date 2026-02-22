# Organize, collaborate, and share

resources with spaces in Amazon Quick

A space in Amazon Quick is a collection of data and Quick resources scoped for
a particular team or domain. You can use spaces to aggregate and organize files, dashboards,
topics, knowledge bases, and application actions into a unified and customizable knowledge
center for your team. Spaces integrate seamlessly with Quick agents for
contextual conversations and are designed to scale across personal, team, and cross-team use
cases.

Spaces allow your team to get the most relevant results from conversational agents and
other AI tools inside Quick by grounding the results with only data relevant for
your task or domain. Multiple people on the team can contribute to the knowledge inside a
space; this reduces data silos and streamline information discovery.

###### Note

Quick resources added to a space respect user access permissions. If a
user can't access a resource outside a space, they won't be able to access it inside a
space. Files uploaded to a space are always available to everyone with access to the
space.

You can use spaces to accomplish tasks like:

- Aggregating and sharing customer feedback, allowing any team member to ask
  questions and get summaries
- Onboarding new team members with team documents, manuals, and processes
- Analyzing hundreds of annual reports
- Summarizing and search for action items from audio meeting recordings

###### Topics

- [Amazon Quick user interactions with
  spaces](#spaces-user-interactions "#spaces-user-interactions")
- [Amazon Quick user permission for spaces](#user-space-permissions "#user-space-permissions")
- [Understanding file upload status](#file-upload-statuses "#file-upload-statuses")
- [Limitations of spaces](#space-quotas "#space-quotas")
- [Creating a space](creating-spaces.md "creating-spaces.md")
- [Managing a space](managing-spaces.md "managing-spaces.md")

## Amazon Quick user interactions with

spaces

The following table shows how each user type in Amazon Quick interacts with
spaces.

| User type                       | Capabilities                                                                                                                                                                                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrators                  | • Control whether users with space creation capabilities can<br>create spaces                                                                                                                                                                       |
| Author Pro and Reader Pro users | • Create and maintain spaces<br>• Add topics, dashboards, knowledge bases, and application<br>actions to spaces<br>• Upload files directly into spaces<br>• Attach an agent to a space<br>• Interact with space data through chat<br>• Share spaces |

## Amazon Quick user permission for spaces

What you can do with a space also depends on the permissions you're assigned for it.
There are two permission types that users can be assigned:

- **Owner** – Owners can create, edit,
  share, and delete a space.
- **Viewer** – Viewers can view ask
  questions, and download files from spaces.

The following table outlines how user permissions determine what you can do with a
Amazon Quick space:

| Permissions type | Permissions                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owners           | • Create a space<br>• Upload files to a space<br>• Share spaces with others<br>• Link and unlink Amazon Quick resources (topics,<br>dashboards, knowledge bases, and application actions) to a<br>space<br>• Delete a space<br>As an owner, you can designate another user co-owner of a space.<br>If you do so, the user can undertake all post-creation management<br>actions an owner can. |
| Viewers          | • Download files uploaded into a space<br>• Ask questions from data inside space<br>• Use a specific space as context for an agent<br>• Search for a space by name<br>• Access a space using a direct URL<br>• View a preset list sample questions to help get started on<br>using the space                                                                                                  |

## Understanding file upload status

When you upload files, you should see the following status messages:

**Uploading**

Files are being uploaded into your computer.

**Processing**

Files are being processed.

**Text ready**

The text content of the document is ready to be queried. However, the
document's images and tables are still processing.

**Ready**

The text and media of the document has been processed.

**Deleting**

The document is being deleted.

## Limitations of spaces

The following list outlines the limitations of spaces:

- A space can't contain other spaces.
- Users can't access Amazon Quick resouces (topics, dashboards) in a space if
  they don't have access to the resource outside it. Sharing a space doesn't
  automatically give access to users to assets within it.
- If an Amazon Quick resource is linked to a space is deleted outside the space,
  users of the space won't get notified of the deletion. Deleted assets will only
  display a message indicating unavailability.
- Files uploaded to spaces will be rejected if your index data storage capacity
  is full. Reach out to your system administrator if this happens.
- Files uploaded to a space must be one of the following formats:
  `.html`, `.ppt`, `.docx`,
  `.txt`, `.pdf`, `.csv`, `.xlsx`,
  `.xml`, `.jpeg`, `.svg`
  `.json`, `.md`
  `.rtf`, `.xslt`
  `.mp3`, `.wav`
  `.m4a`, `.flac`, `.ogg`, `.mp4`,
  `.mov`, `.m4v`.

###### Note

You can only upload JPG images to spaces. PNG is not supported at this
time.

- File uploads are limited to 10 MB for Excel and CSV files, and 50 MB for all
  other supported file types. You will get a "character limit exceeded" error when
  you upload larger documents.
- Spaces support up to 10,000 files (compared to 20 files in regular chat
  conversations), as long as the total space storage is less than 1 GB.
- You can add at most 20 resources of a specific resource type (dashboard,
  topic, knowledge base, or action) to a space.
