from hide_text import hide_text
from reveal_text import reveal_text

# Hide the message
hide_text("sample_image.png", "output_image.png", "This is the hidden message", "mypassword123")

# Reveal the message
print(reveal_text("output_image.png", "mypassword123"))
