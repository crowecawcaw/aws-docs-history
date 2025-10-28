# Using Aurora Serverless v2 with AWS AppSync

Connect your GraphQL API to Aurora Serverless databases using AWS AppSync. This integration
lets you execute SQL statements through GraphQL queries, mutations, and subscriptions -
giving you a flexible way to interact with your relational data.

###### Note

This tutorial uses the `US-EAST-1` Region.

###### Benefits

- Seamless integration between GraphQL and relational databases
- Ability to perform SQL operations through GraphQL interfaces
- Serverless scalability with Aurora Serverless v2
- Secure data access through AWS Secrets Manager
- Protection against SQL injection through input sanitization
- Flexible query capabilities including filtering and range operations

###### Common Use Cases

- Building scalable applications with relational data requirements
- Creating APIs that need both GraphQL flexibility and SQL database capabilities
- Managing data operations through GraphQL mutations and queries
- Implementing secure database access patterns

In this tutorial, you will learn the following.

- Set up an Aurora Serverless v2 cluster
- Enable Data API functionality
- Create and configure database structures
- Define GraphQL schemas for database operations
- Implement resolvers for queries and mutations
- Secure your data access through proper input sanitization
- Execute various database operations through GraphQL interfaces

###### Topics

- [Setting up your database cluster](#create-cluster "#create-cluster")
- [Enable Data API](#enable-data-api "#enable-data-api")
- [Create database and table](#create-database-and-table "#create-database-and-table")
- [GraphQL schema](#graphql-schema "#graphql-schema")
- [Connect Your API to Database Operations](#configuring-resolvers "#configuring-resolvers")
- [Modify Your Data Through the API](#run-mutations "#run-mutations")
- [Retrieve Your Data](#run-queries "#run-queries")
- [Secure Your Data Access](#input-sanitization "#input-sanitization")

## Setting up your database cluster

Before adding an Amazon RDS data source to AWS AppSync, you must first enable a Data API on an
Aurora Serverless v2 cluster and **configure a secret**
using _AWS Secrets Manager_. You can create an Aurora Serverless v2 cluster
using the AWS CLI:

```
aws rds create-db-cluster \
    --db-cluster-identifier appsync-tutorial \
    --engine aurora-mysql \
    --engine-version 8.0 \
    --serverless-v2-scaling-configuration MinCapacity=0,MaxCapacity=1 \
    --master-username USERNAME \
    --master-user-password COMPLEX_PASSWORD \
    --enable-http-endpoint
```

This will return an ARN for the cluster.

After creating the cluster, you must add an Aurora Serverless v2 instance using
the following command.

```
aws rds create-db-instance \
    --db-cluster-identifier appsync-tutorial \
    --db-instance-identifier appsync-tutorial-instance-1 \
    --db-instance-class db.serverless \
    --engine aurora-mysql
```

###### Note

These endpoints take time to activate. You can check their status in the Amazon RDS console in the
**Connectivity & security** tab for the cluster. You can
also check the status of your cluster with the following AWS CLI command.

```
aws rds describe-db-clusters \
    --db-cluster-identifier appsync-tutorial \
    --query "DBClusters[0].Status"
```

You can create a _Secret_ using the AWS Secrets Manager Console or the AWS CLI
with an input file such as the following using the `USERNAME` and
`COMPLEX_PASSWORD` from the previous step.

```
{
    "username": "USERNAME",
    "password": "COMPLEX_PASSWORD"
}
```

Pass this as a parameter to the AWS CLI:

```
aws secretsmanager create-secret --name HttpRDSSecret --secret-string file://creds.json --region us-east-1
```

This will return an ARN for the secret.

**Note the ARN** of your Aurora Serverless cluster and
Secret for later use in the AppSync console when creating a data source.

## Enable Data API

You can enable the Data API on your cluster by [following the
instructions in the RDS documentation](../../../AmazonRDS/latest/AuroraUserGuide/data-api.md "../../../AmazonRDS/latest/AuroraUserGuide/data-api.md"). The Data API must be enabled before
adding as an AppSync data source.

## Create database and table

Once you have enabled your Data API you can ensure it works with the `aws
 rds-data execute-statement` command in the AWS CLI. This will ensure that your
Aurora Serverless cluster is configured correctly before adding it to your AppSync API.
First create a database called _TESTDB_ with
the `--sql` parameter like so:

```
aws rds-data execute-statement --resource-arn "arn:aws:rds:us-east-1:123456789000:cluster:http-endpoint-test" \
--schema "mysql"  --secret-arn "arn:aws:secretsmanager:us-east-1:123456789000:secret:testHttp2-AmNvc1"  \
--region us-east-1 --sql "create DATABASE TESTDB"
```

If this runs without error, add a table with the _create table_ command:

```
aws rds-data execute-statement --resource-arn "arn:aws:rds:us-east-1:123456789000:cluster:http-endpoint-test" \
 --schema "mysql"  --secret-arn "arn:aws:secretsmanager:us-east-1:123456789000:secret:testHttp2-AmNvc1" \
 --region us-east-1 \
 --sql "create table Pets(id varchar(200), type varchar(200), price float)" --database "TESTDB"
```

If everything has run without issue you can move forward to adding the cluster as a
data source in your AppSync API.

## GraphQL schema

Now that your Aurora Serverless Data API is up and running with a table, we will
create a GraphQL schema and attach resolvers for performing mutations and subscriptions.
Create a new API in the AWS AppSync console and navigate to the **Schema** page, and enter the following:

```
type Mutation {
    createPet(input: CreatePetInput!): Pet
    updatePet(input: UpdatePetInput!): Pet
    deletePet(input: DeletePetInput!): Pet
}

input CreatePetInput {
    type: PetType
    price: Float!
}

input UpdatePetInput {
id: ID!
    type: PetType
    price: Float!
}

input DeletePetInput {
    id: ID!
}

type Pet {
    id: ID!
    type: PetType
    price: Float
}

enum PetType {
    dog
    cat
    fish
    bird
    gecko
}

type Query {
    getPet(id: ID!): Pet
    listPets: [Pet]
    listPetsByPriceRange(min: Float, max: Float): [Pet]
}

schema {
    query: Query
    mutation: Mutation
}
```

**Save** your schema and navigate to the **Data Sources** page and create a new data source. Select
**Relational database** for the Data source type, and
provide a friendly name. Use the database name that you created in the last step, as
well as the **Cluster ARN** that you created it in. For the
**Role** you can either have AppSync create a new role
or create one with a policy similar to the below:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-data:BatchExecuteStatement",
 "rds-data:BeginTransaction",
 "rds-data:CommitTransaction",
 "rds-data:ExecuteStatement",
 "rds-data:RollbackTransaction"
 ],
 "Resource": [
 "arn:aws:rds:us-east-1:111122223333:cluster:mydbcluster",
 "arn:aws:rds:us-east-1:111122223333:cluster:mydbcluster:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret",
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret:*"
 ]
 }
 ]
}`

```

Note there are two **Statements** in this policy which
you are granting role access. The first **Resource** is
your Aurora Serverless cluster and the second is your AWS Secrets Manager ARN. You will
need to provide **BOTH** ARNs in the AppSync data source
configuration before clicking **Create**.

Pass this as a parameter to the AWS CLI.

```
aws secretsmanager create-secret \
  --name HttpRDSSecret \
  --secret-string file://creds.json \
  --region us-east-1
```

This will return an ARN for the secret. Take note of the ARN of your Aurora Serverless cluster
and Secret for later when creating a data source in the AWS AppSync console.

### Build Your Database Structure

Once you have enabled your Data API you can ensure it works with the `aws
 rds-data execute-statement` command in the AWS CLI. This will ensure that your
Aurora Serverless v2 cluster is configured correctly before adding it to your AWS AppSync API.
First, create a database called _TESTDB_ with
the `--sql` parameter as follows.

```
aws rds-data execute-statement \
                --resource-arn "arn:aws:rds:us-east-1:`111122223333`:cluster:`appsync-tutorial`" \
                --secret-arn "arn:aws:secretsmanager:us-east-1:`111122223333`:secret:`appsync-tutorial-rds-secret`"  \
                --region us-east-1 \
                --sql "create DATABASE TESTDB"
```

If this runs without errors, add a table with the following _create table_ command.

```
aws rds-data execute-statement \
      --resource-arn "arn:aws:rds:us-east-1:`111122223333`:cluster:`http-endpoint-test`" \
      --secret-arn "arn:aws:secretsmanager:us-east-1:`111122223333`:secret:`testHttp2-AmNvc1`" \
      --region us-east-1 \
      --sql "create table Pets(id varchar(200), type varchar(200), price float)" \
      --database "TESTDB"
```

### Design Your API Interface

After Aurora Serverless v2 Data API is up and running with a table, create a GraphQL
schema and attach resolvers for performing mutations and subscriptions. Create a new
API in the AWS AppSync console and navigate to the **Schema** page in the console, and enter the following.

```
type Mutation {
        createPet(input: CreatePetInput!): Pet
        updatePet(input: UpdatePetInput!): Pet
        deletePet(input: DeletePetInput!): Pet
    }

    input CreatePetInput {
        type: PetType
        price: Float!
    }

    input UpdatePetInput {
        id: ID!
        type: PetType
        price: Float!
    }

    input DeletePetInput {
        id: ID!
    }

    type Pet {
        id: ID!
        type: PetType
        price: Float
    }

    enum PetType {
        dog
        cat
        fish
        bird
        gecko
    }

    type Query {
        getPet(id: ID!): Pet
        listPets: [Pet]
        listPetsByPriceRange(min: Float, max: Float): [Pet]
    }

    schema {
        query: Query
        mutation: Mutation
    }
```

**Save** your schema and navigate to the **Data Sources** page and create a new data source. Choose
**Relational database** for the **Data source** type, and provide a friendly name. Use the
database name that you created in the last step, as well as the **Cluster ARN** that you created it in. For the **Role** you can either have AWS AppSync create a new role or
create one with a policy similar to the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-data:BatchExecuteStatement",
 "rds-data:BeginTransaction",
 "rds-data:CommitTransaction",
 "rds-data:ExecuteStatement",
 "rds-data:RollbackTransaction"
 ],
 "Resource": [
 "arn:aws:rds:us-east-1:111122223333:cluster:mydbcluster",
 "arn:aws:rds:us-east-1:111122223333:cluster:mydbcluster:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret",
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret:*"
 ]
 }
 ]
 }`

```

