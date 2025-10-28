# Best Practice 14.1 – Create mount

points and volume associations to align with function

SAP filesystems have unique performance and sharing requirements. For example, the
performance profile of the database may require the data filesystem to support a high
number of read I/O operations, while the log filesystem is more likely to be constrained
by throughput. Filesystems such as `sapmnt` and `trans` need to be
shared so that all application servers can access logs and transport files. Recognizing
these differences, consider the mapping of filesystems to volumes to ensure there are no
performance bottlenecks and that access requirements are met.

**Suggestion 14.1.1 – Identify the SAP filesystems and directory
requirements for each System**

SAP filesystems include system directories (root, boot), executables, page or swap,
and application-specific requirements. Each of these should be analyzed to consider:

- The impact when a file system is at capacity (100% used), particularly for the
  root directory
- Consistency of build, including whether it is included in an AMI, or deployment
  patterns
- Resilience requirements
- Sharing requirements
- Performance profile
  The core SAP filesystem requirements are listed in the SAP documentation. Use these as
  a baseline and include other requirements specific to your organization.

- SAP Documentation: [SAP Required Filesystems and Directories](https://help.sap.com/docs/SLTOOLSET/910828cec5d14d6685da380aec1dc4ae/de6cad1446a743d3853dbcae48bddfba.html?version=CURRENT_VERSION "https://help.sap.com/docs/SLTOOLSET/910828cec5d14d6685da380aec1dc4ae/de6cad1446a743d3853dbcae48bddfba.html?version=CURRENT_VERSION")

**Suggestion 14.1.2 – Map the appropriate AWS storage service to
match with filesystem function**

A filesystem can either be local or shared (NFS / SMB). For shared filesystems
consider using AWS services, such as Amazon EFS and Amazon FSx, which provide
reliability and availability benefits when compared with a hosted NFS server.

Amazon EC2 instance store is another filesystem option which provides temporary
block-level storage for your instance. We do not recommend its use due to lack of
persistence, availability across instance types, and because it prevents the use of
instance recovery.

**Suggestion 14.1.3 – Use supported filesystem types**

The SAP-supported Linux distributions recommend a number of different file system
types. Later versions are standardizing on XFS, but support should be reviewed to ensure
there is no performance or functionality impact for your operating system and database
version.

- SAP Note: [405827 -
  Linux: Recommended file systems](https://launchpad.support.sap.com/#/notes/405827 "https://launchpad.support.sap.com/#/notes/405827") [Requires SAP Portal Access]
- SAP Note: [2972496

* SAP HANA Filesystem Types](https://launchpad.support.sap.com/#/notes/2972496 "https://launchpad.support.sap.com/#/notes/2972496") [Requires SAP Portal Access]
