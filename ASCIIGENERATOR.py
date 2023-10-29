import pyfiglet
import pyperclip

def list_available_fonts():
    return pyfiglet.FigletFont.getFonts()

def generate_ascii_art(text, font):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    available_fonts = list_available_fonts()
    
    print("Available fonts:")
    for i, font in enumerate(available_fonts, start=1):
        print(f"{i}. {font}")
    
    font_number = input("Enter the number of the font you want to use: ")
    
    try:
        font_number = int(font_number)
        if 1 <= font_number <= len(available_fonts):
            selected_font = available_fonts[font_number - 1]
            
            input_text = input("Enter the text you want to convert to ASCII art: ")
            ascii_art = generate_ascii_art(input_text, selected_font)
            
            print(ascii_art)
            
            copy_to_clipboard = input("Copy the ASCII art to the clipboard? (y/n): ").strip().lower()
            if copy_to_clipboard == 'y':
                pyperclip.copy(ascii_art)
                print("ASCII art copied to clipboard.")
        else:
            print("Invalid font number.")
    except ValueError:
        print("Please enter a valid number.")
