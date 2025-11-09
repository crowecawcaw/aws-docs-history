# Deploying a Node.js Express application to Elastic Beanstalk

This section walks you through deploying a sample application to Elastic Beanstalk using the Elastic Beanstalk Command Line Interface (EB CLI) and then updating the application to
use the [Express](http://expressjs.com/ "http://expressjs.com/") framework.

## Prerequisites

This tutorial requires the following prerequisites:

- The Node.js runtimes
- The default Node.js package manager software, npm
- The Express command line generator
- The Elastic Beanstalk Command Line Interface (EB CLI)

For details about installing the first three listed components and setting up your local development environment, see [Setting up your Node.js development environment for Elastic Beanstalk](nodejs-devenv.md "nodejs-devenv.md"). For this tutorial, you don't need to install the AWS SDK for Node.js, which is also mentioned in the referenced
topic.

For details about installing and configuring the EB CLI, see [Install EB CLI with setup script (recommended)](eb-cli3.md#eb-cli3-install "eb-cli3.md#eb-cli3-install") and [Configure the EB CLI](eb-cli3-configuration.md "eb-cli3-configuration.md").

## Create an Elastic Beanstalk environment

###### Your application directory

This tutorial uses a directory called `nodejs-example-express-rds` for the application source bundle. Create the `nodejs-example-express-rds`
directory for this tutorial.

```
~$ `mkdir nodejs-example-express-rds`
```

###### Note

Each tutorial in this chapter uses it's own directory for the application source bundle. The directory name matches the name of the sample application
used by the tutorial.

Change your current working directory to `nodejs-example-express-rds`.

```
~$ `cd nodejs-example-express-rds`
```

Now, let's set up an Elastic Beanstalk environment running the Node.js platform and the sample application. We'll use the Elastic Beanstalk command line interface (EB CLI).

###### To configure an EB CLI repository for your application and create an Elastic Beanstalk environment running the Node.js platform

1. Create a repository with the **[eb init](eb3-init.md "eb3-init.md")** command.

```
~/nodejs-example-express-rds$ `eb init --platform `node.js` --region `<region>``
```

This command creates a configuration file in a folder named `.elasticbeanstalk` that specifies settings for creating environments
for your application, and creates an Elastic Beanstalk application named after the current folder. 2. Create an environment running a sample application with the **[eb create](eb3-create.md "eb3-create.md")**
command.

```
~/nodejs-example-express-rds$ `eb create --sample `nodejs-example-express-rds``
```

This command creates a load-balanced environment with the default settings for the Node.js platform and the following resources:

    * **EC2 instance** – An Amazon Elastic Compute Cloud (Amazon EC2) virtual
     machine configured to run web apps on the platform that you choose.


    Each platform runs a specific set of software, configuration files, and scripts to support a specific language version, framework, web container, or
     combination of these. Most platforms use either Apache or NGINX as a reverse proxy that sits in front of your web app, forwards requests to it, serves
     static assets, and generates access and error logs.
    * **Instance security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This
     resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic isn't allowed on other ports.
    * **Load balancer** – An Elastic Load Balancing load balancer configured to distribute requests to the instances running your
     application. A load balancer also eliminates the need to expose your instances directly to the internet.
    * **Load balancer security group** – An Amazon EC2 security group configured to allow inbound traffic on port 80. This
     resource lets HTTP traffic from the internet reach the load balancer. By default, traffic isn't allowed on other ports.
    * **Auto Scaling group** – An Auto Scaling group configured to replace
     an instance if it is terminated or becomes unavailable.
    * **Amazon S3 bucket** – A storage location for your source
     code, logs, and other artifacts that are created when you use Elastic Beanstalk.
    * **Amazon CloudWatch alarms** – Two CloudWatch alarms that monitor the load on the instances in your environment and that are
     triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
    * **AWS CloudFormation stack** – Elastic Beanstalk uses AWS CloudFormation to launch the
     resources in your environment and propagate configuration changes. The resources are defined
     in a template that you can view in the [AWS CloudFormation
     console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
    * **Domain name** – A domain name that routes to your
     web app in the form
     *`subdomain`.`region`.elasticbeanstalk.com*.


    ###### Domain security

    To augment the security of your Elastic Beanstalk applications, the *elasticbeanstalk.com* domain is registered in the
     [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/").

    If you ever need to set sensitive cookies in the default domain name for your Elastic Beanstalk applications, we recommend that you use cookies with a
     `__Host-` prefix for increased security. This practice defends your domain against cross-site request forgery attempts (CSRF). For more
     information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla
     Developer Network.

3. When environment creation completes, use the [eb open](eb3-open.md "eb3-open.md") command to open the environment's URL in the
   default browser.

```
~/nodejs-example-express-rds$ `eb open`
```

You have now created a Node.js Elastic Beanstalk environment with a sample application. You can update it with your own application. Next, we update the sample
application to use the Express framework.

## Update the application to use Express

After you've created an environment with a sample application, you can update it with your own application. In this procedure, we first run the
**express** and **npm install** commands to set up the Express framework in your application directory. Then we use the
EB CLI to update your Elastic Beanstalk environment with the updated application.

###### To update your application to use Express

1. Run the `express` command. This generates `package.json`, `app.js`, and a few directories.

```
~/nodejs-example-express-rds$ `express`
```

When prompted, type `y` if you want to continue.

###### Note

If the **express** command doesn't work, you may not have installed the Express command line generator as described in the earlier
_Prerequisites_ section. Or the directory path setting for your local machine may need to be set up to run the
**express** command. See the _Prerequisites_ section for detailed steps about setting up your development environment,
so you can proceed with this tutorial. 2. Set up local dependencies.

```
~/nodejs-example-express-rds$ `npm install`
```

3. (Optional) Verify the web app server starts up.

```
~/nodejs-example-express-rds$ `npm start`
```

You should see output similar to the following:

```
> nodejs@0.0.0 start /home/local/user/node-express
> node ./bin/www
```

The server runs on port 3000 by default. To test it, run `curl http://localhost:3000` in another terminal, or open a browser on the local
computer and enter URL address `http://localhost:3000`.

Press **Ctrl+C** to stop the server. 4. Deploy the changes to your Elastic Beanstalk environment with the [eb deploy](eb3-deploy.md "eb3-deploy.md") command.

```
~/nodejs-example-express-rds$ `eb deploy`
```

5. Once the environment is green and ready, refresh the URL to verify it worked. You should see a web page that says **Welcome to
   Express**.

Next, let's update the Express application to serve static files and add a new page.

###### To configure static files and add a new page to your Express application

1. Add a second configuration file in the [.ebextensions](ebextensions.md "ebextensions.md") folder with the following
   content:

**`nodejs-example-express-rds/.ebextensions/staticfiles.config`**

```
option_settings:
    aws:elasticbeanstalk:environment:proxy:staticfiles:
        /stylesheets: public/stylesheets
```

This setting configures the proxy server to serve files in the `public` folder at the `/public` path of the
application. Serving files statically from the proxy server reduces the load on your application. For more information, see [Static files](create_deploy_nodejs.md#nodejs-platform-console-staticfiles "create_deploy_nodejs.md#nodejs-platform-console-staticfiles") earlier in this chapter. 2. (Optional) To confirm that static mappings are configured correctly, comment out the static mapping configuration in
`nodejs-example-express-rds/app.js`. This removes the mapping from the node application.

```
`//`  app.use(express.static(path.join(__dirname, 'public')));
```

The static file mappings in the `staticfiles.config` file from the previous step should still load the stylesheet successfully,
even after you comment this line out. To verify that the static file mappings are loaded through the proxy static file configuration, rather than the
express application, remove the values following `option_settings:`. After it has been removed from both the static file configuration and
the node application, the stylesheet will fail to load.

Remember to reset the contents of both the `nodejs-example-express-rds/app.js` and `staticfiles.config` when you're done
testing. 3. Add `nodejs-example-express-rds/routes/hike.js`. Type the following:

```
exports.index = function(req, res) {
 res.render('hike', {title: 'My Hiking Log'});
};

exports.add_hike = function(req, res) {
};
```

4. Update `nodejs-example-express-rds/app.js` to include three new lines.

First, add the following line to add a `require` for this route:

```
`var hike = require('./routes/hike');`
```

Your file should look similar to the following snippet:

```
var express = require('express');
var path = require('path');
`var hike = require('./routes/hike');`
```

Then, add the following two lines to `nodejs-example-express-rds/app.js` after `var app = express();`

```
app.get('/hikes', hike.index);
app.post('/add_hike', hike.add_hike);
```

Your file should look similar to the following snippet:

```
var app = express();
`app.get('/hikes', hike.index);
app.post('/add_hike', hike.add_hike);`
```

5. Copy `nodejs-example-express-rds/views/index.jade` to `nodejs-example-express-rds/views/hike.jade`.

```
~/nodejs-example-express-rds$ `cp views/`index.jade views/hike.jade``
```

6. Deploy the changes with the [eb deploy](eb3-deploy.md "eb3-deploy.md") command.

```
~/nodejs-example-express-rds$ `eb deploy`
```

7. Your environment will be updated after a few minutes. After your environment is green and ready, verify it worked by refreshing your browser and
   appending `hikes` at the end of the URL (e.g.,
   `http://node-express-env-syypntcz2q.elasticbeanstalk.com/hikes`).

You should see a web page titled **My Hiking Log**.

You have now created a web application that uses the Express framework. In the next section, we'll modify the application to use an Amazon Relational Database Service (RDS) to
store a hiking log.

## Update the application to use Amazon RDS

In this next step we update the application to use Amazon RDS for MySQL.

###### To update your application to use RDS for MySQL

1. To create an RDS for MySQL database coupled to your Elastic Beanstalk environment, follow the instructions in the [Adding
   a database](create-deploy-nodejs.md "create-deploy-nodejs.md") topic included later in this chapter. Adding a database instance takes about 10 minutes.
2. Update the dependencies section in the `package.json` with the following contents:

```
"dependencies": {
    "async": "^3.2.4",
    "express": "4.18.2",
    "jade": "1.11.0",
    "mysql": "2.18.1",
    "node-uuid": "^1.4.8",
    "body-parser": "^1.20.1",
    "method-override": "^3.0.0",
    "morgan": "^1.10.0",
    "errorhandler": "^1.5.1"
  }
```

3. Run **npm install**.

```
~/nodejs-example-express-rds$ `npm install`
```

4. Update `app.js` to connect to the database, create a table, and insert a single default hiking log. Every time this app is
   deployed it will drop the previous hikes table and recreate it.

```
/**
 * Module dependencies.
 */

 const express = require('express')
 , routes = require('./routes')
 , hike = require('./routes/hike')
 , http = require('http')
 , path = require('path')
 , mysql = require('mysql')
 , async = require('async')
 , bodyParser = require('body-parser')
 , methodOverride = require('method-override')
 , morgan = require('morgan')
 , errorhandler = require('errorhandler');

const { connect } = require('http2');

const app = express()

app.set('views', __dirname + '/views')
app.set('view engine', 'jade')
app.use(methodOverride())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(express.static(path.join(__dirname, 'public')))


app.set('connection', mysql.createConnection({
host: process.env.RDS_HOSTNAME,
user: process.env.RDS_USERNAME,
password: process.env.RDS_PASSWORD,
port: process.env.RDS_PORT}));

function init() {
 app.get('/', routes.index);
 app.get('/hikes', hike.index);
 app.post('/add_hike', hike.add_hike);
}

const client = app.get('connection');
async.series([
 function connect(callback) {
   client.connect(callback);
   console.log('Connected!');
 },
 function clear(callback) {
   client.query('DROP DATABASE IF EXISTS mynode_db', callback);
 },
 function create_db(callback) {
   client.query('CREATE DATABASE mynode_db', callback);
 },
 function use_db(callback) {
   client.query('USE mynode_db', callback);
 },
 function create_table(callback) {
    client.query('CREATE TABLE HIKES (' +
                        'ID VARCHAR(40), ' +
                        'HIKE_DATE DATE, ' +
                        'NAME VARCHAR(40), ' +
                        'DISTANCE VARCHAR(40), ' +
                        'LOCATION VARCHAR(40), ' +
                        'WEATHER VARCHAR(40), ' +
                        'PRIMARY KEY(ID))', callback);
 },
 function insert_default(callback) {
   const hike = {HIKE_DATE: new Date(), NAME: 'Hazard Stevens',
         LOCATION: 'Mt Rainier', DISTANCE: '4,027m vertical', WEATHER:'Bad', ID: '12345'};
   client.query('INSERT INTO HIKES set ?', hike, callback);
 }
], function (err, results) {
 if (err) {
   console.log('Exception initializing database.');
   throw err;
 } else {
   console.log('Database initialization complete.');
   init();
 }
});

module.exports = app
```

5. Add the following content to `routes/hike.js`. This will enable the routes to insert new hiking logs into the
   _HIKES_ database.

```
const uuid = require('node-uuid');
exports.index = function(req, res) {
  res.app.get('connection').query( 'SELECT * FROM HIKES', function(err,
rows) {
    if (err) {
      res.send(err);
    } else {
      console.log(JSON.stringify(rows));
      res.render('hike', {title: 'My Hiking Log', hikes: rows});
  }});
};
exports.add_hike = function(req, res){
  const input = req.body.hike;
  const hike = { HIKE_DATE: new Date(), ID: uuid.v4(), NAME: input.NAME,
  LOCATION: input.LOCATION, DISTANCE: input.DISTANCE, WEATHER: input.WEATHER};
  console.log('Request to log hike:' + JSON.stringify(hike));
  req.app.get('connection').query('INSERT INTO HIKES set ?', hike, function(err) {
      if (err) {
        res.send(err);
      } else {
        res.redirect('/hikes');
      }
   });
};
```

6. Replace the content of `routes/index.js` with the following:

```
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};
```

7. Add the following jade template to `views/hike.jade` to provide the user interface for adding hiking logs.

```
extends layout

block content
  h1= title
  p Welcome to #{title}

  form(action="/add_hike", method="post")
    table(border="1")
      tr
        td Your Name
        td
          input(name="hike[NAME]", type="textbox")
      tr
        td Location
        td
          input(name="hike[LOCATION]", type="textbox")
      tr
        td Distance
        td
          input(name="hike[DISTANCE]", type="textbox")
      tr
        td Weather
        td
          input(name="hike[WEATHER]", type="radio", value="Good")
          | Good
          input(name="hike[WEATHER]", type="radio", value="Bad")
          | Bad
          input(name="hike[WEATHER]", type="radio", value="Seattle", checked)
          | Seattle
      tr
        td(colspan="2")
          input(type="submit", value="Record Hike")

  div
    h3 Hikes
    table(border="1")
      tr
        td Date
        td Name
        td Location
        td Distance
        td Weather
      each hike in hikes
        tr
          td #{hike.HIKE_DATE.toDateString()}
          td #{hike.NAME}
          td #{hike.LOCATION}
          td #{hike.DISTANCE}
          td #{hike.WEATHER}
```

8. Deploy the changes with the [eb deploy](eb3-deploy.md "eb3-deploy.md") command.

```
~/nodejs-example-express-rds$ `eb deploy`
```

## Clean up

If you're done working with Elastic Beanstalk, you can terminate your environment.

Use the **eb terminate** command to terminate your environment and all of the resources that it contains.

```
~/nodejs-example-express-rds$ `eb terminate`
The environment "nodejs-example-express-rds-env" and all associated instances will be terminated.
To confirm, type the environment name: `nodejs-example-express-rds-env`
INFO: terminateEnvironment is starting.
...
```
