# Configurable values

You can set the value of the following broker configuration options by modifying the broker configuration file in the AWS Management Console.

In addition to the values described in the following table, Amazon MQ supports additional broker configuration options related to authentication and authorization as well as resource limits. For more information about these configuration options, see

- [OAuth 2.0 configuration](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md")
- [LDAP configuration](ldap-for-amq-for-rabbitmq.md "ldap-for-amq-for-rabbitmq.md")
- [ARN support](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md")
- [Resource limits](rabbitmq-resource-limits-configuration.md "rabbitmq-resource-limits-configuration.md")

| Configuration                                                     | Default Value                                                                                            | Recommended Value       | Values                                                                              | Applicable Versions | Description                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| consumer_timeout                                                  | 1800000 ms (30 minutes)                                                                                  | 1800000 ms (30 minutes) | 0 to 2,147,483,647 ms. Amazon MQ also supports the value 0, which means "infinite". | All versions        | A timeout on consumer delivery acknowledgement to detect when consumers do not ack deliveries.                                                                    |
| heartbeat                                                         | 60 seconds                                                                                               | 60 seconds              | 60 to 3600 seconds                                                                  | All versions        | Defines the time before a connection is considered unavailable by RabbitMQ.                                                                                       |
| management.restrictions.operator_policy_changes.disabled          | true                                                                                                     | true                    | true, false                                                                         | 3.11 and above      | Turns off making changes to the operator policies. If you make this change, you are highly encouraged to include the HA properties in your own operator policies. |
| quorum_queue.property_equivalence.relaxed_checks_on_redeclaration | true                                                                                                     | true                    | true, false                                                                         | 3.13 and above      | When set to TRUE, your application avoids a channel exception when redeclaring a quorum queue.                                                                    |
| secure.management.http.headers.enabled                            | true for brokers on 3.10 created on or after July 9, 2024. false for brokers created before July 9, 2024 | true                    | true or false                                                                       | 3.10 and above      | Turns on unmodifiable HTTP security headers.                                                                                                                      |

## Configuring consumer delivery acknowledgement

You can configure consumer_timeout to detect when consumers do not ack deliveries. If the consumer does not send an acknowledgment within the timeout value, the channel will be closed. For example, if you are using the default value 1800000 milliseconds, if the consumer does not send a delivery acknowledgement within 1800000 milliseconds, the channel will be closed. Amazon MQ also supports the value 0, which means "infinite".

## Configuring heartbeat

You can configure a heartbeat timeout to find out when connections are disrupted or have failed. The heartbeat value defines the time limit before a connection is considered down.

## Configuring operator policies

The default operator policy on each virtual host has the following recommended HA properties:

```
{
"name": "default_operator_policy_AWS_managed",
"pattern": ".*",
"apply-to": "all",
"priority": 0,
"definition": {
"ha-mode": "all",
"ha-sync-mode": "automatic"
}
}
```

Changes to the operator policies via the AWS Management Console or Management API are not available by default. You can enable changes by adding the following line to the broker configuration:

```
management.restrictions.operator_policy_changes.disabled=false
```

If you make this change, you are highly encouraged to include the HA properties in your own operator policies.

## Configuring relaxed checks on queue declaration

If you have migrated your classic queues to quorum queues but not updated your client code, you can avoid a channel exception when redeclaring a quorum queue by configuring quorum_queue.property_equivalence.relaxed_checks_on_redeclaration set to true.

## Configuring HTTP security headers

The secure.management.http.headers.enabled configuration enables the following HTTP security headers:

- [X-Content-Type-Options: nosniff](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options"): prevents browsers from performing content sniffing, algorithms that are used to deduce the file format of websites.
- [X-Frame-Options: DENY](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options"): prevents others from embedding the management plugin into a frame on their own website to deceive others
- [Strict-Transport-Security: max-age=47304000; includeSubDomains](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security"): enforces browsers to use HTTPS when making subsequent connections to the website and its subdomains for a long period of time (1.5 years).

Amazon MQ for RabbitMQ brokers created on versions 3.10 and above will have secure.management.http.headers.enabled set to true by default. You can turn on these HTTP security headers by setting secure.management.http.headers.enabled to true. If you wish to opt out of these HTTP security headers, set secure.management.http.headers.enabled to false.
