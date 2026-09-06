

# Key considerations for migrating to a new MWAA environment
<a name="key-considerations"></a>

 Learn more about key considerations, such as authentication and the Amazon MWAA execution role, as you plan to migrate your Apache Airflow workloads to Amazon MWAA. 

**Topics**
+ [Authentication](#authentication)
+ [Execution role](#execution-role)

## Authentication
<a name="authentication"></a>

 Amazon MWAA uses AWS Identity and Access Management (IAM) to control access to the Apache Airflow UI. You must create and manage IAM policies that grant your Apache Airflow users permission to access the webserver and manage DAGs. You can manage both authentication and authorization for Apache Airflow's [default roles](https://airflow.apache.org/docs/apache-airflow/stable/security/access-control.html#default-roles) using IAM across different accounts. 

 You can further manage and restrict Apache Airflow users to access only a subset of your workflow DAGs by creating custom Airflow roles and mapping them to your IAM principals. For more information and a step-by-step tutorial, refer to [Tutorial: Restricting an Amazon MWAA user's access to a subset of DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/limit-access-to-dags.html). 

 You can also configure federated identities to access Amazon MWAA. For more information refer to the following. 
+  **Amazon MWAA environment with public access** — [Using Okta as an identity provider with Amazon MWAA](https://aws.amazon.com/blogs/compute/using-okta-as-an-identity-provider-with-amazon-mwaa/) on the *AWS Compute Blog*. 
+  **Amazon MWAA environment with private access** — [Accessing a private Amazon MWAA environment using federated identities](https://d1.awsstatic.com/whitepapers/accessing-a-private-amazon-mwaa-environment-using-federated-identities.pdf). 

## Execution role
<a name="execution-role"></a>

 Amazon MWAA uses an execution role that grants permissions to your environment to access other AWS services. You can provide your workflow with access to AWS services by adding the relevant permissions to the role. If you choose the default option to create a new execution role when you first create the environment, Amazon MWAA attaches the minimal permissions needed to the role, except in the case of CloudWatch Logs for which Amazon MWAA adds all log groups automatically. 

 Once the execution role is created, Amazon MWAA cannot manage its permission policies on your behalf. To update the execution role, you must edit the policy to add and remove permissions as needed. For example, you can [integrate your Amazon MWAA environment with AWS Secrets Manager](https://docs.aws.amazon.com/mwaa/latest/userguide/connections-secrets-manager.html) as a backend to securely store secrets and connection strings to use in your Apache Airflow workflows. To do so, attach the following permission policy to your environment's execution role. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetResourcePolicy",
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret",
                "secretsmanager:ListSecretVersionIds"
            ],
            "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:*"
        },
        {
            "Effect": "Allow",
            "Action": "secretsmanager:ListSecrets",
            "Resource": "*"
        }
    ]
}
```

------

 Integrating with other AWS services follows a similar pattern: you add the relevant permission policy to your Amazon MWAA execution role, granting permission to Amazon MWAA to access the service. For more information about managing the Amazon MWAA execution role, and to see additional examples, visit [Amazon MWAA execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html) in the *Amazon MWAA User Guide*. 