# dictionaries = A changeable , unordered collection of unique key: value pairs they are fast because they use hashing, allows us to access a value quickly- mutable
# get()--> will get you the value of the key,update()-->key and the value or just update the value of the key or just update the key of the value  and pop()--> we mention key here and it removes the value
capitals = {'USA': 'Washington DC', 'India': 'New Delhi',
            'China': 'Beijing', 'Russia': 'Moscow'}
print(capitals['Russia'])
print(capitals.get('China'))
print(capitals.get('Germany'))
print(capitals.keys())
# capitals --> {USA: WASHINGTON DC}  HERE USA IS A KEY AND WASHINGTON DC IS A VALUE
print(capitals.values())
print(capitals.items())
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.update({'Korea': 'Beijing'})
for key, value in capitals.items():
    print(key, value)
capitals.pop('China')
capitals.clear()
