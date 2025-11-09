# Amazon SageMaker AI domain entities and statuses

Amazon SageMaker AI domain supports SageMaker AI machine learning (ML) environments. A SageMaker AI domain is
composed of the following entities and their associated status values. For onboarding steps
to create a domain, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

- **Domain**: A domain consists of the
  following.

      + An associated Amazon Elastic File System (Amazon EFS) volume.
      + A list of authorized users.
      + A variety of security, application, policy, and Amazon Virtual Private Cloud (Amazon VPC)
       configurations.

  Users within a domain can share notebook files and other artifacts with each
  other. An account can have multiple domains. For more information about multiple
  domains, see [Multiple domains overview](domain-multiple.md "domain-multiple.md").

- **User profile**: A user profile represents a single
  user within a domain. It is the main way to reference a user for the purposes of
  sharing, reporting, and other user-oriented features. This entity is created when a
  user onboards to the Amazon SageMaker AI domain. For more information about user profiles, see
  [Domain user profiles](domain-user-profile.md "domain-user-profile.md").
- **Shared space**: A shared space consists of a shared
  JupyterServer application and shared directory. All users within the domain have
  access to the shared space. All user profiles in a domain have access to all shared spaces
  in the domain. For more information about shared spaces, see [Collaboration with shared spaces](domain-space.md "domain-space.md").
- **App**: An app represents an application that supports
  the reading and execution experience of the user’s notebooks, terminals, and
  consoles. The type of app can be JupyterServer, KernelGateway, RStudioServerPro, or
  RSession. A user may have multiple apps active simultaneously.
  The following tables describe the status values for the `domain`,
  `UserProfile`, `shared space`, and `App` entities. Where
  applicable, they also give troubleshooting steps.

domain status values

| Value         | Description                                                                                                                                                                                                                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending       | Ongoing creation of domain.                                                                                                                                                                                                                                                                                                              |
| InService     | Successful creation of domain.                                                                                                                                                                                                                                                                                                           |
| Updating      | Ongoing update of domain.                                                                                                                                                                                                                                                                                                                |
| Deleting      | Ongoing deletion of domain.                                                                                                                                                                                                                                                                                                              |
| Failed        | Unsuccessful creation of domain. Call the `DescribeDomain`<br>API to see the failure reason for domain creation. Delete the failed<br>domain and recreate the domain after fixing the error mentioned in<br>`FailureReason`.                                                                                                             |
| Update_Failed | Unsuccessful update of domain. Call the `DescribeDomain`<br>API to see the failure reason for domain update. Call the<br>`UpdateDomain` API after fixing the error mentioned in<br>`FailureReason`.                                                                                                                                      |
| Delete_Failed | Unsuccessful deletion of domain. Call the `DescribeDomain`<br>API to see the failure reason for domain deletion. Because deletion<br>failed, you might have some resources that are still running, but you cannot<br>use or update the domain. Call the `DeleteDomain` API again<br>after fixing the error mentioned in `FailureReason`. |

`UserProfile` status values

| Value         | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending       | Ongoing creation of `UserProfile`.                                                                                                                                                                                                                                                                                                                                            |
| InService     | Successful creation of `UserProfile`.                                                                                                                                                                                                                                                                                                                                         |
| Updating      | Ongoing update of `UserProfile`.                                                                                                                                                                                                                                                                                                                                              |
| Deleting      | Ongoing deletion of `UserProfile`.                                                                                                                                                                                                                                                                                                                                            |
| Failed        | Unsuccessful creation of `UserProfile`. Call the<br>`DescribeUserProfile` API to see the failure reason for<br>`UserProfile` creation. Delete the failed<br>`UserProfile` and recreate it after fixing the error<br>mentioned in `FailureReason`.                                                                                                                             |
| Update_Failed | Unsuccessful update of `UserProfile`. Call the<br>`DescribeUserProfile` API to see the failure reason for<br>`UserProfile` update. Call the `UpdateUserProfile`<br>API again after fixing the error mentioned in<br>`FailureReason`.                                                                                                                                          |
| Delete_Failed | Unsuccessful deletion of `UserProfile`. Call the<br>`DescribeUserProfile` API to see the failure reason for<br>`UserProfile` deletion. Because deletion failed, you might<br>have some resources that are still running, but you cannot use or update the<br>`UserProfile`. Call the `DeleteUserProfile` API<br>again after fixing the error mentioned in<br>`FailureReason`. |

shared space status values

