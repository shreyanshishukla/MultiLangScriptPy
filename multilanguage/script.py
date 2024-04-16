from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
text = input("Enter a word: ")


language_map=[
          "en_US",
          'en_GB' ,
          'nl_NL' ,
          'es_ES' ,
          'de_DE' ,
          'pt_BR' ,
          'pt_PT' ,
          'ru_RU' ,
          'hr_HR' ,
          'fi_FI' ,
          'fr_FR' ,
          'da_DK' ,
          'sv_SE' ,
          'uk_UA' ,
          'sl_SI' ,
          'it_IT' 
]
output={}
for lang in language_map:
    translation = translator.translate(text, dest=lang)
    output[lang]=translation.text

print("Translation:\n", output)