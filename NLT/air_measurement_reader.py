file = open("sodaq-air-measurements.csv", 'r')
lines = file.readlines()

column_names = lines[0].split(',')
raw_lines = lines[1:]
processed_data = []
x = 1

# // split line and seperate into names
for i, line in enumerate(raw_lines):
    line_data = {}
    values = line.split(',')

    # // Assign a name to every value in a data row
    for value, name in zip(values, column_names):
        line_data[name] = value

    processed_data.append(line_data)


# // go through lines and filter out the wanted data
for line_data in processed_data:

    # // Check if data was gathered during the correct hour
    if line_data['hour\n'] == '15\n':

        lat = line_data['lat']
        lon = line_data['lon']
        temp = line_data['temp_avg']
        pm_25 = line_data['pm_2_5_avg']
        pm10 = line_data['pm_10_avg']

        print(f'meting {x}: coordinaten: ({lat}, {lon}), temperatuur: {temp}, pm2.5: {pm_25}, pm10: {pm10}')
        x += 1