

# Setting up an SSL connection over JDBC
<a name="Appendix.Oracle.Options.SSL.JDBC"></a>

To use an SSL connection over JDBC, you must create a keystore, trust the Amazon RDS root CA certificate, and use the code snippet specified following.

For more information about creating the keystore, see the [Creating a keystore](https://docs.oracle.com/en/database/oracle/oracle-database/19/jjdbc/client-side-security.html) in the Oracle documentation. For reference information, see [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/keytool.html) in the *Java Platform, Standard Edition Tools Reference*.

```
keytool -genkey -alias {{client}} -validity {{365}} -keyalg {{RSA}} -keystore {{clientkeystore}}         
```

Take the following steps to trust the Amazon RDS root CA certificate.

**To trust the Amazon RDS root CA certificate**

1. Download the certificate bundle .pem file that works for all AWS Regions and put the file in the ssl\_wallet directory.

   For information about downloading certificates, see [Using SSL/TLS to encrypt a connection to a DB instance or cluster ](UsingWithRDS.SSL.md).

1. Extract each certificate in the .pem file into a separate file using an OS utility.

1. Convert each certificate to .der format using a separate `openssl` command, replacing {{certificate-pem-file}} with the name of the certificate .pem file (without the .pem extension).

   ```
   openssl x509 -outform der -in {{certificate-pem-file}}.pem -out {{certificate-pem-file}}.der                
   ```

1. Import each certificate into the keystore using the following command.

   ```
   keytool -import -alias rds-root -keystore {{clientkeystore.jks}} -file {{certificate-pem-file}}.der                
   ```

   For more information, see [Rotating your SSL/TLS certificate](UsingWithRDS.SSL-certificate-rotation.md).

1. Confirm that the key store was created successfully.

   ```
   keytool -list -v -keystore {{clientkeystore.jks}}                                            
   ```

   Enter the keystore password when you are prompted for it.

The following code example shows how to set up the SSL connection using JDBC.

```
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;
 
public class OracleSslConnectionTest {
    private static final String DB_SERVER_NAME = "{{dns-name-provided-by-amazon-rds}}";
    private static final String SSL_PORT = "{{ssl-option-port-configured-in-option-group}}";
    private static final String DB_SID = "{{oracle-sid}}";
    private static final String DB_USER = "{{user-name}}";
    private static final String DB_PASSWORD = "{{password}}";
    // This key store has only the prod root ca.
    private static final String KEY_STORE_FILE_PATH = "{{file-path-to-keystore}}";
    private static final String KEY_STORE_PASS = "{{keystore-password}}";
 
    public static void main(String[] args) throws SQLException {
        final Properties properties = new Properties();
        final String connectionString = String.format(
                "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCPS)(HOST=%s)(PORT=%s))(CONNECT_DATA=(SID=%s)))",
                DB_SERVER_NAME, SSL_PORT, DB_SID);
        properties.put("user", DB_USER);
        properties.put("password", DB_PASSWORD);
        properties.put("oracle.jdbc.J2EE13Compliant", "true");
        properties.put("javax.net.ssl.trustStore", KEY_STORE_FILE_PATH);
        properties.put("javax.net.ssl.trustStoreType", "JKS");
        properties.put("javax.net.ssl.trustStorePassword", KEY_STORE_PASS);
        final Connection connection = DriverManager.getConnection(connectionString, properties);
        // If no exception, that means handshake has passed, and an SSL connection can be opened
    }
}
```

**Note**  
Specify a password other than the prompt shown here as a security best practice.