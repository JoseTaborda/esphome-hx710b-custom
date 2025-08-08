import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor

CODEOWNERS = ["@yourgithubusername"]
DEPENDENCIES = []

hx710b_ns = cg.esphome_ns.namespace("hx710b")
HX710BSensor = hx710b_ns.class_("HX710BSensor", sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema(
    HX710BSensor,
    unit_of_measurement="kg",
    accuracy_decimals=2,
).extend({
    cv.Required("dout_pin"): cv.use_id(cg.GPIOPin),
    cv.Required("clk_pin"): cv.use_id(cg.GPIOPin),
}).extend(cv.polling_component_schema("60s"))