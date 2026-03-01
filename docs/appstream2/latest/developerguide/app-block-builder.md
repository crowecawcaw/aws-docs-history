# App Block Builder

An app block builder is a reusable resource that you can use to package your applications
(or app block). You can also use it to test your application package before associating your
application to an Elastic fleet. A single app block builder can be used to create and test
multiple app blocks one by one. Each time a streaming session is created for app block
builder for creating or testing an app block, a new instance is created and used. After the
app block builder instance is terminated, the state of the instance is not persisted.

WorkSpaces Applications Elastic fleets use Amazon EC2 instances to stream applications. You must provide your
application package and associate it with your fleet. To create your own custom application
packaging, connect to an app block builder instance, and then install and configure your
applications for streaming. App block builder creates the packaging for your application and
uploads it to an Amazon S3 bucket in your AWS account.

When you create an app block builder, you choose the following:

- An instance type — WorkSpaces Applications provides different instance sizes with various CPU and
  memory configurations. The instance type must align with the instance family you
  need.
- The VPC, subnets, and security groups to use — Make sure that the subnets and
  security groups provide access to the network resources that your applications
  require. Typical network resources required by applications might include
  licensing servers, database servers, file servers, and application servers. App
  block builder uploads the application package on to an Amazon S3 bucket
  in your AWS account. The VPC you choose for your fleet must provide sufficient
  network access to the Amazon S3 bucket. For more information, see [Store Application Icon, Setup Script, Session Script, and VHD in an S3 Bucket](store-s3-bucket.md "store-s3-bucket.md").

###### Contents

- [Create an App Block Builder](create-app-block-builder.md "create-app-block-builder.md")
- [Connect to an App Block Builder in Amazon WorkSpaces Applications](connect-app-block-builder.md "connect-app-block-builder.md")
- [App Block Builder Actions](app-block-builder-actions.md "app-block-builder-actions.md")
