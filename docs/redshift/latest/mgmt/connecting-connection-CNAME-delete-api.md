Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deleting a custom

domain

To delete the custom domain name, the user must have permissions for the following
actions:

- For a provisioned cluster:
  `redshift:DeleteCustomDomainAssociation`
- For an Amazon Redshift Serverless workgroup:
  `redshiftServerless:DeleteCustomDomainAssociation`
  **On the console**

You can delete the custom domain name by selecting the **Actions**
button and choosing **Delete custom domain name**. After you do
this, you can still connect to the server by updating your tools to use the endpoints
listed in the console.

**Using a CLI command**

The following sample shows how to delete the custom domain name. The delete operation
requires that you provide the existing custom domain name for the cluster.

```
aws redshift delete-custom-domain-association ––cluster-id `redshiftcluster` ––custom-domain-name `customdomainname`
```

The following sample shows how to delete the custom domain name for an
Amazon Redshift Serverless workgroup. The custom domain name is a required parameter.

```
aws redshift-serverless delete-custom-domain-association ––workgroup-name `workgroupname` ––custom-domain-name `customdomainname`
```

For more information, see [DeleteCustomDomainAssociation](../APIReference/API_DeleteCustomDomainAssociation.md "../APIReference/API_DeleteCustomDomainAssociation.md").
