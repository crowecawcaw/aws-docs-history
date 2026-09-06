

# AWS Glue Scala ScalarNode APIs
<a name="glue-etl-scala-apis-glue-types-scalarnode"></a>

**Topics**
+ [ScalarNode class](#glue-etl-scala-apis-glue-types-scalarnode-class)
+ [ScalarNode object](#glue-etl-scala-apis-glue-types-scalarnode-object)

**Package: com.amazonaws.services.glue.types**

## ScalarNode class
<a name="glue-etl-scala-apis-glue-types-scalarnode-class"></a>

**ScalarNode**

```
class ScalarNode extends DynamicNode  (
           value : Any,
           scalarType : TypeCode )
```

### ScalarNode def methods
<a name="glue-etl-scala-apis-glue-types-scalarnode-class-defs"></a>

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
<a name="glue-etl-scala-apis-glue-types-scalarnode-object"></a>

 **ScalarNode**

```
object ScalarNode
```

### ScalarNode def methods
<a name="glue-etl-scala-apis-glue-types-scalarnode-object-defs"></a>

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