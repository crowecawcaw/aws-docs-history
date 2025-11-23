Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift federated permissions - end-to-end examples

The following is an end-to-end example showing how you can create and manage comprehensive data governance policies using Amazon Redshift Federated Permissions. These policies include Row Level Security (RLS), Dynamic Data Masking (DDM), and Column Level Permissions (CLP) that work together to control data access based on user roles and conditions.

You must be a `superuser` or have the [sys:secadmin](r_roles-default.md "r_roles-default.md") role to run this example.

## Prerequisites

The examples assume that the below "IAMR:role_name" roles are already present in the account, if not please create them. Moreover, the Redshift data warehouse is registered with AWS Glue Data Catalog with name "catalog_name" and has a database of "db_name".

## On catalog instance grant sys:secadmin Role to corresponding IAM Role

```
-- Grant sys:secadmin role to relevant user (must be run on Redshift catalog instance)
        GRANT ROLE sys:secadmin TO "IAMR:AccountSecurityAdminrole_name";
```

### Rest will be run on Redshift compute warehouse

If you are using IAM or IdC users, you can skip following two steps to create local warehouse users and Global identity mapping.

#### Step 1: Creating the local warehouse necessary users for testing governance policies

```
-- Create test users.
CREATE USER alice WITH PASSWORD 'Alice_pass_1';
CREATE USER oscar WITH PASSWORD 'Oscar_pass_1';
CREATE USER sierra WITH PASSWORD 'Sierra_pass_1';
```

#### Step 2: Setting Up Global Identity IAM Role Mapping

```
-- Map local users to IAM roles (executed by superuser).

-- Make user sierra a sys:secadmin by setting the global identity
-- to `IAMR:AccountSecurityAdmin`.
-- This role has been granted secadmin privilege on Redshift catalog instance.

ALTER USER sierra SET GLOBAL IDENTITY
IAM_ROLE 'arn:aws:iam::123456789012:role/AccountSecurityAdmin';

ALTER USER alice SET GLOBAL IDENTITY
IAM_ROLE 'arn:aws:iam::123456789012:role/Analyst';

ALTER USER oscar SET GLOBAL IDENTITY
IAM_ROLE 'arn:aws:iam::123456789012:role/Operator';

-- Verify global identity settings.
SET SESSION AUTHORIZATION sierra;
SHOW GLOBAL IDENTITY;

SET SESSION AUTHORIZATION alice;
SHOW GLOBAL IDENTITY;

SET SESSION AUTHORIZATION oscar;
SHOW GLOBAL IDENTITY;

-- Reset to default session.
RESET SESSION AUTHORIZATION;
```

## Setting Up the Environment

First, create tables and populate them with sample customer data and lookup tables for governance policies.

```
-- Create the main customer table.
CREATE TABLE db_name@catalog_name.public.customers (
    id INTEGER,
    name VARCHAR(50),
    email VARCHAR(100),
    region VARCHAR(20),
    revenue DECIMAL(10,2)
);

-- Populate with sample customer data.
INSERT INTO db_name@catalog_name.public.customers VALUES
(1, 'John Smith', 'john@email.com', 'US', 1000.00),
(2, 'Jane Doe', 'jane@email.com', 'EU', 500.00),
(3, 'Mike Johnson', 'mike@email.com', 'US', 2000.00);

-- Grant basic table access.
GRANT ALL ON db_name@catalog_name.public.customers TO PUBLIC;

-- Create lookup table for region-based policies.
CREATE TABLE db_name@catalog_name.public.lookup_regions (
    region_code VARCHAR(20),
    allowed BOOLEAN
);

INSERT INTO db_name@catalog_name.public.lookup_regions VALUES
('US', TRUE),
('EU', FALSE),
('APAC', TRUE);

GRANT ALL ON db_name@catalog_name.public.lookup_regions TO PUBLIC;

-- Create lookup table for revenue-based masking.
CREATE TABLE db_name@catalog_name.public.lookup_revenue_tiers (base_revenue INTEGER);

INSERT INTO db_name@catalog_name.public.lookup_revenue_tiers VALUES (1000), (2000);
GRANT ALL ON db_name@catalog_name.public.lookup_revenue_tiers TO PUBLIC;
```

