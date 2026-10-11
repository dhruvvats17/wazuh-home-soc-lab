# Detection Note: Firewall Events

## Objective
Validate that the configured Windows firewall log source and Wazuh rule identify the intended test event.

## Validation steps
1. Confirm the exact Windows firewall logging/event source used.
2. Generate an authorized, controlled test matching the rule condition.
3. Confirm the original event exists in Windows.
4. Confirm the event reaches Wazuh.
5. Inspect the alert rule ID, level, decoder, and matched fields.
6. Test a non-matching event to look for false positives.
7. Save redacted evidence for each stage.

## Result
The lab notes mention work on a custom TCP DROP-related rule and syntax testing. Do not claim end-to-end detection until the matching event and resulting alert have both been observed and documented.

## Caution
Rule IDs, levels, and field names must be checked against the actual local rule and event. Do not copy a sample rule blindly into production.
