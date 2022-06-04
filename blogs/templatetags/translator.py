from django import template
from deep_translator import GoogleTranslator



uz = 'uz'
ru = 'ru'
en = 'en'
register = template.Library()

@register.filter(name='translate_uz')
def translate_uz(arg):
    return GoogleTranslator(source='auto', target=f'{uz}').translate(f'{arg}')

@register.filter(name='translate_ru')
def translate_ru(arg):
    return GoogleTranslator(source='auto', target=f'{ru}').translate(f'{arg}')

@register.filter(name='translate_en')
def translate_en(arg):
    return GoogleTranslator(source='auto', target=f'{en}').translate(f'{arg}')
