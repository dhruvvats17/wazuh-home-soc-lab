# Sysmon and Windows Event Logging

## Purpose
Sysmon adds detailed telemetry useful for endpoint investigation. Windows Event Logs provide additional operating-system and security context. Availability depends on configuration and audit policy.

## Known lab notes
The lab notes recorded Sysmon Event ID 1 (process creation) during a benign process test. Re-run the test and capture a fresh event before presenting it as current evidence.

## Validation workflow
1. Open Event Viewer.
2. Navigate to `Applications and Services Logs → Microsoft → Windows → Sysmon → Operational`.
3. Filter or locate Event ID 1.
4. Inspect the event timestamp, image/process path, command line if recorded, parent process, and user fields as appropriate.
5. Correlate the event with Wazuh only if the relevant channel is configured for collection.
6. Redact usernames, paths, and other sensitive details before publishing.

## Important
A Sysmon event visible in Event Viewer does not automatically mean that Wazuh received it. Validate both sides independently.
