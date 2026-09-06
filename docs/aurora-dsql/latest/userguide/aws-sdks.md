# Amazon Aurora DSQL cluster connectivity tools

Aurora DSQL is compatible with many third-party database drivers and ORM libraries. AWS provides two types of tools to simplify working with Aurora DSQL:

- **[Connectors](SECTION_connectors.md "SECTION_connectors.md")** – Authentication plugins that extend database drivers to handle IAM token generation automatically. Use connectors when working directly with database drivers.
- **Adapters and dialects** – Extensions for specific ORM frameworks that provide IAM authentication and improved Aurora DSQL compatibility. Use adapters when working with a supported ORM framework.

## Aurora DSQL adapters and dialects

The following table shows the available adapters and dialects for Aurora DSQL. Each
repository is available on the GitHub website.

| Programming language | ORM/Framework | Repository link                                                                                                                                                                               |
| -------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Java                 | Hibernate     | [aurora-dsql-orms/java/hibernate](https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate "https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate")                |
| Python               | Django        | [aurora-dsql-orms/python/django](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/django "https://github.com/awslabs/aurora-dsql-orms/tree/main/python/django")                   |
| Python               | SQLAlchemy    | [aurora-dsql-orms/python/sqlalchemy](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/sqlalchemy "https://github.com/awslabs/aurora-dsql-orms/tree/main/python/sqlalchemy")       |
| Python               | Tortoise ORM  | [aurora-dsql-orms/python/tortoise-orm](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/tortoise-orm "https://github.com/awslabs/aurora-dsql-orms/tree/main/python/tortoise-orm") |
| TypeScript           | Drizzle ORM   | [aurora-dsql-orms/node/drizzle](https://github.com/awslabs/aurora-dsql-orms/tree/main/node/drizzle "https://github.com/awslabs/aurora-dsql-orms/tree/main/node/drizzle")                      |

## Database driver samples

The following table shows sample code for connecting to Aurora DSQL using third-party
database drivers. Each sample repository is
available on the GitHub website.

| Programming language | Driver                     | Sample repository link                                                                                                                                                                                                        |
| -------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C++                  | libpq                      | [aurora-dsql-samples/cpp/libpq](https://github.com/aws-samples/aurora-dsql-samples/tree/main/cpp/libpq "https://github.com/aws-samples/aurora-dsql-samples/tree/main/cpp/libpq")                                              |
| C# (.NET)            | Npgsql                     | [aurora-dsql-samples/dotnet/npgsql](https://github.com/aws-samples/aurora-dsql-samples/tree/main/dotnet/npgsql "https://github.com/aws-samples/aurora-dsql-samples/tree/main/dotnet/npgsql")                                  |
| Go                   | pgx                        | [aurora-dsql-samples/go/pgx](https://github.com/aws-samples/aurora-dsql-samples/tree/main/go/pgx "https://github.com/aws-samples/aurora-dsql-samples/tree/main/go/pgx")                                                       |
| Java                 | HikariCP + pgJDBC          | [aurora-dsql-samples/java/pgjdbc](https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/pgjdbc "https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/pgjdbc")                                        |
| JavaScript           | node-postgres (AWS Lambda) | [aurora-dsql-samples/lambda](https://github.com/aws-samples/aurora-dsql-samples/tree/main/lambda "https://github.com/aws-samples/aurora-dsql-samples/tree/main/lambda")                                                       |
| JavaScript           | node-postgres              | [aurora-dsql-samples/javascript/node-postgres](https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/node-postgres "https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/node-postgres") |
| JavaScript           | Postgres.js                | [aurora-dsql-samples/javascript/postgres-js](https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/postgres-js "https://github.com/aws-samples/aurora-dsql-samples/tree/main/javascript/postgres-js")       |
| Python               | asyncpg                    | [aurora-dsql-samples/python/asyncpg](https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/asyncpg "https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/asyncpg")                               |
| Python               | Psycopg                    | [aurora-dsql-samples/python/psycopg](https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg "https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg")                               |
| Python               | Psycopg2                   | [aurora-dsql-samples/python/psycopg2](https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg2 "https://github.com/aws-samples/aurora-dsql-samples/tree/main/python/psycopg2")                            |
| Ruby                 | pg                         | [aurora-dsql-samples/ruby/ruby-pg](https://github.com/aws-samples/aurora-dsql-samples/tree/main/ruby/ruby-pg "https://github.com/aws-samples/aurora-dsql-samples/tree/main/ruby/ruby-pg")                                     |
| Rust                 | SQLx                       | [aurora-dsql-samples/rust/sqlx](https://github.com/aws-samples/aurora-dsql-samples/tree/main/rust/sqlx "https://github.com/aws-samples/aurora-dsql-samples/tree/main/rust/sqlx")                                              |

## ORM and framework samples

The following table shows sample code for using third-party ORM libraries and
frameworks with Aurora DSQL. Each sample repository is
available on the GitHub website.

| Programming language | ORM/Framework | Sample repository link                                                                                                                                                                                                                                          |
| -------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Java                 | Hibernate     | [aurora-dsql-orms/java/hibernate/examples/pet-clinic-app](https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate/examples/pet-clinic-app "https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate/examples/pet-clinic-app")          |
| Java                 | Liquibase     | [aurora-dsql-samples/java/liquibase](https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/liquibase "https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/liquibase")                                                                 |
| Java                 | Spring Boot   | [aurora-dsql-samples/java/spring\_boot](https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/spring_boot "https://github.com/aws-samples/aurora-dsql-samples/tree/main/java/spring_boot")                                                          |
| Python               | Django        | [aurora-dsql-orms/python/django/examples/pet-clinic-app](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/django/examples/pet-clinic-app "https://github.com/awslabs/aurora-dsql-orms/tree/main/python/django/examples/pet-clinic-app")             |
| Python               | SQLAlchemy    | [aurora-dsql-orms/python/sqlalchemy/examples/pet-clinic-app](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/sqlalchemy/examples/pet-clinic-app "https://github.com/awslabs/aurora-dsql-orms/tree/main/python/sqlalchemy/examples/pet-clinic-app") |
| Python               | Tortoise ORM  | [aurora-dsql-orms/python/tortoise-orm/example](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/tortoise-orm/example "https://github.com/awslabs/aurora-dsql-orms/tree/main/python/tortoise-orm/example")                                           |
| Ruby                 | Rails         | [aurora-dsql-samples/ruby/rails](https://github.com/aws-samples/aurora-dsql-samples/tree/main/ruby/rails "https://github.com/aws-samples/aurora-dsql-samples/tree/main/ruby/rails")                                                                             |
| TypeScript           | Drizzle ORM   | [aurora-dsql-orms/node/drizzle/examples/veterinary-app](https://github.com/awslabs/aurora-dsql-orms/tree/main/node/drizzle/examples/veterinary-app "https://github.com/awslabs/aurora-dsql-orms/tree/main/node/drizzle/examples/veterinary-app")                |
| TypeScript           | Prisma        | [aurora-dsql-samples/typescript/prisma-multi-region](https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/prisma-multi-region "https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/prisma-multi-region")                 |
| TypeScript           | Sequelize     | [aurora-dsql-samples/typescript/sequelize](https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/sequelize "https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/sequelize")                                               |
| TypeScript           | TypeORM       | [aurora-dsql-samples/typescript/type-orm](https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/type-orm "https://github.com/aws-samples/aurora-dsql-samples/tree/main/typescript/type-orm")                                                  |
