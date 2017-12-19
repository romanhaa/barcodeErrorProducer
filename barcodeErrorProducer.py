with open('input.txt') as barcode_file:
    barcode_list = barcode_file.readlines()

barcode_list = [x.strip() for x in barcode_list]

for x in range(0, len(barcode_list)):
  barcode = barcode_list[x]
  barcode_errors = []
  for y in range(0, len(barcode)):
    barcode_temp = list(barcode)
    if barcode[y] == 'A':
      barcode_temp[y] = 'C'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'G'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'T'
      barcode_errors.append(''.join(list(barcode_temp)))
    if barcode[y] == 'C':
      barcode_temp[y] = 'A'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'G'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'T'
      barcode_errors.append(''.join(list(barcode_temp)))
    if barcode[y] == 'G':
      barcode_temp[y] = 'A'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'C'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'T'
      barcode_errors.append(''.join(list(barcode_temp)))
    if barcode[y] == 'T':
      barcode_temp[y] = 'A'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'C'
      barcode_errors.append(''.join(list(barcode_temp)))
      barcode_temp[y] = 'G'
      barcode_errors.append(''.join(list(barcode_temp)))
  barcode_errors = ','.join(barcode_errors)
  output = '\t'.join([barcode, barcode_errors])
  with open('output.txt', 'a') as the_file:
    the_file.write(output+'\n')
