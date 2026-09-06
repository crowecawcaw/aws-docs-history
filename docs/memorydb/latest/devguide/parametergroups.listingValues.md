

# Listing a parameter group's values
<a name="parametergroups.listingValues"></a>

You can list the parameters and their values for a parameter group using the MemoryDB console, the AWS CLI, or the MemoryDB API.

## Listing a parameter group's values (Console)
<a name="parametergroups.listingValuesclusters.viewdetails"></a>

The following procedure shows how to list the parameters and their values for a parameter group using the MemoryDB console.

**To list a parameter group's parameters and their values using the MemoryDB console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. To see a list of all available parameter groups, in the left hand navigation pane choose **Parameter Groups**.

1. Choose the parameter group for which you want to list the parameters and values by choosing name (not the box next to it) of the parameter group's name.

   The parameters and their values will be listed at the bottom of the screen. Due to the number of parameters, you may have to scroll up and down to find the parameter you're interested in.

## Listing a parameter group's values (AWS CLI)
<a name="parametergroups.listingValues.cli"></a>

To list a parameter group's parameters and their values using the AWS CLI, use the command `describe-parameters`.

**Example**  
The following sample code list all the parameters and their values for the parameter group *myRedis6x*.  
For Linux, macOS, or Unix:  

```
aws memorydb describe-parameters \
    --parameter-group-name {{myRedis6x}}
```
For Windows:  

```
aws memorydb describe-parameters ^
    --parameter-group-name {{myRedis6x}}
```

For more information, see [`describe-parameters`](https://docs.aws.amazon.com/cli/latest/reference/memorydb/describe-parameters.html).

## Listing a parameter group's values (MemoryDB API)
<a name="parametergroups.listingValues.api"></a>

To list a parameter group's parameters and their values using the MemoryDB API, use the `DescribeParameters` action.

For more information, see [`DescribeParameters`](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameters.html).