# Storing passwords in the AWS Schema Conversion Tool

You can store a database password or SSL certificate in the AWS SCT cache. To store a
password, choose **Store Password** when you create a connection.

The password is encrypted using the randomly generated token in the
`seed.dat` file. The password is then stored with the user name in the
cache file. If you lose the `seed.dat` file or it becomes corrupted, the
database password might be unencrypted incorrectly. In this case, the connection fails.
