# EUCPERF10-BP04 Remove caches, temporary data, log files, and unneeded files such as

tutorials and sample data before creating an image

Remove non-required files that are installed, downloaded, or created by applications to
optimize storage consumption.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Remove unneeded files from images to optimize storage consumption.

Unnecessary files included in an Amazon WorkSpaces golden image use space for each WorkSpace
provisioned using that image. Similarly, for Amazon AppStream 2.0 where the image builder
volume size is limited, removing unneeded files can provide additional storage space for
other applications.

Consider data access patterns and whether data not included in an image can be
downloaded when needed. For example, if 10% of users access an application library that
can be downloaded when needed, omit the library from images.
