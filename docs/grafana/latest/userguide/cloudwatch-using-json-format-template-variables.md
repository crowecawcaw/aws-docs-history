# Using JSON

format template variables

Some queries accept filters in JSON format and Grafana supports the
conversion of template variables to JSON.

If `env = 'production', 'staging'`, the following query will
return ARNs of EC2 instances for which the `Environment` tag is
`production` or `staging`.

```

resource_arns(us-east-1, ec2:instance, {"Environment":${env:json}})

```
