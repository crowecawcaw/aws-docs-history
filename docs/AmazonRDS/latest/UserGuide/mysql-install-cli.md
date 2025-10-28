# Installing the MySQL command-line client

Most Linux distributions include the MariaDB client instead of the Oracle MySQL
client. To install the MySQL command-line client on Amazon Linux 2023, run the following
command:

```
sudo dnf install mariadb105
```

To install the MySQL command-line client on Amazon Linux 2, run the following command:

```
sudo yum install mariadb
```

To install the MySQL command-line client on most DEB-based Linux distributions, run
the following command:

```
apt-get install mariadb-client
```

To check the version of your MySQL command-line client, run the following
command:

```
mysql --version
```

To read the MySQL documentation for your current client version, run the following
command:

```
man mysql
```
