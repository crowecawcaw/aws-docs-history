

# Troubleshooting and FAQ
<a name="sd-troubleshooting"></a>

## Common issues
<a name="sd-common-issues"></a>


| Issue | Resolution | 
| --- | --- | 
| Search returns no results | Broaden your query. Check enrichment is complete. Verify workspace contains matching data. | 
| Low confidence scores | Query might be too specific. Break into simpler sub-queries. Upload annotations to improve enrichment. | 
| Ingestion stuck or failed | Check supported format (Parquet, MP4, OpenLABEL). Verify S3 permissions. | 
| Slow search performance | Use structured filters to narrow search space. Clear browser cache. | 
| Video segments won't play | Use Chrome for broadest codec support. Check network connectivity. | 

## Frequently asked questions
<a name="sd-faq"></a>

### How does Scenario Discovery protect my data?
<a name="sd-faq-data-protection"></a>

All data is encrypted at rest and in transit. Workspaces are isolated per customer. Data residency is maintained within the selected AWS region.

### Can multiple team members share a workspace?
<a name="sd-faq-share-workspace"></a>

Yes. Workspace admins invite members with role-based access (Workspace Admin, Data Wrangler, Data Curator, ML Engineer).

### How long does enrichment take?
<a name="sd-faq-enrichment-time"></a>

Enrichment processing time is measured by video duration, not file size. Under ideal conditions with no other system load, approximately 100 hours of video completes in 25–30 minutes. Actual processing time depends on the current GPU queue backlog; if other enrichment jobs are running, wait times increase accordingly.

### Can I use my own annotations?
<a name="sd-faq-custom-annotations"></a>

Custom annotation formats are not supported. Upload your annotations in OpenLABEL format.

### What simulation tools are supported?
<a name="sd-faq-simulation"></a>

Scenario Discovery does not integrate directly with simulation tools. Export your curated dataset to your own S3 bucket and connect your tools from there.

### Are there limits in the system?
<a name="sd-faq-limits"></a>

Yes, Scenario Discovery applies default limits across all resources and operations. Most of these limits are adjustable. For detailed information on specific limits and how to request adjustments, refer to the separate limits document that your AWS contact can share with you.