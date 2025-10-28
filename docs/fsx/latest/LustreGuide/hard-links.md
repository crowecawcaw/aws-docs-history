# Hard links and exporting to Amazon S3

If automatic export (with NEW and CHANGED policies) is enabled on a DRA
in your file system, each hard link contained within the DRA is exported to
Amazon S3 as a separate S3 object for each hard link. If a file with multiple hard
links is modified on the file system, all of the copies in S3 are updated,
regardless of which hard link was used when changing the file.

If hard links are exported to S3 using data repository tasks (DRTs),
each hard link contained within the paths specified for the DRT is exported
to S3 as a separate S3 object for each hard link. If a file with multiple
hard links is modified on the file system, each copy in S3 is updated at
the time the respective hard link is exported, regardless of which hard link
was used when changing the file.

###### Important

When a new FSx for Lustre file system is linked to an S3 bucket
to which hard links were previously exported by another FSx for Lustre file system,
AWS DataSync, or Amazon FSx File Gateway, the hard links are subsequently imported as
separate files on the new file system.

## Hard links and released files

A released file is a file whose metadata is present in the file system, but
whose content is only stored in S3. For more information on released files,
see [Releasing files](file-release.md "file-release.md").

###### Important

The use of hard links in a file system that has data repository
associations (DRAs) is subject to the following limitations:

- Deleting and recreating a released file that has multiple
  hard links may cause the content of all hard links to be overwritten.
- Deleting a released file will delete content from all
  hard links that reside outside of a data repository association.
- Creating a hard link to a released file whose corresponding S3 object is in either of the
  S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes will
  not create a new object in S3 for the hard link.
