# Creating linked servers with Teradata

To create a linked server with Teradata, run the following commands:

```
EXECUTE master.dbo.sp_addlinkedserver
    @server = N'`LinkedServer_NAME`',
    @srvproduct=N'',
    @provider=N'MSDASQL',
    @provstr=N'"PROVIDER=MSDASQL;DRIVER={Teradata Database ODBC Driver 17.20};
                DBCName=`Server`;UID=`user_name`;PWD=`user_password`;
                UseDataEncryption=`YES/NO`;SSLMODE=`PREFER/ALLOW/DISABLE`>;"',
    @catalog='`database`'
```

```
EXECUTE master.dbo.sp_addlinkedsrvlogin
    @rmtsrvname = N'`LinkedServer_NAME`',
    @locallogin = NULL ,
    @useself = N'False',
    @rmtuser = N'`user_name`',
    @rmtpassword = N'`user_password`'

```

An example of the the commands above are shown here:

```
EXECUTE master.dbo.sp_addlinkedserver
    @server = N'LinkedServerToTeradata',
    @srvproduct=N'',
    @provider=N'MSDASQL',
    @provstr=N'"PROVIDER=MSDASQL;DRIVER={Teradata Database ODBC Driver 17.20};
                DBCName=`my-teradata-test.cnetsipka.us-west-2.rds.amazonaws.com`;
                UID=master;
                PWD=`Test#1234`;
                UseDataEncryption=YES;
                SSLMODE=PREFER;"',
    @catalog='MyTestTeradataDB'

EXECUTE master.dbo.sp_addlinkedsrvlogin
    @rmtsrvname = N'LinkedServerToTeradata',
    @locallogin = NULL ,
    @useself = N'False',
    @rmtuser = N'master',
    @rmtpassword = N'`Test#1234`'

```

###### Note

Specify a password other than the prompt shown here as a security best practice.
