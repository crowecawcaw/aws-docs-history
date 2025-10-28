# Uninstalling older versions

Uninstalling the AWS Data Provider for SAP does not require SAP downtime and can be done online. The only impact will be a gap in metric monitoring information for the time that the DataProvider was installed on your system.

## Uninstall DataProvider 3.0

**Linux**

1. Log in to Linux as a superuser, like root.
2. Stop and remove the DataProvider using the following command.

**SLES**

```
zypper remove -y aws-sap-dataprovider
```

**RHEL/OEL**

```
yum -y erase aws-sap-dataprovider
```

**Windows**

```
“C:\Program Files\Amazon\DataProvider\uninstall.exe“
```

## Uninstall DataProvider 2.0

**Linux**

1. Log in to Linux as a superuser, like root.
2. Stop and remove the DataProvider using the following command.

```
/usr/local/ec2/aws-agent/bin/aws-agent_uninstall
```

**Windows**

```
“C:\Program Files\Amazon\DataProvider\uninstall.exe“
```
