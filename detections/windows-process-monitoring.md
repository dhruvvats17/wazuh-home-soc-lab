# Detection Note: Windows Process Monitoring

## Objective
Use Sysmon process-creation telemetry to understand how endpoint activity can be investigated.

## Data source
Sysmon Operational log, especially Event ID 1 where process creation logging is enabled. Wazuh visibility depends on the endpoint collection configuration.

## Test
1. Start a known benign application in the lab.
2. Find the corresponding Sysmon event.
3. Verify whether the same event is present in Wazuh.
4. Record relevant fields and the exact timestamp.
5. Do not label a benign test process malicious.

## Expected analysis
Review process image, parent process, command line (if logged), user, timestamp, and related events. Assess whether the process is expected in context.

## Status
Template prepared. Mark as validated only after attaching real Event Viewer and Wazuh evidence.
