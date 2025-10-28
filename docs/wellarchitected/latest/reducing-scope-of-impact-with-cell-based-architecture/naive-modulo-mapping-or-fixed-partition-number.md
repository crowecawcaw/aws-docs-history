# Naïve modulo mapping or

fixed partition number

Naïve modulo mapping uses modular arithmetic to map keys to cells, typically on a
cryptographic hash of the key. This scheme has an effective zero peak-to-average ratio (very
even distribution) and requires minimal state (just the count of cells). But it suffers from
high churn (cell reassignment) when adding or removing cells.

Advantages:

- Simple to implement.
- Avoids hot cells.
  Disadvantages:

- Changing the number of cells requires the rebalance of all cells and their
  customers and tenants.
