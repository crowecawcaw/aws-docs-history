# Changing the Apache Airflow version

Amazon MWAA supports minor version upgrades and downgrades. This means you can update your environment from version `x.**4**.z` to `x.**5**.z` or from `x.**5**.z` to `x.**4**.z`. To perform a major version upgrade, for example from version `**1**.y.z` to `**2**.y.z`, you must create a new environment and migrate your resources. For more information about upgrading to a new major version of Apache Airflow, refer to [Migrating to a new Amazon MWAA environment](../migrationguide/migrating-to-new-mwaa.md "../migrationguide/migrating-to-new-mwaa.md") in the _Amazon MWAA Migration Guide_.

During the upgrade or downgrade process, Amazon MWAA captures a snapshot of your environment metadata, upgrades or downgrades the workers, schedulers, the web server to the new Apache Airflow version, and finally restores the metadata database using the snapshot.

Before you upgrade or downgrade, make sure that your DAGs and other workflow resources are compatible with the new Apache Airflow version you're upgrading to. If you use `requirements.txt` to manage dependencies, you must also ensure that the dependencies you specify in your requirements are compatible with the new version.

###### Topics

- [Upgrade or downgrade your workflow resources](#upgrading-environment-resources "#upgrading-environment-resources")
- [Specify the new version](#upgrading-environment-specify-version "#upgrading-environment-specify-version")

## Upgrade or downgrade your workflow resources

Whenever you're changing Apache Airflow versions, ensure that you [reference the correct `--constraint`](working-dags-dependencies.md#working-dags-dependencies-test-create "working-dags-dependencies.md#working-dags-dependencies-test-create") URL in your `requirements.txt`.

###### Warning

Specifying requirements that are incompatible with your target Apache Airflow version during an upgrade or downgrade might result in a lengthy rollback process to the previous version of Apache Airflow with the previous requirements version.

###### Migrate your workflow resources

1. Create a fork of the [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") repository, and clone a copy of the Amazon MWAA local runner.
2. Checkout to the branch of the aws-mwaa-docker-images repository that matches the version you are upgrading or downgrading to.
3. To update your `requirements.txt`, follow the best practices we recommend in [Managing Python dependencies](best-practices-dependencies.md "best-practices-dependencies.md"), in the _Amazon MWAA User Guide_.
4. (Optional) To speed up the upgrade or downgrade process, [clean up the environment's metadata database](samples-database-cleanup.md "samples-database-cleanup.md"). Environments with a large amount of metadata can take significantly longer to upgrade.
5. After you have successfully tested your workflow resources, copy your DAGs, `requirements.txt`, and plugins to your environment's Amazon S3 bucket.

You are now ready to edit the environment, specify a new Apache Airflow version, and start the update procedure.

## Specify the new version

After you have completed updating your workflow resources to ensure compatibility with the new Apache Airflow version, do the following to edit environment details and specify the version of Apache Airflow that you want to upgrade to.

###### Note

When you perform an upgrade or downgrade, all tasks currently running on the environment are terminated during the procedure. The update procedure can take up to two hours, during which time your environment will be unavailable.

###### Specify a new version using the console

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. From the **Environments** list, choose the environment that you want to upgrade or downgrade.
3. On the environment page, choose **Edit** to edit the environment.
4. In the **Environment details** section, for **Airflow version**, choose the Apache Airflow version number that you want to upgrade or downgrade the environment to from the dropdown list.
5. Choose **Next** until you are on the **Review and save** page.
6. On the **Review and save** page, review your changes, then choose **Save**.

When you apply changes, your environment begins the upgrade or downgrade procedure. During this period, the [status](../API/API_Environment.md#mwaa-Type-Environment-Status "../API/API_Environment.md#mwaa-Type-Environment-Status") of your environment indicates what actions Amazon MWAA is taking, and whether the procedure is successful.

In a successful upgrade or downgrade scenario, the status will be `UPDATING`, then `CREATING_SNAPSHOT` as Amazon MWAA captures a backup of your metadata. Finally, the status will return first to `UPDATING`, then to `AVAILABLE` when the procedure is done.

If the environment fails to updrade or downgrade, your environment status will be `ROLLING_BACK`. If the rollback is successful, the status will first present `UPDATE_FAILED`, indicating that the update failed but the environment is available. If the rollback fails, the status will be `UNAVAILABLE`, indicating that you cannot access the environment.
