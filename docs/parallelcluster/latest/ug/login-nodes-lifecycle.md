# Login Nodes lifecycle

Currently, there is no dedicated command to stop and start the login nodes in a pool. In order to stop the login nodes in a pool the cluster administrator has to update the cluster
configuration specifying zero on the count of login nodes (`Count: 0` ) and then run an [pcluster.update-cluster-v3](pcluster.md "pcluster.md")
command.

###### Note

Logged in users are notified about the termination of the specific instance and about the related gracetime
period. During the gracetime period no new connections will be allowed except for the ones from the [cluster default user](../../../AWSEC2/latest/UserGuide/managing-users.md "../../../AWSEC2/latest/UserGuide/managing-users.md"). The message
shown is customizable by the cluster administrator from the head node or from a login node editing the file 
`/opt/parallelcluster/shared_login_nodes/loginmgtd_config.json`. This termination message is
not visible when you are connected using the [AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") Session Manager.

In order to start the login nodes pool the cluster administrator has to restore the previous `Count` value in the cluster configuration and then run an [update-cluster](pcluster.md "pcluster.md") command.
