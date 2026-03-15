# Verifying connectivity

To verify that VPC connectivity is working correctly:

1. Start a stream session using your stream group.
2. From within your streaming application, connect to a resource in your VPC using
   its private IP address.
3. Verify that the connection succeeds and data can be exchanged.
   If connectivity fails, check the following:

- The transit gateway attachment is in the `available` state.
- Routes are correctly configured in both your VPC route table and the transit gateway route
  table.
- Security groups allow inbound traffic from the service VPC CIDR block.
- Network ACLs (if used) allow the required traffic.