Note there are two **Statements** in this policy which
you are granting role access. The first **Resource** is
your Aurora Serverless v2 cluster and the second is your AWS Secrets Manager ARN. You will
need to provide **BOTH** ARNs in the AWS AppSync data source
configuration before clicking **Create**.

## Connect Your API to Database Operations

Now that we have a valid GraphQL schema and an RDS data source, you can attach
resolvers to the GraphQL fields to your schema. Our API will offer the following
capabilities:

1. create a pet using the _Mutation.createPet_ field
2. update a pet using the _Mutation.updatePet_ field
3. delete a pet using the _Mutation.deletePet_ field
4. get a single using via the _Query.getPet_ field
5. list all using the _Query.listPets_
   field
6. list pets in a price range using the _Query.listPetsByPriceRange_ field

### Mutation.createPet

From the schema editor in the AWS AppSync console, on the right side choose
**Attach Resolver** for `createPet(input:
 CreatePetInput!): Pet`. Choose your RDS data source. In the **request mapping template** section, add the following
template:

```
#set($id=$utils.autoId())
{
"version": "2018-05-29",
    "statements": [
        "insert into Pets VALUES (:ID, :TYPE, :PRICE)",
        "select * from Pets WHERE id = :ID"
    ],
    "variableMap": {
        ":ID": "$ctx.args.input.id",
        ":TYPE": $util.toJson($ctx.args.input.type),
        ":PRICE": $util.toJson($ctx.args.input.price)
    }
}
```

