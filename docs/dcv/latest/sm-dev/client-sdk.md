# Step 1: Generate your API client

The Session Manager APIs are defined in a single YAML file. The APIs are based on the OpenAPI3.0 specification,
which defines a standard, language-agnostic interface to RESTful APIs. For more information, see
[OpenAPI Specification](https://swagger.io/specification/ "https://swagger.io/specification/").

Using the YAML file, you can generate API client in one of the supported languages. To do this, you
must use Swagger Codegen 3.0 or later. For more information about the supported languages, see the
[swagger-codegen repo](https://github.com/swagger-api/swagger-codegen#overview "https://github.com/swagger-api/swagger-codegen#overview").

###### To generate the API client

1. Download the Session Manager API YAML file from the Session Manager Broker. The YAML file is available at the following URL.

```
https://`broker_host_ip`:`port`/dcv-session-manager-api.yaml
```

2. Install Swagger Codegen.
   - macOS

   ```
   `$` brew install swagger-codegen
   ```

   - Other platforms

   ```
   `$` git clone https://github.com/swagger-api/swagger-codegen --branch 3.0.0
   ```

   ```
   `$` cd swagger-codegen
   ```

3. Generate the API client.
   - macOS

   ```
   `$` swagger-codegen generate -i `/path_to/yaml_file` -l `language` -o $`output_folder`
   ```

   - Other platforms

   ```
   `$` mvn clean package
   ```

   ```
   `$` java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i `/path_to/yaml_file` -l `language` -o `output_folder`
   ```
