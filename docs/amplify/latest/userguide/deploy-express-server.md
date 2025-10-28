# Deploying an Express server using the deployment

manifest

This example explains how to deploy a basic Express server using the Amplify Hosting
deployment specification. You can leverage the provided deployment manifest to specify
routing, compute resources, and other configurations.

###### Set up an Express server locally before deploying to Amplify Hosting

1. Create a new directory for your project and install Express and Typescript.

```
mkdir express-app
cd express-app

# The following command will prompt you for information about your project
npm init

# Install express, typescript and types
npm install express --save
npm install typescript ts-node @types/node @types/express --save-dev

```

2. Add a `tsconfig.json` file to the root of your project with the following
   contents.

```
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules"]
}
```

3. Create a directory named `src` in your project root.
4. Create an `index.ts` file in the `src`
   directory. This will be the entry point to the application that starts an Express
   server. The server should be configured to listen on port 3000.

```
// src/index.ts
import express from 'express';

const app: express.Application = express();
const port = 3000;

app.use(express.text());

app.listen(port, () => {
  console.log(`server is listening on ${port}`);
});

// Homepage
app.get('/', (req: express.Request, res: express.Response) => {
  res.status(200).send("Hello World!");
});

// GET
app.get('/get', (req: express.Request, res: express.Response) => {
  res.status(200).header("x-get-header", "get-header-value").send("get-response-from-compute");
});

//POST
app.post('/post', (req: express.Request, res: express.Response) => {
  res.status(200).header("x-post-header", "post-header-value").send(req.body.toString());
});

//PUT
app.put('/put', (req: express.Request, res: express.Response) => {
  res.status(200).header("x-put-header", "put-header-value").send(req.body.toString());
});

//PATCH
app.patch('/patch', (req: express.Request, res: express.Response) => {
  res.status(200).header("x-patch-header", "patch-header-value").send(req.body.toString());
});

// Delete
app.delete('/delete', (req: express.Request, res: express.Response) => {
  res.status(200).header("x-delete-header", "delete-header-value").send();
});

```

5. Add the following scripts to your `package.json` file.

```
"scripts": {
  "start": "ts-node src/index.ts",
  "build": "tsc",
  "serve": "node dist/index.js"
}
```

6. Create a directory named `public` in the root of your project.
   Then create a file named `hello-world.txt` with the following
   contents.

```
Hello world!
```

7. Add a `.gitignore` file to your project root with the following
   contents.

```
.amplify-hosting
dist
node_modules
```

###### Set up the Amplify deployment manifest

1. Create a file named `deploy-manifest.json` in your project's root
   directory.
2. Copy and paste the following manifest into your
   `deploy-manifest.json` file.

```
{
  "version": 1,
  "framework": { "name": "express", "version": "4.18.2" },
  "imageSettings": {
    "sizes": [
      100,
      200,
      1920
    ],
    "domains": [],
    "remotePatterns": [],
    "formats": [],
    "minimumCacheTTL": 60,
    "dangerouslyAllowSVG": false
  },
  "routes": [
    {
      "path": "/_amplify/image",
      "target": {
        "kind": "ImageOptimization",
        "cacheControl": "public, max-age=3600, immutable"
      }
    },
    {
      "path": "/*.*",
      "target": {
        "kind": "Static",
        "cacheControl": "public, max-age=2"
      },
      "fallback": {
        "kind": "Compute",
        "src": "default"
      }
    },
    {
      "path": "/*",
      "target": {
        "kind": "Compute",
        "src": "default"
      }
    }
  ],
  "computeResources": [
    {
      "name": "default",
      "runtime": "nodejs22.x",
      "entrypoint": "index.js"
    }
  ]
}
```

The manifest describes how Amplify Hosting should handle the deployment of your
application. The primary settings are the following.

    * version – Indicates the version of the
     deployment specification that you're using.
    * framework – Adjust this to specify your
     Express server setup.
    * imageSettings – This section is optional
     for an Express server unless you're handling image
     optimization.
    * routes – These are critical for directing
     traffic to the right parts of your app. The `"kind": "Compute"` route
     directs traffic to your server logic.
    * computeResources – Use this section to
     specify your Express server's runtime and entry point.

Next, set up a post-build script that moves the built application artifacts into the
`.amplify-hosting` deployment bundle. The directory structure aligns
with the Amplify Hosting deployment specification.

###### Set up the post-build script

1. Create a directory named `bin` in your project root.
2. Create a file named `postbuild.sh` in the
   `bin` directory. Add the following contents to the
   `postbuild.sh` file.

```
#!/bin/bash

rm -rf ./.amplify-hosting

mkdir -p ./.amplify-hosting/compute

cp -r ./dist ./.amplify-hosting/compute/default
cp -r ./node_modules ./.amplify-hosting/compute/default/node_modules

cp -r public ./.amplify-hosting/static

cp deploy-manifest.json ./.amplify-hosting/deploy-manifest.json
```

3. Add a `postbuild` script to your `package.json` file.
   The file should look like the following.

```
"scripts": {
  "start": "ts-node src/index.ts",
  "build": "tsc",
  "serve": "node dist/index.js",
  "postbuild": "chmod +x bin/postbuild.sh && ./bin/postbuild.sh"
}
```

4. Run the following command to build your application.

```
npm run build
```

5. (Optional) Adjust your routes for Express. You can modify the routes in your
   deployment manifest to fit your Express server. For example, if you don't have any
   static assets in the `public` directory, you might only need the catch-all
   route `"path": "/*"` directing to Compute. This will depend on your server's
   setup.
   Your final directory structure should look like the following.

```
express-app/
├── .amplify-hosting/
│   ├── compute/
│   │   └── default/
│   │       ├── node_modules/
│   │       └── index.js
│   ├── static/
│   │   └── hello.txt
│   └── deploy-manifest.json
├── bin/
│   ├── .amplify-hosting/
│   │   ├── compute/
│   │   │   └── default/
│   │   └── static/
│   └── postbuild.sh*
├── dist/
│   └── index.js
├── node_modules/
├── public/
│   └── hello.txt
├── src/
│   └── index.ts
├── deploy-manifest.json
├── package.json
├── package-lock.json
└── tsconfig.json
```

###### Deploy your server

1. Push your code to your Git repository and then deploy your app to Amplify
   Hosting.
2. Update your build settings to point `baseDirectory` to
   `.amplify-hosting` as follows. During the build, Amplify will
   detect the manifest file in the `.amplify-hosting` directory and
   deploy your Express server as configured.

```
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - nvm use 18
        - npm install
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .amplify-hosting
    files:
      - '**/*'
```

3. To verify that your deployment was successful and that your server is running
   correctly, visit your app at the default URL provided by Amplify Hosting.
