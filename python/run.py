import requests
import logging

import pandas as pd

from datetime import datetime


logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def get_json_data(url):
    """Get the data in json format"""
    response = requests.get(url)

    return response.json()


def get_answers(data):
    """Return answers in array dict"""

    answers = []
    for item in data.get('items', {}):
        answer = {
            'is_answered': item.get('is_answered'),
            'view_count': item.get('view_count'),
            'question_id': item.get('question_id'),
            'creation_date': datetime.utcfromtimestamp(item.get('creation_date')),
            'closed_date': item.get('closed_date'),
            'answer_count': item.get('answer_count'),
            'score': item.get('score'),
            'last_activity_date': item.get('last_activity_date'),
            'last_edit_date': item.get('last_edit_date'),
            'link': item.get('link'),
            'closed_reason': item.get('closed_reason'),
            'title': item.get('title'),
            'owner_id': item.get('owner', {}).get('user_id')
        }
        answers.append(answer)
    
    return answers


def get_owners(data):
    """Get owners in array dict"""

    owners = []
    for item in data.get('items', {}):

        owners.append(item.get('owner'))

    return owners


def get_count_response_answers(df):
    """Return the number of answered and unanswered answers"""

    counts_answers = df.is_answered.value_counts()

    return counts_answers.loc[True], counts_answers.loc[False]


def get_answer_less_visits(df):
    """Return the number of answered and unanswered answers"""

    answer = df[df.view_count == df.view_count.min()]
    
    return answer


def get_old_answer(df):
    """Return the oldest answer"""

    answer = df[df.creation_date == df.creation_date.min()]

    return answer


def get_newest_answer(df):
    """Return newest answer"""

    answer = df[df.creation_date == df.creation_date.max()]

    return answer


def get_more_reputation_owner(df):
    """Return the owner with more reputation"""

    owner = df[df.reputation == df.reputation.max()]

    return owner.reset_index(drop=True)


if __name__ == '__main__':

    url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
    json_data = get_json_data(url)
    owners = get_owners(json_data)
    answers = get_answers(json_data)
    df_owners = pd.DataFrame.from_dict(owners)
    df_answers = pd.DataFrame.from_dict(answers)

    answered, unanswered = get_count_response_answers(df_answers)
    logger.info(f'Respuestas contestadas: {answered}')
    logger.info(f'Respuestas no contestadas: {unanswered}')
    answer_less_views = get_answer_less_visits(df_answers)
    logger.info(f'La respuesta con el menor numero de visitas es la siguiente:\n')
    print(f'\n{answer_less_views}')
    old_answer = get_old_answer(df_answers)
    logger.info(f'La respuesta mas vieja es la siguiente:\n')
    print(old_answer)
    newest_answer = get_newest_answer(df_answers)
    logger.info(f'La respuesta mas nueva es la siguiente:\n')
    print(newest_answer)
    more_reputation_owner = get_more_reputation_owner(df_owners)
    user_id = more_reputation_owner.user_id.iloc[0]
    logger.info('La respuesta del onwers con mayor reputacion es la siguiente:')
    print(df_answers[df_answers.owner_id == user_id])
