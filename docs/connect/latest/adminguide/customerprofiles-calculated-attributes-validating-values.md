# Validate

calculated attribute values in Amazon Connect Customer Profiles using APIs

There are two APIs, `GetCalculatedAttributeForProfile` and
`ListCalculatedAttributesForProfile`, that are at the profile
level.

- **GetCalculatedAttributeForProfile** -
  retrieves a single calculated attribute for a single profile.
- **ListCalculatedAttributesForProfile** -
  retrieves a list of calculated attributes for a single profile
  With a valid profile ID, you should see values for your calculated
  attributes:

**Example response**

```

{
    "CalculatedAttributeName": "_average_hold_time",
    "DisplayName": "Average hold time",
    "IsDataPartial": "true",
    "Value": "24144"
}
```

**IsDataPartial** - This flag means that either the
time range (30 days) or object count have not been achieved and therefore the
calculated attribute is still being calculated. For example, if you want an average
over 30 days, only after 30 days have elapsed will the `IsDataPartial`
field be set to false.

## Retrieve a

list of calculated attributes

**Use the AWS CLI**

```
`aws customer-profiles list-calculated-attributes-for-profile --region `your-region` --domain-name `your-domain-name` --profile-id `your-profile-id``
```

**Use the AWS CLI with a custom JSON
file**

Create a JSON file with the following contents:

```

{
    "DomainName": "your-domain-name",
    "ProfileId" "some-profile-id"
}

```

```
`aws customer-profiles list-calculated-attributes-for-profile --region `your-region` --cli-input-json file://`list_calculated_attributes_for_profile_cli`.json`
```

**Endpoint:**

```
https://profile.`your-region`.amazonaws.com/domains/`your-domain-name`/profile/`your-profile-id`/calculated-attributes/
```

## Retrieve a

single calculated attribute

**Use the AWS CLI**:

```
`aws customer-profiles get-calculated-attributes-for-profile --region `your-region` --domain-name `your-domain-name` --calculated-attribute-name `your-calculated-attribute-name` --profile-id `your-profile-id``
```

**Use the AWS CLI with a custom JSON
file**:

Create a JSON file with the following contents:

```

{
    "DomainName": "your-domain-name",
    "CalculatedAttributeName": "your-calculated-attribute-name",
    "ProfileId" "your-profile-id"
}

```

```
`aws customer-profiles get-calculated-attributes-for-profile --region `your-region` --cli-input-json file://`list_calculated_attributes_for_profile_cli`.json`
```

**Endpoint:**

```
https://profile.`your-region`.amazonaws.com/domains/`your-domain-name`/profile/`your-profile-id`/calculated-attributes/`your-calculated-attribute-name`
```
