import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

DEPENDENCIES = []
CODEOWNERS = ["@JoseTaborda"]

# Definição das constantes necessárias
CONF_HX710B = "hx710b"
CONF_DOUT_PIN = "dout_pin"
CONF_CLK_PIN = "clk_pin"

hx710b_ns = cg.esphome_ns.namespace('hx710b')
HX710BSensor = hx710b_ns.class_('HX710BSensor', sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema(
    HX710BSensor,
    accuracy_decimals=2,
    unit_of_measurement="kg"
).extend({
    cv.Required(CONF_DOUT_PIN): cv.use_id(cg.GPIOPin),
    cv.Required(CONF_CLK_PIN): cv.use_id(cg.GPIOPin),
}).extend(cv.polling_component_schema('20s'))