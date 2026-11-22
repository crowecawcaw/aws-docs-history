

# Create an Amazon RDS DB instance

Create an RDS for MariaDB, RDS for MySQL, or RDS for PostgreSQL DB instance that maintains the data used by a web application. 

------
#### [ RDS for MariaDB ]

**To create a MariaDB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the AWS Management Console, check the AWS Region. It should be the same as the one where you created your EC2 instance.

1. In the navigation pane, choose **Databases**.

1. Choose **Create database**.

1. On the **Create database** page, choose **Standard create**.

1. For **Engine options**, choose **MariaDB**.  
![The Engine options section with MariaDB selected as the engine type. The other engine types shown are Aurora (MySQL Compatible), Aurora (PostgreSQL Compatible), MySQL, PostgreSQL, Oracle, Microsoft SQL Server, and IBM Db2.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/tutorial-create-mariadb.png)

1. For **Templates**, choose **Free tier** or **Sandbox**. **Free tier** appears for free plan accounts. **Sandbox** appears for paid plan accounts.  
![The Templates section with Free tier selected. The other templates shown are Production and Dev/Test.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/tutorial-create-template.png)

1. In the **Availability and durability** section, keep the defaults.

1. In the **Settings** section, set these values:
   + **DB instance identifier** – Type **tutorial-db-instance**.
   + **Master username** – Type **tutorial\_user**.
   + **Auto generate a password** – Leave the option turned off.
   + **Master password** – Type a password.
   + **Confirm password** – Retype the password.  
![The Settings section with tutorial-db-instance entered as the DB instance identifier and tutorial_user entered as the username. Auto generate a password is cleared, and both password fields contain a masked password.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Settings.png)

1. In the **Instance configuration** section, set these values:
   + **Burstable classes (includes t classes)**
   + **db.t3.micro**  
![The Instance configuration section with Burstable classes (includes t classes) selected for DB instance class and db.t3.micro chosen. The db.t3.micro class has 2 vCPUs and 1 GiB RAM.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_DB_instance_micro.png)

1. In the **Storage** section, keep the defaults.

1. In the **Connectivity** section, set these values and keep the other values as their defaults:
   + For **Compute resource**, choose **Connect to an EC2 compute resource**.
   + For **EC2 instance**, choose the EC2 instance you created previously, such as **tutorial-ec2-instance-web-server**.  
![The Connectivity section with Connect to an EC2 compute resource selected for Compute resource and tutorial-ec2-instance-web-server chosen for EC2 instance. A note explains that adding an EC2 compute resource automatically selects the VPC, DB subnet group, and public access settings, and adds VPC security groups to the database and the EC2 instance.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Connectivity.png)

1. In the **Database authentication** section, make sure **Password authentication** is selected.

1. Open the **Additional configuration** section, and enter **sample** for **Initial database name**. Keep the default settings for the other options.

1. To create your MariaDB instance, choose **Create database**.

   Your new DB instance appears in the **Databases** list with the status **Creating**.

1. Wait for the **Status** of your new DB instance to show as **Available**. Then choose the DB instance name to show its details.

1. In the **Connectivity & security** section, view the **Endpoint** and **Port** of the DB instance.  
![The details page for tutorial-db-instance with the Connectivity & security tab open, showing the Endpoint and Port values, which are circled in red for the purposes of the illustration. The port is 3306.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Endpoint_Port.png)

   Note the endpoint and port for your DB instance. You use this information to connect your web server to your DB instance.

1. Complete [Install a web server on your EC2 instance](CHAP_Tutorials.WebServerDB.CreateWebServer.md).

------
#### [ RDS for MySQL ]

**To create a MySQL DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the AWS Management Console, check the AWS Region. It should be the same as the one where you created your EC2 instance.

1. In the navigation pane, choose **Databases**.

1. Choose **Create database**.

1. On the **Create database** page, choose **Standard create**.

1. For **Engine options**, choose **MySQL**.  
![The Engine options section with MySQL selected as the engine type. The other engine types shown are Aurora (MySQL Compatible), Aurora (PostgreSQL Compatible), MariaDB, PostgreSQL, Oracle, Microsoft SQL Server, and IBM Db2.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/tutorial-create-mysql.png)

1. For **Templates**, choose **Free tier** or **Sandbox**. **Free tier** appears for free plan accounts. **Sandbox** appears for paid plan accounts.  
![The Templates section with Free tier selected. The other templates shown are Production and Dev/Test.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/tutorial-create-template.png)

1. In the **Availability and durability** section, keep the defaults.

1. In the **Settings** section, set these values:
   + **DB instance identifier** – Type **tutorial-db-instance**.
   + **Master username** – Type **tutorial\_user**.
   + **Auto generate a password** – Leave the option turned off.
   + **Master password** – Type a password.
   + **Confirm password** – Retype the password.  
![The Settings section with tutorial-db-instance entered as the DB instance identifier and tutorial_user entered as the username. Auto generate a password is cleared, and both password fields contain a masked password.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Settings.png)

1. In the **Instance configuration** section, set these values:
   + **Burstable classes (includes t classes)**
   + **db.t3.micro**  
