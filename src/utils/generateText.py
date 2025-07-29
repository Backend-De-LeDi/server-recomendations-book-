def generateText(book):
    idioma = "desconocido"
    if book.language == 'es':
        idioma = 'español'
    elif book.language == 'en':
        idioma = 'ingles'

    return '\n'.join([
        book.title,
        book.summary,
        ', '.join(book.subgenre),
        idioma,
        book.synopsis,
        ', '.join(book.theme),
        book.genre
    ])
