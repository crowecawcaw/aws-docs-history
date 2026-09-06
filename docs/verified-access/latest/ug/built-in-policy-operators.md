

# Built-in operators for Verified Access policies
<a name="built-in-policy-operators"></a>

When creating the context of an AWS Verified Access policy using various conditions, as discussed in [Verified Access policy statement structure](auth-policies-policy-statement-struct.md), you can use the `&&` operator to add additional conditions. There are also many other built-in operators that you can use to add additional expressive power to your policy conditions. The following table contains all the built-in operators for reference.



- ** \! **
  - **Types and overloads:** Boolean → Boolean
  - **Description:** Logical not.

- ** == **
  - **Types and overloads:** any → any
  - **Description:** Equality. Works on arguments of any type, even if the types don't match. Values of different types are never equal to each other.

- **\!=**
  - **Types and overloads:** any → any
  - **Description:** Inequality; the exact inverse of equality (see above).

- ** < **
  - **Types and overloads:** (long, long) → Boolean
  - **Description:** Long integer less-than.

- ** <= **
  - **Types and overloads:** (long, long) → Boolean
  - **Description:** Long integer less-than-or-equal-to.

- ** > **
  - **Types and overloads:** (long, long) → Boolean
  - **Description:** Long integer greater-than.

- ** >= **
  - **Types and overloads:** (long, long) → Boolean
  - **Description:** Long integer greater-than-or-equal-to.

- **in**
  - **Types and overloads:** (entity, entity) → Boolean / **Description:** Hierarchy membership (reflexive: A in A is always true).
  - **Types and overloads:** (entity, set(entity)) → Boolean / **Description:** Hierarchy membership: A in [B, C, ...] is true if (A and B) \|\| (A in C) \|\| … error if the set contains a non-entity.

- **&&**
  - **Types and overloads:** (Boolean, Boolean) → Boolean
  - **Description:** Logical and (short-circuiting).

- **\|\|**
  - **Types and overloads:** (Boolean, Boolean) → Boolean
  - **Description:** Logical or (short-circuiting).

- **.exists()**
  - **Types and overloads:** entity → Boolean
  - **Description:** Entity existence.

- **has**
  - **Types and overloads:** (entity, attribute) → Boolean
  - **Description:** Infix operator. e has f tests if the record or entity e has a binding for the attribute f. Returns false if e does not exist or if e does exist but doesn't have the attribute f. Attributes can be expressed as identifiers or string literals.

- **like**
  - **Types and overloads:** (string, string) → Boolean
  - **Description:** Infix operator. t like p checks if the text t matches the pattern p, which may include wildcard characters \* that match 0 or more of any character. In order to match a literal star character in t, you can use the special escaped character sequence \\\* in p.

- **.contains()**
  - **Types and overloads:** (set, any) → Boolean
  - **Description:** Set membership (is B an element of A).

- **.containsAll()**
  - **Types and overloads:** (set, set) → Boolean
  - **Description:** Tests if set A contains all of the elements in set B.

- **.containsAny()**
  - **Types and overloads:** (set, set) → Boolean
  - **Description:** Tests if set A contains any of the elements in set B.

