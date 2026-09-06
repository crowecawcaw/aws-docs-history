

# Task 4: Deploy the Backend API
<a name="module-four"></a>

## Overview
<a name="overview"></a>

In this task, you will configure a custom query that will reference the data source and the resolver you defined the previous model to produce a recipe based on a list of ingredients. This query will use a custom type to structure the response from Amazon Bedrock.  

## What you will accomplish
<a name="what-you-will-accomplish"></a>

In this tutorial, you will: 
+ Define a GraphQL Query that takes an array of strings 
+ Define a custom type to be used to structure the response from the query 

## Implementation
<a name="implementation"></a>


|  |  | 
| --- |--- |
| **Time to complete** | 5 minutes  | 
| **Get help** | [Troubleshooting Amplify](https://docs.amplify.aws/react/build-a-backend/troubleshooting/) <br />[Learn about Data](https://docs.amplify.aws/react/build-a-backend/data/)  | 

### Step 1: Set up Amplify Data
<a name="set-up-amplify-data"></a>

1. Update the resource.ts file

   On your local machine, navigate to the **ai-recipe-generator/amplify/data/resource.ts** file, and **update** it with the following code. Then, **save** the file. 
   + The following code defines the **askBedrock** query that takes an array of strings called **ingredients** and returns a **BedrockResponse**. The **.handler(a.handler.custom({ entry: "./bedrock.js", dataSource: "bedrockDS" }))** line sets up a custom handler for this query, defined in **bedrock.js**, using **bedrockDS** as its data source. 

   ```
   import { type ClientSchema, a, defineData } from "@aws-amplify/backend";
   
   const schema = a.schema({
     BedrockResponse: a.customType({
       body: a.string(),
       error: a.string(),
     }),
     askBedrock: a
       .query()
       .arguments({ ingredients: a.string().array() })
       .returns(a.ref("BedrockResponse"))
       .authorization((allow) => [allow.authenticated()])
       .handler(
         a.handler.custom({
           entry: "./bedrock.js",
           dataSource: "bedrockDS"
         })
       ),
   });
   
   export type Schema = ClientSchema<typeof schema>;
   
   export const data = defineData({
     schema,
     authorizationModes: {
       defaultAuthorizationMode: "apiKey",
       apiKeyAuthorizationMode: {
         expiresInDays: 30,
       },
     },
   });
   ```  
![The folder structure of the 'ai-recipe-generator' project, with the 'resource.ts' file highlighted in the data directory.](http://docs.aws.amazon.com/hands-on/latest/build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai/images/recipe-generator-folder-structure-resource.png)

1. Deploy resources

   **Open** a new terminal window, **navigate** to your apps project folder (ai-recipe-generator), and **run** the following command to deploy cloud resources into an isolated development space so you can iterate fast. 

   ```
   npx ampx sandbox
   ```  
![Result of running the npx ampx sandbox command.](http://docs.aws.amazon.com/hands-on/latest/build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai/images/sandbox.png)

1. View confirmation message

   After the cloud sandbox has been fully deployed, your terminal will display a confirmation message.  
![The confirmation message.](http://docs.aws.amazon.com/hands-on/latest/build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai/images/confirmation-message.png)

1. Verify outputs file creation

   Verify that the *amplify\_outputs.json* file was **generated** and **added** to your project.  
![Showing the amplify_outputs.json file in Finder.](http://docs.aws.amazon.com/hands-on/latest/build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai/images/amplify-outputs-json.png)

## Conclusion
<a name="conclusion"></a>

You have configured a GraphQL API to define a custom query to connect to Amazon Bedrock and generate recipes based on a list of ingredients.  