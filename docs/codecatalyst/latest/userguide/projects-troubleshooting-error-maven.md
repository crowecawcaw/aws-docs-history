Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Java API with AWS Fargate blueprint

missing dependencies for **`apache-maven-3.8.6`**

**Issue:** For a project created from the
Java API with AWS Fargate blueprint, the workflow fails with an error for missing
`apache-maven-3.8.6` dependencies. The workflow fails with output similar
to the following example:

```
Step 8/25 : RUN wget https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz -P /tmp
---> Running in 1851ce6f4d1b
[91m--2023-03-10 01:24:55--  https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz
[0m[91mResolving dlcdn.apache.org (dlcdn.apache.org)...
[0m[91m151.101.2.132, 2a04:4e42::644
Connecting to dlcdn.apache.org (dlcdn.apache.org)|151.101.2.132|:443...
[0m[91mconnected.
[0m[91mHTTP request sent, awaiting response... [0m[91m404 Not Found
2023-03-10 01:24:55 ERROR 404: Not Found.
[0mThe command '/bin/sh -c wget https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz -P /tmp' returned a non-zero code: 8
[Container] 2023/03/10 01:24:55 Command failed with exit status 8
```

**Solution:** Update the blueprint Dockerfile using the
following steps.

1. In the search bar, enter `apache-maven-3.8.6` to locate the
   dockerfile inside the project created with the Java API with AWS Fargate
   blueprint.
2. Update the Dockerfile (`/static-assets/app/Dockerfile`) to use
   `maven:3.9.0-amazoncorretto-11` as a base image and remove the
   dependency on the `apache-maven-3.8.6` package.
3. (Recommended) We also recommend updating the Maven heap size to 6 GB.
   Below is an example Dockerfile.

```

FROM maven:3.9.0-amazoncorretto-11 AS builder

COPY ./pom.xml ./pom.xml
COPY src ./src/

ENV MAVEN_OPTS='-Xmx6g'

RUN mvn -Dmaven.test.skip=true clean package

FROM amazoncorretto:11-alpine

COPY —from=builder target/CustomerService-0.0.1.jar CustomerService-0.0.1.jar
EXPOSE 80
CMD ["java","-jar","-Dspring.profiles.active=prod","/CustomerService-0.0.1.jar", "—server.port=80"]
```
