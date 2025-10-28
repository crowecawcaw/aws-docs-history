# Adding an Amazon RDS DB instance to your Node.js Elastic Beanstalk environment

This topic provides instructions to create an Amazon RDS using the Elastic Beanstalk console.
You can use an Amazon Relational Database Service (Amazon RDS) DB instance to store data gathered and modified by your
application. The database can be coupled to your environment and managed by Elastic Beanstalk, or it can be created as decoupled
and managed externally by another service.
In these instructions the database is coupled to your environment and managed by Elastic Beanstalk. For more information about integrating an Amazon RDS with
Elastic Beanstalk, see [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md").

###### Sections

- [Adding a DB instance to your environment](#nodejs-rds-create "#nodejs-rds-create")
- [Downloading a driver](#nodejs-rds-drivers "#nodejs-rds-drivers")
- [Connecting to a database](#nodejs-rds-connect "#nodejs-rds-connect")

## Adding a DB instance to your environment

###### To add a DB instance to your environment

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Database** configuration category, choose **Edit**.
5. Choose a DB engine, and enter a user name and password.
6. To save the changes choose **Apply** at the bottom of the page.

Adding a DB instance takes about 10 minutes. When the environment update is complete, the
DB instance's hostname and other connection information are available to your application
through the following environment properties:

| Property name  | Description                                                                                    | Property value                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RDS_HOSTNAME` | The hostname of the DB instance.                                                               | On the **Connectivity & security** tab on the Amazon RDS console: **Endpoint**. |
| `RDS_PORT`     | The port where the DB instance accepts connections. The default value varies among DB engines. | On the **Connectivity & security** tab on the Amazon RDS console: **Port**.     |
| `RDS_DB_NAME`  | The database name, `ebdb`.                                                                     | On the **Configuration** tab on the Amazon RDS console: **DB Name**.            |
| `RDS_USERNAME` | The username that you configured for your database.                                            | On the **Configuration** tab on the Amazon RDS console: **Master username**.    |
| `RDS_PASSWORD` | The password that you configured for your database.                                            | Not available for reference in the Amazon RDS console.                          | For more information about configuring a database instance coupled with an Elastic Beanstalk environment, see [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md"). ## Downloading a driver Add the database driver to your project's [package.json file](nodejs-platform-dependencies.md#nodejs-platform-packagejson "nodejs-platform-dependencies.md#nodejs-platform-packagejson") under `dependencies`. ###### Example `package.json` – Express with MySQL ``{ "name": "my-app", "version": "0.0.1", "private": true, "dependencies": { "ejs": "latest", "aws-sdk": "latest", "express": "latest", "body-parser": "latest", `"mysql": "latest"` }, "scripts": { "start": "node app.js" } }`` ###### Common driver packages for Node.js <br>• **MySQL** – [mysql](https://www.npmjs.com/package/mysql "https://www.npmjs.com/package/mysql") <br>• **PostgreSQL** – [node-postgres](https://www.npmjs.com/package/pg "https://www.npmjs.com/package/pg") <br>• **SQL Server** – [node-mssql](https://www.npmjs.com/package/mssql "https://www.npmjs.com/package/mssql") <br>• **Oracle** – [node-oracledb](https://www.npmjs.com/package/oracledb "https://www.npmjs.com/package/oracledb") ## Connecting to a database Elastic Beanstalk provides connection information for attached DB instances in environment properties. Use `process.env.`VARIABLE`` to read the properties and configure a database connection. ###### Example app.js – MySQL database connection `var mysql = require('mysql'); var connection = mysql.createConnection({ host     : process.env.RDS_HOSTNAME, user     : process.env.RDS_USERNAME, password : process.env.RDS_PASSWORD, port     : process.env.RDS_PORT }); connection.connect(function(err) { if (err) { console.error('Database connection failed: ' + err.stack); return; } console.log('Connected to database.'); }); connection.end();` For more information about constructing a connection string using node-mysql, see [npmjs.org/package/mysql](https://npmjs.org/package/mysql "https://npmjs.org/package/mysql"). |