The system executes SQL statements sequentially, based on the order in the **statements** array. The results will come back in the
same order. Since this is a mutation, you will run a _select_ statement after the _insert_ to retrieve the committed values in
order to populate the GraphQL response mapping template.

In the **response mapping template** section, add the
following template:

```
$utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
```

Because the _statements_ has two SQL
queries, we need to specify the second result in the matrix that comes back from the
database with: `$utils.rds.toJsonString($ctx.result))[1][0])`.

### Mutation.updatePet

From the schema editor in the AWS AppSync console, choose **Attach Resolver** for `updatePet(input: UpdatePetInput!):
 Pet`. Choose your **RDS data source**. In
the **request mapping template** section, add the
following template.

```
{
"version": "2018-05-29",
    "statements": [
        $util.toJson("update Pets set type=:TYPE, price=:PRICE WHERE id=:ID"),
        $util.toJson("select * from Pets WHERE id = :ID")
    ],
    "variableMap": {
        ":ID": "$ctx.args.input.id",
        ":TYPE": $util.toJson($ctx.args.input.type),
        ":PRICE": $util.toJson($ctx.args.input.price)
    }
}
```

In the **response mapping template** section, add the
following template.

```
$utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
```

### Mutation.deletePet

From the schema editor in the AWS AppSync console, choose **Attach Resolver** for `deletePet(input: DeletePetInput!):
 Pet`. Choose your **RDS data source**. In
