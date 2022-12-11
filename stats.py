class Stats():
    '''статистика текуший игры'''

    def __init__(self):
        '''инициализирует статистику'''
        self.reset_stats()
        self.text_record()
        self.text_chet()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        '''статистика изменяющися во время игры'''
        self.guns_left = 2
        self.score = 0

    def text_record(self):
        '''просто слово рекорд'''
        self.textrecord = 'Рекорд:'

    def text_chet(self):
        '''просто слово счет'''
        self.textchet = 'Счет:'
