# Chapter 7 Studio examples:

``` python
import image
import random

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(3, img.getWidth() - 2):
    for j in range(1, img.getHeight() - 2):
        # we are at pixel (i, j)
        dx = random.randrange(-1, 1) # generates one of -1, 0, +1
        dy = random.randrange(-1, 1) 
        
        new_x = i + dx
        new_y = j + dy
        
        #pick a random neighbor
        nx = random.randint(i-1, i+1) #generates one of i-1, i+1
        ny = random.randint(j-1, j+1)
        
        #set this pixel to neighbor's color
        neighbor_color = img.getPixel(nx, ny)
        newimg.setPixel(i, j, neighbor_color)

newimg.draw(win)
win.exitonclick()

```
