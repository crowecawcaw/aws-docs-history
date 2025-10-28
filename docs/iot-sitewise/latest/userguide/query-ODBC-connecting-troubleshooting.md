# Troubleshooting connection with the ODBC driver

###### Note

If the username and password is already specified in the DSN,
do not specify them again when the ODBC driver manager asks for them.

An error code of `01S02` with a message, `Re-writing `(connection
string option)` (have you specified it several times?)` occurs when a
connection string option is passed more than once in the connection string. Specifying an option
more than once raises an error. When making a connection with a DSN and a connection string, if
a connection option is already specified in the DSN, do not specify it again in the connection string.