## Setting Up Column Level Permissions (CLP)

Configure column-level access for different users to control which columns users can access.

```
-- Grant specific column access to Analyst i.e. `alice`.
GRANT SELECT (id, region) ON db_name@catalog_name.public.customers
    TO "IAMR:Analyst";

-- Grant different column access to Operator i.e. `oscar`.
GRANT SELECT (id, name, revenue) ON db_name@catalog_name.public.customers
    TO "IAMR:operator";
```

## Creating Row Level Security (RLS) Policies

Create RLS policies to control which rows users can see based on their grants and data conditions.

```
-- Switch to admin user to create policies.
SET SESSION AUTHORIZATION sierra;

-- Create simple RLS policy: Analysts see only US customers.
CREATE RLS POLICY db_name@catalog_name.us_only
WITH (region VARCHAR(20))
USING (region = 'US');

-- Attach the policy to the Analyst i.e. `alice`.
ATTACH RLS POLICY db_name@catalog_name.us_only
ON db_name@catalog_name.public.customers
TO "IAMR:Analyst";

-- Enable row level security on the table.
ALTER TABLE db_name@catalog_name.public.customers ROW LEVEL SECURITY ON;

-- Create advanced RLS policy using lookup table.
CREATE RLS POLICY db_name@catalog_name.region_lookup_policy
WITH (region VARCHAR(20)) AS r
USING (r.region IN (
    SELECT region_code
    FROM public.lookup_regions
    WHERE allowed = TRUE
));

-- Attach the lookup-based policy to Operator i.e. `oscar`.
ATTACH RLS POLICY db_name@catalog_name.region_lookup_policy
ON db_name@catalog_name.public.customers
TO "IAMR:Operator";
```

## Creating Dynamic Data Masking (DDM) Policies

Create masking policies to obfuscate sensitive data based on user roles and conditions.

```
-- Create masking policy for PII data (names and emails).
CREATE MASKING POLICY db_name@catalog_name.mask_pii
WITH (DATA VARCHAR(100))
USING (SHA2(DATA + 'secret', 256)::TEXT);

-- Attach masking to name and email columns for all users.
ATTACH MASKING POLICY db_name@catalog_name.mask_pii
ON db_name@catalog_name.public.customers (name)
TO PUBLIC;

ATTACH MASKING POLICY db_name@catalog_name.mask_pii
ON db_name@catalog_name.public.customers (email)
TO PUBLIC;

-- Create conditional masking policy for revenue data.
CREATE MASKING POLICY db_name@catalog_name.conditional_mask
WITH (revenue DECIMAL(10,2))
USING (CASE WHEN revenue IN (SELECT base_revenue
                                    FROM public.lookup_revenue_tiers)
            THEN revenue ELSE 0.00 END);

-- Attach conditional masking to Analyst i.e. `alice` with priority.
ATTACH MASKING POLICY db_name@catalog_name.conditional_mask
ON db_name@catalog_name.public.customers (revenue)
TO "IAMR:Analyst"
PRIORITY 20;
```

## Auditing Available/Applied Policies

Use SHOW commands to confirm your governance policies are properly configured.

```
-- Show all RLS policies in the database.
SHOW RLS POLICIES FROM DATABASE db_name@catalog_name LIMIT 10;

-- Show RLS policies for specific users and tables.
SHOW RLS POLICIES ON db_name@catalog_name.public.customers FOR "IAMR:Analyst" LIMIT 10;
SHOW RLS POLICIES ON db_name@catalog_name.public.customers FOR "IAMR:Operator" LIMIT 10;
SHOW RLS POLICIES ON db_name@catalog_name.public.customers FOR PUBLIC LIMIT 10;

-- Show all masking policies in the database.
SHOW MASKING POLICIES FROM DATABASE db_name@catalog_name LIMIT 10;

-- Show Masking policies for specific users and tables.
SHOW MASKING POLICIES ON db_name@catalog_name.public.customers FOR "IAMR:Analyst" LIMIT 10;
SHOW MASKING POLICIES ON db_name@catalog_name.public.customers FOR "IAMR:Operator" LIMIT 10;
SHOW MASKING POLICIES ON db_name@catalog_name.public.customers FOR PUBLIC LIMIT 10;
```

