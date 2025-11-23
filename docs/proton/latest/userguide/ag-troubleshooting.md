End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Troubleshooting AWS Proton

Learn to troubleshoot issues with AWS Proton.

###### Topics

- [Deployment errors that reference CloudFormation dynamic parameters](#cfn-dynamic-params "#cfn-dynamic-params")

## Deployment errors that reference CloudFormation dynamic parameters

If you see deployment errors that reference your [CloudFormation dynamic variables](../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md "../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md"), verify
that they are [Jinja escaped](https://jinja.palletsprojects.com/en/2.11.x/templates/#escaping "https://jinja.palletsprojects.com/en/2.11.x/templates/#escaping"). These errors can be caused by Jinja misinterpretation of your dynamic variables. The CloudFormation dynamic parameter
syntax is very similar the Jinja syntax you use with your AWS Proton parameters.

Example CloudFormation dynamic variable syntax:

`'{{resolve:secretsmanager:MySecret:SecretString:password:EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE}}'`.

Example AWS Proton parameter Jinja syntax:

`'{{ service_instance.environment.outputs.env-outputs }}'`.

To avoid these misinterpretation errors, Jinja escape your CloudFormation dynamic parameters as shown in the following examples.

This example is from the CloudFormation User Guide. The AWS Secrets Manager secret-name and json-key segments can be used to retrieve the sign-in credentials stored in the secret.

```
MyRDSInstance:
  Type: AWS::RDS::DBInstance
  Properties:
    DBName: 'MyRDSInstance'
      AllocatedStorage: '20'
      DBInstanceClass: db.t2.micro
      Engine: mysql
      MasterUsername: '{{resolve:secretsmanager:MyRDSSecret:SecretString:username}}'
      MasterUserPassword: '{{resolve:secretsmanager:MyRDSSecret:SecretString:password}}'
```

To escape the CloudFormation dynamic parameters you can use two different methods:

- Enclose a block between `{% raw %} and {% endraw %}`:

```
'{% raw %}'
MyRDSInstance:
  Type: AWS::RDS::DBInstance
  Properties:
    DBName: 'MyRDSInstance'
      AllocatedStorage: '20'
      DBInstanceClass: db.t2.micro
      Engine: mysql
      MasterUsername: '{{resolve:secretsmanager:MyRDSSecret:SecretString:username}}'
      MasterUserPassword: '{{resolve:secretsmanager:MyRDSSecret:SecretString:password}}'
'{% endraw %}'
```

- Enclose a parameter between `"{{ }}"`:

```
MyRDSInstance:
  Type: AWS::RDS::DBInstance
  Properties:
    DBName: 'MyRDSInstance'
      AllocatedStorage: '20'
      DBInstanceClass: db.t2.micro
      Engine: mysql
      MasterUsername: "{{ '{{resolve:secretsmanager:MyRDSSecret:SecretString:username}}' }}"
      MasterUserPassword: "{{ '{{resolve:secretsmanager:MyRDSSecret:SecretString:password}}' }}"

```

For information, see [Jinja escaping](https://jinja.palletsprojects.com/en/2.11.x/templates/#escaping "https://jinja.palletsprojects.com/en/2.11.x/templates/#escaping").
