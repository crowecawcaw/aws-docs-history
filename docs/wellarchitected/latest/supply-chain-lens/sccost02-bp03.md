# SCCOST02-BP03 Only store useful data and discard the rest

A well-designed supply chain data management architecture
incorporates a data lake to store processed and normalized useful
data, while raw data is either discarded or archived in
cost-effective storage for potential future needs.

**Desired outcome:** Data lifecycle
is well defined as per business and regulatory requirements.

**Benefits of establishing this best
practice:** Reduced cost, optimized performance, and
better customer satisfaction

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Implement data sanitization to identify, clean, and validate
critical information before cloud transfer, while pre-processing
data to improve bandwidth efficiency, reduce storage costs, and
support high-quality, secure cloud data.

Use edge computing for local analytics and decision-making,
prioritizing critical data for immediate cloud transmission.

### Implementation steps

1. Establish data classification and retention policies that
   define what data should be kept, archived, or discarded
   based on business and regulatory requirements.
2. Implement automated data sanitization processes to clean
   and validate data before storage, removing unnecessary or
   redundant information.
3. Deploy edge computing solutions for local data processing
   and filtering, transmitting only essential data to the
   cloud.
4. Configure automated data lifecycle management to archive
   or delete data according to established retention
   policies.
5. Implement data quality monitoring to make sure only
   valuable, accurate data is retained in storage systems.
6. Regularly review and optimize data retention policies
   based on changing business needs and regulatory
   requirements.
