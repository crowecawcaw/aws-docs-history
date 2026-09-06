

# AWS Glue Scala ChoiceOption APIs
<a name="glue-etl-scala-apis-glue-choiceoption"></a>

**Topics**
+ [ChoiceOption trait](#glue-etl-scala-apis-glue-choiceoption-trait)
+ [ChoiceOption object](#glue-etl-scala-apis-glue-choiceoption-object)
+ [Case class ChoiceOptionWithResolver](#glue-etl-scala-apis-glue-choiceoptionwithresolver-case-class)
+ [Case class MatchCatalogSchemaChoiceOption](#glue-etl-scala-apis-glue-matchcatalogschemachoiceoption-case-class)

**Package: com.amazonaws.services.glue**

## ChoiceOption trait
<a name="glue-etl-scala-apis-glue-choiceoption-trait"></a>

```
trait ChoiceOption extends Serializable 
```

## ChoiceOption object
<a name="glue-etl-scala-apis-glue-choiceoption-object"></a>

 **ChoiceOption**

```
object ChoiceOption
```

A general strategy to resolve choice applicable to all `ChoiceType` nodes in a `DynamicFrame`.
+ `val CAST`
+ `val MAKE_COLS`
+ `val MAKE_STRUCT`
+ `val MATCH_CATALOG`
+ `val PROJECT`

### Def apply
<a name="glue-etl-scala-apis-glue-choiceoption-object-def-apply"></a>

```
def apply(choice: String): ChoiceOption
```



## Case class ChoiceOptionWithResolver
<a name="glue-etl-scala-apis-glue-choiceoptionwithresolver-case-class"></a>

```
case class ChoiceOptionWithResolver(name: String, choiceResolver: ChoiceResolver) extends ChoiceOption {}
```



## Case class MatchCatalogSchemaChoiceOption
<a name="glue-etl-scala-apis-glue-matchcatalogschemachoiceoption-case-class"></a>

```
case class MatchCatalogSchemaChoiceOption() extends ChoiceOption {}
```

