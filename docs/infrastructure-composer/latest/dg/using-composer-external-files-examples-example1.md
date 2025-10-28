# Reference an OpenAPI specification external

file with Infrastructure Composer

This example uses Infrastructure Composer from the console to reference an external
OpenAPI specification file that defines a API Gateway
REST API.

First, create a new project from the Infrastructure Composer **home** page.

Next, activate **local sync** by
selecting **Activate local sync** from the
**Menu**. Create a new folder named
`demo`, allow the prompt to view files, and select
**Activate**. When prompted, select **Save
changes**.

![The Infrastructure Composer Activate local sync window with a demo project folder selected and the Activate button is ready to be selected.](images/aac_use_ex_11.png)
Next, drag an Amazon API Gateway card onto the canvas. Select
**Details** to bring up the **Resource properties** panel.

![An API Gateway resource on the canvas with the Resource properties panel open.](images/aac_use_ex_12.png)
From the **Resource properties** panel,
configure the following and **save**.

- Select the **Use external file for api
  definition** option.
- Input `./api-spec.yaml` as the **relative path to external file**

![A window showing the checkbox marked under Use external file for api definition and a relative path to an external file defined.](images/aac_use_ex_13.png)
This creates the following directory on our local machine:

```
demo
└── api-spec.yaml
```

Now, you can configure the external file on our local machine. Using
our IDE, open the `api-spec.yaml` located in your
project folder. Replace its contents with the following:

```
openapi: '3.0'
info: {}
paths:
  /:
    get:
      responses: {}
    post:
      x-amazon-apigateway-integration:
        credentials:
          Fn::GetAtt:
            - ApiQueuesendmessageRole
            - Arn
        httpMethod: POST
        type: aws
        uri:
          Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:sqs:path/${AWS::AccountId}/${Queue.QueueName}
        requestParameters:
          integration.request.header.Content-Type: '''application/x-www-form-urlencoded'''
        requestTemplates:
          application/json: Action=SendMessage&MessageBody={"data":$input.body}
        responses:
          default:
            statusCode: 200
      responses:
        '200':
          description: 200 response
```

In the Infrastructure Composer **Template** view, you can see that
Infrastructure Composer has automatically updated your template to reference the external
file.

![The Infrastructure Composer template view showing your infrastructure code configured to reference the external file.](images/aac_use_ex_07.png)
