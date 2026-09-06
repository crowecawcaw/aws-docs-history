

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Statement structure and built-in operators for auto-approval and deny-access policies
<a name="auto-approval-deny-access-policy-statement-structure"></a>

The following table shows the structure of auto-approval and deny-access policies.


| Component | Syntax | 
| --- | --- | 
| effect | `permit \| forbid` | 
| scope | `(principal, action, resource)` | 
| condition clause |  <pre>when {<br />    {{principal or resource}} has {{attribute name}}             <br />};</pre>  | 

## Policy components
<a name="policy-components"></a>

An auto-approval or deny-access policy contains the following components:
+ **Effect** – Either `permit` (allow) or `forbid` (deny) access.
+ **Scope** – The principals, actions, and resources to which the effect applies. You can leave the scope in Cedar undefined by not identifying specific principals, actions, or resources. In this case, the policy applies to all possible principals, actions, and resources. For just-in-time node access, the `action` is always `AWS::SSM::Action::"getTokenForInstanceAccess"`.
+ **Condition clause** – The context in which the effect applies.

## Comments
<a name="auth-policies-policy-comments"></a>

You can include comments in your policies. Comments are defined as a line starting with `//` and ending with a newline character.

The following example shows comments in a policy.

```
// Allows users in the Engineering group from the Platform org to automatically connect to nodes tagged with Engineering and Production keys. 
permit (
    principal in AWS::IdentityStore::Group::"d4q81745-r081-7079-d789-14da1EXAMPLE",
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    principal has organization && resource.hasTag("Engineering") && resource.hasTag("Production") && principal.organization == "Platform"
};
```

## Multiple clauses
<a name="multiple-clauses"></a>

You can use more than one condition clause in a policy statement using the `&&` operator.

```
// Allow access if node has tag where the tag key is Environment 
// & tag value is Development 

permit(principal, action == AWS::SSM::getTokenForInstanceAccess, resource)
when {
    resource.hasTag("Environment") &&
    resource.getTag("Environment") == "Development"
};
```

## Reserved characters
<a name="reserved-characters"></a>

The following example shows how to write a policy if a context property uses a `:` (semicolon), which is a reserved character in the policy language.

```
permit (
    principal,
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    principal has employeeNumber && principal.employeeNumber like "E-1*" && resource.hasTag("Purpose") && resource.getTag("Purpose") == "Testing"
}
```

For additional examples, see [Example policy statements](#policy-statement-examples).

## Just-in-time node access schema
<a name="auto-approval-deny-access-policy-statement-schema"></a>

The following is the Cedar schema for just-in-time node access.

```
namespace AWS::EC2 {
    entity Instance tags String;
}


namespace AWS::IdentityStore {
    entity Group;
    
    entity User in [Group] {
    employeeNumber?: String,
    costCenter?: String,
    organization?: String,
    division?: String,
    };

}


namespace AWS::IAM {

    entity Role;
    
    type AuthorizationContext = {
        principalTags: PrincipalTags,
    };
    
    entity PrincipalTags tags String;
}

namespace AWS::SSM {

    entity ManagedInstance tags String;

    action "getTokenForInstanceAccess" appliesTo {
    principal: [AWS::IdentityStore::User],
    resource: [AWS::EC2::Instance, AWS::SSM::ManagedInstance],
    context: {
        "iam": AWS::IAM::AuthorizationContext
        }
    };
}
```

## Built-in operators
<a name="built-in-policy-operators"></a>

When creating the context of an auto-approval or deny-access policy using various conditions, you can use the `&&` operator to add additional conditions. There are also many other built-in operators that you can use to add additional expressive power to your policy conditions. The following table contains all the built-in operators for reference.



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
  - **Description:** Infix operator. t like p checks if the text t matches the pattern p, which may include wildcard characters \* that match 0 or more of any character. To match a literal star character in t, you can use the special escaped character sequence \\\* in p.

- **.hasTag()**
  - **Types and overloads:** (entity, string) → Boolean
  - **Description:** Checks if entity has the specified tag applied.

- **.getTag()**
  - **Types and overloads:** (entity, string) → Boolean
  - **Description:** Returns the value of the specified tag key.

- **.contains()**
  - **Types and overloads:** (set, any) → Boolean
  - **Description:** Set membership (is B an element of A).

- **.containsAll()**
  - **Types and overloads:** (set, set) → Boolean
  - **Description:** Tests if set A contains all of the elements in set B.

- **.containsAny()**
  - **Types and overloads:** (set, set) → Boolean
  - **Description:** Tests if set A contains any of the elements in set B.



## Example policy statements
<a name="policy-statement-examples"></a>

The following are policy statement examples.

```
// Users assuming IAM roles with a principal tag of "Elevated" can automatically access nodes tagged with the "Environment" key when the value equals "prod"
permit(principal, action == AWS::SSM::getTokenForInstanceAccess, resource)
when {
    // Verify IAM role principal tag
    context.iam.principalTags.getTag("AccessLevel") == "Elevated" &&
    
    // Verify the node has a tag with "Environment" tag key and a tag value of "prod"
    resource.hasTag("Environment") &&
    resource.getTag("Environment") == "prod"
};
```

```
// Identity Center users in the "Contractor" division can automatically access nodes tagged with the "Environment" key when the value equals "dev"
permit(principal, action == AWS::SSM::getTokenForInstanceAccess, resource)
when {
    // Verify that the user is part of the "Contractor" division
    principal.division == "Contractor" &&
    
    // Verify the node has a tag with "Environment" tag key and a tag value of "dev"
    resource.hasTag("Environment") &&
    resource.getTag("Environment") == "dev"
};
```

```
// Identity Center users in a specified group can automatically access nodes tagged with the "Environment" key when the value equals "Production"
permit(principal in AWS::IdentityStore::Group::"d4q81745-r081-7079-d789-14da1EXAMPLE",
    action == AWS::SSM::getTokenForInstanceAccess,
    resource)
when {
    resource.hasTag("Environment") &&
    resource.getTag("Environment") == "Production"
};
```