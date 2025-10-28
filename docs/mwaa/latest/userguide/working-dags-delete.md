# Deleting files on Amazon S3

This page describes how versioning works in an Amazon S3 bucket for an Amazon Managed Workflows for Apache Airflow environment, and the steps to delete a DAG, `plugins.zip`, or `requirements.txt` file.

###### Contents

- [Prerequisites](working-dags-delete.md#working-dags-delete-prereqs "working-dags-delete.md#working-dags-delete-prereqs")
- [Versioning overview](working-dags-delete.md#working-dags-delete-overview "working-dags-delete.md#working-dags-delete-overview")
- [How it works](working-dags-delete.md#working-dags-delete-how "working-dags-delete.md#working-dags-delete-how")
- [Deleting a DAG on Amazon S3](working-dags-delete.md#working-dags-s3-dag-delete "working-dags-delete.md#working-dags-s3-dag-delete")
- [Removing a "current" requirements.txt or plugins.zip from an environment](working-dags-delete.md#working-dags-s3-delete-version-c "working-dags-delete.md#working-dags-s3-delete-version-c")
- [Deleting a "non-current" (previous) requirements.txt or plugins.zip version](working-dags-delete.md#working-dags-s3-delete-version-p "working-dags-delete.md#working-dags-s3-delete-version-p")
- [Using lifecycles to delete "non-current" (previous) versions and delete markers automatically](working-dags-delete.md#working-dags-s3-delete-lifecycle "working-dags-delete.md#working-dags-s3-delete-lifecycle")
- [Example lifecycle policy to delete requirements.txt "non-current" versions and delete markers automatically](working-dags-delete.md#working-dags-s3-delete-lifecycle-ex "working-dags-delete.md#working-dags-s3-delete-lifecycle-ex")
- [What's next?](working-dags-delete.md#working-dags-s3-delete-next-up "working-dags-delete.md#working-dags-s3-delete-next-up")

## Prerequisites

You'll need the following before you can complete the steps on this page.

- **Permissions** — Your AWS account must have been granted access by your administrator to the [AmazonMWAAFullConsoleAccess](access-policies.md#console-full-access "access-policies.md#console-full-access")
  access control policy for your environment. In addition, your Amazon MWAA environment must be permitted by your [execution role](mwaa-create-role.md "mwaa-create-role.md") to access the AWS resources used by your environment.
- **Access** — If you require access to public repositories to install dependencies directly on the webserver, your environment must be configured with
  **public network** webserver access. For more information, refer to [Apache Airflow access modes](configuring-networking.md "configuring-networking.md").
- **Amazon S3 configuration** — The [Amazon S3 bucket](mwaa-s3-bucket.md "mwaa-s3-bucket.md") used to store your DAGs, custom plugins in `plugins.zip`,
  and Python dependencies in `requirements.txt` must be configured with _Public Access Blocked_ and _Versioning Enabled_.

## Versioning overview

The `requirements.txt` and `plugins.zip` in your Amazon S3 bucket are versioned. When Amazon S3 bucket versioning is enabled for an object, and an artifact (for example, plugins.zip) is deleted from an Amazon S3 bucket, the file doesn't get deleted entirely. Anytime an artifact is deleted on Amazon S3, a new copy of the file is created that is a 404 (Object not found) error/0k file that says `I'm not here`. Amazon S3 calls this a _delete marker_. A delete marker is a "null" version of the file with a key name (or key) and version ID like any other object.

We recommend deleting file versions and delete markers periodically to reduce storage costs for your Amazon S3 bucket. To delete "non-current" (previous) file versions entirely, you must delete the versions of the files, and then the _delete marker_ for the version.

## How it works

Amazon MWAA runs a sync operation on your Amazon S3 bucket every thirty seconds. This causes any DAG deletions in an Amazon S3 bucket to be synced to the Airflow image of your Fargate container.

For `plugins.zip` and `requirements.txt` files, changes occur only after an environment update when Amazon MWAA builds a new Airflow image of your Fargate container with the custom plugins and Python dependencies. If you delete the _current_ version of any of a `requirements.txt` or `plugins.zip` file, and then update your environment without providing a new version for the deleted file, then the update will fail with an error message, such as, `Unable to read version {version number} of file {file name}`.

## Deleting a DAG on Amazon S3

A DAG file (`.py`) is not versioned and can be deleted directly on the Amazon S3 console. The following steps describe how to delete a DAG on your Amazon S3 bucket.

###### To delete a DAG

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Select the **S3 bucket** link in the **DAG code in S3** pane to open your storage bucket in the console.
4. Choose the `dags` folder.
5. Select the DAG, **Delete**.
6. Under **Delete objects?**, type `delete`.
7. Choose **Delete objects**.

###### Note

Apache Airflow preserves historical DAG runs. After a DAG has been run in Apache Airflow, it remains in the Airflow DAGs list regardless of the file status, until you delete it in Apache Airflow. To delete a DAG in Apache Airflow, choose the red "delete" button in the **Links** column.

## Removing a "current" requirements.txt or plugins.zip from an environment

Currently, there isn't a way to remove a plugins.zip or requirements.txt from an environment after they’ve been added, but we're working on the issue. In the interim, a workaround is to point to an empty text or zip file, respectively.

## Deleting a "non-current" (previous) requirements.txt or plugins.zip version

The `requirements.txt` and `plugins.zip` files in your Amazon S3 bucket are versioned on Amazon MWAA. If you want to delete these files on your Amazon S3 bucket entirely, you must retrieve the current version (121212) of the object (for example, plugins.zip), delete the version, and then remove the _delete marker_ for the file versions.

You can also delete "non-current" (previous) file versions on the Amazon S3 console; however, you'll still need to delete the _delete marker_ using one of the following options.

- To retrieve the object version, refer to [Retrieving object versions from a versioning-enabled bucket](../../../AmazonS3/latest/userguide/RetrievingObjectVersions.md "../../../AmazonS3/latest/userguide/RetrievingObjectVersions.md") _in the Amazon S3 guide_.
- To delete the object version, refer to [Deleting object versions from a versioning-enabled bucket](../../../AmazonS3/latest/userguide/DeletingObjectVersions.md "../../../AmazonS3/latest/userguide/DeletingObjectVersions.md") _in the Amazon S3 guide_.
- To remove a delete marker, refer to [Managing delete markers](../../../AmazonS3/latest/userguide/ManagingDelMarkers.md "../../../AmazonS3/latest/userguide/ManagingDelMarkers.md") _in the Amazon S3 guide_.

## Using lifecycles to delete "non-current" (previous) versions and delete markers automatically

You can configure a lifecycle policy for your Amazon S3 bucket to delete "non-current" (previous) versions of the plugins.zip and requirements.txt files in your Amazon S3 bucket after a certain number of days, or to remove an expired object's delete marker.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Under **DAG code in Amazon S3**, choose your Amazon S3 bucket.
4. Choose **Create lifecycle rule**.

## Example lifecycle policy to delete requirements.txt "non-current" versions and delete markers automatically

Use the following example to create a lifecycle rule that permanently deletes "non-current" versions of a requirements.txt file and their delete markers after thirty days.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Under **DAG code in Amazon S3**, choose your Amazon S3 bucket.
4. Choose **Create lifecycle rule**.
5. In **Lifecycle rule name**, type `Delete previous requirements.txt versions and delete markers after thirty days`.
6. In **Prefix**, **requirements**.
7. In **Lifecycle rule actions**, choose **Permanently delete previous versions of objects** and **Delete expired delete markers or incomplete multipart uploads**.
8. In **Number of days after objects become previous versions**, type `30`.
9. In **Expired object delete markers**, choose **Delete expired object delete markers, objects are permanently deleted after 30 days**.

## What's next?

- Learn more about Amazon S3 delete markers in [Managing delete markers](../../../AmazonS3/latest/user-guide/create-lifecycle.md "../../../AmazonS3/latest/user-guide/create-lifecycle.md").
- Learn more about Amazon S3 lifecycles in [Expiring objects](../../../AmazonS3/latest/userguide/lifecycle-expire-general-considerations.md "../../../AmazonS3/latest/userguide/lifecycle-expire-general-considerations.md").
