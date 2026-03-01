# CloudWatch pipelines configuration for Palo Alto Networks Next-Generation Firewalls

Collects log data from Palo Alto Next-Generation Firewall using basic
authentication.

Configure the Palo Alto NGFW source with the following parameters:

```
source:
  palo_alto_ngfw:
    hostname: "<example-host-name>"
    authentication:
      basic:
        username: "${{aws_secrets:<secret-name>:username}}"
        password: "${{aws_secrets:<secret-name>:password}}"
```

###### Parameters

`hostname` (required)

The Palo Alto NGFW hostname for your firewall.

`authentication.basic.username` (required)

Basic authentication username for Palo Alto NGFW API
authentication.

`authentication.basic.password` (required)

Basic authentication password for Palo Alto NGFW API
authentication.
