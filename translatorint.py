from googletrans import Translator

class UniversalTranslator:
    def __init__(self):
       
        self.translator = Translator()

    def translate(self, text, target_language='en'):
        try:
         
            translation = self.translator.translate(text, dest=target_language)
            return translation.text
        except Exception as e:
            return f"Translation failed: {str(e)}"

def main():
    translator = UniversalTranslator()

    while True:
      
        user_input = input("Enter a word or phrase (or 'exit' to quit): ")

    
        if user_input.lower() == 'exit':
            break

        
        result = translator.translate(user_input, target_language='de')
        print(f"Translation: {result}\n")

if __name__ == "__main__":
    main()
