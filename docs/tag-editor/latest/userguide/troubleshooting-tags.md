# Troubleshooting tag changes

The following checklist might be helpful if errors occur when you try to apply or change
tags on selected resources in [Find resources to tag](find-resources-to-tag.md "find-resources-to-tag.md")
query results.

- The resource might already have the maximum number of tags. Generally, resources
  can have a maximum of 50 user-defined tags. AWS generated tags don't count toward
  the 50-tag maximum. Other users might also be adding tags to the same resource at
  the same time, which could raise the resource's tags to the maximum.
- Some services allow a different character set (or restrict the character set that
  is allowed) for creating tags. If you added or changed tags using special
  characters, review the tag requirements in the resource's service documentation to
  verify that those characters are allowed by the service.
- You might not have permissions to modify the tags for the resource. If you don't
  have permissions to view existing tags on a resource, you can't make changes to the
  resource's tags.
- You might not have permissions to change the resource. Changes to the resource's
  metadata might be restricted by another administrator.
- The resource might have been edited or deleted by another user or process. For
  example, assume that a resource was launched as part of the creation of an AWS CloudFormation
  stack. If the stack was deleted or is no longer in an active state, the resource
  might no longer be available.
- Tag changes might not be possible if a resource is offline or terminated, or if
  other updates (such as software upgrades) to the resource are in progress.
- Tag changes can fail if you close the browser tab or change the page before the
  tag changes complete. Let tag changes finish, and wait for the success or failure
  banner to appear on the page, before you leave the page.
- While there's a rate limit for the AWS Resource Groups Tagging API, the service you're tagging might
  impose a separate limit which you might hit before the Resource Groups Tagging API limit.

## Retry failed tag changes

If tag changes fail on at least one of your selected resources, Tag Editor displays a red
banner at the bottom of the page. The banner shows an error message for each type of
failure that occurs. For each error, the banner identifies the specific resources on
which Tag Editor couldn't make tag changes. After you review and [troubleshoot the errors](troubleshooting-tags.md "troubleshooting-tags.md"), choose
**Retry failed tag changes on resources** to retry changes on only
those resources on which tag changes failed.
