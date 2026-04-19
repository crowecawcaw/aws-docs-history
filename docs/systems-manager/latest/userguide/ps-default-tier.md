# Specifying a default parameter tier

When creating or updating a parameter using the
`PutParameter` operation, you can specify the parameter
tier. Here is an AWS CLI example.

Linux & macOS

```
aws ssm put-parameter \
    --name "default-ami" \
    --type "String" \
    --value "t2.micro" \
    --tier "Standard"
```

Windows

```
aws ssm put-parameter ^
    --name "default-ami" ^
    --type "String" ^
    --value "t2.micro" ^
    --tier "Standard"
```

When you specify a tier in a create or update request, Parameter Store uses that tier. If no tier is specified, the default tier setting determines which tier is used.

By default, Parameter Store uses the standard parameter tier. If you enable the advanced parameter tier, you can set one of the following as the default:

- **Advanced**: All parameters are created as advanced.
- **Intelligent-Tiering**: Parameter Store evaluates each request and selects the appropriate tier.

With Intelligent-Tiering, Parameter Store creates a parameter in the standard tier unless the request includes options that require the advanced tier. If advanced features are requested, the parameter is created as advanced.

## About the default parameter tier

Be default, when you create a new parameter, Parameter Store assigns it to the Standard tier. Standard parameters are available at no cost, but there are size and feature restrictions, as described in [Standard and advanced parameters](parameter-store-advanced-parameters.md#parameter-store-advanced-parameters-table "parameter-store-advanced-parameters.md#parameter-store-advanced-parameters-table"). If your use cases don't support standard parameters, you can set the Advanced tier as the default. The Advanced tier offers higher limits and extra features, at a cost. For more information, see [AWS Systems Manager Pricing for
Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store").

To maximize efficiency and reduce costs, you can set Intelligent-Tiering as the default. This feature determines whether to use the
Standard or Advanced tier based on the content
of the request. For example, if you run a command to create a parameter
that meets all of the criteria for a standard parameter, Intelligent-Tiering creates the parameter in the Standard tier. If you run a command
to create a parameter where one or more criteria don't meet the Standard-tier requirements, Intelligent-Tiering creates the parameter in the Advanced tier.

Intelligent-Tiering offers the following benefits:

**Cost control** – Intelligent-Tiering helps
control your parameter-related costs by always creating standard parameters
unless an advanced parameter is absolutely necessary.

**Automatic upgrade to the advanced-parameter
tier** – When you make a change to your code that requires
upgrading a standard parameter to an advanced parameter, Intelligent-Tiering
handles the conversion for you. You don't need to change your code to handle the
upgrade.

Here are some examples of automatic upgrades:

- Your AWS CloudFormation templates provision numerous parameters when they're
  run. When this process causes you to reach the 10,000 parameter quota in
  the standard-parameter tier, Intelligent-Tiering automatically upgrades
  you to the advanced-parameter tier, and your CloudFormation processes aren't
  interrupted.
- You store a certificate value in a parameter, rotate the certificate
  value regularly, and the content is less than the 4 KB quota of the
  standard-parameter tier. If a replacement certificate value exceeds 4
  KB, Intelligent-Tiering automatically upgrades the parameter to the
  advanced-parameter tier.
- You want to associate numerous existing standard parameters to a
  parameter policy, which requires the advanced-parameter tier. Instead of
  including the `--tier Advanced` option in calls to update parameters, Intelligent-Tiering automatically
  upgrades parameters to the advanced tier.

Intelligent-Tiering upgrades parameters from standard to advanced
whenever advanced-parameter criteria are introduced.

###### Note

You can change Parameter Store default tier settings at any time.
