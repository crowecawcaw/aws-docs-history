

# Listing DB parameter groups in Amazon RDS
<a name="USER_WorkingWithParamGroups.Listing"></a>

You can list the DB parameter groups you've created for your AWS account.

**Note**  
Default parameter groups are automatically created from a default parameter template when you create a DB instance for a particular DB engine and version. These default parameter groups contain preferred parameter settings and can't be modified. When you create a custom parameter group, you can modify parameter settings. 

## Console
<a name="USER_WorkingWithParamGroups.Listing.CON"></a>

**To list all DB parameter groups for an AWS account**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Parameter groups**.

   The DB parameter groups appear in a list.

## AWS CLI
<a name="USER_WorkingWithParamGroups.Listing.CLI"></a>

To list all DB parameter groups for an AWS account, use the AWS CLI [`describe-db-parameter-groups`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameter-groups.html) command.

**Example**  
The following example lists all available DB parameter groups for an AWS account.  

```
aws rds describe-db-parameter-groups
```
The command returns a response like the following:  

```
DBPARAMETERGROUP  default.mysql8.0     mysql8.0  Default parameter group for MySQL8.0
DBPARAMETERGROUP  mydbparametergroup   mysql8.0  My new parameter group
```
The following example describes the *mydbparamgroup1* parameter group.  
For Linux, macOS, or Unix:  

```
aws rds describe-db-parameter-groups \
    --db-parameter-group-name {{mydbparamgroup1}}
```
For Windows:  

```
aws rds describe-db-parameter-groups ^
    --db-parameter-group-name {{mydbparamgroup1}}
```
The command returns a response like the following:  

```
DBPARAMETERGROUP  mydbparametergroup1  mysql8.0  My new parameter group
```

## RDS API
<a name="USER_WorkingWithParamGroups.Listing.API"></a>

To list all DB parameter groups for an AWS account, use the RDS API [`DescribeDBParameterGroups`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameterGroups.html) operation.