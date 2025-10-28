# Using a Cassandra .NET Core client driver to

access Amazon Keyspaces programmatically

This section shows you how to connect to Amazon Keyspaces by using a .NET Core client driver. The
setup steps will vary depending on your environment and operating system, you might have
to modify them accordingly. Amazon Keyspaces requires the use of Transport Layer Security (TLS) to
help secure connections with clients. To connect to Amazon Keyspaces using TLS,
configure your driver to use the system trust store, which includes the Amazon Root CAs
1-4.

1. Install the CassandraCSharpDriver through nuget, using the nuget console.

```
PM> Install-Package CassandraCSharpDriver
```

2. The following example uses a .NET Core C# console project to connect to Amazon Keyspaces
   and run a query.

```
using Cassandra;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Security;
using System.Runtime.ConstrainedExecution;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace CSharpKeyspacesExample
{
    class Program
    {
        public Program(){}

        static void Main(string[] args)
        {
            var userName = "`ServiceUserName`";
            var pwd = "`ServicePassword`";
            certCollection.Add(amazoncert);

            var awsEndpoint =  "`cassandra.us-east-2.amazonaws.com`" ;

            var cluster = Cluster.Builder()
                     .AddContactPoints(awsEndpoint)
                     .WithPort(9142)
                     .WithAuthProvider(new PlainTextAuthProvider(userName, pwd))
                     .WithSSL(new SSLOptions().SetCertificateCollection(certCollection))
                     .Build();

            var session = cluster.Connect();
            var rs = session.Execute("SELECT * FROM system_schema.tables;");
            foreach (var row in rs)
            {
                var name = row.GetValue<String>("keyspace_name");
                Console.WriteLine(name);
            }
        }
    }
}

```

Usage notes:

1. Ensure that you use the default system trust store, which includes the Amazon Root CAs
   1-4.
2. Ensure that the `ServiceUserName` and
   `ServicePassword` match the user
   name and password you obtained when you generated the
   service-specific credentials by following the steps to [Create service-specific
   credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md").
3. For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").
