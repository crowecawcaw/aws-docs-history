# Troubleshooting

If your calls to the Amazon WorkSpaces Secure Browser APIs are hanging, there is likely a misconfiguration in
your VPC Endpoint Service security group or IAM role setup. To resolve this, try the
following:

- While creating your interface VPC endpoint, it might have automatically attached
  to your AWS account’s default security group. Try using a different security group,
  and make sure the inbound and outbound permissions allow you to transfer your data
  appropriately.
- Make sure you are using an IAM role that allows you to call Amazon WorkSpaces Secure Browser APIs.
