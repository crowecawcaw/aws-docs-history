# Applying policies to Amazon MQ for RabbitMQ

You can apply custom policies and limits with Amazon MQ recommended default values. If you have deleted the
recommended default policies and limits, and want to re-create them, or you have created additional vhosts and want to apply
the default policies and limits to your new vhosts, you can use the following steps.

###### Important

On Amazon MQ for RabbitMQ engine versions 3.13 and below,
the current default operator policy is:

```
vhost name pattern apply-to definition priority/ default_operator_policy_AWS_managed .* classic_queues {"ha-mode":"all","ha-sync-mode":"automatic","queue-version":2} 0
```

On versions 4.0 and above, the default operator policy has changed to:

```
vhost name pattern apply-to definition priority/ default_operator_policy_AWS_managed .* classic_queues {"queue-version":2} 0
```

This change is required because classic queue mirroring and HA policy settings are not supported in RabbitMQ 4.

You cannot create a policy that applies to both classic mirrored queues and quorum queues.
If you want your policy to only apply to quorum queues, you must set `--apply-to` to `quorum_queues`.
If you are using classic mirrored queues and quorum queues,
you must create a separate policy with `--apply-to:classic_queues` as well as a quorum queues policy.

###### Important

To perform the following steps, you must have an Amazon MQ for RabbitMQ broker user with administrator
permissions. You can use the administrator user created when you first created the broker, or
another user that you might have created afterwards. The following table provides the
necessary administrator user tag and permissions as regular expression (regexp)
patterns.

| Tags            | Read regexp | Configure regexp | Write regexp |
| --------------- | ----------- | ---------------- | ------------ |
| `administrator` | `.*`        | `.*`             | `.*`         |

