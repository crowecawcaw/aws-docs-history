# Deploy the Amazon Kinesis Video Streams Edge Agent to AWS IoT Greengrass

This section provides a comprehensive guide to use Amazon Kinesis Video Streams with AWS IoT Greengrass. By combining these services, you can efficiently stream video from edge devices to the cloud, enabling a wide range of applications in IoT, surveillance, and more.

You'll find detailed information on:

- Setting up your development environment
- Creating a Kinesis video stream
- Creating and packaging a Lambda function
- Configuring the Kinesis Video Streams core device
- Deploying to the core device
- Verifying your stream
  Follow these steps to deploy the Amazon Kinesis Video Streams Edge Agent to AWS IoT Greengrass to record and upload media
  from IP cameras.

###### Topics

- [Create an Ubuntu Amazon EC2 instance](gs-ubuntu.md "gs-ubuntu.md")
- [Set up the AWS IoT Greengrass V2 core device on the device](gs-setup-gg.md "gs-setup-gg.md")
- [Create the Amazon Kinesis Video Streams and
  AWS Secrets Manager resources for your IP camera RTSP URLs](gs-create-resources.md "gs-create-resources.md")
- [Add permissions to the token exchange service
  (TES) role](gs-add-permissions.md "gs-add-permissions.md")
- [Install the AWS IoT Greengrass Secret Manager
  component on the device](gs-install-secrets-manager.md "gs-install-secrets-manager.md")
- [Deploy the Amazon Kinesis Video Streams Edge Agent AWS IoT Greengrass component on the
  device](gs-deploy-edge.md "gs-deploy-edge.md")
- [Install the AWS IoT Greengrass log manager component on the
  device](gs-publish-edge.md "gs-publish-edge.md")
