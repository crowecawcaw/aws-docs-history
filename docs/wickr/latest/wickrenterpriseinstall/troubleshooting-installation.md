This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Troubleshooting Wickr embedded cluster

installations

All instances of these troubleshooting steps assume you have shell access to the instance
running the Wickr Embedded Cluster installation and have run the `./wickr-enterprise-ha
 shell` command to be able to interact with the Kubernetes installation directly.

## General issues

**Add Node Button Missing From Cluster Management Screen**

**_Airgapped Installs_**

If you are on an airgap installation, please reach out to Wickr Support for assistance in
correcting this behavior.

**_Standard Installs_**

If your license includes the Embedded Cluster Multi-Node entitlement, perform a license
sync to get the latest version. If you are unsure or do not have this entitlement, please reach
out to Wickr Support.

To perform a license sync, complete the following steps.

1. Navigate to the KOTS control panel.
2. On the **Dashboard** page, locate the license section in the upper right
   area of the page.
3. Within this section, in the top right corner, you should see a **Sync
   License** hyperlink. Select the hyperlink.
4. Once the license has been synced, the UI updates and **Last synced a few seconds
   ago** appears.
5. Choose **Redeploy** from the **Version** section of the
   KOTS dashboard page.
6. Once the redeploy finishes, navigate back to **Cluster management** and
   you can add nodes.

## Upgrade issues

**Upgrade Stuck on Upgrading Cluster**

If your upgrade gets stuck on **Upgrading Cluster** this likely means that
some pods are not being terminated appropriately. Log on to the instance and use the
`./wickr-enteprise-ha shell` command to enter the shell environment for managing the
kubernetes installation.

1. Identity the pods that are still running:

`kubectl -n kotsadm get pods | grep Running` 2. `kubectl -n kotsadm delete pod
 `name-of-running-pod``

###### Note

If one of the running pods is `embedded-cluster-upgrade-XXXXXXXXXXXXXX-xxxxx`
or `kotsadm-xxxxxxx` or similar, do not delete it as these pods are necessary for
performing the upgrade. 3. Verify there are no remaining running pods.

`kubectl -n kotsadm get pods | grep Running`

This procedure should allow the cluster upgrade to proceed by the Wickr upgrade.

**Application Did Not Update During Cluster Upgrade And Cannot Deploy New
Version**

If the application remains on the old version after the upgrade, the new version may be in
an inconsistent state.

Check the Kubernetes installation records:

1. Open the Kubernetes shell from the installer.

`./wickr-enterprise-ha shell` 2. Run the following kubectl command:

`kubectl get installations` 3. Output will look something like this:

```

      [root@ip-172-31-6-72 ~]# kubectl get installations
NAME             STATE      INSTALLERVERSION   CREATEDAT              AGE
20251113170603   Obsolete   2.1.3+k8s-1.30     2025-11-13T17:06:05Z   22h
20251113180133   Failed     2.6.0+k8s-1.31     2025-11-13T18:01:37Z   21h

```

4. Delete the failed installation.

`kubectl delete installation 20251113180133` 5. Attempt to run the upgrade again through KOTS Admin panel.

**RabbitMQ Pod Failing with log lines `Error while waiting for Mnesia tables:
 {timeout_waiting_for_tables}`**

The RabbitMQ secret and storage are out of sync. This usually happens when multiple
RabbitMQ instances run and cause leader selection or quorum error. To fix this, delete the
RabbitMQ service and its storage volumes, then redeploy.

To delete the failing RabbitMQ, complete the following steps.

1. Delete the RabbitMQ Statefulset.

`kubectl -n kotsadm delete statefulset rabbitmq —cascade=orphan` 2. Delete the remaining RabbitMQ pods. If there are multiple RabbitMQ-X pods running, issue
this command multiple times updating the RabbitMQ-X value to correspond to the additional pod
names.

`kubectl -n kotsadm delete pod rabbitmq-0` 3. Delete the corresponding PVCs. If there are multiple pods running, issue this command
multiple times updating the data-RabbitMQ-X to correspond to the appropriate pods.

`kubectl -n kotsadm delete pvc data-rabbitmq-0` 4. Check if there are any remaining pods, this should output nothing if successful.

`kubectl -n kotsadm get pods|grep -i rabbitmq` 5. Check if there are any remaining PVCs, this should output nothing if successful.

`kubectl -n kotsadm get pvc|grep -i rabbitmq` 6. Redeploy through KOTS Admin Panel.

For more troubleshooting information, see [Troubleshooting](troubleshooting.md "troubleshooting.md").
