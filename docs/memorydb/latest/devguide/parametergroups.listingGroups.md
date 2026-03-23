# Listing parameter groups by name

You can list the parameter groups using the MemoryDB console, the AWS CLI, or the MemoryDB API.

## Listing parameter groups by name (Console)

The following procedure shows how to view a list of the parameter groups using the MemoryDB console.

###### To list parameter groups using the MemoryDB console

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. To see a list of all available parameter groups,
   in the left hand navigation pane choose **Parameter Groups**.

## Listing parameter groups by name (AWS CLI)

To generate a list of parameter groups using the AWS CLI,
use the command `describe-parameter-groups`.
If you provide a parameter group's name, only that parameter group will be listed.
If you do not provide a parameter group's name, up to `--max-results` parameter groups
will be listed. In either case, the parameter group's name, family, and description are listed.

###### Example

The following sample code lists the parameter group _myRedis6x_.

For Linux, macOS, or Unix:

```
aws memorydb describe-parameter-groups \
    --parameter-group-name `myRedis6x`
```

For Windows:

```
aws memorydb describe-parameter-groups ^
    --parameter-group-name `myRedis6x`
```

The output of this command will look something like this,
listing the name, family, and description for the parameter group.

```
{
    "ParameterGroups": [
	    {
	        "Name": "myRedis6x",
	        "Family": "memorydb_redis6",
	        "Description": "My first parameter group",
                "ARN": "arn:aws:memorydb:us-east-1:012345678912:parametergroup/myredis6x"
	    }
    ]
}
```

###### Example

The following sample code lists the parameter group _myRedis6x_ for parameter groups running on Valkey, or on Redis OSS engine version 5.0.6 onwards.

For Linux, macOS, or Unix:

```
aws memorydb describe-parameter-groups \
    --parameter-group-name `myRedis6x`
```

For Windows:

```
aws memorydb describe-parameter-groups ^
    --parameter-group-name `myRedis6x`
```

The output of this command will look something like this,
listing the name, family and description for the parameter group.

```
{
    "ParameterGroups": [
	    {
	        "Name": "myRedis6x",
	        "Family": "memorydb_redis6",
	        "Description": "My first parameter group",
                "ARN": "arn:aws:memorydb:us-east-1:012345678912:parametergroup/myredis6x"
	    }
    ]
}
```

###### Example

The following sample code lists up to 20 parameter groups.

```
aws memorydb describe-parameter-groups --max-results `20`
```

The JSON output of this command will look something like this,
listing the name, family and description for each parameter group.

```
{
    "ParameterGroups": [
        {
            "ParameterGroupName": "default.memorydb-redis6",
            "Family": "memorydb_redis6",
            "Description": "Default parameter group for memorydb_redis6",
            "ARN": "arn:aws:memorydb:us-east-1:012345678912:parametergroup/default.memorydb-redis6"
        },
        ...
    ]
}
```

For more information, see [`describe-parameter-groups`](../../../cli/latest/reference/memorydb/describe-parameter-groups.md "../../../cli/latest/reference/memorydb/describe-parameter-groups.md").

## Listing parameter groups by name (MemoryDB API)

To generate a list of parameter groups using the MemoryDB API,
use the `DescribeParameterGroups` action.
If you provide a parameter group's name, only that parameter group will be listed.
If you do not provide a parameter group's name, up to `MaxResults` parameter groups
will be listed. In either case, the parameter group's name, family, and description are listed.

###### Example

The following sample code lists up to 20 parameter groups.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DescribeParameterGroups
   &MaxResults=`20`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20210802T192317Z
   &Version=2021-01-01
   &X-Amz-Credential=<credential>
```

The response from this action will look something like this,
listing the name, family and description in the case of memorydb_redis6, for each parameter group.

```
<DescribeParameterGroupsResponse xmlns="http://memory-db.us-east-1.amazonaws.com/doc/2021-01-01/">
  <DescribeParameterGroupsResult>
    <ParameterGroups>
      <ParameterGroup>
        <Name>myRedis6x</Name>
        <Family>memorydb_redis6</Family>
        <Description>My custom Redis OSS 6 parameter group</Description>
        <ARN>arn:aws:memorydb:us-east-1:012345678912:parametergroup/myredis6x</ARN>
      </ParameterGroup>
       <ParameterGroup>
        <Name>default.memorydb-redis6</Name>
        <Family>memorydb_redis6</Family>
        <Description>Default parameter group for memorydb_redis6</Description>
        <ARN>arn:aws:memorydb:us-east-1:012345678912:parametergroup/default.memorydb-redis6</ARN>
      </ParameterGroup>
    </ParameterGroups>
  </DescribeParameterGroupsResult>
  <ResponseMetadata>
    <RequestId>3540cc3d-af48-11e0-97f9-279771c4477e</RequestId>
  </ResponseMetadata>
</DescribeParameterGroupsResponse>
```

###### Example

The following sample code lists the parameter group _myRedis6x_.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DescribeParameterGroups
   &ParameterGroupName=`myRedis6x`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20210802T192317Z
   &Version=2021-01-01
   &X-Amz-Credential=<credential>
```

The response from this action will look something like this,
listing the name, family, and description.

```
<DescribeParameterGroupsResponse xmlns="http://memory-db.us-east-1.amazonaws.com/doc/2021-01-01/">
  <DescribeParameterGroupsResult>
    <ParameterGroups>
      <ParameterGroup>
        <Name>myRedis6x</Name>
        <Family>memorydb_redis6</Family>
        <Description>My custom Redis OSS 6 parameter group</Description>
        <ARN>arn:aws:memorydb:us-east-1:012345678912:parametergroup/myredis6x</ARN>
      </ParameterGroup>
    </ParameterGroups>
  </DescribeParameterGroupsResult>
  <ResponseMetadata>
    <RequestId>3540cc3d-af48-11e0-97f9-279771c4477e</RequestId>
  </ResponseMetadata>
</DescribeParameterGroupsResponse>
```

For more information, see [`DescribeParameterGroups`](../APIReference/API_DescribeParameterGroups.md "../APIReference/API_DescribeParameterGroups.md").
