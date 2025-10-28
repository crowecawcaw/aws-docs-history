# GraphQL type reference

Scalar types in GraphQL represent primitive leaf values in a GraphQL schema. These are the
most basic data types that resolve to a single value. Unlike object types, scalar types cannot
have sub-fields. GraphQL comes with a set of default scalar types:

- **Int**: A signed 32-bit integer
- **Float**: A signed double-precision floating-point
  value
- **String**: A UTF-8 character sequence
- **Boolean**: A true or false value
- **ID**: A unique identifier, often used to refetch an
  object or as the key for a cache
  These scalar types serve as the building blocks for more complex types in your schema. They
  are used to define fields that contain simple, singular values. In addition to these built-in
  scalars, AWS AppSync provides you with additional scalars for different use cases.

Interfaces and Unions in GraphQL are abstract types that allow for flexible and extensible
schema design. They provide mechanisms for grouping related types and enabling polymorphic
queries. An Interface in GraphQL is an abstract type that defines a set of fields that a type
must include to implement the interface. It serves as a contract for objects by specifying a
common set of fields that implementing types must have. Interfaces are useful when you want to
return an object or field that can be of several different types, but still have some
guaranteed fields. By contrast, a Union in GraphQL represents a type that could be one of
several object types, but does not define any common fields between those types. Unions are
helpful when you need to return a field that can be of multiple types, and these types don't
necessarily share common fields. Both Interfaces and Unions are particularly useful in
scenarios where a field might return different types of data, enabling clients to query for
specific fields based on the returned type.

This section is used as a reference for schema types.

**Topics**

- [Scalar types
  in GraphQL](scalars.md "scalars.md")
- [Interfaces and unions in GraphQL](interfaces-and-unions.md "interfaces-and-unions.md")
