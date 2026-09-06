

# Task 1: Create a new Amplify Project
<a name="module-one"></a>


|  |  | 
| --- |--- |
| **Time to complete** | 5 minutes  | 
| **Requires** |  +  A [GitHub account](https://github.com/)  <br />+  GitHub [SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)  <br />+  [Nodejs](https://nodejs.org/en/download) and [npm](https://www.npmjs.com/)    | 
| **Get help** | [Troubleshooting Amplify](https://docs.amplify.aws/react/build-a-backend/troubleshooting/)  | 

## Overview
<a name="overview"></a>

In this task, you will create a new web application using [React](https://reactjs.org/), a JavaScript library for building user interfaces, and learn how to configure AWS Amplify for your first project. 

## What you will accomplish
<a name="what-you-will-accomplish"></a>
+ Create a new web application 
+ Set up Amplify on your project 

## Implementation
<a name="implementation"></a>

### Step 1: Create a new Amplify Project
<a name="primary-step"></a>

1. Check environment

   In a new terminal window or command line, **run** the following commands to verify that you are running at least Node.js version 18.16.0 and npm version 6.14.4 or greater. 
   + If you are not running these versions, visit the [nodejs](https://nodejs.org/) and [npm website](https://www.npmjs.com/) for more information. 
**Note**  
Your output might differ based on the version installed.

   ```
   node -v
   npm -v
   ```  
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/deploy-webapp-amplify/images/resource-creation-interface.png)

1. Create a new React application

   In a new terminal or command line window, **run** the following command to use Vite to create a React application: 

   ```
   npm create vite@latest expensetracker -- --template react
   cd expensetracker
   npm install
   npm run dev
   ```  
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/deploy-webapp-amplify/images/resource-creation-interface-1.png)

1. Open the local development server

   In the terminal window, select and open the **Local link** to view the Vite \+ React application.   
![The navigation interface.](http://docs.aws.amazon.com/hands-on/latest/deploy-webapp-amplify/images/navigation-interface.png)

1. Install Amplify CLI

   **Open** a new terminal window, **navigate** to your projects root folder (**expensetracker**), and **run** the following command: 

   ```
   npm create amplify@latest -y
   ```  
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/deploy-webapp-amplify/images/resource-creation-interface-2.png)

Running the previous command will scaffold a lightweight Amplify project in the app’s directory where you installed the packages. 

![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/deploy-webapp-amplify/images/resource-creation-interface-3.png)


## Conclusion
<a name="conclusion"></a>

In this task, you learned how to create a React frontend application, and installed the amplify packages in preparation to configure a backend for the app.   