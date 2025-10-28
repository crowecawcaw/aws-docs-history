# Access Instance Metadata Service (IMDS)

and user data in Lightsail

_Instance metadata_ is data about your instance that you can use to
configure or manage the running instance. Instance metadata is divided into categories, for
example, hostname, events, and security groups. You can also use instance metadata to access
user data that you specified when launching your instance. For example, you can specify
parameters for configuring your instance, or include a simple script. Instances can also
include dynamic data, such as an instance identity document that is generated when the
instance is launched.

###### Important

Although you can only access instance metadata and user data from within the instance
itself, the data is not protected by authentication or cryptographic methods. Anyone who
has direct access to the instance, and potentially any software running on the instance,
can view its metadata. Therefore, you should not store sensitive data, such as passwords
or long-lived encryption keys, as user data.

## Use the Instance Metadata Service

You can access instance metadata from a running instance in Lightsail by using one
of the following methods:

- Instance Metadata Service Version 1 (IMDSv1) – a request/response method
- Instance Metadata Service Version 2 (IMDSv2) – a session-oriented method

###### Important

Not all instance blueprints in Lightsail support IMDSv2. Use the
`MetadataNoToken` instance metric to track the number of
calls to the instance metadata service that are using IMDSv1. For more
information, see [View instance
metrics](amazon-lightsail-viewing-instance-health-metrics.md "amazon-lightsail-viewing-instance-health-metrics.md").

For more information about using IMDS, see [Configure the
Instance Metadata Service (IMDS)](amazon-lightsail-configuring-instance-metadata-service.md "amazon-lightsail-configuring-instance-metadata-service.md").

## Additional IMDS

documentation

The following IMDS documentation is available in the _Amazon Elastic Compute Cloud User Guide
for Linux Instances_ and the _Amazon Elastic Compute Cloud User Guide for Windows
Instances_:

###### Note

In Amazon EC2, instance blueprints are referred to as Amazon Machine Images
(AMIs).

- For Linux instances:
  - [Configure the instance metadata options](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md")
  - [Retrieve instance metadata](../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md "../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md")
  - [Work
    with instance user data](../../../AWSEC2/latest/UserGuide/instancedata-add-user-data.md "../../../AWSEC2/latest/UserGuide/instancedata-add-user-data.md")
  - [Retrieve dynamic data](../../../AWSEC2/latest/UserGuide/instancedata-dynamic-data-retrieval.md "../../../AWSEC2/latest/UserGuide/instancedata-dynamic-data-retrieval.md")
  - [Instance metadata categories](../../../AWSEC2/latest/UserGuide/instancedata-data-categories.md "../../../AWSEC2/latest/UserGuide/instancedata-data-categories.md")
  - [Example: AMI launch index value](../../../AWSEC2/latest/UserGuide/AMI-launch-index-examples.md "../../../AWSEC2/latest/UserGuide/AMI-launch-index-examples.md")
  - [Instance identity documents](../../../AWSEC2/latest/UserGuide/instance-identity-documents.md "../../../AWSEC2/latest/UserGuide/instance-identity-documents.md")

- For Windows instances:
  - [Configure the instance metadata options](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md")
  - [Retrieve instance metadata](../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md "../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md")
  - [Work
    with instance user data](../../../AWSEC2/latest/UserGuide/instancedata-add-user-data.md "../../../AWSEC2/latest/UserGuide/instancedata-add-user-data.md")
  - [Retrieve dynamic data](../../../AWSEC2/latest/UserGuide/instancedata-dynamic-data-retrieval.md "../../../AWSEC2/latest/UserGuide/instancedata-dynamic-data-retrieval.md")
  - [Instance metadata categories](../../../AWSEC2/latest/UserGuide/instancedata-data-categories.md "../../../AWSEC2/latest/UserGuide/instancedata-data-categories.md")
  - [Example: AMI launch index value](../../../AWSEC2/latest/UserGuide/AMI-launch-index-examples.md "../../../AWSEC2/latest/UserGuide/AMI-launch-index-examples.md")
  - [Instance identity documents](../../../AWSEC2/latest/UserGuide/instance-identity-documents.md "../../../AWSEC2/latest/UserGuide/instance-identity-documents.md")
