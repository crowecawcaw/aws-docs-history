# Troubleshooting

This section describes how to debug and troubleshoot common issues when
working with AWS Lambda MicroVMs.

## Shell access

Use shell access to connect directly to a running MicroVM for debugging
and troubleshooting.

You can connect to a MicroVM shell in two ways:

- **Console** – Select your MicroVM in the Lambda console and choose Connect.
- **CLI** – Generate a shell token with `create-microvm-shell-auth-token`, then use the token to establish a connection.

Generate a shell token, then connect:

```
aws lambda-microvms create-microvm-shell-auth-token \
  --microvm-identifier <id> --expiration-in-minutes 30
# In Console: select MicroVM -> Connect
# In shell: ctr task ls, then ctr task exec -t --exec-id shell <id> /bin/sh
```

The MicroVM must have been run with the `SHELL_INGRESS`
network connector
(`arn:aws:lambda:`us-east-1`:aws:network-connector:aws-network-connector:SHELL_INGRESS`).
If the MicroVM was not launched with this connector,
`create-microvm-shell-auth-token` returns a
`ValidationException`.

For other issues:

- Check the `terminationMessage` field in the
  `get-microvm` response for terminated MicroVMs.
- Check CloudWatch build logs for image creation issues.
- Check the `StateReason` field for network connectors in
  `FAILED` state.

## Troubleshooting

This section provides solutions for common issues when working with Lambda
MicroVMs.

| Symptom                                 | Possible cause and resolution                                                                                                                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Image build fails (`CREATION_FAILED`)   | Check build logs at<br>`/aws/lambda/microvms/<image-name>`. Verify<br>`Dockerfile` syntax, Amazon S3 permissions, and base image<br>availability. Run `docker build` locally to<br>reproduce.                |
| MicroVM stuck in `PENDING`              | Wait and retry. If persistent, check service health. Verify your<br>concurrency quota is not exhausted.                                                                                                      |
| Application not responding after resume | Implement the `/resume` lifecycle hook to re-establish<br>connections and validate state. Check that your app binds to port 8080<br>(or configured port) after resume.                                       |
| 502 Bad Gateway from endpoint           | Application crashed or is not listening. Check runtime logs.<br>Verify `EXPOSE` and `CMD` in<br>`Dockerfile`. If auto-resume, the MicroVM may have failed to<br>resume (check state by using `get-microvm`). |
| 429 Too Many Requests                   | Request rate exceeded. Retry with exponential backoff and<br>jitter.                                                                                                                                         |
| Connections dropping                    | Idle timeout triggered. Implement ping/pong keepalives. Or extend<br>`maxIdleDurationSeconds` in the idle policy.                                                                                            |
| High latency on endpoint                | Bandwidth saturation. Check if traffic exceeds the bandwidth<br>capability for your MicroVM size. Scale up to a larger<br>size.                                                                              |
| Auth token expired (403)                | Tokens have a configurable expiration. Generate a new token before<br>the old one expires. Implement token refresh logic in your<br>client.                                                                  |
| VPC egress not working                  | Verify network connector is in `ACTIVE` state. Check<br>security group rules allow outbound traffic. Confirm subnets have<br>routes to your target resources.                                                |

## Common errors (image creation)

| Error                           | Cause                                                                  | Solution                                                             |
| ------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `S3_ACCESS_DENIED`              | Build role lacks permissions to retrieve Amazon S3 artifact.           | Add `s3:GetObject` permission for your artifact<br>bucket.           |
| `S3_NO_SUCH_KEY`                | Artifact key does not exist in the bucket.                             | Verify the Amazon S3 path is correct.                                |
| `S3_NO_SUCH_BUCKET`             | Amazon S3 bucket does not exist.                                       | Check the bucket name and confirm it has been created.               |
| `S3_INVALID_OBJECT`             | Artifact in Glacier or non-directly-accessible storage<br>class.       | Move the artifact to Standard storage class.                         |
| `S3_CROSS_REGION_ACCESS_DENIED` | Artifact is in a different Region than the MicroVM image.              | Ensure your artifact is in the same Region as your MicroVM<br>image. |
| `ARCHIVE_DOCKERFILE_NOT_FOUND`  | Zip archive is missing a `Dockerfile` in the root<br>directory.        | Add a `Dockerfile` to the root of your zip<br>archive.               |
| `ARCHIVE_INVALID`               | Archive file is not a valid ZIP or is corrupted.                       | Re-create the zip archive and re-upload.                             |
| `CONTAINER_BUILD_FAILED`        | Invalid `Dockerfile` instructions, missing files, or<br>syntax errors. | Debug your `Dockerfile` locally using<br>`docker build`.             |
| `DISK_STORAGE_FULL`             | MicroVM ran out of storage during build.                               | Reduce artifact size or contact support.                             |
| `INTERNAL_PLATFORM_ERROR`       | An internal error occurred.                                            | Retry the operation. If persistent, contact support.                 |

## Network connector troubleshooting

| Error code                         | Cause                                                                                                                                                                       | Solution                                                                                                                                                                                      |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DisallowedByVpcEncryptionControl` | The VPC has an encryption control policy that prevents<br>unencrypted network interfaces or traffic. Lambda cannot create ENIs<br>that satisfy the encryption requirements. | Add Lambda to the VPC encryption control exclusion list. If<br>exclusion is not possible, use a VPC or subnet that does not have<br>restrictive encryption controls applied.                  |
| `Ec2RequestLimitExceeded`          | Lambda makes EC2 API calls (for example,<br>`CreateNetworkInterface`, `DescribeSubnets`) to<br>set up connectivity. Too many concurrent EC2 API calls causes<br>throttling. | Retry the operation after a short delay. If persistent, reduce<br>concurrent network connector operations or request an EC2 API<br>throttling limit increase through AWS Support.             |
| `InsufficientRolePermissions`      | The operator role lacks required EC2 permissions.                                                                                                                           | Ensure the IAM role has necessary EC2 networking<br>permissions.                                                                                                                              |
| `InternalError`                    | An unexpected error occurred within the Lambda service while<br>processing the network connector request.                                                                   | Retry the operation. If it persists after multiple retries,<br>contact AWS Support with the network connector ARN and approximate<br>timestamp.                                               |
| `InvalidSecurityGroup`             | The security group ID does not exist, has been deleted, or does<br>not belong to the same VPC as the specified subnets.                                                     | Verify all security group IDs exist and belong to the same VPC as<br>the subnets. Use `aws ec2 describe-security-groups --group-ids<br><sg-id>` to validate.                                  |
| `InvalidSubnet`                    | The subnet ID does not exist, has been deleted, or belongs to a<br>different VPC than expected.                                                                             | Verify all subnet IDs exist and belong to the correct VPC. Use<br>`aws ec2 describe-subnets --subnet-ids <subnet-id>` to<br>validate.                                                         |
| `SubnetOutOfIPAddresses`           | The subnet's CIDR block is exhausted – all IPs are<br>allocated to ENIs, instances, and other resources, so Lambda cannot<br>create a network interface.                    | Free up IP addresses by removing unused ENIs/instances, or use a<br>different subnet with available capacity. Consider larger subnets (for<br>example, /24 or larger) for network connectors. |
