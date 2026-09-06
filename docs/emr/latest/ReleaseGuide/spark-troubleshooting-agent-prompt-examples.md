

# Prompt Examples
<a name="spark-troubleshooting-agent-prompt-examples"></a>

Here is a list of prompt examples that can be used in the troubleshooting experience.

## 1. Troubleshoot Spark job execution failure
<a name="troubleshoot-job-failure"></a>

EMR on EC2 Troubleshooting:

```
Troubleshoot my EMR-EC2 step with id s-xxxxxxxxxxxx on cluster j-xxxxxxxxxxxxx
```

Glue Job Troubleshooting:

```
Troubleshoot my Glue job with job run id jr_xxxxxxxxxxxxxxxxxxxxxxxxxxxx and job name test_job
```

EMR Serverless Troubleshooting:

```
Troubleshoot my EMR-Serverless job run with application id 00xxxxxxxx and job run id 00xxxxxxxx
```

EMR on EKS Troubleshooting:

```
Troubleshoot my EMR on EKS job run with virtual cluster id <vc-id> and job run id <jr-id>
```

## 2. Request for code fix recommendation
<a name="request-code-fix"></a>

Request code fix recommendation for EMR on EC2 job:

```
Recommend code fix for my EMR on EC2 step with id s-STEP_ID on cluster j-CLUSTER_ID
```

Request code fix recommendation for Glue job:

```
Recommend code fix for my Glue job with job run id jr_JOB_RUN_ID and job name test_job
```

Request code fix recommendation for EMR Serverless job:

```
Recommend code fix for my EMR Serverless job run with application id 00xxxxxxxx and job run id 00xxxxxxxx
```

Request code fix recommendation for EMR on EKS job:

```
Recommend code fix for my EMR on EKS job run with virtual cluster id <vc-id> and job run id <jr-id>
```