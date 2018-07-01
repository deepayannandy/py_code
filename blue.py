######################### DNY ##################################
import bluetooth

print('Searching for device.......')
defid= '00:21:13:00:53:27'

nearby_devices= bluetooth.discover_devices(lookup_names = True)

print('found %d devices'% len(nearby_devices))

for addr, name in nearby_devices:
    print('%s - %s'%(addr, name))
    if defid in addr:
        print('Trusted device found!!!!!! mac id matched')
    else:
        pass
        
