from OmegaExpansion import onionI2C
import time
import sys
print 'Starting: onionI2C module testing...'
i2c     = onionI2C.OnionI2C(0)
# set the verbosity
i2c.setVerbosity(1)
value = [0x00]
data = i2c.writeBytes(0x21, 0x00, value)
while True:
        time.sleep(0.5)
        value1 = [0xFF]
        data = i2c.writeBytes(0x21, 0x09, value1)
        print "Turning all Relays ON"
        time.sleep(1)
        data = i2c.writeBytes(0x21, 0x09, value)
        print "Turning all Relays OFF"
        time.sleep(1)
        print "\n"

