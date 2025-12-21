**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Amazon Glacier Data Model

The Amazon Glacier data model core components include vaults and archives. Amazon Glacier is a
REST-based web service. In terms of REST, vaults and archives are the resources. In
addition, the Amazon Glacier data model includes job and notification-configuration
resources. These resources complement the core resources.

###### Topics

- [Vault](#data-model-vault "#data-model-vault")
- [Archive](#data-model-archive "#data-model-archive")
- [Job](#data-model-job "#data-model-job")
- [Notification Configuration](#data-model-notification-config "#data-model-notification-config")

## Vault

In Amazon Glacier, a _vault_ is a container for
storing archives. A vault is similar to an Amazon S3 bucket. When you create a vault, you
specify a name and choose an AWS Region where you want to create the vault.

Each vault resource has a unique address. The general form is:

```
https://`region-specific-endpoint`/`account-id`/vaults/`vault-name`
```

For example, suppose that you create a vault (`examplevault`) in the
US West (Oregon) Region in your account with the ID 111122223333. You can address this
vault by using the following URI:

```
https://glacier.us-west-2.amazonaws.com/111122223333/vaults/examplevault
```

Here is what the various components of the URI mean:

- `glacier.us-west-2.amazonaws.com` identifies the
  US West (Oregon) Region.
- `111122223333` is the AWS account ID that owns the
  vault.
- `vaults` refers to the collection of vaults that are owned by
  the AWS account.
- `examplevault` identifies a specific vault in the vaults
  collection.

An AWS account can create vaults in any supported AWS Region. For list of
supported AWS Regions, see [Accessing Amazon Glacier](amazon-glacier-accessing.md "amazon-glacier-accessing.md"). Within a Region, an account must use
unique vault names. An AWS account can create same-named vaults in different
Regions.

You can store an unlimited number of archives in a vault. Depending on your
business or application needs, you can store these archives in one vault or multiple
vaults.

Amazon Glacier supports various vault operations. Vault operations are Region-specific.
For example, when you create a vault, you create it in a specific Region. When you
request a vault list, you request it from a specific AWS Region, and the resulting
list includes only vaults created in that specific Region.

## Archive

An _archive_ can be any data, such as a photo,
video, or document. An archive is similar to an Amazon S3 object, and is the base unit of
storage in Amazon Glacier. Each archive has a unique ID and an optional description. You
can specify this optional description only during the upload of an archive.
Amazon Glacier assigns the archive an ID, which is unique in the AWS Region in which
the archive is stored.

Each archive has a unique address. The general form is as follows:

```
https://`region-specific-endpoint`/`account-id`/vaults/`vault-name`/archives/`archive-id`
```

The following is an example URI of an archive stored in the
`examplevault` vault in the US West (Oregon) Region in account
111122223333:

```
https://glacier.us-west-2.amazonaws.com/111122223333/vaults/examplevault/archives/NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId
```

You can store an unlimited number of archives in a vault.

## Job

An Amazon Glacier job can retrieve an archive, or get an inventory of a vault.

Retrieving archives and vault inventories (lists of archives) are asynchronous
operations in Amazon Glacier, in which you first initiate a job, and then download the
job output after Amazon Glacier completes the job.

###### Note

Amazon Glacier offers a cold-storage data-archival solution. If your application
needs a storage solution that requires real-time data retrieval, you might
consider using Amazon S3. For more information, see [Amazon Simple Storage Service (Amazon S3)](http://aws.amazon.com/s3 "http://aws.amazon.com/s3").

To initiate a vault inventory job, you provide a vault name. Archive retrieval
jobs require both the vault name and the archive ID. You can also provide an
optional job description to help identify the jobs.

Archive retrieval and vault inventory jobs are associated with a vault. A vault
can have multiple jobs in progress at any point in time. When you send a job request
(initiate a job), Amazon Glacier returns to you a job ID to track the job. Each job is
uniquely identified by a URI of the form:

```
https://`region-specific-endpoint`/`account-id`/vaults/`vault-name`/jobs/`job-id`
```

The following is an example of a job associated with an `examplevault`
vault in the US West (Oregon) Region in account 111122223333.

```
https://glacier.us-west-2.amazonaws.com/111122223333/vaults/examplevault/jobs/HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID
```

For each job, Amazon Glacier maintains information, such as the job type, description,
creation date, completion date, and job status. You can obtain information about a
specific job or obtain a list of all your jobs associated with a vault. The list of
jobs that Amazon Glacier returns includes all the in-progress and recently finished jobs.

## Notification Configuration

Because jobs take time to run, Amazon Glacier supports a notification mechanism to
notify you when a job is completed. You can configure a vault to send a notification
to an Amazon Simple Notification Service (Amazon SNS) topic when a job is completed. You can specify one Amazon SNS
topic per vault in the notification configuration.

Amazon Glacier stores the notification configuration as a JSON document. The following
is an example vault notification configuration:

```
{
   "Topic": "arn:aws:sns:us-west-2:111122223333:mytopic",
   "Events": ["ArchiveRetrievalCompleted", "InventoryRetrievalCompleted"]
}
```

Notification configurations are associated with vaults; you can have one for each
vault. Each notification configuration resource is uniquely identified by a URI of
the form:

```
https://`region-specific-endpoint`/`account-id`/vaults/`vault-name`/`notification-configuration`
```

Amazon Glacier supports operations to set, get, and delete a notification
configuration. When you delete a notification configuration, no notifications are
sent when any data retrieval operation on the vault is completed.
