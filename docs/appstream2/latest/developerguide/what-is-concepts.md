# Key Concepts of Amazon WorkSpaces Applications

To get the most out of WorkSpaces Applications, be familiar with the following concepts:

**application**

An _application_ contains the information necessary to
launch the application that you want to stream to your users. An application
is associated with the resource that contains the files necessary to launch
the application, such as an app block or image.

**app block**

An _app block_ contains the application files that you
want to stream to your users, and the details necessary to configure
it.

**app block builder**

An _app block builder_ is a virtual machine that you
use to create an app block. You can launch and connect to an app block
builder by using the WorkSpaces Applications console. After you connect to an appblock
builder, you can install your application(s). App block builder packages
your app contents, uploads it to an Amazon S3 bucket, and completes
app block creation.

**image builder**

An _image builder_ is a virtual machine that you use to
create an image. You can launch and connect to an image builder by using the
WorkSpaces Applications console. After you connect to an image builder, you can install, add,
and test your applications, and then use the image builder to create an
image. You can launch new image builders by using private images that you
own.

**image**

An _image_ contains applications that you can stream to
your users, and default system and application settings to enable your users
to get started with their applications quickly. AWS provides base images
that you can use to create image builders to then create images that include
your own applications. After you create an image, you can't change it. To
add other applications, update existing applications, or change image
settings, you must create a new image. You can copy your images to other
AWS Regions or share them with other AWS accounts in the same Region.
your users, and default system and application settings to enable your users
to get started with their applications quickly.

**fleet**

A _fleet_ consists of fleet instances (also known as
streaming instances) that run the applications and desktops that you
specify.

**stack**

A _stack_ consists of an associated fleet, user access
policies, and storage configurations. You set up a stack to start streaming
applications to users.

**streaming instance**

A _streaming instance_ (also known as a fleet instance)
is an EC2 instance that is made available to a single user for application
streaming. After the user’s session completes, the instance is terminated by
EC2.

**user pool**

Use the _user pool_ to manage users and their assigned
stacks.

**auto scaling rules**

_Auto scaling rules_ are schedule-based and usage-based
policies that you can apply to an Always-On or On-Demand fleet to
automatically manage the number of streaming instances available for users
to stream from.

**multi-session**

A _multi-session_ fleet allows you to provision more
than one user session on a single fleet instance. The underlying
infrastructure resources are shared across all of the user sessions.

###### Note

Multi-session is available only on Always-on and On-demand fleets
powered by a Windows operating system. Multi-session is not available on
Elastic fleets or the Linux operating system.

Make sure you are using latest WorkSpaces Applications images for multi-session fleets.
To keep your images are up-to-date, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md "keep-image-updated.md"). For details on supported images and
WorkSpaces Applications agent versions for multi-session, see [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md "base-image-version-history.md").