![The Instance configuration section with Burstable classes (includes t classes) selected for DB instance class and db.t3.micro chosen. The db.t3.micro class has 2 vCPUs and 1 GiB RAM.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_DB_instance_micro.png)

1. In the **Storage** section, keep the defaults.

1. In the **Connectivity** section, set these values and keep the other values as their defaults:
   + For **Compute resource**, choose **Connect to an EC2 compute resource**.
   + For **EC2 instance**, choose the EC2 instance you created previously, such as **tutorial-ec2-instance-web-server**.  
![The Connectivity section with Connect to an EC2 compute resource selected for Compute resource and tutorial-ec2-instance-web-server chosen for EC2 instance. A note explains that adding an EC2 compute resource automatically selects the VPC, DB subnet group, and public access settings, and adds VPC security groups to the database and the EC2 instance.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Connectivity.png)

1. In the **Database authentication** section, make sure **Password authentication** is selected.

1. Open the **Additional configuration** section, and enter **sample** for **Initial database name**. Keep the default settings for the other options.

1. To create your MySQL DB instance, choose **Create database**.

   Your new DB instance appears in the **Databases** list with the status **Creating**.

1. Wait for the **Status** of your new DB instance to show as **Available**. Then choose the DB instance name to show its details.

1. In the **Connectivity & security** section, view the **Endpoint** and **Port** of the DB instance.  
![The details page for tutorial-db-instance with the Connectivity & security tab open, showing the Endpoint and Port values, which are circled in red for the purposes of the illustration. The port is 3306.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Endpoint_Port.png)

   Note the endpoint and port for your DB instance. You use this information to connect your web server to your DB instance.

1. Complete [Install a web server on your EC2 instance](CHAP_Tutorials.WebServerDB.CreateWebServer.md).

------
#### [ RDS for PostgreSQL ]

**To create a PostgreSQL DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the AWS Management Console, check the AWS Region. It should be the same as the one where you created your EC2 instance.

1. In the navigation pane, choose **Databases**.

1. Choose **Create database**.

1. On the **Create database** page, choose **Standard create**.

1. For **Engine options**, choose **PostgreSQL**.  
![The Engine options section with PostgreSQL selected as the engine type. The other engine types shown are Aurora (MySQL Compatible), Aurora (PostgreSQL Compatible), MySQL, MariaDB, Oracle, Microsoft SQL Server, and IBM Db2.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/tutorial-create-postgres.png)

1. For **Templates**, choose **Free tier** or **Sandbox**. **Free tier** appears for free plan accounts. **Sandbox** appears for paid plan accounts.  
![The Templates section with Free tier selected. The other templates shown are Production and Dev/Test.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/tutorial-create-template.png)

1. In the **Availability and durability** section, keep the defaults.

1. In the **Settings** section, set these values:
   + **DB instance identifier** – Type **tutorial-db-instance**.
   + **Master username** – Type **tutorial\_user**.
   + **Auto generate a password** – Leave the option turned off.
   + **Master password** – Type a password.
   + **Confirm password** – Retype the password.  
![The Settings section with tutorial-db-instance entered as the DB instance identifier and tutorial_user entered as the username. Auto generate a password is cleared, and both password fields contain a masked password.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Settings.png)

1. In the **Instance configuration** section, set these values:
   + **Burstable classes (includes t classes)**
   + **db.t3.micro**  
![The Instance configuration section with Burstable classes (includes t classes) selected for DB instance class and db.t3.micro chosen. The db.t3.micro class has 2 vCPUs and 1 GiB RAM.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_DB_instance_micro.png)

1. In the **Storage** section, keep the defaults.

1. In the **Connectivity** section, set these values and keep the other values as their defaults:
   + For **Compute resource**, choose **Connect to an EC2 compute resource**.
   + For **EC2 instance**, choose the EC2 instance you created previously, such as **tutorial-ec2-instance-web-server**.  
![The Connectivity section with Connect to an EC2 compute resource selected for Compute resource and tutorial-ec2-instance-web-server chosen for EC2 instance. A note explains that adding an EC2 compute resource automatically selects the VPC, DB subnet group, and public access settings, and adds VPC security groups to the database and the EC2 instance.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Connectivity.png)

1. In the **Database authentication** section, make sure **Password authentication** is selected.

1. Open the **Additional configuration** section, and enter **sample** for **Initial database name**. Keep the default settings for the other options.

1. To create your PostgreSQL DB instance, choose **Create database**.

   Your new DB instance appears in the **Databases** list with the status **Creating**.

1. Wait for the **Status** of your new DB instance to show as **Available**. Then choose the DB instance name to show its details.

1. In the **Connectivity & security** section, view the **Endpoint** and **Port** of the DB instance.  
![The details page for tutorial-db-instance with the Connectivity & security tab open, showing the Endpoint and Port values, which are circled in red for the purposes of the illustration. The port is 5432.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Tutorial_WebServer_Endpoint_Port_postgres.png)

   Note the endpoint and port for your DB instance. You use this information to connect your web server to your DB instance.

1. Complete [Install a web server on your EC2 instance](CHAP_Tutorials.WebServerDB.CreateWebServer.md).

------