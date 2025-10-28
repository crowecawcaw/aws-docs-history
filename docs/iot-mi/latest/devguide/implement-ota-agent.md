# Implement OTA agent

When you receive the job document from managed integrations, you must have an implementation of your own
OTA agent that processes the job document, downloads updates, and performs any installation operations.
The OTA Agent needs to perform the following steps:

1. Parse job documents for firmware Amazon S3 URLs.
2. Download firmware updates through HTTP.
3. Verify digital signatures.
4. Install validated updates.
5. Call `iotmi\_JobsHandler\_updateJobStatus` with `SUCCESS` or
   `FAILED` status.
   When your device successfully completes the OTA operation, it must call the
   `iotmi\_JobsHandler\_updateJobStatus` API with a status of `JobSucceeded`
   to report a successful job.

```
/**
 * @brief Enumeration of possible job statuses.
 */
typedef enum{
    JobQueued,     /** The job is in the queue, waiting to be processed. */
    JobInProgress, /** The job is currently being processed. */
    JobFailed,     /** The job processing failed. */
    JobSucceeded,  /** The job processing succeeded. */
    JobRejected    /** The job was rejected, possibly due to an error or invalid request. */
} iotmi_JobCurrentStatus_t;

/**
 * @brief Update the status of a job with optional status details.
 *
 * @param[in] pJobId Pointer to the job ID string.
 * @param[in] jobIdLength Length of the job ID string.
 * @param[in] status The new status of the job.
 * @param[in] statusDetails Pointer to a string containing additional details about the job status.
 *                          This can be a JSON-formatted string or NULL if no details are needed.
 * @param[in] statusDetailsLength Length of the status details string. Set to 0 if `statusDetails` is NULL.
 *
 * @return 0 on success, non-zero on failure.
 */
int iotmi_JobsHandler_updateJobStatus( const char * pJobId,
                                        size_t jobIdLength,
                                        iotmi_JobCurrentStatus_t status,
                                        const char * statusDetails,
                                        size_t statusDetailsLength );
```
