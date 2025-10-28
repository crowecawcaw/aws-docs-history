# DLAMI Support Policy

Here you can find details of the support policy for AWS Deep Learning AMIs (DLAMI).

For a list of the DLAMI frameworks and operating system that AWS currently supports, see the [DLAMI Support
Policy](dlami-support-policy-table.md "dlami-support-policy-table.md") page. The following terminology applies to all DLAMIs mentioned in the Support policy page and this page:

- **Current version** specifies the framework version in the format
  _x.y.z_. In this format, _x_ refers to the major version, _y_ refers to the minor version, and _z_ refers to the patch version. For example, for TensorFlow 2.10.1,
  the major version is 2, the minor version is 10, and the patch version is 1.
- **End of patch** specifies how long AWS supports a particular framework or operating system
  version.
  For detailed information about specific DLAMIs, see [Deep Learning AMIs Release Notes](appendix-ami-release-notes.md "appendix-ami-release-notes.md").

## DLAMI Support FAQs

- [What framework versions get security patches?](#framework-support-policy-faq-security "#framework-support-policy-faq-security")
- [Which operating system get security patches?](#operating-system-support-policy-faq-security "#operating-system-support-policy-faq-security")
- [What images does AWS publish when new framework versions are released?](#support-policy-faq-publishing "#support-policy-faq-publishing")
- [What images get new SageMaker AI/AWS
  features?](#support-policy-faq-features "#support-policy-faq-features")
- [How is current version defined in the Supported Frameworks table?](#support-policy-faq-current-version "#support-policy-faq-current-version")
- [What if I am running a version that is not in the Supported table?](#support-policy-faq-older-version "#support-policy-faq-older-version")
- [Do DLAMIs support previous patch versions of a Framework Version?](#support-policy-faq-previous-version-support "#support-policy-faq-previous-version-support")
- [How can I find the latest patched image for a supported framework version?](#support-policy-faq-latest-patched-image "#support-policy-faq-latest-patched-image")
- [How frequently are new images released?](#support-policy-faq-new-image-frequency "#support-policy-faq-new-image-frequency")
- [Will my instance be patched in place while my workload is running?](#support-policy-faq-in-place-patch "#support-policy-faq-in-place-patch")
- [What happens when a new patched or updated framework version is available?](#support-policy-faq-new-image-available "#support-policy-faq-new-image-available")
- [Are dependencies updated without changing the framework version?](#support-policy-faq-dependencies "#support-policy-faq-dependencies")
- [When does active support for my framework version end?](#support-policy-faq-end-of-support "#support-policy-faq-end-of-support")
- [Will images with framework versions that are no longer actively maintained be patched?](#support-policy-faq-end-of-patch "#support-policy-faq-end-of-patch")
- [How do I use an older framework version?](#support-policy-faq-using-older-framework-version "#support-policy-faq-using-older-framework-version")
- [How do I stay up-to-date with support changes in frameworks and their versions?](#support-policy-faq-stay-up-to-date "#support-policy-faq-stay-up-to-date")
- [Do I need a commercial license to use the Anaconda Repository?](#support-policy-faq-anaconda-repository "#support-policy-faq-anaconda-repository")

### What framework versions get security patches?

If the framework version is under **Supported Framework Versions** in
the [AWS Deep Learning AMIs Support Policy table](dlami-support-policy-table.md "dlami-support-policy-table.md"), it gets security patches.

### Which operating system get security patches?

If the operating system is listed under **Supported Operating System Versions** in
the [AWS Deep Learning AMIs Support Policy table](dlami-support-policy-table.md "dlami-support-policy-table.md"), it gets security patches.

### What images does AWS publish when new framework versions are released?

We publish new DLAMIs soon after new versions of TensorFlow and PyTorch
are released. This includes major versions, major-minor versions, and
major-minor-patch versions of frameworks. We also update images when new versions of
drivers and libraries become available. For more information on image maintenance,
see [When does active support for my framework version end?](#support-policy-faq-end-of-support "#support-policy-faq-end-of-support")

### What images get new SageMaker AI/AWS

features?

New features typically release in the latest version of DLAMIs for
PyTorch and TensorFlow. Refer to the release notes for a specific image for details
on new SageMaker AI or AWS features. For a list of available DLAMIs, see [Release Notes for DLAMI](appendix-ami-release-notes.md "appendix-ami-release-notes.md"). For more information on image maintenance, see
[When does active support for my framework version end?](#support-policy-faq-end-of-support "#support-policy-faq-end-of-support")

### How is current version defined in the Supported Frameworks table?

The current version in the [AWS Deep Learning AMIs Support Policy table](dlami-support-policy-table.md "dlami-support-policy-table.md") refers to the newest
framework version that AWS makes available on GitHub. Each latest release includes
updates to the drivers, libraries, and relevant packages in the DLAMI. For
information on image maintenance, see [When does active support for my framework version end?](#support-policy-faq-end-of-support "#support-policy-faq-end-of-support")

### What if I am running a version that is not in the Supported table?

If you are running a version that is not in the [AWS Deep Learning AMIs Support Policy table](dlami-support-policy-table.md "dlami-support-policy-table.md"), you
may not have the most updated drivers, libraries, and relevant packages. For a more
up-to-date version, we recommend that you upgrade to one of the supported frameworks
or operating system available using the latest DLAMI of your choice. For a list of available
DLAMIs, see [Release Notes for DLAMI](appendix-ami-release-notes.md "appendix-ami-release-notes.md").

### Do DLAMIs support previous patch versions of a Framework Version?

No. We support the latest patch version of each framework’s latest major version
released 365 days from its initial GitHub release as stated in the [AWS Deep Learning AMIs Support Policy table](dlami-support-policy-table.md "dlami-support-policy-table.md"). For
more information, see [What if I am running a version that is not in the Supported table?](#support-policy-faq-older-version "#support-policy-faq-older-version")

### How can I find the latest patched image for a supported framework version?

To use a DLAMI with the latest framework version, you can use AWS CLI or SSM parameters to retrieve the [DLAMI
ID](find-dlami-id.md "find-dlami-id.md") and use it to launch the DLAMI using the [EC2 Console](launch-from-console.md "launch-from-console.md").
For sample AWS CLI or SSM parameter commands to retrieve the AWS Deep Learning AMIs ID, refer to the DLAMI release notes page [single-framework DLAMI release notes](appendix-ami-release-notes-single.md "appendix-ami-release-notes-single.md"). The framework version that you
choose must be listed under **Supported Framework Versions** in the [AWS Deep Learning AMIs Support Policy table](dlami-support-policy-table.md "dlami-support-policy-table.md").

### How frequently are new images released?

Providing updated patch versions is our highest priority. We routinely create
patched images at the earliest opportunity. We monitor for newly patched framework
versions (ex. TensorFlow 2.9 to TensorFlow 2.9.1) and new minor release versions
(ex. TensorFlow 2.9 to TensorFlow 2.10) and make them available at the earliest
opportunity. When an existing version of TensorFlow is released with a new version
of CUDA, we release a new DLAMI for that version of TensorFlow with support
for the new CUDA version.

### Will my instance be patched in place while my workload is running?

No. Patch updates for DLAMI are not “in-place” updates.

You must turn on a new EC2 instance, migrate your workloads and scripts, and then turn off your previous instance.

### What happens when a new patched or updated framework version is available?

To be notified of changes in DLAMI, please subscribe to the notifications for the relevant DLAMI, see [Receive Notifications on New Updates](release-notifications.md "release-notifications.md") .

### Are dependencies updated without changing the framework version?

We update dependencies without changing the framework version. However, if a
dependency update causes an incompatibility, we create an image with a different
version. Be sure to check the [Release Notes for DLAMI](appendix-ami-release-notes.md "appendix-ami-release-notes.md") for updated dependency information.

### When does active support for my framework version end?

DLAMI images are immutable. Once they are created they do not change.
There are four main reasons why active support for a framework version ends:

- [Framework version (patch) upgrades](#support-policy-faq-end-of-support-version-patch "#support-policy-faq-end-of-support-version-patch")
- [AWS security patches](#support-policy-faq-end-of-support-security-patch "#support-policy-faq-end-of-support-security-patch")
- [End of patch date (Aging out)](#support-policy-faq-end-of-support-aging-out "#support-policy-faq-end-of-support-aging-out")
- [Dependency end-of-support](#support-policy-faq-end-of-support-dependency "#support-policy-faq-end-of-support-dependency")

###### Note

Due to the frequency of version patch upgrades and security patches,
we recommend checking the release notes page for your DLAMI often, and upgrading when changes are made.

#### Framework version (patch) upgrades

If you have a DLAMI workload based on TensorFlow 2.7.0 and TensorFlow
releases version 2.7.1 on GitHub, then AWS releases a new DLAMI with
TensorFlow 2.7.1. The previous images with 2.7.0 are no longer actively maintained
once the new image with TensorFlow 2.7.1 is released. The DLAMI with
TensorFlow 2.7.0 does not receive further patches. The DLAMI release
notes page for TensorFlow 2.7 is then updated with the latest information. There
is no individual release note page for each minor patch.

New DLAMIs created due to patch upgrades are designated with a new [AMI ID](find-dlami-id.md "find-dlami-id.md").

#### AWS security patches

If you have a workload based on an image with TensorFlow 2.7.0 and AWS makes a
security patch, then a new version of the DLAMI is released for
TensorFlow 2.7.0. The previous version of the images with TensorFlow 2.7.0 is no
longer actively maintained. For more information, see [Will my instance be patched in place while my workload is running?](#support-policy-faq-in-place-patch "#support-policy-faq-in-place-patch") For
steps on finding the latest DLAMI, see [How can I find the latest patched image for a supported framework version?](#support-policy-faq-latest-patched-image "#support-policy-faq-latest-patched-image")

New DLAMIs created due to patch upgrades are designated with a new [AMI ID](find-dlami-id.md "find-dlami-id.md").

#### End of patch date (Aging out)

DLAMIs hit their end of patch date 365 days after the GitHub release date.

For [multi-framework DLAMIs](appendix-ami-release-notes-multi.md "appendix-ami-release-notes-multi.md"), when one of the framework versions is
updated, a new DLAMI with the updated version is required. The DLAMI with the
old framework version is no longer actively maintained.

###### Important

We make an exception when there is a major framework update. For example. if
TensorFlow 1.15 updates to TensorFlow 2.0, then we continue to support the most
recent version of TensorFlow 1.15 for a period of two years from the date of the
GitHub release or six months after the origin framework maintenance team drops
support, whichever date is earlier.

#### Dependency end-of-support

If you are running a workload on a TensorFlow 2.7.0 DLAMI image with
Python 3.6 and that version of Python is marked for end-of-support, then all
DLAMI images based on Python 3.6 will no longer be actively maintained.
Similarly, if an OS version like Ubuntu 16.04 is marked for end-of-support, then
all DLAMI images that are dependent on Ubuntu 16.04 will no longer be
actively maintained.

### Will images with framework versions that are no longer actively maintained be patched?

No. Images that are no longer actively maintained will not have new
releases.

### How do I use an older framework version?

To use a DLAMI with an older framework version, retrieve the [DLAMI
ID](find-dlami-id.md "find-dlami-id.md") and use it to launch the DLAMI using the [EC2 Console](launch-from-console.md "launch-from-console.md"). For AWS CLI commands to retrieve the AMI ID, refer to the release notes page
in the [single-framework DLAMI release notes](appendix-ami-release-notes-single.md "appendix-ami-release-notes-single.md").

### How do I stay up-to-date with support changes in frameworks and their versions?

Stay up-to-date with DLAMI frameworks and versions using the [AWS Deep Learning AMIs Framework Support Policy table](dlami-support-policy-table.md "dlami-support-policy-table.md"), the [DLAMI release notes](appendix-ami-release-notes.md "appendix-ami-release-notes.md").

### Do I need a commercial license to use the Anaconda Repository?

Anaconda shifted to a commercial licensing model for certain users. Actively
maintained DLAMIs have been migrated to the publicly available open-source
version of Conda ([conda-forge](https://anaconda.org/conda-forge "https://anaconda.org/conda-forge"))
from the Anaconda channel.