For more information about creating RabbitMQ users and managing user tags and permissions,
see [Amazon MQ for RabbitMQ broker users](rabbitmq-simple-auth-broker-users.md#rabbitmq-basic-elements-user "rabbitmq-simple-auth-broker-users.md#rabbitmq-basic-elements-user").

###### To apply default policies and virtual host limits using the RabbitMQ web

console

1.  Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2.  In the left navigation pane, choose **Brokers**.
3.  From the list of brokers, choose the name of the broker to which you want to apply the new policy.
4.  On the broker details page, in the **Connections** section, choose the
    **RabbitMQ web console** URL. The RabbitMQ web console opens in a new
    browser tab or window.
5.  Log in to the RabbitMQ web console with your broker administrator user name and
    password.
6.  In the RabbitMQ web console, at the top of the page, choose
    **Admin**.
7.  On the **Admin** page, in the right navigation pane, choose
    **Policies**.
8.  On the **Policies** page, you can see a list of the broker's current
    **User policies**. Below **User policies**, expand
    **Add / update a policy**.
9.  To create a new broker policy, under **Add / update a policy**, do
    the following:
    1. For **Virtual host**, choose the name of the vhost to which you want to attach the policies
       from the dropdown list. To choose the default vhost, choose **/**.

    ###### Note

    If you have not created additional vhosts, the **Virtual host** option is not shown in the RabbitMQ console, and the
    policies are applied only to the default vhost. 2. For **Name**, enter a name for your policy, for example,
    `policy-defaults`. 3. For **Pattern**, enter the regexp pattern
    `.*` so that the policy matches all queues on the
    broker. 4. For **Apply to**, choose **Exchanges and
    queues** from the dropdown list. 5. For **Priority**, enter an integer greater than all other policies applied to the vhost.
    You can apply exactly one set of policy definitions to RabbitMQ queues and exchanges at any given time.
    RabbitMQ chooses the matching policy with the highest priority value.
    For more information about policy priorities and how to combine
    policies, see [Policies](https://www.rabbitmq.com/parameters.html#policies "https://www.rabbitmq.com/parameters.html#policies") in the RabbitMQ Server Documentation. 6. For **Definition**, add the following key-value pairs:

        * `queue-mode`=`lazy`.
         Choose **String** from the dropdown list.
        * `overflow`=`reject-publish`. Choose
         **String** from the dropdown list.


        ###### Note

        Does not apply to single-instance brokers.
        * `max-length`=``number-of-messages``.
         Replace `number-of-messages` with the [Amazon MQ recommended value](rabbitmq-defaults.md#rabbitmq-defaults-values "rabbitmq-defaults.md#rabbitmq-defaults-values")
         according to the broker's instance size and deployment mode, for example,
         `8000000` for an `mq.m7g.large` cluster.
         Choose **Number** from the dropdown list.


        ###### Note

        Does not apply to single-instance brokers.

    7. Choose **Add / update policy**.

10. Confirm that the new policy appears in the list of **User
    policies**.

###### Note

For cluster brokers, Amazon MQ automatically applies the `ha-mode: all` and `ha-sync-mode: automatic`
policy definitions. 11. From the right navigation pane, choose **Limits**. 12. On the **Limits** page, you can see a list of the broker's current
**Virtual host limits**. Below **Virtual host limits**, expand
**Set / update a virtual host limit**. 13. To create a new vhost limit, under **Set / update a virtual host limit**, do
the following:

    1. For **Virtual host**, choose the name of the vhost to which you want to attach the policies
     from the dropdown list. To choose the default vhost, choose **/**.
    2. For **Limit**, choose **max-connections** from the
     dropdown options.
    3. For **Value**, enter the [Amazon MQ recommended value](rabbitmq-defaults.md#rabbitmq-defaults-values "rabbitmq-defaults.md#rabbitmq-defaults-values")
     according to the broker's instance size and deployment mode, for example,
     `15000` for an `mq.m5.large` cluster.
    4. Choose **Set / update limit**.
    5. Repeat the steps above, and for **Limit**, choose **max-queues** from
     the dropdown options.

14. Confirm that the new limits appear in the list of **Virtual
    host limits**.

###### To apply default policies and virtual host limits using the RabbitMQ management API

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. In the left navigation pane, choose **Brokers**.
3. From the list of brokers, choose the name of the broker to which you want to apply the new policy.
4. On the broker's page, in the **Connections** section, note the
   **RabbitMQ web console** URL. This is the broker endpoint that you use
   in an HTTP request.
5. Open a new terminal or command line window of your choice.
6. To create a new broker policy, enter the following `curl` command. This
   command assumes a queue on the default `/` vhost, which is encoded as
   `%2F`. To apply the policy to another vhost, replace `%2F` with the vhost's name.

###### Note

Replace `username` and `password`
with your administrator sign-in credentials. Replace `number-of-messages`
with the [Amazon MQ recommended value](rabbitmq-defaults.md#rabbitmq-defaults-values "rabbitmq-defaults.md#rabbitmq-defaults-values")
according to the broker's instance size and deployment mode. Replace `policy-name`
with a name for your policy. Replace `broker-endpoint` with the URL that you noted previously.

```
curl -i -u `username`:`password` -H "content-type:application/json" -XPUT \
-d '{"pattern":".*", "priority":1, "definition":{"queue-mode":lazy, "overflow":"reject-publish", "max-length":"`number-of-messages`"}}' \
`broker-endpoint`/api/policies/%2F/`policy-name`

```

7. To confirm that the new policy is added to your broker's user policies, enter the
   following `curl` command to list all broker policies.

```
curl -i -u `username`:`password` `broker-endpoint`/api/policies
```

8. To create a new `max-connections` virtual host limits, enter the following `curl` command. This
   command assumes a queue on the default `/` vhost, which is encoded as
   `%2F`. To apply the policy to another vhost, replace `%2F` with the vhost's name.

###### Note

Replace `username` and `password`
with your administrator sign-in credentials. Replace `max-connections`
with the [Amazon MQ recommended value](rabbitmq-defaults.md#rabbitmq-defaults-values "rabbitmq-defaults.md#rabbitmq-defaults-values")
according to the broker's instance size and deployment mode. Replace the
broker endpoint with the URL that you noted previously.

```
curl -i -u `username`:`password` -H "content-type:application/json" -XPUT \
-d '{"value":"`number-of-connections`"}' \
`broker-endpoint`/api/vhost-limits/%2F/max-connections

```

9. To create a new `max-queues` virtual host limit, repeat the previous step, but modify the curl command
   as shown in the following.

```
curl -i -u `username`:`password` -H "content-type:application/json" -XPUT \
-d '{"value":"`number-of-queues`"}' \
`broker-endpoint`/api/vhost-limits/%2F/max-queues

```

10. To confirm that the new limits are added to your broker's virtual host limits, enter the
    following `curl` command to list all broker virtual host limits.

```
curl -i -u `username`:`password` `broker-endpoint`/api/vhost-limits
```
