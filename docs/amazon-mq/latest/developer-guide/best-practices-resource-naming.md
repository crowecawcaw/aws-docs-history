

# Best practices for resource naming in Amazon MQ for RabbitMQ
<a name="best-practices-resource-naming"></a>

 Although RabbitMQ permits arbitrary UTF-8 characters in vhost names, queue names, exchange names, and policy names, Amazon MQ for RabbitMQ recommends using a standard character set. 

## Naming conventions
<a name="naming-conventions"></a>

 We recommend following supported characters for vhost names, queue names, exchange names, and policy names: 
+ Letters (A–Z, a–z)
+ Numbers (0–9)
+ Hyphens (`-`), underscores (`_`), periods (`.`), colons (`:`), and forward slashes (`/`)

**Important**  
Using other special characters in vhost names, queue names, exchange names, or policy names may prevent Amazon MQ from performing certain broker maintenance operations.