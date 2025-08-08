import esphome.codegen as cg
from esphome.components import sensor
from esphome.const import CONF_ID

hx710b_ns = cg.esphome_ns.namespace("hx710b")

CONFIG_SCHEMA = sensor.SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(HX710BSensor),
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)