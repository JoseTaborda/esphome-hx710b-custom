import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

# Adicione estas linhas:
hx710b_ns = cg.esphome_ns.namespace('hx710b')
HX710BSensor = hx710b_ns.class_('HX710BSensor', sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = sensor.SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(HX710BSensor),
})