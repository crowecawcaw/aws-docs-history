# Elastic Beanstalk deploy action reference

Elastic Beanstalk is a platform within AWS that is used for deploying and scaling web applications.
You use an Elastic Beanstalk action to deploy application code to your deployment environment.

###### Topics

- [Action type](#action-reference-Beanstalk-type "#action-reference-Beanstalk-type")
- [Configuration parameters](#action-reference-Beanstalk-config "#action-reference-Beanstalk-config")
- [Input artifacts](#action-reference-Beanstalk-input "#action-reference-Beanstalk-input")
- [Output artifacts](#action-reference-Beanstalk-output "#action-reference-Beanstalk-output")
- [Service role permissions:
  ElasticBeanstalk deploy action](#edit-role-beanstalk "#edit-role-beanstalk")
- [Action declaration](#action-reference-Beanstalk-example "#action-reference-Beanstalk-example")
- [See also](#action-reference-Beanstalk-links "#action-reference-Beanstalk-links")

## Action type

- Category: `Deploy`
- Owner: `AWS`
- Provider: `ElasticBeanstalk`
- Version: `1`

## Configuration parameters

**ApplicationName**

Required: Yes

The name of the application that you created in Elastic Beanstalk.

**EnvironmentName**

Required: Yes

The name of the environment that you created in Elastic Beanstalk. An environment is a
collection of AWS resources running an application version. Each
environment runs only one application version at a time, however, you can
run the same application version or different application versions in many
environments simultaneously.

## Input artifacts

- **Number of artifacts:**
  `1`
- **Description:** The input artifact for the
  action.

## Output artifacts

- **Number of artifacts:**
  `0`
- **Description:** Output artifacts do not apply
  for this action type.

## Service role permissions:

`ElasticBeanstalk` deploy action

For Elastic Beanstalk, the following are the minimum permissions needed to create pipelines
with an `ElasticBeanstalk` deploy action.

```
{
    "Effect": "Allow",
    "Action": [
        "elasticbeanstalk:*",
        "ec2:*",
        "elasticloadbalancing:*",
        "autoscaling:*",
        "cloudwatch:*",
        "s3:*",
        "sns:*",
        "cloudformation:*",
        "rds:*",
        "sqs:*",
        "ecs:*"
    ],
    "Resource": "`resource_ARN`"
},
```

###### Note

You should replace wildcards in the resource policy with the resources for the
account you want to limit access to. For more information about creating a
policy that grants least-privilege access, see [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").

## Action declaration

YAML

```
Name: Deploy
Actions:
  - Name: Deploy
    ActionTypeId:
      Category: Deploy
      Owner: AWS
      Provider: ElasticBeanstalk
      Version: '1'
    RunOrder: 1
    Configuration:
      ApplicationName: `my-application`
      EnvironmentName: `my-environment`
    OutputArtifacts: []
    InputArtifacts:
      - Name: SourceArtifact
    Region: us-west-2
    Namespace: DeployVariables

```

JSON

```
{
    "Name": "Deploy",
    "Actions": [
        {
            "Name": "Deploy",
            "ActionTypeId": {
                "Category": "Deploy",
                "Owner": "AWS",
                "Provider": "ElasticBeanstalk",
                "Version": "1"
            },
            "RunOrder": 1,
            "Configuration": {
                "ApplicationName": "`my-application`",
                "EnvironmentName": "`my-environment`"
            },
            "OutputArtifacts": [],
            "InputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "Region": "us-west-2",
            "Namespace": "DeployVariables"
        }
    ]
},
```

## See also

The following related resources can help you as you work with this action.

- [Deploying a Flask
  application to Elastic Beanstalk](../../../elasticbeanstalk/latest/dg/create-deploy-python-flask.md "../../../elasticbeanstalk/latest/dg/create-deploy-python-flask.md") – This tutorial walks you through the
  creation of your application and environment resources in Elastic Beanstalk using a sample
  Flask application. You can then build your pipeline with an Elastic Beanstalk deployment
  action that deploys your application from your source repository to your Elastic Beanstalk
  environment.
