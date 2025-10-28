# Uninstall the Amazon EMR on EKS vertical

autoscaling operator

If you want to remove the vertical autoscaling operator from your Amazon EKS cluster, use the
`cleanup` command with the Operator SDK CLI as shown in the following example.
This also deletes upstream dependencies that installed with the operator, such as the
Vertical Pod Autoscaler.

```
operator-sdk cleanup emr-dynamic-sizing
```

If there are any running jobs on the cluster when you delete the operator, those jobs
continue to run without vertical autoscaling. If you submit jobs on the cluster after you
delete the operator, Amazon EMR on EKS will ignore any vertical autoscaling-related parameters that
you may have defined during [configuration](jobruns-vas-configure.md "jobruns-vas-configure.md").
