def get_integer(help_text):
  return int(input(help_text))

primary = True
num = get_integer("Please enter a number: ")
if num == 1:
  print "The number",num, "is primary"
else:
  for i in range(2,num-1):
    if num % i==0:
      primary = False
      break
    else:
      continue
  if primary==True:
    print "Thr number",num, "is primary"
  else: 
    print "The number",num, "is NOT primary"

