**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Using service-linked roles for

Amazon Chime

Amazon Chime uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon Chime. Service-linked roles are predefined by Amazon Chime and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Amazon Chime more efficient because you aren't required to
manually add the necessary permissions. Amazon Chime defines the permissions of its service-linked
roles, and unless defined otherwise, only Amazon Chime can assume its roles. The defined permissions
include the trust policy and the permissions policy. The permissions policy cannot be attached
to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your Amazon Chime resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [Using roles with shared Alexa for Business
  devices](using-service-linked-roles-a4b.md "using-service-linked-roles-a4b.md")
- [Using roles with live transcription](using-service-linked-roles-transcription.md "using-service-linked-roles-transcription.md")
- [Using roles with Amazon Chime SDK media
  pipelines](using-service-linked-roles-media-pipeline.md "using-service-linked-roles-media-pipeline.md")
