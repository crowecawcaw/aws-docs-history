# AWS Glue Scala ScalarNode APIs

###### Topics

- [ScalarNode class](#glue-etl-scala-apis-glue-types-scalarnode-class "#glue-etl-scala-apis-glue-types-scalarnode-class")
- [ScalarNode object](#glue-etl-scala-apis-glue-types-scalarnode-object "#glue-etl-scala-apis-glue-types-scalarnode-object")
  **Package: com.amazonaws.services.glue.types**

## ScalarNode class

**ScalarNode**

```
class ScalarNode extends DynamicNode  (
           value : Any,
           scalarType : TypeCode )
```

### ScalarNode def methods

```
def compare( other : Any,
             operator : String
           ) : Boolean
```

```
def getValue
```

```
def hashCode : Int
```

```
def nodeType
```

```
def toJson
```

## ScalarNode object

**ScalarNode**

```
object ScalarNode
```

### ScalarNode def methods

```
def apply( v : Any ) : DynamicNode
```

```
def compare( tv : Ordered[T],
             other : T,
             operator : String
           ) : Boolean
```

```
def compareAny( v : Any,
                y : Any,
                o : String )
```

```
def withEscapedSpecialCharacters( jsonToEscape : String ) : String
```
