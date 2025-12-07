# Prompt Examples for the Spark Upgrade Agent

We list a few different prompt examples that can be used in the upgrade process.

## 1. Provide existing EMR Step information for the agent for upgrading a Spark application

```
Upgrade my Spark application <local-project-path> from EMR version 6.0.0 to 7.12.0.
Use EMR-EC2 Cluster <cluster-id> to run the validation and s3 paths
s3://<please fill in your staging bucket path> to store updated application artifacts. The Spark
application is already executed in the source EMR-EC2 Cluster <cluster-id> with
step id <step-id>.
```

## 2. List analysis (used for Upgrades) and check the status of a specific analysis

```
Can you list all the spark upgrade analysis.
```

```
Describe the analysis with analysis id <analysis id>.
```

## 3. Modify an upgrade plan after it's generated

```
Help me to update the generated upgrade plan to skip the local test step.
```

## 4. Override the default configuration for a upgrade validation job execution

```
For submitting my EMR Severless validaiton job. I would like to use S3 logging instead
of CW logging, and use this S3 path <S3 path prefix>.
```
