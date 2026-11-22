

# Update a resource gateway in VPC Lattice

After you create a resource gateway, you can update its security groups and its Resource Config DNS Resolution setting.

**To update a resource gateway using the AWS CLI**  
Use the `update-resource-gateway` command. Change DNS resolution in a separate request, without other changes. The update is asynchronous: the resource gateway status is `UPDATE_IN_PROGRESS`, then `ACTIVE`. If the update fails, the status is `UPDATE_FAILED` and the setting reverts to its previous value. The following example changes DNS resolution to `IN_VPC`.

```
aws vpc-lattice update-resource-gateway \
  --resource-gateway-identifier rgw-0123456789abcdef0 \
  --resource-config-dns-resolution IN_VPC
```