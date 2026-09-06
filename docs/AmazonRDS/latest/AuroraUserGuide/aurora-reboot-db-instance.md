

# Rebooting a DB instance within an Aurora cluster
<a name="aurora-reboot-db-instance"></a>

 This procedure is the most important operation that you take when performing reboots with Aurora. Many of the maintenance procedures involve rebooting one or more Aurora DB instances in a particular order. 

## Console
<a name="USER_RebootInstance.Console"></a>

**To reboot a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Databases**, and then choose the DB instance that you want to reboot. 

1.  For **Actions**, choose **Reboot**. 

    The **Reboot DB Instance** page appears. 

1.  Choose **Reboot** to reboot your DB instance. 

    Or choose **Cancel**. 

## AWS CLI
<a name="USER_RebootInstance.CLI"></a>

 To reboot a DB instance by using the AWS CLI, call the [`reboot-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/reboot-db-instance.html) command. 

**Example**  
For Linux, macOS, or Unix:  

```
aws rds reboot-db-instance \
    --db-instance-identifier {{mydbinstance}}
```
For Windows:  

```
aws rds reboot-db-instance ^
    --db-instance-identifier {{mydbinstance}}
```

## RDS API
<a name="USER_RebootInstance.API"></a>

 To reboot a DB instance by using the Amazon RDS API, call the [`RebootDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBInstance.html) operation. 