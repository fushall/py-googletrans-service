import googletrans


def google_translate(text: str, src_lang: str = 'auto', dest_lang: str = 'en') -> str:
    translator = googletrans.Translator(service_urls=['translate.google.cn'])
    result = translator.translate(text=text, src=src_lang, dest=dest_lang)
    return result.text
