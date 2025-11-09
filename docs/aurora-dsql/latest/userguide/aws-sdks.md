# Amazon Aurora DSQL cluster connectivity tools

AWS provides various tools for connecting to and working with Aurora DSQL databases. These include database drivers, ORM libraries, and specialized adapters that make it easier for developers to build applications in their preferred programming language.

## Database Drivers

The following table shows the available database drivers for connecting directly to Aurora DSQL.

| Programming language | Driver                   | Sample repository link                                                                                                                                                                                                                                                 |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C++                  | libpq                    | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/cpp/libpq](https://github.com/aws-samples/aurora-dsql-samples/tree/main/cpp/libpq "https://github.com/aws-samples/aurora-dsql-samples/tree/main/cpp/libpq")                                              |
| C# (.NET)            | Npgsql                   | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/dotnet/npgsql](https://github.com/aws-samples/aurora-dsql-samples/tree/main/dotnet/npgsql "https://github.com/aws-samples/aurora-dsql-samples/tree/main/dotnet/npgsql")                                  |
| Go                   | pgx                      | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/go/pgx](https://github.com/aws-samples/aurora-dsql-samples/tree/main/go/pgx "https://github.com/aws-samples/aurora-dsql-samples/tree/main/go/pgx")                                                       |
| Java                 | pgJDBC                   | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/pgjdbc](https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/pgjdbc "https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/pgjdbc")                                        |
| Java                 | Aurora DSQL JDBC Wrapper | [https://github.com/awslabs/aurora-dsql-jdbc-wrapper](https://github.com/awslabs/aurora-dsql-jdbc-wrapper "https://github.com/awslabs/aurora-dsql-jdbc-wrapper")                                                                                                       |
| JavaScript           | node-postgres            | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/node-postgres](https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/node-postgres "https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/node-postgres") |
| JavaScript           | Postgres.js              | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/postgres-js](https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/postgres-js "https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/postgres-js")       |
| Python               | Psycopg                  | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg](https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg "https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg")                               |
| Python               | Psycopg2                 | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg2](https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg2 "https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg2")                            |
| Ruby                 | pg                       | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/ruby/ruby-pg](https://github.com/aws-samples/aurora-dsql-samples/tree/main/ruby/ruby-pg "https://github.com/aws-samples/aurora-dsql-samples/tree/main/ruby/ruby-pg")                                     |
| Rust                 | SQLx                     | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/rust/sqlx](https://github.com/aws-samples/aurora-dsql-samples/tree/main/rust/sqlx "https://github.com/aws-samples/aurora-dsql-samples/tree/main/rust/sqlx")                                              |

## Object-Relational Mapping (ORM)

libraries

The following table shows sample code for using standalone ORM libraries with Aurora DSQL.

| Programming language | ORM Library | Sample repository link                                                                                                                                                                                                                                           |
| -------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Java                 | Hibernate   | [https://github.com/awslabs/aurora-dsql-hibernate/tree/main/examples/pet-clinic-app](https://github.com/awslabs/aurora-dsql-hibernate/tree/main/examples/pet-clinic-app "https://github.com/awslabs/aurora-dsql-hibernate/tree/main/examples/pet-clinic-app")    |
| Python               | SQLAlchemy  | [https://github.com/awslabs/aurora-dsql-sqlalchemy/tree/main/examples/pet-clinic-app](https://github.com/awslabs/aurora-dsql-sqlalchemy/tree/main/examples/pet-clinic-app "https://github.com/awslabs/aurora-dsql-sqlalchemy/tree/main/examples/pet-clinic-app") |
| TypeScript           | Sequelize   | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/sequelize](https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/sequelize "https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/sequelize")       |
| TypeScript           | TypeORM     | [https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/type-orm](https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/type-orm "https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/type-orm")          |

## Aurora DSQL adapters and dialects

The following table shows the available adapters and dialects specifically designed for Aurora DSQL.

| Programming language | ORM/Framework | Repository link                                                                                                                                               |
| -------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Java                 | Hibernate     | [https://github.com/awslabs/aurora-dsql-hibernate/](https://github.com/awslabs/aurora-dsql-hibernate/ "https://github.com/awslabs/aurora-dsql-hibernate/")    |
| Python               | Django        | [https://github.com/awslabs/aurora-dsql-django/](https://github.com/awslabs/aurora-dsql-django/ "https://github.com/awslabs/aurora-dsql-django/")             |
| Python               | SQLAlchemy    | [https://github.com/awslabs/aurora-dsql-sqlalchemy/](https://github.com/awslabs/aurora-dsql-sqlalchemy/ "https://github.com/awslabs/aurora-dsql-sqlalchemy/") |
