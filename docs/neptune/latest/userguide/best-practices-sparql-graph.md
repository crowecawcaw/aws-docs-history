# Specifying a Named Graph for Load

Amazon Neptune associates every triple with a named graph. If you don't specify a named
graph when loading, inserting, or updating triples, Neptune uses the fallback named graph
defined by the URI, `http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`.

If you are using the Neptune bulk loader, you can specify the named graph to use
for all triples (or quads with the fourth position blank) by using the
`parserConfiguration: namedGraphUri` parameter. For information about the
Neptune loader `Load` command syntax, see [Neptune Loader Command](load-api-reference-load.md "load-api-reference-load.md").
