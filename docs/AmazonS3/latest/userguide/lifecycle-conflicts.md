# How Amazon S3 handles conflicts in lifecycle configurations

Generally, Amazon S3 Lifecycle optimizes for cost. For example, if two expiration policies overlap, the shorter expiration policy is honored so that data is not stored for longer than expected. Likewise, if two transition policies overlap, S3 Lifecycle transitions your objects to the lower-cost storage class.

In both cases, S3 Lifecycle tries to choose the path that is least expensive for you. An exception to this general rule is with the S3 Intelligent-Tiering storage class. S3 Intelligent-Tiering is favored by S3 Lifecycle over any storage class, aside from the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes.

When you have multiple rules in an S3 Lifecycle configuration, an object can become
 eligible for multiple S3 Lifecycle actions on the same day. In such cases, Amazon S3
 follows these general rules:


* Permanent deletion takes precedence over transition.
* Transition takes precedence over creation of [delete markers](DeleteMarker.md "DeleteMarker.md").
* When an object is eligible for both an S3 Glacier Flexible Retrieval and an
 S3 Standard-IA (or an S3 One Zone-IA) transition, Amazon S3 chooses the
 S3 Glacier Flexible Retrieval transition.

## Examples of overlapping filters and
 conflicting lifecycle actions


You might specify an S3 Lifecycle configuration in which you specify overlapping
 prefixes, or actions. The following examples show how Amazon S3 resolves potential conflicts.


###### Example 1: Overlapping prefixes (no conflict)

The following example configuration has two rules that specify overlapping
 prefixes as follows:


* The first rule specifies an empty filter, indicating all objects in the
 bucket.
* The second rule specifies a key name prefix (`logs/`),
 indicating only a subset of objects.
Rule 1 requests Amazon S3 to delete all objects one year after creation. Rule 2
 requests Amazon S3 to transition a subset of objects to the S3 Standard-IA storage class
 30 days after creation.


```
<LifecycleConfiguration>
  <Rule>
    <ID>Rule 1</ID>
    <Filter>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>365</Days>
    </Expiration>
  </Rule>
  <Rule>
    <ID>Rule 2</ID>
    <Filter>
      <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <StorageClass>STANDARD_IA</StorageClass>
      <Days>30</Days>
    </Transition>
   </Rule>
</LifecycleConfiguration>
```
Since there is no conflict in this case, Amazon S3 will transition the objects with the
 `logs/` prefix to the S3 Standard-IA storage class 30 days after creation.
 When any object reaches one year after creation, it will be deleted.


###### Example 2: Conflicting lifecycle actions

In this example configuration, there are two rules that direct Amazon S3 to perform two
 different actions on the same set of objects at the same time in the objects'
 lifetime:


* Both rules specify the same key name prefix, so both rules apply to the
 same set of objects.
* Both rules specify the same 365 days after object creation when the rules
 apply.
* One rule directs Amazon S3 to transition objects to the S3 Standard-IA storage
 class and another rule wants Amazon S3 to expire the objects at the same
 time.

```
<LifecycleConfiguration>
  <Rule>
    <ID>Rule 1</ID>
    <Filter>
      <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>365</Days>
    </Expiration>        
  </Rule>
  <Rule>
    <ID>Rule 2</ID>
    <Filter>
      <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <StorageClass>STANDARD_IA</StorageClass>
      <Days>365</Days>
    </Transition>
   </Rule>
</LifecycleConfiguration>
```
In this case, because you want objects to expire (to be removed), there is no
 point in changing the storage class, so Amazon S3 chooses the expiration action on these
 objects.


###### Example 3: Overlapping prefixes resulting in conflicting lifecycle actions

In this example, the configuration has two rules, which specify overlapping
 prefixes as follows:


* Rule 1 specifies an empty prefix (indicating all objects).
* Rule 2 specifies a key name prefix (`logs/`) that identifies a
 subset of all objects.
For the subset of objects with the `logs/` key name prefix, S3 Lifecycle
 actions in both rules apply. One rule directs Amazon S3 to transition objects 10 days
 after creation, and another rule directs Amazon S3 to transition objects 365 days after
 creation. 


```
<LifecycleConfiguration>
  <Rule>
    <ID>Rule 1</ID>
    <Filter>
      <Prefix></Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <StorageClass>STANDARD_IA</StorageClass>
      <Days>10</Days> 
    </Transition>
  </Rule>
  <Rule>
    <ID>Rule 2</ID>
    <Filter>
      <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <StorageClass>STANDARD_IA</StorageClass>
      <Days>365</Days> 
    </Transition>
   </Rule>
</LifecycleConfiguration>
```
In this case, Amazon S3 chooses to transition them 10 days after creation. 


###### Example 4: Tag-based filtering and resulting conflicting lifecycle actions

Suppose that you have the following S3 Lifecycle configuration that has two rules, each
 specifying a tag filter:


* Rule 1 specifies a tag-based filter (`tag1/value1`). This rule
 directs Amazon S3 to transition objects to the S3 Glacier Flexible Retrieval storage
 class 365 days after creation.
* Rule 2 specifies a tag-based filter (`tag2/value2`). This rule
 directs Amazon S3 to expire objects 14 days after creation.
The S3 Lifecycle configuration is shown in following example.


```
<LifecycleConfiguration>
  <Rule>
    <ID>Rule 1</ID>
    <Filter>
      <Tag>
         <Key>tag1</Key>
         <Value>value1</Value>
      </Tag>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <StorageClass>GLACIER</StorageClass>
      <Days>365</Days> 
    </Transition>
  </Rule>
  <Rule>
    <ID>Rule 2</ID>
    <Filter>
      <Tag>
         <Key>tag2</Key>
         <Value>value2</Value>
      </Tag>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>14</Days> 
    </Expiration>
   </Rule>
</LifecycleConfiguration>
```
If an object has both tags, then Amazon S3 has to decide which rule to follow. In this
 case, Amazon S3 expires the object 14 days after creation. The object is removed, and
 therefore the transition action does not apply.
