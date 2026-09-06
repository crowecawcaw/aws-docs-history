

# Amazon SageMaker AI domain entities and statuses
<a name="sm-domain"></a>

Amazon SageMaker AI domain supports SageMaker AI machine learning (ML) environments. A SageMaker AI domain is composed of the following entities and their associated status values. For onboarding steps to create a domain, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).
+  **Domain**: A domain consists of the following.
  + An associated Amazon Elastic File System (Amazon EFS) volume.
  + A list of authorized users.
  + A variety of security, application, policy, and Amazon Virtual Private Cloud (Amazon VPC) configurations.

  Users within a domain can share notebook files and other artifacts with each other. An account can have multiple domains. For more information about multiple domains, see [Multiple domains overview](domain-multiple.md).
+  **User profile**: A user profile represents a single user within a domain. It is the main way to reference a user for the purposes of sharing, reporting, and other user-oriented features. This entity is created when a user onboards to the Amazon SageMaker AI domain. For more information about user profiles, see [Domain user profiles](domain-user-profile.md).
+  **Shared space**: A shared space consists of a shared JupyterServer application and shared directory. All users within the domain have access to the shared space. All user profiles in a domain have access to all shared spaces in the domain. For more information about shared spaces, see [Collaboration with shared spaces](domain-space.md).
+  **App**: An app represents an application that supports the reading and execution experience of the user’s notebooks, terminals, and consoles. The type of app can be JupyterServer, KernelGateway, RStudioServerPro, or RSession. A user may have multiple apps active simultaneously.

The following tables describe the status values for the `domain`, `UserProfile`, `shared space`, and `App` entities. Where applicable, they also give troubleshooting steps.

domain status values


| Value | Description | 
| --- | --- | 
| Pending | Ongoing creation of domain. | 
| InService | Successful creation of domain. | 
| Updating | Ongoing update of domain. | 
| Deleting | Ongoing deletion of domain. | 
| Failed | Unsuccessful creation of domain. Call the DescribeDomain API to see the failure reason for domain creation. Delete the failed domain and recreate the domain after fixing the error mentioned in FailureReason. | 
| Update\_Failed | Unsuccessful update of domain. Call the DescribeDomain API to see the failure reason for domain update. Call the UpdateDomain API after fixing the error mentioned in FailureReason. | 
| Delete\_Failed | Unsuccessful deletion of domain. Call the DescribeDomain API to see the failure reason for domain deletion. Because deletion failed, you might have some resources that are still running, but you cannot use or update the domain. Call the DeleteDomain API again after fixing the error mentioned in FailureReason. | 

`UserProfile` status values


| Value | Description | 
| --- | --- | 
| Pending | Ongoing creation of UserProfile. | 
| InService | Successful creation of UserProfile. | 
| Updating | Ongoing update of UserProfile. | 
| Deleting | Ongoing deletion of UserProfile. | 
| Failed | Unsuccessful creation of UserProfile. Call the DescribeUserProfile API to see the failure reason for UserProfile creation. Delete the failed UserProfile and recreate it after fixing the error mentioned in FailureReason. | 
| Update\_Failed | Unsuccessful update of UserProfile. Call the DescribeUserProfile API to see the failure reason for UserProfile update. Call the UpdateUserProfile API again after fixing the error mentioned in FailureReason. | 
| Delete\_Failed | Unsuccessful deletion of UserProfile. Call the DescribeUserProfile API to see the failure reason for UserProfile deletion. Because deletion failed, you might have some resources that are still running, but you cannot use or update the UserProfile. Call the DeleteUserProfile API again after fixing the error mentioned in FailureReason. | 

shared space status values


| Value | Description | 
| --- | --- | 
| Pending | Ongoing creation of shared space. | 
| InService | Successful creation of shared space. | 
| Deleting | Ongoing deletion of shared space. | 
| Failed | Unsuccessful creation of shared space. Call the DescribeSpace API to see the failure reason for shared space creation. Delete the failed shared space and recreate it after fixing the error mentioned in FailureReason. | 
| Update\_Failed | Unsuccessful update of shared space. Call the DescribeSpace API to see the failure reason for shared space update. Call the UpdateSpace API again after fixing the error mentioned in FailureReason. | 
| Delete\_Failed | Unsuccessful deletion of shared space. Call the DescribeSpace API to see the failure reason for shared space deletion. Because deletion failed, you might have some resources that are still running, but you cannot use or update the shared space. Call the DeleteSpace API again after fixing the error mentioned in FailureReason. | 
| Deleted | Successful deletion of shared space. | 

`App` status values


| Value | Description | 
| --- | --- | 
| Pending | Ongoing creation of App. | 
| InService | Successful creation of App. | 
| Deleting | Ongoing deletion of App. | 
| Failed | Unsuccessful creation of App. Call the DescribeApp API to see the failure reason for App creation. Call the CreateApp API again after fixing the error mentioned in FailureReason. | 
| Deleted | Successful deletion of App. | 

## Maintenance of applications
<a name="domain-maintenance"></a>

At least once every 90 days, SageMaker AI performs security and performance updates to the underlying software for Amazon SageMaker Studio Classic JupyterServer and KernelGateway, SageMaker Canvas, and Amazon SageMaker Data Wrangler applications. Some maintenance items, such as operating system upgrades, require that SageMaker AI takes your application offline for a short time during the maintenance window. Because this maintenance takes the application offline, you cannot perform any operations while the underlying software is being updated. When the maintenance activity is in progress, the state of the application transitions from **InService** to **Pending**. When maintenance is complete, the status of the application transitions back to **InService**. If patching fails, then the status of the application becomes **Failed**. If an application is in the **Failed** state, we recommend creating a new application of the same type. For information about creating Studio Classic applications, see [Shut Down and Update Amazon SageMaker Studio Classic and Apps](studio-tasks-update.md). For information about creating SageMaker Canvas applications, see [Applications management](canvas-manage-apps.md).

For apps running on training plan capacity, Studio requires an additional instance from the training plan during maintenance. If no instances are available, maintenance fails and the app transitions to `Failed` status. To recover the app in case of maintenance failures, verify that your training plan has at least one available instance, then create the app again. Also ensure that your instance group has at least one subnet in the training plan's Availability Zone with one free IP address.

For more information, contact https://aws.amazon.com/premiumsupport/.

**Topics**
+ [Maintenance of applications](#domain-maintenance)
+ [Complete prerequisites](domain-prerequisites.md)
+ [Hide machine learning tools and applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md)
+ [Hide instance types and images in the Amazon SageMaker Studio UI](studio-updated-ui-customize-instances-images.md)
+ [Multiple domains overview](domain-multiple.md)
+ [Isolate domain resources](domain-resource-isolation.md)
+ [Default settings for Amazon SageMaker AI domains](domain-set-defaults.md)
+ [Custom tag propagation](custom-tags.md)
+ [Adding a custom file system to a domain](domain-custom-file-system.md)
+ [View domain environment details](domain-space-environment.md)
+ [View domains](domain-view.md)
+ [Edit domain settings](domain-edit.md)
+ [Delete an Amazon SageMaker AI domain](gs-studio-delete-domain.md)
+ [Domain user profiles](domain-user-profile.md)
+ [IAM Identity Center groups in a domain](domain-groups.md)
+ [Understanding domain space permissions and execution roles](execution-roles-and-spaces.md)
+ [View SageMaker AI resources in your domain](sm-console-domain-resources-view.md)
+ [Shut down SageMaker AI resources in your domain](sm-console-domain-resources-shut-down.md)
+ [Where to shut down resources per SageMaker AI features](sm-shut-down-resources-per-feature.md)