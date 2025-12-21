# Creating a parameter group

You need to create a new parameter group if there is one or more parameter values that you want
changed from the default values.
You can create a parameter group using the MemoryDB console, the AWS CLI, or the MemoryDB API.

## Creating a parameter group (Console)

The following procedure shows how to create a parameter group using the MemoryDB console.

###### To create a parameter group using the MemoryDB console

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. To see a list of all available parameter groups,
   in the left hand navigation pane choose **Parameter Groups**.
3. To create a parameter group, choose **Create parameter group**.

The **Create parameter group** page appears. 4. In the **Name** box, type in a unique name for this parameter group.

When creating a cluster
or modifying a cluster's parameter group, you will choose the parameter group by its name.
Therefore, we recommend that the name be informative and somehow identify the parameter group's family.

Parameter group naming constraints are as follows:

    * Must begin with an ASCII letter.
    * Can only contain ASCII letters, digits, and hyphens.
    * Must be 1–255 characters long.
    * Can't contain two consecutive hyphens.
    * Can't end with a hyphen.

5. In the **Description** box, type in a description for the parameter group.
6. In the engine version compatibility box, choose an engine version that this parameter group corresponds to.
7. In the **Tags**, optionally add tags to search and filter your parameter groups or track your AWS costs.
8. To create the parameter group, choose **Create**.

To terminate the process without creating the parameter group, choose **Cancel**. 9. When the parameter group is created, it will have the family's default values.
To change the default values you must modify the parameter group.
For more information, see [Modifying a parameter group](parametergroups.md "parametergroups.md").

## Creating a parameter group (AWS CLI)

To create a parameter group using the AWS CLI, use the command `create-parameter-group` with
these parameters.

- `--parameter-group-name` —
  The name of the parameter group.

Parameter group naming constraints are as follows:

    + Must begin with an ASCII letter.
    + Can only contain ASCII letters, digits, and hyphens.
    + Must be 1–255 characters long.
    + Can't contain two consecutive hyphens.
    + Can't end with a hyphen.

- `--family` —
  The engine and version family for the parameter group.
- `--description` —
  A user supplied description for the parameter group.

The following example creates a parameter group named _myRedis6x_ using the memorydb_redis6
family as the template.

For Linux, macOS, or Unix:

```
aws memorydb create-parameter-group \
    --parameter-group-name `myRedis6x`  \
    --family `memorydb_redis6` \
    --description `"My first parameter group"`
```

For Windows:

```
aws memorydb create-parameter-group ^
    --parameter-group-name `myRedis6x`  ^
    --family `memorydb_redis6` ^
    --description `"My first parameter group"`
```

The output from this command should look something like this.

```
{
    "ParameterGroup": {
        "Name": "myRedis6x",
        "Family": "memorydb_redis6",
        "Description": "My first parameter group",
        "ARN": "arn:aws:memorydb:us-east-1:012345678912:parametergroup/myredis6x"
    }
}
```

When the parameter group is created, it will have the family's default values.
To change the default values you must modify the parameter group.
For more information, see [Modifying a parameter group](parametergroups.md "parametergroups.md").

For more information, see [`create-parameter-group`](../../../cli/latest/reference/memorydb/create-parameter-group.md "../../../cli/latest/reference/memorydb/create-parameter-group.md").

## Creating a parameter group (MemoryDB API)

To create a parameter group using the MemoryDB API, use the `CreateParameterGroup` action with
these parameters.

- `ParameterGroupName` —
  The name of the parameter group.

Parameter group naming constraints are as follows:

    + Must begin with an ASCII letter.
    + Can only contain ASCII letters, digits, and hyphens.
    + Must be 1–255 characters long.
    + Can't contain two consecutive hyphens.
    + Can't end with a hyphen.

- `Family` —
  The engine and version family for the parameter group. For example,
  `memorydb_redis6`.
- `Description` —
  A user supplied description for the parameter group.

The following example creates a parameter group named _myRedis6x_ using the memorydb_redis6
family as the template.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=CreateParameterGroup
   &Family=`memorydb_redis6`
   &ParameterGroupName=`myRedis6x`
   &Description=`My%20first%20parameter%20group`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20210802T192317Z
   &Version=2021-01-01
   &X-Amz-Credential=<credential>
```

The response from this action should look something like this.

```
<CreateParameterGroupResponse xmlns="http://memory-db.us-east-1.amazonaws.com/doc/2021-01-01/">
  <CreateParameterGroupResult>
    <ParameterGroup>
      <Name>myRedis6x</Name>
      <Family>memorydb_redis6</Family>
      <Description>My first parameter group</Description>
      <ARN>arn:aws:memorydb:us-east-1:012345678912:parametergroup/myredis6x</ARN>
    </ParameterGroup>
  </CreateParameterGroupResult>
  <ResponseMetadata>
    <RequestId>d8465952-af48-11e0-8d36-859edca6f4b8</RequestId>
  </ResponseMetadata>
</CreateParameterGroupResponse>
```

When the parameter group is created, it will have the family's default values.
To change the default values you must modify the parameter group.
For more information, see [Modifying a parameter group](parametergroups.md "parametergroups.md").

For more information, see [`CreateParameterGroup`](../APIReference/API_CreateParameterGroup.md "../APIReference/API_CreateParameterGroup.md").
