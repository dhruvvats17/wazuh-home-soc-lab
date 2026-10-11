# Case 003 — Windows Process Event Review

**Status:** Evidence collection required

## Objective
Review a Sysmon process-creation event and determine whether it is expected or requires further investigation.

## Evidence to collect
- Sysmon Event ID and timestamp
- Process image and parent process
- Command line and user, if recorded and safe to disclose
- Corresponding Wazuh event, if collected
- Related events that provide context

## Analysis
A process-creation event is not automatically malicious. Consider the executable path, parent-child relationship, command line, signature/reputation where available, user context, and surrounding activity.

## Conclusion
[Document only conclusions supported by the observed evidence.]