the **request mapping template** section, add the
following template.

```
{
"version": "2018-05-29",
    "statements": [
        $util.toJson("select * from Pets WHERE id=:ID"),
        $util.toJson("delete from Pets WHERE id=:ID")
    ],
    "variableMap": {
        ":ID": "$ctx.args.input.id"
    }
}
```

In the **response mapping template** section, add the
following template.

```
$utils.toJson($utils.rds.toJsonObject($ctx.result)[0][0])
```

### Query.getPet

Now that the mutations are created for your schema, connect the three queries to
showcase how to get individual items, lists, and apply SQL filtering. From the
**schema editor** in the AWS AppSync console,
choose **Attach Resolver** for `getPet(id:
 ID!): Pet`. Choose your **RDS data
source**. In the **request mapping
template** section, add the following template.

```
{
"version": "2018-05-29",
        "statements": [
            $util.toJson("select * from Pets WHERE id=:ID")
    ],
    "variableMap": {
        ":ID": "$ctx.args.id"
    }
}
```

In the **response mapping template** section, add the
following template:

```
$utils.toJson($utils.rds.toJsonObject($ctx.result)[0][0])
```

### Query.listPets

From the schema editor in the AWS AppSync console, on the right side choose
**Attach Resolver** for `getPet(id: ID!):
 Pet`. Choose your **RDS data source**. In
the **request mapping template** section, add the
following template.

```
{
    "version": "2018-05-29",
    "statements": [
        "select * from Pets"
    ]
}
```

In the **response mapping template** section, add the
following template.

```
$utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
```

### Query.listPetsByPriceRange

From the schema editor in the AWS AppSync console, on the right side choose
**Attach Resolver** for `getPet(id: ID!):
 Pet`. Choose your **RDS data source**. In
the **request mapping template** section, add the
following template.

```
{
    "version": "2018-05-29",
    "statements": [
            "select * from Pets where price > :MIN and price < :MAX"
    ],

    "variableMap": {
        ":MAX": $util.toJson($ctx.args.max),
        ":MIN": $util.toJson($ctx.args.min)
    }
}
```

In the **response mapping template** section, add the
following template:

```
$utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
```

## Modify Your Data Through the API

Now that you have configured all of your resolvers with SQL statements and connected
your GraphQL API to your Serverless Aurora Data API, you can begin performing mutations
and queries. In AWS AppSync console, choose the **Queries**
tab and enter the following to create a Pet:

```
mutation add {
    createPet(input : { type:fish, price:10.0 }){
        id
        type
        price
    }
}
```

The response should contain the _id_,
_type_, and _price_ like so:

```
{
  "data": {
    "createPet": {
      "id": "c6fedbbe-57ad-4da3-860a-ffe8d039882a",
      "type": "fish",
      "price": "10.0"
    }
  }
}
```

You can modify this item by running the _updatePet_ mutation:

```
mutation update {
    updatePet(input : {
        id: ID_PLACEHOLDER,
        type:bird,
        price:50.0
    }){
        id
        type
        price
    }
}
```

Note that we used the _id_ which was
returned from the _createPet_ operation
earlier. This will be a unique value for your record as the resolver leveraged
`$util.autoId()`. You could delete a record in a similar manner:

```
mutation delete {
    deletePet(input : {id:ID_PLACEHOLDER}){
        id
        type
        price
    }
}
```

Create a few records with the first mutation with different values for _price_ and then run some queries.

