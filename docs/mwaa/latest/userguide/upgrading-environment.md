

# Changing the Apache Airflow version
<a name="upgrading-environment"></a>

 Amazon MWAA supports minor and major version upgrades and downgrades. 

A minor version upgrade means you can update your environment from version `x.4.z` to `x.5.z` or from `x.5.z` to `x.4.z`.

To perform a major version upgrade, for example from version `2.y.z` to `3.y.z`, you must first perform a minor upgrade to the latest Airflow `2.11.x` version followed by upgrade to `3.x`. Alternatively, to perform a major upgrade from Airflow `2.10.3` and below, you need to create a new environment and migrate your resources. You can also downgrade from Airflow version `3.y.z` to Airflow version `2.11.x`. For more information about upgrading to a new major version of Apache Airflow, see [Migrating to a new Amazon MWAA environment](https://docs.aws.amazon.com/mwaa/latest/migrationguide/migrating-to-new-mwaa.html). 

During the upgrade or downgrade process, Amazon MWAA captures a snapshot of your environment metadata, upgrades or downgrades the workers, schedulers, the web server to the new Apache Airflow version, and finally restores the metadata database using the snapshot.

Before you upgrade or downgrade, make sure that your DAGs and other workflow resources are compatible with the new Apache Airflow version you're upgrading to. If you use `requirements.txt` to manage dependencies, you must also ensure that the dependencies you specify in your requirements are compatible with the new version.

**Topics**
+ [Upgrade or downgrade your workflow resources](#upgrading-environment-resources)
+ [Specify the new version](#upgrading-environment-specify-version)

## Upgrade or downgrade your workflow resources
<a name="upgrading-environment-resources"></a>

Whenever you're changing Apache Airflow versions, ensure that you [reference the correct `--constraint`](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html#working-dags-dependencies-test-create) URL in your `requirements.txt`.

**Warning**  
 Specifying requirements that are incompatible with your target Apache Airflow version during an upgrade or downgrade might result in a lengthy rollback process to the previous version of Apache Airflow with the previous requirements version.

**Migrate your workflow resources**

1. Create a fork of the [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images) repository, and clone a copy of the Amazon MWAA local runner.

1.  Checkout to the branch of the aws-mwaa-docker-images repository that matches the version you are upgrading or downgrading to. 

1. To update your `requirements.txt`, follow the best practices we recommend in [Managing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices-dependencies.html), in the *Amazon MWAA User Guide*.

1.  (Optional) To speed up the upgrade or downgrade process, [clean up the environment's metadata database](samples-database-cleanup.md). Environments with a large amount of metadata can take significantly longer to upgrade.

1. After you have successfully tested your workflow resources, copy your DAGs, `requirements.txt`, and plugins to your environment's Amazon S3 bucket.

You are now ready to edit the environment, specify a new Apache Airflow version, and start the update procedure.

## Specify the new version
<a name="upgrading-environment-specify-version"></a>

After you have completed updating your workflow resources to ensure compatibility with the new Apache Airflow version, do the following to edit environment details and specify the version of Apache Airflow that you want to upgrade to.

**Note**  
When you perform an upgrade or downgrade, all tasks currently running on the environment are terminated during the procedure. The update procedure can take up to two hours, during which time your environment will be unavailable.

**Specify a new version using the console**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1.  From the **Environments** list, choose the environment that you want to upgrade or downgrade. 

1. On the environment page, choose **Edit** to edit the environment.

1.  In the **Environment details** section, for **Airflow version**, choose the Apache Airflow version number that you want to upgrade or downgrade the environment to from the dropdown list.

1. Choose **Next** until you are on the **Review and save** page.

1. On the **Review and save** page, review your changes, then choose **Save**.

When you apply changes, your environment begins the upgrade or downgrade procedure. During this period, the [status](https://docs.aws.amazon.com/mwaa/latest/API/API_Environment.html#mwaa-Type-Environment-Status) of your environment indicates what actions Amazon MWAA is taking, and whether the procedure is successful.

In a successful upgrade or downgrade scenario, the status will be `UPDATING`, then `CREATING_SNAPSHOT` as Amazon MWAA captures a backup of your metadata. Finally, the status will return first to `UPDATING`, then to `AVAILABLE` when the procedure is done.

If the environment fails to upgrade or downgrade, your environment status will be `ROLLING_BACK`. If the rollback is successful, the status will first present `UPDATE_FAILED`, indicating that the update failed but the environment is available. If the rollback fails, the status will be `UNAVAILABLE`, indicating that you cannot access the environment.