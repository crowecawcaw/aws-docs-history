# Adding filters to Lifecycle rules

Filters are an optional Lifecyle rule element that you can use to specify which objects that the rule applies to.

The following elements can be used to filter objects:

**Key prefix**
You can filter objects based on a prefix. If you want to apply a lifecycle action to a subset of objects with different prefixes, create separate rules for each action.

**Object tags**
You can filter objects based on one or more tags. Each tag must match both the key and value exactly, and, if you specify multiple tags each tag key must be unique. A filter with multiple object tags applies to a subset of objects that has all the tags specified. If an object has additional tags specified, the filter will still apply.

###### Note

If you specify only a `Key` element and no `Value` element, the rule will apply only to objects that match the tag key and that do not have a value specified.

**Minimum or maximum object size**
You can filter objects based on size. You can specify a minimum size (`ObjectSizeGreaterThan`) or a maximum size (`ObjectSizeLessThan`), or you can specify a range of object sizes in the same filter. Object size values are in bytes. Maximum filter size is 5 TB. Amazon S3 applies a default minimum object size to lifecycle configuration. For more information, see [Example: Allowing objects smaller than 128 KB to be transitioned](lifecycle-configuration-examples.md#lc-small-objects "lifecycle-configuration-examples.md#lc-small-objects").

You can combine different filter elements in which case Amazon S3 uses a logical `AND`.

## Filter examples

The following examples show how you can use different filter elements:

- **Specifying a filter by using key prefixes**
  – This example shows an S3 Lifecycle rule that applies to a subset of
  objects based on the key name prefix (`logs/`). For example, the
  Lifecycle rule applies to the objects `logs/mylog.txt`,
  `logs/temp1.txt`, and `logs/test.txt`. The rule does
  not apply to the object `example.jpg`.

```
<LifecycleConfiguration>
    <Rule>
        <Filter>
           <Prefix>logs/</Prefix>
        </Filter>
        `transition/expiration actions`
         ...
    </Rule>
    ...
</LifecycleConfiguration>
```

###### Note

If you have one or more prefixes that start with the same characters, you can include all of those prefixes in your rule by specifying a partial prefix with no trailing slash (`/`) in the filter. For example, suppose that you have these prefixes:

```
sales1999/
                sales2000/
                sales2001/
```

To include all three prefixes in your rule, specify `sales` as the prefix in your lifecycle rule.

If you want to apply a lifecycle action to a subset of objects based on
different key name prefixes, specify separate rules. In each rule, specify a
prefix-based filter. For example, to describe a lifecycle action for objects
with the key prefixes `projectA/` and `projectB/`, you
specify two rules as follows:

```
<LifecycleConfiguration>
    <Rule>
        <Filter>
           <Prefix>projectA/</Prefix>
        </Filter>
        `transition/expiration actions`
         ...
    </Rule>

    <Rule>
        <Filter>
           <Prefix>projectB/</Prefix>
        </Filter>
        `transition/expiration actions`
         ...
    </Rule>
</LifecycleConfiguration>
```

For more information about object keys, see [Naming Amazon S3 objects](object-keys.md "object-keys.md").

- **Specifying a filter based on object tags**
  – In the following example, the Lifecycle rule specifies a filter based on
  a tag (`key`) and value
  (`value`). The rule then applies
  only to a subset of objects with the specific tag.

```
<LifecycleConfiguration>
    <Rule>
        <Filter>
           <Tag>
              <Key>`key`</Key>
              <Value>`value`</Value>
           </Tag>
        </Filter>
        `transition/expiration actions`
        ...
    </Rule>
</LifecycleConfiguration>
```

You can specify a filter based on multiple tags. You must wrap the tags in the
`<And>` element, as shown in the following example. The
rule directs Amazon S3 to perform lifecycle actions on objects with two tags (with
the specific tag key and value).

```
<LifecycleConfiguration>
    <Rule>
      <Filter>
         <And>
            <Tag>
               <Key>`key1`</Key>
               <Value>`value1`</Value>
            </Tag>
            <Tag>
               <Key>`key2`</Key>
               <Value>`value2`</Value>
            </Tag>
             ...
          </And>
      </Filter>
      `transition/expiration actions`
    </Rule>
</Lifecycle>
```

The Lifecycle rule applies to objects that have both of the tags specified.
Amazon S3 performs a logical `AND`. Note the following:

    + Each tag must match *both* the key
     and value exactly. If you specify only a `<Key>` element
     and no `<Value>` element, the rule will apply only to
     objects that match the tag key and that do *not* have a value specified.
    + The rule applies to a subset of objects that has all the tags
     specified in the rule. If an object has additional tags specified, the
     rule will still
     apply.

###### Note

When you specify multiple tags in a filter, each tag key must be
unique.

- **Specifying a filter based on both the prefix and one or
  more tags** – In a Lifecycle rule, you can specify a filter
  based on both the key prefix and one or more tags. Again, you must wrap all of
  these filter elements in the `<And>` element, as
  follows:

```
<LifecycleConfiguration>
    <Rule>
        <Filter>
          <And>
             <Prefix>`key-prefix`</Prefix>
             <Tag>
                <Key>`key1`</Key>
                <Value>`value1`</Value>
             </Tag>
             <Tag>
                <Key>`key2`</Key>
                <Value>`value2`</Value>
             </Tag>
              ...
          </And>
        </Filter>
        <Status>Enabled</Status>
        `transition/expiration actions`
    </Rule>
</LifecycleConfiguration>

```

Amazon S3 combines these filters by using a logical `AND`. That is, the
rule applies to the subset of objects with the specified key prefix and the
specified tags. A filter can have only one prefix, and zero or more tags.

- **Specifying an empty filter** – You can specify an empty filter, in which case the rule
  applies to all objects in the bucket.

```
<LifecycleConfiguration>
    <Rule>
        <Filter>
        </Filter>
        <Status>Enabled</Status>
        `transition/expiration actions`
    </Rule>
</LifecycleConfiguration>

```

- **>Specifying an object size filter** – To filter a rule by object size, you can specify a
  minimum size (`ObjectSizeGreaterThan`) or a maximum size
  (`ObjectSizeLessThan`), or you can specify a range of object
  sizes.

Object size values are in bytes. Maximum filter size is 5 TB. Some storage
classes have minimum object size limitations. For more information, see [Comparing the Amazon S3 storage classes](storage-class-intro.md#sc-compare "storage-class-intro.md#sc-compare").

```
<LifecycleConfiguration>
    <Rule>
        <Filter>
            <ObjectSizeGreaterThan>500</ObjectSizeGreaterThan>
        </Filter>
        <Status>Enabled</Status>
        `transition/expiration actions`
    </Rule>
</LifecycleConfiguration>

```

###### Note

The `ObjectSizeGreaterThan` and `ObjectSizeLessThan`
filters exclude the specified values. For example, if you set objects sized
128 KB to 1024 KB to move from the S3 Standard storage class to the
S3 Standard-IA storage class, objects that are exactly 1024 KB and 128 KB
won't transition to S3 Standard-IA. Instead, the rule will apply only to
objects that are greater than 128 KB and less than 1024 KB in size.

If you're specifying an object size range, the
`ObjectSizeGreaterThan` integer must be less than the
`ObjectSizeLessThan` value. When using more than one filter, you
must wrap the filters in an `<And>` element. The following
example shows how to specify objects in a range between 500 bytes and 64,000
bytes.

```
<LifecycleConfiguration>
    <Rule>
        <Filter>
            <And>
                <Prefix>`key-prefix`</Prefix>
                <ObjectSizeGreaterThan>500</ObjectSizeGreaterThan>
                <ObjectSizeLessThan>64000</ObjectSizeLessThan>
            </And>
        </Filter>
        <Status>Enabled</Status>
        `transition/expiration actions`
    </Rule>
</LifecycleConfiguration>

```
