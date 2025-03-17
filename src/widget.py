from typing import Union
'''аннотируем тип переменной'''


def mask_account_card(card_info: Union[str]) -> str:
    '''Создаём функцию, принимающая информацию о карте в виде строки'''

    if 'Счет' in card_info:
        first_part_account = '**'
        second_part_account = card_info[-4:]
        '''определяем, какие части аккаунта будут замаскированы'''
        card_info = (f'Счет {first_part_account}{second_part_account}')
        '''складываем части аккаунта вместе'''
        return card_info

    else:
        first_part_card = card_info[:-12]
        second_part_card = card_info[-12:-10]
        third_part_card = '**'
        fourth_part_card = '****'
        fifth_part_card = card_info[-4:]

        '''определяем, какие части карты будут замаскированы'''

        card_info = (f'{first_part_card} {second_part_card}{third_part_card} '
                              f'{fourth_part_card} {fifth_part_card}')

        '''складываем части карты вместе'''

        return card_info


print(mask_account_card('MasterCard 7158300734726758'))