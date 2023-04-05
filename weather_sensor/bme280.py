import board
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

while True:
    print("Temperature: %0.1f C" % bme280.temperature)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Humidity: %0.1f %%" % bme280.humidity)
