# Features of Amazon WorkSpaces Applications

Using Amazon WorkSpaces Applications provides the following advantages:

**Access desktop applications securely from any supported
device**

Your desktop applications can be accessed securely through an
HTML5-capable web browser on Windows and Linux PCs, Macs, Chromebooks,
iPads, and Android tablets. Or, for supported versions of Windows, the
WorkSpaces Applications client can be used for application streaming.

**Secure applications and data**

Applications and data remain on AWS — only encrypted pixels are
streamed to users. Applications run on an WorkSpaces Applications instance dedicated to each
user so that compute resources are not shared. Applications can run inside
your own virtual private cloud (VPC), and you can use Amazon VPC security
features to control access. This enables you to isolate your applications
and deliver them in a secure way.

**Consistent, scalable performance**

WorkSpaces Applications runs on AWS with access to compute capabilities not available on
local devices, which means that your applications run with consistently high
performance. You can instantly scale locally and globally, and ensure that
your users always get a low-latency experience. Unlike on-premises
solutions, you can quickly deploy your applications to the AWS region that
is closest to your users, and start streaming with no incremental capital
investment.

**Integrate with your IT environment**

Integrate with your existing AWS services and your on-premises environments.
By running applications inside your VPCs, your users can access data and other
resources that you have in AWS. This reduces the movement of data between AWS
and your environment and provides a faster user experience.

Integrate with your existing Microsoft Active Directory environment.
This enables you to use existing Active Directory governance,
user experience, and security policies with your streaming applications.

Configure identity federation, which allows your users to access
their applications using their corporate credentials. You can also allow
authenticated access to your IT resources from applications running on
WorkSpaces Applications.

**Choose the fleet type that meets your needs**

These are the types of fleets:

- Always-On — Streaming instances run all the time, even when
  no users are streaming applications and desktops. Streaming
  instances must be provisioned before a user is able to stream. The
  number of streaming instances provisioned is managed through auto
  scaling rules. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md "autoscaling.md").

When your users choose their application or desktop, they will
start streaming instantly. You are charged the running instance fee
for all streaming instances, even when no users are
streaming.

- On-Demand — Streaming instances run only when users are
  streaming applications and desktops. Streaming instances not yet
  assigned to users are in a stopped state. Streaming instances must
  be provisioned before a user is able to stream. The number of
  streaming instances provisioned is managed through auto scaling
  rules. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md "autoscaling.md").

When your users choose their application or desktop, they will
start streaming after a 1-2 minute wait. You are charged a lower
stopped instance fee for streaming instances that are not yet
assigned to users, and the running instance fee for streaming
instances that are assigned to users.

- Elastic — The pool of streaming instances is managed by
  WorkSpaces Applications. When your users select their application or desktop to
  launch, they will start streaming after the app block has been
  downloaded and mounted to a streaming instance.

You are charged the running instance fee for Elastic fleet
streaming instances only for the duration of the streaming session,
in seconds.

For more information, see [Amazon WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/ "https://aws.amazon.com/appstream2/pricing/").
