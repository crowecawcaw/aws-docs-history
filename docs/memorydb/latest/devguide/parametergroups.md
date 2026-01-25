# Listing a parameter group's values

You can list the parameters and their values
for a parameter group using the MemoryDB console, the AWS CLI, or the MemoryDB API.

## Listing a parameter group's values (Console)

The following procedure shows how to list the parameters and their values
for a parameter group using the MemoryDB console.

###### To list a parameter group's parameters and their values using the MemoryDB console

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. To see a list of all available parameter groups,
   in the left hand navigation pane choose **Parameter Groups**.
3. Choose the parameter group for which you want to list the parameters and values by
   choosing name (not the box next to it) of the parameter group's name.

The parameters and their values will be listed at the bottom of the screen. Due to the number of
parameters, you may have to scroll up and down to find the parameter you're interested in.

## Listing a parameter group's values (AWS CLI)

To list a parameter group's parameters and their values using the AWS CLI,
use the command `describe-parameters`.

The following sample code list all the parameters and their values
for the parameter group _myRedis6x_.

For Linux, macOS, or Unix:

```
aws memorydb describe-parameters \
    --parameter-group-name `myRedis6x`
```

For Windows:

```
aws memorydb describe-parameters ^
    --parameter-group-name `myRedis6x`
```

For more information, see
[`describe-parameters`](../../../cli/latest/reference/memorydb/describe-parameters.md "../../../cli/latest/reference/memorydb/describe-parameters.md").

## Listing a parameter group's values (MemoryDB API)

To list a parameter group's parameters and their values using the MemoryDB API,
use the `DescribeParameters` action.

For more information, see [`DescribeParameters`](../APIReference/API_DescribeParameters.md "../APIReference/API_DescribeParameters.md").
