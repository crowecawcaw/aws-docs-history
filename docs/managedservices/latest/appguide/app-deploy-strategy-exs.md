# Application maintenance

Once infrastructure is deployed, updating it in a consistent way across all your AMS
environments, from QA to staging to production, is the challenge.

This section provides an overview of the AMS workload ingestion process and some
examples of different methods you can use to keep your cloud infrastructure layer up to
date.

## Application maintenance strategies

How you deploy your applications impacts how you maintain them. This section
provides some strategies for application maintenance.

Environment updates can involve any of these changes:

- Security updates
- New versions of your applications
- Application configuration changes
- Updates to dependencies

###### Note

For any application deployment, no matter the method, always file a service
request beforehand to let AMS know that you are going to deploy an application.

| Immutable vs Mutable Application Installation Examples | Compute Instance Mutability | App Install Method             | AMI |
| ------------------------------------------------------ | --------------------------- | ------------------------------ | --- |
| Mutable                                                | With CodeDeploy             | AMS-provided                   |
| Manually                                               |
| With a Chef or Puppet, Pull-Based                      |
| With Ansible or Salt, Push-Based                       |
| Immutable                                              | With a Golden AMI           | Custom (based on AMS-provided) |
