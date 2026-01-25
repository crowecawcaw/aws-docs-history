# Deleting an ElastiCache parameter group

You can delete a custom parameter group using the ElastiCache console, the AWS CLI, or the
ElastiCache API.

You cannot delete a parameter group if it is associated with any clusters. Nor can you
delete any of the default parameter groups.

## Deleting a parameter group

(Console)

The following procedure shows how to delete a parameter group using the ElastiCache
console.

###### To delete a parameter group using the ElastiCache console

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. To see a list of all available parameter groups, in the left hand
   navigation pane choose **Parameter Groups**.
3. Choose the parameter groups you want to delete by choosing the box to the
   left of the parameter group's name.

The **Delete** button will become active. 4. Choose **Delete**.

The **Delete Parameter Groups** confirmation screen will
appear. 5. To delete the parameter groups, on the **Delete Parameter
Groups** confirmation screen, choose
**Delete**.

To keep the parameter groups, choose **Cancel**.

## Deleting a parameter group

(AWS CLI)

To delete a parameter group using the AWS CLI, use the command
`delete-cache-parameter-group`. For the parameter group to delete,
the parameter group specified by `--cache-parameter-group-name` cannot
have any clusters associated with it, nor can it be a default parameter
group.

The following sample code deletes the _myMem14_ parameter
group.

For Linux, macOS, or Unix:

```
aws elasticache delete-cache-parameter-group \
    --cache-parameter-group-name `myRed28`
```

For Windows:

```
aws elasticache delete-cache-parameter-group ^
    --cache-parameter-group-name `myRed28`
```

For more information, see [`delete-cache-parameter-group`](../../../cli/latest/reference/elasticache/delete-cache-parameter-group.md "../../../cli/latest/reference/elasticache/delete-cache-parameter-group.md").

## Deleting a parameter group

(ElastiCache API)

To delete a parameter group using the ElastiCache API, use the
`DeleteCacheParameterGroup` action. For the parameter group to
delete, the parameter group specified by `CacheParameterGroupName` cannot
have any clusters associated with it, nor can it be a default parameter
group.

With Memcached, the following sample code deletes the _myMem14_ parameter
group.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DeleteCacheParameterGroup
   &CacheParameterGroupName=`myMem14`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &Version=2015-02-02
   &X-Amz-Credential=<credential>
```

The following sample code deletes the _myRed28_ parameter
group.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DeleteCacheParameterGroup
   &CacheParameterGroupName=`myRed28`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &Version=2015-02-02
   &X-Amz-Credential=<credential>
```

For more information, see [`DeleteCacheParameterGroup`](../APIReference/API_DeleteCacheParameterGroup.md "../APIReference/API_DeleteCacheParameterGroup.md").
