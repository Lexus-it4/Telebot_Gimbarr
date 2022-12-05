from fuzzywuzzy import fuzz


def recognize_question(question, questions):
    """Подбор ответа на вопрос в чате"""
    recognized = {'id': '', 'percent': 0}

    for key, value in questions.items():
        for quest in value:
            percent = fuzz.ratio(question, quest)
            if percent > recognized['percent']:
                recognized['id'] = key
                recognized['percent'] = percent

    if recognized['percent'] > 45:
        return recognized['id']
    else:
        return 0
