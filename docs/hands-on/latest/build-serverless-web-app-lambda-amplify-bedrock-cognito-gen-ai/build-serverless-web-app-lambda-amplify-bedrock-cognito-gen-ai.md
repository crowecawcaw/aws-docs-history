

# Build a serverless web application using generative AI
<a name="build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai"></a>


|  |  | 
| --- |--- |
| **AWS experience** | Beginner  | 
| **Time to complete** | 35 minutes  | 
| **Cost to complete** | Less than USD 0.10 if you complete the tutorial and delete the resources at the end | 
| **Requires** |  +  AWS account with administrator-level access  <br />+  AWS profile [configured](https://docs.amplify.aws/react/start/account-setup/)  <br />+  [Node.js](https://nodejs.org/en/download) and [npm](https://www.npmjs.com/)  <br />+  A [GitHub](https://github.com/) account   Accounts created within the past 24 hours might not yet have access to the services required for this tutorial.  | 
| **Last updated** | September 10, 2026  | 

## Overview
<a name="overview"></a>

In this tutorial, you learn how to use AWS Amplify to build a serverless web application powered by generative AI using Amazon Bedrock and the [Claude 3.5 Sonnet](https://aws.amazon.com/bedrock/claude/) foundation model. Users can enter a list of ingredients, and the application generates recipes based on the input ingredients. The application includes an HTML-based user interface for ingredient submission and a backend web app to request AI-generated recipes. 

## What you will accomplish
<a name="what-you-will-accomplish"></a>

In this tutorial, you complete the following tasks: 
+ Configure AWS Amplify to host your frontend application with continuous deployment built in 
+ Configure Amplify Auth and enable Amazon Bedrock foundation model access 
+ Build an app backend for handling requests for your web application 
+ Use Amplify Data to call the serverless backend 
+ Connect the app to the backend 

## Prerequisites
<a name="prerequisites"></a>

Before you start this tutorial, you need the following: 
+ An AWS account: if you don't already have one, follow the [Set up your environment](https://docs.aws.amazon.com/hands-on/latest/setup-environment/) tutorial. 
+ Your AWS profile configured for [local development](https://docs.amplify.aws/react/start/account-setup/).
+ [Node.js](https://nodejs.org/en/download) and [npm](https://www.npmjs.com/) installed on your environment. 
+ Familiarity with git and a [GitHub](https://github.com) account. 

## Application architecture
<a name="application-architecture"></a>

The following diagram provides a visual representation of the services used in this tutorial and how they are connected. This application uses AWS Amplify, a GraphQL API built with AWS AppSync, AWS Lambda, and Amazon Bedrock. 

As you go through the tutorial, you learn about the services in detail and find resources that help you get up to speed with them. 

![Architecture diagram illustrating a serverless generative AI application on AWS, featuring user interaction through AWS Amplify, authentication via Amazon Cognito, data flow using AWS AppSync and GraphQL, AWS Lambda for compute, and Amazon Bedrock for generative AI capabilities.](https://docs.aws.amazon.com/hands-on/latest/build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai/images/serverless-genai-architecture-diagram.png)


## Implementation
<a name="implementation"></a>

Complete the following steps to build, deploy, and run the application. 

### Step 1: Host a static website
<a name="task-1-host-static-website"></a>

AWS Amplify offers a Git-based CI/CD workflow for building, deploying, and hosting single-page web applications or static sites with backends. When connected to a Git repository, Amplify determines the build settings for both the frontend framework and any configured backend resources, and automatically deploys updates with every code commit. 

In this task, you start by creating a new React application and pushing it to a GitHub repository. You then connect the repository to AWS Amplify web hosting and deploy it to a globally available content delivery network (CDN) hosted on an `amplifyapp.com` domain. 

#### Create a new React application
<a name="task-1-create-react-app"></a>

1. Create the application

   1. In a new terminal or command line window, run the following command to use Vite to create a React application: 

     ```
     npm create vite@latest ai-recipe-generator -- --template react-ts -y
     cd ai-recipe-generator
     npm install
     npm run dev
     ```

1. Open the application

   1. In the terminal window, select and open the local link to view the Vite \+ React application. 

#### Initialize a GitHub repository
<a name="task-1-init-github-repo"></a>

In this step, you create a GitHub repository and commit your code to the repository. You need a GitHub account to complete this step. If you do not have an account, [sign up on GitHub](https://github.com/). 

**Note**  
If you have never used GitHub on your computer, follow [the steps to connect to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) before continuing to allow connection to your account.

1. Sign in to GitHub

   1. Sign in to the [GitHub website](https://github.com/). 

1. Start a new repository

   In the **Start a new repository** section, make the following selections: 

   1. For **Repository name**, enter `ai-recipe-generator`, and choose the **Public** radio button. 

   1. Then choose **Create a new repository**. 

1. Initialize Git

   1. Open a new terminal window, navigate to your project's root folder (`ai-recipe-generator`), and run the following commands to initialize a git repository and push the application to the new GitHub repository: 
**Note**  
Replace the SSH GitHub URL in the command with your GitHub URL.

     ```
     git init
     git add .
     git commit -m "first commit"
     git remote add origin git@github.com:<your-username>/ai-recipe-generator.git
     git branch -M main
     git push -u origin main
     ```

#### Install the Amplify packages
<a name="task-1-install-amplify-packages"></a>

1. Install Amplify

   1. Open a new terminal window, navigate to your app's root folder (`ai-recipe-generator`), and run the following command: 

     ```
     npm create amplify@latest -y
     ```

1. View directory

   1. Running the previous command scaffolds a lightweight Amplify project in the app's directory. 

#### Deploy your app with AWS Amplify
<a name="task-1-deploy-app"></a>

1. Open the Amplify console

   1. Sign in to the AWS Management Console in a new browser window, and open the [AWS Amplify console](https://console.aws.amazon.com/amplify/apps). 

   1. Choose **Create new app**. 

1. Select GitHub to deploy your app

   1. On the **Start building with Amplify** page, for **Deploy your app**, select **GitHub**, and choose **Next**. 

1. Authenticate with GitHub

   1. When prompted, authenticate with GitHub. You are automatically redirected back to the Amplify console. 

   1. Choose the repository and main branch you created earlier. 

   1. Then choose **Next**. 

1. Confirm the build settings

   1. Leave the default build settings, and choose **Next**. 

1. Review configuration

   1. Review the inputs selected, and choose **Save and deploy**. 

1. View your app

   1. AWS Amplify now builds your source code and deploys your app at `https://...amplifyapp.com`, and on every git push your deployment instance updates. It might take up to 5 minutes to deploy your app. 

   1. After the build completes, choose the **Visit deployed URL** button to see your web app up and running live.   
![The AWS Amplify dashboard showing the deployed 'ai-recipe-generator' app. Highlights include the production branch labeled as 'main', its deployed status, domain URL, last updated time, last commit (auto-build), repository link, and a prominent 'Visit deployed URL' button in the top right.](https://docs.aws.amazon.com/hands-on/latest/build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai/images/amplifylong-dashboard-deployed-recipe.png)

### Step 2: Manage users
<a name="task-2-manage-users"></a>

Now that you have a React web app, you configure an authentication resource for the app using AWS Amplify Auth, powered by Amazon Cognito. Amazon Cognito is a user directory service that manages user registration, authentication, account recovery, and more. 

You use the AWS Management Console to enable access to Amazon Bedrock and the Claude 3.5 Sonnet foundation model, which the app uses to generate recipes. 

#### Set up Amplify Auth
<a name="task-2-set-up-amplify-auth"></a>

The app uses email as the default login mechanism. When users sign up, they receive a verification email. In this step, you customize the verification email that is sent to users. 
+ Modify the resource file

  1. On your local machine, navigate to the `ai-recipe-generator/amplify/auth/resource.ts` file and update it with the following code. Then, save the file. 

    ```
    import { defineAuth } from "@aws-amplify/backend";
    
    export const auth = defineAuth({
      loginWith: {
        email: {
          verificationEmailStyle: "CODE",
          verificationEmailSubject: "Welcome to the AI-Powered Recipe Generator!",
          verificationEmailBody: (createCode) =>
            `Use this code to confirm your account: ${createCode()}`,
        },
      },
    });
    ```

#### Set up Amazon Bedrock model access
<a name="task-2-bedrock-model-access"></a>

Amazon Bedrock provides access to foundation models from leading AI companies. For this tutorial, you need access to the Anthropic Claude 3.5 Sonnet model in the US East (N. Virginia) (`us-east-1`) Region. 

1. Open the Amazon Bedrock console

   1. Sign in to the AWS Management Console in a new browser window, and open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/). Verify that you are in the US East (N. Virginia) (`us-east-1`) Region. 

1. Open the model catalog

   1. In the left navigation pane, under **Discover**, choose **Model catalog**. 

1. Find the Claude 3.5 Sonnet model

   1. Filter by the **Anthropic** provider, and then choose the Claude 3.5 Sonnet model. 

1. Request model access

   1. Choose **Request model access**. If this is the first time your account requests access to an Anthropic model, choose **Submit use case details**, complete the one-time form (a description of your intended use and a website URL), and then choose **Submit**. Access is typically granted immediately. 
**Note**  
If your account already has access to Anthropic models, the model opens directly and the use case form is not required. The form is required only once per account.

### Step 3: Build a serverless backend
<a name="task-3-build-serverless-backend"></a>

In this task, you configure a serverless function using AWS Amplify and AWS Lambda. This function takes an input parameter, the ingredients, to generate a prompt. It then sends this prompt to Amazon Bedrock through an HTTP POST request to the Claude 3.5 Sonnet model. The body of the request includes the prompt string within a messages array. 

#### Create a Lambda function for handling requests
<a name="task-3-create-lambda-function"></a>

1. Create a Lambda function

   1. On your local machine, navigate to the `ai-recipe-generator/amplify/data` folder, and create a file named `bedrock.js`. 

1. Add the function code

   1. Then, update the file with the following code: 

     ```
     export function request(ctx) {
         const { ingredients = [] } = ctx.args;
       
         // Construct the prompt with the provided ingredients
         const prompt = `Suggest a recipe idea using these ingredients: ${ingredients.join(", ")}.`;
       
         // Return the request configuration
         return {
           resourcePath: `/model/anthropic.claude-3-5-sonnet-20241022-v2:0/invoke`,
           method: "POST",
           params: {
             headers: {
               "Content-Type": "application/json",
             },
             body: JSON.stringify({
               anthropic_version: "bedrock-2023-05-31",
               max_tokens: 1000,
               messages: [
                 {
                   role: "user",
                   content: [
                     {
                       type: "text",
                       text: prompt,
                     },
                   ],
                 },
               ],
             }),
           },
         };
       }
       
       export function response(ctx) {
         // Parse the response body
         const parsedBody = JSON.parse(ctx.result.body);
         // Extract the text content from the response
         const res = {
           body: parsedBody.content[0].text,
         };
         // Return the response
         return res;
       }
     ```

   This code defines a request function that constructs the HTTP request to invoke the Claude 3.5 Sonnet foundation model in Amazon Bedrock. The response function parses the response and returns the generated recipe. 

#### Add Amazon Bedrock as a data source
<a name="task-3-add-bedrock-data-source"></a>
+ Update the backend file

  1. Update the `amplify/backend.ts` file with the following code. Then, save the file. 

     ```
     import { defineBackend } from "@aws-amplify/backend";
     import { data } from "./data/resource";
     import { PolicyStatement } from "aws-cdk-lib/aws-iam";
     import { auth } from "./auth/resource";
     
     const backend = defineBackend({
       auth,
       data,
     });
     
     const bedrockDataSource = backend.data.resources.graphqlApi.addHttpDataSource(
       "bedrockDS",
       "https://bedrock-runtime.us-east-1.amazonaws.com",
       {
         authorizationConfig: {
           signingRegion: "us-east-1",
           signingServiceName: "bedrock",
         },
       }
     );
     
     bedrockDataSource.grantPrincipal.addToPrincipalPolicy(
       new PolicyStatement({
         resources: [
           "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0",
         ],
         actions: ["bedrock:InvokeModel"],
         
       })
     );
     ```

  1. The code adds an HTTP data source for Amazon Bedrock to your API and grants it permissions to invoke the Claude model. 

### Step 4: Deploy the backend API
<a name="task-4-deploy-backend-api"></a>

In this task, you configure a custom query that references the data source and the resolver you defined in the previous task to produce a recipe based on a list of ingredients. This query uses a custom type to structure the response from Amazon Bedrock. 

#### Set up Amplify Data
<a name="task-4-set-up-amplify-data"></a>

1. Update the resource.ts file

   1. On your local machine, navigate to the `ai-recipe-generator/amplify/data/resource.ts` file, and update it with the following code. Then, save the file. 

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

   1. The following code defines the `askBedrock` query that takes an array of strings called `ingredients` and returns a `BedrockResponse`. The `.handler(a.handler.custom({ entry: "./bedrock.js", dataSource: "bedrockDS" }))` line sets up a custom handler for this query, defined in `bedrock.js`, using `bedrockDS` as its data source. 
**Note**  
The API key expires in 30 days, as set by `expiresInDays: 30`. If you return to this app later and see authorization failures, redeploy the backend to rotate the API key.

1. Deploy resources

   1. Open a new terminal window, navigate to your app's project folder (`ai-recipe-generator`), and run the following command to deploy cloud resources into an isolated development space so you can iterate fast. 

     ```
     npx ampx sandbox
     ```

1. View confirmation message

   1. After the cloud sandbox is fully deployed, your terminal displays a confirmation message.

1. Verify outputs file creation

   1. Verify that the `amplify_outputs.json` file was generated and added to your project.

### Step 5: Build the frontend
<a name="task-5-build-frontend"></a>

In this task, you update the website you created in [Step 1: Host a static website](#task-1-host-static-website) to use the Amplify UI component library to scaffold out an entire user authentication flow, allowing users to sign up, sign in, and reset their password, and invoke the GraphQL API to use the custom query for generating a recipe based on a list of ingredients. 

#### Install the Amplify libraries
<a name="task-5-install-amplify-libraries"></a>

You need two Amplify libraries for your project. The main `aws-amplify` library contains all of the client-side APIs for connecting your app's frontend to your backend, and the `@aws-amplify/ui-react` library contains framework-specific UI components. 
+ Install the libraries

  1. Open a new terminal window, navigate to your project's root folder (`ai-recipe-generator`), and run the following command to install the libraries. 

    ```
    npm install aws-amplify @aws-amplify/ui-react
    ```

#### Style the app UI
<a name="task-5-style-app-ui"></a>

1. Modify the index CSS

   1. On your local machine, navigate to the `ai-recipe-generator/src/index.css` file, and update it with the following code to center the app UI. Then, save the file. 

     ```
     :root {
       font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
       line-height: 1.5;
       font-weight: 400;
     
       color: rgba(255, 255, 255, 0.87);
     
       font-synthesis: none;
       text-rendering: optimizeLegibility;
       -webkit-font-smoothing: antialiased;
       -moz-osx-font-smoothing: grayscale;
     
       max-width: 1280px;
       margin: 0 auto;
       padding: 2rem;
     
     }
     
     .card {
       padding: 2em;
     }
     
     .read-the-docs {
       color: #888;
     }
     
     .box:nth-child(3n + 1) {
       grid-column: 1;
     }
     .box:nth-child(3n + 2) {
       grid-column: 2;
     }
     .box:nth-child(3n + 3) {
       grid-column: 3;
     }
     ```

1. Modify the app CSS

   1. Update the `src/App.css` file with the following code to style the ingredients form. Then, save the file.

     ```
     .app-container {
     
       margin: 0 auto;
       padding: 20px;
       text-align: center;
     }
     
     .header-container {
       padding-bottom: 2.5rem;
       margin:  auto;
       text-align: center;
     
       align-items: center;
       max-width: 48rem;
       
       
     }
     
     .main-header {
       font-size: 2.25rem;
       font-weight: bold;
       color: #1a202c;
     }
     
     .main-header .highlight {
       color: #2563eb;
     }
     
     @media (min-width: 640px) {
       .main-header {
         font-size: 3.75rem;
       }
     }
     
     .description {
     
       font-weight: 500;
       font-size: 1.125rem;
       max-width: 65ch;
       color: #1a202c;
     }
     
     .form-container {
       margin-bottom: 20px;
     }
     
     .search-container {
       display: flex;
       flex-direction: column;
       gap: 10px;
       align-items: center;
     }
     
     .wide-input {
       width: 100%;
       padding: 10px;
       font-size: 16px;
       border: 1px solid #ccc;
       border-radius: 4px;
     }
     
     .search-button {
       width: 100%; /* Make the button full width */
       max-width: 300px; /* Set a maximum width for the button */
       padding: 10px;
       font-size: 16px;
       background-color: #007bff;
       color: white;
       border: none;
       border-radius: 4px;
       cursor: pointer;
     }
     
     .search-button:hover {
       background-color: #0056b3;
     }
     
     .result-container {
       margin-top: 20px;
       transition: height 0.3s ease-out;
       overflow: hidden;
     }
     
     .loader-container {
       display: flex;
       flex-direction: column;
       align-items: center;
       gap: 10px;
     }
     
     .result {
       background-color: #f8f9fa;
       border: 1px solid #e9ecef;
       border-radius: 4px;
       padding: 15px;
       white-space: pre-wrap;
       word-wrap: break-word;
       color: black;
       font-weight: bold;
       text-align: left; /* Align text to the left */
     }
     ```

#### Implement the UI
<a name="task-5-implement-ui"></a>

1. Add authentication

   1. On your local machine, navigate to the `ai-recipe-generator/src/main.tsx` file, and update it with the following code. Then, save the file. 

      ```
      import React from "react";
      import ReactDOM from "react-dom/client";
      import App from "./App.jsx";
      import "./index.css";
      import { Authenticator } from "@aws-amplify/ui-react";
      
      ReactDOM.createRoot(document.getElementById("root")!).render(
        <React.StrictMode>
          <Authenticator>
            <App />
          </Authenticator>
        </React.StrictMode>
      );
      ```

   1. The code uses the Amplify Authenticator component to scaffold out an entire user authentication flow, allowing users to sign up, sign in, reset their password, and confirm sign-in for multi-factor authentication (MFA). 

1. Configure the Amplify library

   1. Replace the contents of the `ai-recipe-generator/src/App.tsx` file with the following code, then save the file. 

      ```
      import { FormEvent, useState } from "react";
      import { Loader, Placeholder } from "@aws-amplify/ui-react";
      import "./App.css";
      import { Amplify } from "aws-amplify";
      import { Schema } from "../amplify/data/resource";
      import { generateClient } from "aws-amplify/data";
      import outputs from "../amplify_outputs.json";
      import "@aws-amplify/ui-react/styles.css";
      
      Amplify.configure(outputs);
      
      const amplifyClient = generateClient<Schema>({
        authMode: "userPool",
      });
      
      function App() {
        const [result, setResult] = useState<string>("");
        const [loading, setLoading] = useState(false);
      
        const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
          event.preventDefault();
          setLoading(true);
          try {
            const formData = new FormData(event.currentTarget);
            const { data, errors } = await amplifyClient.queries.askBedrock({
              ingredients: [formData.get("ingredients")?.toString() || ""],
            });
            if (!errors) {
              setResult(data?.body || "No data returned");
            } else {
              console.log(errors);
            }
          } catch (e) {
            alert(`An error occurred: ${e}`);
          } finally {
            setLoading(false);
          }
        };
      
        return (
          <div className="app-container">
            <div className="header-container">
              <h1 className="main-header">
                Meet Your Personal
                <br />
                <span className="highlight">Recipe AI</span>
              </h1>
              <p className="description">
                Simply type a few ingredients using the format ingredient1,
                ingredient2, etc., and Recipe AI will generate an all-new recipe on
                demand...
              </p>
            </div>
            <form onSubmit={onSubmit} className="form-container">
              <div className="search-container">
                <input
                  type="text"
                  className="wide-input"
                  id="ingredients"
                  name="ingredients"
                  placeholder="Ingredient1, Ingredient2, Ingredient3,...etc"
                />
                <button type="submit" className="search-button">
                  Generate
                </button>
              </div>
            </form>
            <div className="result-container">
              {loading ? (
                <div className="loader-container">
                  <p>Loading...</p>
                  <Loader size="large" />
                  <Placeholder size="large" />
                  <Placeholder size="large" />
                  <Placeholder size="large" />
                </div>
              ) : (
                result && <p className="result">{result}</p>
              )}
            </div>
          </div>
        );
      }
      
      export default App;
      ```

   1. The code starts by configuring the Amplify library with the client configuration file (`amplify_outputs.json`). It then generates a data client using the `generateClient()` function. The app presents a form for submitting a list of ingredients. After you submit the list, the app uses the data client to pass the list to the `askBedrock` query and retrieve the generated recipe, and then displays it to you. 

1. Launch the app

   1. Open a new terminal window, navigate to your project's root directory (`ai-recipe-generator`), and run the following command to launch the app: 

     ```
     npm run dev
     ```

1. Open the app

   1. Select the local host link to open the Vite \+ React application. 

1. Create an account

   1. Choose the **Create Account** tab, and use the authentication flow to create a new user by entering your email address and a password. 

   1. Then, choose **Create Account**. 

1. Enter verification code

   1. You receive a verification code by email. Enter the verification code to log in to the app. 

1. Generate recipes

   1. When signed in, you can enter ingredients and choose **Generate** to generate recipes.   
![A web app titled 'Meet Your Personal Recipe AI' showing an input box for typing ingredients such as chicken, white rice, yellow squash, and onion, with a 'Generate' button for creating recipes using AI.](https://docs.aws.amazon.com/hands-on/latest/build-serverless-web-app-lambda-amplify-bedrock-cognito-gen-ai/images/uba-serverless-gen-generate-ingredients.png)

1. Push changes

   1. In the open terminal window, run the following command to push the changes to GitHub: 

     ```
     git add .
     git commit -m 'connect to bedrock'
     git push origin main
     ```

1. View your changes

   1. Sign in to the AWS Management Console in a new browser window, and open the [AWS Amplify console](https://console.aws.amazon.com/amplify/apps). 

   1. AWS Amplify automatically builds your source code and deploys your app at `https://...amplifyapp.com`, and on every git push your deployment instance updates. Choose the **Visit deployed URL** button to see your web app up and running live. 

## Clean up resources
<a name="clean-up-resources"></a>

In this task, you go through the steps to delete all the resources you created throughout this tutorial. It is a best practice to delete resources you are no longer using to avoid unwanted charges. 

1. Open general settings

   1. In the Amplify console, in the left navigation for the `ai-recipe-generator` app, choose **App settings**, and select **General settings**. 

1. Delete the app

   1. In the **General settings** section, choose **Delete app**. 

## Congratulations
<a name="congratulations"></a>

You have created a React web app and used Amplify and Amazon Bedrock to develop an AI-powered recipe generator app. Additionally, you have deployed the app on AWS using Amplify Hosting. 

## Next steps
<a name="next-steps"></a>

To continue building on what you learned in this tutorial, see the following resources: 
+ [Prompt engineering guidelines for Anthropic Claude models](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html) 
+ [Build a backend with AWS Amplify (Gen 2)](https://docs.amplify.aws/react/build-a-backend/) 

## Related resources
<a name="related-resources"></a>

To learn more about the AWS services you used in this tutorial, see the following resources: 
+ [AWS Amplify (Gen 2) documentation](https://docs.amplify.aws/) 
+ [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) 
+ [Anthropic Claude models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) 
+ [Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) 
+ [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 