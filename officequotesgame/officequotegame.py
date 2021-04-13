import random


def main():
    print_header()
    questions()


def print_header():
    print('\n Welcome to Who Said It?, Office Edition!\n\n Guess who said the following 10 quotes. Good Luck!\n')


def questions():
    # Office characters and a list of their quotes
    office_cast = {
        'Michael': ['Make friends first, make sales second, make love third. In no particular order.',
                    '''Would I rather be feared or loved? Easy. Both.
                    I want people to be afraid of how much they love me.''',
                    "I'm not superstitious but I am a little stitious."],
        'Dwight': ['Jim told me you could buy gay-dar online.',
                   'Powerpoints are the peacocks of the business world; all show, no meat.',
                   '''I never smile if I can help it. Showing one's teeth is a submission signal in primates.
                   Someone smiles at me, all I see is a chimpanzee begging for its life.'''],
        'Jim': ['''Stanley just drank OJ out of my mug, and didn't seem to realize that it wasn't his hot coffee. 
                    So the question has to be asked, is there no limit to what he won't notice?''',
                'So I either get more involved or I take a sick day. Leaving Dwight in charge. Oh God.',
                'Fact. Bears eat beets. Bears. Beets. Battlestar Galactica.'],
        'Pam': ["There’s a lot of beauty in ordinary things. Isn’t that kind of the point?",
                'Be Strong. Trust Yourself. Love Yourself.',
                "And I feel God in this Chili's Tonight"],
        'Andy': ['My parents used to scramble to find babysitters, so they could take my little brother to do stuff.',
                 'There are two things I am passionate about: recycling and revenge.',
                 '''Tough day. Yes. But I feel good. I put the office in their place, took a bunch of painkillers, 
                 drank a bottle of wine, took my pants off. I just feel good.'''],
        'Stanley': ["Life is short. Drive fast and leave a sexy corpse. That's one of my mottos.",
                    'I took an extra shot of insulin in preparation for this cake today.',
                    'Did I Stutter!?'],
        'Creed': ['''I’ve been involved in a number of cults, both as a leader and a follower. 
                     You have more fun as a follower. But you make more money as a leader.''',
                  'You ever seen a foot with four toes?',
                  'Cool beans, man! I live by the quarry. We should hang out by the quarry and throw things down there.'],
        'Oscar': ['Saddle shoes with denim? I will literally call protective services.',
                  '''I love a good quitting story. It makes me feel like I have control over my own life. 
                  Gives me hope. Maybe I will have one of own someday. [laughs] But I dream... so...''',
                  '''The Dunder Mifflin stock symbol is DMI. Do you know what that stands for? Dummies, morons 
                  and idiots. Because that's what you'd have to be to own it. And, as one of those idiots, 
                  I believe the board owes me answers.'''],
        'Kevin': ['''Mini-cupcakes? As in the mini version of regular cupcakes? Which is already a mini version of cake?
        Honestly, where does it end with you people?''',
                  'You think this is a great party? This cake has vegetables in it',
                  'Why waste time say lot word when few word do trick.'],
        'Angela': ['No, orange is whorish.',
                   'I once reported Oscar to the INS. Turns out he’s clean, but I’m glad I did it.',
                   '''Sometimes, the clothes at GapKids are just too flashy. So I’m forced to go to the American Girl
                      store and order clothes for large colonial dolls.'''],
        'Darryl': ['You need to access your uncrazy side',
                   'In the gang world we use something called Fluffy Fingers.',
                   '''My future isn't going to be determined by seven little white lotto balls. 
                   It's going to be determined by two big black balls.'''],
        'Kelly': ['Who says exactly what they’re thinking? What kind of a game is that?',
                  'Ultimatums are key. Basically nobody does anything for me anymore unless I threaten to kill myself.',
                  'I think sometimes people are really mean to the hot, popular girl.'],
        'Ryan': ['''Maybe we weren't right together, but, it's weird. I'd rather she be alone than with somebody. 
                    Is that love?''',
                 '''Now that I've quit the rat race I realize there's so much more to life than being the 
                    youngest VP in the company's history''',
                 "I don't think Michael's ever done drugs. I don't know if anyone has ever offered him any."],
        'Toby': ['''Michael's like a movie on a plane. It's not great, but it's something to watch. And then
        when it's over, you're like, How much time is left on this flight? Now what?''',
                 '''I know people are only this excited to talk to me because of the trial. But, they talk to 
                    me for a while, and maybe people realize I have something to say. And then one day, 
                    we're just talking.''',
                 '''Every Friday at 4:00 I have a standing appointment with Dwight for him to file a grievance 
                 against Jim. I tell him that I'm sending them to a special file in New York. That box is 
                 the special file in New York.'''],
        'Phyllis': ['You have a lot to learn about this town, Sweetie',
                    'Close your mouth Sweetie, you look like a trout',
                    "I'm glad Michael's getting help. He has a lot of issues, and he's stupid"],
        'Gabe': ['''I wish my gym didn't allow full nudity in the locker room. Okay, seeing these old guys walking around
        naked feels almost passive-aggressive. But I deal with it. 'Cause it's policy. See what I mean?''',
                 '''Apparently, I bear a passing resemblance to Abraham Lincoln. Makes it kind of hard for me to go
        to places like museums, historical monuments, elementary schools... I don't see it.''',
                 '''The beginning here has been a little bit of a fiasco. Either they don't respect me or they 
                 respect me too much. And some of them still think that I'm the I.T. guy. This Cookie Monster thing 
                 is an opportunity to show people that I'm an authority figure.'''],
        'Erin': ['''Whenever I'm sick, it goes away within a few hours. Except that once when I was in the hospital 
                 from age three to six.''',
                 '''Planking is one of those things where, hey, you either get it or you don't... I don't, but 
                 I'm so excited to be a part of it.''',
                 'I would like another alcohol.']
    }
    # Pick an Office character and one of their quotes randomly,
    # randomly select 2 other characters for options, user inputs a choice.
    score = 0
    count = 1
    cast = ['Michael', 'Dwight', 'Jim', 'Pam', 'Andy', 'Stanley', 'Creed', 'Oscar', 'Kevin', 'Angela', 'Darryl',
            'Kelly', 'Ryan', 'Toby', 'Phyllis', 'Gabe', 'Erin']
    while count < 11:
        a = random.choice(list(office_cast.keys()))
        b = random.choice(office_cast[a])
        c = random.choice(cast)
        if c == a:
            c = random.choice(cast)
        d = random.choice(cast)
        while d == a and c:
            d = random.choice(cast)
        choices = [a, c, d]
        choicelow = [a.lower(), c.lower(), d.lower()]
        random.shuffle(choices)
        print('Question', count, ': Who said:\n', b)
        print(*choices, sep=", ")
        ans = input('\n Type Character: ')
        while ans.lower() not in choicelow:
            print('Please pick from the choices.')
            ans = input('\n Type Character: ')
        if ans.lower() == a.lower():
            score += 1
            count += 1
            print('Correct! \n')
        else:
            print('Wrong! It was', a, '!\n')
            count += 1
    print('You got', score, 'out of 10 right! Thanks for playing!')


if __name__ == '__main__':
    main()
