# Using a Cassandra Perl client driver to

access Amazon Keyspaces programmatically

This section shows you how to connect to Amazon Keyspaces by using a Perl client driver. For
this code sample, we used Perl 5. Amazon Keyspaces requires the use of Transport Layer Security
(TLS) to help secure connections with clients.

###### Important

Amazon Keyspacescertificates are transitioning to the Amazon Trust Services (ATS) hierarchy.
Ensure your environment trusts the Amazon Root CAs 1–4 to avoid connection errors during this rotation.
The Perl driver doesn't validate the server's Amazon SSL certificate, which means
that you can't confirm that you are connecting to Amazon Keyspaces. The second step, to configure the
driver to use TLS when connecting to Amazon Keyspaces is still required, and ensures that data
transferred between the client and server is encrypted.

1. Download the Cassandra DBI driver from [https://metacpan.org/pod/DBD::Cassandra](https://metacpan.org/pod/DBD::Cassandra "https://metacpan.org/pod/DBD::Cassandra") and install the driver to
   your Perl environment. The exact steps depend on the environment. The following
   is a common example.

```
cpanm DBD::Cassandra
```

2. Create a file for your application.

```
touch cqlapp.pl
```

3. Add the following sample code to the cqlapp.pl file.

```
use DBI;
my $user = "`ServiceUserName`";
my $password = "`ServicePassword`";
my $db = DBI->connect("dbi:Cassandra:host=`cassandra.us-east-2.amazonaws.com`;port=9142;tls=1;",
$user, $password);

my $rows = $db->selectall_arrayref("select * from system_schema.keyspaces");
print "Found the following Keyspaces...\n";
for my $row (@$rows) {
      print join(" ",@$row['keyspace_name']),"\n";
}

$db->disconnect;
```

###### Important

Ensure that the `ServiceUserName` and
`ServicePassword` match the user
name and password you obtained when you generated the
service-specific credentials by following the steps to [Create service-specific
credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md").

###### Note

For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md"). 4. Run the application.

```
perl cqlapp.pl
```
