# Windows Wazuh Agent

## Purpose
Document endpoint enrollment and telemetry delivery from Windows to Wazuh.

## Known lab notes
A Windows endpoint named `Window-Victim` was previously listed as an active Wazuh agent. Agent state can change, so capture fresh evidence before claiming it is currently connected.

## Validation
1. Open the Wazuh Dashboard and inspect the agent status.
2. On Windows, check the Wazuh Agent service in Services.
3. Verify the configured manager address and connectivity using the local configuration.
4. Generate a harmless test event and confirm it reaches Wazuh.
5. Record timestamp, source, relevant fields, and screenshot.

## Evidence
Save a redacted screenshot as `screenshots/agents-status.png`. Do not include credentials or unnecessary host details.
