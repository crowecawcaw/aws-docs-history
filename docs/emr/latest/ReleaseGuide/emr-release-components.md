# About Amazon EMR Releases

An Amazon EMR release is a set of open-source applications from the big-data ecosystem. Each
release comprises different big-data applications, components, and features that you select
to have Amazon EMR install and configure when you create a cluster. Applications are packaged
using a system based on [Apache BigTop](http://bigtop.apache.org/ "http://bigtop.apache.org/"), which
is an open-source project associated with the Hadoop ecosystem. This guide provides information for applications included in Amazon EMR releases.

For more information about getting started and working with Amazon EMR, see the [Amazon EMR Management Guide](../ManagementGuide.md "../ManagementGuide.md").

When you launch a cluster, you can choose from multiple releases of Amazon EMR. This allows you to test and use application versions that fit your compatibility requirements.
You specify the release number with the _release label_. Release labels are in the form `emr-`x.x.x``. For example, `emr-7.11.0`.

Beginning with Amazon EMR 5.18.0, you can use the Amazon EMR artifact repository to build your job code against the exact versions of libraries and dependencies that are available with specific Amazon EMR releases. For more information, see [Checking dependencies using the Amazon EMR artifact repository](emr-artifact-repository.md "emr-artifact-repository.md").

To get updates when a new Amazon EMR release is available, subscribe to the [RSS feed for Amazon EMR release notes](amazon-emr-release-notes.md "amazon-emr-release-notes.md").

**Latest release** details, including application versions, release notes, components, and configuration classifications of Amazon EMR 7.x, 6.x, and 5.x series:

- [Amazon EMR Release 7.11.0](emr-7110-release.md "emr-7110-release.md")
- [Amazon EMR Release 6.15.0](emr-6150-release.md "emr-6150-release.md")
- [Amazon EMR Release 5.36.2](emr-5362-release.md "emr-5362-release.md")

###### Note

New Amazon EMR releases are made available in different Regions over a period of several days, beginning with the first Region on the initial release date. The latest release version may not be available in your Region during this period.

**Release notes** for the latest Amazon EMR releases and a history of all releases:

- [What's new?](emr-whatsnew.md "emr-whatsnew.md")
- [Amazon EMR archive of release notes](emr-whatsnew-history.md "emr-whatsnew-history.md")
  **A comprehensive history of application versions** in each Amazon EMR release:

- [Application versions in Amazon EMR 7.x
  releases](emr-release-app-versions-7.md "emr-release-app-versions-7.md")
- [Application versions in Amazon EMR 6.x releases](emr-release-app-versions-6.md "emr-release-app-versions-6.md")
- [Application versions in Amazon EMR 5.x releases](emr-release-app-versions-5.md "emr-release-app-versions-5.md")
- [Application versions in Amazon EMR 4.x releases](emr-release-app-versions-4.md "emr-release-app-versions-4.md")
  **Details for each Amazon EMR release** and differences between release series, where applicable:

- [Amazon EMR 7.x release versions](emr-release-7x.md "emr-release-7x.md")
- [Amazon EMR 6.x release versions](emr-release-6x.md "emr-release-6x.md")
- [Amazon EMR 5.x release versions](emr-release-5x.md "emr-release-5x.md")
- [Amazon EMR 4.x release versions](emr-release-4x.md "emr-release-4x.md")
- [Amazon EMR 2.x and 3.x AMI versions](emr-release-3x.md "emr-release-3x.md")
