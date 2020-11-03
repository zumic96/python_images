from PIL import Image

words = Image.open('word_matrix.png')
mask_image = Image.open('mask.png')
resized_mask = mask_image.resize(words.size)
resized_mask.putalpha(128)
words.paste(resized_mask,(0,0),resized_mask)
words.show()