# Maven troubleshooting

The following information might help you troubleshoot common issues with Maven and CodeArtifact.

## Disable parallel puts to fix error 429: Too Many Requests

Starting with version 3.9.0, Maven uploads package artifacts in parallel (up to 5 files at a time).
This can cause CodeArtifact to occassionally respond with an error response code 429 (Too Many Requests). If you
encounter this error, you can disable parallel puts to fix it.

To disable parallel puts, set the `aether.connector.basic.parallelPut` property to `false`
in your profile in your `settings.xml` file as shown by the following example:

```
<settings>
    <profiles>
        <profile>
            <id>default</id>
            <properties>
                <aether.connector.basic.parallelPut>false</aether.connector.basic.parallelPut>
            </properties>
        </profile>
    </profiles>
<settings>
```

For more information, see [Artifact Resolver Configuration Options](https://maven.apache.org/resolver/configuration.html "https://maven.apache.org/resolver/configuration.html") in the Maven documentation.
