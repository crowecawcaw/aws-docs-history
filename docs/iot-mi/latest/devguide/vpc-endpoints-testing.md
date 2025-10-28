# Testing your VPC endpoint

After you create your VPC endpoint, you can test the connection by making API calls to AWS IoT Managed integrations from an EC2 instance in your VPC.

## Prerequisites

- An EC2 instance in a private subnet within your VPC
- Appropriate IAM permissions for AWS IoT Managed integrations operations
- Security group rules that allow HTTPS traffic (port 443) to the VPC endpoint

## Testing the connection

1. Connect to your Amazon EC2 instance in the private subnet.
2. Verify DNS resolution for the private DNS name:

```
dig api.iotmanagedintegrations.region.api.aws
```

3. Test HTTPS connectivity:

```
curl -v https://api.iotmanagedintegrations.region.api.aws
```

4. Make an AWS IoT Managed integrations API call:

```
aws iot-managed-integrations list-destinations \
  --region region \
  --endpoint-url https://api.iotmanagedintegrations.region.api.aws
```

Replace `region` with your AWS Region (for example, `ca-central-1`).