## Testing Access Patterns

Test how different users see the data based on their roles and applied policies.

```
-- Test as analyst: Only US customers, only id/region columns,
-- conditional revenue masking.
SET SESSION AUTHORIZATION alice;
SELECT id, region FROM db_name@catalog_name.public.customers ORDER BY id;
SELECT id, region, revenue FROM db_name@catalog_name.public.customers ORDER BY id;

-- Test as operator: Allowed regions only, masked names, specific columns.
SET SESSION AUTHORIZATION oscar;
SELECT id, name, revenue FROM db_name@catalog_name.public.customers ORDER BY id;
SELECT id, name, region FROM db_name@catalog_name.public.customers ORDER BY id;

-- Test as admin: Full access to all data.
SET SESSION AUTHORIZATION sierra;
SELECT * FROM db_name@catalog_name.public.customers ORDER BY id;
```

## Altering Policies

Modify existing policies to change their behavior without recreating them.

```
-- Switch back to admin user.
SET SESSION AUTHORIZATION sierra;

-- Alter the PII masking policy to use simple string replacement.
ALTER MASKING POLICY db_name@catalog_name.mask_pii
USING ('***MASKED***'::TEXT);

-- Alter the conditional masking policy to use different threshold.
ALTER MASKING POLICY db_name@catalog_name.conditional_mask
USING (CASE WHEN revenue >= 500.00 THEN revenue ELSE -1.00 END);

-- Alter the RLS policy to show only disallowed regions.
ALTER RLS POLICY db_name@catalog_name.region_lookup_policy
USING (r.region IN (
    SELECT region_code
    FROM db_name@catalog_name.public.lookup_regions
    WHERE allowed = FALSE
));
```

## Detaching and Dropping Policies

Remove policies when they're no longer needed.

```
-- Detach RLS policies from users.
DETACH RLS POLICY db_name@catalog_name.us_only
ON db_name@catalog_name.public.customers
FROM "IAMR:Analyst";

DETACH RLS POLICY db_name@catalog_name.region_lookup_policy
ON db_name@catalog_name.public.customers
FROM "IAMR:Operator";

-- Detach masking policies.
DETACH MASKING POLICY db_name@catalog_name.mask_pii
ON db_name@catalog_name.public.customers (name)
FROM PUBLIC;

DETACH MASKING POLICY db_name@catalog_name.mask_pii
ON db_name@catalog_name.public.customers (email)
FROM PUBLIC;

DETACH MASKING POLICY db_name@catalog_name.conditional_mask
ON db_name@catalog_name.public.customers (revenue)
FROM "IAMR:Analyst";
```

## Clean up: Turn off RLS and drop policies

```
-- Turn off Row-level security.
ALTER TABLE db_name@catalog_name.public.customers ROW LEVEL SECURITY OFF;

-- Drop policies.
DROP RLS POLICY db_name@catalog_name.us_only CASCADE;
DROP RLS POLICY db_name@catalog_name.region_lookup_policy CASCADE;
DROP MASKING POLICY db_name@catalog_name.mask_pii CASCADE;
DROP MASKING POLICY db_name@catalog_name.conditional_mask CASCADE;

-- Drop tables.
DROP TABLE db_name@catalog_name.public.customers;
DROP TABLE db_name@catalog_name.public.lookup_regions;
DROP TABLE db_name@catalog_name.public.lookup_revenue_tiers;
```

## Reset Global identity

```
-- TO rest the global identity.
ALTER USER alice RESET GLOBAL IDENTITY;
ALTER USER oscar RESET GLOBAL IDENTITY;
ALTER USER sierra RESET GLOBAL IDENTITY;
```
