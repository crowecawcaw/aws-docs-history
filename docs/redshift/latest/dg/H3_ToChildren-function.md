Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# H3_ToChildren

H3_ToChildren returns a list of child H3 cell IDs at a specified resolution for a given H3 index.
For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_ToChildren(*index*, *resolution*)
```

## Arguments

_index_

A value of data type `BIGINT` or `VARCHAR` that represents the index of an H3 cell, or an expression that evaluates to one of these data types.

_resolution_

A value of data type `INTEGER` or an expression that evaluates to an `INTEGER` type. The value represents the resolution of the children cell IDs. The value must be an integer between the resolution of the input _index_ and 15, inclusive.

## Return type

`SUPER` – represents a list of H3 cell IDs.

If either _index_ or _resolution_ is NULL, then NULL is returned.

If _index_ is not valid, then an error is returned.

If _resolution_ is not between the resolution of _index_ and 15, inclusive, then an error is returned.

If the output size exceeds the maximum SUPER size limit, then an error is returned.

## Examples

The following SQL inputs a VARCHAR that represents the index of an H3 cell, and an INTEGER that represents the desired resolution of all the children, and returns a SUPER array containing the children at resolution 6.

```
SELECT H3_ToChildren('85283473fffffff', 6);
```

```

 h3_tochildren
--------------------------------------------------------------------------------------------------------------------------------------
 [604189641121202175,604189641255419903,604189641389637631,604189641523855359,604189641658073087,604189641792290815,604189641926508543]

```

The following SQL inputs a BIGINT that represents the index of an H3 cell, and an INTEGER that represents the desired resolution of all the children, and returns a SUPER array containing the children at resolution 6.

```
SELECT H3_ToChildren(599686042433355775, 6);
```

```

 h3_tochildren
--------------------------------------------------------------------------------------------------------------------------------------
 [604189641121202175,604189641255419903,604189641389637631,604189641523855359,604189641658073087,604189641792290815,604189641926508543]

```

Note: A difference of 7 or less between _resolution_ and _index_ resolution is safe.

The following example demonstrates a workaround for queries that exceed the SUPER size limit. When the resolution difference between the input H3 index and the desired child resolution is too large (greater than 7). This procedure solves the problem by incrementally expanding children in smaller steps (maximum 5 resolution levels at a time) and storing the final results in a user-created table.

```
CREATE OR REPLACE PROCEDURE generate_h3_children()
LANGUAGE plpgsql
AS $$
BEGIN
    -- Drop and create h3_children table that will contain the results
    DROP TABLE IF EXISTS h3_children;
    CREATE TABLE h3_children (
        h3_index BIGINT,
        child_res INTEGER,
        children SUPER
    );

    -- Create temporary table for steps
    DROP TABLE IF EXISTS h3_steps;
    CREATE TABLE h3_steps (
        h3_index BIGINT,
        current_res INTEGER,
        target_res INTEGER,
        h3_array SUPER
    );

    -- Initial insert into h3_steps
    INSERT INTO h3_steps
    SELECT h3_index, H3_Resolution(h3_index), child_res, ARRAY(h3_index)
    FROM h3_indexes; -- Insert from your table with h3_index and child_res as columns

    -- Loop until we reach target resolution
    -- We expect at most 3 iterations considering that we can start at resolution
    -- 0 and target/child resolution equal to 15 (0 -> 5 -> 10 -> 15)
    WHILE EXISTS (
        SELECT 1
        FROM h3_steps h
        GROUP BY h3_index, target_res
        HAVING MAX(current_res) < target_res
    ) LOOP
        -- Populate the h3_steps table with the tables that need to
        -- reach closer to the target res
        INSERT INTO h3_steps
        SELECT
            h.h3_index,
            LEAST(h.current_res + 5, h.target_res), -- Do not exceed target res
            h.target_res,
            -- Take the children of the child cell at resolution current_res of the
            -- h3_index
            H3_ToChildren(c.child::BIGINT, LEAST(h.current_res + 5, h.target_res))
        FROM h3_steps h, UNNEST(h.h3_array) AS c(child)
        WHERE h.current_res < h.target_res
        AND h.current_res = (SELECT MAX(current_res)
                           FROM h3_steps
                           WHERE h3_index = h.h3_index
        );
    END LOOP;

    -- Store final results
    INSERT INTO h3_children
    SELECT h3_index AS h3_index, target_res AS child_res, h3_array AS children
    FROM h3_steps
    WHERE current_res = target_res;
END;
$$;

-- Create the source table for H3_ToChildren queries
CREATE TABLE h3_indexes (
    h3_index BIGINT,
    child_res INTEGER,
    PRIMARY KEY (h3_index, child_res)
);
INSERT INTO h3_indexes (h3_index, child_res)
VALUES (x'8001fffffffffff'::BIGINT, 11);

-- Execute the procedure
CALL generate_h3_children();

-- View results
SELECT * FROM h3_children;
```
