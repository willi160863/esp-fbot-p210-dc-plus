# AFERIY P210 DC Plus

Extension of ESP-FBot for experimental local control of the AFERIY P210 DC input settings.

## Added controls

- Holding register 15: DC input mode
  - `0` = `PV/MPPT`
  - `1` = `DC Source`
- Holding register 20: DC charge current
  - `1..20` = amperes

## ESPHome external component

```yaml
external_components:
  - source: github://willi160863/esp-fbot-p210-dc-plus
    refresh: 10s
```

## Number control

Add under the existing `number:` / `platform: fbot` block:

```yaml
    dc_charge_current:
      name: "DC Charge Current"
      min_value: 1
      max_value: 20
      step: 1
```

## Select control

Add under the existing `select:` / `platform: fbot` block:

```yaml
    dc_input_mode:
      name: "DC Input Mode"
```

The existing BR and WR installations do not need to use this fork. It is intended to be enabled only on the PO test installation first.

Important: validate the ESPHome configuration before flashing. The new controls are experimental and based on the identified P210 holding-register mapping.
