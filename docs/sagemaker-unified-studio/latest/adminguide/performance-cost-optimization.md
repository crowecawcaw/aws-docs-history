# Performance and cost optimization

## File size limitations

Files over 15 MB cannot be directly uploaded to shared folders through the Amazon SageMaker Unified Studio interface in space-based tools
like JupyterLab and Code Editor. Large files must be uploaded to local folder in JupyterLab first, then copy or move to
the shared folder if needed.

## Cost management considerations

Heavy file read/write workloads in shared storage can incur additional S3 access costs, while frequent S3 operations may
affect performance for collaborative workflows.

**For space-based tools (like JupyterLab):** Apart from the shared folder, space-based tools
such as JupyterLab and Code Editor also have an EBS-based personal folder per user per project. We recommend using this local
storage for intermediate and temporary files during development work, as it provides superior performance for frequent file
operations. Only move final versions of files that are ready for sharing with other project users to the S3 shared folder.
This approach minimizes S3 operations and associated costs while maintaining optimal performance for iterative development work.

###### Note

This storage strategy applies specifically to space-based tools like JupyterLab and Code Editor that have
access to both local EBS storage and shared storage. For web-based tools like Query Editor, intermediate or
temporary files are generated during normal operation, but since these tools don't have a dedicated personal
folder, all files are saved directly to shared storage. Web-based tools rely entirely on the shared storage
for file operations and don't have the option to use local EBS storage for performance optimization.