| Value         | Description                                                                                                                                                                                                                                                                                                                                              |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending       | Ongoing creation of shared space.                                                                                                                                                                                                                                                                                                                        |
| InService     | Successful creation of shared space.                                                                                                                                                                                                                                                                                                                     |
| Deleting      | Ongoing deletion of shared space.                                                                                                                                                                                                                                                                                                                        |
| Failed        | Unsuccessful creation of shared space. Call the `DescribeSpace` API<br>to see the failure reason for shared space creation. Delete the failed shared space and<br>recreate it after fixing the error mentioned in<br>`FailureReason`.                                                                                                                    |
| Update_Failed | Unsuccessful update of shared space. Call the `DescribeSpace` API to<br>see the failure reason for shared space update. Call the `UpdateSpace`<br>API again after fixing the error mentioned in<br>`FailureReason`.                                                                                                                                      |
| Delete_Failed | Unsuccessful deletion of shared space. Call the `DescribeSpace` API<br>to see the failure reason for shared space deletion. Because deletion failed, you<br>might have some resources that are still running, but you cannot use or<br>update the shared space. Call the `DeleteSpace` API again after fixing<br>the error mentioned in `FailureReason`. |
| Deleted       | Successful deletion of shared space.                                                                                                                                                                                                                                                                                                                     |

`App` status values

| Value     | Description                                                                                                                                                                                           |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending   | Ongoing creation of `App`.                                                                                                                                                                            |
| InService | Successful creation of `App`.                                                                                                                                                                         |
| Deleting  | Ongoing deletion of `App`.                                                                                                                                                                            |
| Failed    | Unsuccessful creation of `App`. Call the<br>`DescribeApp` API to see the failure reason for<br>`App` creation. Call the `CreateApp` API again<br>after fixing the error mentioned in `FailureReason`. |
| Deleted   | Successful deletion of `App`.                                                                                                                                                                         |

## Maintenance of applications

At least once every 90 days, SageMaker AI performs security and performance updates to the
underlying software for Amazon SageMaker Studio Classic JupyterServer and KernelGateway, SageMaker Canvas, and
Amazon SageMaker Data Wrangler applications. Some maintenance items, such as operating system upgrades,
require that SageMaker AI takes your application offline for a short time during the maintenance
window. Because this maintenance takes the application offline, you cannot perform any
operations while the underlying software is being updated. When the maintenance activity
is in progress, the state of the application transitions from
**InService** to **Pending**. When maintenance is
complete, the status of the application transitions back to
**InService**. If patching fails, then the status of the
application becomes **Failed**. If an application is in the
**Failed** state, we recommend creating a new application of the
same type. For information about creating Studio Classic applications, see [Shut Down and Update Amazon SageMaker Studio Classic and Apps](studio-tasks-update.md "studio-tasks-update.md"). For information
about creating SageMaker Canvas applications, see [Applications management](canvas-manage-apps.md "canvas-manage-apps.md").

For more information, contact https://aws.amazon.com/premiumsupport/.

###### Topics

- [Complete prerequisites](domain-prerequisites.md "domain-prerequisites.md")
- [Hide machine learning tools and
  applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md "studio-updated-ui-customize-tools-apps.md")
- [Hide instance types and
  images in the Amazon SageMaker Studio UI](studio-updated-ui-customize-instances-images.md "studio-updated-ui-customize-instances-images.md")
- [Multiple domains overview](domain-multiple.md "domain-multiple.md")
- [Isolate domain resources](domain-resource-isolation.md "domain-resource-isolation.md")
- [Default settings for Amazon SageMaker AI domains](domain-set-defaults.md "domain-set-defaults.md")
- [Custom tag propagation](custom-tags.md "custom-tags.md")
- [Adding a custom file system to a domain](domain-custom-file-system.md "domain-custom-file-system.md")
- [View domain environment details](domain-space-environment.md "domain-space-environment.md")
- [View domains](domain-view.md "domain-view.md")
- [Edit domain settings](domain-edit.md "domain-edit.md")
- [Delete an Amazon SageMaker AI domain](gs-studio-delete-domain.md "gs-studio-delete-domain.md")
- [Domain user profiles](domain-user-profile.md "domain-user-profile.md")
- [IAM Identity Center groups in a domain](domain-groups.md "domain-groups.md")
- [Understanding domain space permissions and
  execution roles](execution-roles-and-spaces.md "execution-roles-and-spaces.md")
- [View SageMaker AI resources in your
  domain](sm-console-domain-resources-view.md "sm-console-domain-resources-view.md")
- [Shut down SageMaker AI resources in your
  domain](sm-console-domain-resources-shut-down.md "sm-console-domain-resources-shut-down.md")
- [Where to shut down resources per SageMaker AI
  features](sm-shut-down-resources-per-feature.md "sm-shut-down-resources-per-feature.md")
