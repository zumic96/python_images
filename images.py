from PIL import Image
# Open image
mac = Image.open('example.jpg')
# Show image and get info
mac.show()
mac.size
mac.filename
mac.format_description

# Cropping
mac.crop((0,0,100,100))
pencils = Image.open('pencils.jpg')
pencils.size
# TOP pencils
x = 0
y = 0
w = 1950/3
h = 1300/10
pencils.crop((x,y,w,h))
# BOTTOM pencils
x = 0
y = 1100
w = 1950/3
h = 1300
pencils.crop((x,y,w,h))
# Grab computer
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
mac.crop((x,y,w,h))

# Paste
computer = mac.crop((x,y,w,h))
mac.paste(im=computer, box=(0,0))
mac.paste(im=computer, box=(796,0))
mac.show()

# Resize
mac.size
mac.resize((3000,500))

# Rotate
mac.rotate(90)

# Transparency
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

blue.putalpha(0)
blue.putalpha(128)
blue.putalpha(255)
blue.show()

red.putalpha(0)
red.putalpha(128)
red.putalpha(255)
red.show()

blue.paste(im=red,box=(0,0),mask=red)
blue.show()

blue.save("purple.png")