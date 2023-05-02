import re
import long_responses as long

def message_probability(user_message, recgonized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Calculates how many words present in the message
    for word in user_message:
        if word in recgonized_words:
            message_certainty += 1
    # Calculates the percent of recgonized words in a user message
    percentage = float(message_certainty) / float(len(recgonized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Reponses ---------------------------
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'joel'], required_words=['joel', 'love'])
    response('I\'m glad to hear you\'re doing good!', ['i', 'am', 'doing', 'good', 'fine', 'great'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing response system
while True:
    print('Bot: ' + get_response(input("You: ")))