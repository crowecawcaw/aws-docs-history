# Prerequisites for Enabling

Application Settings Persistence

To enable application settings persistence, you must first do the
following:

- Check that you have the correct AWS Identity and Access Management (IAM) permissions for Amazon S3
  actions. For more information, see the _IAM Policies and the Amazon
  S3 Bucket for Home Folders_ section in [Identity and Access Management for Amazon AppStream 2.0](controlling-access.md "controlling-access.md").
- Use an image that was created from a base image published by AWS on or
  after December 7, 2017. For a current list of released AWS base images,
  see [AppStream 2.0 Base Image and Managed Image Update
  Release Notes](base-image-version-history.md "base-image-version-history.md").
- Associate the stack on which you plan to enable this feature with a fleet
  based on an image that uses a version of the AppStream 2.0 agent released on or
  after August 29, 2018. For more information, see [AppStream 2.0 Agent Release Notes](agent-software-versions.md "agent-software-versions.md").
- Enable network connectivity to Amazon S3 from your virtual private cloud (VPC)
  by configuring internet access or a VPC endpoint for Amazon S3. For more
  information, see the _Home Folders and VPC Endpoints_
  section in [Networking and Access for Amazon AppStream 2.0](managing-network.md "managing-network.md").
