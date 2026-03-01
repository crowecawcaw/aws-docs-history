# WorkSpaces Applications App Blocks

Elastic fleet streaming instances utilize applications that are installed on virtual
hard disk (VHD) files stored within an Amazon S3 bucket in your account. When it comes to
app blocks with custom packaging, you have the flexibility to create your own VHD
file and upload it to an Amazon S3 bucket within your account. Alternatively, for app
blocks with WorkSpaces Applications packaging, you can take advantage of the app block builder, which
handles the packaging of your applications, creates a VHD file, and uploads it to
your Amazon S3 bucket.

By using the WorkSpaces Applications packaged app block, you not only eliminate the need for manual
steps in building a VHD file, but also remove the requirement for a setup script. It
expands application compatibility with elastic fleets, as well as reduces manual
administrative steps required to create an app block. WorkSpaces Applications handles the setup of
app blocks with WorkSpaces Applications packaging automatically without the need of any setup
scripts. However, you can still provide optional post-setup scripts to customize the
installation for your needs.

###### Contents

- [Overview](appstream-app-blocks-overview.md "appstream-app-blocks-overview.md")
- [Unsupported Applications](appstream-app-blocks-unsupported.md "appstream-app-blocks-unsupported.md")
- [Create an WorkSpaces Applications App Block](appstream-app-blocks-create.md "appstream-app-blocks-create.md")
- [Activate an App Block](appstream-app-blocks-activate.md "appstream-app-blocks-activate.md")
- [Create an App Block with an Existing App Package](appstream-app-blocks-create-VHD.md "appstream-app-blocks-create-VHD.md")
- [Test an App Block](appstream-app-blocks-test.md "appstream-app-blocks-test.md")
- [Associate an App Block in Amazon WorkSpaces Applications](appstream-app-blocks-associate.md "appstream-app-blocks-associate.md")
- [Disassociate an App Block in Amazon WorkSpaces Applications](appstream-app-blocks-disassociate.md "appstream-app-blocks-disassociate.md")