## Retrieve Your Data

Still in the **Queries** tab of the console, use the
following statement to list all of the records you’ve created.

```
query allpets {
    listPets {
        id
        type
        price
    }
}
```

Leverage the SQL _WHERE_ predicate that had `where price > :MIN and price <
 :MAX` in our mapping template for _Query.listPetsByPriceRange_ with the following GraphQL query:

```
query petsByPriceRange {
    listPetsByPriceRange(min:1, max:11) {
        id
        type
        price
    }
}
```

You should only see records with a _price_
over $1 or less than $10. Finally, you can perform queries to retrieve individual
records as follows:

```
query onePet {
    getPet(id:ID_PLACEHOLDER){
        id
        type
        price
    }
}
```

## Secure Your Data Access

SQL injection is a security vulnerability in database applications. It occurs when
attackers insert malicious SQL code through user input fields. This can allow unauthorized
access to database data. We recommend that you carefully
validate and sanitize all user inputs before processing using `variableMap` for
protection against SQL injection attacks. If variable maps are not used, you are
responsible for sanitizing the arguments of their GraphQL operations. One way to do this
is to provide input specific validation steps in the request mapping template before execution
of a SQL statement against your Data API. Let’s see how we can modify the request mapping
template of the `listPetsByPriceRange` example. Instead of relying solely on the
user input you can do the following:

```
#set($validMaxPrice = $util.matches("\d{1,3}[,\\.]?(\\d{1,2})?",$ctx.args.maxPrice))

#set($validMinPrice = $util.matches("\d{1,3}[,\\.]?(\\d{1,2})?",$ctx.args.minPrice))


#if (!$validMaxPrice || !$validMinPrice)
    $util.error("Provided price input is not valid.")
#end
{
    "version": "2018-05-29",
    "statements": [
            "select * from Pets where price > :MIN and price < :MAX"
    ],

    "variableMap": {
        ":MAX": $util.toJson($ctx.args.maxPrice),
        ":MIN": $util.toJson($ctx.args.minPrice)
    }
}
```

Another way to protect against rogue input when executing resolvers against your Data
API is to use prepared statements together with stored procedure and parameterized
inputs. For example, in the resolver for `listPets` define the following
procedure that executes the _select_ as a
prepared statement:

```
CREATE PROCEDURE listPets (IN type_param VARCHAR(200))
  BEGIN
     PREPARE stmt FROM 'SELECT * FROM Pets where type=?';
     SET @type = type_param;
     EXECUTE stmt USING @type;
     DEALLOCATE PREPARE stmt;
  END
```

Create this in your Aurora Serverless v2 Instance.

```
aws rds-data execute-statement --resource-arn "arn:aws:rds:us-east-1:xxxxxxxxxxxx:cluster:http-endpoint-test" \
--schema "mysql"  --secret-arn "arn:aws:secretsmanager:us-east-1:xxxxxxxxxxxx:secret:httpendpoint-xxxxxx"  \
--region us-east-1  --database "DB_NAME" \
--sql "CREATE PROCEDURE listPets (IN type_param VARCHAR(200)) BEGIN PREPARE stmt FROM 'SELECT * FROM Pets where type=?'; SET @type = type_param; EXECUTE stmt USING @type; DEALLOCATE PREPARE stmt; END"
```

The resulting resolver code for listPets is simplified since we now simply call the
stored procedure. At a minimum, any string input should have single quotes [escaped](#escaped "#escaped").

```
#set ($validType = $util.isString($ctx.args.type) && !$util.isNullOrBlank($ctx.args.type))
#if (!$validType)
    $util.error("Input for 'type' is not valid.", "ValidationError")
#end

{
    "version": "2018-05-29",
    "statements": [
        "CALL listPets(:type)"
    ]
    "variableMap": {
        ":type": $util.toJson($ctx.args.type.replace("'", "''"))
    }
}
```

### Using escape strings

Use single quotes to mark the start and end of string literals in an SQL statement
e.g.. `'some string value'`. To allow string values with one or more
single quote characters ( `'`) to be used within a string, each must
be replaced with two single quotes (`''`). For example, if the input
string is `Nadia's dog`, you would escape it for the SQL statement
like

```
update Pets set type='Nadia''s dog' WHERE id='1'
```
