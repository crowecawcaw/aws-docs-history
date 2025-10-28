# Enable Internet

Access for WorkSpaces Pools

After your NAT gateway is available on a VPC, you can enable internet access
for your WorkSpaces Pools. You can enable internet access when you [create the
WorkSpaces Pool directory](create-directory-pools.md "create-directory-pools.md"). Choose the VPC with a NAT gateway when you
create the directory. Then select a private subnet for **Subnet
1** and, optionally, another private subnet for **Subnet
2**. If you don't already have a private subnet in your VPC, you
may need to create a second private subnet.

You can test your internet connectivity by starting your WorkSpaces Pool, and then
connecting to a WorkSpace in the pool and browsing to the internet.
