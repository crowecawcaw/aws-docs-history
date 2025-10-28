# Monitoring vertical autoscaling for Amazon EMR on EKS

You can use the **kubectl** Kubernetes command line tool to list the active, vertical
autoscaling-related recommendations on your cluster. You can also view your tracked job
signatures, and purge any unneeded resources that are associated with the signatures.

## List the vertical autoscaling recommendations

for your cluster

Use kubectl to get the `verticalpodautoscaler` resource, and view the
current status and recommendations. The following example query returns all active
resources on your Amazon EKS cluster.

```
kubectl get verticalpodautoscalers \
-o custom-columns="NAME:.metadata.name,"\
"SIGNATURE:.metadata.labels.emr-containers\.amazonaws\.com/dynamic\.sizing\.signature,"\
"MODE:.spec.updatePolicy.updateMode,"\
"MEM:.status.recommendation.containerRecommendations[0].target.memory" \
--all-namespaces
```

The output from this query resembles the following:

```
NAME                  SIGNATURE                MODE      MEM
ds-`example-id-1`-vpa   `job-signature-1`          Off       `none`
ds-`example-id-2`-vpa   `job-signature-2`          Initial   12936384283
```

## Query and delete the vertical autoscaling

recommendations for your cluster

When you delete an Amazon EMR vertical autoscaling job-run resource, it automatically
deletes the associated VPA object that tracks and stores recommendations.

The following example uses kubectl to purge recommendations for a job that is
identified by a signature:

```
kubectl delete jobrun -n emr -l=emr-containers\.amazonaws\.com/dynamic\.sizing\.signature=integ-test
jobrun.dynamicsizing.emr.services.k8s.aws "ds-`job-signature`" deleted
```

If you don't know the specific job signature, or want to purge all of the resources on
the cluster, you can use `--all` or `--all-namespaces` in your
command instead of the unique job ID, as shown in the following example:

```
kubectl delete jobruns --all --all-namespaces
jobrun.dynamicsizing.emr.services.k8s.aws "ds-`example-id`" deleted
```
