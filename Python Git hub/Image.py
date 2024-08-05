#1.
from PIL import Image

# Open an image file
image_path = r"C:\Users\abise\OneDrive\Pictures\1 (1).jpg"
img = Image.open(image_path)

# Display the image
img.show()
#2a.[VVI] Program To Change the Dimension of an image
def Resize(width,height,input_path,output_path):
    from PIL import Image
    image=Image.open(input_path)
    resize_image=image.resize((width,height))
    resize_image.save(output_path)
    print("Image Re-sized successfully")
input_path=input("Enter The Input Path: ")
output_path=input("Enter The Output Path: ")
width=int(input("Enter Desired Width: "))
height=int(input("Enter Desired Height: "))
Resize(width,height,input_path,output_path)
#2b.[VVI] Program To Change the Dimension of an image
from PIL import Image

def resize_image(input_path, output_path, width, height):
    """
    Resize an image to the specified width and height.
    
    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the resized image.
        width (int): Desired width of the resized image.
        height (int): Desired height of the resized image.
    """
    # Open the image
    image = Image.open(input_path)
    
    # Resize the image
    resized_image = image.resize((width, height))
    
    # Save the resized image
    resized_image.save(output_path)
    
    print(f"Image resized and saved to {output_path}")

if __name__ == "__main__":
    # Provide input and output paths along with desired width and height
    input_path = r"C:\Users\abise\OneDrive\Pictures\c.jpg"
    output_path = r"C:\Users\abise\OneDrive\Pictures\c.jpg"
    width = 1280
    height = 180
    
    # Resize the image
    resize_image(input_path, output_path, width, height)
#3. audio file implementation
import pygame

# Initialize Pygame 
pygame.init()#manually initializing the init function because it is not part of any class

# Specify the path to your audio file
audio_path = r"C:\Users\abise\Music\(webmusic.in)_Pehli-Nazar-Mein.mp3"

# Load the audio file
pygame.mixer.music.load(audio_path)

# Play the audio file
pygame.mixer.music.play()

# Add a delay to allow the audio to play (adjust the duration as needed)
pygame.time.delay(5000)  # 5000 milliseconds (5 seconds)

# # Stop the audio playback
# pygame.mixer.music.stop()

# Quit Pygame
pygame.quit()



