# Deployment troubleshooting

## Problem: MSK cluster deployment timeout

MSK cluster creation takes longer than expected or times out during CDK deployment.

### Resolution

MSK cluster creation typically takes 15-20 minutes. This is normal AWS behavior. If the deployment times out:

1. Check the CloudFormation stack status:

```
aws cloudformation describe-stacks --stack-name cms-dev-msk \
  --query "Stacks[0].StackStatus"
```

2. If the stack is in `CREATE_IN_PROGRESS`, wait for it to complete. Do not cancel the deployment.
3. If the stack is in `ROLLBACK_COMPLETE`, delete it and retry:

```
aws cloudformation delete-stack --stack-name cms-dev-msk
# Wait for deletion, then redeploy
cd deployment && make phase3
```

## Problem: VPC Destination creation fails

The TelemetryIntegrationStack fails when creating the IoT Rule VPC Destination.

### Resolution

1. Verify the MSK cluster is in `ACTIVE` state:

```
aws kafka list-clusters \
  --query "ClusterInfoList[?contains(ClusterName, 'cms-dev')].[ClusterName,State]" \
  --output table
```

2. Verify the VPC has available ENI capacity. VPC Destinations create ENIs in the private subnets.
3. Check that the security group allows inbound traffic on the MSK broker port (9098 for IAM auth).
4. Redeploy the integration stack:

```
cd deployment && make phase3b
```

## Problem: Flink JAR not found during deployment

The FlinkStack deployment fails because the JAR file is not in S3.

### Resolution

1. Build the Flink JAR:

```
cd modules/flink
mvn clean package -DskipTests
```

2. Package and upload to S3:

```
cd target
zip -j /tmp/cms-telemetry-processor-1.0.0.zip \
  cms-telemetry-processor-1.0.0.jar

# Get the S3 bucket name from CloudFormation outputs
BUCKET=$(aws cloudformation describe-stacks --stack-name cms-dev-flink \
  --query "Stacks[0].Outputs[?OutputKey=='FlinkJarBucketOutput'].OutputValue" \
  --output text)
aws s3 cp /tmp/cms-telemetry-processor-1.0.0.zip s3://$BUCKET/jars/
```

3. Redeploy the Flink stack:

```
cd deployment && make phase4
```
