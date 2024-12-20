import art

def format_text(text, style):
    """Formats the input text based on the specified style ('uppercase', 'lowercase', 'title')."""
    styles = {"uppercase" : text.upper(), "lowercase" : text.lower(), "title" : text.title()}

    if style in styles:
        return styles.get(style)
    else:
        return "Style not found."

def main():
    """Runs the main loop of the text formatting application."""
    text_example = "Example Text"
    styles = {"Uppercase": text_example.upper(), "Lowercase": text_example.lower(), "Title": text_example.title()}
    while True:
        print(art.logo)
        print("\nAvailable styles with examples:")
        i = 1
        for style, example in styles.items():
            print(f"{i}. {style}: {example}")
            i += 1

        print("=" * 50)

        text = input("Enter your text: ")
        style = input("Enter your style (eg. 'uppercase'): ")

        print(format_text(text, style))

        close_app = input("\nDo you want try again? 'y' or 'n': ")
        print("\n" * 20)
        if close_app != 'y':
            print(f"Thank you for using this app.")
            break

main()