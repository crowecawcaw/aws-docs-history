

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy a sample stateful workload to EKS Auto Mode
<a name="sample-storage-workload"></a>

This tutorial will guide you through deploying a sample stateful application to your EKS Auto Mode cluster. The application writes timestamps to a persistent volume, demonstrating EKS Auto Mode’s automatic EBS volume provisioning and persistence capabilities.

## Prerequisites
<a name="_prerequisites"></a>
+ An EKS Auto Mode cluster
+ The AWS CLI configured with appropriate permissions
+  `kubectl` installed and configured
  + For more information, see [Set up to use Amazon EKS](setting-up.md).

## Step 1: Configure your environment
<a name="_step_1_configure_your_environment"></a>

1. Set your environment variables:

   ```
   export CLUSTER_NAME=my-auto-cluster
   export AWS_REGION="us-west-2"
   ```

1. Update your kubeconfig:

   ```
   aws eks update-kubeconfig --name "${CLUSTER_NAME}"
   ```

## Step 2: Create the storage class
<a name="_step_2_create_the_storage_class"></a>

The `StorageClass` defines how EKS Auto Mode will provision EBS volumes.

EKS Auto Mode does not create a `StorageClass` for you. You must create a `StorageClass` referencing `ebs.csi.eks.amazonaws.com` to use the storage capability of EKS Auto Mode.

1. Create a file named `storage-class.yaml`:

   ```
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: auto-ebs-sc
     annotations:
       storageclass.kubernetes.io/is-default-class: "true"
   provisioner: ebs.csi.eks.amazonaws.com
   volumeBindingMode: WaitForFirstConsumer
   parameters:
     type: gp3
     encrypted: "true"
   ```

1. Apply the `StorageClass`:

   ```
   kubectl apply -f storage-class.yaml
   ```

 **Key components:** 
+  `provisioner: ebs.csi.eks.amazonaws.com` - Uses EKS Auto Mode
+  `volumeBindingMode: WaitForFirstConsumer` - Delays volume creation until a pod needs it
+  `type: gp3` - Specifies the EBS volume type
+  `encrypted: "true"` - EBS will use the default `aws/ebs` key to encrypt volumes created with this class. This is optional, but recommended.
+  `storageclass.kubernetes.io/is-default-class: "true"` - Kubernetes will use this storage class by default, unless you specify a different volume class on a persistent volume claim. Use caution when setting this value if you are migrating from another storage controller. (optional)

## Step 3: Create the persistent volume claim
<a name="_step_3_create_the_persistent_volume_claim"></a>

The PVC requests storage from the `StorageClass`.

1. Create a file named `pvc.yaml`:

   ```
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: auto-ebs-claim
   spec:
     accessModes:
       - ReadWriteOnce
     storageClassName: auto-ebs-sc
     resources:
       requests:
         storage: 8Gi
   ```

1. Apply the PVC:

   ```
   kubectl apply -f pvc.yaml
   ```

 **Key components:** 
+  `accessModes: ReadWriteOnce` - Volume can be mounted by one node at a time
+  `storage: 8Gi` - Requests an 8 GiB volume
+  `storageClassName: auto-ebs-sc` - References the `StorageClass` we created

## Step 4: Deploy the Application
<a name="_step_4_deploy_the_application"></a>

The Deployment runs a container that writes timestamps to the persistent volume.

1. Create a file named `deployment.yaml`:

   ```
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: inflate-stateful
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: inflate-stateful
     template:
       metadata:
         labels:
           app: inflate-stateful
       spec:
         terminationGracePeriodSeconds: 0
         nodeSelector:
           eks.amazonaws.com/compute-type: auto
         containers:
           - name: bash
             image: public.ecr.aws/docker/library/bash:4.4
             command: ["/usr/local/bin/bash"]
             args: ["-c", "while true; do echo $(date -u) >> /data/out.txt; sleep 60; done"]
             resources:
               requests:
                 cpu: "1"
             volumeMounts:
               - name: persistent-storage
                 mountPath: /data
         volumes:
           - name: persistent-storage
             persistentVolumeClaim:
               claimName: auto-ebs-claim
   ```

1. Apply the Deployment:

   ```
   kubectl apply -f deployment.yaml
   ```

 **Key components:** 
+ Simple bash container that writes timestamps to a file
+ Mounts the PVC at `/data` 
+ Requests 1 CPU core
+ Uses node selector for EKS managed nodes

## Step 5: Verify the Setup
<a name="_step_5_verify_the_setup"></a>

1. Check that the pod is running:

   ```
   kubectl get pods -l app=inflate-stateful
   ```

1. Verify the PVC is bound:

   ```
   kubectl get pvc auto-ebs-claim
   ```

1. Check the EBS volume:

   ```
   # Get the PV name
   PV_NAME=$(kubectl get pvc auto-ebs-claim -o jsonpath='{.spec.volumeName}')
   # Describe the EBS volume
   aws ec2 describe-volumes \
     --filters Name=tag:CSIVolumeName,Values=${PV_NAME}
   ```

1. Verify data is being written:

   ```
   kubectl exec "$(kubectl get pods -l app=inflate-stateful \
     -o=jsonpath='{.items[0].metadata.name}')" -- \
     cat /data/out.txt
   ```

## Step 6: Cleanup
<a name="_step_6_cleanup"></a>

Run the following command to remove all resources created in this tutorial:

```
# Delete all resources in one command
kubectl delete deployment/inflate-stateful pvc/auto-ebs-claim storageclass/auto-ebs-sc
```

## What’s Happening Behind the Scenes
<a name="_whats_happening_behind_the_scenes"></a>

1. The PVC requests storage from the `StorageClass` 

1. When the Pod is scheduled:

   1. EKS Auto Mode provisions an EBS volume

   1. Creates a PersistentVolume

   1. Attaches the volume to the node

1. The Pod mounts the volume and begins writing timestamps

## Snapshot Controller
<a name="_snapshot_controller"></a>

EKS Auto Mode is compatible with the Kubernetes CSI Snapshotter, also known as the snapshot controller. However, EKS Auto Mode does not include the snapshot controller. You are responsible for installing and configuring the snapshot controller. For more information, see [Enable snapshot functionality for CSI volumes](csi-snapshot-controller.md).

Review the following `VolumeSnapshotClass` that references the storage capability of EKS Auto Mode.

```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: auto-ebs-vsclass
driver: ebs.csi.eks.amazonaws.com
deletionPolicy: Delete
```

 [Learn more about the Kubernetes CSI Snapshotter.](https://github.com/kubernetes-csi/external-snapshotter/blob/master/README.md#usage) 