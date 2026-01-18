# Uninstall the Guidance

## Uninstall steps

### Step 1: Stop data ingestion

```
 # Stop fleet simulator if running
# Disconnect vehicles from IoT Core
```

### Step 2: Delete CDK stacks in reverse order

```
 cd deployment

cdk destroy cms-<stage>-flink
cdk destroy cms-<stage>-telemetry-integration
cdk destroy cms-<stage>-msk
cdk destroy cms-<stage>-ui
cdk destroy cms-<stage>-iot
cdk destroy cms-<stage>-storage
```

### Step 3: Clean up additional resources

```
 # Remove S3 buckets (if not automatically deleted)
aws s3 rb s3://cms-<stage>-<bucket-name> --force
```
