import random

class Card:
    def __init__(self, number):
        self.number = number
        if number > 10:
            self.value = 10
        else:
            self.value = number

def play():
    card1 = deck.pop()
    card2 = deck.pop()

    totalScore = 0

    print('Your hand is: ')
    print(card1.number)
    print(card2.number)

    if card1.number == 1:
        print('Your first card is an ace')
        ace_answer = input('Do you want its value to be 11? Yes/No: ')
        print(ace_answer)
        if ace_answer == "Yes" or ace_answer == "Y":
            totalScore += 11
        else:
            totalScore += 1

    else: 
        totalScore += card1.value        

    if card2.number == 1:
        print('Your second card is an ace')
        ace_answer = input('Do you want its value to be 11? Yes/No: ')
        print(ace_answer)
        if ace_answer == "Yes" or ace_answer == "Y":
            totalScore += 11
        else:
            totalScore += 1

    else: 
        totalScore += card2.value

    print('Your initial score is: ' + str(totalScore))

    if totalScore == 21: 
        print('You won')
        exit()

    hit_answer = input('Do you want to hit or stand? H/S: ')

    while hit_answer == 'H':
        newcard = deck.pop()
        print('Your card is: ' + str(newcard.number))

        if newcard.number == 1:
            print('Your new card is an ace')
            ace_answer = input('Do you want its value to be 11? Yes/No: ')
            print(ace_answer)
            if ace_answer == "Yes" or ace_answer == "Y":
                totalScore += 11
            else:
                totalScore += 1


        else: 
            totalScore += newcard.value
        
        if totalScore > 21:
            print('Your are bust')
            break

        elif totalScore == 21:
            print('You won')

        else:
            print('Your score is: ' + str(totalScore))
            hit_answer = input('Do you want to hit or stand? H/S: ')

    print('Your final score is: ' + str(totalScore))


if __name__ == '__main__':
    deck = [Card(number) for number in range(1, 14) for i in range (1,5)]
    random.shuffle(deck)
    play()