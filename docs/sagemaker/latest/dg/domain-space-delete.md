# Delete a shared space

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

The following topic shows how to delete an Amazon SageMaker Studio Classic shared space from the Amazon SageMaker AI console or
AWS CLI. A shared space can only be deleted if it has no running applications.

###### Topics

- [Console](#domain-space-delete-console "#domain-space-delete-console")
- [AWS CLI](#domain-space-delete-cli "#domain-space-delete-cli")

## Console

Complete the following procedure to delete a shared space in the Amazon SageMaker AI domain from the SageMaker AI
console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain that you want to create a shared space for.
5. On the **domain details** page, choose the **Space
   management** tab.
6. Select the shared space that you want to delete. The shared space must not contain any non-failed
   apps.
7. Choose **Delete**. This opens a new window.
8. Choose **Yes, delete space**.
9. Enter _delete_ in the field.
10. Choose **Delete space**.

## AWS CLI

To delete a shared space from the AWS CLI, run the following command from the terminal of your local
machine.

```
aws --region `region` \
sagemaker delete-space \
--domain-id `domain-id` \
--space-name `space-name`
```
