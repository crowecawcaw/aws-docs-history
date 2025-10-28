# SPARQL subject prediction example

_Subject prediction_ predicts the subject given a predicate and an object.

For example, the following query predicts who (of type `foaf:User`)
will watch a given movie:

```
SELECT * WHERE { ?input `(a `foaf:Movie`)` .
    SERVICE neptune-ml:inference {
        neptune-ml:config neptune-ml:modelType 'SUBJECT_PREDICTION' ;
                          neptune-ml:input ?input ;
                          neptune-ml:predicate <http://aws.amazon.com/neptune/csv2rdf/object_Property/rated> ;
                          neptune-ml:output ?output ;
                          neptune-ml:outputClass <http://aws.amazon.com/neptune/csv2rdf/class/User> ;        }
}
```
