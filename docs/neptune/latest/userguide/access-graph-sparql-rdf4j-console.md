# Using the RDF4J console to connect to a

Neptune DB instance

The RDF4J Console allows you to experiment with Resource Description Framework (RDF)
graphs and queries in a REPL (read-eval-print loop) environment.

You can add a remote graph database as a repository and query it from the RDF4J Console.
This section walks you through the configuration of the RDF4J Console to connect remotely to a
Neptune DB instance.

###### To connect to Neptune using the RDF4J Console

1. Download the RDF4J SDK from the [Download
   page](http://rdf4j.org/download/ "http://rdf4j.org/download/") on the RDF4J website.
2. Unzip the RDF4J SDK zip file.
3. In a terminal, navigate to the RDF4J SDK directory, and then enter the following command
   to run the RDF4J Console:

```
bin/console.sh
```

You should see output similar to the following:

```
14:11:51.126 [main] DEBUG o.e.r.c.platform.PlatformFactory - os.name = linux
14:11:51.130 [main] DEBUG o.e.r.c.platform.PlatformFactory - Detected Posix platform
Connected to default data directory
RDF4J Console 3.6.1

3.6.1
Type 'help' for help.
>
```

You are now at the `>` prompt. This is the general prompt for the RDF4J
Console. You use this prompt for setting up repositories and other operations. A
repository has its own prompt for running queries. 4. At the `>` prompt, enter the following to create a SPARQL repository for
your Neptune DB instance:

```
create sparql
```

5. The RDF4J Console prompts you for values for the variables required to connect to the
   SPARQL endpoint.

```
Please specify values for the following variables:
```

Specify the following values:

| Variable Name                                            | Value                                           |
| -------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPARQL query endpoint                                    | `https://`your-neptune-endpoint`:`port`/sparql` |
| SPARQL update endpoint                                   | `https://`your-neptune-endpoint`:`port`/sparql` |
| Local repository ID [endpoint@localhost]                 | `neptune`                                       |
| Repository title [SPARQL endpoint repository @localhost] | `Neptune DB instance`                           | For information about finding the address of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section. If the operation is successful, you see the following message: `Repository created` 6. At the `>` prompt, enter the following to connect to the Neptune DB instance: `open neptune` If the operation is successful, you see the following message: `Opened repository 'neptune'` You are now at the `neptune>` prompt. At this prompt, you can run queries against the Neptune graph. ###### Note Now that you have added the repository, the next time you run `bin/console.sh`, you can immediately run the `open neptune` command to connect to the Neptune DB instance. 7. At the `neptune>` prompt, enter the following to run a SPARQL query that returns up to 10 of the triples (subject-predicate-object) in the graph by using the `?s ?p ?o` query with a limit of 10. To query for something else, replace the text after the `sparql` command with another SPARQL query. `sparql select ?s ?p ?o where {?s ?p ?o} limit 10` |
