# Configure permissions to work with user-defined types (UDTs) in Amazon Keyspaces

Like tables, UDTs are bound to a specific keyspace. But unlike tables, you can't
define permissions directly for UDTs. UDTs are not considered resources in AWS and
they have no unique identifiers in the format of an Amazon Resource Name (ARN). Instead,
to give an IAM principal permissions to perform specific actions on a UDT, you have
to define permissions for the keyspace that the UDT is bound to. To work with UDTs in
multi-Region keyspaces, additional permissions are required.

To be able to create, view, or delete UDTs, the principal, for example
an IAM user or role, needs the same permissions that are required to perform the same action on the keyspace that the UDT is bound to.

For more information about AWS Identity and Access Management, see [AWS Identity and Access Management for Amazon Keyspaces](security-iam.md "security-iam.md").

## Permissions to create a UDT

To create a UDT in a single-Region keyspace, the principal needs `Create` permissions for the keyspace.

The following IAM policy is an example of this.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cassandra:Create",
            "Resource": [
                "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/`my_keyspace`/"
            ]
        }
    ]
}
```

To create a UDT in a multi-Region keyspace, in addition to `Create` permissions the principal also needs
permissions for the action `CreateMultiRegionResource` for the specified keyspace.

The following IAM policy is an example of this.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action":  [ "cassandra:Create", "cassandra:CreateMultiRegionResource" ],
            "Resource": [
                "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/`my_keyspace`/"
            ]
        }
    ]
}
```

## Permissions to view a UDT

To view or list UDTs in a single-Region keyspace, the principal needs read permissions for the system keyspace. For
more information, see [system_schema_mcs](working-with-keyspaces.md#keyspace_system_schema_mcs "working-with-keyspaces.md#keyspace_system_schema_mcs").

The following IAM policy is an example of this.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":"cassandra:Select",
         "Resource":[
             "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
         ]
      }
   ]
}
```

To view or list UDTs for a multi-Region keyspace, the principal needs permissions
for the actions `SELECT` and `SelectMultiRegionResource` for
the system keyspace. For more information, see [system_multiregion_info](working-with-keyspaces.md#keyspace_system_multiregion_info "working-with-keyspaces.md#keyspace_system_multiregion_info").

The following IAM policy is an example of this.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action": ["cassandra:Select", "cassandra:SelectMultiRegionResource"],
         "Resource":[
             "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
         ]
      }
   ]
}
```

## Permissions to delete a UDT

To delete a UDT from a single-Region keyspace, the principal needs permissions for the `Drop` action for the specified keyspace.

The following IAM policy is an example of this.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cassandra:Drop",
            "Resource": [
                "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/`my_keyspace`/"
            ]
        }
    ]
}
```

To delete a UDT from a multi-Region keyspace, the principal needs permissions for the `Drop` action
and for the `DropMultiRegionResource` action for the specified keyspace.

The following IAM policy is an example of this.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action":  [ "cassandra:Drop", "cassandra:DropMultiRegionResource" ],
            "Resource": [
                "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/`my_keyspace`/"
            ]
        }
    ]
}
```
