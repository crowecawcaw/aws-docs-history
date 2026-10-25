

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Calling stored procedures across databases and through data sharing
<a name="stored-procedure-data-sharing"></a>

With Amazon Redshift, you can call stored procedures across databases and through data sharing. While connected to a database, you can call a stored procedure in another database on the same cluster. You can also call a procedure that a producer shares with you through a datashare. This topic explains how to use this feature and its limitations.

The examples in this section use a producer database named `producer_db` that is shared through the datashare `salesshare`. On the consumer, `datashare_db` is the database created from that datashare, and `consumer_db` is a database local to the consumer.

## Sharing and calling a procedure
<a name="stored-procedure-data-sharing-call"></a>

To share a procedure, grant `EXECUTE` on it to the datashare, and give the consumer access to the datashare.

To call a remote stored procedure, first run `USE` to set the database context to the database that contains the procedure. For a procedure shared through a datashare, that is the database that you created from the datashare. Then call the procedure by its one-part, two-part, or three-part name. You must run `USE` even when you call the procedure by its three-part name.

```
-- On the producer, in producer_db
CREATE PROCEDURE public.refresh_summary(p_region varchar)
AS $$
BEGIN
  DELETE FROM public.sales_summary WHERE region = p_region;
  INSERT INTO public.sales_summary
    SELECT region, SUM(amount) FROM public.sales WHERE region = p_region GROUP BY region;
END;
$$ LANGUAGE plpgsql;

CREATE DATASHARE salesshare;
GRANT USAGE ON SCHEMA public TO DATASHARE salesshare;
GRANT SELECT ON public.sales TO DATASHARE salesshare;
GRANT SELECT, INSERT, DELETE ON public.sales_summary TO DATASHARE salesshare;
GRANT EXECUTE ON PROCEDURE public.refresh_summary(varchar) TO DATASHARE salesshare;
GRANT USAGE ON DATASHARE salesshare TO NAMESPACE 'consumer-namespace-id';
```

On the consumer, create a database from the datashare, set the database context, and call the procedure.

```
-- On the consumer, in consumer_db
CREATE DATABASE datashare_db FROM DATASHARE salesshare OF NAMESPACE 'producer-namespace-id';

USE datashare_db;

-- Three-part name
CALL datashare_db.public.refresh_summary('WEST');

-- Two-part name
CALL public.refresh_summary('WEST');

-- One-part name
SET search_path TO public;
CALL refresh_summary('WEST');
```

To stop sharing the procedure, revoke `EXECUTE` on it from the datashare.

```
-- On the producer
REVOKE EXECUTE ON PROCEDURE public.refresh_summary(varchar) FROM DATASHARE salesshare;
```

## How object names resolve
<a name="stored-procedure-data-sharing-names"></a>
+ One-part and two-part names in the procedure body resolve in the database set by `USE`, so `public.sales` refers to `datashare_db.public.sales`.
+ Three-part names resolve the same way as in any other statement that you run on the consumer. Use the consumer-side name of a shared database, such as `datashare_db`, or the name of a database local to the consumer.
+ The same rules apply to dynamic SQL that the procedure runs with `EXECUTE` and to procedures that it calls.

The following procedure compares a total in the shared table with a total in a table that is local to the consumer.

```
-- On the producer, in producer_db
CREATE PROCEDURE public.compare_totals(p_region varchar)
AS $$
DECLARE
  shared_total decimal(12,2);
  local_total decimal(12,2);
BEGIN
  SELECT SUM(amount) INTO shared_total
    FROM datashare_db.public.sales WHERE region = p_region;
  SELECT SUM(total) INTO local_total
    FROM consumer_db.public.regional_totals WHERE region = p_region;
  RAISE INFO 'shared: %, local: %', shared_total, local_total;
END;
$$ LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE public.compare_totals(varchar) TO DATASHARE salesshare;
```

```
-- On the consumer, in consumer_db
USE datashare_db;
CALL datashare_db.public.compare_totals('WEST');

INFO:  shared: 150.00, local: 150.00
```

## Writing to more than one database
<a name="stored-procedure-data-sharing-writes"></a>

A transaction can write to only one database. After `USE datashare_db`, writes that use one- or two-part names go to the shared database. To write to another database, the procedure commits the current transaction, runs `USE` to change the database context, and then writes with one- or two-part names. Run `COMMIT` immediately before each `USE` in the procedure body.

A `USE` or `RESET USE` in the procedure body applies to the statements that follow it, and stays in effect in your session after the procedure returns. After `RESET USE`, the statements run in the database that you're connected to on the consumer.

The following procedure updates a summary in the shared database and then writes a log row to a database local to the consumer.

```
-- On the producer, in producer_db
CREATE PROCEDURE public.summarize_and_log(p_region varchar)
AS $$
BEGIN
  DELETE FROM public.sales_summary WHERE region = p_region;
  INSERT INTO public.sales_summary
    SELECT region, SUM(amount) FROM public.sales WHERE region = p_region GROUP BY region;
  COMMIT;
  USE consumer_db;
  INSERT INTO public.run_log VALUES (p_region, GETDATE());
END;
$$ LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE public.summarize_and_log(varchar) TO DATASHARE salesshare;
```

```
-- On the consumer, in consumer_db
USE datashare_db;
CALL datashare_db.public.summarize_and_log('EAST');
SHOW USE;

 Use Database
--------------
 consumer_db
```

## Limitations
<a name="stored-procedure-data-sharing-limitations"></a>

The following limitations apply to procedures that you call across databases or through data sharing:
+ You can't call a procedure created with `SECURITY DEFINER`.
+ You can't call a `NONATOMIC` procedure through data sharing.
+ You can't call a procedure through a datashare that is shared with another AWS account, or through a datashare managed by Lake Formation.
+ You can't call a procedure in a database created from a datashare with the `WITH PERMISSIONS` clause.
+ You can't create, replace, or drop a procedure in another database. Run these commands in the database that contains the procedure.
+ You can't call a procedure through an external schema. Run `USE` instead.
+ The procedure can't use the `%TYPE` attribute.
+ Statements in the procedure behave the same way as when you run them against the other database or through data sharing, not as local statements. For example, `TRUNCATE` on a table in the shared database doesn't commit the transaction, so a later `ROLLBACK` in the procedure also undoes the `TRUNCATE`.