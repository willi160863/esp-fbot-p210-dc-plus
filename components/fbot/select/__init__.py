import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select
from esphome.const import CONF_OPTIONS
from .. import fbot_ns, Fbot, CONF_FBOT_ID

DEPENDENCIES = ["fbot"]
CONF_LIGHT_MODE = "light_mode"
CONF_AC_CHARGE_LIMIT = "ac_charge_limit"
CONF_DC_INPUT_MODE = "dc_input_mode"
FbotSelect = fbot_ns.class_("FbotSelect", select.Select, cg.Component)
LIGHT_MODE_OPTIONS = {"Off":0,"On":1,"SOS":2,"Flashing":3}
AC_CHARGE_LIMIT_DEFAULT_OPTIONS = ["300W","500W","700W","900W","1100W"]
DC_INPUT_MODE_OPTIONS = ["PV/MPPT", "DC Source"]

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_FBOT_ID): cv.use_id(Fbot),
    cv.Optional(CONF_LIGHT_MODE): select.select_schema(FbotSelect, icon="mdi:lightbulb-multiple"),
    cv.Optional(CONF_AC_CHARGE_LIMIT): select.select_schema(FbotSelect, icon="mdi:lightning-bolt").extend({
        cv.Optional(CONF_OPTIONS, default=AC_CHARGE_LIMIT_DEFAULT_OPTIONS): cv.All(cv.ensure_list(cv.string), cv.Length(min=5,max=5)),
    }),
    cv.Optional(CONF_DC_INPUT_MODE): select.select_schema(FbotSelect, icon="mdi:solar-power"),
})

async def to_code(config):
    parent = await cg.get_variable(config[CONF_FBOT_ID])
    if CONF_LIGHT_MODE in config:
        var = await select.new_select(config[CONF_LIGHT_MODE], options=list(LIGHT_MODE_OPTIONS.keys()))
        await cg.register_component(var, config[CONF_LIGHT_MODE]); cg.add(var.set_parent(parent)); cg.add(var.set_select_type("light_mode")); cg.add(parent.set_light_mode_select(var))
    if CONF_AC_CHARGE_LIMIT in config:
        ac_config=config[CONF_AC_CHARGE_LIMIT]; options=ac_config.get(CONF_OPTIONS,AC_CHARGE_LIMIT_DEFAULT_OPTIONS)
        var=await select.new_select(ac_config,options=options); await cg.register_component(var,ac_config); cg.add(var.set_parent(parent)); cg.add(var.set_select_type("ac_charge_limit")); cg.add(parent.set_ac_charge_limit_select(var))
    if CONF_DC_INPUT_MODE in config:
        var=await select.new_select(config[CONF_DC_INPUT_MODE],options=DC_INPUT_MODE_OPTIONS)
        await cg.register_component(var,config[CONF_DC_INPUT_MODE]); cg.add(var.set_parent(parent)); cg.add(var.set_select_type("dc_input_mode")); cg.add(parent.set_dc_input_mode_select(var))
