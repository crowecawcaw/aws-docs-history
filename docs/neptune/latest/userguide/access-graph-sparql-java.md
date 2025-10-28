# Using Java to connect to a Neptune DB

instance

This section walks you through the running of a complete Java sample that connects to an
Amazon Neptune DB instance and performs a SPARQL query.

Follow these instructions from an Amazon EC2 instance in the same virtual private cloud (VPC) as
your Neptune DB instance.

###### To connect to Neptune using Java

1. Install Apache Maven on your EC2 instance. If using Amazon Linux 2023 (preferred), use:

```
sudo dnf update -y
sudo dnf install maven -y
```

If using Amazon Linux 2, download the latest binary from [https://maven.apache.org/download.cgi:](https://maven.apache.org/download.cgi: "https://maven.apache.org/download.cgi:")

```
sudo yum remove maven -y
wget https://dlcdn.apache.org/maven/maven-3/ <version>/binaries/apache-maven-<version>-bin.tar.gz
sudo tar -xzf apache-maven-<version>-bin.tar.gz -C /opt/
sudo ln -sf /opt/apache-maven-<version> /opt/maven
echo 'export MAVEN_HOME=/opt/maven' >> ~/.bashrc
echo 'export PATH=$MAVEN_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

2. This example was tested with Java 8 only. Enter the following to install Java 8 on your
   EC2 instance:

```
sudo yum install java-1.8.0-devel
```

3. Enter the following to set Java 8 as the default runtime on your EC2 instance:

```
sudo /usr/sbin/alternatives --config java
```

When prompted, enter the number for Java 8. 4. Enter the following to set Java 8 as the default compiler on your EC2 instance:

```
sudo /usr/sbin/alternatives --config javac
```

When prompted, enter the number for Java 8. 5. In a new directory, create a `pom.xml` file, and then open it in a
text editor. 6. Copy the following into the `pom.xml` file and save it
(you can usually adjust the version numbers to the latest stable version):

```
<project xmlns="https://maven.apache.org/POM/4.0.0" xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="https://maven.apache.org/POM/4.0.0 https://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.amazonaws</groupId>
  <artifactId>RDFExample</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>RDFExample</name>
  <url>https://maven.apache.org</url>
  <dependencies>
    `<dependency>
 <groupId>org.eclipse.rdf4j</groupId>
 <artifactId>rdf4j-runtime</artifactId>
 <version>3.6</version>
 </dependency>`
  </dependencies>
  <build>
    <plugins>
      <plugin>
          <groupId>org.codehaus.mojo</groupId>
          <artifactId>exec-maven-plugin</artifactId>
          <version>1.2.1</version>
          <configuration>
            <mainClass>com.amazonaws.App</mainClass>
          </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

###### Note

If you are modifying an existing Maven project, the required dependency is
highlighted in the preceding code. 7. To create subdirectories for the example source code
(`src/main/java/com/amazonaws/`), enter the following at the command
line:

```
mkdir -p `src/main/java/com/amazonaws/`
```

8. In the `src/main/java/com/amazonaws/` directory, create a file
   named `App.java`, and then open it in a text editor.
9. Copy the following into the `App.java` file. Replace
   `your-neptune-endpoint` with the address of your
   Neptune DB instance.

###### Note

For information about finding the hostname of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section.

```
package com.amazonaws;

import org.eclipse.rdf4j.repository.Repository;
import org.eclipse.rdf4j.repository.http.HTTPRepository;
import org.eclipse.rdf4j.repository.sparql.SPARQLRepository;

import java.util.List;
import org.eclipse.rdf4j.RDF4JException;
import org.eclipse.rdf4j.repository.RepositoryConnection;
import org.eclipse.rdf4j.query.TupleQuery;
import org.eclipse.rdf4j.query.TupleQueryResult;
import org.eclipse.rdf4j.query.BindingSet;
import org.eclipse.rdf4j.query.QueryLanguage;
import org.eclipse.rdf4j.model.Value;

public class App
{
    public static void main( String[] args )
    {
        String sparqlEndpoint = "https://`your-neptune-endpoint`:`port`/sparql";
        Repository repo = new SPARQLRepository(sparqlEndpoint);
        repo.initialize();

        try (RepositoryConnection conn = repo.getConnection()) {
           String queryString = "SELECT ?s ?p ?o WHERE { ?s ?p ?o } limit 10";

           TupleQuery tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString);

           try (TupleQueryResult result = tupleQuery.evaluate()) {
              while (result.hasNext()) {  // iterate over the result
                   BindingSet bindingSet = result.next();

                   Value s = bindingSet.getValue("s");
                   Value p = bindingSet.getValue("p");
                   Value o = bindingSet.getValue("o");

                   System.out.print(s);
                   System.out.print("\t");
                   System.out.print(p);
                   System.out.print("\t");
                   System.out.println(o);
              }
           }
        }
    }
}
```

10. Use the following Maven command to compile and run the sample:

```
mvn compile exec:java
```

The preceding example returns up to 10 of the triples (subject-predicate-object) in the
graph by using the `?s ?p ?o` query with a limit of 10. To query for something
else, replace the query with another SPARQL query.

The iteration of the results in the example prints the value of each variable returned.
The `Value` object is converted to a `String` and then printed. If you
change the `SELECT` part of the query, you must modify the code.
