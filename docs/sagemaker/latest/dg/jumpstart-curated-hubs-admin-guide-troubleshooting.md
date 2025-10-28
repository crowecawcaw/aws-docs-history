# Troubleshooting

The following sections give information about IAM permissions issues that might
arise when creating a private model hub, as well as informationa bout how to resolve
those issues.

**`ValidationException` when calling the `CreateModel` operation:
Could not access model data**

This exception arises when you do not have the appropriate Amazon S3 permissions
configured for your **Admin** role. For more information on the
Amazon S3 permissions needed to create a private hub, see **Step 3** in [Create a private model hub](jumpstart-curated-hubs-admin-guide-create.md "jumpstart-curated-hubs-admin-guide-create.md").

**`Access Denied` or `Forbidden` when calling `create()`**

You are denied access when creating a private hub if you do not have the
appropriate permissions to access the Amazon S3 bucket associated with the SageMaker
**Public models** hub. For more information on the Amazon S3
permissions needed to create a private hub, see **Step 3** in [Create a private model hub](jumpstart-curated-hubs-admin-guide-create.md "jumpstart-curated-hubs-admin-guide-create.md").
