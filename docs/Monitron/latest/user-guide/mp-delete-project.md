Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Deleting a project

With the `deleteProject` operation, you must have the AWS IAM Identity Center permissions
for deletion. Without these permissions, the console's delete project functionality will
still remove the project. However, it will not remove the resources from IAM Identity Center and you
may end up with dangling references on IAM Identity Center.

###### To delete a project

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/ "https://console.aws.amazon.com/monitron/") .
2. Choose **Create Project**.
3. In the navigation pane, choose **Projects**.
4. From the **Projects** list, choose the project you want to
   delete.
5. Choose **Delete Project**.
6. Enter **Delete** in the confirmation box to confirm the
   deletion.

If the project contains any active assets, sensors or gateways, you have to
remove them before deleting the project. If this is the case, the confirmation
box and option to delete don't appear.

If there are active assets or sensors that need to be removed to delete this
project, ask an Admin user do this or do it yourself by logging into the
_Amazon Monitron mobile app_. 7. Choose **Delete**.
