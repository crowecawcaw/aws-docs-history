

# Deleting an RDS Proxy
<a name="rds-proxy-deleting"></a>

 You can delete a proxy when you no longer need it. Or, you might delete a proxy if you take the DB instance or cluster associated with it out of service. 

## AWS Management Console
<a name="rds-proxy-deleting.console"></a>

**To delete a proxy**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Proxies**. 

1.  Choose the proxy to delete from the list. 

1.  Choose **Delete Proxy**. 

## AWS CLI
<a name="rds-proxy-deleting.CLI"></a>

 To delete a DB proxy, use the AWS CLI command [delete-db-proxy](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-proxy.html). To remove related associations, also use the [deregister-db-proxy-targets](https://docs.aws.amazon.com/cli/latest/reference/rds/deregister-db-proxy-targets.html) command. 

```
aws rds delete-db-proxy --name {{proxy_name}}
```

```
aws rds deregister-db-proxy-targets
    --db-proxy-name {{proxy_name}}
    [--target-group-name {{target_group_name}}]
    [--target-ids {{comma_separated_list}}]       # or
    [--db-instance-identifiers {{instance_id}}]       # or
    [--db-cluster-identifiers {{cluster_id}}]
```

## RDS API
<a name="rds-proxy-deleting.API"></a>

 To delete a DB proxy, call the Amazon RDS API function [DeleteDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBProxy.html). To deregister targets from the proxy, you can call [DeregisterDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeregisterDBProxyTargets.html). 