# Adding an Amazon RDS DB instance to your .NET application

environment

This topic provides instructions to create an Amazon RDS using the Elastic Beanstalk console.
You can use an Amazon Relational Database Service (Amazon RDS) DB instance to store data gathered and modified by your
application. The database can be coupled to your environment and managed by Elastic Beanstalk, or it can be created as decoupled
and managed externally by another service.
In these instructions the database is coupled to your environment and managed by Elastic Beanstalk. For more information about integrating an Amazon RDS with
Elastic Beanstalk, see [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md").

###### Sections

- [Adding a DB instance to your environment](#dotnet-rds-create "#dotnet-rds-create")
- [Downloading a driver](#dotnet-rds-drivers "#dotnet-rds-drivers")
- [Connecting to a database](#dotnet-rds-connect "#dotnet-rds-connect")

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

| Property name  | Description                                                                                    | Property value                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `RDS_HOSTNAME` | The hostname of the DB instance.                                                               | On the **Connectivity & security\*<br>• tab on the Amazon RDS console: **Endpoint\*\*. |
| `RDS_PORT`     | The port where the DB instance accepts connections. The default value varies among DB engines. | On the **Connectivity & security\*<br>• tab on the Amazon RDS console: **Port\*\*.     |
| `RDS_DB_NAME`  | The database name, `ebdb`.                                                                     | On the **Configuration\*<br>• tab on the Amazon RDS console: **DB Name\*\*.            |
| `RDS_USERNAME` | The username that you configured for your database.                                            | On the **Configuration\*<br>• tab on the Amazon RDS console: **Master username\*\*.    |
| `RDS_PASSWORD` | The password that you configured for your database.                                            | Not available for reference in the Amazon RDS console.                                 |

For more information about configuring a database instance coupled with an Elastic Beanstalk environment,
see [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md").

## Downloading a driver

Download and install the `EntityFramework` package and a database driver for
your development environment with `NuGet`.

###### Common entity framework database providers for .NET

- **SQL Server** –
  `Microsoft.EntityFrameworkCore.SqlServer`
- **MySQL** –
  `Pomelo.EntityFrameworkCore.MySql`
- **PostgreSQL** –
  `Npgsql.EntityFrameworkCore.PostgreSQL`

## Connecting to a database

Elastic Beanstalk provides connection information for attached DB instances in environment properties.
Use `ConfigurationManager.AppSettings` to read the properties and configure a
database connection.

###### Example Helpers.cs - connection string method

```
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Web;

namespace MVC5App.Models
{
  public class Helpers
  {
    public static string GetRDSConnectionString()
    {
      var appConfig = ConfigurationManager.AppSettings;

      string dbname = appConfig["RDS_DB_NAME"];

      if (string.IsNullOrEmpty(dbname)) return null;

      string username = appConfig["RDS_USERNAME"];
      string password = appConfig["RDS_PASSWORD"];
      string hostname = appConfig["RDS_HOSTNAME"];
      string port = appConfig["RDS_PORT"];

      return "Data Source=" + hostname + ";Initial Catalog=" + dbname + ";User ID=" + username + ";Password=" + password + ";";
    }
  }
}
```

Use the connection string to initialize your database context.

###### Example DBContext.cs

```
using System.Data.Entity;
using System.Security.Claims;
using System.Threading.Tasks;
using Microsoft.AspNet.Identity;
using Microsoft.AspNet.Identity.EntityFramework;

namespace MVC5App.Models
{
  public class RDSContext : DbContext
  {
    public RDSContext()
      : base(`GetRDSConnectionString()`)
    {
    }

    public static RDSContext Create()
    {
      return new RDSContext();
    }
  }
}
```
