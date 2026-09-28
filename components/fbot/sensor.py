import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    CONF_BATTERY_LEVEL,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_FREQUENCY,
    STATE_CLASS_MEASUREMENT,
    UNIT_PERCENT,
    UNIT_WATT,
    UNIT_KILOWATT_HOURS,
    UNIT_MINUTE,
    UNIT_VOLT,
    UNIT_HERTZ,
)
from . import fbot_ns, Fbot, CONF_FBOT_ID

DEPENDENCIES = ["fbot"]

CONF_INPUT_POWER = "input_power"
CONF_AC_INPUT_POWER = "ac_input_power"
CONF_DC_INPUT_POWER = "dc_input_power"
CONF_OUTPUT_POWER = "output_power"
CONF_SYSTEM_POWER = "system_power"
CONF_TOTAL_POWER = "total_power"
CONF_REMAINING_TIME = "remaining_time"
CONF_BATTERY_S1_LEVEL = "battery_s1_level"
CONF_BATTERY_S2_LEVEL = "battery_s2_level"
CONF_THRESHOLD_CHARGE = "threshold_charge"
CONF_THRESHOLD_DISCHARGE = "threshold_discharge"
CONF_CHARGE_LEVEL = "charge_level"
CONF_AC_OUT_VOLTAGE = "ac_out_voltage"
CONF_AC_OUT_FREQUENCY = "ac_out_frequency"
CONF_AC_IN_FREQUENCY = "ac_in_frequency"
CONF_TIME_TO_FULL = "time_to_full"
CONF_USB_A1_POWER = "usb_a1_power"
CONF_USB_A2_POWER = "usb_a2_power"
CONF_USB_C1_POWER = "usb_c1_power"
CONF_USB_C2_POWER = "usb_c2_power"
CONF_USB_C3_POWER = "usb_c3_power"
CONF_USB_C4_POWER = "usb_c4_power"
CONF_DC_INPUT_MODE_RAW = "dc_input_mode_raw"
CONF_DC_CHARGE_CURRENT_RAW = "dc_charge_current_raw"
CONF_AC_CHARGE_APPOINTMENT_RAW = "ac_charge_appointment_raw"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_FBOT_ID): cv.use_id(Fbot),
        cv.Optional(CONF_BATTERY_LEVEL): sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=1, device_class=DEVICE_CLASS_BATTERY, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_BATTERY_S1_LEVEL): sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=1, device_class=DEVICE_CLASS_BATTERY, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_BATTERY_S2_LEVEL): sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=1, device_class=DEVICE_CLASS_BATTERY, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_INPUT_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=0, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_AC_INPUT_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=0, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_DC_INPUT_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=0, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_OUTPUT_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=0, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_SYSTEM_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=0, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_TOTAL_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=0, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_REMAINING_TIME): sensor.sensor_schema(unit_of_measurement=UNIT_MINUTE, accuracy_decimals=0, device_class=DEVICE_CLASS_DURATION, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_THRESHOLD_CHARGE): sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=0, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_THRESHOLD_DISCHARGE): sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=0, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_CHARGE_LEVEL): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=0, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_AC_OUT_VOLTAGE): sensor.sensor_schema(unit_of_measurement=UNIT_VOLT, accuracy_decimals=2, device_class=DEVICE_CLASS_VOLTAGE, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_AC_OUT_FREQUENCY): sensor.sensor_schema(unit_of_measurement=UNIT_HERTZ, accuracy_decimals=2, device_class=DEVICE_CLASS_FREQUENCY, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_AC_IN_FREQUENCY): sensor.sensor_schema(unit_of_measurement=UNIT_HERTZ, accuracy_decimals=3, device_class=DEVICE_CLASS_FREQUENCY, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_TIME_TO_FULL): sensor.sensor_schema(unit_of_measurement=UNIT_MINUTE, accuracy_decimals=0, device_class=DEVICE_CLASS_DURATION, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_USB_A1_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_USB_A2_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_USB_C1_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_USB_C2_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_USB_C3_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_USB_C4_POWER): sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_DC_INPUT_MODE_RAW): sensor.sensor_schema(accuracy_decimals=0, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_DC_CHARGE_CURRENT_RAW): sensor.sensor_schema(accuracy_decimals=0, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_AC_CHARGE_APPOINTMENT_RAW): sensor.sensor_schema(accuracy_decimals=0, state_class=STATE_CLASS_MEASUREMENT),
    }
)

async def to_code(config):
    parent = await cg.get_variable(config[CONF_FBOT_ID])
    mappings = [
        (CONF_BATTERY_LEVEL, parent.set_battery_percent_sensor),
        (CONF_BATTERY_S1_LEVEL, parent.set_battery_percent_s1_sensor),
        (CONF_BATTERY_S2_LEVEL, parent.set_battery_percent_s2_sensor),
        (CONF_INPUT_POWER, parent.set_input_power_sensor),
        (CONF_AC_INPUT_POWER, parent.set_ac_input_power_sensor),
        (CONF_DC_INPUT_POWER, parent.set_dc_input_power_sensor),
        (CONF_OUTPUT_POWER, parent.set_output_power_sensor),
        (CONF_SYSTEM_POWER, parent.set_system_power_sensor),
        (CONF_TOTAL_POWER, parent.set_total_power_sensor),
        (CONF_REMAINING_TIME, parent.set_remaining_time_sensor),
        (CONF_THRESHOLD_CHARGE, parent.set_threshold_charge_sensor),
        (CONF_THRESHOLD_DISCHARGE, parent.set_threshold_discharge_sensor),
        (CONF_CHARGE_LEVEL, parent.set_charge_level_sensor),
        (CONF_AC_OUT_VOLTAGE, parent.set_ac_out_voltage_sensor),
        (CONF_AC_OUT_FREQUENCY, parent.set_ac_out_frequency_sensor),
        (CONF_AC_IN_FREQUENCY, parent.set_ac_in_frequency_sensor),
        (CONF_TIME_TO_FULL, parent.set_time_to_full_sensor),
        (CONF_USB_A1_POWER, parent.set_usb_a1_power_sensor),
        (CONF_USB_A2_POWER, parent.set_usb_a2_power_sensor),
        (CONF_USB_C1_POWER, parent.set_usb_c1_power_sensor),
        (CONF_USB_C2_POWER, parent.set_usb_c2_power_sensor),
        (CONF_USB_C3_POWER, parent.set_usb_c3_power_sensor),
        (CONF_USB_C4_POWER, parent.set_usb_c4_power_sensor),
        (CONF_DC_INPUT_MODE_RAW, parent.set_dc_input_mode_raw_sensor),
        (CONF_DC_CHARGE_CURRENT_RAW, parent.set_dc_charge_current_raw_sensor),
        (CONF_AC_CHARGE_APPOINTMENT_RAW, parent.set_ac_charge_appointment_raw_sensor),
    ]
    for key, setter in mappings:
        if key in config:
            sens = await sensor.new_sensor(config[key])
            cg.add(setter(sens))
