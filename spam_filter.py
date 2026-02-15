# Spam Filter in Python

class SpamFilter:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def is_spam(self, message):
        for rule in self.rules:
            if rule.message_matches(message):
                return True
        return False

class Rule:
    def __init__(self, keyword):
        self.keyword = keyword

    def message_matches(self, message):
        return self.keyword in message.lower()

# Example usage
if __name__ == '__main__':
    spam_filter = SpamFilter()
    spam_filter.add_rule(Rule('spam'))
    spam_filter.add_rule(Rule('buy now'))

    messages = [
        "This is a regular message.",
        "Buy now and save money!",
        "Limited time offer on spam!"
    ]

    for msg in messages:
        if spam_filter.is_spam(msg):
            print(f'Spam detected: {msg}')
        else:
            print(f'Not spam: {msg}')
