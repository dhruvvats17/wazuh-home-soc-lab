# Troubleshooting Notes

Use this as a record of symptoms, tests, root cause, and verified resolution.

| Symptom | Checks | Evidence to record |
|---|---|---|
| Agent appears disconnected | Service status, manager address, network reachability, agent logs | Before/after status and timestamps |
| Dashboard does not load | Service health, local reachability, browser error | Sanitized service output |
| Events missing | Correct channel, agent collection config, event timestamp, manager receipt | Source event and Wazuh search |
| Custom rule does not trigger | XML syntax, rule ID, parent rule/decoder, matching fields, test event | Syntax validation and actual alert |
| Test traffic is not visible | Firewall policy, routing, service listener, correct interface | Authorized test details and logs |

Do not record a cause as confirmed until a test supports it. Remove private addresses and sensitive output from public evidence where unnecessary.
